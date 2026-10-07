# VELABUILT — "ONE SECOND" · Revision v1.2
### Creative execution reset after the Higgsfield reference review
*Status: PLAN ONLY. Production paused. Nothing was generated or spent this turn. Balance 83.92 (0.96 spent in total). Checkpoint 3 has not started.*
*Supersedes the execution sections of v1 and v1.1. The concept, brand line, the hotel cut, the inquiry-cut hook and the budget/kill-point discipline carry over. Where documents differ, v1.2 wins.*

**How the references were inspected:** cut detection, timestamped contact sheets every 0.4 s, full-resolution frame review, optical-flow camera-motion measurement per half-second, local speech transcription, and loudness and spectrogram analysis of all five clips. Working files are in `refwork/`.

**Key fact:** the five clips are not five films. They are **consecutive segments of one ~75-second Higgsfield ad**. A food-truck owner talks to camera ("I sell burritos now… nobody actually knows [I] exist… I'd do these three things"), cutting between generated cinematic footage, app screen recordings, kinetic captions and proof shots, ending on "Comment ADS and I'll send you the full setup" and the button "Here you go man, extra protein."

---

## 1. Reference analysis

### What the references do better than H1/CP2

| # | Craft | Reference | Ours (H1 / CP2) |
|---|---|---|---|
| 1 | **A person, not a figure** | One consistent character across about 20 setups, always *doing* something: leaning into lens, pushing the burrito at us, a peace sign for "Step 2", an open palm toward the camera, a side-eye smirk over his shoulder at the crowd. Behaviour carries personality. | A woman in profile, eyes down, holding a pose. No relationship to the camera, no behaviour, no event. A painting of a baker. |
| 2 | **Lens and proximity** | Wide-angle (about 18–24mm feel) at arm's length. Foreground objects swell (burrito, palm, fingers, napkin), giving energy and intimacy. | About 40mm from about 3 m: a neutral observer that keeps us outside. |
| 3 | **Shot diversity** | 7–9 distinct setups per 15 s: extreme-wide establishing shot, sign hero, address MCU, wide-angle lean-in, product hero with the person behind in forced perspective, macro prop insert (ticket spike), over-the-shoulder hand-off to customer hands, back-to-camera turn. | One setup for 5 s. |
| 4 | **Motivated, varied camera** (measured) | Crash zoom of about 140%/s from the truck exterior to the chef; whip pans used *as* cuts; a push straight into a sauce cup that becomes the next scene; handheld selfie; lateral tracking along the counter. Speed changes with intent. | A constant 2–5%/s drift. The camera has no reason to move and no reason to be where it is. |
| 5 | **Environmental storytelling** | Boardwalk at dusk with a Ferris wheel gives place and time. An empty lot (the problem) becomes a queue (the result). A ticket spike filling with orders tells the success story through a prop. | A dark, generic room. Nothing says who the bakery serves, where it is, or that it has customers. |
| 6 | **A brand world** | Red and cream identity on the truck, the sign, bags, order tickets and the napkin flag. Every object belongs to the business. | Unbranded. Nothing marks it as *a* business. |
| 7 | **Readable commercial light** | Faces lit; practical fluorescents; dusk sky; food bright enough to sell. | "Expensive" achieved through darkness: chiaroscuro murk is a common AI-cinematic cliché, not direction. |
| 8 | **Edit rhythm** | Cuts on spoken beats every 1–3 s; speech drives the edit; key words punched with kinetic type. | No edit at all. |
| 9 | **Tactility** | Hands on food, handing bags into customers' hands, sauce drizzle, slapping the counter. | One decorative pour. |
| 10 | **Humour and a button** | "Extra protein" closes the piece on character. | None. |

### What doesn't work in the references (not our bar)
- **The format is a creator-tutorial direct-response ad.** Roughly 40% of the runtime is white app screen recordings, which break the world. It sells a *tool*; ours must sell the *result*.
- **The sound is a flat, dense wall.** The spectrogram shows continuous music plus voice with almost no dynamics. The only silence in the whole piece is about 0.5 s before the end sting. No real sound design, no use of silence. **ONE SECOND has to do the opposite.**
- **AI tells:** crowds of soft, generic faces; a glossy, uniform "AI commercial" sheen; a flame burst that reads as an effect; slightly off food geometry.
- **Fabricated proof:** view counters ticking 129K → 329K. We won't fake results.
- **The narrative is a list** (Steps 1–3), not a story. The emotional arc is thin. It works as direct response, not as a brand film.

