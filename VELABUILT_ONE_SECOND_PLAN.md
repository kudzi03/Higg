# VELABUILT — "ONE SECOND"
### Flagship vertical brand film · 36s · 9:16 · Pre-production bible v1
*Status: PLAN ONLY. Zero credits spent. Awaiting approval.*

---

## 0. Account audit (live, read from the connected Higgsfield account on 2026-10-07)

**Balance: 84.88 credits · Plan: Basic.** All costs below are exact preflight quotes from the account (`get_cost`, no jobs submitted), 9:16, audio off.

### Image models (per image)
| Model | Cost | Use in this film |
|---|---|---|
| **Soul Cinema** (`soul_cinematic`, 2K) | **0.12** | Primary look-dev and hero stills. Cinema-grade lighting. Nearly free. |
| Soul 2.0 / Soul Location (2K) | 0.12 | Backup for people / environment plates |
| GPT Image 2.5 (2K, medium) | 1.0 | Backup precise generation |
| Nano Banana 2 (1K / 2K) | 1.5 / 2.0 | — |
| **Nano Banana Pro** (2K) | **2.0** | Precise reference edits only (same character, new lighting; end frames) |
| Cinema Studio Image 2.5 (2K) | 2.0 | Not needed (Soul Cinema covers it) |
| Seedream 5.0 Pro (2K) | 2.5 | Not needed |
| Image Decompose (layers) | 2.0 | Fallback only, if local layer separation fails |
| Background Remover | 1.0 | Fallback only |

### Video models
| Model | Quote | Per second | Verdict |
|---|---|---|---|
| **Kling 3.0 std** (3–15s, start + end frame) | 3s = **4.5** · 5s = 7.5 | 1.5 | Workhorse. Durations can be trimmed to the second. |
| **Kling 3.0 pro** | 4s = 7.0 · 5s = **8.75** | 1.75 | Hero shot only |
| Cinema Studio Video v2 std / pro (speed-ramp control) | 5s = 5 · 4s pro = 6 | 1.0 / 1.5 | Cheaper alternative with a built-in `slowmo` / `speedup` ramp |
| Hailuo 2.3 Fast (6s 768p / 1080p) | 4 / 7 | 0.67 | Cheapest usable; good for a soft-focus background plate |
| Kling 2.6 / Grok 1.5 Lite (5s) | 5 | 1.0 | Budget backups |
| Wan 3.0 720p | 8.75 | — | No advantage |
| Kling 3.0 Turbo 720p / 1080p | 7.5 / 10 | — | No advantage over std |
| Seedance 2.0 / 2.5 · Cinema Studio 3.0 · Happy Horse | 22.5 / 35 / 25 / 12.5 | — | **Excluded.** One clip would eat a third of the budget. |
| Veo 3.1 Lite (4s) | 6 | 1.5 | Backup |
| Genjutsu (motion transfer / object swap) | needs a source video to quote | — | **Not in this cut.** Phase-2 tool (see §8). |

### Audio
| Model | Cost | Note |
|---|---|---|
| Seed Audio TTS | 0.3 per line | Cheap enough for temp VO and as a final fallback |
| Eleven v4 (via Higgsfield) | quote at use | Final-voice option |
| Music / SFX | — | **Higgsfield has no general music or SFX model** (Sonilo / Mirelo are game-pipeline only). Music and SFX come from outside (see §5). |

### Free resources found
- **This container**: ffmpeg 6.1, ImageMagick, Python (PIL/numpy), Node 22 and headless Chromium. Compositing, 2.5D parallax, particle simulations, typography, the phone UI, the grade, sound editing and the mix can all be done here at zero credits.
- **Higgsfield sandbox** (`sandbox_exec`): ffmpeg, sox and Playwright. Free.
- **Higgsfield's "Bullet time" and "Frozen in motion" presets**: watch the free previews as proof of how the models handle frozen time. Don't run the preset chains: they cost unknown credits and produce a template look.

