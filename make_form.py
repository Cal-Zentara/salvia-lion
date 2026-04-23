from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
    HRFlowable, Table, TableStyle, Image as RLImage, PageBreak, KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

OUT  = r'C:\Users\Aesth\Desktop\Salvia_Lion_Reiki_Intake_Form.pdf'
LION = r'C:\Users\Aesth\Desktop\Zentara\Projects\SmallProjects\SpiritNancy\pics\lion_pdf.png'

PURPLE = HexColor('#1E0040')
LPURPLE = HexColor('#EDE7F6')
BLACK  = HexColor('#1a1a1a')
GREY   = HexColor('#aaaaaa')
WHITE  = HexColor('#ffffff')
W = 7.8 * inch

doc = SimpleDocTemplate(OUT, pagesize=letter,
    rightMargin=0.6*inch, leftMargin=0.6*inch,
    topMargin=0.5*inch, bottomMargin=0.5*inch)

# ── Styles ───────────────────────────────────────────────────────
def sty(name, **kw):
    defaults = dict(fontName='Helvetica', fontSize=9.5, textColor=BLACK,
                    spaceBefore=0, spaceAfter=0, leading=13)
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)

title_s  = sty('t',  fontName='Helvetica-Bold', fontSize=22, textColor=PURPLE, alignment=TA_CENTER)
sub_s    = sty('su', fontSize=9, textColor=PURPLE, alignment=TA_CENTER)
ftitle_s = sty('ft', fontName='Helvetica-Bold', fontSize=14, textColor=PURPLE, alignment=TA_CENTER, spaceBefore=6, spaceAfter=6)
sh_s     = sty('sh', fontName='Helvetica-Bold', fontSize=10, textColor=WHITE)
label_s  = sty('lb', fontName='Helvetica-Bold', fontSize=8.5, textColor=BLACK)
body_s   = sty('bo', fontSize=8.5, textColor=BLACK, leading=12)
italic_s = sty('it', fontName='Helvetica-Oblique', fontSize=8.5, textColor=HexColor('#333333'), leading=12, spaceBefore=3, spaceAfter=4)
bullet_s = sty('bu', fontSize=8.5, textColor=BLACK, leading=13, leftIndent=12, firstLineIndent=-10, spaceBefore=2)
waiver_s = sty('wv', fontSize=8, textColor=BLACK, leading=12)
priv_s   = sty('pr', fontSize=7.5, textColor=HexColor('#444444'), leading=11)
minor_s  = sty('mn', fontName='Helvetica-Oblique', fontSize=7.5, textColor=HexColor('#888888'), spaceBefore=2)

def sp(n=4): return Spacer(1, n)

def sec(text):
    t = Table([[Paragraph(text, sh_s)]], colWidths=[W])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),PURPLE),
        ('LEFTPADDING',(0,0),(-1,-1),8), ('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),4),  ('BOTTOMPADDING',(0,0),(-1,-1),4),
    ]))
    return t

def lfield(label, lw, fw):
    t = Table([[Paragraph(label, label_s), '']], colWidths=[lw, fw])
    t.setStyle(TableStyle([
        ('LINEBELOW',(1,0),(1,0),0.5,GREY),
        ('TOPPADDING',(0,0),(-1,-1),3), ('BOTTOMPADDING',(0,0),(-1,-1),1),
        ('VALIGN',(0,0),(-1,-1),'BOTTOM'),
    ]))
    return t

def wline(sb=11):
    return HRFlowable(width='100%', thickness=0.5, color=GREY, spaceBefore=sb, spaceAfter=2)

