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
| Services (3-card grid) | `index.html` | 140–177 |
| Services styles + card tilt | `style.css` | 479–579 |
| Membership section (Monthly Hold) | `index.html` | 180–237 |
| Membership styles | `style.css` | 581–731 |
| Bath salts shop (video + scent selector) | `index.html` | 240–284 |
| Bath salts styles | `style.css` | 733–871 |
| Testimonials carousel | `index.html` | 286–376 |
| Testimonials carousel styles | `style.css` | 865–995 |
| How It Works horizontal scroll | `style.css` | 996–1057 |
| FAQ accordion | `index.html` | 408–446 |
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

No client-side persistence beyond theme preference. All CTAs are `mailto:` links — no form submission.

- **localStorage key:** `sl-theme` — values `'light'` or `'dark'` (set by theme toggle, `app.js` lines 195–206)
- **Query params:** none
- **API endpoints:** none
- **Primary contact email (all CTAs):** `Lionsalvia@gmail.com`
- **Bath salts order CTA:** `mailto:Lionsalvia@gmail.com?subject=...` (manual email order, Stripe pending)
- **Monthly Hold waitlist CTA:** `mailto:Lionsalvia@gmail.com?subject=Monthly Hold Waitlist`

### Known Gotchas

- **`base.css` is inlined into `style.css`** (lines 1–19) — originally imported from `../shared/base.css`, now local to avoid path issues. `utils.js` is still imported directly from local copy.
- **Hero lion blend mode switches on mobile** — `mix-blend-mode: screen` on desktop (line 265) → `normal` on mobile (line 280). Intentional: screen mode breaks readability on small screens.
- **Hero is `flex-column` on mobile** (line 1403) — lion image moves below text from absolutely-positioned right side on desktop.
- **About photo has no crop** — explicitly `75% width, height: auto` (line 457–458) to preserve full face.
- **Service card `object-position` overrides** — Tarot `center 30%` and Energy Clearing `center 40%` (lines 159, 169) to frame faces correctly.
- **Carousel is hand-rolled** (`transform: translateX`, 100% width per card, lines 40, 877–879) — not a library. Auto-advance uses `setInterval`, no pause-on-hover.
- **Horizontal drag scroll uses multiplier `1.5`** (line 122) — snappier than mouse movement by design.
- **FAQ `max-height: 300px` hard limit** (line 1119) — if answer content grows beyond this, it will clip. Would need dynamic height measurement to fix.
- **`showToast()` needs `#toast-container` in DOM** — if `base.css` is removed, toasts won't render (`utils.js` lines 56–73).

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
5. Services — 3 cards with photos (Books.jpeg for Reiki, Tarot Cards for Tarot, EsponSalt.jpeg for Energy Clearing)
6. **Bath Salts Shop** — Video.mp4 autoplay left, product info right. 3 interactive scent selector pills (purple). Pricing: $10 single / $24 bundle of 3. Order button emails Lionsalvia@gmail.com
7. Testimonials — 3 real (Cal, Vikki, Rosemary), 4 placeholders — auto-advances, prev/next arrow controls, Cal has photo
8. How It Works — 3 steps with Salvia's real before/during/after process (from Q8)
9. FAQ — 6 questions accordion, uses Salvia's real words
10. CTA — "There's a reason you were led here" + Salvia's Q12 quote
11. Footer — name, tagline, wellness disclaimer

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

**Section location:** Between Services and Bath Salts Shop in index.html

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
- **Bath salt product details:** 3.1oz / 88g, scents: White Tea & Lavender / Neroli & Eucalyptus / Chamomile & Lavender, ingredients: baking soda, corn starch, Epsom salt, jojoba oil, vitamin E, essential oils, SLSA
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
- Real payment/order link for bath salts — Stripe setup pending (Nancy needs to open a separate business checking first)
- Send Her People questions (Q13–18) when timing is right
- Nancy to set up PandaDoc account for digital intake form signing

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

## Booking Calendar

**Nancy's requirements (2026-04-29):**
- 2 sessions per week max
- 1 weekend day + 1 weekday — flexible on exact times, client and Nancy work it out
- Weekly cap: once 2 sessions are booked that week, no more slots show

**Tool decision:** Calendly free plan — 1 event type, unlimited bookings, connects to Google Calendar. Free forever for her use case.

**Status:** Not yet set up. Waiting on Nancy to confirm she's ready.

**Next action:** Set up Calendly, embed booking link on site (replace "Reach Out Now" email button or add as second CTA).

---

## Next Steps
- ~~**Bill Nancy $57.25** for stamp order #5486467~~ ✅ Done 2026-04-29
- ~~Bath salts Reel~~ ✅ Built + approved 2026-04-29 — Nancy posts 2026-04-30
- Set up Calendly booking calendar per specs above → embed on site
- Nancy opens business checking account → connect to Stripe for bath salt payments
- Nancy creates PandaDoc account (Lionsalvia@gmail.com) → upload intake PDF → set signature field → embed link on site
- Salvia approves her profile photo on live site
- Collect 1–2 more real testimonials
- Send Her People questions (Q13–18) when timing feels right