**Conclusion:** their *filmmaking grammar* is the bar: character behaviour, wide-angle proximity, coverage, motivated camera, environment and props as story, rhythm. Their *format* (UI tutorial, wall-to-wall VO, flat mix) is not.

### The H1 diagnosis, answering your questions
- **Why is the camera here?** There's no reason. It's where a painter stands.
- **Why this lens?** A default.
- **Why this instant?** It's a pose, not an instant.
- **What happened before, and what happens after?** Nothing and nothing.
- **What does it reveal about the business?** Only that it has a window.

H1 fails as *direction*, not as rendering. More adjectives can't fix that.

---

## 2. Audit of the material we already have
| Item | Verdict | Note |
|---|---|---|
| ONE SECOND concept, 06:47:12 timestamps, tick motif | **KEEP** | Stronger now: the second becomes the climax of real action |
| Three worlds (bakery, steel, skincare); hotel cut | **KEEP** | Each now gets its own grammar |
| "Worth stopping for." / inquiry hook "THIS IS A BAKERY AD." | **KEEP** | See §17 |
| CP2 renderer (depth, matting, inpainting, 3D particles, inertial camera, rack focus, lens and grain) | **KEEP** | It becomes the frozen-second engine |
| CP2 **Version B** grammar (rack focus through suspended matter) | **KEEP** | The signature move of every frozen shot |
| Hybrid phone reveal method | **KEEP + strengthen** | §16 |
| Budget, kill-point and checkpoint discipline; safe zones | **KEEP** | New kill points in §13 |
| Voice Approach A | **MODIFY** | Restaged as performance and inner thought (§15) |
| Frozen-time engine | **MODIFY** | It now runs on *freeze frames taken from generated footage*, so the freeze is literally that moment |
| The original material chain (glaze → serum → spark → dust) | **REPURPOSE** | Becomes *match cuts* inside the cross-cut, not composited morphs |
| r2_5 beam frame | **REPURPOSE** | Atmosphere insert or fallback transition plate only |
| H1 (r2_4) | **REPURPOSE (demoted)** | No longer the hero. Lighting/colour reference for dawn window light, and an emergency fallback plate for the inquiry cut. Not a casting reference: we recast for personality. |
| CP2 Version A (constant drift) | **ABANDON** | It reads as a screensaver |
| Still-first architecture (designed still → 2.5D as the film's language) | **ABANDON** | It's the root cause of the "AI still" feel |
| The planned 8.75-credit "baker lowers jug and turns" | **ABANDON** | It buys a gesture, not a moment |
| The macro glaze-drop still as cold open; drop-into-drop composite | **ABANDON** | Replaced by a physical, loud cold open |
| 40mm observational default; darkness as luxury | **ABANDON** | — |

---

## 3. Revised filmmaking philosophy
1. **Directed coverage of people doing their craft, edited to sound, building to one impossible instant.** That replaces "beautiful frames moved slowly."
2. **Each business is a miniature campaign with its own grammar:** lens, movement, rhythm, light and sound. If you muted the bakery and the steel shop, you should still be able to tell them apart from the camera behaviour alone.
3. **Time freezes once, on a motivated instant** (a sound triggers it), and **the camera keeps moving.** Frozen time becomes the *payoff* of the film, not its medium.
4. **Live action first.** The frozen moments are built from frames of the same generated footage, so the frozen world *is* the world we just watched.
5. **Structure: a converging cross-cut.**
   - The last seconds before 06:47:12, across three businesses, cutting faster and faster.
   - The second itself: a frozen tour.
   - 06:47:13: time resumes.
   - The reveal, then the end card.
6. **Behaviour beats for every person.** Strength, heat, perfectionism, humour, warmth.
7. **Sound is designed first.** Each world has a sonic signature. The ticks are the clock's last seconds. Silence *is* the freeze.
8. **Light motivated by each business's real sources:** window, oven, arc, lamp. Readable faces. Darkness only where the source dictates it.
9. **A brand world:** name on the window glass, stamp on bags, mark on steel, a label-free bottle with a brand card. Text is added in compositing on flat surfaces (in frozen shots), never left to the model in moving shots.

---

## 4. Treatment, second by second (flagship, 36 s, 9:16)
*Legend: GEN = generative video · LOCAL = CP2 engine / compositing · STILL = Soul Cinema still (0.12) · PRAC = practical phone footage.*
*Timestamps on screen: tiny monospace, lower left, ticking 06:47:06 → :12.*

### Part 1: The last seconds (0:00–0:14). Converging cross-cut; cuts land on ticks or world sounds and get shorter.

| # | Time | World | Shot / action | Lens · camera | Light | Performance | Transition | Sound | Source | Cr |
|---|---|---|---|---|---|---|---|---|---|---|
| B1 | 0:00.0–1.2 | Bakery | **Cold open.** A ball of dough is slammed down onto a floured bench inches from the lens. Flour detonates toward the camera. | ~14mm low at bench level. Locked, with a jolt on impact (the camera "feels" the hit). | Cool dawn window plus warm pendant | Practised, strong hands; a forearm with an old oven burn | Hard cut on the grinder spin-up | 0.3 s silence → **SLAP** → flour whump; tick (:06) under the slap | GEN G1a | (G1a) |
| S1 | 1.2–2.3 | Steel | Camera **rig-mounted on the grinder guard**: the disc bites the beam and sparks blast across the lens. | Wide, extreme close; mechanical vibration | Hard white spark light, blue dawn spill | Gloves, pressure | Cut on the glass "tink" | Grinder whine rising, metal shriek; tick (:07) | GEN G2 | (G2) |
| K1 | 2.3–3.6 | Skincare | **Absolute stillness.** Locked macro of a glass pipette tip; a drop swells under surface tension. | 100mm macro; motion-control creep | Soft top light, refraction caustics | Implied: a fingertip steadies the bottle | Cut on the oven door clunk | Near silence, glass *tink*, breath; tick (:08) quieter | STILL + LOCAL micro-animation (swell, caustic drift) | 0.12 |
| B2 | 3.6–5.0 | Bakery | **Camera inside the deck oven:** the door swings open toward lens, heat shimmer, her face lit orange as she slides a peel under the tray. | ~18mm from inside the oven, slight push out | Oven glow vs. blue room | **Squints at the heat**, jaw set | Cut on the visor clack | Door clunk, roar, crust crackle | GEN G1a | — |
| S2 | 5.0–6.2 | Steel | Low angle: the fabricator straightens, wipes his brow with a forearm, **flips his visor down with a nod**. | 24mm, low and heavy, handheld | Spark plus a sodium work lamp | Weight, decision | Cut on the pipette release | Visor *clack* (the cut), arc buzz | GEN G2 (later frames) | — |
| K2 | 6.2–7.4 | Skincare | The drop releases and falls toward the inner wrist; the slider follows it down. | Macro, slider follows the fall | Same | — | Cut on the thumb-lick sound | A tiny liquid *plip* pre-echo, reversed | STILL + LOCAL (CP2 move) | 0.12 |
| B3 | 7.4–8.6 | Bakery | Wide-angle close, 3/4 to lens: she tastes glaze off her thumb, raises an eyebrow and mutters ***"…too much glaze."*** then shrugs and does it anyway. | ~20mm close, slight handheld | Window key on her face | **Perfectionism and humour.** The thumb hides her lips, so lip-sync is forgiving. | Cut on the spark shower | Dry, close dialogue; apron rustle | GEN G1a | — |
| S3 | 8.6–9.4 | Steel | Punch-in: arc light blooming in the visor glass. | Crop from G2 | Arc white | — | Cut on a tick | Arc crackle | GEN G2 (crop) | — |
| X | 9.4–12.1 | All | **Convergence.** Micro-cuts of 0.5–0.3 s, re-cut from existing footage: flour in the light / spark / drop / glaze / spark / drop. The material match cuts live here. | — | — | — | Accelerating | Ticks :09–:11, each louder and drier; the three world sounds layer and rise | LOCAL edit | 0 |
| B4a | 12.1–14.0 | Bakery | **Hero.** Counter height, wide lens. She slides a tray of glazed croissants **toward the lens**; they loom. Behind her, through the shop, the front door starts to open, a customer backlit by the street. Her eyes begin to lift. | ~20mm at the customer's eye line to the pastry, slow push | Sun breaking through the door gap | **The glance**: she knows a customer is coming | **The door bell = the 12th tick** | Tray scrape, door latch, **DING** | GEN G1b | (G1b) |

### Part 2: The second (0:14–0:24). Everything stops. The camera doesn't.

| # | Time | World | Shot | Camera | Sound | Source | Cr |
|---|---|---|---|---|---|---|---|
| BF1 | 14.0–16.8 | Bakery | Frozen: a glaze drip hangs from the tray edge, flour suspended, the customer frozen mid-step in the doorway. **Rack from the drip (near) to the customer's face (far): her first look into the shop.** Window lettering "SONA BAKERY" composited, reversed in the glass. | CP2-B move: rise and rack | The bell's ring time-stretched into a sustained chord; sub; all other sound gone | LOCAL on the B4 freeze frame (+ optional cleanup) | (1.5) |
| KF | 16.8–19.0 | Skincare | The drop hangs **1 mm above skin**; the camera orbits it. Refraction inside the drop shows the studio window. | Slow orbit (CP2) | Glassy frozen tone; inner VO ***"Three drops. Never four."*** | STILL + LOCAL (refraction) | 0.12 |
| SF | 19.0–21.8 | Steel | **Thousands of sparks hang impossibly in space.** The camera pushes *through* the spark field toward the visor; sparks slide past the lens. | CP2 push plus a 3D spark simulation continuing the real spark trajectories | Spark crackle stretched into granular glitter; inner VO ***"Steady… steady."*** | LOCAL on the G2 freeze frame | 0 |
| GL | 21.8–23.2 | City | **The same second, everywhere:** four 0.35 s frozen glimpses (a concierge mid-handshake; an architect's hand over a site model; a SaaS founder mid-gesture at a whiteboard; tailor's chalk on cloth), each stamped `06:47:12`. | Micro CP2 drift | Single held chord | STILL ×4 + LOCAL | 0.48 |
| BF2 | 23.2–24.0 | Bakery | Back to the baker: a punch-in on her frozen eyes, lifting toward the door. | Slow push | Silence | LOCAL (B4 freeze) | 0 |

### Part 3: Resume and reveal (0:24–0:31)

| # | Time | Shot | Sound | Source | Cr |
|---|---|---|---|---|---|
| B4b | 24.0–25.4 | **TICK → 06:47:13.** Time resumes: the customer steps in, the bell finishes its ring, **the baker looks up and smiles.** No words. | Everything floods back: bell tail, street, oven, **music hit** | GEN G1b (frames after the freeze) | — |
| R | 25.4–31.0 | **Reveal.** Sound-bridge cut: the ad's bell → a different real bell. Over the shoulder of a customer in a queue of three at 11:20, phone in hand (real) playing B4b. The ordinary bakery behind: bright, busy, the baker soft at the counter. *"Is that here?"* / ***"Every morning."*** | Real bell, room tone, espresso hiss; the score collapses into the phone speaker | PRAC phone + STILL background + LOCAL composite | 0.24 |

### Part 4: End (0:31–0:36)

| Time | Picture | Sound |
|---|---|---|
| 31.0 | Warm black | Room tone out |
| 31.2 | **You get one second.** | Music returns to full range |
| 33.0 | **VELABUILT** | Single low note |
| 33.8 | **Worth stopping for.** (velabuilt.com, small) | — |
| 35.5 | — | **Final tick.** Silence. |

---

## 5. Shot hierarchy
| Class | Shots |
|---|---|
| **HERO** | **B4a/BF1/B4b** (the one second: hero performance, freeze and resume) · **SF** (the frozen spark field: the wonder shot) · **B1** (the cold-open hook) |
| SUPPORT | B2, B3, S1, S2, KF |
| TRANSITION | X (convergence), the bell sound bridge, GL glimpses |
| UTILITY | K1/K2, S3 crop, reveal background, end card, timestamps |

**Most of the generation budget goes to: G1b (B4, the hero), G1a (bakery coverage incl. B1), G2 (steel, the source of SF).**

---

## 6. Bakery redesign: filmmaking, not prettier pictures
- **The moment chosen:** *the second the first customer of the day steps in.* Before it: she's been there since 4 a.m., slamming, baking, tasting. After it: a stranger becomes a regular. That's literally the "one second" VelaBuilt sells.
- **Camera position:** at counter height, *the customer's eye line to the pastry*. The croissants loom in the wide lens; the customer is small in the doorway. The frame places us *between* the product and the person who might buy it.
- **Lens:** about 20mm, close. Intimacy and forced perspective, like the references' proximity. **No more observational 40mm.**
- **Coverage builds the character in four beats:**
  - **Strength:** the dough slam.
  - **Endurance:** the oven heat squint.
  - **Perfectionism with humour:** "too much glaze", the shrug.
  - **Warmth:** the smile at the customer.
- **Environment:** a real street outside the door, shop name on the glass, paper bags stamped, a chalkboard (blurred). The reveal later shows the same shop busy, so success is told through the environment.
- **Physicality:** slam, peel, tray slide, thumb taste, door. Every shot has a verb.
- **Light:** dawn window, oven, a pendant over the counter, the sun breaking through the opening door at the hero moment. The light *changes* because the door opens.
- **Casting note:** 40s, laugh lines, a flour-dusted forearm with an old burn mark, hair tied with whatever was at hand. Not a model; a person.

## 7. Steel: its own grammar
**Mechanical, heavy, violent. The camera is a tool too.**
- Rig-mounted on the grinder; low angles; vibration; hard cuts on impacts (visor clack, grinder spin-up).
- Sparks *cross* the lens, not decorate the background.
- **Performance:** the brow-wipe with a forearm; the nod before the visor drops. The face is mostly hidden (visor), so identity risk is low and his body says everything.
- **Light:** arc white, sodium work lamp, blue dawn through the roll-up door. No warm beauty light.
- **Sound:** the loudest world. Grinder whine, metal ring, arc buzz, a boot on a steel plate.
- **Frozen payoff (SF):** the violence stops mid-air, and the camera flies through it.

## 8. Skincare: its own grammar
**Controlled, intimate, precise, nearly silent.**
- Locked-off macro, a motion-control slider creep, almost no cuts. Glass, liquid, surface tension, refraction, skin texture.
- **The person:** present through precision rather than her face. A fingertip steadying the bottle, the breath before the drop, eyes closed in the refraction. Counting under her breath is heard only in the frozen second.
- **Light:** soft, clean, cool top light with one warm accent; caustics.
- **Sound:** room hush, glass *tink*, breath, a liquid *plip*.
- **Why this world can be mostly local:** its grammar *is* stillness. A locked macro in which almost nothing moves is the one place where a still plus subtle local animation (the drop swelling, caustic drift, a slider creep) can pass as real footage. It's chosen because the grammar demands it, not because it's free. It's the riskiest local element, so there's a priced fallback (§10).

---

## 9. Where the frozen-time technology stays (and only there)
It stays **only inside the second** (0:14–0:24): BF1, KF, SF, GL, BF2. That's where it creates wonder: the world has stopped and we're moving through it.
- **It runs on real footage frames** (the B4 and G2 freeze frames), so the freeze is the moment we just saw.
- **Upgrades needed (local, 0 credits):**
  - continuing spark trajectories into frozen 3D particles
  - refraction inside the drop
  - composited window lettering
  - motion-blur-tolerant depth on video frames
  - an optional one-image cleanup of the hero freeze frame (Nano Banana 2, 1.5 credits) if video compression or motion blur shows in the slow rack
- **It's not used** for the bakery or steel live action (that's real generated motion), the reveal, or the end card. The skincare *live* shots K1/K2 are the single exception, justified by their grammar (§8).

