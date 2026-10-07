# Depth + subject matte for a still. Usage: analyze.py <image> <outprefix> <modeldir>
import sys, numpy as np, cv2, onnxruntime as ort
img_path, out, mdir = sys.argv[1:4]
bgr = cv2.imread(img_path); H, W = bgr.shape[:2]
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0

# --- depth (Depth Anything V2 small): relative inverse depth, larger = nearer
dw, dh = 518, 924
x = cv2.resize(rgb, (dw, dh), interpolation=cv2.INTER_CUBIC)
x = (x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
x = x.transpose(2, 0, 1)[None].astype(np.float32)
s = ort.InferenceSession(f"{mdir}/depth_small.onnx", providers=["CPUExecutionProvider"])
d = s.run(None, {s.get_inputs()[0].name: x})[0].squeeze()
d = cv2.resize(d, (W, H), interpolation=cv2.INTER_CUBIC)
d = (d - d.min()) / (d.max() - d.min())
np.save(f"{out}_disp.npy", d.astype(np.float32))
cv2.imwrite(f"{out}_disp.png", (d * 255).astype(np.uint8))

# --- subject matte (RMBG-1.4)
x = cv2.resize(rgb, (1024, 1024), interpolation=cv2.INTER_LINEAR)
x = ((x - 0.5) / 1.0).transpose(2, 0, 1)[None].astype(np.float32)
s = ort.InferenceSession(f"{mdir}/rmbg.onnx", providers=["CPUExecutionProvider"])
m = s.run(None, {s.get_inputs()[0].name: x})[0].squeeze()
m = cv2.resize(m, (W, H), interpolation=cv2.INTER_LINEAR)
m = (m - m.min()) / (m.max() - m.min())
np.save(f"{out}_matte.npy", m.astype(np.float32))
cv2.imwrite(f"{out}_matte.png", (m * 255).astype(np.uint8))
print("ok", W, H, "disp range", float(d.min()), float(d.max()))