### Unknowns to confirm before the first spend
1. Whether Basic blocks any model at submit time (a cost quote doesn't prove access). I'll test access on the first cheap image.
2. Commercial-use terms on Basic. Reviews say paid tiers include commercial rights; confirm on the account's terms page.
3. Kling std output resolution (expected 720p; pro expected 1080p).

---

## 1. The concept: "ONE SECOND"

**Every small business gets one second.** One second for a stranger walking past, or scrolling past, to decide whether you're worth remembering.

The film stops time inside that second. At **06:47:12** one morning, in one city, four small businesses are frozen mid-moment: a baker, a skincare founder, a steel fabricator and a family hotelier. Each is lit and framed like a flagship luxury campaign. The camera travels through the frozen city from one business to the next, each world turning into the next through matching shapes and materials: a glaze drop, a serum drop, a molten spark, a city light, a coffee pour, a glaze pour.

At 06:47:13 time resumes. Then the camera pulls back and the big campaign we've been watching turns out to be **an ad on a customer's phone, standing in line at a small, ordinary bakery.** The owner behind the counter is the woman from the ad.

**Why it's strong**
- **The idea is the offer.** "Your one second" is the first impression a business makes, and that's what VelaBuilt sells. The film acts out the claim instead of stating it.
- **It's a story.** It has a premise (one second), rising action (the frozen city), a release (time resumes), a reveal (the phone) and a punchline (the owner's line). It isn't a montage.
- **The reveal works on the target viewer.** The audience believes they're watching a big-budget film, then finds out it belongs to a corner bakery. That flip is what makes a business owner think *"I want my company to look like THAT."*
- **The constraint becomes the style.** Frozen time is built from stills, which are cheap (0.12 credits) and where AI is at its best. AI's weak points (liquid physics, hands in motion) mostly disappear inside a frozen frame, where odd physics reads as style. **The concept was chosen because it is both the best idea and the most budget-proof one.**
- **It rewards a second viewing.** Every timestamp reads 06:47:12, so the whole film is one second long. Viewers who notice tend to replay and share it.
- **It sells the result, not the tools.** It never mentions AI, models or prompts. VelaBuilt appears only as the company that made "that."

**Brand line (end card):** *Your customers never see your budget. / They see your one second.* → **VELABUILT** — *Big-brand campaigns for businesses of every size.*

Alternative end lines for A/B cutdowns: *"Make your one second unforgettable."* · *"Look like the brand you already are."* · *"Your business deserves to look bigger than it is."*

---

## 2. Treatment (36 seconds)

Black. One clock tick, dry and close. Then the tick stretches into a long, glassy shimmer, and everything stops.

A single drop of amber glaze hangs in darkness, lit from the side like jewellery. Flour dust hangs around it, motionless. Timecode in the corner: **06:47:12.** A woman's voice, close and unhurried: *"Every morning, I get one second."*

The camera pushes into the drop. Inside its curved surface is another world, upside down. We pass through the surface and the image rights itself. We're in a small skincare studio: a pipette, a suspended drop of serum, caustic light on stone, the founder out of focus with her eyes closed. **06:47:12 — Ivy Skin Studio.** A second voice: *"One second to be noticed."*

We follow the serum drop down. A white flash, two frames long, and the drop is now molten: an orange spark suspended inside a galaxy of sparks around a welder's helmet. A small steel workshop, blue dawn coming through the roll-up door. **06:47:12 — Kade Steelworks.** A gravelly voice: *"To be trusted."*

The sparks blur into bokeh, and the bokeh becomes the city's lights, still on at dawn below a small hotel's rooftop terrace. The owner, in his sixties, is pouring the first coffee of the day. The stream hangs in the air between copper pot and cup, and steam hangs above it. **06:47:12 — The Lantern House.** *"To be remembered."*

We tilt down the coffee stream and it becomes a ribbon of glaze running over a tray of croissants. Wide: the bakery we started in, every element frozen. The baker mid-motion, a cloud of flour caught in a shaft of morning light, the street outside still blue. **06:47:12 — Sona Bakery.**

Half a second of complete silence.

**TICK. 06:47:13.**

Time resumes. The flour cloud rolls through the light, glaze drips, the oven fan roars back in, the door bell rings, and the music hits. The baker sets the ladle down and turns toward the door.

The image shrinks into a phone screen. Same shot, now playing small and tinny in a customer's hand, standing in line at an ordinary bakery at eleven in the morning: mixed fluorescent and daylight, an espresso machine hissing, a chalkboard. Behind the counter, out of focus, the same woman is boxing pastries.

Customer, half-laughing: *"Wait — this is you?"*
The baker, without looking up: *"Every morning."*

Super: **Your customers never see your budget.**
Cut to the warm black of the opening drop: **They see your one second.**
**VELABUILT.** *Big-brand campaigns for businesses of every size.*
One final tick. Silence.

---

## 3. Second-by-second shot list
24 fps · 1080×1920 master · score at **60 BPM, so one beat equals one second.** Every major cut lands on a whole second; the unfreeze hits exactly at 0:22.00.

