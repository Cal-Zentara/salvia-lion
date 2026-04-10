# CLAUDE.md — Spirit Nancy

## Project

Demo website for Salvia Lion (Nancy's pen name) — a spiritual healer offering Reiki, tarot guidance, and energy clearing. Built in SSP as a 4-file static site. Not live yet — holding until Salvia is ready.

## Stack

| Layer  | Tech                        |
| ------ | --------------------------- |
| UI     | HTML + CSS + Vanilla JS     |
| Fonts  | Cormorant Garamond (headlines), Lato (body) — Google Fonts |
| Shared | ../shared/base.css, utils.js |

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

1. Nav — Spirit Nancy logo, links (About, Services, How It Works, Stories), ☀️/🌙 theme toggle, Reach Out Now button
2. Hero — "Leave feeling loved, comforted, and hopeful" — Spirit Lion image bottom right (mix-blend-mode: screen on dark, multiply on light)
3. Teal marquee strip — 12 items including Moon Ceremonies + Space Clearing
4. About Nancy — banner photo (EsponSalt.jpeg, dark overlay), Meet Nancy eyebrow below photo, two-column (story left, Nancy's photo + why card right), "Why she does this" card full-width horizontal below
5. Services — 3 cards with photos (Books.jpeg for Reiki, Tarot Cards for Tarot, Sage for Energy Clearing)
6. Testimonials — 2 real (Cal + Vikki), 4 placeholders — auto-advances, prev/next arrow controls, Cal has photo
7. How It Works — 3 steps with Nancy's real before/during/after process (from Q8)
8. FAQ — 6 questions accordion, uses Nancy's real words
9. CTA — "There's a reason you were led here" + Nancy's Q12 quote
10. Footer — name, tagline, wellness disclaimer

## About Nancy

- Offers: Reiki (hands-on + distance), tarot, chakra balancing, aura cleansing, breathwork, sage/smudging, space clearing, Epsom salt baths, meditation, visualization, journaling prompts, crystals (amethyst, black tourmaline, rose quartz, selenite), full moon + new moon ceremonies
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

## Status — 2026-04-09

- Site functionally complete, not live — holding until Nancy picks her pen name and is ready
- Light mode + dark mode toggle added — Nancy to choose preferred theme
- All Q1–Q12 answered and live on site
- How It Works rewritten with Nancy's real process (Q8)
- CTA updated with Nancy's Q12 copy
- FAQ section added with 6 questions using Nancy's real words
- Photos added: EsponSalt (about banner), Reiki.webp, Sage.avif, Books.jpeg, Spirit Lion (hero), Nancy profile photo (about section), Cal testimonial photo
- Spirit Lion: `Mystical lion with glowing energy trails.png` — mix-blend-mode: screen (dark) / multiply (light)
- 2 real testimonials: Cal + Vikki. Cal has photo (`Testimonial1.jpeg`)
- Buttons changed from "Book a Session" → "Reach Out Now"
- All emojis removed except ☀️/🌙 theme toggle

## Pending Before Go-Live
- Pen name confirmed: **Salvia Lion** — site updated
- Real booking link (Calendly or email)
- Her photo approval
- Pricing (optional)
- 1–2 more real testimonials

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

## Next Steps
- Wait for Nancy's pen name — update site name + branding when confirmed
- Send Her People questions (Q13–18) when timing is right
- Deploy when Nancy is ready
