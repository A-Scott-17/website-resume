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
    return Paragraph(value, styles[style])


story = [
    text("Alexander Scott", "name"),
    text("SECURITY OPERATIONS  |  COMPUTER INFORMATION SYSTEMS  |  TECHNOLOGY", "tag"),
    text("Charleston, SC  ·  AlexEScott00@gmail.com  ·  (309) 370-8891", "contact"),
    text("linkedin.com/in/alexescott  ·  github.com/A-Scott-17  ·  a-scott-17.github.io/website-resume/", "contact"),
    Spacer(1, 7),
    HRFlowable(width="100%", thickness=1.2, color=MAROON),
    text("PROFILE", "section"),
    text("Former U.S. Marine Corps Sergeant and College of Charleston CIS student seeking a Summer 2027 internship in cybersecurity, technical security, IT, or information systems. Five years in security operations and leadership, including WHCA national-security missions; now developing programming, web, and applied AI skills."),
    text("EXPERIENCE", "section"),
    text("White House Communications Agency  |  Security and Section Leadership  |  Jan 2021–Dec 2022", "role"),
    text("• Provided 24/7 security for assets vital to national security in coordination with the U.S. Secret Service and other agencies, supporting Presidential and Vice-Presidential missions."),
    text("• Progressed from Post Stander to Team Leader (4 personnel), Squad Leader (12), and Section Leader/NCOIC (up to 27)."),
    text("• As Sergeant of the Guard, coordinated 16+ Marines in daily post operations; supported access control, camera and alarm monitoring, threat and emergency response across three compounds."),
    text("• Delivered monthly updates to DoD stakeholders; facilitated or supported security and emergency-response training for 30+ Marines. Supported technical-security personnel with protective measures for sensitive mission environments."),
    text("1st Battalion, 1st Marines  |  Team Leader / Assistant NCOIC  |  Jan 2023–Feb 2024", "role"),
    text("• Led and mentored Marines while supporting training, readiness, personnel accountability, and mission execution at Camp Pendleton."),
    text("Marine Barracks Washington  |  Post Stander / Team Leader  |  Mar 2020–Jan 2021", "role"),
    text("• Provided physical security supporting senior Department of Defense leadership and security procedures in sensitive environments."),
    text("SELECTED TECHNICAL PROJECTS", "section"),
    text("Local business websites  |  Independent developer", "role"),
    text("• Built and deployed live websites for Titan Brazilian Jiu-Jitsu and Cooper Counseling, translating client requirements into responsive pages and clear inquiry paths. Worked with HTML, CSS, JavaScript, Git, production hosting, DNS, HTTPS, forms, and SEO."),
    text("AI-Assisted Physical Security Management System  |  Work in progress", "role"),
    text("• Exploring a simulated access-log and incident-review workflow with AI-assisted event explanations and human decisions. Concept and development stage; no completed detection system claimed."),
    text("EDUCATION &amp; SKILLS", "section"),
    text("College of Charleston  |  B.S. Computer Information Systems  |  Expected Fall 2027", "role"),
    text("Overall GPA 3.259 · CIS GPA 3.386 · Applied AI, Programming I &amp; II, User Interface Development, Management Information Systems", "small"),
    text("Development: HTML, CSS, JavaScript, Python, Java  ·  Deployment: Git, GitHub, GitHub Pages, DNS, HTTPS  ·  Security: access control, surveillance and alarm monitoring, emergency response, risk management", "small"),
    text("RECOGNITION", "section"),
    text("Presidential Support Badge · Marine Corps Good Conduct Award · Letter of Appreciation · TS/SCI obtained in 2020 (current status not stated)", "small"),
]

doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=letter, rightMargin=43, leftMargin=43,
    topMargin=36, bottomMargin=34, title="Alexander Scott Resume", author="Alexander Scott"
)
doc.build(story)
print(OUTPUT)
