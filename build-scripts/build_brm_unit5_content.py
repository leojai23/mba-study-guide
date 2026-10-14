# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Business-Research-Methods\units"
BOOK_HTML = "Book: <em>Business Research Methods</em> (BA4205, Anna University MBA Sem II, Regulation 2021)"
BOOK_PLAIN = "Business Research Methods (BA4205), Dr. T. Vetrivel &amp; Dr. P. Priyadarsini, Thakur Publication"

TOPICS = [
    ("topic1-the-research-report.html", "The Research Report"),
    ("topic2-report-structure-front-matter.html", "Report Structure: Front Matter"),
    ("topic3-report-structure-findings-and-closing.html", "Report Structure: Findings and Closing"),
    ("topic4-report-writing-process.html", "Report Writing Process"),
    ("topic5-ethics-in-business-research.html", "Ethics in Business Research"),
]

WINE_THEME = dict(accent="#7a1f3d", accent_dark="#4d1326", accent_light="#faebf0",
                   border="#f0d7df", shadow="rgba(122,31,61,.14)")

U = common.UnitBuilder(5, "Report Design, Writing and Ethics in Business Research", TOPICS,
                        subject="Business Research Methods",
                        subject_root=SUBJECT_ROOT,
                        book_html=BOOK_HTML, book_plain=BOOK_PLAIN, theme=WINE_THEME)

def T(i):
    fname, title = TOPICS[i-1]
    prev_link = (TOPICS[i-2][0], TOPICS[i-2][1]) if i > 1 else None
    next_link = (TOPICS[i][0], TOPICS[i][1]) if i < len(TOPICS) else None
    return fname, title, prev_link, next_link

# ================= Topic 1 =================
fname, title, prev_link, next_link = T(1)
overview = ("A research study is only as useful as the report that communicates it. This topic covers what "
            "a research report is, what makes it good, the functions it serves, its main types, and why "
            "report writing matters.")