## 10. Generative video allocation (exact quoted prices)
| Gen | Shots | Model / workflow | Duration | Credits | Why it can't be faked locally | Fallback |
|---|---|---|---|---|---|---|
| **G1b** | B4a + B4b (+ the BF1 freeze frame) | **Kling 3.0 pro**, image-to-video, start frame (Soul Cinema still) **plus end frame** (Nano Banana 2 edit, 1.5) to pin the smile | 4 s | **7.0** (+1.5 end frame) | A two-person interaction, a physical tray slide, a door, a glance and a smile. Human performance and timing. It's also the source of the freeze and the resume. | Kling 3.0 std 4s (6.0), with the customer reduced to a backlit silhouette |
| **G1a** | B1, B2, B3 | **Cinema Studio Video v2, std, multi-shot (custom 3-shot prompt)**, start image = the same character still | 5 s | **5.0** | Dough and flour physics, oven heat shimmer, performance, three angles of the *same* person in one pass | Kling 3.0 std 5s (7.5); or regenerate only a failed shot with Kling std 3s (4.5) |
| **G2** | S1, S2, S3 (+ the SF freeze frame) | **Hailuo 2.3 Fast, 1080**, start-frame still (one continuous take, cut into three in the edit) | 6 s | **7.0** | Spark physics, mechanical vibration, body weight; the source of the frozen spark field | Seedance 2.0 Mini 5s 720p (5.0), or Kling 3.0 std 4s (6.0) |
| (G3) | K1/K2, only if the local version fails | Hailuo 2.3 Fast 768, 6s | 6 s | (4.0) | Only if the local macro reads as still | Cut skincare to KF only |

