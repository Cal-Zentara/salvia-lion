# STATUS — Spirit Nancy (Salvia Lion)

*Last updated: 2026-06-06*

## What this is
Site for Salvia Lion (Nancy's pen name) — Reiki, tarot, energy clearing, moon ceremonies, bath salts shop. Not publicly launched yet.

## What's live
- Site at https://cal-zentara.github.io/salvia-lion/
- 11 sections built and styled, mobile-responsive
- Pricing set: Reiki 30min $88.88 / 60min $168.88, Tarot 30min $44 / 60min $77 (Lavender Moon collab), Pet Reiki $66.66, Sacred Hold $444 founding / $668.68 standard, bath salts $10/$24 bundle
- 6 Stripe payment links live — one per scent ($10 each) + bundle ($24) + Sacred Hold founding ($444/mo) + Sacred Hold standard ($668.68/mo)
- Scent pills on site update the Order Yours button to the correct Stripe link when clicked
- Bundle of 3 has its own permanent button alongside Order Yours
- Real product photos: triple bag shot + individual Neroli and Sage bags swap on scent selection
- Sage & Lavender marked bundle-only — $10 single option hides when selected
- Service card photos updated: bookshelf (Reiki), tarot cards at center 65% (Tarot/Lavender Moon collab), AI-generated energy clearing
- Membership renamed from Monthly Hold → Sacred Hold on site
- 10% Lavender Moon discount removed from site (never confirmed with Dalena)
- Garden Grove business license letter received — Nancy handling (EIN done, BofA open, paying GG next)
- Reiki Intake PDF built (`Salvia_Lion_Reiki_Intake_Form.pdf`) — parked, Nancy emails manually for now
- Stripe LIVE — account activated 2026-05-31, all 6 payment links processing

## What's next
- **CONTENT — next action:** build the Week 1 Monday carousel ("What Reiki is" / "3 signs the exhaustion you feel isn't even yours") for June 9. Copy is written and locked in `salvialion/2026-06-03/what-is-reiki-carousel.md`. Just needs the slides generated (awaiting Cal's explicit go — never gen without it). Then start writing the 6 unwritten protection carousels + the 3 faceless process videos.
0. **$100 ad budget ready to spend** — boost the "Protecting your energy" carousel in the IG app. Settings: women 28-55 US, interests Reiki/energy healing/spirituality/meditation/crystals, $10/day x 10 days, Instagram placement, goal = More messages. (Not yet run as of Jun 2.)
1. Nancy fixes Google Calendar booking timezone (GMT → Pacific) — needs desktop mode on Safari
2. Nancy shares booking link → embed as "Book a Session" button on site
3. Setting up Etsy shop — connecting bank for payouts via Plaid (in progress 2026-06-06, Nancy). Bank account must be under her real name, Nancy Huynh.
4. Do a test purchase on each of the 6 Stripe links (now live) to confirm money flows
5. Archive old combined Stripe link (`14A5kCchb3usedodqRcbC00`) in Stripe dashboard
6. Get individual White Tea & Lavender bag photo (landscape/horizontal) to replace triple shot on that scent

## Done
- ✅ **Roadmap deepened + hooks/times/SEO/faceless added (2026-06-03, session 2):** Researched hooks that work in her niche → saved `Marketing/salvialion-hooks.md` (the rule: surprise stops the scroll, recognition makes them save; 6 formulas with ready Salvia versions). Added to `9-WEEK-ROADMAP.md`: a hook for all 27 posts + how-to-use guide, best posting times (a starting guess, her IG Insights are empty at 4 followers so unverifiable), and an Instagram SEO keyword list for captions/slides. Rebuilt the "What Is Reiki" carousel around the "3 signs the exhaustion you feel isn't even yours" hook (`salvialion/2026-06-03/what-is-reiki-carousel.md`, 8 slides, light cream style). Also made a rendered preview page (`9-WEEK-ROADMAP.html` + `roadmap-view/index.html`, viewable in Claude desktop preview via the "roadmap" launch config).
- ✅ **DECISIONS LOCKED (2026-06-03):** (1) Go wellness-broad, not just spiritual — ride the nervous-system / stress-relief wave, Reiki as the deeper why. (2) Faceless but REAL, never an AI avatar (her realness is the whole asset). (3) Faceless setup: real hands/product/atmosphere b-roll + ONE consistent AI voice (ElevenLabs Anaya, same as Blue Moon reel) reading HER real words + minimal elegant 2-word text added in POST (soft serif, lowercase, NOT bold caps). All locked in the roadmap "Faceless video setup" section. (4) Confirmed via real research + Nancy herself: Reiki clears + heals mainly, ends sessions empowering, NOT "replenishing" (her words). (5) Competitor model = @nalaasashakur (Naturally Nala, 39.8K) proves the faceless wellness-broad lane works.
- ✅ Content strategy built (2026-06-03): `Marketing/salvialion-content-masterclass.md` (10-step marketing roadmap modeled on Unik's, anchored in her real positioning/voice/discovery answers) + `Marketing/content/9-WEEK-ROADMAP.md` (9 weeks, M/W/F, every post tagged by job: Teach / Connect / Sell-or-Prove). Mix is research-backed: ~70% value, ~18% selling. Simple at-a-glance table sits at the top of the roadmap file. Locked production rules (carousel style, Reiki symbols, caption format) are in the roadmap's "Production details" section.
- ⚠️ Found the 6-part Protection deep-dive series copy + Higgsfield prompts were NEVER actually saved (an old note claimed they existed; they don't). Corrected in `CONTENT-TRACKER.md`. They fill the Monday Teach slots in weeks 2,3,4,6,7,9 — still need writing.
- ✅ 4th testimonial added + LIVE — bath salts review from reviewer credited as "Mai" (her middle name; shares first name "Nancy" with Salvia, so middle name used to avoid looking like a self-review). First testimonial specifically about the product (2026-06-02)
- ✅ Facebook Page created for Salvia Lion + linked to @salvialion Instagram (2026-06-02) — required infrastructure for running IG/FB ads. Meta Business portfolio "Salvia Lion" also created. Login Lionsalvia@gmail.com.
- ✅ Content tracker built — `Marketing/content/CONTENT-TRACKER.md` logs every post (live, written, ideas). Only 3 posts actually live on IG: "Why salt?" carousel (Apr 29), Blue Moon reel (May 31), "Protecting your energy" carousel (Jun 1, Nancy made herself)
- ✅ 4-week content calendar built — `Marketing/content/CONTENT-CALENDAR.md`, M/W/F schedule, full captions in her voice ready to copy-paste
- ✅ Billed Salvia $57.25 for stamp order #5486467 (2026-04-29)
- ✅ 3 warmup IG posts written (2026-04-27) — Pet Insight, Empath Angle, Ritual Walk-Through
- ✅ 4 full carousel concepts written (2026-04-29) — "Led here", "You're not imagining it", "I needed healing first", "Three scents"
- ✅ Bath Salt Tips carousel (HowSalt / Ritual / WhySalt) — POSTED to IG 2026-04-29 via IG Mega Generator pipeline. Do not reuse.
- ✅ IG Mega Generator pipeline built — drop PNGs → convert → Drive → Instagram, zero manual steps. Nancy's posting tool going forward.
- ✅ Nancy added as Instagram Tester on Zentara Social-IG Meta app (2026-04-29)
- ✅ IG bio set — "Reiki practitioner · Bath salts charged with intention · For people who feel everything · DM to order · $10/$24 🦁"
- ✅ Bath salts Reel built (2026-04-29) — 6 clips edited in Descript, 48 seconds, music "Dreamers", warm color grade, Studio Sound noise removal, Salvia Lion logo outro. Nancy approved. Posts 2026-04-30.
- ✅ Sticker label redesign prompt created — dark version (black/purple/teal) + light version (warm cream/spa feel). Nancy requested light after dark looked too "rave". Generating via GPT Image 2.
- ✅ 6 Stripe payment links created — 3 single bag scents + bundle + 2 Sacred Hold tiers (2026-05-22)
- ✅ Scent pills wired to per-scent Stripe links — Order Yours button updates on pill click (2026-05-22)
- ✅ Monthly Hold renamed Sacred Hold on site (2026-05-22)
- ✅ 10% Lavender Moon discount removed from site (2026-05-22)

## Key files
- `index.html` / `style.css` / `app.js` / `utils.js` — site
- `make_form.py` — generates Reiki Intake PDF
- `Salvia_Lion_Reiki_Intake_Form.pdf` — 2-page intake/waiver form (parked)
- `pics/lion_stamp_v5.png` — ordered stamp artwork
- `CLAUDE.md` — full doc, Nancy's discovery answers Q7-12, decisions, stamp order details

## Deploy notes
- GitHub: `Cal-Zentara/salvia-lion`
- Theme persists via localStorage key `sl-theme`
- Hosting: GitHub Pages