| # | Time | Shot | Frame / camera | Text on screen | Voice | Build method |
|---|---|---|---|---|---|---|
| **S01** | 0:00–0:04 | **Macro glaze drop (frozen).** Amber drop hanging from the out-of-focus curl of a croissant; flour particles suspended; warm black. | 100mm macro look. Slow push 100→118% plus slight lateral drift; the foreground flour layer moves 1.6× faster (parallax). Focus breathes slightly. | 0:00.5 `06:47:12` | 0:01.0 VO1 | Still **H2** + 2.5D parallax + local particle simulation |
| T1 | 0:03.0–0:04.0 | **Into the drop.** The skincare world is visible inverted inside the drop; we push through and the image rotates upright. | Ease-in zoom to 800% into the drop | — | — | Compositing (see §6) |
| **S02** | 0:04–0:08 | **Skincare (frozen).** Pipette from top of frame (only thumb and index visible), serum drop suspended over an amber unlabeled bottle; caustics on travertine; founder's face soft in the background. | 85mm. Lateral slide L→R with 2° roll; three parallax layers. | 0:04.5 `06:47:12 · Ivy Skin Studio` | 0:05.0 VO2 | Still **H3**, 2.5D (or a 3s Kling "frozen drift" if the test passes) |
| T2 | 0:07.4–0:08.0 | **Serum → molten spark.** Tilt down the drop's path; the drop heats amber→white-orange; 2-frame white flash; cut to a spark at the same screen position and scale. | Matched position at x 50%, y 46% | — | — | Compositing |
| **S03** | 0:08–0:13 | **Steelworks (frozen).** Welder kneeling at a steel beam, auto-darkening helmet (face hidden), a fan of sparks frozen around them; blue dawn through the roll-up door, orange spark light. | 35mm. Starts close on one spark, pulls back and arcs 8° left. | 0:08.5 `06:47:12 · Kade Steelworks` | 0:09.5 VO3 | Still **H4** + **Kling 3.0 std 3s frozen-orbit test (V3)**; fallback is 2.5D with a spark simulation |
| T3 | 0:12.0–0:13.0 | **Sparks → city lights.** Sparks defocus into bokeh discs; the discs slide into the hotel's city lights; rack focus. | Blur 0→60px, then 60→0 on the next shot | — | — | Compositing + procedural bokeh |
| **S04** | 0:13–0:18 | **Hotel rooftop (frozen).** Blue-hour city lights below; owner (60s, linen shirt) pouring from a copper pot; the coffee stream hangs mid-air with steam above it; one white cup on zinc. | 50mm. Crane down from the city to the pour. | 0:13.5 `06:47:12 · The Lantern House` | 0:15.0 VO4 | Still **H5**, 2.5D (or a Kling 3s drift if V3 passes) |
| T4 | 0:17.4–0:18.0 | **Coffee stream → glaze stream.** Whip-tilt down the stream with directional motion blur; the stream is in the same position and direction across the cut. | Stream locked at x 52% | — | — | Compositing |
| **S05** | 0:18–0:22 | **Bakery wide (frozen hero).** Baker (40s, dark apron, flour on her forearms) holding a glaze ladle over a tray; flour cloud suspended in a shaft of golden window light; street outside still blue. | 40mm. Slow push that **ends exactly at the native framing of H1** so it hands off seamlessly to the video. | 0:18.5 `06:47:12 · Sona Bakery` | — | Still **H1**, 2.5D |
| — | 0:21.5–0:22.0 | **Silence.** | Push stops | — | — | — |
| **S06** | 0:22–0:26 | **UNFREEZE (hero).** Time resumes: flour rolls through the light, glaze drips, she sets the ladle down and turns her head toward the door bell. | Locked camera, slight drift | 0:22.0 `06:47:13` | — | **V1: Kling 3.0 pro 5s from H1** (H1 is frame 0, so the cut can't jump) |
| T5 | 0:25.5–0:26.5 | **Pull-out into the phone.** S06 shrinks into the phone screen with glass reflection, a slight screen grid and a generic vertical-video UI. | Scale 100→22% with motion blur | — | — | Compositing |
| **S07** | 0:26–0:31 | **Reveal.** Over-the-shoulder: customer's hand holding the phone in the foreground (screen playing S06); the real bakery at 11am behind, ordinary and a little cluttered; baker soft in the background, boxing pastries. | Phone-height handheld (synthetic shake applied to the whole composite) | 0:29.8 `Your customers never see your budget.` | 0:27.2 D1 · 0:28.8 D2 | **H6** (reference edit of H1) → **V2: Kling 3.0 std 4s background plate**; still foreground phone layer; screen insert |
| **S08** | 0:31–0:36 | **End card.** Warm black with the dimmed macro drop (H2) back for a callback. | Locked | 0:31.2 `They see your one second.` · 0:33.0 **VELABUILT** · 0:33.6 `Big-brand campaigns for businesses of every size.` · 0:34.2 `velabuilt.com` | — | Motion design (free) |

---

## 4. Exact voiceover, dialogue and copy

**Voiceover: four owners finishing one sentence (four different real voices)**
| ID | Time | Speaker | Line | Direction |
|---|---|---|---|---|
| VO1 | 0:01.0–0:02.8 | Baker (40s, warm, slightly tired, a little amused) | "Every morning, I get one second." | Close mic, almost to herself. No performance, no "ad voice." |
| VO2 | 0:05.0–0:06.4 | Skincare founder (late 20s, precise) | "One second to be noticed." | Soft, deliberate, slight smile. |
| VO3 | 0:09.5–0:10.4 | Welder (50s, low, gravel) | "To be trusted." | Flat and plain. Two beats of pause before "trusted." |
| VO4 | 0:15.0–0:16.2 | Hotel owner (60s, gentle, a light accent is welcome) | "To be remembered." | Warm, nostalgic, unhurried. |

**Dialogue (S07). No lips are on screen, so no lip-sync is needed.**
| ID | Time | Speaker | Line | Direction |
|---|---|---|---|---|
| D1 | 0:27.2–0:28.2 | Customer (off-axis, back of head only) | "Wait — this is you?" | Real surprise, half a laugh. |
| D2 | 0:28.8–0:29.6 | Baker (soft focus, looking down at the box) | "Every morning." | Quiet pride. Don't play it as a punchline. |

**Copy**
- Timestamps: `06:47:12` (×5), then `06:47:13`
- Business names (fictional; checked against real-brand conflicts before lock): Sona Bakery · Ivy Skin Studio · Kade Steelworks · The Lantern House
- Super: **Your customers never see your budget.**
- End card: **They see your one second.** / **VELABUILT** / *Big-brand campaigns for businesses of every size.* / velabuilt.com *(confirm domain)*

**Typography:** Timestamps and business names in a monospace (IBM Plex Mono, 22px, +80 tracking, 75% white), lower left inside the safe area. Headlines in a refined serif (Instrument Serif, 64–72px, centered). Each headline settles letter by letter from a 6px drift with motion blur, as if it froze in mid-air like everything else. Wordmark: VelaBuilt's own logo if one exists; otherwise a wide-tracked grotesk (Inter Tight SemiBold, +200 tracking). Safe area: keep text out of the top 220px, the bottom 420px and the right 160px of the 1080×1920 frame, so platform UI doesn't cover it.

---

## 5. Sound design and music (designed with the picture)

**Rules:** (1) **Frozen means near-silent and huge**: sub drone, room tone removed, crystalline harmonics. **Live means a rush of real sound.** The alternation is the film's sonic structure. (2) **The tick is the motif**: one tick opens the film, one tick unfreezes it, one tick closes it. (3) **60 BPM**: one beat per second, felt more than heard.

| Time | Sound design | Music |
|---|---|---|
| 0:00 | Single dry clock tick, close-mic. Time-stretched ×40 into a reverberant glassy shimmer (the "freeze"). Sub drone at 32 Hz fades in. | — |
| 0:01–0:03 | Bakery frozen tone: slowed oven hum, crust crackle stretched into grain. VO1 dry and intimate, no reverb. | Felt heartbeat pulse at 60 BPM, sub only |
| 0:03–0:04 (T1) | Underwater "whoomp" muffle into a glassy open. | — |
| 0:04–0:08 | Wet-finger-on-glass harmonic (E). Drop shimmer. VO2. | 4-note felt-piano motif enters (E–G#–B–C#), very soft |
| 0:07.4–0:08 (T2) | Glass ping pitch-dropped into a metallic "shhk"; 2-frame flash = transient snap. | Motif holds |
| 0:08–0:13 | Slowed metal ring (an anvil hit stretched to 4s); sparks as a granular crystalline glitter, panned wide. VO3. | Low strings (cello pedal) enter |
| 0:12–0:13 (T3) | Spark crackle filter-swept up into wind. | — |
| 0:13–0:18 | Dawn city: distant traffic hush, wind across the terrace, one bird held as a sustained note (frozen). VO4. | Motif plus strings; slow swell begins (Shepard-style rising tension) |
| 0:17.4–0:18 (T4) | Reverse pour plus whoosh. | — |
| 0:18–0:21.5 | All frozen tones layered; the drone rises. | Full swell, building |
| **0:21.5–0:22.0** | **Hard silence**: everything cuts, including the reverb tails. | **Silence** |
| **0:22.0** | **TICK** (sharp, loud). Then the real world floods in at once: oven fan, tray clink, flour whoosh, door bell, street outside. | **Music hit**: full chord (piano + strings + low boom), the motif at full voice |
| 0:25.5–0:26.5 (T5) | The music gets **band-limited to phone-speaker quality** (HPF 350 Hz, LPF 4.5 kHz, slight distortion) as the picture shrinks into the phone. | The same cue, now diegetic, playing from the phone |
| 0:26–0:31 | Real bakery room: espresso hiss, cup clink, low murmur, paper bag. D1 and D2 dry, natural, slight room. | Phone-speaker music under the dialogue |
| 0:31–0:35.5 | Room tone fades out. | Music returns full-range for the resolving chord; a single low piano note on the wordmark |
| 0:35.5 | **Final tick.** Short tail. Silence. | — |

**Sources:**
- **SFX**: CC0 libraries (Freesound CC0 filter, Pixabay SFX). Ticks, stretches, risers, drones and glass harmonics can be synthesized locally (sox/numpy). 0 credits.
- **Music**: Higgsfield has no music model. Options, in order: (a) a licensed library track (Artlist, Musicbed or Epidemic) in the "minimal piano + strings, 60 BPM" brief, re-edited to the cue sheet above; (b) **ElevenLabs Music** through your ElevenLabs connector (it's in this session; it uses ElevenLabs credits, not Higgsfield credits); (c) a commissioned composer for the flagship version. The cue sheet above is the brief for any of them.
- **Voices**: **Recommended: record real people** (friends or actual small-business owners) on a phone in a closet or a car. Free, and more authentic than any synthetic voice, which suits a film about real owners. Fallback: Seed Audio or Eleven v4 through Higgsfield (0.3 credits per line on Seed Audio). Temp VO for the animatic: Seed Audio, about 2 credits total.
- **Mix**: −14 LUFS integrated for social, true peak −1 dBTP. The 0:22 hit is the loudest moment.

---

## 6. Camera, lighting, production design and performance

**Visual language:** single-source chiaroscuro for the frozen worlds, so each one feels like a luxury still life. **Amber is the thread through the film**: glaze, serum, molten steel, city sodium lights, coffee and morning sun are all the same warm hue against cool blue-dawn fill. The reveal breaks that palette on purpose: flat, mixed fluorescent-daylight, slightly green, handheld. Lens look: modern anamorphic-ish character (soft oval bokeh, gentle blue streak flares added in comp), fine 35mm grain throughout, so stills and video read as one medium.

| World | Light | Production design | Performance |
|---|---|---|---|
| Macro drop (S01) | One hard warm key from camera left (3200K) + a cool rim from behind. Background falls to black. | Laminated croissant curl, deep-amber glaze, flour as stars. | — |
| Skincare (S02) | Soft overhead box + a caustic projector pattern (rippled water light) across travertine. 4500K. | Amber glass dropper bottle, **no label** (it can be added for a real client later), dried botanicals, stone. Small studio, styled minimal. | Founder: eyes closed, chin slightly raised. Calm, private, mid-ritual. |
| Steel (S03) | Spark light (warm orange, from the work point) vs. cold blue dawn through the roll-up door. Haze in the air. | Real small shop: steel beam on trestles, clamps, a grinder, a worn workbench. | Welder: kneeling, body angled into the work, helmet down. Grounded, physical. |
| Hotel (S04) | Blue hour: cool ambient + warm practical string lights + the steam backlit. | Rooftop terrace with plants, one zinc table, a copper pot, one white cup, the city below. | Owner: half-smile, eyes on the cup. Hospitality as care. |
| Bakery hero (S05/S06) | A hard golden sun shaft through the shop window (key) cutting through the flour cloud; cool blue street through the glass. | Deck oven, wooden bench, croissant tray, a glaze ladle, a brass door bell. | Baker: concentrated, almost tender; in V1, a small exhale, ladle down, head turns toward the bell. **One action only.** |
| Reveal (S07) | Ordinary: overhead fluorescent + window daylight, low contrast, slightly green. | Same bakery, now busy and real: paper bags, chalkboard (blurred, no legible text), tip jar, a queue of two. | Customer: casual, amused. Baker: soft focus, boxing pastries, small smile on "Every morning." |

### Transitions (all built in compositing: 0 credits, fully controllable, no rerolls)
| T | Effect | Technique |
|---|---|---|
| **T1 Drop → skincare** | Push into the drop; the next world is visible upside down inside it (real refraction physics), then rights itself as we pass through. | H3 is barrel-distorted, rotated 180° and masked into H2's drop alpha (ImageMagick `-distort Barrel` + mask). An eased zoom to 800% into the drop, then a crossfade at maximum zoom while H3 de-distorts and rotates upright over 10 frames. Chromatic fringe on the drop edge. |
| **T2 Serum → spark** | The drop heats to molten; flash; it's now a spark. | The drop is zoomed and curve-shifted amber → white-orange, bloom glow added; a 2-frame white flash; hard cut to H4 at the same screen position and scale, then pull out. **H4 is composed so one spark sits at the drop's coordinates** (x 50%, y 46%); comp scale/offset handles small errors. |
| **T3 Sparks → city lights** | Sparks melt into bokeh, which becomes the city. | Gaussian defocus ramp on S03; procedural bokeh discs (Python) spawned at the brightest-spark positions and animated to the city-light positions in H5; S04 starts defocused and racks to sharp. |
| **T4 Coffee → glaze** | One continuous falling stream across two worlds. | Both stills are composed with the stream at x 52%, falling top to bottom; whip-tilt down with directional motion blur (12 frames); the cut sits inside the blur. |
| **T0/Unfreeze** | Frozen still comes to life without a jump. | V1 is generated **from H1 as its first frame**, and S05's 2.5D move ends at H1's native framing, so frame 0 of the video is the exact last frame of the still. Speed ramp: the first 8 frames of V1 are slowed to ~30% (frame-blended), then real time. Optionally Higgsfield `fps_boost` for a cleaner ramp. |
| **T5 Into the phone** | The hero shot becomes an ad on a phone. | S06 scales down onto the corner-pinned screen in S07, with motion blur, a glass reflection layer, a faint pixel grid and a **generic** vertical-video UI (no real platform branding). Audio band-limiting is applied over the same frames. |

**2.5D "frozen camera" method (S01–S05):** layer separation into foreground, subject and background, done locally (segmentation + hand-painted masks; Higgsfield Image Decompose at 2 credits as a fallback). Clean background plates via local inpainting (OpenCV Telea; parallax moves are small). Depth-correct parallax, micro camera roll, focus breathing, slow particle drift (flour, steam and sparks crawling at about 1% speed, as if shot at 10,000 fps), lens bloom, grain. **That's the difference between a cinematic frozen-time move and a cheap "Ken Burns" pan, and the first checkpoint tests exactly this before any video credits are spent.**

---

## 7. Higgsfield model per asset, and why

| Asset | Model | Why |
|---|---|---|
| H1–H5 hero stills (look-dev and finals) | **Soul Cinema 2K** (0.12) | Cinema-grade lighting and composition at almost no cost: about 16 attempts for the price of one Nano Banana Pro image. |
| H2 macro drop (needs to match H1's palette and props) | Soul Cinema, with H1 as the image reference | Keeps the glaze, croissant and light consistent with H1 |
| H6 reveal plate (same baker, ordinary lighting) | **Nano Banana Pro** (2.0), H1 as reference | The best at keeping identity and wardrobe while changing lighting and setting. Worth 2 credits here, and only here. |
| End frame for V1 (only if a reroll is needed) | Nano Banana Pro edit of H1 | Pinning the end pose turns a gamble into a controlled interpolation |
| **V1 hero unfreeze** | **Kling 3.0 pro, 5s, from H1** (8.75) | Best human motion and particle physics per credit in the catalog, at 1080p. This is the most important shot. |
| V2 reveal background plate | **Kling 3.0 std, 4s** (6.0); fallback Hailuo 2.3 Fast (4.0) | The plate is soft focus behind a foreground layer, so the cheap tier is enough |
| V3 steel frozen-orbit test | **Kling 3.0 std, 3s** (4.5) | Cheapest real-camera test of "frozen time" on the most forgiving shot (helmet, no face, sparks) |
| V4/V5 skincare and hotel frozen drift (optional) | Kling 3.0 std, 3s each (4.5) | Only if V3 proves frozen time beats 2.5D |
| Temp VO | Seed Audio (0.3 per line) | Lets the animatic be judged with real timing |
| Upscale | Local first (Lanczos + light sharpen + grain); Bytedance Video Upscale only if V2 needs it (quote at use) | V1 is already 1080p; grain hides the rest |
| **Not used** | Seedance 2.x, Cinema Studio 3.0/4.0, Veo 3.1, Marketing Studio, Ads Studio, Soul ID training, lip-sync, Genjutsu | Too expensive for the gain, built for templates, or solving problems this design doesn't have (no lip-sync, no recurring characters) |

---

## 8. Done in motion design, compositing and editing instead of generation
Every transition (T1–T5) · all 2.5D camera moves · flour, spark, steam and bokeh particle simulations · all typography and timestamps · the phone UI and screen insert · the handheld shake on the reveal · speed ramps · the white flash · the lens flares, bloom, chromatic fringe and grain · the color grade (one LUT across all shots) · the end card · all sound design, edit and mix · the 4:5 and 1:1 derivative crops.

**Genjutsu, phase 2 only.** Once the flagship exists, Genjutsu Object Swap on V2 (the reveal) can produce vertical-specific versions (a barbershop, a florist) from the same motion without re-shooting, which makes it the right tool for scaling the campaign. It doesn't help this cut.

---

## 9. Asset dependency map

```
                         ┌──────────────────────────┐
                         │ H1  Bakery hero still    │  ← ANCHOR. Made first. Everything references it.
                         │ (Soul Cinema 2K)         │
                         └──┬──────┬──────┬─────────┘
          style/palette ref │      │      │ identity ref
   ┌────────────┬───────────┘      │      └──────────────┐
   ▼            ▼                  ▼                      ▼
 H2 Macro     H3/H4/H5          S05 (2.5D)             H6 Reveal plate
 drop         Skincare/Steel/    │                     (Nano Banana Pro edit)
 (S01, S08)   Hotel stills       ▼                        │
   │            │            V1 Hero unfreeze ─────┐      ▼
   │            │            (Kling pro, H1=frame0)│   V2 BG plate (Kling std)
   │            │                │                 │      │
   │            ├─► V3 test ─► (V4/V5 if pass)     │      │  + FG phone/hand layer (cut from H6, local)
   │            │                │                 │      │  + screen insert = V1  ◄┘
   ▼            ▼                ▼                 ▼      ▼
 T1 (H2⊃H3)   T2,T3,T4 comps    S06 ───────────► T5 ──► S07 Reveal
   └────────────┴──────────────── EDIT / GRADE / TYPE / SOUND ──► MASTER 9:16
                                                         └──► 4:5 / 1:1 crops (free)
                                                         └──► 16:9 (phase 2: outpaint stills + regenerate V1/V2)
```
**Reuse rules:** H1 is generated once and used five times (S05 still, V1 source, H2 and H6 reference, palette master). V1 is used twice (S06 and the phone screen in S07). H2 is used twice (S01 and the end card). No asset is regenerated for another format.

---

## 10. Credit budget (exact account prices; balance 84.88)

| Item | Unit | Minimum | Realistic | Worst case |
|---|---|---|---|---|
| Look-dev and hero stills H1–H5 (Soul Cinema) | 0.12 | 10 imgs = 1.2 | 30 = 3.6 | 60 = 7.2 |
| H6 reveal plate (Nano Banana Pro) | 2.0 | 1 = 2.0 | 2 = 4.0 | 3 = 6.0 |
| Fix edits / V1 end frame (Nano Banana Pro) | 2.0 | 0 | 2 = 4.0 | 4 = 8.0 |
| Layer separation fallback (Decompose) | 2.0 | 0 | 1 = 2.0 | 3 = 6.0 |
| **V1 hero unfreeze** (Kling pro 5s) | 8.75 | 1 = 8.75 | 2 = 17.5 | 3 = 26.25 |
| V2 reveal plate (Kling std 4s) | 6.0 | 1 = 6.0 | 1.5 avg = 9.0 | 2 = 12.0 |
| V3 steel frozen test (Kling std 3s) | 4.5 | 0 (skip) | 1 = 4.5 | 2 = 9.0 |
| V4 + V5 frozen drift (Kling std 3s) | 4.5 | 0 | 2 = 9.0 | 3 = 13.5 |
| Temp / fallback VO (Seed Audio) | 0.3 | 0 (real voices) | 7 = 2.1 | 18 = 5.4 |
| Upscale (V2) | ~1–3 | 0 | 1.5 | 3.0 |
| **Total** | | **≈ 18** | **≈ 57** | **≈ 96** |
| **Balance left** | | **≈ 67** | **≈ 28** | **−11** |

**Guardrails that keep the worst case from happening:**
1. **A 15-credit reserve** is never touched until picture lock (for the final fix that always comes up).
2. **Per-asset caps:** V1 gets at most 3 attempts, V2 at most 2. V3 gets 1, and if it fails, all frozen worlds stay 2.5D (saves 13.5).
3. **Order of priority:** if V1 needs its third attempt, V4/V5 are cancelled automatically.
4. **Floor version (about 18 credits)** ships even if almost everything goes wrong: every frozen world in 2.5D, one hero unfreeze, one reveal plate.
5. Every generation is preflighted with `get_cost` first, and I report the exact cost before submitting.

---

## 11. Credit-saving production strategy
1. **Zero-credit animatic first.** Grey-box frames (typography, simple shapes, the drop as a circle) rendered locally with the full timing, transitions, temp sound design and supers. This locks pacing, transition timing and copy **before any image is generated.**
2. **Look-dev at 0.12 a frame.** Iterate composition, light and palette on Soul Cinema in very small batches (2–4 images). Upgrade to Nano Banana Pro only for identity-preserving edits.
3. **Prove the frozen look on the anchor before generating the rest.** Build S05's 2.5D move from H1 alone (0 credits). If it doesn't look like a flagship ad, we change strategy after spending about 1 credit, not 50.
4. **Treat the hero still as the hero video's first frame.** Image-to-video from an approved frame takes composition, light, wardrobe and set out of the gamble; only motion is left to chance.
5. **Trim durations to the second.** Kling is billed per second (std 1.5/s), so generate exactly what the edit uses: 3s, not 5s.
6. **Keep pro for one shot.** Only V1 is generated at pro; the reveal plate is soft focus and doesn't need it.
7. **Prompt one action per clip.** Single, simple motion briefs (one head turn, one ladle set down) reduce rerolls more than any other prompt choice.
8. **Use end frames as the rescue, not the default.** If V1's first attempt drifts, a 2-credit end frame pins the outcome for the second attempt.
9. **Never use model audio.** Sound is designed separately, so `sound: off` on every video saves credits and keeps the mix clean.
10. **Get derivatives without spending.** 4:5 and 1:1 come from center-safe composition; 16:9 is a later phase.

---

## 12. The three shots that get most of the budget (≈ 60% of spend)
1. **S05/S06: bakery hero tableau and unfreeze (H1 + V1).** The emotional payoff, the "this looks expensive" proof, the source of the phone screen and the reference for H2/H6. *Budget: up to 3 V1 attempts (26 credits) plus generous H1 look-dev.*
2. **S01: macro glaze drop (H2).** The first 1.5 seconds decide whether anyone keeps watching; it also returns as the end card and carries T1. *Budget: the most look-dev iterations of any still.*
3. **S07: the reveal (H6 + V2).** The idea lands here. If it feels fake, the whole film turns into a gimmick; it has to feel completely ordinary and real. *Budget: Nano Banana Pro for identity, 2 plate attempts.*

---

## 13. What's likely to fail, and how the design already avoids it
| Risk | Redesign already in the plan |
|---|---|
| Lip-sync on dialogue looks fake | **Removed.** The customer is seen from behind; the baker is in soft focus, looking down. No lips on screen. |
| Hands (extra fingers, wrong grips) | Skincare: only thumb and index visible, mostly behind the pipette bulb. Baker: one simple ladle grip, partly occluded. Welder: gloved. Nano Banana Pro fix in reserve. |
| Liquid physics in motion | Liquids appear **frozen** in stills, where odd physics reads as style. The only liquid in motion (V1 glaze drip) is small and secondary to the flour cloud, which is forgiving. |
| Faces / identity drift | Welder in a helmet; the founder soft-focus with eyes closed; the baker in half-profile rim light in H1 and soft focus in H6. Identity carried by wardrobe (dark apron, hair tied back) more than by the face. |
| Garbled AI text (signs, labels, UI) | Every prompt says "no text, no logos." Unlabeled bottle, blurred chalkboard. All text and UI are added in comp. |
| A video model "unfreezes" a frozen shot | Frozen worlds default to 2.5D (fully controllable). Kling frozen drift is opt-in and only after one 4.5-credit test. |
| 2.5D looks cheap | Real layer separation, slow moves, particle crawl, lens behavior, grain. **Validated at checkpoint 2 for 0 credits before committing.** |
| A jump cut at the unfreeze | V1's frame 0 *is* H1, and the 2.5D move ends on H1's native framing. |
| Match transitions don't line up | Composition coordinates are written into every prompt (drop at x 50%/y 46%, stream at x 52%), and comp reposition/scale absorbs the rest. Stills are generated at 2K for 120% headroom. |
| The phone screen in the reveal warps in video | The phone is a **still foreground layer** composited over the moving background plate; the screen content is inserted in comp. |
| Basic plan blocks a model at submit | Every role has a priced fallback (Kling std → Hailuo 2.3 Fast / Kling 2.6 / Grok Lite at 4–5 credits). Access is checked on the first cheap job. |
| Fictional brand names clash with real businesses | Checked before lock; swappable for real VelaBuilt clients in case-study versions. |
| Platform UI covers text | Safe areas defined in §4. |

---

## 14. Production checkpoints (on approval, one at a time; I stop after each)
| CP | What I do | Credits | You decide |
|---|---|---|---|
| **0** | Zero-credit animatic: grey-box frames, full timing, transitions, supers, temp sound. Confirm local layer-separation tools work. | **0** | Pacing, copy, story |
| **1** | H1 look-dev: 4–8 Soul Cinema frames of the bakery hero, in small batches. | ≈ 0.5–1 | Lock H1 |
| **2** | S05 2.5D frozen-camera test from H1, rendered locally, with sound. | **0** | **Does the frozen look feel like a flagship ad?** (strategy gate) |
| **3** | V1 hero unfreeze, Kling 3.0 pro 5s (cost quoted before submitting). | 8.75 | **Concept go / no-go** |
| **4** | H2 + H6 (+ H3–H5 look-dev on Soul Cinema). | ≈ 3–6 | Lock all stills |
| **5** | V2 reveal plate; optional V3 frozen test. | 6–10.5 | Reveal and frozen-video decision |
| **6** | Full assembly: comps, grade, typography, sound, mix (local). | **0** | Picture lock |
| **7** | Fixes from the 15-credit reserve; final master + 4:5 / 1:1. | ≤ 15 | Delivery |

**Inputs needed from you before CP0:** (1) The VelaBuilt logo and the confirmed domain. (2) Whether the four voices will be real recordings (recommended) or synthetic. (3) Music route: a library track you license, ElevenLabs Music (ElevenLabs credits) or a composer. (4) Approval of the concept, the copy and the fictional business names.
