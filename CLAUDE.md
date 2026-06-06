# CLAUDE.md — Spirit Nancy

## Quick Nav — Read First

| I'm doing... | Read only... |
|---|---|
| Continuing work / resuming | `STATUS.md` |
| Fixing a bug | `STATUS.md` + Files / Sections tables |
| Adding a feature | `STATUS.md` + Design + relevant file |
| Working on intake PDF | `make_form.py` + Digital signing section |
| Understanding the whole project | This CLAUDE.md in full |

**Do not explore.** If the answer isn't in the files above, ask before searching.

---

## Dev Reference — Symbol Map / Schema / Gotchas

> Keep line ranges current. If a code change shifts lines, update the table in the same edit.

### Symbol Map

| Feature | File | Lines |
|---|---|---|
| Nav (logo, links, theme toggle, hamburger) | `index.html` | 14–32 |
| Nav + mobile hamburger styles | `style.css` | 119–1343 |
| Hero (lion image, text) | `index.html` | 34–54 |
| Hero styles | `style.css` | 193–282 |
| Services (3-card grid: Reiki, Tarot, Energy & Tools) | `index.html` | 147–193 |
| Services styles + card tilt | `style.css` | 479–586 |
| Bath salts shop (video + scent selector) | `index.html` | 196–240 |
| Bath salts styles | `style.css` | 733–871 |
| Pet Reiki section (single centered card) | `index.html` | 243–262 |
| Membership section (Sacred Hold) | `index.html` | 265–323 |
| Membership styles | `style.css` | 581–731 |
| Testimonials carousel | `index.html` | 326–372 |
| Testimonials carousel styles | `style.css` | 865–995 |
| How It Works horizontal scroll | `style.css` | 996–1057 |
| FAQ accordion | `index.html` | 404–447 |
| FAQ styles | `style.css` | 1059–1127 |
| Mobile nav overlay | `index.html` | 469–479 |
| Mobile nav styles | `style.css` | 1344–1442 |
| Theme CSS variables | `style.css` | 26–44 |
| Light-mode theme overrides | `style.css` | 1214–1287 |
| Scroll reveal styles | `style.css` | 1302–1312 |
| Scroll reveal (fade-in observer) | `app.js` | 5–17 |
| Carousel auto-advance + controls | `app.js` | 19–66 |
| 3D card tilt on hover | `app.js` | 68–82 |
| Magnetic button pull | `app.js` | 84–98 |
| Horizontal drag scroll | `app.js` | 100–125 |
| FAQ expand/collapse | `app.js` | 141–158 |
| Mobile nav toggle logic | `app.js` | 160–188 |
| Theme toggle + localStorage persistence | `app.js` | 190–207 |
| Shared utilities (storage, toast, fetch) | `utils.js` | 1–153 |
| Shared base reset + toast container | `shared/base.css` | 1–47 (now inlined into style.css) |

### Data Schema

No client-side persistence beyond theme preference.

- **localStorage key:** `sl-theme` — values `'light'` or `'dark'` (set by theme toggle, `app.js` lines 195–206)
- **Query params:** none
- **API endpoints:** none
- **Primary contact email (all CTAs):** `Lionsalvia@gmail.com`
- **Bath salts Stripe links (per scent):**
  - White Tea & Lavender $10: `https://buy.stripe.com/dRm6oG6WRfdaglwbiJcbC01`
  - Neroli & Eucalyptus $10: `https://buy.stripe.com/fZu5kC80Vfda8T4aeFcbC02`
  - Sage & Lavender $10: `https://buy.stripe.com/9B68wO5SN0igfhsdqRcbC03`
  - Bundle of 3 $24: `https://buy.stripe.com/6oUbJ0bd75CA7P09aBcbC04`
- **Session Stripe links:**
  - Reiki 30 min $88.88: `https://buy.stripe.com/7sY6oG80VaWU1qCdqRcbC07`
  - Reiki 60 min $168.88: `https://buy.stripe.com/8x2eVc2GB4yw5GSeuVcbC08`
  - Distance Reiki for Pets $66.66: `https://buy.stripe.com/dRm9AS1CxgheglweuVcbC09`
- **Sacred Hold Stripe links:**
  - Founding $444/mo: `https://buy.stripe.com/dRm00ia93e96fhsaeFcbC05`
  - Standard $668.68/mo: `https://buy.stripe.com/28E7sK0yt1mk3yKfyZcbC06`
- ✅ Stripe account ACTIVATED (confirmed 2026-05-31) — all payment links live and processing