notes = """
<h3>1.1 Introduction to the Research Report</h3>
<p>A research report is the formal written document that communicates the purpose, methodology, findings and conclusions of a research study to its intended audience, translating analysis into a form that can inform decisions.</p>

<h3>1.2 Characteristics of a Good Research Report</h3>
<ul>
<li>Clear and precise in language, avoiding unnecessary jargon.</li>
<li>Logically organised, with a structure the reader can follow easily.</li>
<li>Accurate and objective, fairly representing the data and its limitations.</li>
<li>Complete, covering the full research process from problem to conclusion.</li>
<li>Concise, presenting information efficiently without padding.</li>
</ul>

<h3>1.3 Function of Reports</h3>
<ul>
<li>Communicates research findings to decision-makers who did not conduct the study themselves.</li>
<li>Provides a permanent record of the research for future reference.</li>
<li>Serves as the basis for managerial action and policy decisions.</li>
<li>Allows the research methodology to be reviewed and, if needed, replicated.</li>
</ul>

<h3>1.4 Types of Reports</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Technical Report</strong></td><td>Detailed, methodologically thorough, written for researchers/specialists.</td></tr>
<tr><td><strong>Popular/Management Report</strong></td><td>Simplified, emphasises findings and recommendations, written for non-technical management readers.</td></tr>
<tr><td><strong>Interim Report</strong></td><td>A progress update issued before the study is complete.</td></tr>
<tr><td><strong>Final Report</strong></td><td>The complete, conclusive report issued at the end of the study.</td></tr>
<tr><td><strong>Oral Report</strong></td><td>A verbal presentation of findings, often supported by a written summary and slides.</td></tr>
</table>

<h3>1.5 Contents of a Report</h3>
<p>At a minimum, a report should cover: the title and purpose of the study, the research methodology used, the key findings, the conclusions drawn, and recommendations for action.</p>

<h3>1.6 Importance of Report Writing</h3>
<p>No matter how rigorous the underlying research, its value is realised only when it is clearly communicated to those who will act on it. A well-written report builds the credibility of the research, ensures findings are correctly understood, and provides a lasting, reviewable record that supports informed managerial decision-making.</p>
"""
terms = [
    ("Research Report", "The formal written document that communicates the purpose, methodology, findings and conclusions of a research study."),
    ("Technical Report", "A detailed, methodologically thorough report written for researchers or specialists."),
    ("Popular/Management Report", "A simplified report emphasising findings and recommendations, written for non-technical management readers."),
]
examprep = [
    "Research report = formal document communicating purpose, method, findings, conclusions.",
    "Good report: clear, logically organised, accurate/objective, complete, concise.",
    "Report types: technical vs popular/management; interim vs final; written vs oral.",
    "Minimum contents: title/purpose, methodology, findings, conclusions, recommendations.",
]
questions = [
    ("What are the characteristics of a good research report?", "A good research report is clear and precise in language, logically organised so the reader can follow it easily, accurate and objective in representing the data and its limitations, complete in covering the full research process, and concise in presenting information without unnecessary padding."),
    ("Differentiate between a technical report and a popular (management) report.", "A technical report is detailed and methodologically thorough, written for researchers or specialists who need to evaluate the methods used. A popular or management report is simplified, emphasising findings and recommendations over methodological detail, and is written for non-technical management readers who need to act on the results."),
    ("Why is report writing important in the research process?", "Report writing is important because the value of research is only realised once it is clearly communicated to decision-makers. A well-written report builds the credibility of the research, ensures findings are correctly understood, and provides a lasting, reviewable record that supports informed managerial action."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("This topic covers the opening sections of a standard research report format &mdash; everything "
            "from the title page through to the statement of the research method, which together orient "
            "the reader before the findings are presented.")
notes = """
<h3>2.1 Introduction to Report Structure</h3>
<p>While exact formats vary by organisation, most research reports follow a broadly standard structure so that readers familiar with research reports in general can quickly locate the section they need.</p>

<h3>2.2 Title of the Report</h3>
<p>The title should concisely and accurately convey the subject of the study, be specific enough to distinguish it from other work, and avoid unnecessary jargon.</p>

<h3>2.3 Table of Contents and Chapterisation</h3>
<p>The table of contents lists every major section and sub-section with page numbers, organised into a logical chapter structure (e.g. Introduction, Literature Review, Methodology, Findings, Conclusions) so the reader can navigate the report efficiently.</p>

<h3>2.4 Contents of Each Chapter</h3>
<p>Each chapter should open with a brief statement of its purpose, be organised under clear sub-headings, and close with a short summary or transition to the next chapter where useful.</p>

<h3>2.5 Executive Summary</h3>
<p>A concise, self-contained overview &mdash; typically one to two pages &mdash; of the problem, method, key findings and recommendations, written so a busy reader can grasp the essentials without reading the full report.</p>

<h3>2.6 Introduction to the Report</h3>
<p>Sets the context for the study: the background of the problem, why it matters to the organisation, and an outline of what the rest of the report covers.</p>

<h3>2.7 Statement of Objectives</h3>
<p>Clearly lists the specific objectives the research was designed to achieve, giving the reader a yardstick against which to judge whether the study succeeded.</p>

<h3>2.8 Literature Review: Analysis of Previous Research</h3>
<p>Summarises and critically evaluates prior research relevant to the problem, showing how the current study builds on, differs from, or fills a gap left by earlier work.</p>

<h3>2.9 Research Method</h3>
<p>Describes the research design used, the sampling plan, the data collection methods and instruments, and the analytical techniques applied &mdash; in enough detail that a reader could assess (or replicate) the approach.</p>
"""
terms = [
    ("Executive Summary", "A concise, self-contained overview of a report's problem, method, findings and recommendations."),
    ("Literature Review", "A section summarising and critically evaluating prior research relevant to the current study's problem."),
]
examprep = [
    "Front matter sequence: title &rarr; table of contents/chapterisation &rarr; chapter contents &rarr; executive summary &rarr; introduction &rarr; objectives &rarr; literature review &rarr; research method.",
    "Executive summary = short, self-contained, covers problem/method/findings/recommendations.",
    "Literature review = evaluates prior research, shows how the current study fits in.",
    "Research method section = design, sampling, data collection, analysis techniques, detailed enough to assess/replicate.",
]
questions = [
    ("What is the purpose of the executive summary in a research report?", "The executive summary is a concise, self-contained overview, typically one to two pages, covering the research problem, method, key findings and recommendations. It allows a busy reader, such as senior management, to grasp the essential conclusions of the study without reading the full report."),
    ("What should the research method section of a report contain?", "The research method section should describe the research design used, the sampling plan, the data collection methods and instruments employed, and the analytical techniques applied, in sufficient detail that a reader can assess the soundness of the approach or replicate the study."),
    ("Explain the role of the literature review in a research report.", "The literature review summarises and critically evaluates prior research relevant to the current problem, showing how the current study builds on, differs from, or fills a gap left by earlier work, and thereby justifying the need for the present research."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("Continuing the report structure, this topic covers the sections that present and close out the "
            "research: interpretation of results, conclusions, recommendations, limitations, and references."
            )
notes = """
<h3>3.1 Interpretation of Results</h3>
<p>Explains what the analysed data actually means in the context of the research objectives &mdash; going beyond raw statistics to explain their practical significance for the business problem under study.</p>

<h3>3.2 Conclusions</h3>
<p>States, clearly and directly, the answers the study has found to its research questions, each conclusion tied back to specific findings presented earlier in the report.</p>

<h3>3.3 Suggestions and Recommendations</h3>
<p>Translates the conclusions into specific, actionable recommendations for management, ideally prioritised and, where possible, linked to an estimate of their likely impact or feasibility.</p>

<h3>3.4 Limitations of the Study</h3>
<p>Honestly states the constraints that may affect how far the findings can be generalised or relied upon &mdash; such as sample size, geographic scope, time period, or methodological constraints &mdash; so readers can correctly judge the findings' applicability.</p>

<h3>3.5 Reference Section</h3>
<p>Lists, in a consistent citation format, every source cited in the report &mdash; books, journal articles, reports and websites &mdash; allowing readers to locate the original material and verify claims.</p>

<h3>3.6 Putting It Together: Report Format Flow</h3>
<table class="compare">
<tr><th>Section Group</th><th>Purpose</th></tr>
<tr><td>Front matter (Title &rarr; Research Method)</td><td>Orients the reader: what was studied, why, and how.</td></tr>
<tr><td>Results and closing (Interpretation &rarr; References)</td><td>Presents what was found and what should be done about it.</td></tr>
</table>
"""
terms = [
    ("Interpretation of Results", "The section of a report that explains what analysed data means in the context of the research objectives."),
    ("Recommendations", "Specific, actionable suggestions for management derived from a study's conclusions."),
    ("Limitations of the Study", "An honest statement of the constraints affecting how far a study's findings can be generalised or relied upon."),
]
examprep = [
    "Closing sequence: interpretation of results &rarr; conclusions &rarr; suggestions/recommendations &rarr; limitations &rarr; reference section.",
    "Conclusions = direct answers to research questions, tied to specific findings.",
    "Recommendations = actionable, ideally prioritised by impact/feasibility.",
    "Limitations section = honestly states constraints (sample size, scope, time, method) affecting generalisability.",
]
questions = [
    ("Why must a research report include a section on its own limitations?", "A report must honestly state its limitations, such as sample size, geographic scope, time period or methodological constraints, so that readers can correctly judge how far the findings can be generalised or relied upon, rather than over-applying conclusions beyond what the study actually supports."),
    ("Distinguish between conclusions and recommendations in a research report.", "Conclusions are direct, evidence-based answers to the research questions, each tied back to specific findings. Recommendations go a step further, translating those conclusions into specific, actionable suggestions for management, ideally prioritised by their likely impact or feasibility."),
    ("What is the purpose of the reference section in a report?", "The reference section lists, in a consistent citation format, every source cited in the report, allowing readers to locate the original material, verify claims, and assess how the current study relates to prior work."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("Beyond deciding what sections to include, writing an effective report requires attention to "
            "process, audience, tone and presentation. This topic covers the practical craft of report "
            "writing."
            )
notes = """
<h3>4.1 Introduction to Report Writing</h3>
<p>Report writing is the process of translating research findings into a document that communicates clearly and persuasively to its intended readers, requiring as much care as the research itself.</p>

<h3>4.2 Process of Writing Research Reports</h3>
<ol>
<li>Organise the findings and supporting data logically before drafting begins.</li>
<li>Prepare a detailed outline matching the report's intended structure.</li>
<li>Write the first draft, following the outline section by section.</li>
<li>Revise for clarity, accuracy, and logical flow.</li>
<li>Proofread and format the final version.</li>
</ol>

<h3>4.3 Writing the Draft</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Role of Audience</h4>
<p>The language, level of technical detail, and emphasis of the report should be tailored to who will read it &mdash; a technical report for researchers can use statistical terminology freely, while a management report should minimise jargon and foreground implications for decisions.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Comprehension</h4>
<p>Use clear, simple sentence structure, define technical terms when first used, and support complex findings with charts or tables so they are easier to grasp.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Tone</h4>
<p>Maintain an objective, professional tone throughout, presenting both supporting and contradicting evidence fairly rather than only evidence that favours a particular conclusion.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Final Proof</h4>
<p>Carefully proofread the final draft for factual accuracy, consistency between the text and any figures/tables, correct referencing, and grammar/spelling errors before submission.</p>

<h3>4.4 Presentation Considerations</h3>
<ul>
<li>Use headings, white space and consistent formatting to make the report easy to navigate.</li>
<li>Use charts, graphs and tables to present quantitative findings more clearly than text alone.</li>
<li>Keep visual elements simple, correctly labelled, and directly relevant to the point being made.</li>
</ul>

<h3>4.5 Precautions in Writing the Report</h3>
<ul>
<li>Avoid overstating conclusions beyond what the data actually supports.</li>
<li>Avoid excessive technical jargon when writing for a non-technical audience.</li>
<li>Ensure every claim in the report is traceable back to the underlying data or a cited source.</li>
<li>Avoid presenting personal opinion as if it were a research finding.</li>
</ul>
"""
terms = [
    ("Report Writing", "The process of translating research findings into a document that communicates clearly and persuasively to its intended readers."),
]
examprep = [
    "Writing process: organise findings &rarr; outline &rarr; draft &rarr; revise &rarr; proofread/format.",
    "Tailor language/detail to the audience: technical report vs management report.",
    "Maintain objective tone: present both supporting and contradicting evidence fairly.",
    "Precautions: don't overstate conclusions, avoid excess jargon, keep claims traceable to data, avoid stating opinion as finding.",
]
questions = [
    ("Why must the role of the audience be considered when writing a research report?", "The language, level of technical detail and emphasis of a report should be tailored to its readers. A technical report for fellow researchers can use statistical terminology freely, while a management report should minimise jargon and foreground the practical implications for decisions, since the two audiences need the findings communicated differently."),
    ("What precautions should be taken while writing a research report?", "Writers should avoid overstating conclusions beyond what the data actually supports, avoid excessive technical jargon when writing for a non-technical audience, ensure every claim is traceable back to underlying data or a cited source, and avoid presenting personal opinion as if it were a research finding."),
    ("Outline the process of writing a research report.", "The process begins with organising the findings and supporting data logically, preparing a detailed outline matching the report's structure, writing the first draft section by section, revising for clarity and logical flow, and finally proofreading and formatting the finished version."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("The final topic of the course addresses research ethics &mdash; the principles that govern "
            "how research should be conducted and reported responsibly, and the balance between "
            "subjectivity and objectivity in the research process.")
notes = """
<h3>5.1 Introduction to Ethics in Research</h3>
<p>Research ethics are the moral principles that guide how a study is designed, conducted and reported, ensuring that participants, clients and the broader public are treated fairly and that findings can be trusted.</p>

<h3>5.2 Principles of Ethical Research</h3>
<ul>
<li><strong>Informed consent</strong> &mdash; participants should understand and voluntarily agree to take part.</li>
<li><strong>Confidentiality and privacy</strong> &mdash; respondent data should be protected and used only for its stated purpose.</li>
<li><strong>Avoidance of harm</strong> &mdash; the research process should not cause physical, psychological or financial harm to participants.</li>
<li><strong>Honesty and transparency</strong> &mdash; findings must be reported accurately, including results that do not support the researcher's expectations.</li>
<li><strong>Avoidance of deception</strong> &mdash; participants should not be misled about the nature or purpose of the study without strong justification and appropriate debriefing.</li>
</ul>

<h3>5.3 Ethical Behaviour of the Researcher</h3>
<p>An ethical researcher avoids data fabrication or manipulation, properly credits the work of others through accurate citation, discloses any conflicts of interest, and respects the rights and dignity of respondents throughout the study.</p>

<h3>5.4 Subjectivity in Research</h3>
<p>Subjectivity refers to the influence of the researcher's own beliefs, expectations or interests on how a study is designed, data is interpreted, or conclusions are framed. Some subjectivity is unavoidable (e.g. in choosing what to study), but uncontrolled subjectivity can bias findings.</p>

<h3>5.5 Objectivity in Research</h3>
<p>Objectivity is the practice of basing conclusions strictly on the evidence, using methods and reasoning that another researcher could independently verify, and actively guarding against the influence of personal bias on the results.</p>

<h3>5.6 Significance of Ethics in Research</h3>
<ul>
<li>Protects the rights, dignity and wellbeing of research participants.</li>
<li>Maintains the credibility and trustworthiness of research findings.</li>
<li>Protects the reputation of the researcher and the sponsoring organisation.</li>
<li>Ensures research can be built upon reliably by future studies.</li>
</ul>
"""
terms = [
    ("Research Ethics", "The moral principles that guide how a study is designed, conducted and reported, protecting participants and the integrity of findings."),
    ("Informed Consent", "The principle that research participants should understand and voluntarily agree to take part in a study."),
    ("Subjectivity (in Research)", "The influence of a researcher's own beliefs, expectations or interests on the design, interpretation or framing of a study."),
    ("Objectivity (in Research)", "The practice of basing research conclusions strictly on verifiable evidence, free from personal bias."),
]
examprep = [
    "Ethical principles: informed consent, confidentiality/privacy, avoidance of harm, honesty/transparency, avoidance of deception.",
    "Ethical researcher behaviour: no data fabrication, proper citation, disclosed conflicts of interest, respect for respondents.",
    "Subjectivity = researcher's own beliefs/bias influencing the study; Objectivity = conclusions based strictly on evidence.",
    "Ethics matters for: participant protection, research credibility, researcher/organisation reputation, future research reliability.",
]
questions = [
    ("What are the key principles of ethical research?", "Key principles include informed consent (participants understand and voluntarily agree to take part), confidentiality and privacy of respondent data, avoidance of harm to participants, honesty and transparency in reporting findings (including unfavourable results), and avoidance of deception without strong justification and proper debriefing."),
    ("Distinguish between subjectivity and objectivity in research.", "Subjectivity refers to the influence of the researcher's own beliefs, expectations or interests on how a study is designed, data is interpreted, or conclusions are framed. Objectivity is the practice of basing conclusions strictly on verifiable evidence using methods another researcher could independently check, actively guarding against personal bias."),
    ("Why is ethics significant in business research?", "Ethics in research protects the rights, dignity and wellbeing of research participants, maintains the credibility and trustworthiness of the findings, protects the reputation of the researcher and sponsoring organisation, and ensures that the research can be reliably built upon by future studies."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

U.write_index("Book: <em>Business Research Methods</em> (BA4205) &middot; Unit 5 covers the research report, its structure, the report writing process, and ethics in business research.")
print("Unit 5 index done")
