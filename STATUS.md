# STATUS — Spirit Nancy (Salvia Lion)

*Last updated: 2026-05-22*

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
- Stripe account under review (2-3 days from 2026-05-22) — payments will activate once cleared

## What's next
1. Nancy fixes Google Calendar booking timezone (GMT → Pacific) — needs desktop mode on Safari
2. Nancy shares booking link → embed as "Book a Session" button on site
3. Wait for Stripe review to clear (2-3 days from 2026-05-22)
4. Do a test purchase on each of the 6 Stripe links once review clears
5. Archive old combined Stripe link (`14A5kCchb3usedodqRcbC00`) in Stripe dashboard
6. Get individual White Tea & Lavender bag photo (landscape/horizontal) to replace triple shot on that scent

## Done
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
