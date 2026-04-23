# STATUS — Spirit Nancy (Salvia Lion)

*Last updated: 2026-04-23*

## What this is
Demo/soon-to-be-live site for Salvia Lion (Nancy's pen name) — Reiki, tarot, energy clearing, moon ceremonies, bath salts shop. Holding release until she's ready.

## What's live
- Site at https://cal-zentara.github.io/salvia-lion/ (not public-launched yet)
- 11 sections built: nav, hero, marquee, about, services, bath salts shop, testimonials, how it works, FAQ, CTA, footer
- Pricing set: Reiki/Tarot 30min $88.88 / 60min $168.88, Monthly Hold $444 founding / $668.68 standard, bath salts $10/$24 bundle
- Reiki Intake PDF built (`Salvia_Lion_Reiki_Intake_Form.pdf`) — 2-page form with liability waiver, built via Python/ReportLab (`make_form.py`)
- Bath salt copy (Nancy-provided), contact email (Lionsalvia@gmail.com) all wired

## What's broken / blocked
- **Payments blocked** — Nancy needs to open a business checking account before Stripe can be set up for bath salt orders
- **Digital signing blocked** — Nancy needs to create PandaDoc account (Lionsalvia@gmail.com) → upload intake PDF → embed link on site
- Awaiting Salvia's approval of her profile photo on the live site
- Only 3 real testimonials (Cal, Vikki, Rosemary) + 4 placeholders — need 1-2 more real ones

## What's next
1. **Bill Nancy $57.25** for stamp order #5486467 (RubberStamps.net, ships 5-10 business days from April 19)
2. Nancy opens business checking → Stripe setup for bath salts
3. Nancy creates PandaDoc account → upload intake PDF → sign-embed on site
4. Collect more real testimonials
5. Send Nancy Her People questions Q13-18 when timing is right

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
