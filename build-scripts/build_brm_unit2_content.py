# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Business-Research-Methods\units"
BOOK_HTML = "Book: <em>Business Research Methods</em> (BA4205, Anna University MBA Sem II, Regulation 2021)"
BOOK_PLAIN = "Business Research Methods (BA4205), Dr. T. Vetrivel &amp; Dr. P. Priyadarsini, Thakur Publication"

TOPICS = [
    ("topic1-research-design-meaning-and-types.html", "Research Design: Meaning and Types"),
    ("topic2-exploratory-and-descriptive-research-design.html", "Exploratory and Descriptive Research Design"),
    ("topic3-experimental-causal-research-design.html", "Experimental (Causal) Research Design"),
    ("topic4-variables-in-research.html", "Variables in Research"),
    ("topic5-measurement-in-research.html", "Measurement in Research"),
    ("topic6-scaling-techniques.html", "Scaling Techniques"),
]

WINE_THEME = dict(accent="#7a1f3d", accent_dark="#4d1326", accent_light="#faebf0",
                   border="#f0d7df", shadow="rgba(122,31,61,.14)")

U = common.UnitBuilder(2, "Understanding Research Design and Measurement", TOPICS,
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
overview = ("A research design is the master blueprint for a study. This topic covers what makes a design "
            "good, the factors that shape it, and the broad categories of research design available.")
notes = """
<h3>1.1 Meaning and Definition of Research Design</h3>
<p>A research design is the overall plan or blueprint that specifies the methods and procedures for collecting and analysing the information needed to answer the research problem. It is the framework that links the research questions to the data that will be gathered.</p>

<h3>1.2 Features of a Good Research Design</h3>
<ul>
<li>Clearly specifies the objectives and the information needed.</li>
<li>Minimises bias and maximises the reliability of the data collected.</li>
<li>Provides the maximum relevant information at the lowest possible cost.</li>
<li>Is flexible enough to allow consideration of different aspects of the problem.</li>
<li>Specifies a sound, feasible plan for sampling, data collection and analysis.</li>
</ul>

<h3>1.3 Factors Affecting Research Design</h3>
<ul>
<li>The nature and degree of clarity of the research problem.</li>
<li>The objectives of the study (exploratory, descriptive or causal).</li>
<li>Availability of time, budget and skilled personnel.</li>
<li>Availability and accessibility of data sources.</li>
<li>The degree of accuracy required in the findings.</li>
</ul>

<h3>1.4 Significance of Research Design</h3>
<p>A sound research design ensures that the study collects the right data, in the right way, to answer the research question efficiently, reduces wasted effort and cost, and makes the findings more reliable and defensible.</p>

<h3>1.5 Research Design Process</h3>
<ol>
<li>Review the research problem and objectives.</li>
<li>Decide on the type of design (exploratory, descriptive or causal) appropriate to the objectives.</li>
<li>Determine the data sources (primary and/or secondary) and data collection methods.</li>
<li>Decide on the sampling design.</li>
<li>Plan the data analysis approach.</li>
<li>Prepare the research proposal/plan.</li>
</ol>

<h3>1.6 Types of Research Design</h3>
<table class="compare">
<tr><th>Type</th><th>Used When</th></tr>
<tr><td><strong>Exploratory Research Design</strong></td><td>The problem is vague or not well understood; the goal is to gain insight and clarify the issue.</td></tr>
<tr><td><strong>Descriptive Research Design</strong></td><td>The problem is clearly defined; the goal is to describe characteristics of a population or phenomenon.</td></tr>
<tr><td><strong>Experimental / Causal Research Design</strong></td><td>The goal is to establish a cause-and-effect relationship between variables.</td></tr>
</table>
"""
terms = [
    ("Research Design", "The overall plan or blueprint specifying the methods and procedures for collecting and analysing data to answer the research problem."),
    ("Exploratory Research Design", "A design used when the problem is not well understood, aimed at gaining insight."),
    ("Descriptive Research Design", "A design used to describe the characteristics of a population or phenomenon."),
    ("Causal Research Design", "A design used to establish cause-and-effect relationships between variables."),
]
examprep = [
    "Research design = blueprint linking the research question to the data plan.",
    "Good design: clear objectives, minimises bias, cost-efficient, flexible, sound sampling/analysis plan.",
    "Factors affecting design: problem clarity, objectives, time/budget, data availability, accuracy needed.",
    "Three broad design types: exploratory, descriptive, causal/experimental.",
]
questions = [
    ("Define research design and list the features of a good research design.", "A research design is the overall plan or blueprint that specifies the methods and procedures for collecting and analysing data needed to answer the research problem. A good design clearly specifies objectives, minimises bias, maximises reliability, provides maximum relevant information at the lowest cost, and remains flexible."),
    ("What factors influence the choice of a research design?", "The choice of research design is influenced by the nature and clarity of the research problem, the study's objectives, available time and budget, the accessibility of data sources, and the degree of accuracy required in the findings."),
    ("Describe the research design process.", "The process moves from reviewing the problem and objectives, to selecting the design type (exploratory, descriptive or causal), determining data sources and collection methods, deciding the sampling design, planning the analysis approach, and preparing the research proposal."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("This topic covers the two non-causal research designs in detail: exploratory research, used "
            "to clarify an ill-defined problem, and descriptive research, used to portray characteristics "
            "of a population once the problem is clear.")
notes = """
<h3>2.1 Exploratory Research Design</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Introduction</h4>
<p>Exploratory research is undertaken when the researcher has little prior understanding of the problem. It is flexible, unstructured, and aims to generate insight and hypotheses for further, more structured study rather than to provide final answers.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Methods of Exploratory Research</h4>
<ul>
<li>Literature survey of existing published material.</li>
<li>Expert/key-informant interviews with individuals knowledgeable about the problem.</li>
<li>Focus group discussions with a small set of relevant participants.</li>
<li>Case study analysis of similar, insight-generating situations.</li>
<li>Pilot surveys on a small scale.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Application</h4>
<p>Used at the start of a research project to clarify concepts, identify relevant variables, and sharpen a vague problem into a precise, researchable one.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Significance and Limitations</h4>
<p>Significant because it prevents wasted effort on a poorly defined problem and surfaces hypotheses worth testing. Limited because its findings are typically not representative or conclusive enough to be used directly for final decisions.</p>

<h3>2.2 Descriptive Research Design</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Introduction</h4>
<p>Descriptive research is undertaken when the problem is already well structured, to accurately describe the characteristics of a population, a market, or a phenomenon &mdash; answering questions of who, what, when, where and how, but not why.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Methods of Descriptive Research</h4>
<ul>
<li>Sample surveys using structured questionnaires.</li>
<li>Observation studies recording behaviour as it occurs.</li>
<li>Analysis of secondary/archival data.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Application</h4>
<p>Used for market characteristic studies, usage/attitude studies, and any situation requiring an accurate profile of a defined group.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Significance and Limitations</h4>
<p>Significant because it is systematic and produces data that generalises to a wider population when properly sampled. Limited because it only describes relationships observed &mdash; it cannot by itself prove that one variable causes another.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Descriptive Research Design</h4>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Cross-Sectional Studies</strong></td><td>Data collected from a sample of the population at one point in time.</td></tr>
<tr><td><strong>Longitudinal Studies</strong></td><td>Data collected from the same sample (a "panel") repeatedly over time.</td></tr>
</table>
"""
terms = [
    ("Exploratory Research", "Flexible, unstructured research undertaken to gain insight and clarify a poorly understood problem."),
    ("Descriptive Research", "Research undertaken to accurately describe the characteristics of a population or phenomenon once the problem is clearly defined."),
    ("Cross-Sectional Study", "A descriptive design that collects data from a sample at a single point in time."),
    ("Longitudinal Study", "A descriptive design that collects data from the same sample repeatedly over time."),
]
examprep = [
    "Exploratory research: ill-defined problem, flexible methods, generates insight/hypotheses, not conclusive.",
    "Exploratory methods: literature survey, expert interviews, focus groups, case studies, pilot surveys.",
    "Descriptive research: well-defined problem, answers who/what/when/where/how, not why.",
    "Descriptive methods: sample surveys, observation, secondary data analysis.",
    "Descriptive design types: cross-sectional (one point in time) vs longitudinal (repeated over time).",
]
questions = [
    ("When is exploratory research used, and what methods does it employ?", "Exploratory research is used when the researcher has little prior understanding of the problem and needs to gain insight before a structured study. It uses flexible methods such as literature surveys, expert interviews, focus group discussions, case studies, and small-scale pilot surveys."),
    ("Explain descriptive research design and its types.", "Descriptive research is used once the problem is well defined, to accurately portray the characteristics of a population through sample surveys, observation or secondary data. It has two main types: cross-sectional studies, which collect data at a single point in time, and longitudinal studies, which track the same sample repeatedly over time."),
    ("What are the limitations of exploratory and descriptive research?", "Exploratory research produces findings that are typically not representative or conclusive enough for final decisions, since its methods are flexible and small-scale. Descriptive research can accurately describe relationships observed in the data but cannot by itself establish that one variable causes another."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("Experimental (causal) research design is used to establish cause-and-effect relationships. "
            "This topic covers the logic of causality, the main experimental design types, and how the "
            "validity of experimental findings is assessed.")
notes = """
<h3>3.1 Introduction</h3>
<p>Experimental research deliberately manipulates one or more independent variables under controlled conditions to observe the effect on a dependent variable, allowing the researcher to draw causal conclusions that descriptive research cannot.</p>

<h3>3.2 Criteria for Causality in Experimental Research</h3>
<ul>
<li><strong>Concomitant variation</strong> &mdash; the cause and effect must vary together as predicted.</li>
<li><strong>Time order of occurrence</strong> &mdash; the cause must occur before (or simultaneously with) the effect.</li>
<li><strong>Elimination of other possible causes</strong> &mdash; other plausible explanations for the effect must be ruled out.</li>
</ul>

<h3>3.3 Causal Relationships and Basic Principles of Experimental Design</h3>
<p>A true experiment is built on three basic principles: <strong>manipulation</strong> of the independent variable by the researcher, <strong>control</strong> of extraneous factors that could also explain the effect, and <strong>randomisation</strong> of subjects to groups to spread out the influence of unknown factors evenly.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Treatment and Control Group</h4>
<p>The <strong>treatment (experimental) group</strong> receives the manipulated independent variable (e.g. a new advertising campaign); the <strong>control group</strong> does not, providing a baseline against which the effect of the treatment can be measured.</p>

<h3>3.4 Types/Methods of Experimental Research Design</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Pre-Experimental Designs</strong></td><td>Simplest designs, with little or no control over extraneous variables or randomisation (e.g. a one-group, before-after study); weak for establishing causality.</td></tr>
<tr><td><strong>True Experimental Designs</strong></td><td>Use random assignment to treatment and control groups with proper controls (e.g. pretest-posttest control group design), giving the strongest basis for causal conclusions.</td></tr>
<tr><td><strong>Quasi-Experimental Designs</strong></td><td>Used when full randomisation is not possible (e.g. in field settings); some control is exercised but groups are not fully randomised.</td></tr>
<tr><td><strong>Statistical Designs</strong></td><td>Use statistical techniques (e.g. factorial designs) to control for multiple independent variables and their interactions simultaneously.</td></tr>
</table>

<h3>3.5 Validity of Findings</h3>
<ul>
<li><strong>Internal Validity</strong> &mdash; the degree to which the observed effect can confidently be attributed to the manipulated variable and not to some other factor.</li>
<li><strong>External Validity</strong> &mdash; the degree to which the findings can be generalised beyond the specific experimental setting to other people, places and times.</li>
<li><strong>Trade-offs Between Internal and External Validity</strong> &mdash; tightly controlled lab experiments tend to have high internal but lower external validity, while realistic field experiments tend to have the reverse.</li>
</ul>

<h3>3.6 Application, Significance and Limitations</h3>
<p>Experimental design is applied in test marketing, product testing and advertising-effectiveness studies. It is significant because it is the strongest design for establishing causality. Its limitations include high cost, the difficulty of controlling all extraneous variables (especially in field settings), and possible artificiality when conducted in a laboratory.</p>
"""
terms = [
    ("Experimental Research", "Research that deliberately manipulates an independent variable under controlled conditions to observe its effect on a dependent variable."),
    ("Treatment Group", "The group in an experiment that receives the manipulated independent variable."),
    ("Control Group", "The group in an experiment that does not receive the treatment, serving as a baseline."),
    ("Internal Validity", "The degree to which an observed effect can be confidently attributed to the manipulated variable rather than another factor."),
    ("External Validity", "The degree to which experimental findings can be generalised beyond the specific setting studied."),
]
examprep = [
    "Causality criteria: concomitant variation, correct time order, elimination of other causes.",
    "Experimental design principles: manipulation, control, randomisation.",
    "Design types: pre-experimental (weak) &lt; quasi-experimental &lt; true experimental (strongest, randomised).",
    "Internal validity = confidence effect is due to the treatment; external validity = generalisability.",
    "Trade-off: lab experiments favour internal validity, field experiments favour external validity.",
]
questions = [
    ("What criteria must be met to establish a causal relationship?", "Three criteria must be met: concomitant variation (the cause and effect vary together as predicted), correct time order (the cause precedes the effect), and elimination of other plausible causes for the observed effect."),
    ("Distinguish between true experimental and quasi-experimental designs.", "True experimental designs randomly assign subjects to treatment and control groups under full researcher control, giving the strongest basis for causal conclusions. Quasi-experimental designs are used when full randomisation is not feasible, such as in real-world field settings, and provide weaker but still useful evidence of causality."),
    ("Explain internal and external validity and the trade-off between them.", "Internal validity is the degree to which an observed effect can be confidently attributed to the manipulated variable rather than some other factor, while external validity is the degree to which findings generalise beyond the specific experimental setting. Tightly controlled lab experiments tend to have high internal validity but lower external validity, while realistic field experiments tend to show the opposite trade-off."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("Every research design works with variables. This topic defines the different roles a variable "
            "can play in a study, which is essential to correctly designing and interpreting any causal "
            "research.")
notes = """
<h3>4.1 Independent and Dependent Variables</h3>
<p>The <strong>independent variable</strong> is the variable the researcher manipulates or that is assumed to cause a change. The <strong>dependent variable</strong> is the outcome variable that is measured to see the effect of that manipulation.</p>

<h3>4.2 Concomitant Variable</h3>
<p>A concomitant (or covariate) variable is a variable that is related to the dependent variable and is measured so its influence can be statistically controlled for, separating its effect from that of the independent variable.</p>

<h3>4.3 Moderating Variables</h3>
<p>A moderating variable affects the strength or direction of the relationship between the independent and dependent variables. For example, the effect of advertising spend on sales may be stronger in urban markets than rural ones &mdash; here, location moderates the relationship.</p>

<h3>4.4 Extraneous Variables</h3>
<p>Extraneous variables are factors other than the independent variable that could influence the dependent variable and distort the results if not controlled through good research design.</p>

<h3>4.5 Intervening Variables</h3>
<p>An intervening variable is a theoretical link that explains the mechanism through which the independent variable affects the dependent variable, without itself being directly observed (e.g. "employee motivation" intervening between "training" and "productivity").</p>

<h3>4.6 Summary Comparison</h3>
<table class="compare">
<tr><th>Variable Type</th><th>Role</th></tr>
<tr><td>Independent</td><td>Presumed cause; manipulated or selected by the researcher.</td></tr>
<tr><td>Dependent</td><td>Outcome measured to detect the effect.</td></tr>
<tr><td>Concomitant (Covariate)</td><td>Related variable statistically controlled for.</td></tr>
<tr><td>Moderating</td><td>Changes the strength/direction of the IV&ndash;DV relationship.</td></tr>
<tr><td>Extraneous</td><td>Uncontrolled factor that could distort results if ignored.</td></tr>
<tr><td>Intervening</td><td>Unobserved mechanism linking the IV to the DV.</td></tr>
</table>
"""
terms = [
    ("Independent Variable", "The variable manipulated or presumed to cause a change in a study."),
    ("Dependent Variable", "The outcome variable measured to detect the effect of the independent variable."),
    ("Moderating Variable", "A variable that affects the strength or direction of the relationship between the independent and dependent variables."),
    ("Extraneous Variable", "A factor other than the independent variable that could influence the dependent variable and distort results if uncontrolled."),
    ("Intervening Variable", "A theoretical, unobserved link explaining the mechanism through which the independent variable affects the dependent variable."),
]
examprep = [
    "Independent variable = presumed cause; Dependent variable = measured effect.",
    "Concomitant variable = related variable controlled for statistically.",
    "Moderating variable = changes strength/direction of the IV-DV relationship.",
    "Extraneous variable = uncontrolled factor that can distort results.",
    "Intervening variable = unobserved mechanism linking IV to DV.",
]
questions = [
    ("Differentiate between independent and dependent variables with an example.", "The independent variable is the variable manipulated or presumed to cause a change, while the dependent variable is the outcome measured to detect that effect. For example, in a study of advertising, advertising spend is the independent variable and resulting sales is the dependent variable."),
    ("Explain moderating and extraneous variables.", "A moderating variable affects the strength or direction of the relationship between the independent and dependent variables, such as market location changing how strongly advertising affects sales. An extraneous variable is an uncontrolled factor other than the independent variable that could also influence the dependent variable and distort the results if not accounted for in the research design."),
    ("What is an intervening variable? Give an example.", "An intervening variable is a theoretical, unobserved link that explains the mechanism by which the independent variable affects the dependent variable. For example, employee motivation may intervene between training (independent variable) and productivity (dependent variable), explaining why training leads to higher output."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("Before data can be collected, the concepts under study must be translated into measurable "
            "form. This topic covers the measurement process, the techniques used, and the sources of "
            "measurement error.")
notes = """
<h3>5.1 Introduction to Measurement</h3>
<p>Measurement is the process of assigning numbers or labels to objects, events or characteristics according to a defined set of rules, so that abstract concepts can be studied empirically.</p>

<h3>5.2 Process of Measurement</h3>
<ol>
<li>Identify and clearly define the concept to be measured.</li>
<li>Develop an operational definition that specifies exactly how the concept will be observed/measured.</li>
<li>Select or design the measurement instrument (scale, questionnaire item, test).</li>
<li>Apply the instrument and record the resulting data.</li>
<li>Assess the quality (validity and reliability) of the measurement.</li>
</ol>

<h3>5.3 Techniques of Measurement</h3>
<ul>
<li>Self-report techniques (questionnaires, rating scales completed by respondents).</li>
<li>Observational techniques (recording behaviour directly).</li>
<li>Physiological/objective measures (e.g. sales figures, attendance records).</li>
<li>Projective techniques (indirect methods used to uncover underlying attitudes).</li>
</ul>

<h3>5.4 Errors in Measurement</h3>
<table class="compare">
<tr><th>Error Type</th><th>Description</th></tr>
<tr><td><strong>Systematic (Constant) Error</strong></td><td>A consistent bias that affects measurement in the same direction every time (e.g. a leading question that always skews answers toward one option).</td></tr>
<tr><td><strong>Random Error</strong></td><td>Unpredictable variation from one measurement to another with no consistent direction, caused by chance factors.</td></tr>
</table>

<h3>5.5 Difficulties in Measurement</h3>
<ul>
<li>Many business and social concepts (e.g. "satisfaction", "loyalty") are abstract and not directly observable.</li>
<li>Respondents may answer inaccurately due to memory lapses, social desirability bias, or misunderstanding.</li>
<li>Different instruments can yield different results for the same underlying concept.</li>
</ul>

<h3>5.6 Criteria for Good Measurement</h3>
<ul>
<li><strong>Validity</strong> &mdash; the instrument actually measures the concept it is intended to measure.</li>
<li><strong>Reliability</strong> &mdash; the instrument produces consistent results on repeated application.</li>
<li><strong>Sensitivity</strong> &mdash; the instrument can detect small but meaningful differences.</li>
<li><strong>Practicality</strong> &mdash; the instrument is economical, convenient and interpretable to use.</li>
</ul>
"""
terms = [
    ("Measurement", "The process of assigning numbers or labels to objects, events or characteristics according to defined rules."),
    ("Operational Definition", "A precise specification of exactly how a concept will be observed or measured."),
    ("Systematic Error", "A consistent measurement bias that affects results in the same direction every time."),
    ("Validity (Measurement)", "The extent to which an instrument actually measures the concept it is intended to measure."),
    ("Reliability (Measurement)", "The extent to which an instrument produces consistent results on repeated application."),
]
examprep = [
    "Measurement process: define concept &rarr; operational definition &rarr; choose instrument &rarr; apply &rarr; assess quality.",
    "Techniques: self-report, observation, objective/physiological measures, projective techniques.",
    "Errors: systematic (consistent bias) vs random (unpredictable variation).",
    "Good measurement criteria: validity, reliability, sensitivity, practicality.",
]
questions = [
    ("Describe the process of measurement in research.", "Measurement begins with identifying and defining the concept to be measured, developing an operational definition of exactly how it will be observed, selecting or designing a measurement instrument, applying it to collect data, and finally assessing the validity and reliability of the resulting measurement."),
    ("Distinguish between systematic and random error in measurement.", "Systematic (constant) error is a consistent bias that skews measurement in the same direction every time, such as a leading survey question. Random error is unpredictable variation from one measurement to another caused by chance factors, with no consistent direction."),
    ("What criteria determine whether a measurement is good?", "Good measurement requires validity (the instrument measures what it is intended to measure), reliability (it produces consistent results on repeated use), sensitivity (it can detect small but meaningful differences), and practicality (it is economical and convenient to use)."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("Scaling converts qualitative judgements into quantitative data that can be analysed "
            "statistically. This topic covers the types of scales and the main scaling techniques used "
            "in business research.")
notes = """
<h3>6.1 Introduction to Scaling</h3>
<p>Scaling is the process of assigning numbers to an object or respondent's attitude, opinion or perception so that it can be compared, ranked or statistically analysed against others.</p>

<h3>6.2 Process of Scale Construction</h3>
<ol>
<li>Define the attitude or construct to be scaled.</li>
<li>Generate a pool of potential items/statements.</li>
<li>Select the scaling technique to apply.</li>
<li>Pre-test the scale on a sample.</li>
<li>Refine and finalise the scale based on pre-test results.</li>
</ol>

<h3>6.3 Types of Scales (Levels of Measurement)</h3>
<table class="compare">
<tr><th>Scale Type</th><th>Description</th></tr>
<tr><td><strong>Nominal Scale</strong></td><td>Labels/categorises data with no inherent order (e.g. gender, brand names). Only counts/frequencies are meaningful.</td></tr>
<tr><td><strong>Ordinal Scale</strong></td><td>Ranks data in order, but the gaps between ranks are not necessarily equal (e.g. satisfaction ranked "low/medium/high").</td></tr>
<tr><td><strong>Interval Scale</strong></td><td>Ranked data with equal intervals between points, but no true/absolute zero (e.g. temperature in &deg;C).</td></tr>
<tr><td><strong>Ratio Scale</strong></td><td>Interval scale with a true zero point, allowing meaningful ratios (e.g. sales revenue, age, income).</td></tr>
</table>

<h3>6.4 Scaling Techniques</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Ranking Scales (Comparative)</h4>
<p>Respondents directly compare items against each other and arrange them in order (e.g. rank 5 brands from most to least preferred).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Rating Scales (Non-Comparative)</h4>
<p>Respondents evaluate each item independently against a fixed scale (e.g. a 5-point Likert scale from "strongly disagree" to "strongly agree").</p>

<h3>6.5 Validity and Reliability of the Scaling Instrument</h3>
<p>As with any measurement tool, a scale must be checked for validity (does it truly capture the intended attitude?) and reliability (does it give consistent results when repeated?) before its results can be trusted.</p>

<h3>6.6 Importance of Scaling</h3>
<p>Scaling allows subjective concepts such as attitudes, satisfaction and preference to be expressed numerically, enabling statistical comparison, ranking and hypothesis testing that would otherwise be impossible with purely qualitative descriptions.</p>

<h3>6.7 Issues in Designing Attitude Scales</h3>
<ul>
<li>Choosing the appropriate number of scale points (too few loses precision; too many can confuse respondents).</li>
<li>Avoiding leading, ambiguous or double-barrelled statements.</li>
<li>Deciding whether to include a neutral midpoint.</li>
<li>Ensuring the scale is balanced, with an equal number of favourable and unfavourable positions.</li>
</ul>
"""
terms = [
    ("Nominal Scale", "A scale that labels or categorises data with no inherent order."),
    ("Ordinal Scale", "A scale that ranks data in order without equal gaps between ranks."),
    ("Interval Scale", "A ranked scale with equal intervals between points but no true zero."),
    ("Ratio Scale", "An interval scale with a true zero point, allowing meaningful ratios."),
    ("Likert Scale", "A common rating scale on which respondents indicate their degree of agreement with a statement."),
]
examprep = [
    "Scale construction: define construct &rarr; generate items &rarr; choose technique &rarr; pre-test &rarr; refine.",
    "Four levels of measurement: nominal (labels) &lt; ordinal (ranks) &lt; interval (equal gaps, no true zero) &lt; ratio (true zero).",
    "Ranking scales = comparative (items compared to each other); Rating scales = non-comparative (items rated independently).",
    "Scale must have validity (measures the right thing) and reliability (consistent results).",
    "Design issues: number of scale points, avoiding leading/ambiguous items, neutral midpoint, balance.",
]
questions = [
    ("Explain the four levels of measurement scales with examples.", "Nominal scales label data with no order, such as brand names. Ordinal scales rank data without equal gaps, such as low/medium/high satisfaction. Interval scales have equal intervals but no true zero, such as temperature in Celsius. Ratio scales have a true zero and allow meaningful ratios, such as sales revenue or age."),
    ("Differentiate between ranking and rating scales.", "Ranking (comparative) scales require respondents to directly compare items against each other and arrange them in order, such as ranking five brands by preference. Rating (non-comparative) scales ask respondents to evaluate each item independently against a fixed scale, such as a 5-point Likert agreement scale."),
    ("What issues must be considered when designing an attitude scale?", "Key issues include choosing an appropriate number of scale points, avoiding leading, ambiguous or double-barrelled statements, deciding whether to include a neutral midpoint, and ensuring the scale is balanced with an equal number of favourable and unfavourable positions."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 6 done")

U.write_index("Book: <em>Business Research Methods</em> (BA4205) &middot; Unit 2 covers research design fundamentals, exploratory/descriptive/experimental designs, variables in research, measurement, and scaling techniques.")
print("Unit 2 index done")
