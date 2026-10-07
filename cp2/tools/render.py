# Frozen-time camera move renderer: per-pixel depth warp (2 layers) + 3D particles + lens/film.
# Usage: render.py <config.json>
import json, sys, math, os
import numpy as np, cv2

cfg = json.load(open(sys.argv[1]))
rng = np.random.default_rng(cfg.get("seed", 7))
OW, OH = 1080, 1920
FPS = 24
N = int(round(cfg["seconds"] * FPS))
outdir = cfg["out"]; os.makedirs(outdir, exist_ok=True)
only = cfg.get("only_frames")  # list of frame indices for previews

# ---------------- source + analysis
src = cv2.imread(cfg["image"]).astype(np.float32) / 255.0
H, W = src.shape[:2]
disp = np.load(cfg["disp"]); matte = np.load(cfg["matte"])
# light denoise: remove baked grain so it doesn't slide with the image; fresh grain added later
den = cv2.fastNlMeansDenoisingColored((src * 255).astype(np.uint8), None, 4, 4, 5, 15).astype(np.float32) / 255.0

f = cfg.get("focal_px", 2275.0)
cx, cy = W / 2.0, H / 2.0
Zn, Zf = cfg.get("z_near", 1.15), cfg.get("z_far", 7.0)
dsm = cv2.bilateralFilter(disp.astype(np.float32), 9, 0.08, 9)
Z = 1.0 / (dsm * (1 / Zn - 1 / Zf) + 1 / Zf)

# ---------------- layers
a = np.clip((matte - 0.35) / 0.3, 0, 1)
near = ((disp > cfg.get("near_disp", 0.80)) & (np.arange(H)[:, None] > H * 0.62)).astype(np.float32)
alpha = np.maximum(a, cv2.GaussianBlur(near, (0, 0), 2.0))
alpha = cv2.GaussianBlur(alpha, (0, 0), 0.8)