**Generation order** is **G1b first.** If the hero moment fails, we stop before buying coverage.

## 11. Cheap / local allocation (no visible quality loss)
- **The frozen second:** BF1, KF, SF, GL, BF2.
- **Skincare macros** (K1/K2/KF): 2–3 stills, local animation.
- **The city glimpses:** 4 stills.
- **Reveal:** practical phone footage plus one background still.
- **Edit-driven coverage:** the convergence micro-cuts (re-cuts of existing footage); punch-ins and crops; speed ramps; match cuts.
- **Graphics:** timestamps, typography, the end card, the inquiry-cut graphics, brand-world decals in frozen shots.
- **Finish:** grade and grain; the full sound design and mix.
- **Voices:** real voices recorded free, or Seed Audio TTS at 0.3 per line.
- **Music:** a licensed track or ElevenLabs (outside the Higgsfield budget).

## 12. Credit budget (exact quotes; 0.96 already spent)
| Item | Minimum | **Target** | Contingency |
|---|---|---|---|
| Look-dev stills (Soul Cinema at 0.12): characters, start frames, skincare, glimpses, reveal background | 1.5 | **2.5** | 3.5 |
| G1b hero (Kling 3.0 pro 4s) | 7.0 | **7.0** | 7.0 + 1 diagnosed retry (7.0) |
| G1b end frame (Nano Banana 2) | 0 | **1.5** | 1.5 |
| G1a bakery coverage (Cinema Studio v2 std multi-shot 5s) | 5.0 | **5.0** | 5.0 + fallback (4.5) |
| G2 steel (Hailuo 2.3 Fast 1080 6s) | 0 (steel frozen-only from a still) | **7.0** | 7.0 |
| Hero freeze-frame cleanup (Nano Banana 2) | 0 | 0 (only if needed) | 1.5 |
| G3 skincare fallback | 0 | 0 | 4.0 |
| **New spend** | **13.5** | **23.0** | **42.5 (do not plan on this)** |
| **Project total incl. 0.96** | **≈ 14.5** | **≈ 24.0** | ≈ 43.5 |