### Known Gotchas

- **`base.css` is inlined into `style.css`** (lines 1–19) — originally imported from `../shared/base.css`, now local to avoid path issues. `utils.js` is still imported directly from local copy.
- **Hero lion blend mode switches on mobile** — `mix-blend-mode: screen` on desktop (line 265) → `normal` on mobile (line 280). Intentional: screen mode breaks readability on small screens.
- **Hero is `flex-column` on mobile** (line 1403) — lion image moves below text from absolutely-positioned right side on desktop.
- **About photo has no crop** — explicitly `75% width, height: auto` (line 457–458) to preserve full face.
- **Service card `object-position` overrides** — Tarot `center 65%`, Energy Clearing `center 40%` — to frame the subject correctly in the cropped card header.
- **Carousel is hand-rolled** (`transform: translateX`, 100% width per card, lines 40, 877–879) — not a library. Auto-advance uses `setInterval`, no pause-on-hover.
- **Horizontal drag scroll uses multiplier `1.5`** (line 122) — snappier than mouse movement by design.
- **FAQ `max-height: 300px` hard limit** (line 1119) — if answer content grows beyond this, it will clip. Would need dynamic height measurement to fix.
- **`showToast()` needs `#toast-container` in DOM** — if `base.css` is removed, toasts won't render (`utils.js` lines 56–73).
- **Image files split across two folders** — webpage images (hero, service cards, about, testimonial) live in `pics/Webpage/`. Bath salts product photos live in `pics/` root. GitHub Pages is Linux (case-sensitive) — paths must match exactly.
- **Sage & Lavender is bundle-only** — the pill has `data-bundle-only="true"`. When selected, JS hides the `.price-single` elements and shows `.bundle-only-note`. Do not remove this without updating inventory first.
- **Bath salts section uses a swappable product image, not a video** — `#bath-salts-product-img` src swaps on pill click via `initScentSelector()` in `app.js`. Each pill has `data-img="..."` and `data-link="..."` — clicking a pill swaps the image AND updates `#order-btn` href to that scent's Stripe link. White Tea & Lavender currently points to `pics/triplesalt.jpeg` (no individual shot yet).
- **"Monthly Hold" renamed to "Sacred Hold"** on the site. Do not revert — name change is intentional.
- **10% Lavender Moon discount removed** — was never confirmed with Dalena, removed from site entirely. Do not add back without explicit confirmation.
- **Old combined Stripe link is dead** — `14A5kCchb3usedodqRcbC00` (had both products) is archived. All 6 active links are in Data Schema above.

---

## Project

