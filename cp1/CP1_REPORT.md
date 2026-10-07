# CHECKPOINT 1 — H1 Bakery Hero Frame · Report
*Stopped at end of CP1. Nothing beyond CP1 has been started.*

## Spend
| | Credits |
|---|---|
| Balance before CP1 | 84.88 |
| Round 1: 4 × Soul Cinema 2K | 0.48 |
| Round 2: 4 × Soul Cinema 2K | 0.48 |
| **CP1 total** | **0.96** |
| **Balance now** | **83.92** |
| Project spend vs. target (≤ 25) / ceiling (40) | 0.96 / 25 / 40 |

Also confirmed: Basic can submit to Soul Cinema. Real cost per image is exactly 0.12; the quote rounds up to "1".

## What was generated (see `contact_sheet.jpg`)
| Frame | Direction | Verdict | Why |
|---|---|---|---|
| r1_0 | Wide tableau, ladle | ✗ | Strong mood, but the glaze loops *upward* above the ladle like a rope; garbled text on the oven |
| r1_1 | Medium, ladle | ✗ (best light) | The exact light the film needs (diagonal beam full of dust, blue street), but the glaze falls into a bowl from nowhere |
| r1_2 | Medium, ladle | ✗ | Floating bowl, sparkler-like stream |
| r1_3 | Medium, ladle | ✗ | The ladle became a sphere; daylight street with green trees |
| **r2_4** | **Wide, jug pour, text-only** | **✓ conditional pass → H1 candidate** | See below |
| r2_5 | Wide, jug pour, text-only | ✗ for H1 / ✓ as a bonus asset | Stunning beam, but the baker is too small for the hero shot. **Reusable at no cost** as the "entering through the light shaft" frame for the sparks → dust transition. |
| r2_6 | Jug, r1_1 as reference | ✗ | The reference carried its physics error over: glaze falls from a lamp |
| r2_7 | Jug, r1_1 as reference | ✗ | Glaze falls from the ceiling |

**Diagnosis:** round 1 failed on one variable, the pouring action ("a ladle pouring a ribbon"). Changing only that to "a small jug, one thin stream from the spout" fixed it. Using r1_1 as an image reference brought its error back, so **don't use reference images on this model for H1.**

## r2_4 against the H1 rubric
| Criterion | Result |
|---|---|
| Sits next to a top-tier food campaign frame without apology | **Yes on light and composition.** The image is slightly soft, which reads as 35mm film, not as AI. |
| Single motivated light source | **Pass.** A hard diagonal sun shaft through a tall window, cool blue fill. |
| Hands and face clean at 100% zoom | **Pass.** A natural profile; the grip on the jug and the hand on the tray are anatomically clean. |
| Flour and glaze physically believable | **Glaze: pass** (it leaves the spout correctly and drops sit beside the stream). **Flour: weak.** It's haze in the beam rather than a distinct frozen cloud. |
| Holds at 9:16 inside the safe areas | **Fixable for free.** The tray sits right on the bottom UI boundary (see `safezone_test.jpg`). Fix: scale up 8% and shift up 140 px when compositing. |
| Amber / blue palette | **Pass** |

**Two gaps remain, and both have free fixes planned:**
1. **Weak flour cloud.** A particle-simulated flour cloud composited into the beam at CP2 (0 credits). Only if that fails to convince: one Nano Banana Pro edit of r2_4 (2 credits).
2. **Tray in the UI zone.** Reframe as above (0 credits).

**Unfreeze note for later (CP3):** her arm is raised holding the jug, so the single motion is natural: *she lowers the jug and turns her head toward the door.*

## Recommendation: PROCEED to CP2 (the 2.5D frozen-camera test, 0 credits). Don't revise or kill.
- The evidence that the target standard is reachable: in 8 frames costing under a credit, the model produced campaign-grade light twice (r2_4, r2_5). The only failure mode was diagnosed and fixed by changing one variable.
- **What CP1 does *not* prove yet:** whether the frozen look survives movement, and whether the unfreeze works. Those are CP2 (free) and CP3 (the kill point), exactly as planned.
- I won't proceed without your approval.

---

## Requested design item A: brand descriptor