- **The target hits 24.0 with no rerolls**, because order, end frames and multi-shot do the work that rerolls would otherwise do.
- **Any retry is a deliberate overrun** past 25 and needs your approval and a stated reason.
- **The contingency column shows worst-case exposure**, not a plan. The 40 emergency ceiling still stands and needs explicit permission.
- **Minimum viable premium:** the bakery fully live (G1a + G1b); steel frozen-only from a still plus the spark simulation; skincare local. That's 14.5 total, and it still has a real performance, a real hero moment and a real frozen second.

## 13. Failure points, redesigned now, and new kill points
| Risk | Likelihood | Redesign already made |
|---|---|---|
| **G1b two-person interaction** (door, customer, glance, smile) | High | The customer is a backlit silhouette deep in the background; the door is a simple swing; the baker has one action (eyes up, smile) after the tray slide; the **end frame pins the smile** |
| G1a multi-shot ignores the shot plan | Medium | An explicit per-shot prompt; the same start image; fallback is a single-shot Kling replacement for the failed shot only |
| The "inside the oven" POV isn't understood | Medium | Fallback angle: low beside the oven mouth looking up at her (still strong) |
| Lip-sync on "too much glaze" | Low | Her thumb occludes her lips; the line is dubbed in post |
| Steel motion-blurred sparks in the freeze frame | Medium | The frozen spark field is rebuilt by the 3D spark simulation seeded from the real trajectories |
| **Skincare local macro reads as a still** | **Medium-high** | Tested locally first (free). Fallback G3 (4.0), or cut to KF only. |
| Character consistency between G1a and G1b | Medium | The same character still feeds both; wardrobe locked; the reveal baker is soft-focus |
| The cross-cut confuses viewers | Medium | Each world has its own colour, sound and camera signature, plus a timestamp; the bakery opens and closes the sequence |
| Freeze frames too soft for a 3 s rack | Medium | Hero cleanup edit (1.5); short racks elsewhere |

