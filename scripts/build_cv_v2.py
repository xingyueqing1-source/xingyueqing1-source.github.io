from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
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


OUTPUT = Path("output") / "pdf" / "Yueqing-Xing-CV-English.pdf"

PAGE_WIDTH, PAGE_HEIGHT = A4
NAVY = colors.HexColor("#142B40")
BLUE = colors.HexColor("#275F89")
GOLD = colors.HexColor("#C3984A")
INK = colors.HexColor("#20303E")
MUTED = colors.HexColor("#65727D")
PAPER = colors.HexColor("#F7F5F0")
SIDEBAR_TEXT = colors.HexColor("#EAF0F4")
SIDEBAR_MUTED = colors.HexColor("#BAC6CF")
RULE = colors.HexColor("#D6DEE4")

LEFT_MARGIN = 13 * mm
RIGHT_MARGIN = 13 * mm
TOP_MARGIN = 11 * mm
BOTTOM_MARGIN = 12 * mm
CONTENT_WIDTH = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
RIGHT_CONTENT_WIDTH = CONTENT_WIDTH - 55 * mm - 30

styles = getSampleStyleSheet()


def paragraph_style(name, **kwargs):
    parent = kwargs.pop("parent", styles["Normal"])
    return ParagraphStyle(name, parent=parent, **kwargs)


NAME = paragraph_style(
    "Name",
    fontName="Helvetica-Bold",
    fontSize=25,
    leading=30,
    textColor=NAVY,
)
TAGLINE = paragraph_style(
    "Tagline",
    fontName="Helvetica",
    fontSize=9.2,
    leading=12,
    textColor=BLUE,
)
CONTACT = paragraph_style(
    "Contact",
    fontName="Helvetica",
    fontSize=8.1,
    leading=11.2,
    alignment=TA_RIGHT,
    textColor=MUTED,
)
LEFT_SECTION = paragraph_style(
    "LeftSection",
    fontName="Helvetica-Bold",
    fontSize=8.5,
    leading=10,
    textColor=GOLD,
    spaceBefore=1,
    spaceAfter=3,
)
LEFT_TITLE = paragraph_style(
    "LeftTitle",
    fontName="Helvetica-Bold",
    fontSize=8.8,
    leading=11,
    textColor=colors.white,
)
LEFT_BODY = paragraph_style(
    "LeftBody",
    fontName="Helvetica",
    fontSize=7.9,
    leading=10.5,
    textColor=SIDEBAR_TEXT,
)
LEFT_MUTED = paragraph_style(
    "LeftMuted",
    fontName="Helvetica",
    fontSize=7.6,
    leading=9.9,
    textColor=SIDEBAR_MUTED,
)
LEFT_BULLET = paragraph_style(
    "LeftBullet",
    fontName="Helvetica",
    fontSize=7.8,
    leading=10.35,
    leftIndent=7,
    firstLineIndent=-7,
    textColor=SIDEBAR_TEXT,
    spaceAfter=1.4,
)
RIGHT_SECTION = paragraph_style(
    "RightSection",
    fontName="Helvetica-Bold",
    fontSize=10.4,
    leading=12,
    textColor=BLUE,
    spaceBefore=1,
    spaceAfter=1,
)
SUMMARY = paragraph_style(
    "Summary",
    fontName="Helvetica",
    fontSize=8.85,
    leading=12.2,
    textColor=INK,
)
PROJECT_TITLE = paragraph_style(
    "ProjectTitle",
    fontName="Helvetica-Bold",
    fontSize=9.45,
    leading=11.4,
    textColor=NAVY,
)
PROJECT_DATE = paragraph_style(
    "ProjectDate",
    fontName="Helvetica-Bold",
    fontSize=7.55,
    leading=9.6,
    alignment=TA_RIGHT,
    textColor=MUTED,
)
AUTHORS = paragraph_style(
    "Authors",
    fontName="Helvetica",
    fontSize=7.5,
    leading=9.65,
    textColor=MUTED,
)
VENUE = paragraph_style(
    "Venue",
    fontName="Helvetica-Bold",
    fontSize=7.75,
    leading=9.85,
    textColor=GOLD,
)
RIGHT_BULLET = paragraph_style(
    "RightBullet",
    fontName="Helvetica",
    fontSize=7.8,
    leading=10.45,
    leftIndent=8,
    firstLineIndent=-8,
    textColor=INK,
    spaceBefore=0.5,
)
SERVICE_TITLE = paragraph_style(
    "ServiceTitle",
    fontName="Helvetica-Bold",
    fontSize=8.45,
    leading=10.5,
    textColor=NAVY,
)
SERVICE_BODY = paragraph_style(
    "ServiceBody",
    fontName="Helvetica",
    fontSize=7.75,
    leading=10.35,
    textColor=INK,
)
CITATION = paragraph_style(
    "Citation",
    fontName="Helvetica",
    fontSize=7.75,
    leading=10.4,
    leftIndent=9,
    firstLineIndent=-9,
    textColor=INK,
)