def inpaint(img, mask, scale=0.5, radius=6):
    sm = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    mm = cv2.resize(mask, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
    out = cv2.inpaint((np.clip(sm, 0, 1) * 255).astype(np.uint8), mm, radius, cv2.INPAINT_TELEA)
    out = cv2.resize(out, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255
    out = cv2.GaussianBlur(out, (0, 0), 3)
    m = mask.astype(np.float32)[..., None] / 255.0
    return img * (1 - m) + out * m

hole = (cv2.dilate((alpha > 0.08).astype(np.uint8), np.ones((15, 15), np.uint8)) * 255).astype(np.uint8)
bg = inpaint(den, hole)
# background depth behind fg: fill fg region with surrounding (far) depth
Zbg = Z.copy()
zb = cv2.inpaint(np.clip((Z / 8.0) * 255, 0, 255).astype(np.uint8), hole, 9, cv2.INPAINT_TELEA).astype(np.float32) / 255 * 8.0
Zbg = np.where(hole > 0, np.maximum(zb, Z), Z)
Zbg = cv2.GaussianBlur(Zbg, (0, 0), 4)
# fg colour decontamination: push solid-interior colours outward across the edge band
solid = (alpha > 0.92).astype(np.uint8)
ring = ((cv2.dilate(solid, np.ones((9, 9), np.uint8)) - solid) * 255).astype(np.uint8)
fgc = (np.clip(den, 0, 1) * 255).astype(np.uint8)
fgc = cv2.inpaint(fgc, ring, 4, cv2.INPAINT_TELEA).astype(np.float32) / 255
fgc = np.where(solid[..., None] > 0, den, fgc)
# fg depth extended outward so edge sampling is consistent
Zfg = np.where(alpha > 0.5, Z, 0).astype(np.float32)
k = np.ones((5, 5), np.uint8)
for _ in range(12):
    grown = cv2.dilate(Zfg, k)
    Zfg = np.where(Zfg > 0, Zfg, grown)
Zfg = np.where(Zfg > 0, Zfg, Zbg)

# ---------------- beam light map (where warm light hits the air) for particle illumination
lum = cv2.cvtColor(den, cv2.COLOR_BGR2GRAY)
warm = np.clip(den[..., 2] - den[..., 0], 0, 1)  # R - B
beam = cv2.GaussianBlur(lum * (0.5 + warm), (0, 0), 18)
beam = np.clip((beam - np.percentile(beam, 60)) / (np.percentile(beam, 99.5) - np.percentile(beam, 60)), 0, 1) ** 1.3
light_rgb = np.array(cfg.get("light_bgr", [0.55, 0.80, 1.0]), np.float32)

# ---------------- camera path
def _bez(x, x1, x2):
    # cubic bezier (0,0),(x1,0),(x2,1),(1,1); solve for param by bisection
    lo, hi = np.zeros_like(x), np.ones_like(x)
    for _ in range(30):
        m = (lo + hi) / 2
        bx = 3 * (1 - m) ** 2 * m * x1 + 3 * (1 - m) * m ** 2 * x2 + m ** 3
        lo = np.where(bx < x, m, lo); hi = np.where(bx >= x, m, hi)
    m = (lo + hi) / 2
    return 3 * (1 - m) * m ** 2 + m ** 3

P0 = np.array(cfg["pose_start"], np.float64)   # tx,ty,tz (m), yaw,pitch,roll (deg)
P1 = np.array(cfg["pose_end"], np.float64)
ex1, ex2 = cfg.get("ease", [0.55, 0.18])
over = cfg.get("overshoot", 0.015)
float_amp = np.array(cfg.get("float_amp", [0.0012, 0.0010, 0.0008, 0.03, 0.025, 0.02]))
phases = rng.uniform(0, 2 * np.pi, (6, 3)); freqs = np.array([0.31, 0.57, 0.93])

def pose(i):
    t = i / max(N - 1, 1)
    s = float(_bez(np.array([t]), ex1, ex2)[0])
    s += over * math.sin(math.pi * min(1, max(0, (t - 0.55) / 0.45))) * (1 - t) * 2.2  # tiny settle overshoot
    p = P0 + (P1 - P0) * s
    tt = i / FPS
    noise = np.array([sum(math.sin(2 * math.pi * freqs[j] * tt + phases[k, j]) for j in range(3)) / 3 for k in range(6)])
    return p + noise * float_amp * (0.35 + 0.65 * (1 - t))  # float decays as the operator settles

def rot(yaw, pitch, roll):
    y, p, r = map(math.radians, (yaw, pitch, roll))
    Ry = np.array([[math.cos(y), 0, math.sin(y)], [0, 1, 0], [-math.sin(y), 0, math.cos(y)]])
    Rx = np.array([[1, 0, 0], [0, math.cos(p), -math.sin(p)], [0, math.sin(p), math.cos(p)]])
    Rz = np.array([[math.cos(r), -math.sin(r), 0], [math.sin(r), math.cos(r), 0], [0, 0, 1]])
    return Ry @ Rx @ Rz  # camera-to-world

# output window in source-plane coords
zoom = cfg.get("zoom", 1.22)
c0 = np.array(cfg.get("window_center", [W / 2, H - (H / 2) / zoom - 40]), np.float64)
sc = (W / OW) / zoom
oy, ox = np.mgrid[0:OH, 0:OW].astype(np.float32)
qx = (c0[0] + (ox - OW / 2) * sc).astype(np.float32)
qy = (c0[1] + (oy - OH / 2) * sc).astype(np.float32)

uu, vv = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))

def flow_field(Zmap, T, R):
    X = (uu - cx) * Zmap / f; Y = (vv - cy) * Zmap / f
    Rt = R.T
    Xc, Yc, Zc = X - T[0], Y - T[1], Zmap - T[2]
    Xn = Rt[0, 0] * Xc + Rt[0, 1] * Yc + Rt[0, 2] * Zc
    Yn = Rt[1, 0] * Xc + Rt[1, 1] * Yc + Rt[1, 2] * Zc
    Zn_ = np.maximum(Rt[2, 0] * Xc + Rt[2, 1] * Yc + Rt[2, 2] * Zc, 0.05)
    return (f * Xn / Zn_ + cx - uu).astype(np.float32), (f * Yn / Zn_ + cy - vv).astype(np.float32)

