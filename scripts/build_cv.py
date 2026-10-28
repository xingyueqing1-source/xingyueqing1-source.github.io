from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


# Run this script from the repository root. Keeping the output path relative
# avoids Windows code-page issues when a parent directory contains CJK text.
OUTPUT = Path("output") / "pdf" / "Yueqing-Xing-CV-English.pdf"

NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#255D8A")
GOLD = colors.HexColor("#B88A3B")
TEXT = colors.HexColor("#1E2936")
MUTED = colors.HexColor("#5C6670")
LIGHT = colors.HexColor("#D9E0E6")

PAGE_WIDTH, PAGE_HEIGHT = A4
LEFT = RIGHT = 14 * mm
TOP = 11 * mm
BOTTOM = 11 * mm
CONTENT_WIDTH = PAGE_WIDTH - LEFT - RIGHT


styles = getSampleStyleSheet()


def style(name, **kwargs):
    base = kwargs.pop("parent", styles["Normal"])
    return ParagraphStyle(name, parent=base, **kwargs)


NAME = style(
    "Name",
    fontName="Helvetica-Bold",
    fontSize=21,
    leading=23,
    alignment=TA_CENTER,
    textColor=NAVY,
    spaceAfter=2,
)
CONTACT = style(
    "Contact",
    fontName="Helvetica",
    fontSize=8.4,
    leading=11,
    alignment=TA_CENTER,
    textColor=MUTED,
)
SECTION = style(
    "Section",
    fontName="Helvetica-Bold",
    fontSize=10.3,
    leading=12,
    textColor=BLUE,
    spaceBefore=4,
    spaceAfter=1,
)
BODY = style(
    "Body",
    fontName="Helvetica",
    fontSize=8.45,
    leading=11.1,
    textColor=TEXT,
)
BODY_SMALL = style(
    "BodySmall",
    fontName="Helvetica",
    fontSize=7.8,
    leading=10.2,
    textColor=TEXT,
)
BODY_MUTED = style(
    "BodyMuted",
    fontName="Helvetica",
    fontSize=8,
    leading=10.4,
    textColor=MUTED,
)
ITEM_TITLE = style(
    "ItemTitle",
    fontName="Helvetica-Bold",
    fontSize=8.75,
    leading=10.8,
    textColor=NAVY,
)
ITEM_META = style(
    "ItemMeta",
    fontName="Helvetica-Bold",
    fontSize=7.8,
    leading=10,
    alignment=TA_RIGHT,
    textColor=MUTED,
)
BULLET = style(
    "Bullet",
    fontName="Helvetica",
    fontSize=8.05,
    leading=10.45,
    leftIndent=8,
    firstLineIndent=-8,
    textColor=TEXT,
    spaceBefore=0.5,
)
FOOTER = style(
    "Footer",
    fontName="Helvetica",
    fontSize=7,
    leading=8,
    alignment=TA_CENTER,
    textColor=MUTED,
)


def section_title(title):
    return KeepTogether(
        [
            Spacer(1, 2.5),
            Paragraph(title.upper(), SECTION),
            HRFlowable(width="100%", thickness=0.8, color=NAVY, spaceBefore=0, spaceAfter=4),
        ]
    )


def project_header(dates, title, role):
    table = Table(
        [
            [
                Paragraph(dates, ITEM_META),
                Paragraph(title, ITEM_TITLE),
                Paragraph(role, ITEM_META),
            ]
        ],
        colWidths=[32 * mm, CONTENT_WIDTH - 32 * mm - 31 * mm, 31 * mm],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 6),
                ("LEFTPADDING", (1, 0), (1, 0), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
            ]
        )
    )
    return table