**Recommendation for the flagship: no descriptor.** End on **VELABUILT** + **Worth stopping for.** (with the URL small).
- **The film is the descriptor.** Thirty-five seconds have already shown what VelaBuilt does. A line explaining it underneath is redundant and makes the ending sound less sure of itself.
- **Any descriptor narrows the audience.** "Independent", "small" and "every size" each rule someone out or say nothing. The common denominator across contractors, engineering, SaaS, property, consumer brands and hospitality is the *result*, which the tagline already names.
- **It matches how premium end cards work:** wordmark plus one line.
- **The risk:** a viewer who doesn't know what VelaBuilt is. That's covered by the post caption, the profile, and the inquiry cut, which carries the explanation.
- **A/B in the edit (free):** with or without the descriptor, in case you want evidence.

**For the inquiry cut**, which needs to be explicit, replace the v1.1 subline:
- ~~"Campaign films for independent businesses, without a campaign-sized production."~~
- → **"Flagship campaign films, without a flagship-sized production."**

It works for any sector and says the real value without a price claim. The headline stays **"Look like the business you already are."**

## Requested design item B: the reveal (no ideal bakery or actor assumed)

### Recommended: the HYBRID, "real phone, generated world"
**What's real (you film it in about 10 minutes, anywhere, for 0 credits):**
- Your own hand holding phone B, which plays the V1 export at full brightness, filmed by phone A over your shoulder.
- Shoot near a window with an overhead light on: mixed daylight and indoor light, close to the "11 a.m. bakery" look.
- Phone A: 2× lens, focus locked on the screen, exposure locked, 4K at 24 or 25 fps.
- Behind the phone: anything dim and mid-tone (a hallway, a kitchen wall), 2 m or more away so it goes soft.

That captures the real screen glow, moiré and reflections, a real hand, real light spilling onto the thumb, real handheld micro-motion, real focus breathing and the phone camera's own noise. **These are exactly the details that give away a composite when they're faked.**

**What's generated:** the bakery environment and the soft-focus baker. Either a 2.5D still (H6, 2 credits) or a moving plate (V2, Kling std 4s, 6 credits).

**Joining them:**
1. **Tracking:** the phone is a rigid rectangle, so its four corners are tracked in your footage with OpenCV (free). That gives the exact real handheld motion, which is applied to the background at 0.35× for depth-correct parallax.
2. **Separating hand and phone from your background:** local segmentation. The edges are forgiving because the bakery behind is soft. Fallback: Higgsfield's video background remover (cost quoted before use).
3. **Light match:** your real hand's lighting is the reference. The bakery plate is graded to match it, never the other way round.
4. **Finish:** one grain, one lens and one vignette pass over the whole frame. The audio is the real phone speaker re-recorded off the real phone (free).

### Comparison
| | Fully generated | **Hybrid (recommended)** | Fully practical |
|---|---|---|---|
| Realism of phone, hand and screen | Medium: every physical cue is simulated, which is the classic tell | **High: all real** | Highest |
| Realism of environment and person | Medium-high (soft focus helps) | Medium-high (same) | Highest |
| Same-bakery continuity with the ad | Good (generated from H1) | **Good (generated from H1)** | Only if the ad is generated from that real location |
| Overall believability (estimate) | 65–75% | **85–90%** | 100% |
| Difficulty for you | None | **Low: one 10-minute phone shoot at home** | High: location, person, permission, releases |
| Difficulty for me | High: 12 simulated realism layers | Medium: tracking, matting, light matching | Low |
| Credit cost | 8 (H6 + V2) | **2–8** (still or moving background) | 0 |
| Main risk | Looks composited | Light mismatch between your room and the plate (solved by shooting near a window and grading the plate to your footage) | Logistics and consent |

**Hybrid workflow order:** CP3 (V1 approved) → I send you a one-page shot card, and you film three takes → I composite.

**Cost decision:** start with the background as a **2.5D still (2 credits)**. A soft-focus background barely needs to move. Only spend the 6 on a V2 moving plate if the still reads as frozen in the three-viewer test. **Expected cost for the reveal: 2 credits.**

## Deliverables in `cp1/`
- `contact_sheet.jpg`: all 8 frames, labelled
- `h1_candidate_1080.png`: r2_4 at 1080×1920
- `safezone_test.jpg`: r2_4 with the platform UI zones and the timestamp type placed
- `raw/`: full-resolution originals (not committed; also stored in your Higgsfield library)