def inverse_map(dx, dy, zoom_breath=1.0):
    bx = (c0[0] + (qx - c0[0]) / zoom_breath).astype(np.float32)
    by = (c0[1] + (qy - c0[1]) / zoom_breath).astype(np.float32)
    px, py = bx.copy(), by.copy()
    for _ in range(5):
        fx = cv2.remap(dx, px, py, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        fy = cv2.remap(dy, px, py, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        px, py = bx - fx, by - fy
    return px, py, bx, by

# ---------------- particles (world space, rest camera coords)
def sample_uv(n, density):
    p = density.ravel() / density.sum()
    idx = rng.choice(p.size, n, p=p)
    v, u = np.unravel_index(idx, density.shape)
    return u + rng.random(n), v + rng.random(n)

pc = cfg.get("particles", {})
dens = cv2.resize(beam, (W // 4, H // 4)) + pc.get("base_density", 0.02)
cloud_c = np.array(pc.get("cloud_center_uv", [380, 1250]), np.float32)
gy, gx = np.mgrid[0:H // 4, 0:W // 4].astype(np.float32) * 4
cloud = np.exp(-(((gx - cloud_c[0]) / pc.get("cloud_rx", 260)) ** 2 + ((gy - cloud_c[1]) / pc.get("cloud_ry", 340)) ** 2))
dens = dens + pc.get("cloud_boost", 1.5) * cloud * (0.3 + cv2.resize(beam, (W // 4, H // 4)))
n_spec = pc.get("specks", 42000)
u_, v_ = sample_uv(n_spec, dens); u_ *= 4; v_ *= 4
u_ = np.clip(u_, 0, W - 1); v_ = np.clip(v_, 0, H - 1)
zs = Z[v_.astype(int), u_.astype(int)]
zmin = pc.get("zmin", 0.55)
r = rng.random(n_spec)
pz = np.exp(np.log(zmin) + r * (np.log(np.minimum(zs * 0.97, 4.0)) - np.log(zmin)))
# concentrate cloud specks at the cloud depth
in_cloud = cloud[(v_ / 4).astype(int).clip(0, H // 4 - 1), (u_ / 4).astype(int).clip(0, W // 4 - 1)] > 0.35
cz = pc.get("cloud_depth", 1.75)
pz = np.where(in_cloud & (rng.random(n_spec) < 0.7), np.minimum(cz + rng.normal(0, 0.18, n_spec), zs * 0.97), pz)
PX = (u_ - cx) * pz / f; PY = (v_ - cy) * pz / f; PZ = pz
lit = beam[v_.astype(int), u_.astype(int)]
lit = np.clip(lit * pc.get("lit_gain", 1.4) + pc.get("ambient", 0.03), 0, 1.5)
bright = np.minimum(rng.lognormal(-0.9, pc.get('bright_sigma', 0.95), n_spec), pc.get('bright_cap', 2.2)) * pc.get("speck_gain", 1.0) * lit
size0 = rng.lognormal(math.log(pc.get("speck_size_m", 0.00055)), 0.45, n_spec)  # metres
vel = rng.normal(0, pc.get("drift_mps", 0.003), (n_spec, 3))
# near bokeh specks (close to lens)
n_bok = pc.get("bokeh", 70)
bu, bv = sample_uv(n_bok, dens); bu *= 4; bv *= 4
bz = rng.uniform(pc.get("bokeh_z", [0.32, 0.7])[0], pc.get("bokeh_z", [0.32, 0.7])[1], n_bok)
BX = (bu - cx) * bz / f; BY = (bv - cy) * bz / f
blit = np.clip(beam[np.clip(bv, 0, H - 1).astype(int), np.clip(bu, 0, W - 1).astype(int)] * 1.6 + 0.05, 0, 1.4)
bbright = rng.lognormal(-0.3, 0.4, n_bok) * pc.get("bokeh_gain", 0.6) * blit
PX = np.concatenate([PX, BX]); PY = np.concatenate([PY, BY]); PZ = np.concatenate([PZ, bz])
bright = np.concatenate([bright, bbright]); size0 = np.concatenate([size0, rng.uniform(0.0012, 0.0025, n_bok)])
vel = np.concatenate([vel, rng.normal(0, 0.002, (n_bok, 3))])

# cloud puffs: fractal-noise sprites in world space
def noise_sprite(sz, seed):
    g = np.random.default_rng(seed)
    acc = np.zeros((sz, sz), np.float32)
    for o, amp in [(4, 1.0), (8, 0.5), (16, 0.28), (32, 0.16), (64, 0.08)]:
        n = g.random((o, o)).astype(np.float32)
        acc += cv2.resize(n, (sz, sz), interpolation=cv2.INTER_CUBIC) * amp
    acc = (acc - acc.min()) / (acc.max() - acc.min())
    yy, xx = np.mgrid[0:sz, 0:sz].astype(np.float32) / sz - 0.5
    fall = np.clip(1 - (np.sqrt(xx ** 2 + yy ** 2) / 0.5), 0, 1) ** 1.6
    a = np.clip((acc * fall - 0.18) / 0.5, 0, 1) ** 1.4
    return a
puffs = []
for j in range(pc.get("puffs", 12)):
    uc = cloud_c[0] + rng.normal(0, pc.get("cloud_rx", 260) * 0.45)
    vc = cloud_c[1] + rng.normal(0, pc.get("cloud_ry", 340) * 0.45)
    zc = cz + rng.normal(0, 0.15)
    l = beam[int(np.clip(vc, 0, H - 1)), int(np.clip(uc, 0, W - 1))]
    puffs.append(dict(X=(uc - cx) * zc / f, Y=(vc - cy) * zc / f, Z=zc, s=rng.uniform(*pc.get('puff_size', [0.07, 0.17])),
                      spr=noise_sprite(256, 100 + j), lit=float(np.clip(l * 1.5 + 0.08, 0, 1.2)),
                      rot=rng.uniform(0, 360), v=rng.normal(0, 0.002, 3)))
puff_gain = pc.get("puff_gain", 0.32)

def coc_px(Zp, zfocus):
    return cfg.get("coc_k", 20.0) * np.abs(1.0 / Zp - 1.0 / zfocus) / sc

def render_particles(T, R, t, zfocus, fg_a_out, fg_z_out, bg_z_out):
    Rt = R.T
    X = PX + vel[:, 0] * t - T[0]; Y = PY + vel[:, 1] * t - T[1]; Zc = PZ + vel[:, 2] * t - T[2]
    Xn = Rt[0, 0] * X + Rt[0, 1] * Y + Rt[0, 2] * Zc
    Yn = Rt[1, 0] * X + Rt[1, 1] * Y + Rt[1, 2] * Zc
    Zz = Rt[2, 0] * X + Rt[2, 1] * Y + Rt[2, 2] * Zc
    ok = Zz > 0.12
    u = f * Xn / np.maximum(Zz, 0.12) + cx; v = f * Yn / np.maximum(Zz, 0.12) + cy
    ox_ = (u - c0[0]) / sc + OW / 2; oy_ = (v - c0[1]) / sc + OH / 2
    ok &= (ox_ > -40) & (ox_ < OW + 40) & (oy_ > -40) & (oy_ < OH + 40)
    ix = np.clip(ox_.astype(int), 0, OW - 1); iy = np.clip(oy_.astype(int), 0, OH - 1)
    # occlusion: hidden behind fg where fg is nearer; hidden behind bg surface
    behind_fg = Zz > fg_z_out[iy, ix] + 0.04
    vis = np.where(behind_fg, 1 - fg_a_out[iy, ix], 1.0) * (Zz < bg_z_out[iy, ix] * 0.995)
    rad = f * size0 / np.maximum(Zz, 0.12) / sc + coc_px(np.maximum(Zz, 0.12), zfocus)
    energy = bright * vis * ok * (f * size0 / np.maximum(Zz, 0.12) / sc + 0.6) ** 2
    acc = np.zeros((OH, OW), np.float32)
    bins = [0, 1.3, 2.2, 3.6, 6, 10, 17, 30, 60]
    for b0, b1 in zip(bins[:-1], bins[1:]):
        m = ok & (rad >= b0) & (rad < b1) & (energy > 1e-5)
        if not m.any():
            continue
        buf = np.zeros((OH, OW), np.float32)
        np.add.at(buf, (iy[m], ix[m]), energy[m])
        rr = (b0 + b1) / 2
        if rr < 1.6:
            buf = cv2.GaussianBlur(buf, (0, 0), 0.7)
        elif rr < 7:
            buf = cv2.GaussianBlur(buf, (0, 0), rr * 0.55)
        else:  # bokeh disc with soft rim
            kk = int(rr * 2) | 1
            yy, xx = np.mgrid[0:kk, 0:kk] - kk // 2
            d = np.sqrt(xx ** 2 + yy ** 2) / (kk / 2)
            disc = np.clip((1 - d) * 6, 0, 1) * (0.75 + 0.25 * d)
            disc = (disc / disc.sum()).astype(np.float32)
            buf = cv2.filter2D(buf, -1, disc)
        acc += buf
    return acc

def render_puffs(T, R, t, zfocus, frame, fg_a_out, fg_z_out):
    Rt = R.T
    for p in puffs:
        X = p["X"] + p["v"][0] * t - T[0]; Y = p["Y"] + p["v"][1] * t - T[1]; Zc = p["Z"] + p["v"][2] * t - T[2]
        Xn = Rt[0, 0] * X + Rt[0, 1] * Y + Rt[0, 2] * Zc
        Yn = Rt[1, 0] * X + Rt[1, 1] * Y + Rt[1, 2] * Zc
        Zz = Rt[2, 0] * X + Rt[2, 1] * Y + Rt[2, 2] * Zc
        if Zz < 0.2:
            continue
        u = f * Xn / Zz + cx; v = f * Yn / Zz + cy
        ox_ = (u - c0[0]) / sc + OW / 2; oy_ = (v - c0[1]) / sc + OH / 2
        size = f * p["s"] / Zz / sc
        if size < 4:
            continue
        spr = p["spr"]
        M = cv2.getRotationMatrix2D((128, 128), p["rot"] + t * 0.6, size / 256)
        M[0, 2] += ox_ - 128; M[1, 2] += oy_ - 128
        a = cv2.warpAffine(spr, M, (OW, OH), flags=cv2.INTER_LINEAR, borderValue=0)
        blur = coc_px(np.array([Zz]), zfocus)[0] * 0.5 + 1.5
        a = cv2.GaussianBlur(a, (0, 0), blur)
        hid = (Zz > fg_z_out + 0.04).astype(np.float32) * fg_a_out
        a = a * (1 - hid) * puff_gain * p["lit"]
        col = light_rgb[None, None, :] * 0.95
        frame = frame * (1 - a[..., None] * 0.25) + col * a[..., None]
    return frame

# ---------------- lens / film post
def post(img, i):
    g = rng  # per-frame
    # bloom
    l = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bt = cfg.get('bloom_thresh', 0.72)
    hi = np.clip((l - bt) / (1 - bt), 0, 1)[..., None] * img
    b1 = cv2.GaussianBlur(hi, (0, 0), 14); b2 = cv2.GaussianBlur(hi, (0, 0), 48)
    bl = cfg.get('bloom', [0.07, 0.05])
    img = img + bl[0] * b1 + bl[1] * b2 * np.array([0.7, 0.85, 1.0], np.float32)
    # barrel distortion + chromatic aberration in one remap per channel
    yy, xx = np.mgrid[0:OH, 0:OW].astype(np.float32)
    nx = (xx - OW / 2) / (OH / 2); ny = (yy - OH / 2) / (OH / 2)
    r2 = nx ** 2 + ny ** 2
    out = np.empty_like(img)
    for ch, ca in zip(range(3), (0.9988, 1.0, 1.0013)):  # B,G,R
        k = 1 + cfg.get("barrel", 0.012) * r2
        mx = (nx * k * ca) * (OH / 2) + OW / 2 + weave[i][0]
        my = (ny * k * ca) * (OH / 2) + OH / 2 + weave[i][1]
        out[..., ch] = cv2.remap(img[..., ch], mx.astype(np.float32), my.astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    img = out
    # vignette
    img = img * (1 - 0.32 * np.clip(r2 / 1.3, 0, 1) ** 1.3)[..., None]
    # grain: luminance-weighted, slightly clumped, fresh every frame
    l = cv2.cvtColor(np.clip(img, 0, 1), cv2.COLOR_BGR2GRAY)
    gn = cv2.GaussianBlur(g.normal(0, 1, (OH, OW)).astype(np.float32), (0, 0), 0.65)
    gw = cfg.get('grain', [0.012, 0.028])
    w = gw[0] + gw[1] * (l * (1 - l)) * 4
    img = img + (gn * w)[..., None] * np.array([1.0, 0.97, 1.03], np.float32)
    return np.clip(img, 0, 1)

wv = np.cumsum(rng.normal(0, 0.12, (N, 2)), axis=0); wv -= cv2.GaussianBlur(wv, (1, 31), 8)
weave = wv * 0.8

# ---------------- focus schedule
def focus_at(i):
    fz = cfg.get("focus", [[0, 1.75], [1, 1.75]])
    t = i / max(N - 1, 1)
    ts = [p[0] for p in fz]; zs = [p[1] for p in fz]
    # ease between keys in diopters
    for k in range(len(ts) - 1):
        if ts[k] <= t <= ts[k + 1]:
            s = float(_bez(np.array([(t - ts[k]) / max(ts[k + 1] - ts[k], 1e-6)]), 0.5, 0.5)[0])
            d = (1 / zs[k]) + ((1 / zs[k + 1]) - (1 / zs[k])) * s
            return 1 / d
    return zs[-1] if t > ts[-1] else zs[0]

plate_focus = cfg.get("plate_focus", 1.75)
frames = only if only else range(N)
cov_min = 1.0
for i in frames:
    p = pose(i); T = p[:3]; R = rot(*p[3:])
    zf_ = focus_at(i)
    breath = 1.0 + cfg.get("breathing", 0.012) * (1 / zf_ - 1 / plate_focus) / (1 / 0.6 - 1 / plate_focus + 1e-6)
    # background layer
    dx, dy = flow_field(Zbg, T, R)
    px, py, _, _ = inverse_map(dx, dy, breath)
    bgw = cv2.remap(bg, px, py, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    bgz = cv2.remap(Zbg, px, py, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    valid = ((px >= 0) & (px < W - 1) & (py >= 0) & (py < H - 1)).mean()
    cov_min = min(cov_min, valid)
    # foreground layer
    dx, dy = flow_field(Zfg, T, R)
    px, py, _, _ = inverse_map(dx, dy, breath)
    fgw = cv2.remap(fgc, px, py, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    faw = cv2.remap(alpha, px, py, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    fgz = cv2.remap(Zfg, px, py, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    # defocus of the plates when focus departs from the plate's baked focus
    pb_fg = coc_px(np.array([1.75]), zf_)[0] - coc_px(np.array([1.75]), plate_focus)[0]
    if pb_fg > 0.6:
        fgw = cv2.GaussianBlur(fgw, (0, 0), pb_fg * 0.5); faw = cv2.GaussianBlur(faw, (0, 0), pb_fg * 0.5)
        bgw = cv2.GaussianBlur(bgw, (0, 0), pb_fg * 0.35)
    frame = bgw * (1 - faw[..., None]) + fgw * faw[..., None]
    t = i / FPS
    frame = render_puffs(T, R, t, zf_, frame, faw, fgz)
    parts = render_particles(T, R, t, zf_, faw, fgz, bgz)
    frame = frame + parts[..., None] * light_rgb[None, None, :] * cfg.get("particle_gain", 2.6)
    frame = post(frame, i)
    cv2.imwrite(f"{outdir}/f_{i:04d}.png", (frame * 255).astype(np.uint8))
print("done", len(list(frames)), "frames; min coverage", round(float(cov_min), 4))