def bullet(text):
    return Paragraph(f"- {text}", BULLET)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.5)
    canvas.line(LEFT, 8 * mm, PAGE_WIDTH - RIGHT, 8 * mm)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(LEFT, 4.6 * mm, "Yueqing Xing - Curriculum Vitae")
    canvas.drawRightString(PAGE_WIDTH - RIGHT, 4.6 * mm, "Updated October 2026")
    canvas.restoreState()


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=LEFT,
        rightMargin=RIGHT,
        topMargin=TOP,
        bottomMargin=BOTTOM,
        title="Yueqing Xing - Curriculum Vitae",
        author="Yueqing Xing",
        subject="Academic curriculum vitae",
    )

    story = [
        Paragraph("Yueqing Xing", NAME),
        Paragraph(
            "Nanjing, China &nbsp;&nbsp;|&nbsp;&nbsp; "
            "xingyueqing1@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; "
            '<link href="https://github.com/xingyueqing1-source" color="#255D8A">github.com/xingyueqing1-source</link>',
            CONTACT,
        ),
        Spacer(1, 3),
        HRFlowable(width="100%", thickness=1.2, color=GOLD, spaceBefore=0, spaceAfter=2),
        section_title("Education"),
    ]

    education = Table(
        [
            [
                Paragraph(
                    "<b>Nanjing University of Science and Technology</b><br/>"
                    "B.Eng. in Cybersecurity, School of Cyber Science and Engineering",
                    BODY,
                ),
                Paragraph("Sep 2023 - Present", ITEM_META),
            ],
            [
                Paragraph(
                    "GPA: <b>3.72/4.00</b> &nbsp;|&nbsp; Weighted average: <b>88.71/100</b> &nbsp;|&nbsp; "
                    "Rank: <b>4/51 (top 7.8%)</b>",
                    BODY_SMALL,
                ),
                Paragraph("CET-4: 635 &nbsp; CET-6: 647", BODY_MUTED),
            ],
        ],
        colWidths=[CONTENT_WIDTH - 48 * mm, 48 * mm],
    )
    education.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 2),
                ("BOTTOMPADDING", (0, 1), (-1, 1), 0),
            ]
        )
    )
    story.extend(
        [
            education,
            Paragraph(
                "<b>Research interests:</b> Machine Learning, Recommender Systems, Matrix Completion, "
                "and Uncertainty Quantification",
                BODY_SMALL,
            ),
            section_title("Research Projects"),
            project_header(
                "Mar 2025 - Jul 2026",
                "Conformalized 1-Bit Matrix Completion: Theory and Applications",
                "Project Lead",
            ),
            bullet(
                "Proposed C1B-MC, a distribution-free framework for uncertainty quantification in binary matrix completion; developed odds-ratio weighting for covariate shift and derived exact finite-sample marginal coverage bounds with infinity-norm truncation."
            ),
            bullet(
                "Implemented a joint low-rank factorization and log-barrier optimization strategy; achieved target coverage on real data and stress tests where classical asymptotic methods failed under overparameterization. Manuscript accepted to an ICDM 2026 Workshop."
            ),
            Spacer(1, 2.5),
            project_header(
                "Jan 2026 - Jun 2026",
                "Elastic Net and Nuclear Norm Matrix Regression for Face Recognition",
                "Core Member",
            ),
            bullet(
                "Designed the application framework for Elastic Net Nuclear Norm Matrix Regression and contributed to its ADMM and singular-value-thresholding implementation."
            ),
            bullet(
                "Ran experiments under illumination and occlusion shifts, conducted classification-accuracy ablations, and visualized finite-iteration convergence. Manuscript accepted to ICETCI 2026."
            ),
            Spacer(1, 2.5),
            project_header(
                "Sep 2024 - Nov 2024",
                "Feedforward Neural Network from First Principles",
                "Independent Project",
            ),
            bullet(
                "Derived and implemented matrix operations, ReLU gradients, Softmax probabilities, backpropagation, and gradient descent using NumPy without automatic differentiation; reached 84.8% validation accuracy on MNIST after hyperparameter ablations."
            ),
            section_title("Selected Honors"),
        ]
    )

    honors = [
        ("2025-2026", "National Scholarship"),
        ("2026", "Mathematical Contest in Modeling - Meritorious Winner"),
        ("2024", "National English Competition for College Students - National Grand Prize"),
        ("2024", "NECCS National Finals - First Prize in Speech and Second Prize in Debate"),
        ("2024", "FLTRP Vocabulary Competition - First Prize, Jiangsu Province"),
        ("2024", "Chinese Mathematics Competitions for College Students - Third Prize, Jiangsu Province"),
        ("", "NJUST Outstanding Student Scholarship - Second Class (5 awards)"),
        ("", "Outstanding League Member"),
        ("", "Excellent Participant in Scientific and Technological Activities"),
    ]
    honor_rows = []
    for year, award in honors:
        honor_rows.append([Paragraph(year, BODY_MUTED), Paragraph(award, BODY_SMALL)])
    honor_table = Table(honor_rows, colWidths=[25 * mm, CONTENT_WIDTH - 25 * mm])
    honor_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.1),
            ]
        )
    )
    story.extend([honor_table, section_title("Leadership and Service")])

    service = Table(
        [
            [
                Paragraph("<b>Peer Mentor, Zhixin College, NJUST</b>", BODY_SMALL),
                Paragraph("Sep 2025 - Present", ITEM_META),
            ],
            [
                Paragraph(
                    "Mentor junior undergraduates on coursework and career planning; support academic exchange and student well-being activities.",
                    BODY_SMALL,
                ),
                "",
            ],
            [
                Paragraph("<b>Student Assistant, Jiangyin Campus Student Affairs Office</b>", BODY_SMALL),
                Paragraph("Oct 2023 - Jun 2025", ITEM_META),
            ],
            [
                Paragraph(
                    "Supported student services, document drafting, ID-card applications, and preliminary medical-insurance reimbursement review.",
                    BODY_SMALL,
                ),
                "",
            ],
        ],
        colWidths=[CONTENT_WIDTH - 45 * mm, 45 * mm],
    )
    service.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    story.extend(
        [
            service,
            section_title("Technical Profile"),
            Paragraph(
                "<b>Methods:</b> Conformal prediction, matrix completion, low-rank optimization, ADMM, "
                "statistical learning, ablation studies &nbsp;|&nbsp; <b>Programming:</b> Python, NumPy, data visualization",
                BODY_SMALL,
            ),
        ]
    )

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    from build_cv_v2 import build as build_v2

    build_v2()