**New kill points (production resumes only with your approval):**
- **K0, look-dev (at most 2 credits):** at most 16 Soul Cinema frames to find the baker character and the B4 start frame. The test: *every* start frame must answer the director questions (why here, why this lens, what just happened, what happens next, what does it reveal). **If none passes: stop.**
- **K1, the hero gate (G1b, 7.0 + 1.5; cumulative about 11.5):** pass needs a clean tray slide, a believable silhouette entrance, a natural glance and smile, and a usable freeze frame. **If it fails: stop the flagship and diagnose. A single retry happens only with a named, fixable cause and your approval.** No unchanged reroll, ever.
- **K2, coverage (G1a):** if fewer than 2 of the 3 shots are usable, replace only the failed shot once (4.5), or cut the bakery to the shots that work.
- **Tripwire:** spend reaches **18 credits** before both G1b and G1a are approved → full review.

## 14. Sound map
| Time | What is heard | Function |
|---|---|---|
| 0:00.0–0:00.3 | **Silence** | Lean-in |
| 0:00.3 | **Dough SLAP**, flour whump; first tick (:06) buried under it | A hook made of sound |
| 0:01–0:09 | **No score.** A rhythm built from the worlds themselves (musique concrète): slap, grinder whine, glass *tink*, oven roar, visor *clack*, arc buzz. Each cut is **triggered by the next world's sound**: grinder spin-up → S1, *tink* → K1, door clunk → B2, *clack* → S2. | Sound drives the edit |
| 0:01–0:12 | **Ticks :06 → :11**, one per second, each closer, drier and louder; a low sub swell rises underneath | The countdown to *the* second |
| 0:09.4–0:12.1 | All three world sounds layered and rising; micro-cuts on the off-beats | Convergence |
| 0:12.1–0:14.0 | Tray scrape, door latch… | Tension |
| **0:14.0** | **The door bell DING = the 12th tick.** 100 ms of hard silence. | **The second begins** |
| 0:14–0:24 | **The frozen second.** No environment at all. The bell's ring stretched into a sustained chord (the bell *becomes* the music). A sub. Each frozen world gets a ghost of its sound: spark crackle → granular glitter; liquid → a glassy tone. **Inner voices, dry and intimate:** "Three drops. Never four." (KF) · "Steady… steady." (SF) | Wonder, interiority |
| 0:23.2–0:24.0 | Everything fades to near-nothing on her eyes | Breath before |
| **0:24.0** | **TICK (:13)** → everything returns at once: bell tail, street, oven, door, and **the first real music hit** | Release |
| 0:25.4 | **Sound-bridge cut**: the ad's bell → a different, cheaper real bell in real room acoustics; the score collapses into a band-limited phone speaker | The reveal is heard before it's understood |
| 0:26–0:31 | Café room tone, espresso hiss, murmur. *"Is that here?"* / *"Every morning."* | Truth |
| 0:31–0:35.5 | Room tone out; the music returns to full range for one resolving chord | Brand |
| 0:35.5 | **Final tick.** Silence. | ONE SECOND, said in sound |