def section_right(title):
    table = Table(
        [[Paragraph(title.upper(), RIGHT_SECTION)]],
        colWidths=[RIGHT_CONTENT_WIDTH],
    )
    table.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 0.75, BLUE),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return table


def section_left(title):
    table = Table(
        [[Paragraph(title.upper(), LEFT_SECTION)]],
        colWidths=[55 * mm - 24],
    )
    table.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 0.45, colors.HexColor("#446073")),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return table


def left_bullet(text):
    return Paragraph(f"- {text}", LEFT_BULLET)


def right_bullet(text):
    return Paragraph(f"- {text}", RIGHT_BULLET)


def project(title, dates, authors, venue, bullets):
    title_table = Table(
        [[Paragraph(title, PROJECT_TITLE), Paragraph(dates, PROJECT_DATE)]],
        colWidths=[RIGHT_CONTENT_WIDTH - 33 * mm, 33 * mm],
    )
    title_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    flowables = [
        title_table,
        Paragraph(authors, AUTHORS),
        Paragraph(venue, VENUE),
    ]
    flowables.extend(right_bullet(item) for item in bullets)
    flowables.append(Spacer(1, 4))
    return flowables


def footer(canvas, _doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.45)
    canvas.line(LEFT_MARGIN, 7.2 * mm, PAGE_WIDTH - RIGHT_MARGIN, 7.2 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 6.8)
    canvas.drawString(LEFT_MARGIN, 4.1 * mm, "Yueqing Xing - Academic Curriculum Vitae")
    canvas.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, 4.1 * mm, "Updated October 2026")
    canvas.restoreState()


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
        title="Yueqing Xing - Academic Curriculum Vitae",
        author="Yueqing Xing",
        subject="Academic curriculum vitae",
    )

    header = Table(
        [
            [
                [
                    Paragraph("Yueqing Xing", NAME),
                    Spacer(1, 3),
                    Paragraph(
                        "Cybersecurity undergraduate focused on reliable machine learning",
                        TAGLINE,
                    ),
                ],
                Paragraph(
                    "Nanjing, China<br/>"
                    '<link href="mailto:xingyueqing1@gmail.com" color="#275F89">xingyueqing1@gmail.com</link><br/>'
                    '<link href="https://github.com/xingyueqing1-source" color="#275F89">github.com/xingyueqing1-source</link>',
                    CONTACT,
                ),
            ]
        ],
        colWidths=[CONTENT_WIDTH - 61 * mm, 61 * mm],
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    left = [
        section_left("Education"),
        Paragraph("Nanjing University of Science and Technology", LEFT_TITLE),
        Paragraph("B.Eng. in Cybersecurity", LEFT_BODY),
        Paragraph("School of Cyber Science and Engineering", LEFT_MUTED),
        Paragraph("Sep 2023 - Jun 2027 (expected)", LEFT_MUTED),
        Spacer(1, 5),
        Paragraph("GPA", LEFT_MUTED),
        Paragraph("3.72 / 4.00", LEFT_TITLE),
        Paragraph("Weighted average: 88.71 / 100", LEFT_BODY),
        Paragraph("Rank: 4 / 51 (top 7.8%)", LEFT_BODY),
        Spacer(1, 9),
        section_left("Research Interests"),
        left_bullet("Machine Learning"),
        left_bullet("Recommender Systems"),
        left_bullet("Matrix Completion"),
        left_bullet("Uncertainty Quantification"),
        Spacer(1, 8),
        section_left("Technical Profile"),
        left_bullet("Python and NumPy"),
        left_bullet("Conformal prediction"),
        left_bullet("Low-rank optimization"),
        left_bullet("ADMM and ablation studies"),
        left_bullet("Data visualization"),
        Spacer(1, 8),
        section_left("English"),
        Paragraph("CET-4: 635", LEFT_BODY),
        Paragraph("CET-6: 647", LEFT_BODY),
        Spacer(1, 8),
        section_left("Selected Honors"),
        Paragraph("2025-2026", LEFT_MUTED),
        Paragraph("National Scholarship", LEFT_BODY),
        Spacer(1, 3),
        Paragraph("2026", LEFT_MUTED),
        Paragraph("MCM Meritorious Winner", LEFT_BODY),
        Spacer(1, 3),
        Paragraph("2024", LEFT_MUTED),
        Paragraph("NECCS National Grand Prize", LEFT_BODY),
        Spacer(1, 3),
        Paragraph("2024", LEFT_MUTED),
        Paragraph("NECCS Finals: 1st in Speech, 2nd in Debate", LEFT_BODY),
        Spacer(1, 3),
        Paragraph("Additional", LEFT_MUTED),
        Paragraph("NJUST Outstanding Student Scholarship, Second Class (5 awards)", LEFT_BODY),
        Spacer(1, 3),
        Paragraph("2024", LEFT_MUTED),
        Paragraph("FLTRP Vocabulary Competition, Jiangsu First Prize", LEFT_BODY),
        Spacer(1, 3),
        Paragraph("2024", LEFT_MUTED),
        Paragraph("Chinese Mathematics Competition, Jiangsu Third Prize", LEFT_BODY),
        Spacer(1, 3),
        Paragraph("Additional", LEFT_MUTED),
        Paragraph("Outstanding League Member; Excellent Participant in Scientific and Technological Activities", LEFT_BODY),
    ]

    right = [
        section_right("Profile"),
        Paragraph(
            "Fourth-year cybersecurity undergraduate developing reliable machine learning methods with finite-sample guarantees. Current work centers on conformal inference for matrix completion, with an emphasis on distribution shift, model misspecification, and reproducible empirical evaluation.",
            SUMMARY,
        ),
        Spacer(1, 8),
        section_right("Research Experience"),
        *project(
            "Conformalized 1-Bit Matrix Completion",
            "Mar 2025 - Jul 2026",
            "Yueqing Xing, Siyuan Wu, Ji Cui, Liangliang Yuan",
            "Accepted, TrustRS @ IEEE ICDM 2026 | Project Lead",
            [
                "Proposed C1B-MC, a distribution-free framework for uncertainty quantification in binary matrix completion, with odds-ratio weighting for covariate shift.",
                "Derived finite-sample marginal coverage bounds with infinity-norm truncation; implemented low-rank factorization with log-barrier optimization and validated target coverage on simulated and MovieLens data.",
                "Developed an observable hinge-score variant and stress-tested the method under model misspecification and overparameterization, where asymptotic baselines lost coverage.",
            ],
        ),
        *project(
            "The Matrix Regression Model Based on Elastic Net and Its Application in Face Recognition",
            "Jan 2026 - Jun 2026",
            "Liangliang Yuan, Yueqing Xing, Siyuan Wu, Jiacheng Yin",
            "Accepted, ICETCI 2026 | Core Member",
            [
                "Developed the ENNMR application framework, combining Elastic Net regularization with nuclear-norm matrix regression to preserve image structure while encouraging sparse coefficients.",
                "Contributed to ADMM implementation and experiments on Extended Yale B and AR, including accuracy ablations and finite-iteration convergence analysis.",
                "Evaluated robustness under illumination changes and contiguous occlusion and visualized convergence behavior across optimization settings.",
            ],
        ),
        *project(
            "Feedforward Neural Network from First Principles",
            "Sep 2024 - Nov 2024",
            "Independent project",
            "NumPy implementation | MNIST validation accuracy: 84.8%",
            [
                "Derived and implemented matrix layers, ReLU, Softmax, backpropagation, and gradient descent without automatic differentiation; evaluated learning rate, iteration count, and hidden-layer width.",
                "Built MNIST preprocessing and one-hot encoding pipelines and conducted multi-dimensional hyperparameter ablations.",
            ],
        ),
        section_right("Selected Publications"),
        Paragraph(
            "1. <b>Y. Xing</b>, S. Wu, J. Cui, and L. Yuan. \"Conformalized 1-Bit Matrix Completion.\" Accepted to TrustRS: Workshop on Trustworthy Recommender Systems across Learning, Relearning, and Unlearning at IEEE ICDM 2026.",
            CITATION,
        ),
        Spacer(1, 3),
        Paragraph(
            "2. L. Yuan, <b>Y. Xing</b>, S. Wu, and J. Yin. \"The Matrix Regression Model Based on Elastic Net and Its Application in Face Recognition.\" Accepted to ICETCI 2026.",
            CITATION,
        ),
        Spacer(1, 7),
        section_right("Leadership and Service"),
    ]

    service_one = Table(
        [[Paragraph("Peer Mentor, Zhixin College, NJUST", SERVICE_TITLE), Paragraph("Sep 2025 - Present", PROJECT_DATE)]],
        colWidths=[RIGHT_CONTENT_WIDTH - 33 * mm, 33 * mm],
    )
    service_two = Table(
        [[Paragraph("Student Assistant, Jiangyin Campus Student Affairs Office", SERVICE_TITLE), Paragraph("Oct 2023 - Jun 2025", PROJECT_DATE)]],
        colWidths=[RIGHT_CONTENT_WIDTH - 33 * mm, 33 * mm],
    )
    for table in (service_one, service_two):
        table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            )
        )

    right.extend(
        [
            service_one,
            Paragraph(
                "Mentor junior undergraduates on coursework and career planning and support academic exchange and student well-being activities.",
                SERVICE_BODY,
            ),
            Spacer(1, 4),
            service_two,
            Paragraph(
                "Supported student services, document drafting, ID-card applications, and preliminary medical-insurance reimbursement review.",
                SERVICE_BODY,
            ),
            Spacer(1, 7),
            Paragraph(
                '<link href="https://github.com/xingyueqing1-source/C1B-MC" color="#275F89"><b>Open-source code:</b> github.com/xingyueqing1-source/C1B-MC</link>',
                SERVICE_BODY,
            ),
        ]
    )

    main = Table(
        [[left, right]],
        colWidths=[55 * mm, CONTENT_WIDTH - 55 * mm],
        rowHeights=[224 * mm],
        cornerRadii=[7, 7, 7, 7],
    )
    main.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), NAVY),
                ("BACKGROUND", (1, 0), (1, 0), PAPER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (0, 0), 12),
                ("RIGHTPADDING", (0, 0), (0, 0), 12),
                ("TOPPADDING", (0, 0), (0, 0), 13),
                ("BOTTOMPADDING", (0, 0), (0, 0), 13),
                ("LEFTPADDING", (1, 0), (1, 0), 15),
                ("RIGHTPADDING", (1, 0), (1, 0), 15),
                ("TOPPADDING", (1, 0), (1, 0), 13),
                ("BOTTOMPADDING", (1, 0), (1, 0), 13),
            ]
        )
    )

    story = [
        header,
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=1.3, color=GOLD, spaceBefore=0, spaceAfter=6),
        main,
    ]
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    build()