Demo website for Salvia Lion (Nancy's pen name) — a spiritual healer offering Reiki, tarot guidance, and energy clearing. Built in SSP as a 4-file static site. Not live yet — holding until Salvia is ready.

## Stack

| Layer  | Tech                        |
| ------ | --------------------------- |
| UI     | HTML + CSS + Vanilla JS     |
| Fonts  | Cormorant Garamond (headlines), Lato (body) — Google Fonts |
| Shared | base.css inlined into style.css (no longer imported), utils.js |

## Files

| File         | Purpose                            |
| ------------ | ---------------------------------- |
| index.html   | Full site structure, 8 sections    |
| style.css    | Deep midnight indigo + gold theme  |
| app.js       | Carousel, tilt, magnetic, reveal   |
| utils.js     | Copied from shared/utils.js        |

## Design

- Background: deep black `#07090c`
- Primary accent: teal `#14b8a6` — borders, buttons, marquee, nav
- Secondary accent: purple `#8b5cf6` / lavender `#a78bfa` — em highlights, step numbers, about card border, hero glow
- Font: Cormorant Garamond (headlines, light weight 300), Lato (body)
- No uppercase on headlines — removed to feel soft, not sporty
- Effects: scroll reveal, 3D card tilt, magnetic buttons, animated gradient CTA, horizontal drag scroll

## Sections

1. Nav — Salvia Lion logo, links (About, Services, Shop, How It Works, Stories), ☀️/🌙 theme toggle, Reach Out Now button. Mobile: hamburger menu with full-screen overlay
2. Hero — "Leave feeling loved, comforted, and hopeful" — Spirit Lion image below text on mobile (mix-blend-mode: normal on mobile, screen on desktop dark)
3. Teal marquee strip — 12 items including Moon Ceremonies + Space Clearing
4. About Salvia — NO banner photo (removed). Meet Salvia eyebrow, two-column (story left, Salvia's photo + why card right), "Why she does this" card full-width horizontal below. Profile photo: 75% width, height: auto, no crop
5. Services — "Three paths to peace": 3 cards (Reiki, Tarot, Energy & Tools). Pet Reiki was pulled out into its own section (see #7) so the Bath Salts shop can sit directly under the tools/services
6. **Bath Salts Shop** — product image left, product info right. 3 interactive scent selector pills (purple). Pricing: $10 single / $24 bundle of 3. Order button → Stripe
7. **Pet Reiki** — standalone section (`#pets-section`), single centered service card (Distance Reiki for Pets, $66.66). Sits between Bath Salts and Membership
8. Membership — "The Sacred Hold" (`#membership`), moved below Pet Reiki so the individual offerings come before the bundle
9. Testimonials — 3 real (Cal, Vikki, Rosemary), 4 placeholders — auto-advances, prev/next arrow controls, Cal has photo
10. How It Works — 3 steps with Salvia's real before/during/after process (from Q8)
11. FAQ — 6 questions accordion, uses Salvia's real words
12. CTA — "There's a reason you were led here" + Salvia's Q12 quote
13. Footer — name, tagline, wellness disclaimer

**Section order (2026-05-31):** Nav → Hero → Marquee → About → Services (3 cards) → Bath Salts → Pet Reiki → Membership → Testimonials → How It Works → FAQ → CTA → Footer

## About Nancy

- **Credential: Certified Reiki Master (Level 3/4)** — the highest level of Reiki training. Can teach and attune others but does not want to. This is a key credibility signal — use it near pricing everywhere.
- Offers: Reiki (hands-on + distance), tarot, chakra balancing, aura cleansing, breathwork, sage/smudging, space clearing, Epsom salt baths, meditation, visualization, journaling prompts, crystals (amethyst, black tourmaline, rose quartz, selenite), full moon + new moon ceremonies
- **Distance Reiki for pets** — confirmed 2026-04-27. She's done several sessions, clients love it. Pricing confirmed: **$66.66 per session** (angel number, balance and harmony). Added as 4th service card on site. Needs a real pet photo to replace Books.jpeg placeholder. She's willing to film video content for it (on a calm pet, not Bruce — her own pet who doesn't like it).
- Spirit animal: male lion
- Core message: people leave feeling loved, comforted, peaceful, and hopeful
- She sympathizes deeply with clients — most come to her feeling lost
- She wants people to feel heard, understood, validated, and hopeful for the future
- Not business-focused — service and heart-led approach

## Client Discovery Questions

30 questions across 5 sections of 6. Used to gather copy for the real site once Nancy is ready.

| Section             | Questions |
| ------------------- | --------- |
| The Opening 6       | 1–6       |
| Her Story           | 7–12      |
| Her People          | 13–18     |
| Her Services & Tools| 19–24     |
| Her Presence & Brand| 25–30     |

**Status:** Opening 6 fully answered. Her Story (Q7–Q12) sent. Q7 answered.

### The Opening 6 (sent)

**Q1: What have you personally been through that makes you feel called to do this kind of work?**
> "I remember at my last job, I was getting intense headaches and anxiety attacks. Things I didn't really experience with any other careers or experiences. No medicine or doctor could help me at the time. As a last resort, I went to a Reiki master for a session. My headaches started dissipating and my anxiety attacks became less frequent. That session shifted my entire life's trajectory spiritually. It took some time to figure it out but I'm confident enough now to know peoples' energies and anxiousness were affecting me at my last job. I didn't know how to clear energy and not absorb energy at the time. That one reiki session opened up a whole new world for me and I believe it will continue to do so for others like me in due time."

**Q2: Why do you want to help people heal?**
> "Life's not easy but that doesn't mean you have to make it harder for yourself. I'd liked to share the knowledge and experiences I've gained that I thought were effective for me for others who are also hoping to realign with their truth. A healed person will absolutely be able to affect those around them — creating a ripple effect. I'd liked to think creating that ripple effect will eventually come back around to help those around me that I wasn't able to help in some way or another."

**Q3: What comes up for you when you think about putting your healing gift out there?**
> "That if I only reach 1 person, that's enough, that's plenty."
> *(Note: Added to site as a pull quote in the About section)*

**Q4: If you had 10 minutes this week, would it feel easier to write a few sentences about why you do what you do, or just list your favorite tools like crystals and Epsom salt?**
> "Favorite tools/rituals."
> *(Note: She finds it easier to list tools than write paragraphs — use that when asking for content. Full confirmed tool list: Reiki, tarot, chakra balancing, aura cleansing, breathwork, sage/smudging, Epsom salt baths, meditation, visualization, journaling, crystals. Energy Clearing card updated on site.)*

**Q5: What would make it easier for you to take that first step — would you want someone in your corner, or do you prefer to move at your own pace?**
> "I normally like to go at my own pace, usually when something/someone inspires me. I'm still looking for a mentor in my field."

**Q6: How do you like to be reminded to follow through on something — alarm, someone texting you, or something else?**
> "I usually calendar things to remind myself but if it's an event with someone else, friend following up is always welcomed."
> *(Note: Operational — follow up with a friend-style check-in, not a hard push)*

## Copy Rule

Every answer Nancy gives goes directly onto the site using her exact words — lightly edited for readability only (tighten, don't change meaning or voice). No invented copy.

## Monthly Membership — The Monthly Hold

Added 2026-04-17. Idea from Dalena.

**Package:** 4 distance Reiki sessions + 1 monthly card pull + 4 weekly card pulls + 4 bath salt bags (shipped or local pickup)

**Pricing:**
- Founding member rate: $444/month — first 3 clients, locked in for life (444 = angel number, matches 4x4x4 package)
- Standard rate: $668.68/month

**Sessions:** Distance Reiki via scheduled time window (not Zoom call) — client relaxes at home, Salvia runs the session at agreed time, sends debrief + chakra notes by email after

**Bath salts delivery:** Both shipping and local pickup offered

**CTA:** "Join the Waitlist" button — emails Lionsalvia@gmail.com?subject=Monthly Hold Waitlist

**Section location:** After the Pet Reiki section in index.html (order: Services → Bath Salts → Pet Reiki → Membership)

## Status — 2026-04-19

- **LIVE** at https://cal-zentara.github.io/salvia-lion/ (Cal-Zentara GitHub account)
- Pen name confirmed: **Salvia Lion** — all "Spirit Nancy" / "Nancy" references updated throughout
- Full audit completed and fixed: mobile hamburger nav, theme persistence (localStorage), aria-labels, dead CSS removed, base.css inlined
- About banner photo (EsponSalt.jpeg) removed — section starts directly with "Meet Salvia" eyebrow
- Energy Clearing service card updated from Sage.avif → EsponSalt.jpeg
- Profile photo: full image shown (no crop), 75% width, height auto
- Theme preference persists on refresh via localStorage key `sl-theme`
- CTA email placeholder: Lionsalvia@gmail.com — needs real email before go-live
- **Bath salts shop section added** — Video.mp4 generated via Kie.ai (Veo 3.1), pricing $10/$24 bundle, 3 scent selector buttons
- **Bath salt product details:** 3.1oz / 88g, scents: White Tea Lavender / Neroli Eucalyptus / Sage Lavender, ingredients: baking soda, corn starch, Epsom salt, jojoba oil, vitamin E, essential oils, SLSA
- **Mobile lion fixed** — lion now shows below hero text on mobile, mix-blend-mode: normal on mobile (screen on desktop)
- **Bath salts copy updated (2026-04-15)** — Nancy provided new description: "crafted to not only cleanse and purify your energy but also charged with intentions to aid in recovery and healing. Perfect for after a long week at work, crowded places, or an intense workout." Replaced old placeholder copy in index.html:190
- **Physical stamp ordered (2026-04-19)** — RubberStamps.net order #5486467, 3x3.5 wood stamp + ink pad, $57.25 total. Stamp image: `pics/lion_stamp_v5.png` (pencil sketch conversion). Ships 5–10 days. Bill Nancy $57.25.
- **Contact email updated** — All buttons now point to Lionsalvia@gmail.com (was placeholder)
- **Pricing live on site** — Reiki/Tarot: 30 min $88.88 / 60 min $168.88. Monthly Hold: $444 founding (3 spots) / $668.68 standard. Bath salts: $10 single / $24 bundle
- **444 angel number** — Nancy chose $444 for founding rate because the package is 4 sessions + 4 card pulls + 4 bags
- **Reiki Intake PDF built (2026-04-19)** — 2-page PDF at `Salvia_Lion_Reiki_Intake_Form.pdf`. Page 1: About Holy Fire® Reiki + what to expect. Page 2: client intake form + liability waiver + signature. Built with Python/ReportLab (`make_form.py`). Dark purple `#1E0040` headers, lion stamp image in header.
- **Digital signing** — Researched options. Recommendation: **PandaDoc free plan** (60 docs/year, upload exact PDF, client signs in browser, no account needed, signed copy auto-emailed). Nancy needs to create account at pandadoc.com with Lionsalvia@gmail.com first.

## Pending Before Go-Live
- Salvia's approval of her profile photo on the live site
- 1–2 more real testimonials
- ~~Real payment/order link for bath salts — Stripe setup pending~~ ✅ Stripe activated 2026-05-31, all links live
- Send Her People questions (Q13–18) when timing is right
- ⏸️ PandaDoc digital signing — ON HOLD per Cal (2026-05-31), do not action until he says so

## How Nancy Works (operational notes)
- Goes at her own pace — don't push, let inspiration drive her
- Easier to list things than write paragraphs — ask in list format
- Responds well to friend-style follow-ups, not hard reminders
- Still looking for a mentor in her field

## Her Story Answers (Q7–12)

**Q7: Who is the kind of person that needs you most — what are they going through when they find you?**
> "In the past, I've noticed that people barely starting their spiritual journey finds their way to me. They're excited and afraid at the same time. Excited for their newly discovered chapter but also a bit afraid of the many unknowns and variables associated with the new chapter. They usually benefit from information on protection, cleansing, mindfulness."
*(Note: "Excited and afraid at the same time" + "newly discovered chapter" = real client language — use on site)*

**Q8: What happens in a session — is it different or the same setup every time?**
> "Before session, I like to meditate and ground myself and ask my guides for help. During session, I like to call in my client's guides so we're all working together. I make note of everything — feeling, sensation, thought, visuals that comes up during session. After the session, I reach out and ask how they feel, if they noticed anything during session, debrief. It is similar from session to session. The cards pulled are usually summarized and sent in an email along with information on the different chakras that came up during session."
*(Note: This is the real How It Works content — before/during/after structure. Use to rewrite the 3 steps section.)*

**Q9: What do people say to you after?**
> "They usually say they feel relaxed or sleepy."

**Q10: What do you wish more people understood about energy and how it affects them daily?**
> "Pets are also energetic beings and having a dog or a cat that goes outside helps pet parents ground their energy. If you are used to working in a stressful or crowded environment, it's also important to know how to cleanse your physical and energetic body of other people's energy before you step inside your sanctuary."
*(Note: Unique insight — could be a standalone section or blog post. Very relatable.)*

**Q11: How did you know you were ready to help others — not just heal yourself?**
> "When I gave people information on cleansing, clearing, and protection and it resonated for them or helped them in some way — that's when I knew I wanted to help people."
*(Note: Good for About section — shows she didn't decide to help, she was pulled into it by results.)*

**Q12: What would you say to someone who is curious but skeptical — who wants to believe but isn't sure?**
> "There has to be a reason why you were led to try this (reiki or a reading). Why not see what comes up for you and the reader and decide how you feel about it after."
*(Note: Perfect CTA copy — non-pushy, meets skeptics where they are.)*

---

## Stamp Order — 2026-04-19

Ordered via RubberStamps.net. Cal paid upfront — bill Nancy $57.25.

| Field | Detail |
|---|---|
| Order Number | 5486467 |
| Date | 2026-04-19 |
| Item 1 | 3x3.5 Rubber Stamp, Rich Walnut Handle — $30.95 |
| Item 2 | All-Purpose Large 4x7" Black Stamp Pad — $15.95 |
| Subtotal | $46.90 |
| Tax | $3.40 |
| Shipping | $6.95 (First-Class Mail, 5–10 business days) |
| **Grand Total** | **$57.25** |
| Payment | Amex *398 |
| Ship To | Christopher D Le, 1773 S Caroleen St, Anaheim CA 92804 |
| Stamp image file | `pics/lion_stamp_v5.png` (pencil sketch conversion of original lion PNG) |

## Bath Salts Marketing — 2026-04-30

### Image Generation Rule (Always Apply)
- **Always generate images at the LOWEST quality/resolution first** (e.g. 1k, low res) unless Cal explicitly asks for higher. Drafts are for picking the concept cheaply; only upscale/re-render at high quality (2k/4k) after Cal approves the one he wants. Do not default to high-res.

### Carousel Design Rules (Always Apply)
- **Lion stamp color: teal and purple — every carousel, no exceptions.** Never charcoal, black, or single-color.
- Light version carousel: cream/ivory background, dark charcoal text, teal + purple lion stamp
- Dark version carousel: deep black (#07090c) background, white/teal text, teal + purple lion stamp

### Etsy Shop — LIVE (2026-06-05)
- **Shop is open:** salvialion.etsy.com (account email Lionsalvia@gmail.com). Paid the one-time $29 Etsy setup fee.
- **Nancy ships from ZIP 92840** (Garden Grove, CA). US-only shipping for now (avoids EU/GPSR compliance).
- **First listing LIVE:** "Reiki Charged Bath Salts..." — $10.00, 10 in stock, made-to-order, auto-renews Oct 5 2026.
  - Processing: Made to order, **5–7 business days** (Nancy's call — 5–7 is standard, 3 is express).
  - Shipping: **Calculated, buyer-pays**, saved profile named **"Bath Salts US"** (reuse for future listings). Item weight 5 oz, size 6×4×2 in.
  - Returns: Simple policy, 30 days, buyer responsible.
  - Variations: custom "Scent" with 3 options (White Tea & Lavender, Neroli & Eucalyptus, Sage & Lavender), photos linked per scent.
  - 13 tags used (reiki bath salts, energy clearing, spiritual bath, empath gift, aura cleansing, bath salt soak, epsom bath salt, cleansing ritual, spiritual gift, self care gift, lavender bath, witchy bath salt, meditation bath).
- **$24 BUNDLE LISTING — LIVE (2026-06-06):** "Reiki Bath Salt Bundle of 3..." $24.00, 10 in stock. Bundle = **one of each scent** (no scent variation/picker — fixed set). Item weight 13 oz. Triple-pack photo as thumbnail. Same "Bath Salts US" shipping profile. Shop now has **2 active listings**.
- **Shop polish done (2026-06-06):** Shop icon = SalviaLionLogo.png (green-circle lion). Tagline = "Reiki-charged bath salts, made by a Reiki Master 🦁". Shop announcement + About story added (Nancy's real Q1 voice). Banner generated via Higgsfield (2 wide 21:9 options saved at `pics/etsy-banner-option1.png` / `option2.png`) — Cal picking one to upload as Big Banner.
- **Copy note:** Bath salts framing is **clear → heal → empower** (Nancy ends sessions empowering). She does NOT position them as "replenishing" — keep that word out of all copy.
- **Amazon = phase 2** (heavier: cosmetic compliance, brand registry, barcodes). Do Etsy reviews first.

### IG Caption Format (Approved)
Nancy approved a long-form caption format — she wants buyers to see exactly which scent they're getting. Full format + example saved in Claude memory: `feedback_salvia-lion-ig-caption-format.md`

**Caption structure:** Hook (her voice) → what it does / who it's for → product list (each scent on own line w/ emoji) → promo note → price + CTA → dots → hashtags

**Pre-orders active now — going live in June.**

---

## Bath Salts Marketing — 2026-04-27

Full roadmap saved at: `C:\Users\Aesth\Desktop\Zentara\Projects\Marketing\bath-salts\salvia-lion-roadmap.md`

### Copy Changes Made (2026-04-27)
- **Eyebrow:** "Available Now" → "Salvia's Handcrafted Blends"
- **Title:** "Handcrafted bath salts" → "Bath salts for people who feel everything"
- **Description:** Rewrote to lead with empath pain point → Reiki credential → outcome ("clear, grounded, lighter")
- **Added:** Ritual instruction line — "Run a warm bath — add the whole bag — set an intention — let the water do the rest." (styled teal italic, `.bath-salts-ritual`)
- **Scents label:** "Choose your scent" → "Pick your blend"
- **Bundle label:** "Bundle of 3 — try every scent" → "Bundle of 3 — one for every kind of week"

### Buyer Research Findings (Reddit + Etsy)
**Who buys:** Empaths and sensitive people ("I absorb others' energy"), spiritual beginners, stressed professionals after hard weeks.

**Why they buy (triggers):**
- Scent is #1 — always lead with it
- Instructions included — "how to use" copy drives conversions
- Maker's story — handmade by a Reiki healer = more powerful than factory-made
- Specific outcomes — not "relax" but "clear, grounded, protected"
- Packaging + presentation signal legitimacy

**Exact buyer phrases to use in copy:**
- "I absorb others' energy"
- "After a long week at work, crowded places"
- "Charged with intentions"
- "Feel grounded, calm, protected"
- "Reset / cleanse / clear my energy"

**Nancy's biggest differentiator:** Nobody on Etsy positions as a practitioner who makes the salts as part of their healing practice. She's a Reiki healer who charges every bag — that's the gap nobody else fills.

### Etsy Competitive Landscape
- Top sellers price: $8–15 single / $20–40 bundle. Nancy's $10/$24 is in the sweet spot.
- Top sellers have 500+ reviews — social proof is the unlock
- Gaps in market: no personal healer backstory, weak video, no distance healing mention
- Nancy's advantages: Reiki credential, Video.mp4, real client testimonials, cross-sell to sessions

### Marketing Roadmap — Skills by Phase
See full roadmap at `Marketing/bath-salts/salvia-lion-roadmap.md`.

**Phase 1 — Now (no Stripe needed):**
1. `/voice-extractor` → document Nancy's real voice from Q&A answers
2. `/reddit-insights` → "spiritual bath salts," "energy clearing," "empath self-care" (needs API key setup at reddit-insights.com)
3. `/cal-content` for SpiritNancy → 10–15 IG post ideas + captions in her voice
4. `/market-social` → 30-day IG content calendar
5. `/testimonial-collector` → ask Reiki/tarot clients this week
6. `/kie-video` → short Reels content

**Phase 2 — When Stripe is live:**
1. `/page-cro` → audit bath salts section for conversion friction
2. `/popup-cro` → exit-intent email capture
3. `/cal-ai-findability` → score Nancy's AI search visibility
4. `/schema-markup` → tag products with price/scents for Google rich results
5. `/market-emails` → nurture sequence: intro → education → buy
6. `/pricing-strategy` → validate $10/$24, test bundle psychology

**Phase 3 — Scaling:**
1. `/ad-creative` + `/paid-ads` → target Reiki/tarot/chakra audiences on IG/Meta
2. `/cold-outreach-sequence` → yoga studios, spiritual coaches, wellness bloggers
3. `/referral-program` → "gift a friend" system for first buyers

### Etsy as a Channel
Worth opening an Etsy shop once Nancy has 5–10 reviews and product photos. Use it as a second discovery channel — Etsy buyers are already searching and ready to buy. Run IG to build brand, Etsy to capture search traffic.

---

## Content Resource — Salvia's Words & Knowledge
*Everything pulled directly from conversations with Nancy. Use her exact words whenever possible.*

### Reiki Symbols She Uses

| Symbol | Used for | Nancy's words |
|---|---|---|
| Cho Ku Rei | Every session — power symbol | "The same ones I use in my session" |
| Sei He Ki | Every session — mental/emotional symbol | "The same ones I use in my session" |
| Hon Sha Ze Sho Nen | Distance Reiki symbol | "Used to send reiki far away" |

- She uses **Cho Ku Rei and Sei He Ki in every session** — including to charge the bath salts
- Hon Sha Ze Sho Nen is what makes distance Reiki possible — this is the "how" behind remote sessions
- Bath salts are charged using these actual symbols, not just general intention

### The 5 Reiki Precepts (Core Principles)
*Nancy: "These are the core principles for reiki that every student knows...if you want to make a future post about reiki"*

1. Just for today, I will not be angry *(Ikaru na)*
2. Just for today, I will not worry *(Shinpai suna)*
3. Just for today, I will be grateful *(Kansha shite)*
4. Just for today, I will do my work honestly *(Gyo o hakame)*
5. Just for today, I will be kind to every living thing *(Hito ni shinsetsu ni)*

### Master vs Practitioner — In Her Words
- "Besides the experience, a master has taken more advanced classes and they can initiate and train others. Their energy is going to be different from a practitioner who has only done level 1."
- "If I ever paid for Reiki, I would go to a master. Whereas I can probably find a practitioner who needs to do Reiki on 10 people because of their class for free."
- She CAN teach and attune others — but doesn't want to. She wants to heal, not train.
- This distinction directly justifies the $444 / $168.88 pricing — use it near prices.

### Content Angles (Ready to Film)
1. **Master vs practitioner** — the energy difference, why it matters, why she charges what she charges
2. **The two symbols** — Cho Ku Rei + Sei He Ki, what they do, she draws them before every session
3. **Distance Reiki explained** — Hon Sha Ze Sho Nen, how healing travels across any distance
4. **Bath salts ritual** — she charges each bag with Reiki symbols before it ships. Nobody else does this.
5. **The 5 Precepts** — educational, shareable, hits the spiritual audience perfectly
6. **"She doesn't want to teach"** — personal angle, makes her feel real and heart-led

### Bath Salts Charging (Confirmed 2026-04-29)
Nancy confirmed she uses Cho Ku Rei and Sei He Ki to charge every bath salt bag with intentions. This is the actual Reiki practice behind the product — not a marketing phrase. Use this in content and copy.

### Nancy's Teaching Handouts (received 2026-05-31)
*Nancy sent two of her own beginner handouts. Her exact words — verbatim. Great source for blog posts / IG carousels / an on-site "Learn" section. She tagged them: Protection = "a great post for beginners," Crystal grids = "for the crystal users."*

> **GUIDING ANGLE for beginner/Protection content (Cal, 2026-05-31):** Frame protection as a *skill most people simply never learned* — NOT as empaths being helpless victims who "absorb everyone's energy." The empowering truth: you're not doomed to feel drained; once you learn to protect your own energy, you stop soaking it up. This positions Salvia as a teacher of a skill, not a source of sympathy. Tie every "aura / energy" explanation back to "and here's how you take control of it." Avoid victim framing.
>
> Working plain-language definition of *aura* (our words, beginner-friendly): "Your aura is the energy field around you. Most people never learn to protect it — so they walk around picking up everyone else's energy without realizing it. Learning to protect your own changes everything."

**PROTECTION**
> Importance: It is not only important to protect yourself when entering the spiritual world, it is also important to protect yourself in your day to day Earthbound world. All people have auras which can be under attack, as we open our auras to connect we open the ability to be attacked from all sides, thus opening us up for an energy dip, illness, etc. It is important to be conscious of this and protect ourselves on a daily basis.
>
> **Ways to protect yourself:**
> - Meditation
> - Grounding
> - Opening and closing of your chakras
> - Calling in your guides, archangels, angels and higher self
> - Visualizing the shower water removing any unneeded energy from you and seeing it go down the drain, then picture the water being drops of white light that washes protection over your body
> - Crystals, stones, spiritual medals
> - Requesting those only of the light being allowed to work through you
> - Recognizing and removing yourself from a lower energy room
> - Reiki attunements

**CREATING ENERGY GRIDS USING CRYSTALS**
> Grids are created to (a) protect a space from unwanted energy entering an area and (b) to energize the space within the grid with certain qualities.
>
> **Directions:**
> 1. Select 3 crystals of the same kind (e.g. 3 clear quartz, 3 rose quartz, 3 tiger eyes). Size does not matter — they can be very large or small based on the area you will be setting them in. The grid can be done without crystals, however the crystals tend to anchor the energy longer.
>
> When choosing your crystal, you may want to select them on their metaphysical properties and what your desired outcome is based on. Some samples:
> - **All purpose** — Clear quartz (set the crystal's intention for what you want)
> - **Healing** — Aventurine, Malachite
> - **Love** — Rose Quartz
> - **Protection** — Citrine, Hematite, Black Tourmaline
> - **Psychic Work** — Sodalite, Lapis Lazuli, Amethyst
>
> 2. Place three different crystals in the shape of an equilateral triangle (or as close as possible) around the area you wish to protect or empower. The crystals do not need to be on the same level and they do not need to be visible.
> 3. Stand outside of the triangle between 2 of the crystals. It does not matter which stones you stand between.

## Booking Calendar

**Nancy's requirements (2026-04-29):**
- 2 sessions per week max
- 1 weekend day + 1 weekday — flexible on exact times, client and Nancy work it out
- Weekly cap: once 2 sessions are booked that week, no more slots show

**Tool decision:** Google Calendar Appointment Schedule (free, no third-party needed).

**Status:** ✅ Booking page created 2026-04-30. Timezone fixed to Pacific Time 2026-05-25.

**Next action:** Embed Nancy's booking link on site once she shares it. Also fix timezone + description on desktop.

---

## Next Steps
- ~~**Bill Nancy $57.25** for stamp order #5486467~~ ✅ Done 2026-04-29
- ~~Bath salts Reel~~ ✅ Built + approved 2026-04-30 — Nancy posts 2026-05-01 (full moon)
- ~~Set up booking calendar~~ ✅ Google Calendar Appointment Schedule created 2026-04-30
- ~~Fix booking page timezone (GMT → Pacific) + description~~ ✅ Done 2026-05-25
- ~~Nancy to share booking link → embed on site as "Book a Session" button~~ ✅ Done 2026-05-25 — https://calendar.app.google/zyUNUM2JjPNhdqrD8
- Confirm 10% Lavender Moon discount with Dalena before site goes live
- Nancy opens business checking account → connect to Stripe for bath salt payments
- ⏸️ ON HOLD (per Cal, 2026-05-31): Nancy creates PandaDoc account (Lionsalvia@gmail.com) → upload intake PDF → set signature field → embed link on site
- Salvia approves her profile photo on live site
- Collect 1–2 more real testimonials
- Send Her People questions (Q13–18) when timing feels right