**Music, deliberately unlike the references:** no wall-to-wall bed. Rhythm made of real sounds until 0:24. The first actual musical hit lands *at the resume*, so music itself means "time is moving again."

## 15. Dialogue, reassessed
**Keep Approach A, restaged around performance:**
- **"Too much glaze."** becomes on-camera, muttered during the thumb taste (B3). That's character behaviour, not narration. Her lips are occluded, so it can be dubbed.
- **"Three drops. Never four."** and **"Steady… steady."** become **inner voices inside the frozen second.** That's the only place a line can be heard while time is stopped, and it tells us what each person cares about in *their* second. There's no lip-sync risk.
- **The reveal:** *"Is that here?" / "Every morning."* Unchanged; still the best two lines.
- **Considered and rejected:** a greeting from the baker at the resume ("Morning."). The smile does more, and it would add lip-sync risk for no gain.
- **The references' lesson** is that performance carries personality, not that a film needs more words. We stay at about 14 spoken words; they use about 150.

## 16. Final reveal: still the strongest, now strengthened
**Why it stays:** it's the *commercial argument* (this is an ordinary business), and nothing else in the film makes that point.

**Upgrades:**
- (a) **The sound bridge**: the ad's bell → a real bell.
- (b) The phone plays **B4b (the smile at the customer)** while the real baker behind is busy, so the ad's warmth sits against real morning chaos.
- (c) **A queue of three**: success told through the environment, the reference grammar applied honestly.
- (d) **The customer's glance** from phone to counter motivates "Is that here?"

