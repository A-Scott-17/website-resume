"""Build the public one-page resume from verified portfolio information."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "resume" / "alexander-scott-resume.pdf"
OUTPUT.parent.mkdir(exist_ok=True)

MAROON = colors.HexColor("#8b1e14")
DARK = colors.HexColor("#35100c")
MUTED = colors.HexColor("#55423e")

styles = {
    "name": ParagraphStyle("Name", fontName="Times-Bold", fontSize=23, leading=26, textColor=MAROON, alignment=TA_CENTER),
    "tag": ParagraphStyle("Tag", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=DARK, alignment=TA_CENTER),
    "contact": ParagraphStyle("Contact", fontName="Helvetica", fontSize=8.7, leading=12, textColor=MUTED, alignment=TA_CENTER),
    "section": ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=9.6, leading=12, textColor=MAROON, spaceBefore=13, spaceAfter=5),
    "role": ParagraphStyle("Role", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=DARK, spaceBefore=5),
    "body": ParagraphStyle("Body", fontName="Helvetica", fontSize=8.9, leading=12.4, textColor=DARK, spaceAfter=3.5),
    "small": ParagraphStyle("Small", fontName="Helvetica", fontSize=8.4, leading=11.7, textColor=MUTED, spaceAfter=2.5),
}


def text(value, style="body"):
    # Keep the public PDF readable in standard PDF fonts and text extractors.
    value = value.translate(str.maketrans({"–": "-", "—": "-", "•": "-", "·": "|"}))
    return Paragraph(value, styles[style])


story = [
    text("Alexander Scott", "name"),
    text("FORMER U.S. MARINE CORPS SERGEANT  |  COMPUTER INFORMATION SYSTEMS STUDENT", "tag"),
    text("Charleston, SC  ·  AlexEScott00@gmail.com  ·  (309) 370-8891", "contact"),
    text("linkedin.com/in/alexescott  ·  <link href='https://github.com/A-Scott-17' color='#55423e'>github.com/A-Scott-17</link>  ·  a-scott-17.github.io/website-resume/", "contact"),
    Spacer(1, 7),
    HRFlowable(width="100%", thickness=1.2, color=MAROON),
    text("PROFILE", "section"),
    text("Former U.S. Marine Corps Sergeant with five years of service (July 2019–July 2024), including security operations and personnel leadership at the White House Communications Agency. College of Charleston Computer Information Systems student seeking a Summer 2027 internship in technical security, cybersecurity, IT, information systems, or defense technology."),
    text("SECURITY EXPERIENCE", "section"),
    text("White House Communications Agency  |  Security Operations and Leadership  |  Jan 2021–Dec 2022", "role"),
    text("• Progressed from Post Stander (Jan–Apr 2021) to Team Leader (~4 personnel, Apr–Aug 2021), Squad Leader (~12, Aug 2021–May 2022), and Section Leader/NCOIC (up to 27, May–Dec 2022)."),
    text("• As Sergeant of the Guard, supervised 16+ posted Marines and managed shift-level security operations across three compounds simultaneously, including post assignments, access-control issues, personnel accountability, incident response, and reporting."),
    text("• Presented monthly security and readiness updates to WHCA leadership and interagency partners. Planned and instructed security and emergency-response training events for groups of 30+ Marines."),
    text("• Assisted technical-security personnel with security equipment and supported physical security requirements for sensitive communications assets and SCIF environments during domestic and international missions."),
    text("1st Battalion, 1st Marines  |  Team Leader / Assistant NCOIC  |  Jan 2023–Feb 2024", "role"),
    text("• Team Leader, B Company (Jan–Jun 2023); Assistant NCOIC, ADRC (Jun 2023–Feb 2024)."),
    text("Marine Barracks Washington  |  Post Stander / Team Leader  |  Mar 2020–Jan 2021", "role"),
    text("• Provided shift-based physical security for senior Marine Corps and Navy leadership, their families, and guests; served in a continuous security operation with recall requirements."),
    text("TECHNICAL PROJECTS", "section"),
    text("<link href='https://github.com/A-Scott-17/emotion-detection' color='#35100c'>AI Emotion Detection</link>  |  Developer", "role"),
    text("• Built a Python webcam demo with OpenCV face detection and a TensorFlow/Keras happy/sad classifier. Security-camera use was conceptual; the program does not detect threats or people needing assistance."),
    text("Titan Brazilian Jiu-Jitsu  |  Website developer", "role"),
    text("• Worked with the owner to plan, code, deploy, and revise a responsive class and trial-inquiry website. Used HTML, CSS, JavaScript, GitHub Pages, DNS, HTTPS, and FormSubmit."),
    text("Cooper Counseling  |  Website developer", "role"),
    text("• Built and deployed a multi-page counseling website, integrated a Hushmail contact form, supported hosting and domain migration, improved SEO metadata and routing, and made owner-requested revisions."),
    text("EDUCATION &amp; SKILLS", "section"),
    text("College of Charleston  |  B.S. Computer Information Systems  |  Expected Fall 2027", "role"),
    text("Overall GPA 3.259 · CIS GPA 3.386 · Completed: Applied AI, Programming I &amp; II, Management Information Systems · In progress Fall 2026: User Interface Development, Entrepreneurship", "small"),
    text("Development: HTML, CSS, JavaScript, Python, Java · Deployment: Git, GitHub, DNS, HTTPS · Security: access control, camera and alarm monitoring, emergency response, incident reporting, SCIF security support", "small"),
    text("AWARDS AND RECOGNITION", "section"),
    text("Presidential Support Badge (Jan 2022) · Marine Corps Good Conduct Award (Jul 2022) · Letter of Appreciation from the Sergeant Major of the Marine Corps · Global War on Terrorism Service Medal", "small"),
    text("SECURITY CLEARANCE", "section"),
    text("TS/SCI obtained in 2020.", "small"),
]

doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=letter, rightMargin=43, leftMargin=43,
    topMargin=36, bottomMargin=34, title="Alexander Scott Resume", author="Alexander Scott"
)
doc.build(story)
print(OUTPUT)
