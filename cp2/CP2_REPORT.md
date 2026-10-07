# CHECKPOINT 2: Frozen-Time Camera Move · Report
*Stopped at the end of CP2. No Higgsfield video was generated and CP3 has not started.*

## Spend
| | Credits |
|---|---|
| CP2 generation spend | **0.00** (everything was rendered locally) |
| Cost quotes only (no jobs) | outpaint 2.00 · FLUX outpaint 3.08 |
| **Balance** | **83.92** (unchanged since CP1) |
| Project total so far | 0.96 of the 25 target / 40 ceiling |

## What was built (all local, 0 credits)
**A real depth camera, not cut-out cards.**
- Monocular depth (Depth Anything V2) and subject matting (RMBG-1.4) run locally on H1.
- The image is split into two layers: the baker, jug, stream, tray and bench in front; the room behind. The room is filled in behind the baker, and the baker's edge colours are cleaned.
- Each pixel moves according to its own depth through a perspective camera: a dolly, not a zoom, so the bench, baker and window all scale and shift by different amounts.

**Frozen flour and dust in 3D.**
- About 22–26k fine motes, a few near-lens out-of-focus discs, and 14–16 soft cloud puffs, all placed in world space and projected through the same camera, so they parallax correctly.
- They're lit only inside the sunbeam, hidden behind the baker, defocused by distance from the focus plane, and drift very slightly (about 1% of real time) so the frame never looks dead.

**Lens and film.**
- An inertial camera path with a heavy settle and an operator float that fades out.
- A slight roll, lens breathing during the focus pull, bloom, edge chromatic aberration, barrel distortion, vignette and gate weave.
- **The source's baked-in grain is removed and fresh grain is added every frame**, so no grain texture slides with the image. That's a classic "photo being pushed around" giveaway.

**Framing.** A 1.22× crop places the glaze landing and the croissants above the bottom UI zone.

| Version | Move | File |
|---|---|---|
| **A, restrained** | 5s slow push with a slight arc to the right and a roll settle. Ends on the exact H1 rest framing. | `out/cp2_A_1080x1920.mp4` |
| **B, ambitious** | 5s. Opens tight inside the sunbeam, focused on frozen motes about 0.8 m away. **Racks focus to the baker** while pulling back and arcing down. Ends on the same rest framing. | `out/cp2_B_1080x1920.mp4` |
| C, r2_5 test | 3s drift through the r2_5 beam | `out/cp2_C_r25_beam_1080x1920.mp4` |
| Comparison | A and B side by side, with a 1s hold | `out/cp2_A_vs_B_side_by_side.mp4` |

---

## 1. Which version wins: B
- **It produces an optical event a photograph can't have.** The rack focus, from in-focus dust to the baker, with lens breathing, is the strongest "a real camera was here" signal in the test.
- **Its depth reads strongly.** Measured frame-to-frame, B's foreground/background separation is about 4× A's (see the difference maps). Window, baker, bench and dust move as separate planes.
- **It's the right shot for the story.** v1.1 says we arrive *through the light shaft* from the sparks transition. B's first frame *is* that landing: in-focus motes in a beam. The transition and the camera move become one gesture.
- **The handoff is the same as A's.** B ends on the identical rest framing, so CP3's video starts on the same frame either way.

**Why A loses:** it's technically clean (no artefacts at all), but the move is so restrained that on a phone screen it risks reading as a slow zoom on a photo, which is exactly the failure the brief warns about. **A remains a fallback** if B's opening defocus feels too long in the edit.

## 2. Does frozen time still feel premium in motion? Yes, on the evidence I can measure.
- The sunbeam, the frozen glaze stream and the suspended dust survive the move, and the frame reads as a lit physical space, not a flat picture.
- **Honest limitation:** I judge motion from frame sequences, crops and difference maps, not by watching in real time the way a viewer does.
- **Your gate test:** watch `cp2_A_vs_B_side_by_side.mp4` on a phone at full brightness, then show B to one or two people who know nothing about the project and ask: *"Was this filmed, or is it a photo being moved?"* That was the Gate 1 test in the plan.

