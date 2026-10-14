# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Business-Research-Methods\units"
BOOK_HTML = "Book: <em>Business Research Methods</em> (BA4205, Anna University MBA Sem II, Regulation 2021)"
BOOK_PLAIN = "Business Research Methods (BA4205), Dr. T. Vetrivel &amp; Dr. P. Priyadarsini, Thakur Publication"

TOPICS = [
    ("topic1-introduction-to-research.html", "Introduction to Research"),
    ("topic2-business-research.html", "Business Research"),
    ("topic3-types-of-research.html", "Types of Research"),
    ("topic4-research-problem.html", "The Research Problem"),
    ("topic5-research-objectives-and-hypotheses.html", "Research Objectives and Hypotheses"),
    ("topic6-theory-and-research.html", "Theory and Research"),
]

WINE_THEME = dict(accent="#7a1f3d", accent_dark="#4d1326", accent_light="#faebf0",
                   border="#f0d7df", shadow="rgba(122,31,61,.14)")

U = common.UnitBuilder(1, "Introduction to Business Research", TOPICS,
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
overview = ("This opening topic introduces research itself &mdash; what it means, why organisations undertake "
            "it, the broad process it follows, and how the idea of research has evolved over time.")
notes = """
<h3>1.1 Introduction to Research</h3>
<p>Research is a systematic, organised and objective process of inquiry undertaken to find answers to questions or solutions to problems. It involves the careful collection, recording and analysis of data in order to establish facts, verify existing knowledge, or develop new understanding.</p>

<h3>1.2 Nature of Research</h3>
<ul>
<li><strong>Systematic</strong> &mdash; follows a planned, step-by-step process rather than random inquiry.</li>
<li><strong>Objective</strong> &mdash; aims to minimise personal bias and rely on verifiable evidence.</li>
<li><strong>Empirical</strong> &mdash; grounded in observation and data, not mere opinion.</li>
<li><strong>Logical</strong> &mdash; proceeds through reasoned, replicable steps.</li>
<li><strong>Analytical</strong> &mdash; uses appropriate methods to critically evaluate data and draw conclusions.</li>
</ul>

<h3>1.3 Objectives of Research</h3>
<ul>
<li>To gain familiarity with a phenomenon or achieve new insights into it (exploratory objective).</li>
<li>To accurately portray the characteristics of a particular individual, group or situation (descriptive objective).</li>
<li>To determine the frequency with which something occurs or with which it is associated with something else (diagnostic objective).</li>
<li>To test a hypothesis of a causal relationship between variables (hypothesis-testing objective).</li>
</ul>

<h3>1.4 Research Process</h3>
<p>Although the exact steps vary by study, research generally follows this broad sequence:</p>
<ol>
<li>Identifying and formulating the research problem.</li>
<li>Reviewing the related literature.</li>
<li>Formulating a hypothesis (where applicable).</li>
<li>Designing the research (choosing the research design and methodology).</li>
<li>Collecting the data.</li>
<li>Analysing the data.</li>
<li>Interpreting the results and drawing conclusions.</li>
<li>Preparing and presenting the research report.</li>
</ol>

<h3>1.5 Significance of Research</h3>
<ul>
<li>Provides the basis for almost all management decisions by replacing guesswork with evidence.</li>
<li>Helps identify and solve operational and strategic business problems.</li>
<li>Provides a rational, systematic basis for decision-making in uncertain conditions.</li>
<li>Generates new knowledge and contributes to the overall body of theory in a field.</li>
<li>Supports policy formulation at both organisational and governmental levels.</li>
</ul>

<h3>1.6 Limitations of Research</h3>
<ul>
<li>Findings are often specific to the time, place and context studied, limiting generalisability.</li>
<li>Constrained by the availability of time, money and skilled personnel.</li>
<li>Data quality depends on respondent honesty and researcher objectivity, both of which can introduce error.</li>
<li>Complex social and business phenomena cannot always be fully captured through measurement.</li>
</ul>

<h3>1.7 Research in an Evolutionary Perspective</h3>
<p>Research as a formal discipline has evolved from simple trial-and-error problem solving in ancient times, through the development of the scientific method during the Renaissance and Enlightenment, to today's highly specialised, technology-enabled research methodologies. In business, research has grown from basic record-keeping and intuition-based decisions into a structured management function supported by statistics, computing and dedicated research departments.</p>
"""
terms = [
    ("Research", "A systematic, objective and organised process of inquiry undertaken to find answers to questions or solutions to problems."),
    ("Exploratory Objective", "A research objective aimed at gaining familiarity with, or new insight into, a phenomenon."),
    ("Descriptive Objective", "A research objective aimed at accurately portraying the characteristics of an individual, group or situation."),
    ("Diagnostic Objective", "A research objective aimed at determining the frequency of occurrence or association between variables."),
]
examprep = [
    "Research = systematic + objective + empirical + logical + analytical inquiry.",
    "Four objectives: exploratory, descriptive, diagnostic, hypothesis-testing.",
    "Research process: problem &rarr; literature review &rarr; hypothesis &rarr; design &rarr; data collection &rarr; analysis &rarr; interpretation &rarr; report.",
    "Significance: basis for decisions, problem-solving, new knowledge, policy formulation.",
    "Limitations: context-specific findings, resource constraints, data-quality dependence.",
]
questions = [
    ("Define research and explain its nature.", "Research is a systematic, objective and organised process of inquiry undertaken to find answers to questions or solutions to problems through the collection, recording and analysis of data. Its nature is systematic, objective, empirical, logical and analytical."),
    ("What are the main objectives of research?", "Research has four broad objectives: exploratory (gaining familiarity with a phenomenon), descriptive (accurately portraying characteristics), diagnostic (determining frequency or association), and hypothesis-testing (testing a causal relationship between variables)."),
    ("Outline the steps in the research process.", "The research process typically moves through: identifying and formulating the problem, reviewing related literature, formulating a hypothesis, designing the research, collecting data, analysing data, interpreting results, and preparing the research report."),
    ("Discuss the significance and limitations of research in business.", "Research provides a rational, evidence-based foundation for management decisions, helps solve operational problems and generates new knowledge, but is limited by context-specific findings, constraints of time/money/skill, and dependence on data quality and researcher objectivity."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("This topic narrows the focus from research in general to business research specifically &mdash; "
            "its meaning, the value it creates for management, and the factors that shape how it is carried "
            "out within organisations.")
notes = """
<h3>2.1 Meaning and Definition of Business Research</h3>
<p>Business research is the systematic and objective process of gathering, recording and analysing data to assist in making business decisions. It applies the general principles of research to problems specific to business functions such as marketing, finance, operations and human resources.</p>

<h3>2.2 Nature of Business Research</h3>
<ul>
<li>Applied in orientation &mdash; directed at solving a practical business problem rather than pure theory-building.</li>
<li>Decision-oriented &mdash; findings are meant to support a specific managerial decision.</li>
<li>Interdisciplinary &mdash; draws on economics, statistics, psychology, sociology and management theory.</li>
<li>Time-bound &mdash; usually conducted under practical deadlines imposed by the decision it supports.</li>
</ul>

<h3>2.3 Objectives of Business Research</h3>
<ul>
<li>To identify and define business problems and opportunities.</li>
<li>To generate, refine and evaluate possible courses of managerial action.</li>
<li>To monitor performance and understand the business environment.</li>
<li>To improve the overall understanding of business processes as a body of knowledge.</li>
</ul>

<h3>2.4 Scope of Business Research</h3>
<p>Business research spans virtually every functional area: marketing research (consumer behaviour, demand forecasting), financial research (investment analysis, risk assessment), human resource research (employee satisfaction, performance), production/operations research (quality, productivity), and research into the general business environment (economic, legal, social and technological factors).</p>

<h3>2.5 Managerial Value and Significance of Business Research</h3>
<ul>
<li>Reduces uncertainty and risk by replacing intuition with systematic evidence.</li>
<li>Identifies problems early, before they escalate into crises.</li>
<li>Reveals new opportunities for products, markets or efficiency improvements.</li>
<li>Improves the quality and speed of managerial decision-making.</li>
<li>Helps evaluate the outcomes of past decisions, enabling continuous improvement.</li>
</ul>

<h3>2.6 Factors Affecting Business Research</h3>
<table class="compare">
<tr><th>Factor</th><th>Effect on Research</th></tr>
<tr><td><strong>Time constraints</strong></td><td>Tight decision deadlines may force a less rigorous, faster design.</td></tr>
<tr><td><strong>Budget</strong></td><td>Available funds limit sample size, data sources and methods used.</td></tr>
<tr><td><strong>Availability of data</strong></td><td>Access to reliable primary or secondary data shapes what questions can be answered.</td></tr>
<tr><td><strong>Management support</strong></td><td>Lack of top management buy-in can limit resources and the use of findings.</td></tr>
<tr><td><strong>Nature of the decision</strong></td><td>High-stakes, irreversible decisions justify more rigorous, costlier research.</td></tr>
<tr><td><strong>Ethical and legal considerations</strong></td><td>Privacy, confidentiality and regulatory requirements constrain data collection methods.</td></tr>
</table>
"""
terms = [
    ("Business Research", "The systematic and objective process of gathering, recording and analysing data to assist in making business decisions."),
    ("Marketing Research", "Business research focused on consumer behaviour, demand and market conditions."),
    ("Decision-Oriented Research", "Research explicitly designed to support a specific managerial decision rather than pure knowledge-building."),
]
examprep = [
    "Business research = systematic, applied, decision-oriented research for business problems.",
    "Scope: marketing, finance, HR, production/operations, and the business environment.",
    "Value: reduces uncertainty, identifies problems/opportunities, improves decision quality.",
    "Key factors affecting it: time, budget, data availability, management support, decision stakes, ethics/law.",
]
questions = [
    ("Define business research. How does it differ from research in general?", "Business research is the systematic and objective process of gathering, recording and analysing data to assist specific business decisions. Unlike research in general, it is applied and decision-oriented, aimed at solving a practical managerial problem within a limited time frame rather than building pure theoretical knowledge."),
    ("Explain the managerial significance of business research.", "Business research reduces uncertainty by replacing intuition with evidence, helps identify problems and opportunities early, improves the quality and speed of decisions, and allows managers to evaluate the outcomes of earlier decisions for continuous improvement."),
    ("What factors affect how business research is conducted?", "Business research is shaped by time constraints, available budget, the availability and quality of data, the level of management support, the stakes of the decision being supported, and ethical or legal considerations around data collection."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("Research can be classified in several overlapping ways &mdash; by purpose, by method, and by "
            "the time dimension it covers. This topic surveys the major types used in business research.")
notes = """
<h3>3.1 Classification by Purpose</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Pure / Basic / Fundamental Research</strong></td><td>Undertaken purely to expand knowledge and understand principles, with no immediate practical application in mind.</td></tr>
<tr><td><strong>Applied / Practical / Need-Based / Action-Based Research</strong></td><td>Undertaken to solve a specific, immediate practical problem faced by an organisation.</td></tr>
<tr><td><strong>Theoretical Research</strong></td><td>Focused on developing or testing theory, often building on pure research.</td></tr>
</table>

<h3>3.2 Research by Rigour and Approach</h3>
<ul>
<li><strong>Empirical Research</strong> &mdash; based on observed and measured data/experience rather than theory alone.</li>
<li><strong>Scientific Research</strong> &mdash; follows the formal scientific method: observation, hypothesis, testing, conclusion.</li>
<li><strong>Social Research</strong> &mdash; studies human behaviour and social relationships, often using qualitative and quantitative methods together.</li>
<li><strong>Historical Research</strong> &mdash; studies past events and records to understand their causes and consequences.</li>
</ul>

<h3>3.3 Exploratory and Conclusive Research</h3>
<ul>
<li><strong>Exploratory / Formulative Research</strong> &mdash; conducted when the problem is not yet clearly defined, to gain insight and clarify the real issue before a more structured study.</li>
<li><strong>Conclusive Research</strong> &mdash; conducted once the problem is clearly defined, to provide information useful in reaching a decision. It has two sub-types:
  <ul>
  <li><strong>Descriptive / Statistical Research</strong> &mdash; describes characteristics of a population or phenomenon (the "what", "who", "when", "where").</li>
  <li><strong>Causal / Experimental / Explanatory Research</strong> &mdash; establishes cause-and-effect relationships between variables (the "why").</li>
  </ul>
</li>
</ul>

<h3>3.4 Research by Time Dimension</h3>
<ul>
<li><strong>Cross-Sectional Research</strong> &mdash; collects data from a sample at one single point in time, giving a "snapshot".</li>
<li><strong>Time-Series Research</strong> &mdash; collects data on the same variables repeatedly over a period of time, revealing trends and changes.</li>
</ul>

<h3>3.5 Other Types</h3>
<p>Other commonly cited types include <strong>case study research</strong> (in-depth study of a single unit or small number of units), <strong>survey research</strong> (structured data collection from a sample), and <strong>action research</strong> (research conducted by practitioners to improve their own practice in real time).</p>
"""
terms = [
    ("Pure/Basic Research", "Research undertaken purely to expand knowledge, with no immediate practical application."),
    ("Applied Research", "Research undertaken to solve a specific, immediate practical problem."),
    ("Exploratory Research", "Research conducted when a problem is not yet clearly defined, to gain insight before a structured study."),
    ("Descriptive Research", "Conclusive research that describes the characteristics of a population or phenomenon."),
    ("Causal Research", "Conclusive research that establishes cause-and-effect relationships between variables."),
]
examprep = [
    "By purpose: pure/basic vs applied/practical research.",
    "By definedness of problem: exploratory (ill-defined problem) vs conclusive (well-defined problem).",
    "Conclusive splits into descriptive (what/who/when/where) and causal (why).",
    "By time: cross-sectional (one point in time) vs time-series (repeated over time).",
    "Others: empirical, scientific, social, historical, case study, survey, action research.",
]
questions = [
    ("Distinguish between pure and applied research.", "Pure (basic/fundamental) research aims to expand knowledge and understand principles with no immediate practical use in mind, while applied (practical/need-based) research is directed at solving a specific, immediate problem faced by an organisation."),
    ("Differentiate between exploratory and conclusive research.", "Exploratory research is undertaken when a problem is not yet clearly defined, to gain insight and clarify the real issue. Conclusive research is undertaken once the problem is clearly defined, to provide decision-useful information, and splits further into descriptive research (describing characteristics) and causal research (establishing cause-and-effect)."),
    ("Explain cross-sectional and time-series research with examples.", "Cross-sectional research collects data from a sample at a single point in time, such as a one-time customer satisfaction survey. Time-series research collects data on the same variables repeatedly over time, such as tracking monthly sales figures over several years to identify trends."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("Every research study begins with a problem. This topic covers how a research problem is "
            "identified, its components, how it is defined precisely, and how it is redefined into "
            "answerable questions.")
notes = """
<h3>4.1 Components of a Research Problem</h3>
<ul>
<li>The unit of analysis or population affected.</li>
<li>The variables or factors involved.</li>
<li>The relationship being studied between those variables.</li>
<li>The environment or context within which the problem exists.</li>
</ul>

<h3>4.2 Identifying the Research Problem</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Major Sources for Identifying a Problem in Business Research</h4>
<ul>
<li>Personal experience and observation of business operations.</li>
<li>Discussions with managers, employees and customers.</li>
<li>Review of academic and trade literature.</li>
<li>Analysis of past data, reports and performance trends.</li>
<li>Feedback, complaints and suggestions from stakeholders.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Problem Identification Process</h4>
<p>Broadly: recognising a symptom (e.g. falling sales) &rarr; investigating possible underlying causes &rarr; narrowing down to the actual researchable problem.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Criteria for Identifying a Good Problem</h4>
<ul>
<li>Researchable &mdash; capable of being studied with available methods and resources.</li>
<li>Significant &mdash; addresses an issue of real managerial importance.</li>
<li>Specific and clear, not vague or overly broad.</li>
<li>Feasible within the available time and budget.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Precautions in Identification of a Research Problem</h4>
<p>Avoid problems that are too broad, already answered elsewhere, based on personal bias, or impossible to investigate with available data and resources.</p>

<h3>4.3 Defining the Research Problem</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Need for Problem Definition</h4>
<p>A precisely defined problem focuses the entire research effort; an ill-defined problem wastes time and resources collecting the wrong data.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Steps in Problem Definition</h4>
<ol>
<li>Understand the management decision that triggered the need for research.</li>
<li>Discuss the problem with relevant stakeholders.</li>
<li>Review any available secondary data.</li>
<li>State the problem in clear, specific, researchable terms.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Guidelines for Problem Definition</h4>
<p>State the problem in terms of a clear objective, avoid ambiguous terms, and ensure the problem is narrow enough to be addressed with the time and resources available.</p>

<h3>4.4 Redefining the Research Problem</h3>
<p>Once broadly defined, the problem is translated into a hierarchy of increasingly specific questions:</p>
<table class="compare">
<tr><th>Question Type</th><th>Description</th></tr>
<tr><td><strong>Management Questions</strong></td><td>What does the manager need to decide? (broadest level)</td></tr>
<tr><td><strong>Research Questions</strong></td><td>What information is needed to help answer the management question?</td></tr>
<tr><td><strong>Investigative Questions</strong></td><td>What specific sub-questions must be answered to address each research question?</td></tr>
<tr><td><strong>Measurement Questions</strong></td><td>What exact questions will be put to respondents or what data will be measured? (most specific level)</td></tr>
</table>
"""
terms = [
    ("Research Problem", "A specific issue or gap in knowledge that a research study is designed to investigate and resolve."),
    ("Management Question", "The broad decision-level question a manager needs answered, which triggers the research."),
    ("Investigative Question", "A specific sub-question that must be answered to address a broader research question."),
    ("Measurement Question", "The exact, specific question put to respondents or the exact data measured during data collection."),
]
examprep = [
    "Components of a research problem: unit of analysis, variables, relationship, environment.",
    "Sources for identifying problems: experience, discussions, literature, past data, stakeholder feedback.",
    "Good problem: researchable, significant, specific, feasible.",
    "Problem definition steps: understand decision &rarr; discuss &rarr; review secondary data &rarr; state clearly.",
    "Redefinition hierarchy: management question &rarr; research question &rarr; investigative question &rarr; measurement question.",
]
questions = [
    ("What are the components of a research problem?", "A research problem comprises the unit of analysis or population affected, the variables or factors involved, the relationship being studied between them, and the environment or context within which the problem exists."),
    ("Explain the process and criteria for identifying a good research problem.", "Problem identification moves from recognising a symptom, through investigating possible causes, to narrowing down to the actual researchable problem, drawing on sources such as personal experience, stakeholder discussion, literature and past data. A good problem must be researchable, significant, specific and feasible within available time and budget."),
    ("Describe the hierarchy used to redefine a research problem into measurement questions.", "The broad management question (what the manager needs to decide) is translated into research questions (what information is needed), which are broken into investigative questions (specific sub-questions), and finally into measurement questions (the exact questions put to respondents or data measured)."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("Once the problem is defined, the researcher sets clear objectives and, where appropriate, "
            "formulates testable hypotheses that the study will investigate.")
notes = """
<h3>5.1 Research Objectives</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Research Objectives</h4>
<ul>
<li><strong>General objective</strong> &mdash; the overall purpose or goal of the study.</li>
<li><strong>Specific objectives</strong> &mdash; the concrete, measurable sub-goals that together fulfil the general objective.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Components of a Research Objective</h4>
<p>A well-stated objective identifies the variable(s) to be studied, the population or unit of analysis, and the relationship or outcome to be examined.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Guidelines for Statement of Research Objectives</h4>
<ul>
<li>State objectives in clear, specific, and measurable terms.</li>
<li>Use action verbs (e.g. "to determine", "to compare", "to examine").</li>
<li>Ensure objectives are realistic given the available time and resources.</li>
<li>Keep each objective focused on a single, well-defined outcome.</li>
</ul>

<h3>5.2 Research Hypotheses</h3>
<p>A hypothesis is a tentative, testable statement about the expected relationship between two or more variables, proposed as a possible answer to the research problem before data is collected.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Characteristics of a Good Hypothesis</h4>
<ul>
<li>Clear and precisely stated.</li>
<li>Testable through empirical data.</li>
<li>Consistent with existing knowledge, yet capable of extending it.</li>
<li>States a relationship between two or more variables.</li>
<li>Limited in scope, not overly broad or vague.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Hypotheses</h4>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Null Hypothesis (H&#8320;)</strong></td><td>States there is no relationship or difference between the variables studied.</td></tr>
<tr><td><strong>Alternative Hypothesis (H&#8321;)</strong></td><td>States that a relationship or difference does exist.</td></tr>
<tr><td><strong>Directional Hypothesis</strong></td><td>Specifies the expected direction of the relationship (e.g. "higher advertising spend increases sales").</td></tr>
<tr><td><strong>Non-Directional Hypothesis</strong></td><td>States a relationship exists without specifying its direction.</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Significance of Hypotheses</h4>
<p>Hypotheses give the research direction and focus, suggest the type of data needed, and provide a framework against which the collected data can be formally tested.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Limitations of Hypotheses</h4>
<p>A poorly formulated hypothesis can bias data collection toward confirming a preconceived belief, and not every exploratory study requires (or can support) a formal hypothesis.</p>
"""
terms = [
    ("Research Objective", "A clear, specific statement of what a research study intends to achieve or discover."),
    ("Hypothesis", "A tentative, testable statement about the expected relationship between two or more variables."),
    ("Null Hypothesis (H0)", "A hypothesis stating there is no relationship or difference between the variables studied."),
    ("Alternative Hypothesis (H1)", "A hypothesis stating that a relationship or difference does exist between the variables studied."),
]
examprep = [
    "Objectives: general (overall purpose) vs specific (measurable sub-goals).",
    "Good objective: clear, specific, measurable, realistic, uses action verbs.",
    "Hypothesis = tentative, testable statement of an expected relationship between variables.",
    "Good hypothesis: clear, testable, consistent with knowledge, states a relationship, limited in scope.",
    "Types: null (H0, no relationship) vs alternative (H1, relationship exists); directional vs non-directional.",
]
questions = [
    ("Define research objectives and state the guidelines for writing them.", "Research objectives are clear, specific statements of what a study intends to achieve. They should be stated in clear, measurable terms using action verbs, kept realistic given available time and resources, and each should focus on a single well-defined outcome."),
    ("Define hypothesis and explain the characteristics of a good hypothesis.", "A hypothesis is a tentative, testable statement about the expected relationship between two or more variables, proposed before data is collected. A good hypothesis is clear, testable, consistent with existing knowledge, states a specific relationship between variables, and is limited enough in scope to be investigated."),
    ("Distinguish between null and alternative hypotheses.", "The null hypothesis (H0) states that no relationship or difference exists between the variables studied, while the alternative hypothesis (H1) states that a relationship or difference does exist. Research uses statistical tests on sample data to decide whether to reject the null hypothesis in favour of the alternative."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("This closing topic of Unit 1 looks at the relationship between theory and research &mdash; how "
            "theory guides research design and interpretation, and the building blocks that make up a theory.")
notes = """
<h3>6.1 Introduction</h3>
<p>Theory and research are closely interlinked: theory provides the conceptual framework that guides what to study and how to interpret findings, while research in turn tests, refines, or builds new theory.</p>

<h3>6.2 Role of Theory in Research</h3>
<ul>
<li>Provides a framework for defining the research problem and relevant variables.</li>
<li>Helps generate hypotheses that research can test.</li>
<li>Guides the choice of research design and the interpretation of results.</li>
<li>Helps explain <em>why</em> an observed relationship between variables exists, not just <em>that</em> it exists.</li>
</ul>

<h3>6.3 Importance of Theory in Research</h3>
<ul>
<li>Prevents research from being a disconnected collection of isolated facts.</li>
<li>Allows findings from different studies to be compared and accumulated into a coherent body of knowledge.</li>
<li>Improves the ability to generalise and predict beyond the specific sample studied.</li>
<li>Gives researchers a basis for proposing practical recommendations grounded in established principles.</li>
</ul>

<h3>6.4 Components of Theory</h3>
<table class="compare">
<tr><th>Component</th><th>Description</th></tr>
<tr><td><strong>Concepts</strong></td><td>Abstract ideas or categories used to classify observations (e.g. "motivation", "customer loyalty").</td></tr>
<tr><td><strong>Constructs</strong></td><td>Concepts specifically defined and used for a particular research purpose, often built from more basic concepts.</td></tr>
<tr><td><strong>Variables</strong></td><td>Measurable representations of constructs that can take different values (e.g. a loyalty score).</td></tr>
<tr><td><strong>Propositions</strong></td><td>Statements about the relationship between two or more concepts or constructs.</td></tr>
<tr><td><strong>Hypotheses</strong></td><td>Propositions stated in a testable form, ready to be examined with empirical data.</td></tr>
</table>
"""
terms = [
    ("Theory", "A systematic set of interrelated concepts, definitions and propositions that explains or predicts a phenomenon."),
    ("Concept", "An abstract idea or category used to classify observations."),
    ("Construct", "A concept specifically defined and used for a particular research purpose."),
    ("Proposition", "A statement about the relationship between two or more concepts or constructs."),
]
examprep = [
    "Theory guides what to study, how to design research, and how to interpret results.",
    "Importance of theory: avoids disconnected facts, enables comparison across studies, supports generalisation.",
    "Components of theory (building up): concepts &rarr; constructs &rarr; variables &rarr; propositions &rarr; hypotheses.",
]
questions = [
    ("Explain the role of theory in research.", "Theory provides the conceptual framework that guides the definition of the research problem and relevant variables, helps generate testable hypotheses, guides the choice of research design, and helps explain why an observed relationship exists rather than simply that it exists."),
    ("Why is theory important in research?", "Theory prevents research from producing a disconnected collection of isolated facts, allows findings across different studies to be compared and accumulated into a coherent body of knowledge, improves the ability to generalise beyond the specific sample studied, and grounds practical recommendations in established principles."),
    ("List and briefly explain the components of theory.", "Theory is built from concepts (abstract classifying ideas), constructs (concepts specifically defined for a research purpose), variables (measurable representations of constructs), propositions (statements of relationship between concepts), and hypotheses (propositions stated in a testable form)."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 6 done")

U.write_index("Book: <em>Business Research Methods</em> (BA4205) &middot; Unit 1 covers the foundations of research: its nature, business applications, types, problem identification, objectives/hypotheses, and the link between theory and research.")
print("Unit 1 index done")