def header():
    """Shared header: lion left, title right."""
    lion = RLImage(LION, width=1.25*inch, height=0.83*inch)
    rows = [
        [lion, Paragraph('Salvia Lion', title_s)],
        ['',   Paragraph('Reiki &bull; Tarot &bull; Energy Healing', sub_s)],
    ]
    t = Table(rows, colWidths=[1.45*inch, 6.35*inch])
    t.setStyle(TableStyle([
        ('SPAN',    (0,0),(0,1)),
        ('VALIGN',  (0,0),(0,1),'MIDDLE'),
        ('VALIGN',  (1,0),(1,1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),0), ('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    return t

# ════════════════════════════════════════════════════════════════
# PAGE 1 — About & What to Expect
# ════════════════════════════════════════════════════════════════
story = []
story.append(header())
story.append(HRFlowable(width='100%', thickness=2, color=PURPLE, spaceBefore=5, spaceAfter=5))
story.append(Paragraph('Welcome to Your Reiki Session', ftitle_s))

# About Holy Fire Reiki
story.append(sec('About Holy Fire\u00ae Reiki'))
story.append(sp(5))
story.append(Paragraph(
    'Salvia Lion practices <b>Holy Fire\u00ae Reiki</b> \u2014 a form introduced by the International Center '
    'for Reiki Training (ICRT) that combines traditional Usui Reiki with a powerful Holy Fire energy. '
    'This energy is sourced from a higher level of consciousness and is associated with unconditional love. '
    'It provides deep healing, purifies, and empowers, often bringing feelings of safety, love, and peace. '
    '<b>Holy Fire Reiki is non-religious</b> and works continuously in the background, spontaneously '
    'healing issues as they arise. All sessions with Salvia Lion are conducted via <b>distance Reiki</b> \u2014 '
    'you relax at home during a scheduled time window while Salvia runs your session remotely.',
    italic_s))
story.append(sp(8))

# What to Expect
story.append(sec('What to Expect During Your Session'))
story.append(sp(5))
story.append(Paragraph(
    'Every person\u2019s experience is unique. Below are common sensations clients report \u2014 '
    'none of them are cause for concern. You may experience some, all, or none of these:',
    body_s))
story.append(sp(6))

experiences = [
    ('Deep Relaxation',         'A calm, heavy, trance-like state. Some clients fall into a deep, restful sleep \u2014 this is completely normal.'),
    ('Energy Sensations',       'Warmth, coolness, tingling, or a gentle buzzing feeling throughout the body.'),
    ('Emotional Release',       'Feelings of peace, joy, or even tears as energy blockages are cleared. This is a healthy part of the process.'),
    ('Visual Phenomena',        'You may see colors, shapes, or soft light behind your closed eyes.'),
    ('Sense of Extra Presence', 'Some clients feel a sense of extra hands or a gentle movement. This is the energy working \u2014 nothing to worry about.'),
    ('Feeling Nothing',         'Also completely normal. The energy is still working on a subtle level even if you don\u2019t feel it.'),
    ('Clarity & Insight',       'Sudden feelings of mental clarity, peace, or emotional lightness after the session.'),
]

for title, desc in experiences:
    story.append(Paragraph(f'\u2022 <b>{title}:</b> {desc}', bullet_s))

story.append(sp(8))
story.append(sec('After Your Session'))
story.append(sp(5))
story.append(Paragraph(
    'Salvia will reach out after your session to check in. You will receive a debrief by email including '
    'a summary of what came up, any card pull results, and notes on the chakras that were active during '
    'your session. Drink plenty of water afterward \u2014 hydration supports the integration process.',
    italic_s))

story.append(sp(10))
story.append(Paragraph('\u2014 Please turn over to complete your intake form \u2014',
    sty('pt', fontSize=8, textColor=HexColor('#888888'), alignment=TA_CENTER, fontName='Helvetica-Oblique')))

# ════════════════════════════════════════════════════════════════
# PAGE 2 — Intake Form + Consent
# ════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(header())
story.append(HRFlowable(width='100%', thickness=2, color=PURPLE, spaceBefore=5, spaceAfter=5))
story.append(Paragraph('Reiki Client Intake &amp; Consent Form', ftitle_s))

# Client Info
story.append(sec('Client Information'))
story.append(sp(5))
story.append(lfield('Name (Please Print):', 1.9*inch, 5.9*inch))
story.append(sp(2))
story.append(lfield('E-mail:', 0.65*inch, 7.15*inch))
story.append(sp(2))
story.append(lfield('Phone:', 0.6*inch, 7.2*inch))
story.append(sp(2))

cit = Table([[
    Paragraph('City:', label_s), '',
    Paragraph('State:', label_s), '',
    Paragraph('Zip:', label_s), ''
]], colWidths=[0.45*inch, 2.9*inch, 0.65*inch, 1.1*inch, 0.45*inch, 2.25*inch])
cit.setStyle(TableStyle([
    ('LINEBELOW',(1,0),(1,0),0.5,GREY), ('LINEBELOW',(3,0),(3,0),0.5,GREY), ('LINEBELOW',(5,0),(5,0),0.5,GREY),
    ('TOPPADDING',(0,0),(-1,-1),3), ('BOTTOMPADDING',(0,0),(-1,-1),1),
    ('VALIGN',(0,0),(-1,-1),'BOTTOM'),
]))
story.append(cit)
story.append(sp(2))

ec = Table([[
    Paragraph('Emergency Contact:', label_s), '',
    Paragraph('Phone:', label_s), ''
]], colWidths=[1.6*inch, 3.4*inch, 0.65*inch, 2.15*inch])
ec.setStyle(TableStyle([
    ('LINEBELOW',(1,0),(1,0),0.5,GREY), ('LINEBELOW',(3,0),(3,0),0.5,GREY),
    ('TOPPADDING',(0,0),(-1,-1),3), ('BOTTOMPADDING',(0,0),(-1,-1),1),
    ('VALIGN',(0,0),(-1,-1),'BOTTOM'),
]))
story.append(ec)
story.append(sp(2))
story.append(lfield('How did you hear about my services?', 2.75*inch, 5.05*inch))
story.append(sp(6))

# Session Details
story.append(sec('Session Details'))
story.append(sp(5))

rb = Table([[
    Paragraph('Have you had a Reiki session before?', label_s),
    Paragraph('Yes _____', body_s), Paragraph('No _____', body_s),
    Paragraph('Date of last session:', label_s), ''
]], colWidths=[2.7*inch, 0.75*inch, 0.75*inch, 1.55*inch, 2.05*inch])
rb.setStyle(TableStyle([
    ('LINEBELOW',(4,0),(4,0),0.5,GREY),
    ('TOPPADDING',(0,0),(-1,-1),3), ('BOTTOMPADDING',(0,0),(-1,-1),1),
    ('VALIGN',(0,0),(-1,-1),'BOTTOM'),
]))
story.append(rb)
story.append(sp(5))

story.append(Paragraph('Reason for seeking Reiki &amp; goal for this session:', label_s))
story.append(wline(10))
story.append(wline(10))
story.append(sp(2))

story.append(Paragraph('Do you have any particular area of concern?', label_s))
story.append(wline(10))
story.append(sp(2))

story.append(Paragraph('Additional comments or questions before we begin:', label_s))
story.append(wline(10))
story.append(wline(10))
story.append(sp(6))

# Consent
story.append(sec('Consent &amp; Liability Waiver'))
story.append(sp(5))

waiver_text = (
    'I understand that Reiki (Holy Fire\u00ae style) is a simple, gentle, spiritually-guided energy technique '
    'used for stress reduction and relaxation. I understand that Salvia Lion does not diagnose conditions, '
    'prescribe, or perform medical treatment. Reiki does not take the place of medical or psychological care '
    'and may complement any care I am currently receiving. I understand the body has the ability to heal '
    'itself and that complete relaxation supports this process. I acknowledge that long-term imbalances may '
    'require multiple sessions. By signing below, I voluntarily consent to receive distance Reiki from '
    'Salvia Lion and waive any and all liability claims against Salvia Lion and her practice.'
)
wb = Table([[Paragraph(waiver_text, waiver_s)]], colWidths=[W])
wb.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,-1),LPURPLE), ('BOX',(0,0),(-1,-1),1,PURPLE),
    ('TOPPADDING',(0,0),(-1,-1),6), ('BOTTOMPADDING',(0,0),(-1,-1),6),
    ('LEFTPADDING',(0,0),(-1,-1),8), ('RIGHTPADDING',(0,0),(-1,-1),8),
]))
story.append(wb)
story.append(sp(8))

sig = Table([[
    Paragraph('Signature:', label_s), '',
    Paragraph('Date:', label_s), ''
]], colWidths=[0.8*inch, 4.8*inch, 0.5*inch, 1.7*inch])
sig.setStyle(TableStyle([
    ('LINEBELOW',(1,0),(1,0),0.75,HexColor('#555555')),
    ('LINEBELOW',(3,0),(3,0),0.75,HexColor('#555555')),
    ('TOPPADDING',(0,0),(-1,-1),10), ('BOTTOMPADDING',(0,0),(-1,-1),1),
    ('VALIGN',(0,0),(-1,-1),'BOTTOM'),
]))
story.append(sig)
story.append(Paragraph('(If client is a minor, a parent or guardian must sign)', minor_s))
story.append(sp(6))
story.append(HRFlowable(width='100%', thickness=1, color=PURPLE, spaceBefore=3, spaceAfter=4))
story.append(Paragraph(
    '<b>Privacy Notice:</b> No information about any client will be discussed or shared with any '
    'third party without written consent of the client, or a parent/guardian if the client is under 18.',
    priv_s))

doc.build(story)
print('Saved:', OUT)