**Method:** the hybrid from CP1. Your real hand, phone, screen glow, reflections and focus, filmed in about 10 minutes, plus one generated background still (0.12) with the same baker, soft. Optional local depth drift. **0.24 credits.**

## 17. Brand ending, reassessed
- **Flagship:** **You get one second.** → **VELABUILT** → **Worth stopping for.** I removed "Make it worth stopping for" from v1.1: saying the line twice weakened it. No descriptor, as decided.
- **Inquiry cut (20 s), bakery only, a core deliverable:**
  - **The hook works even better now:** **"THIS IS A BAKERY AD."** lands over the visceral dough slam and flour burst (B1), not a static drop.
  - **Order:** B1 → B2 → B3 → B4a → BF1 (2.5 s frozen) → B4b → reveal → end card.
  - **End card:** *Look like the business you already are.* / *Flagship campaign films, without a flagship-sized production.* / **Tell us about your business. velabuilt.com**
  - **Cost:** the same assets, 0 extra credits.

## 18. Sales test
*Would the owner of a normal bakery, contractor, engineering firm, hotel, restaurant, fashion company or SaaS company immediately understand "VelaBuilt could make MY business look extraordinary"?*

| Owner | Answer | Why |
|---|---|---|
| Bakery, restaurant, food | **Yes**, strongly | The bakery world plus the reveal |
| Contractor, engineering | **Yes** | The steel world: the most surprising proof that trades can look epic |
| Consumer, beauty brand | **Yes** | Skincare |
| Hospitality, property, SaaS, fashion | **Partly → yes** | **Fixed in v1.2 by GL**: four 0.35 s frozen glimpses (concierge, architect, SaaS founder, tailor) all at 06:47:12, "the same second, everywhere." That costs about 0.5 credits. **SaaS remains the weakest:** a whiteboard glimpse implies, it doesn't prove. Phase 2 inquiry cuts per vertical solve it properly. |

**The reveal is the commercial hinge:** an ordinary shop, a real phone, a queue. Without it the film is "nice AI art". With it, it's an offer.

## 19. Quality test
*With the logo removed, beside the Higgsfield references in an Instagram feed, would the filmmaking feel competitive?*

**The truthful answer: competitive in direction and clearly stronger in sound and structure, if G1b and G1a land. Not competitive in sheer volume of coverage.**
- **We match their grammar:**
  - about 20 distinct setups
  - wide-angle proximity
  - behaviour beats
  - motivated, changing camera (crash moves, rig mounts, a push-through, rack focus)
  - an environment and brand world
- **We beat them on:**
  - a real story, not a list
  - sound design, silence and dynamics
  - the frozen second, a set piece they don't have
  - honesty: no fabricated metrics
- **Where we're behind:** they almost certainly generated dozens of clips and picked the best; we buy three generations. We compensate with multi-shot generation, end frames, one take re-cut into several shots, and freeze-frame reuse.
- **If G1b fails, the answer becomes no.** That's why K1 is the kill point.
- **H1 and CP2 alone would not be competitive.** That's the reason for this revision.

## 20. Recommendation: **PROCEED** (to a redefined Checkpoint 3)
**Why proceed:**
- The concept survives the reference test and gets *stronger*. "One second" becomes the climax of real, directed action instead of an excuse for stills.
- The budget still lands at about 24 credits.
- The kill points mean we find out whether the hero moment works after about 11.5 credits, not 24.

**Why not "revise again":** the remaining unknowns can't be answered on paper. They need the K0 look-dev frames and the K1 hero generation.

**Why not abandon:** nothing in the references beats the idea. They beat our *execution*, and this plan replaces it.

**Redefined CP3, for your approval (nothing has started):**
- **CP3a (at most 2 credits):** cast the baker and design the B4 start frame plus the end frame on Soul Cinema / Nano Banana 2, against the director-question test. Then stop.
- **CP3b (7.0):** G1b hero generation. **The kill point.** Then stop.

*No generation, no credits spent, and Checkpoint 3 has not begun. Balance: 83.92.*