## 3. Artefacts and weaknesses exposed by movement
| # | Issue | Severity | Fix |
|---|---|---|---|
| 1 | **The flour cloud reads as luminous haze plus fine specks, not a defined, billowing frozen cloud** (like a high-speed-photography flour burst) | Medium | Accept for the frozen shot. If you want a hero billow, see Q5. |
| 2 | B's plate defocus uses a gaussian blur, so blurred highlights (window, glaze) lack real lens-bokeh shape | Low | Free: a disc-shaped blur on highlights |
| 3 | The 1.22× crop upscales the source about 1.14×: slightly softer than native, invisible under grain at phone size | Low | Accept, or the Q5 outpaint |
| 4 | A's opening frame leaves about 0.2% of pixels (a strip of 2 px or less at one edge) uncovered | Very low | Free: zoom 1.23 |
| 5 | The sunbeam is baked into the back-wall layer, so it moves like the wall rather than as a volume in the air | Low | Masked: the lit motes carry the volume, and it isn't noticeable at B's amplitude. A larger move would expose it. |
| 6 | Mote lighting comes from a 2D beam map, so at much larger moves some lit motes would drift outside the visible beam | Low | Fine within B's range; it limits how far the move can go |
| 7 | Croissant highlights bloom slightly hot on some frames | Very low | Free: tame the bloom |
| 8 | **Not tested: sound.** The frozen-time feeling will depend heavily on the freeze-shimmer sound design. | — | Assembly checkpoint |

**Clean:** no cut-out halo on hair, profile, arm or jug at maximum offset; no visible background stretching behind the arm or bench; the glaze stream stays continuous and legible (soft during the rack, crisp on landing); safe zones hold.

**r2_5 (Version C):** the beam is beautiful in motion, but the baker reads as dark eye sockets with an odd raised hand, and it's a *different room* from H1. Cutting between them would break spatial continuity, and B already enters through H1's own beam. **Verdict: not needed in S05. Kept as a backup landing plate for the sparks → dust transition.**

## 4. Does the simulated flour cloud work?
**As frozen atmosphere: yes.** The dust in the beam and the fine suspended flour over the croissants are convincing and carry most of the 3D effect.

**As a dramatic "frozen flour explosion": no.** It reads as haze, not a sculpted billow.

**Important for CP3:** the CP3 video is generated from the *raw* H1, which has no simulated particles. The plan carries the particle simulation over the start of the video and **lets the frozen motes start drifting and falling as time resumes**. That keeps the cut seamless, and makes the dust part of the "unfreeze" payoff at no cost.

## 5. Does H1 need the optional 2-credit edit before animation? No.
- **For framing:** the 1.22× crop already puts the landing above the UI zone. An outpaint (2.00 credits, or 3.08 for FLUX) would buy extra headroom and resolution, but it changes H1, adds a seam risk, and isn't needed.
- **For the flour:** the simulation covers the frozen shot, and carrying it over the video covers the unfreeze.
- **The only reason to spend it:** if you specifically want a *visible, defined flour billow* in the unfreeze shot. Kling animates what's in the start frame, so it can only roll a cloud that exists in H1. My recommendation is to try CP3 without it. If the first unfreeze attempt feels thin, the edit becomes the diagnosed variable change for attempt 2, which is consistent with the reroll rules.

## 6. Should CP3 proceed? Yes, conditionally.
**Proceed if:** after watching the side-by-side, you agree B reads as a filmed camera move.

**CP3 as planned:**
- **One** Kling 3.0 pro, 5s, image-to-video from raw H1 (r2_4). **8.75 credits.** Quoted again before submission.
- Prompt: a single action. *Time resumes; she lowers the jug and turns her head toward the shop door.* The glaze stream continues and drips; dust drifts through the beam. Locked camera with slight drift, no sound.
- **Kill point unchanged:** at most 2 attempts. If neither yields 2.5 s or more of clean footage from frame 0, the flagship stops. Cumulative spend at that point: **18.46 at most.**

## 7. Credits
**CP2 spend: 0.00. Remaining balance: 83.92. Project total: 0.96.**

## Files
`out/`: the A and B masters, the A/B side-by-side, the C test, keyframe strips and end-frame safe-zone checks. `tools/`: the reproducible renderer (`analyze.py`, `render.py`, `finish.sh`). `work/*.json`: the exact settings for each version.
