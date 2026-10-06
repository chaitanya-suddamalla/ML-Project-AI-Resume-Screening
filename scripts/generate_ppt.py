import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_slide_layout = prs.slide_layouts[6]

    # Theme Colors
    COLOR_BG = RGBColor(11, 17, 32)         # #0B1120 Deep Navy
    COLOR_CARD = RGBColor(26, 36, 56)       # #1A2438 Glass Card
    COLOR_TEXT = RGBColor(241, 245, 249)     # #F1F5F9 Slate White
    COLOR_SUBTEXT = RGBColor(148, 163, 184)  # #94A3B8 Slate Gray
    COLOR_TEAL = RGBColor(20, 184, 166)      # #14B8A6 Teal
    COLOR_EMERALD = RGBColor(16, 185, 129)   # #10B981 Emerald
    COLOR_AMBER = RGBColor(245, 158, 11)     # #F59E0B Amber
    COLOR_CYAN = RGBColor(6, 182, 212)       # #06B6D4 Cyan

    def set_slide_background(slide):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = COLOR_BG

    def add_header(slide, title_text, category_text="SHORT-TERM INDUSTRY INTERNSHIP REVIEW"):
        # Header category tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.4))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = category_text.upper()
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_TEAL

        # Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.733), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_TEXT

    def add_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s1)

    # Decorative Card
    card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.0), Inches(11.333), Inches(5.5))
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_CARD
    card.line.color.rgb = COLOR_TEAL

    tf1 = card.text_frame
    tf1.word_wrap = True
    tf1.margin_left = Inches(0.5)
    tf1.margin_right = Inches(0.5)
    tf1.margin_top = Inches(0.5)

    p = tf1.paragraphs[0]
    p.text = "G. PULLA REDDY ENGINEERING COLLEGE (AUTONOMOUS), KURNOOL"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL

    p = tf1.add_paragraph()
    p.text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING"
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_SUBTEXT
    p.space_after = Pt(24)

    p = tf1.add_paragraph()
    p.text = "AI-Based Resume Screening and Job Matching System"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "Short-Term Industry Internship Review Presentation"
    p.font.size = Pt(16)
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(36)

    p = tf1.add_paragraph()
    p.text = "Presenter: Meda Geethika (Reg. No: 239X1A05D6) | Branch: B.Tech CSE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT

    p = tf1.add_paragraph()
    p.text = "Internship Organization: InternPe | Domain: AI / Machine Learning"
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_SUBTEXT

    p = tf1.add_paragraph()
    p.text = "Faculty Guide: Smt. Y. Supriya Reddy, Assistant Professor, Dept. of CSE"
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_CYAN

    add_notes(s1, "Respected Faculty Evaluators, my Guide Smt. Y. Supriya Reddy ma'am, and dear classmates, a very good morning to all of you. My name is Meda Geethika, studying B.Tech in Computer Science and Engineering at G. Pulla Reddy Engineering College (Autonomous), Kurnool, bearing Register Number 239X1A05D6. Today, I am presenting my 8-week Short-Term Industry Internship Review presentation on the project titled 'AI-Based Resume Screening and Job Matching System', completed under the mentorship of InternPe in the Artificial Intelligence and Machine Learning domain. Over the next 15 minutes, I will walk you through the problem statement, system architecture, NLP algorithms, implementation details, and learning outcomes.")

    # ==========================================
    # SLIDE 2: STUDENT & INTERNSHIP DETAILS
    # ==========================================
    s2 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s2)
    add_header(s2, "Student & Internship Registration Details")

    table_shape = s2.shapes.add_table(10, 2, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.2))
    table = table_shape.table
    table.columns[0].width = Inches(3.5)
    table.columns[1].width = Inches(8.233)

    details = [
        ("Student Name", "Meda Geethika"),
        ("Register Number", "239X1A05D6"),
        ("Degree & Branch", "B.Tech – Computer Science and Engineering"),
        ("Institution", "G. Pulla Reddy Engineering College (Autonomous), Kurnool"),
        ("Internship Organization", "InternPe"),
        ("Internship Domain", "Artificial Intelligence / Machine Learning"),
        ("Internship Title", "Real Time Machine Learning Project Using Python"),
        ("Duration & Dates", "8 Weeks (04-05-2026 to 28-06-2026)"),
        ("Mode of Internship", "Virtual / Remote"),
        ("Faculty Guide", "Smt. Y. Supriya Reddy, Assistant Professor, Dept. of CSE")
    ]

    for idx, (label, val) in enumerate(details):
        cell_lbl = table.cell(idx, 0)
        cell_val = table.cell(idx, 1)

        cell_lbl.fill.solid()
        cell_lbl.fill.fore_color.rgb = COLOR_CARD
        cell_val.fill.solid()
        cell_val.fill.fore_color.rgb = COLOR_BG

        p0 = cell_lbl.text_frame.paragraphs[0]
        p0.text = label
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_TEAL

        p1 = cell_val.text_frame.paragraphs[0]
        p1.text = val
        p1.font.size = Pt(11)
        p1.font.color.rgb = COLOR_TEXT

    add_notes(s2, "This table summarizes my official internship registration details. I completed my 8-week virtual internship from May 4th, 2026 to June 28th, 2026 with InternPe. The domain assigned was Artificial Intelligence and Machine Learning, focusing on building a real-time Python machine learning project. Throughout this period, I worked under the continuous guidance of our faculty guide, Smt. Y. Supriya Reddy ma'am, to align the technical learning with academic computer science principles.")

    # ==========================================
    # SLIDE 3: ABOUT INTERNPE & INTERNSHIP ROLE
    # ==========================================
    s3 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s3)
    add_header(s3, "About Organization & Internship Role")

    # Left Card: About InternPe
    c_left = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = COLOR_CARD
    tf_l = c_left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = Inches(0.4)
    tf_l.margin_top = Inches(0.4)

    p = tf_l.paragraphs[0]
    p.text = "About InternPe"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(14)

    bullets_l = [
        "Technology & career-development platform specializing in practical engineering skill acquisition.",
        "Provides project-based internship opportunities across Software Development, Data Science, AI and ML.",
        "Focuses on task-oriented learning, Python framework utilization, and modular application development.",
        "Helps students gain hands-on industrial exposure beyond theoretical classroom concepts."
    ]
    for b in bullets_l:
        p = tf_l.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(10)

    # Right Card: My Role
    c_right = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = COLOR_CARD
    tf_r = c_right.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = Inches(0.4)
    tf_r.margin_top = Inches(0.4)

    p = tf_r.paragraphs[0]
    p.text = "My Internship Role & Deliverables"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(14)

    bullets_r = [
        "Domain Role: AI / Machine Learning Project Intern.",
        "Project Task: End-to-end design & implementation of an AI-Based Resume Screening & Job Matching System.",
        "Responsibilities: Multi-format document parsing (PDF/DOCX/TXT), NLP text cleaning, TF-IDF vectorization, Cosine Similarity math, skill extraction, and persistent learning roadmaps.",
        "Full-Stack Integration: Connected Python FastAPI REST backend with a modern React.js frontend interface."
    ]
    for b in bullets_r:
        p = tf_r.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(10)

    add_notes(s3, "InternPe provides project-based learning for computer science engineering students. During my internship, I was tasked with developing a real-time machine learning application in Python. My role involved taking raw, unstructured resume files and job descriptions, applying Natural Language Processing concepts to extract information, and building a working web application. This gave me practical exposure to the complete ML lifecycle, from data preprocessing to web integration.")

    # Helper function for grid slides
    def create_grid_slide(slide_num, title, items, notes):
        s = prs.slides.add_slide(blank_slide_layout)
        set_slide_background(s)
        add_header(s, title)

        coords = [
            (Inches(0.8), Inches(1.5)), (Inches(4.8), Inches(1.5)), (Inches(8.8), Inches(1.5)),
            (Inches(0.8), Inches(4.2)), (Inches(4.8), Inches(4.2)), (Inches(8.8), Inches(4.2))
        ]

        for idx, item in enumerate(items[:6]):
            x, y = coords[idx]
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(3.733), Inches(2.4))
            card.fill.solid()
            card.fill.fore_color.rgb = COLOR_CARD
            tf = card.text_frame
            tf.word_wrap = True
            tf.margin_left = Inches(0.25)
            tf.margin_top = Inches(0.25)

            p0 = tf.paragraphs[0]
            p0.text = f"{idx+1}. {item['title']}"
            p0.font.size = Pt(13)
            p0.font.bold = True
            p0.font.color.rgb = COLOR_TEAL
            p0.space_after = Pt(8)

            p1 = tf.add_paragraph()
            p1.text = item['desc']
            p1.font.size = Pt(10)
            p1.font.color.rgb = COLOR_TEXT

        add_notes(s, notes)

    # ==========================================
    # SLIDE 4: INTERNSHIP OBJECTIVES
    # ==========================================
    objectives = [
        {"title": "AI/ML Workflow Mastery", "desc": "Understand the complete Machine Learning lifecycle: Data preprocessing -> Feature engineering -> Model vectorization -> Deployment."},
        {"title": "Data & NLP Preprocessing", "desc": "Learn text tokenization, noise removal, stop-word filtering, and special programming symbol preservation (C++, C#, React.js)."},
        {"title": "Mathematical Vectorization", "desc": "Apply TF-IDF N-gram feature representation and Cosine Similarity math to compute text similarity scores."},
        {"title": "Full-Stack System Architecture", "desc": "Connect Python FastAPI REST APIs with an interactive React.js single-page application dashboard."},
        {"title": "Skill-Gap Diagnostics", "desc": "Automate categorization of matched vs missing skills and auto-generate personalized practice learning roadmaps."},
        {"title": "Ethical AI Implementation", "desc": "Design a career diagnostic tool with automated PII privacy masking that avoids automated hiring bias."}
    ]
    create_grid_slide(4, "Internship Learning Objectives", objectives, "The primary objectives of this internship were six-fold: First, to gain hands-on experience with the complete ML project lifecycle; second, to learn Python libraries like Pandas, NumPy, Scikit-Learn, and FastAPI; third, to understand how unstructured text is converted into numerical vectors using TF-IDF; fourth, to calculate text similarity using Cosine Similarity; fifth, to automate skill-gap identification and generate learning roadmaps; and sixth, to ensure the tool operates ethically as a career-assistance system rather than making automated hiring decisions.")

    # ==========================================
    # SLIDE 5: PROBLEM STATEMENT & MOTIVATION
    # ==========================================
    s5 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s5)
    add_header(s5, "Problem Statement & Industry Motivation")

    # Left: Traditional Flaws
    c_flaws = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_flaws.fill.solid()
    c_flaws.fill.fore_color.rgb = COLOR_CARD
    tf_fl = c_flaws.text_frame
    tf_fl.word_wrap = True
    tf_fl.margin_left = Inches(0.3)
    tf_fl.margin_top = Inches(0.3)

    p = tf_fl.paragraphs[0]
    p.text = "Flaws in Traditional Manual Screening"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_AMBER
    p.space_after = Pt(12)

    flaws = [
        "Time-Consuming: Recruiters manually scan hundreds of unstructured PDF resumes.",
        "Overlooking Complex Vocabularies: Multi-word technical frameworks (e.g. React.js, FastAPI, CI/CD) get missed.",
        "Lack of Candidate Feedback: Job seekers receive zero visibility into why their resume failed to match requirements.",
        "Flawed Keyword Counting: Exact keyword matches penalize valid industry synonyms (e.g. React.js vs React)."
    ]
    for f in flaws:
        p = tf_fl.add_paragraph()
        p.text = "• " + f
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(8)

    # Right: Problem Statement Definition
    c_ps = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    c_ps.fill.solid()
    c_ps.fill.fore_color.rgb = COLOR_CARD
    tf_ps = c_ps.text_frame
    tf_ps.word_wrap = True
    tf_ps.margin_left = Inches(0.3)
    tf_ps.margin_top = Inches(0.3)

    p = tf_ps.paragraphs[0]
    p.text = "Formal Problem Statement"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL
    p.space_after = Pt(12)

    p = tf_ps.add_paragraph()
    p.text = "\"Develop an automated NLP/ML-based web application that parses unstructured candidate resumes, compares them against target job descriptions using TF-IDF and Cosine Similarity, highlights matched and missing skills, and provides personalized skill-gap learning recommendations.\""
    p.font.size = Pt(12)
    p.font.italic = True
    p.font.color.rgb = COLOR_TEXT
    p.space_after = Pt(16)

    p = tf_ps.add_paragraph()
    p.text = "Core Requirements:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(6)

    bullets_ps = [
        "Multi-Format Parser: Support PDF, DOCX, and TXT with PII privacy masking.",
        "Reproducible NLP Pipeline: TF-IDF vector space model with Cosine Similarity.",
        "Transparent Skill Dictionary: Canonical mapping for 150+ categorized technical skills.",
        "Persistent Learning Roadmap: SQLite tracking for missing skill gap exercises."
    ]
    for b in bullets_ps:
        p = tf_ps.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(6)

    add_notes(s5, "In the traditional hiring and preparation process, manual resume evaluation is slow, repetitive, and subjective. Recruiters manually read through hundreds of resumes, while candidates applying for technical roles often have no clear idea of why their resume failed to match a job description. Furthermore, simple keyword matching is flawed because candidates write skills in different ways—for example, writing 'React.js' instead of 'React'. Our problem statement addresses this gap by building an intelligent NLP system that measures text similarity, extracts technical skills, and provides actionable feedback to students.")

    # ==========================================
    # SLIDE 6: PROPOSED SYSTEM OVERVIEW
    # ==========================================
    system_features = [
        {"title": "Multi-Format Ingestion", "desc": "Parses PDF, DOCX, and TXT resumes with PyMuPDF and python-docx, masking candidate emails/phones."},
        {"title": "Token Protection", "desc": "Custom regex preprocessor preserves special programming symbols (C++, C#, .NET, React.js, CI/CD)."},
        {"title": "TF-IDF Vector Space", "desc": "Converts text into numerical feature vectors using Scikit-Learn TfidfVectorizer (max_features=5000, ngram_range=(1,2))."},
        {"title": "Cosine Similarity Math", "desc": "Calculates vector angle similarity percentage (0–100%) labeled clearly as a Text Similarity Score."},
        {"title": "Transparent Dictionary", "desc": "Matches phrase boundaries and canonical synonyms (React.js -> React) across 150+ categorized skills."},
        {"title": "Persistent Skill Roadmap", "desc": "Generates practice projects for missing skills with SQLite status tracking (Not Started, In Progress, Completed)."}
    ]
    create_grid_slide(6, "Proposed System Overview & Solution Architecture", system_features, "To solve the problem, we proposed a full-stack ML application. The system ingests resumes in PDF, DOCX, or TXT format, cleans the text while protecting technical terms like C++ and React.js, converts the text into numerical vectors using TF-IDF, calculates similarity using Cosine Similarity, categorizes skills into matched and missing, and generates a personalized learning roadmap. Importantly, we clearly state in the application interface that this is a career assistance diagnostic tool, not an automated hiring system.")

    # ==========================================
    # SLIDE 7: END-TO-END SYSTEM WORKFLOW
    # ==========================================
    s7 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s7)
    add_header(s7, "End-to-End System Processing Workflow")

    flow_steps = [
        ("1. Input Resume File", "PDF / DOCX / TXT Upload"),
        ("2. Text Extractor", "PyMuPDF & python-docx"),
        ("3. PII Privacy Sanitizer", "Email / Phone Regex Mask"),
        ("4. NLP Preprocessor", "Symbol Protection & Clean"),
        ("5. TF-IDF Vectorizer", "N-Gram (1,2) Sparse Matrix"),
        ("6. Cosine Similarity", "Vector Angle % Calculation"),
        ("7. Skill Extractor", "Phrase Boundary Regex"),
        ("8. Gap Generator", "Personalized Roadmap"),
        ("9. SQLite Database", "Analysis & Checklist Tables"),
        ("10. React Dashboard", "Interactive User UI")
    ]

    for idx, (step_t, step_d) in enumerate(flow_steps):
        row = idx // 5
        col = idx % 5
        x = Inches(0.8 + col * 2.4)
        y = Inches(1.8 + row * 2.6)

        box = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(2.133), Inches(2.1))
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD
        box.line.color.rgb = COLOR_TEAL

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.15)
        tf.margin_top = Inches(0.2)

        p0 = tf.paragraphs[0]
        p0.text = step_t
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_EMERALD
        p0.space_after = Pt(6)

        p1 = tf.add_paragraph()
        p1.text = step_d
        p1.font.size = Pt(10)
        p1.font.color.rgb = COLOR_SUBTEXT

    add_notes(s7, "This flowchart illustrates the complete end-to-end data processing workflow. The user provides a resume and a job description. The document parser extracts text, sanitizes PII, and sends it to the NLP engine. Here, text preprocessing preserves key technical symbols. Then, TF-IDF converts the texts into high-dimensional vectors, and Cosine Similarity computes the similarity score. Simultaneously, the skill extractor matches terms against our skill dictionary, categorizes them into matched and missing skills, generates project exercises for missing skills, and saves the full analysis into SQLite for display on the React dashboard.")

    # ==========================================
    # SLIDE 8: SYSTEM ARCHITECTURE (LAYERED VIEW)
    # ==========================================
    s8 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s8)
    add_header(s8, "System Architecture (Multi-Layered View)")

    layers = [
        ("Presentation Layer (Frontend)", "React.js 18 + Vite | Tailwind CSS | Glassmorphic UI Dashboard | Recharts Data Charts", COLOR_CYAN),
        ("Application Backend Layer", "Python FastAPI | Uvicorn Server | REST APIs (/upload, /analyze, /skills, /checklist)", COLOR_TEAL),
        ("Document Parsing & Privacy Layer", "PyMuPDF (fitz) | python-docx | Regex PII Masking ([CONFIDENTIAL_EMAIL], [CONFIDENTIAL_PHONE])", COLOR_EMERALD),
        ("NLP & Machine Learning Engine", "Scikit-Learn TfidfVectorizer | Cosine Similarity Math | Transparent Skill Extractor (skills.json)", COLOR_AMBER),
        ("Persistence & Database Layer", "SQLite3 Relational DB | SQLAlchemy 2.0 ORM (resumes, job_descriptions, analysis_results, checklist_items)", COLOR_TEAL)
    ]

    for idx, (title, desc, color) in enumerate(layers):
        y = Inches(1.5 + idx * 1.05)
        box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.733), Inches(0.85))
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD
        box.line.color.rgb = color

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.15)

        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = color
        p0.space_after = Pt(2)

        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(10)
        p1.font.color.rgb = COLOR_TEXT

    add_notes(s8, "Slide 8 displays our multi-tier layered system architecture. At the top is the Presentation Layer built with React.js and Tailwind CSS. The frontend communicates with the Application Backend built using Python FastAPI via REST APIs. When a request arrives, the backend passes the document to the Document Processing Layer where PyMuPDF or python-docx extracts raw text and masks PII. The text then flows into the Machine Learning Engine containing Scikit-Learn TF-IDF vectorizers and Cosine Similarity functions. Finally, results are persisted into SQLite tables via SQLAlchemy ORM.")

    # ==========================================
    # SLIDE 9: DOCUMENT INGESTION & PII PRIVACY PROTECTION
    # ==========================================
    s9 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s9)
    add_header(s9, "Document Ingestion & PII Privacy Protection")

    ingest_cards = [
        {"title": "PDF Ingestion", "desc": "Parsed using PyMuPDF (fitz), extracting text blocks across pages while validating layout integrity."},
        {"title": "DOCX Ingestion", "desc": "Parsed using python-docx, iterating paragraph vectors and data tables."},
        {"title": "TXT Ingestion", "desc": "Direct UTF-8 plain text reader supporting raw resume copy-paste."},
        {"title": "Error Safeguards", "desc": "Catches 0-page or unreadable scanned image PDFs, enforcing 5MB max file limits and 30-char min text thresholds."},
        {"title": "Automated PII Masking", "desc": "Regex sanitization replaces contact details prior to vectorization: Emails -> [CONFIDENTIAL_EMAIL], Phone -> [CONFIDENTIAL_PHONE]."},
        {"title": "Privacy Preservation", "desc": "Ensures no candidate contact details are exposed in analysis logs, maintaining ethical AI standards."}
    ]
    create_grid_slide(9, "Document Ingestion & PII Privacy Protection", ingest_cards, "Slide 9 covers document parsing and privacy protection. Resumes come in various file formats—PDF, DOCX, and TXT. We implemented robust parsers using PyMuPDF and python-docx. If a user uploads an unreadable image-based scanned PDF, the parser catches the error and instructs the user gracefully. Furthermore, to comply with ethical data practices, we built regex-based PII sanitization that automatically replaces emails, phone numbers, and personal website links with confidential placeholders before NLP processing.")

    # ==========================================
    # SLIDE 10: NLP TEXT PREPROCESSING PIPELINE
    # ==========================================
    s10 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s10)
    add_header(s10, "NLP Text Preprocessing Pipeline")

    # Flow Representation
    box_flow = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(1.0))
    box_flow.fill.solid()
    box_flow.fill.fore_color.rgb = COLOR_CARD
    tf_f = box_flow.text_frame
    tf_f.margin_left = Inches(0.3)
    tf_f.margin_top = Inches(0.2)
    p = tf_f.paragraphs[0]
    p.text = "Raw Text Document  ──>  Technical Token Protection  ──>  Case Normalization  ──>  Noise Removal  ──>  Stop-Word Filtering"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD

    # Technical Token Protection Card
    c_tp = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.8), Inches(5.6), Inches(3.9))
    c_tp.fill.solid()
    c_tp.fill.fore_color.rgb = COLOR_CARD
    tf_tp = c_tp.text_frame
    tf_tp.margin_left = Inches(0.3)
    tf_tp.margin_top = Inches(0.3)

    p = tf_tp.paragraphs[0]
    p.text = "Technical Token Preservation Strategy"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL
    p.space_after = Pt(10)

    p_body = [
        "Standard tokenization strips punctuation, destroying programming terms:",
        "• C++  -->  converted to 'cplusplus'",
        "• C#   -->  converted to 'csharp'",
        "• .NET -->  converted to 'dotnet'",
        "• React.js --> converted to 'reactjs'",
        "• Node.js  --> converted to 'nodejs'",
        "• CI/CD   --> converted to 'cicd'"
    ]
    for b in p_body:
        p = tf_tp.add_paragraph()
        p.text = b
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(4)

    # Detailed Pipeline Actions Card
    c_pa = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.8), Inches(5.733), Inches(3.9))
    c_pa.fill.solid()
    c_pa.fill.fore_color.rgb = COLOR_CARD
    tf_pa = c_pa.text_frame
    tf_pa.margin_left = Inches(0.3)
    tf_pa.margin_top = Inches(0.3)

    p = tf_pa.paragraphs[0]
    p.text = "Pipeline Processing Steps"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(10)

    p_steps = [
        "1. Case Normalization: Lowercases text for consistent vocabulary matching.",
        "2. Noise Cleanup: Removes special punctuation while preserving hyphenated/slashed technical tokens.",
        "3. Stop-Word Removal: Filters high-frequency English stop words (the, and, with) using Scikit-Learn's English dictionary.",
        "4. Whitespace Collapse: Normalizes extra tabs, newlines, and multi-spaces."
    ]
    for s_step in p_steps:
        p = tf_pa.add_paragraph()
        p.text = s_step
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(8)

    add_notes(s10, "Text preprocessing is one of the most critical steps in any NLP pipeline. If you use standard regex cleaning on programming terms, 'C++' becomes just 'C', and 'React.js' becomes 'React' and 'js'. To solve this, we built a custom technical token preservation engine. Before tokenization, terms like C++ are mapped to 'cplusplus', C# to 'csharp', and React.js to 'reactjs'. After protecting these terms, the text is lowercased, punctuation is cleaned, generic English stop-words are removed, and multi-space gaps are collapsed.")

    # ==========================================
    # SLIDE 11: FEATURE REPRESENTATION: TF-IDF VECTORIZATION
    # ==========================================
    s11 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s11)
    add_header(s11, "Feature Representation: TF-IDF Vectorization")

    # Math formulas box
    c_math = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_math.fill.solid()
    c_math.fill.fore_color.rgb = COLOR_CARD
    tf_m = c_math.text_frame
    tf_m.margin_left = Inches(0.3)
    tf_m.margin_top = Inches(0.3)

    p = tf_m.paragraphs[0]
    p.text = "TF-IDF Mathematical Formulation"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(12)

    formulas = [
        "Term Frequency (TF):",
        "  TF(t, d) = (Count of term t in d) / (Total terms in d)",
        "",
        "Inverse Document Frequency (IDF):",
        "  IDF(t, D) = log( (1 + |D|) / (1 + |{d ∈ D : t ∈ d}|) ) + 1",
        "",
        "TF-IDF Score:",
        "  TF-IDF(t, d, D) = TF(t, d) * IDF(t, D)",
        "",
        "Purpose: Downweights generic words while assigning high numerical weights to rare technical skills."
    ]
    for f in formulas:
        p = tf_m.add_paragraph()
        p.text = f
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(4)

    # Configuration Box
    c_cfg = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    c_cfg.fill.solid()
    c_cfg.fill.fore_color.rgb = COLOR_CARD
    tf_c = c_cfg.text_frame
    tf_c.margin_left = Inches(0.3)
    tf_c.margin_top = Inches(0.3)

    p = tf_c.paragraphs[0]
    p.text = "TfidfVectorizer Configuration Parameters"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL
    p.space_after = Pt(12)

    configs = [
        ("max_features = 5000", "Caps vocabulary size to top 5,000 most informative terms, reducing memory footprint and noise."),
        ("ngram_range = (1, 2)", "Captures single words (unigrams: 'Python') and 2-word phrases (bigrams: 'Machine Learning', 'REST API')."),
        ("sublinear_tf = True", "Applies 1 + log(TF) dampening to prevent excessively repeated keywords from distorting scores."),
        ("stop_words = 'english'", "Strips high-frequency non-technical words while preserving technical programming symbols.")
    ]
    for title_c, desc_c in configs:
        p = tf_c.add_paragraph()
        p.text = title_c
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_CYAN

        p_d = tf_c.add_paragraph()
        p_d.text = desc_c
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = COLOR_TEXT
        p_d.space_after = Pt(8)

    add_notes(s11, "To allow mathematical algorithms to compare resumes with job descriptions, we must convert text into numbers. We use TF-IDF vectorization. Term Frequency measures how often a word appears in a document, while Inverse Document Frequency dampens common words and gives higher weight to rare, informative technical terms like 'FastAPI' or 'Kubernetes'. We configured Scikit-Learn's TfidfVectorizer with an N-gram range of (1, 2). This allows our model to capture both single-word skills like 'Python' and two-word phrases like 'Machine Learning' or 'REST API'.")

    # ==========================================
    # SLIDE 12: SIMILARITY MEASUREMENT: COSINE SIMILARITY
    # ==========================================
    s12 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s12)
    add_header(s12, "Similarity Measurement: Cosine Similarity")

    # Left: Formula & Concept
    c_cos = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_cos.fill.solid()
    c_cos.fill.fore_color.rgb = COLOR_CARD
    tf_cs = c_cos.text_frame
    tf_cs.margin_left = Inches(0.3)
    tf_cs.margin_top = Inches(0.3)

    p = tf_cs.paragraphs[0]
    p.text = "Cosine Similarity Formulation"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL
    p.space_after = Pt(12)

    cos_text = [
        "Measures the cosine of the angle θ between vector A (Resume) and vector B (Job Spec) in multi-dimensional vector space:",
        "",
        "  Cosine Sim(A, B) = (A · B) / (||A|| * ||B||)",
        "                  = Σ(Ai * Bi) / ( √(Σ Ai²) * √(Σ Bi²) )",
        "",
        "Geometric Intuition:",
        "• cos(0°)  = 1.0  --> Identical Vocabulary Vector Angle",
        "• cos(90°) = 0.0  --> Orthogonal / Zero Vocabulary Overlap"
    ]
    for ct in cos_text:
        p = tf_cs.add_paragraph()
        p.text = ct
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(4)

    # Right: Score Boundaries & Baseline
    c_sb = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    c_sb.fill.solid()
    c_sb.fill.fore_color.rgb = COLOR_CARD
    tf_sb = c_sb.text_frame
    tf_sb.margin_left = Inches(0.3)
    tf_sb.margin_top = Inches(0.3)

    p = tf_sb.paragraphs[0]
    p.text = "Score Thresholds & Jaccard Baseline"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_AMBER
    p.space_after = Pt(12)

    thresholds = [
        ("80% – 100% Match:", "High Similarity (Strong technical vocabulary alignment)"),
        ("55% – 79% Match:", "Moderate Similarity (Good core match, minor skill gaps)"),
        ("30% – 54% Match:", "Fair Similarity (Partial match, key skills missing)"),
        ("0% – 29% Match:", "Low Similarity (Significant skill gap alignment needed)")
    ]
    for level_t, level_d in thresholds:
        p = tf_sb.add_paragraph()
        p.text = level_t + " " + level_d
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(6)

    p = tf_sb.add_paragraph()
    p.text = "Jaccard Keyword Overlap Baseline:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(4)

    p = tf_sb.add_paragraph()
    p.text = "Calculates Jaccard Index = |A ∩ B| / |A ∪ B| to compare raw token set overlap against TF-IDF Cosine Similarity on the Model Evaluation page."
    p.font.size = Pt(10)
    p.font.color.rgb = COLOR_TEXT

    add_notes(s12, "Once the resume and job description are converted into TF-IDF vectors, we measure their alignment using Cosine Similarity. Mathematically, Cosine Similarity calculates the dot product of the two vectors divided by the product of their magnitudes. If two documents use identical technical terms in similar proportions, the angle between their vectors approaches 0 degrees, giving a Cosine Similarity score near 1.0 or 100%. If they share no vocabulary, the vectors are orthogonal, yielding 0%. This percentage is presented on our dashboard clearly as a Text Similarity Score.")

    # ==========================================
    # SLIDE 13: SKILL EXTRACTION & CANONICAL SYNONYM MAPPING
    # ==========================================
    s13 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s13)
    add_header(s13, "Skill Extraction & Canonical Synonym Mapping")

    # Catalog Dict Card
    c_cat = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_cat.fill.solid()
    c_cat.fill.fore_color.rgb = COLOR_CARD
    tf_ct = c_cat.text_frame
    tf_ct.margin_left = Inches(0.3)
    tf_ct.margin_top = Inches(0.3)

    p = tf_ct.paragraphs[0]
    p.text = "Transparent Skill Catalog (skills.json)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(12)

    cat_info = [
        "150+ Categorized Technical Skills across 6 domain areas:",
        "• Programming Languages (Python, JavaScript, Java, C++, SQL)",
        "• Frameworks & Libraries (React, Node.js, FastAPI, Express.js)",
        "• Databases & Storage (PostgreSQL, MongoDB, Redis, SQLite)",
        "• Tools, Cloud & DevOps (Git, Docker, Kubernetes, AWS, Linux)",
        "• Computer Science & ML (DSA, NLP, Machine Learning, OOP)",
        "• Soft Skills (Problem Solving, Teamwork, Communication)"
    ]
    for ci in cat_info:
        p = tf_ct.add_paragraph()
        p.text = ci
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(6)

    # Extraction Engine Card
    c_ext = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    c_ext.fill.solid()
    c_ext.fill.fore_color.rgb = COLOR_CARD
    tf_ex = c_ext.text_frame
    tf_ex.margin_left = Inches(0.3)
    tf_ex.margin_top = Inches(0.3)

    p = tf_ex.paragraphs[0]
    p.text = "Extraction & Synonym Mapping Engine"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(12)

    ext_info = [
        ("Phrase Boundary Regex Matching:", "Uses (?:\b|_)<term>(?:\b|_) to prevent false substring matches (e.g. Java inside JavaScript)."),
        ("Canonical Synonym Normalization:", "Maps variations to standard skill names (React.js / ReactJS / React JS -> React)."),
        ("Categorization Output:", "• Matched Skills: Present in both resume & job spec.\n• Missing Skills: Required by job spec but missing from resume.\n• Resume-Only Skills: Additional skills candidate possesses.")
    ]
    for title_e, desc_e in ext_info:
        p = tf_ex.add_paragraph()
        p.text = title_e
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEAL

        p_d = tf_ex.add_paragraph()
        p_d.text = desc_e
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = COLOR_TEXT
        p_d.space_after = Pt(8)

    add_notes(s13, "In addition to statistical vector similarity, our system performs transparent phrase-based skill extraction. We created an extensible JSON skill dictionary containing over 150 categorized technical skills with synonym mappings. For example, if a resume contains 'React.js' and the job post asks for 'ReactJS', our canonical lookup table maps both to the standard name 'React'. Using boundary regular expressions, we prevent false sub-string matches—such as accidentally matching 'Java' inside 'JavaScript'. This categorizes skills into Matched, Missing, and Resume-Only skills.")

    # ==========================================
    # SLIDE 14: SKILL GAP ANALYSIS & ROADMAP
    # ==========================================
    s14 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s14)
    add_header(s14, "Skill Gap Analysis & Personalized Learning Roadmap")

    # Roadmap Table
    table_shape_r = s14.shapes.add_table(5, 5, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.2))
    table_r = table_shape_r.table
    table_r.columns[0].width = Inches(1.8)
    table_r.columns[1].width = Inches(2.2)
    table_r.columns[2].width = Inches(4.533)
    table_r.columns[3].width = Inches(1.4)
    table_r.columns[4].width = Inches(1.8)

    headers_r = ["Missing Skill", "Relevance Context", "Suggested Practice Project Exercise", "Level", "Status Tracking"]
    for idx, h in enumerate(headers_r):
        cell = table_r.cell(0, idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_CARD
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEAL

    sample_rows = [
        ("Docker", "Containerization tool requested for microservice execution.", "Build multi-stage Dockerfiles for FastAPI & React with Docker Compose.", "Intermediate", "[In Progress]"),
        ("Kubernetes", "Container orchestration framework for cluster deployment.", "Deploy containerized app on local Minikube cluster with YAML manifests.", "Advanced", "[Not Started]"),
        ("CI/CD", "Continuous integration pipeline framework requested.", "Create GitHub Actions workflow for automated pytest regression checks.", "Intermediate", "[Completed]"),
        ("PostgreSQL", "Enterprise relational database required for data querying.", "Design PostgreSQL relational schema with index tuning and JOIN queries.", "Intermediate", "[Not Started]")
    ]

    for r_idx, r_data in enumerate(sample_rows):
        for c_idx, val in enumerate(r_data):
            cell = table_r.cell(r_idx+1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9)
            p.font.color.rgb = COLOR_TEXT

    add_notes(s14, "Slide 14 demonstrates the core student-assistance feature: Skill Gap Analysis and Personalized Roadmaps. In this example, the candidate possesses Java, Python, SQL, and React, but lacks Docker, Kubernetes, and CI/CD requested by the job description. For each missing skill, the system queries our recommendation engine and automatically generates a practical project exercise, assigns a proficiency level based on job context, and tracks progress via interactive status buttons—Not Started, In Progress, or Completed.")

    # ==========================================
    # SLIDE 15: MODULAR SYSTEM IMPLEMENTATION
    # ==========================================
    s15 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s15)
    add_header(s15, "Modular System Implementation Architecture")

    modules = [
        ("app/utils/parser.py", "Extracts text from PDF, DOCX, and TXT files. Sanitizes PII contact info automatically."),
        ("app/ml/preprocessing.py", "Preserves technical symbols (C++, C#, .NET, React.js) and cleans text noise."),
        ("app/ml/vectorizer.py", "Wraps Scikit-Learn TfidfVectorizer (ngram_range=(1,2), max_features=5000)."),
        ("app/ml/similarity.py", "Computes Cosine Similarity and Jaccard Keyword Overlap baseline scores."),
        ("app/ml/skill_extractor.py", "Executes phrase boundary regex matching against skills.json catalog."),
        ("app/ml/pipeline.py", "Master orchestrator unifying parsing, ML vectorization, skill gaps, and roadmaps."),
        ("app/models/models.py", "SQLAlchemy ORM database schemas (resumes, job_descriptions, analyses, checklist)."),
        ("app/api/ router endpoints", "FastAPI REST API controllers (/upload, /jobs, /analyze, /analyses, /skills, /checklist).")
    ]
    create_grid_slide(15, "Modular System Implementation Architecture", [{"title": m[0], "desc": m[1]} for m in modules[:6]], "The backend is architected in a modular structure inside FastAPI. Each component has a distinct single responsibility: `parser.py` handles multi-format file reading and PII masking; `preprocessing.py` handles technical token protection; `vectorizer.py` wraps Scikit-Learn's TF-IDF vectorizer; `similarity.py` calculates Cosine and Jaccard metrics; `skill_extractor.py` handles phrase matching; `pipeline.py` orchestrates the entire workflow; and `models.py` manages SQLAlchemy database models. This modular architecture makes the project easy to debug, test, and expand.")

    # ==========================================
    # SLIDE 16: TECHNOLOGY STACK & TOOLS
    # ==========================================
    s16 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s16)
    add_header(s16, "Technology Stack & Development Tools")

    table_shape_t = s16.shapes.add_table(11, 3, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.2))
    table_t = table_shape_t.table
    table_t.columns[0].width = Inches(2.5)
    table_t.columns[1].width = Inches(3.2)
    table_t.columns[2].width = Inches(6.033)

    t_headers = ["Layer / Category", "Technology / Tool", "Purpose in Project Implementation"]
    for idx, h in enumerate(t_headers):
        cell = table_t.cell(0, idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_CARD
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEAL

    t_rows = [
        ("Programming Language", "Python 3.14", "Core backend application logic, ML modeling, and text processing."),
        ("ML / NLP Libraries", "Scikit-Learn", "TfidfVectorizer and cosine_similarity computation."),
        ("Data Processing", "Pandas & NumPy", "Data array operations, matrix manipulation, and evaluation metrics."),
        ("Document Parsers", "PyMuPDF (fitz) & python-docx", "Extracting raw text from PDF and DOCX resume uploads."),
        ("Model Persistence", "Joblib", "Serialization and joblib persistence of fitted TF-IDF models."),
        ("Backend Web Framework", "FastAPI & Uvicorn", "High-performance asynchronous REST API backend server."),
        ("Database & ORM", "SQLite3 & SQLAlchemy 2.0", "Persistent relational database storage for history and checklists."),
        ("Frontend Framework", "React.js 18 & Vite", "Single-page responsive user dashboard interface."),
        ("Styling & Icons", "Tailwind CSS & Lucide Icons", "Glassmorphic visual styling, custom cards, and dark theme UI."),
        ("Automated Testing", "Pytest & HTTPX", "Unit and integration testing suite for parsers, pipeline, and APIs.")
    ]

    for r_idx, r_data in enumerate(t_rows):
        for c_idx, val in enumerate(r_data):
            cell = table_t.cell(r_idx+1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9)
            p.font.color.rgb = COLOR_TEXT

    add_notes(s16, "Slide 16 summarizes the full technology stack. On the backend, we use Python 3.14, Scikit-Learn for TF-IDF and Cosine Similarity, Pandas and NumPy for data manipulation, PyMuPDF and python-docx for document parsing, and FastAPI with Uvicorn for serving REST APIs. On the database side, we use SQLite3 with SQLAlchemy ORM. On the frontend, we use React.js with Vite, Tailwind CSS for glassmorphic styling, and Lucide React for UI icons. Automated testing is handled using Pytest.")

    # ==========================================
    # SLIDE 17: APPLICATION DASHBOARDS & INTERFACE LAYOUT
    # ==========================================
    ui_panels = [
        {"title": "Dual-Pane Analysis Engine", "desc": "Upload resume file (PDF/DOCX/TXT) or paste text alongside target job description specs with quick demo data loader."},
        {"title": "Radial Similarity Gauge", "desc": "Visual circular SVG gauge displaying TF-IDF Cosine Match percentage, level, and Jaccard baseline readout."},
        {"title": "Categorized Skill Badges", "desc": "Interactive skill badges using Green (Matched), Amber (Missing Gaps), and Blue (Extra Resume Skills)."},
        {"title": "Personalized Skill Roadmap", "desc": "Actionable practice project table for missing skills with interactive status buttons (Not Started, In Progress, Completed)."},
        {"title": "SQLite History Log", "desc": "Searchable history log table storing past analysis runs with detail view modal and single-click deletion."},
        {"title": "Model Evaluation Page", "desc": "Hyperparameter documentation, benchmark baseline comparison, precision/recall metrics, and limitations."}
    ]
    create_grid_slide(17, "Application Dashboard & Interface Panels", ui_panels, "Slide 17 illustrates the user interface layout of our React application. The interface contains five main panels: First, an Interactive Dual-Pane Editor for uploading resumes and entering job descriptions; Second, a Radial SVG Similarity Gauge displaying the Cosine match percentage and qualitative level; Third, Categorized Skill Badges using green for matched, amber for missing, and blue for extra skills; Fourth, an Interactive Learning Roadmap table where users toggle skill progress; and Fifth, an Analysis History Log and Model Evaluation Page.")

    # ==========================================
    # SLIDE 18: CHALLENGES & TECHNICAL SOLUTIONS
    # ==========================================
    s18 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s18)
    add_header(s18, "Challenges Encountered & Technical Solutions")

    table_shape_c = s18.shapes.add_table(6, 3, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.2))
    table_c = table_shape_c.table
    table_c.columns[0].width = Inches(3.2)
    table_c.columns[1].width = Inches(3.5)
    table_c.columns[2].width = Inches(5.033)

    c_headers = ["Challenge Encountered", "Technical Approach", "Implemented Solution"]
    for idx, h in enumerate(c_headers):
        cell = table_c.cell(0, idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_CARD
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEAL

    c_rows = [
        ("Special Symbol Destruction\nRegex strips +, # from C++, C#, .NET", "Technical Token Preservation", "Built pre-tokenization regex mapper converting C++ -> cplusplus, C# -> csharp, .NET -> dotnet."),
        ("Synonym Phrasing Variance\nCandidates write React.js vs React", "Canonical Dictionary Mapping", "Created skills.json catalog mapping variations (React.js, ReactJS) to standard skill React."),
        ("Unreadable Image PDFs\nScanned image PDFs extract 0 text", "Exception Safeguards & Validation", "Implemented 0-character page detection returning clear diagnostic guidance."),
        ("Candidate PII Exposure\nStoring emails/phones exposes PII", "Automated Privacy Masking", "Built regex sanitization replacing emails, phone numbers, and URLs with placeholders."),
        ("Over-fitting Keyword Counts\nRepeated keywords distort scores", "Sublinear TF Dampening", "Configured Scikit-Learn sublinear_tf=True (1 + log(TF)) to dampen term frequencies.")
    ]

    for r_idx, r_data in enumerate(c_rows):
        for c_idx, val in enumerate(r_data):
            cell = table_c.cell(r_idx+1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9)
            p.font.color.rgb = COLOR_TEXT

    add_notes(s18, "During implementation, we encountered five key technical challenges: First, standard tokenization destroyed special programming symbols like C++ and C#. We solved this using pre-tokenization regex preservation. Second, synonym variance caused identical skills to be missed. We solved this with a canonical dictionary lookup. Third, scanned image PDFs produced zero text. We implemented page content validation safeguards. Fourth, storing contact details posed privacy concerns. We built automated PII regex masking. Fifth, keyword repetition distorted scores. We applied sublinear term frequency dampening.")

    # ==========================================
    # SLIDE 19: SKILLS ACQUIRED & LEARNING OUTCOMES
    # ==========================================
    s19 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s19)
    add_header(s19, "Skills Acquired & Internship Learning Outcomes")

    outcomes = [
        ("Technical Mastery", [
            "Python 3.14 advanced scripting & module design",
            "Scikit-Learn TF-IDF vectorization & Cosine math",
            "Natural Language Processing (tokenization, cleaning)",
            "FastAPI REST API design & Pydantic validation",
            "React.js 18 frontend dashboard development"
        ], COLOR_TEAL),
        ("Practical Engineering", [
            "Complete Machine Learning lifecycle execution",
            "Unstructured PDF/DOCX document parsing",
            "SQLite relational database design & SQLAlchemy ORM",
            "Automated unit testing with Pytest (12/12 passed)",
            "PII privacy protection implementation"
        ], COLOR_EMERALD),
        ("Professional Skills", [
            "Analytical thinking & problem solving",
            "Systematic software debugging & testing",
            "Technical documentation & API design",
            "Academic presentation & viva defense",
            "Ethical AI guidelines implementation"
        ], COLOR_CYAN)
    ]

    for idx, (title_o, items_o, color_o) in enumerate(outcomes):
        x = Inches(0.8 + idx * 4.0)
        box = s19.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.5), Inches(3.733), Inches(5.2))
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD
        box.line.color.rgb = color_o

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p0 = tf.paragraphs[0]
        p0.text = title_o
        p0.font.size = Pt(14)
        p0.font.bold = True
        p0.font.color.rgb = color_o
        p0.space_after = Pt(12)

        for item_o in items_o:
            p = tf.add_paragraph()
            p.text = "• " + item_o
            p.font.size = Pt(10)
            p.font.color.rgb = COLOR_TEXT
            p.space_after = Pt(8)

    add_notes(s19, "This internship provided immense learning outcomes across three dimensions: Technical Mastery, Practical Engineering, and Professional Skills. Technically, I mastered Python-based NLP, Scikit-Learn TF-IDF vectorization, Cosine Similarity math, FastAPI, and React.js. Practically, I learned how to handle unstructured real-world document parsing, build REST APIs, integrate databases using SQLAlchemy, and write unit tests with Pytest. Professionally, I strengthened my problem-solving ability, technical documentation, and academic presentation skills.")

    # ==========================================
    # SLIDE 20: CONCLUSION & FUTURE SCOPE
    # ==========================================
    s20 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s20)
    add_header(s20, "Conclusion & Future Enhancements")

    # Left: Conclusion
    c_con = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    c_con.fill.solid()
    c_con.fill.fore_color.rgb = COLOR_CARD
    tf_co = c_con.text_frame
    tf_co.margin_left = Inches(0.3)
    tf_co.margin_top = Inches(0.3)

    p = tf_co.paragraphs[0]
    p.text = "Project Conclusion Summary"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(12)

    conclusions = [
        "Developed and verified an AI-Based Resume Screening and Job Matching System.",
        "Applied TF-IDF vectorization and Cosine Similarity to compute text similarity scores.",
        "Created a transparent skill catalog dictionary supporting phrase boundary regex and canonical synonyms.",
        "Built an interactive skill-gap learning roadmap with persistent SQLite status tracking.",
        "Achieved 100% test pass rate across 12 automated Pytest unit and integration tests."
    ]
    for c in conclusions:
        p = tf_co.add_paragraph()
        p.text = "• " + c
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(8)

    # Right: Future Scope
    c_fut = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    c_fut.fill.solid()
    c_fut.fill.fore_color.rgb = COLOR_CARD
    tf_fu = c_fut.text_frame
    tf_fu.margin_left = Inches(0.3)
    tf_fu.margin_top = Inches(0.3)

    p = tf_fu.paragraphs[0]
    p.text = "Future Scope & Enhancements"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_CYAN
    p.space_after = Pt(12)

    futures = [
        "Semantic Transformer Integration: Incorporate Sentence-BERT (all-MiniLM-L6-v2) embeddings for deep contextual similarity.",
        "Negation Detection: Add dependency parsing to recognize phrases like 'not familiar with Docker'.",
        "Expanded Skill Catalog: Broaden skill dictionary across specialized engineering domains.",
        "Cloud Hosting: Deploy FastAPI backend to Render/Koyeb and React frontend to Vercel/Netlify for 24/7 public access."
    ]
    for f in futures:
        p = tf_fu.add_paragraph()
        p.text = "• " + f
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_TEXT
        p.space_after = Pt(8)

    p = tf_fu.add_paragraph()
    p.text = "\nTHANK YOU! Questions & Discussion Welcome."
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL

    add_notes(s20, "In conclusion, this internship project successfully bridges the gap between candidate resumes and job descriptions using Natural Language Processing and Machine Learning. We developed a working system that extracts skills, measures TF-IDF vector similarity, identifies skill gaps, and guides student preparation—all while maintaining data privacy and ethical disclaimers. In the future, we plan to incorporate advanced transformer models like Sentence-BERT for deeper contextual understanding and expand our skill dictionary. I extend my sincere gratitude to InternPe, our department, and my faculty guide Smt. Y. Supriya Reddy ma'am for their constant support. Thank you, and I am now open to any questions.")

    output_path = os.path.join(os.path.dirname(__file__), "..", "AI_Based_Resume_Screening_Internship_Presentation_Meda_Geethika.pptx")
    prs.save(output_path)
    print(f"Presentation successfully saved to: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    create_presentation()
