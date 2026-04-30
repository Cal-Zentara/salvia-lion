# STATUS — Spirit Nancy (Salvia Lion)

*Last updated: 2026-04-29 (evening)*

## What this is
Demo/soon-to-be-live site for Salvia Lion (Nancy's pen name) — Reiki, tarot, energy clearing, moon ceremonies, bath salts shop. Holding release until she's ready.

## What's live
- Site at https://cal-zentara.github.io/salvia-lion/ (not public-launched yet)
- 11 sections built: nav, hero, marquee, about, services, bath salts shop, testimonials, how it works, FAQ, CTA, footer
- Pricing set: Reiki/Tarot 30min $88.88 / 60min $168.88, Monthly Hold $444 founding / $668.68 standard, bath salts $10/$24 bundle
- Reiki Intake PDF built (`Salvia_Lion_Reiki_Intake_Form.pdf`) — 2-page form with liability waiver, built via Python/ReportLab (`make_form.py`)
- Bath salt copy rewritten 2026-04-27 — empath angle, Reiki credential, ritual instruction line added

## What's broken / blocked
- **Payments blocked** — Nancy needs to open a business checking account before Stripe can be set up for bath salt orders
- **Digital signing blocked** — Nancy needs to create PandaDoc account (Lionsalvia@gmail.com) → upload intake PDF → embed link on site

## What's next
1. Nancy posts bath salts Reel tomorrow (2026-04-30) — built in Descript, approved by Nancy
2. Set up booking calendar — Calendly free plan (1 event type, unlimited bookings). Nancy's specs: 2 sessions/week max, 1 weekend day + 1 weekday, flexible on exact time. Embed on site once set up.
3. Nancy posts IG Stories this week: poll (scent choice), question box ("when do you feel most drained?"), this-or-that (morning vs night bath)
4. Send Salvia the 3 sample IG posts (saved at `Marketing/content/salvialion/2026-04-27/posts-2026-04-27.md`)
5. Salvia opens business checking → Stripe setup for bath salts
6. Salvia creates PandaDoc account → upload intake PDF → sign-embed on site
7. Run `/testimonial-collector` once Salvia has first buyers

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
## Key files
- `index.html` / `style.css` / `app.js` / `utils.js` — site
- `make_form.py` — generates Reiki Intake PDF
- `Salvia_Lion_Reiki_Intake_Form.pdf` — 2-page intake/waiver form
- `pics/lion_stamp_v5.png` — ordered stamp artwork
- `CLAUDE.md` — full doc, Nancy's discovery answers Q7-12, decisions, stamp order details

## Deploy notes
- GitHub: `Cal-Zentara/salvia-lion`
- Theme persists via localStorage key `sl-theme`
- Hosting: GitHub Pages
