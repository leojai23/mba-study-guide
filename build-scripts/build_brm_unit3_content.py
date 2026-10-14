# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Business-Research-Methods\units"
BOOK_HTML = "Book: <em>Business Research Methods</em> (BA4205, Anna University MBA Sem II, Regulation 2021)"
BOOK_PLAIN = "Business Research Methods (BA4205), Dr. T. Vetrivel &amp; Dr. P. Priyadarsini, Thakur Publication"

TOPICS = [
    ("topic1-data-collection-and-primary-data.html", "Data Collection and Primary Data"),
    ("topic2-questionnaire-design.html", "Questionnaire Design"),
    ("topic3-observation-and-survey-method.html", "Observation and Survey Method"),
    ("topic4-interview-method-and-experiments.html", "Interview Method and Experiments"),
    ("topic5-secondary-data.html", "Secondary Data"),
    ("topic6-sampling-and-sampling-techniques.html", "Sampling and Sampling Techniques"),
]

WINE_THEME = dict(accent="#7a1f3d", accent_dark="#4d1326", accent_light="#faebf0",
                   border="#f0d7df", shadow="rgba(122,31,61,.14)")

U = common.UnitBuilder(3, "Collection of Data", TOPICS,
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
overview = ("Data collection is the heart of the research process. This topic introduces the overall "
            "data collection task, then focuses on primary data &mdash; data gathered firsthand for the "
            "specific research problem at hand.")
notes = """
<h3>1.1 Data Collection</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Introduction</h4>
<p>Data collection is the process of gathering information relevant to the research objectives, following the plan set out in the research design. The quality of the entire study depends heavily on how carefully this step is executed.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Methods of Data Collection</h4>
<p>Data can be collected directly from original sources (<strong>primary data</strong>) or obtained from material already collected and published by others (<strong>secondary data</strong>). The choice of method depends on the nature of the problem, time and budget available, and the required accuracy.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Precautions in Data Collection</h4>
<ul>
<li>Clearly define what data is actually needed before collection begins.</li>
<li>Choose a collection method appropriate to the respondents and the problem.</li>
<li>Pre-test instruments to catch ambiguity or bias before full-scale collection.</li>
<li>Train field staff/interviewers to minimise inconsistency.</li>
<li>Build in quality checks to catch incomplete or inconsistent responses early.</li>
</ul>

<h3>1.2 Primary Data</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Introduction</h4>
<p>Primary data is data collected firsthand by the researcher specifically for the study at hand, and does not exist prior to the research being conducted.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Methods of Collecting Primary Data</h4>
<ul>
<li>Observation.</li>
<li>Interviews (personal, telephonic).</li>
<li>Questionnaires and schedules.</li>
<li>Surveys.</li>
<li>Experiments.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Significance</h4>
<p>Primary data is current, directly relevant to the specific problem, and under the researcher's control in terms of accuracy and scope &mdash; no other existing dataset will fit the exact research question as precisely.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Limitations</h4>
<p>Collecting primary data is expensive and time-consuming compared to using existing secondary data, and requires careful design to avoid bias or error.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Tools for Collecting Primary Data</h4>
<p>Structured questionnaires, interview schedules, observation checklists, and increasingly, online survey platforms and mobile data-collection apps.</p>
"""
terms = [
    ("Data Collection", "The process of gathering information relevant to the research objectives, following the research design."),
    ("Primary Data", "Data collected firsthand by the researcher specifically for the study at hand."),
    ("Secondary Data", "Data already collected and published by someone else for a purpose other than the current study."),
]
examprep = [
    "Data collection quality depends on clear data needs, appropriate method, pre-testing, trained staff, quality checks.",
    "Primary data = firsthand, collected specifically for this study; current and problem-specific but costly/time-consuming.",
    "Primary data methods: observation, interviews, questionnaires/schedules, surveys, experiments.",
    "Tools: structured questionnaires, interview schedules, observation checklists, online survey platforms.",
]
questions = [
    ("What precautions should be taken while collecting data?", "Researchers should clearly define the data actually needed, choose a collection method appropriate to the respondents and problem, pre-test instruments to catch ambiguity or bias, train field staff for consistency, and build in quality checks to catch incomplete or inconsistent responses early."),
    ("Define primary data and list its collection methods.", "Primary data is data collected firsthand by the researcher specifically for the study at hand. It is collected through methods such as observation, personal or telephonic interviews, questionnaires and schedules, surveys, and experiments."),
    ("What are the significance and limitations of primary data?", "Primary data is significant because it is current, directly relevant to the specific research problem, and collected under the researcher's control for accuracy. Its main limitation is that it is more expensive and time-consuming to collect than using existing secondary data, and requires careful design to avoid bias."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("The questionnaire is the most widely used tool for collecting primary data. This topic covers "
            "how questionnaires are constructed, the types of questions and questionnaires used, and the "
            "precautions needed to ensure they produce valid data.")
notes = """
<h3>2.1 Introduction to the Questionnaire</h3>
<p>A questionnaire is a structured set of questions designed to collect information from respondents in a standardised format, allowing responses from many people to be compared and analysed systematically.</p>

<h3>2.2 Types of Questions</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Open-Ended Questions</strong></td><td>Allow respondents to answer in their own words; rich detail but harder to code and analyse.</td></tr>
<tr><td><strong>Closed-Ended Questions</strong></td><td>Provide fixed response options (multiple-choice, yes/no, rating scales); easy to code and analyse, but may limit expression.</td></tr>
<tr><td><strong>Dichotomous Questions</strong></td><td>Offer exactly two response options (e.g. Yes/No).</td></tr>
<tr><td><strong>Multiple-Choice Questions</strong></td><td>Offer several predefined options, of which the respondent selects one or more.</td></tr>
</table>

<h3>2.3 Types of Questionnaires</h3>
<ul>
<li><strong>Structured Questionnaire</strong> &mdash; fixed wording and order of questions, mostly closed-ended.</li>
<li><strong>Unstructured Questionnaire</strong> &mdash; flexible, open-ended, used in exploratory research.</li>
<li><strong>Mail/Online Questionnaire</strong> &mdash; self-administered, distributed by post or electronically.</li>
<li><strong>Personally Administered Questionnaire</strong> &mdash; completed in the presence of a researcher or field investigator.</li>
</ul>

<h3>2.4 Construction of a Questionnaire</h3>
<ol>
<li>Decide the exact information needed based on the research objectives.</li>
<li>Decide the question types and response format.</li>
<li>Decide the wording of each question.</li>
<li>Decide the sequence of questions (general to specific, easy to sensitive).</li>
<li>Decide the physical layout and length.</li>
<li>Pre-test the questionnaire and revise.</li>
</ol>

<h3>2.5 Precautions in Questionnaire Design</h3>
<ul>
<li>Avoid leading, loaded or ambiguous questions.</li>
<li>Avoid double-barrelled questions (asking two things at once).</li>
<li>Keep language simple and avoid jargon.</li>
<li>Keep the questionnaire as short as the objectives permit.</li>
</ul>

<h3>2.6 Validity, Significance and Limitations</h3>
<p>A valid questionnaire actually measures what it claims to, which is why careful wording and pre-testing matter. Questionnaires are significant because they allow large-scale, standardised, low-cost data collection, but are limited by the risk of non-response, misunderstood questions, and respondents' willingness to answer honestly.</p>
"""
terms = [
    ("Questionnaire", "A structured set of questions designed to collect information from respondents in a standardised format."),
    ("Open-Ended Question", "A question that allows respondents to answer freely in their own words."),
    ("Closed-Ended Question", "A question that provides fixed response options for the respondent to choose from."),
    ("Double-Barrelled Question", "A poorly worded question that asks about two issues at once, making the answer ambiguous."),
]
examprep = [
    "Questions: open-ended (free response) vs closed-ended (fixed options, incl. dichotomous & multiple-choice).",
    "Questionnaire types: structured vs unstructured; mail/online vs personally administered.",
    "Construction steps: decide info needed &rarr; question types &rarr; wording &rarr; sequence &rarr; layout &rarr; pre-test.",
    "Precautions: avoid leading/loaded/double-barrelled questions, keep language simple and length short.",
]
questions = [
    ("Differentiate between open-ended and closed-ended questions.", "Open-ended questions allow respondents to answer freely in their own words, providing rich detail but making coding and analysis harder. Closed-ended questions provide fixed response options such as multiple-choice or yes/no, which are easier to code and analyse but may limit how respondents can express themselves."),
    ("Outline the steps in constructing a questionnaire.", "Questionnaire construction involves deciding the exact information needed based on research objectives, choosing question types and response formats, carefully wording each question, sequencing questions logically, deciding on physical layout and length, and finally pre-testing and revising the instrument."),
    ("What precautions should be taken when designing questionnaire items?", "Designers should avoid leading, loaded or ambiguous questions, avoid double-barrelled questions that ask two things at once, use simple language free of jargon, and keep the questionnaire as short as the research objectives allow."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("Beyond questionnaires, researchers also gather primary data by directly observing behaviour "
            "or by conducting structured surveys. This topic compares these two closely related methods."
            )
notes = """
<h3>3.1 Observation</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Introduction</h4>
<p>Observation involves systematically watching and recording behaviour, events or conditions as they naturally occur, without relying on respondents to report on themselves.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Observation</h4>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Participant Observation</strong></td><td>The observer becomes part of the group or situation being studied.</td></tr>
<tr><td><strong>Non-Participant Observation</strong></td><td>The observer remains separate, watching without taking part.</td></tr>
<tr><td><strong>Structured Observation</strong></td><td>Uses a predefined checklist/format specifying exactly what to record.</td></tr>
<tr><td><strong>Unstructured Observation</strong></td><td>Open-ended recording of whatever seems relevant, common in exploratory studies.</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Process</h4>
<p>Define what behaviour to observe &rarr; select the setting and observation method &rarr; train observers &rarr; record observations systematically &rarr; analyse the recorded data.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Significance and Limitations</h4>
<p>Observation captures actual behaviour rather than reported behaviour, avoiding recall and social-desirability bias. However, it cannot reveal motives, attitudes or intentions behind the behaviour, can be time-consuming, and the presence of an observer may itself alter behaviour.</p>

<h3>3.2 Survey</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Introduction</h4>
<p>A survey is a method of collecting data from a sample of respondents, typically through questionnaires or interviews, to describe the characteristics or opinions of a larger population.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Methods</h4>
<p>Personal (face-to-face) surveys, telephone surveys, mail surveys, and online/electronic surveys.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Significance and Limitations</h4>
<p>Surveys can efficiently cover large, geographically dispersed samples and produce data that can be statistically generalised. Limitations include the risk of non-response, respondent dishonesty or inaccurate recall, and the cost of reaching a sufficiently large, representative sample.</p>

<h3>3.3 Survey versus Observation</h3>
<table class="compare">
<tr><th>Aspect</th><th>Survey</th><th>Observation</th></tr>
<tr><td>Data source</td><td>Respondent self-report</td><td>Directly observed behaviour</td></tr>
<tr><td>Can capture attitudes/motives?</td><td>Yes</td><td>No (only behaviour)</td></tr>
<tr><td>Risk of reporting bias</td><td>Higher</td><td>Lower</td></tr>
<tr><td>Typical scale</td><td>Large samples</td><td>Often smaller, intensive</td></tr>
</table>
"""
terms = [
    ("Observation", "A data collection method involving systematically watching and recording behaviour as it naturally occurs."),
    ("Participant Observation", "Observation in which the observer becomes part of the group or situation being studied."),
    ("Survey", "A method of collecting data from a sample of respondents, typically via questionnaire or interview, to describe a larger population."),
]
examprep = [
    "Observation types: participant vs non-participant; structured vs unstructured.",
    "Observation captures actual behaviour, avoids recall bias, but cannot reveal motives/attitudes.",
    "Survey methods: personal, telephone, mail, online.",
    "Survey vs Observation: self-report vs directly observed; surveys can capture attitudes, observation cannot.",
]
questions = [
    ("Differentiate between participant and non-participant observation.", "In participant observation, the observer becomes part of the group or situation being studied, gaining an insider's perspective. In non-participant observation, the observer remains separate from the group, watching and recording behaviour without taking part in it."),
    ("What are the significance and limitations of the observation method?", "Observation captures actual behaviour rather than self-reported behaviour, avoiding recall and social-desirability bias. However, it cannot reveal the underlying motives, attitudes or intentions behind the behaviour, can be time-consuming, and the presence of an observer may itself alter the behaviour being studied."),
    ("Compare survey and observation as methods of data collection.", "A survey collects data through respondent self-report via questionnaires or interviews and can capture attitudes and opinions, but carries a higher risk of reporting bias. Observation directly records actual behaviour with lower reporting bias, but cannot capture underlying motives or attitudes and is often conducted on a smaller, more intensive scale."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("This topic covers two more primary data collection approaches: the interview, where data is "
            "gathered through direct conversation, and experiments, a brief recap of using controlled "
            "manipulation to generate data.")
notes = """
<h3>4.1 Interview</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Introduction</h4>
<p>An interview is a method of data collection involving direct, purposeful conversation between an interviewer and a respondent, allowing for more depth and flexibility than a self-administered questionnaire.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Characteristics</h4>
<ul>
<li>Involves direct interaction, allowing the interviewer to clarify questions and probe deeper.</li>
<li>Can capture non-verbal cues and context that a written questionnaire cannot.</li>
<li>Requires skilled interviewers to minimise bias from how questions are asked.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Interviews</h4>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Structured Interview</strong></td><td>Fixed set of questions asked in the same order to every respondent.</td></tr>
<tr><td><strong>Unstructured Interview</strong></td><td>Open, flexible conversation guided by broad topics rather than fixed questions.</td></tr>
<tr><td><strong>Semi-Structured Interview</strong></td><td>Combines a fixed core of questions with the flexibility to probe further.</td></tr>
<tr><td><strong>Depth Interview</strong></td><td>In-depth, one-on-one interview aimed at uncovering underlying motivations and attitudes.</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Significance and Limitations</h4>
<p>Interviews allow rich, detailed and flexible data collection with high response quality, but are costly, time-consuming, difficult to scale to large samples, and susceptible to interviewer bias.</p>

<h3>4.2 Experiments</h3>
<p>As covered under experimental research design, experiments generate primary data by deliberately manipulating an independent variable under controlled conditions and measuring the resulting change in a dependent variable. As a data collection method, experiments provide the strongest basis for establishing cause-and-effect relationships, though they are often costly and may not reflect real-world conditions as faithfully as field-based methods.</p>
"""
terms = [
    ("Interview", "A data collection method involving direct, purposeful conversation between an interviewer and a respondent."),
    ("Structured Interview", "An interview using a fixed set of questions asked in the same order to every respondent."),
    ("Depth Interview", "An in-depth, one-on-one interview aimed at uncovering underlying motivations and attitudes."),
]
examprep = [
    "Interview = direct conversation; allows clarification, probing, capturing non-verbal cues.",
    "Interview types: structured, unstructured, semi-structured, depth interview.",
    "Interviews: rich/flexible data but costly, hard to scale, risk of interviewer bias.",
    "Experiments: manipulate IV under controlled conditions, strongest for establishing causality.",
]
questions = [
    ("What are the characteristics of the interview method of data collection?", "Interviews involve direct interaction, allowing the interviewer to clarify questions and probe deeper, and can capture non-verbal cues and context that a written questionnaire cannot. They require skilled interviewers to minimise bias introduced by how questions are asked."),
    ("Differentiate between structured and unstructured interviews.", "A structured interview uses a fixed set of questions asked in the same order to every respondent, producing standardised, comparable data. An unstructured interview is an open, flexible conversation guided by broad topics rather than fixed questions, allowing deeper exploration at the cost of standardisation."),
    ("What are the significance and limitations of interviews as a data collection method?", "Interviews allow rich, detailed and flexible data collection with generally high response quality, since the interviewer can clarify questions and probe further. Their limitations include high cost, difficulty scaling to large samples, and the risk of interviewer bias influencing responses."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("Not all research data needs to be collected firsthand. This topic covers secondary data "
            "&mdash; data already gathered by someone else &mdash; and when it is appropriate to rely on "
            "it instead of, or alongside, primary data.")
notes = """
<h3>5.1 Introduction to Secondary Data</h3>
<p>Secondary data is data that has already been collected, processed and published by some other individual or organisation for a purpose other than the current research problem, but which the researcher can reuse.</p>

<h3>5.2 Primary versus Secondary Data</h3>
<table class="compare">
<tr><th>Aspect</th><th>Primary Data</th><th>Secondary Data</th></tr>
<tr><td>Source</td><td>Collected firsthand by the researcher</td><td>Already collected by someone else</td></tr>
<tr><td>Cost and time</td><td>Higher</td><td>Lower, usually faster to obtain</td></tr>
<tr><td>Relevance to the specific problem</td><td>Exact fit</td><td>May not perfectly match the current problem</td></tr>
<tr><td>Control over quality</td><td>Full control</td><td>Depends entirely on the original source</td></tr>
</table>

<h3>5.3 Methods/Sources of Secondary Data</h3>
<ul>
<li>Government publications and official statistics (census, trade, economic data).</li>
<li>Industry/trade association reports.</li>
<li>Company records, annual reports and internal databases.</li>
<li>Academic journals, books and prior research studies.</li>
<li>Commercial market research reports and databases.</li>
<li>Online/digital sources, including news archives and statistical portals.</li>
</ul>

<h3>5.4 Significance of Secondary Data</h3>
<ul>
<li>Saves considerable time and cost compared to fresh primary data collection.</li>
<li>Useful for exploratory research, establishing background and context, and defining the research problem.</li>
<li>Can provide historical/time-series data otherwise impossible to gather within a study's timeframe.</li>
</ul>

<h3>5.5 Limitations of Secondary Data</h3>
<ul>
<li>May be outdated by the time it is used.</li>
<li>May not match the exact definitions, units or population of the current study.</li>
<li>Quality and accuracy depend on the original source, which the researcher cannot verify directly.</li>
<li>May have been collected for a different purpose, limiting its direct applicability.</li>
</ul>
"""
terms = [
    ("Secondary Data", "Data already collected, processed and published by someone else for a purpose other than the current research problem."),
]
examprep = [
    "Secondary data = already collected by someone else, reused for the current study.",
    "Sources: government publications, trade reports, company records, journals, commercial databases, online sources.",
    "Significance: saves time/cost, good for exploratory work and historical/time-series data.",
    "Limitations: may be outdated, mismatched definitions/units, unverifiable quality, different original purpose.",
]
questions = [
    ("Define secondary data and distinguish it from primary data.", "Secondary data is data that has already been collected, processed and published by someone else for a purpose other than the current study, but which the researcher reuses. Unlike primary data, which is collected firsthand and fits the specific problem exactly, secondary data is cheaper and faster to obtain but may not perfectly match the current research problem, and its quality depends entirely on the original source."),
    ("List the major sources of secondary data.", "Major sources include government publications and official statistics, industry/trade association reports, company records and annual reports, academic journals and prior research, commercial market research databases, and online sources such as statistical portals and news archives."),
    ("What are the limitations of using secondary data?", "Secondary data may be outdated by the time it is used, may not match the exact definitions, units or population of the current study, its quality cannot be directly verified by the researcher, and it may have been collected for a different purpose, limiting how directly it applies to the current problem."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("Since it is rarely practical to study an entire population, researchers draw a sample. This "
            "topic covers the basics of sampling and the probability and non-probability techniques used "
            "to select a sample.")
notes = """
<h3>6.1 Sampling: Introduction</h3>
<p>Sampling is the process of selecting a subset (sample) of individuals or units from a larger population, so that conclusions drawn from the sample can be used to make inferences about the whole population.</p>

<h3>6.2 Basic Concepts in Sampling</h3>
<ul>
<li><strong>Population</strong> &mdash; the entire group of individuals or units of interest to the study.</li>
<li><strong>Sample</strong> &mdash; a subset of the population actually studied.</li>
<li><strong>Sampling Frame</strong> &mdash; the actual list or source from which the sample is drawn.</li>
<li><strong>Sampling Unit</strong> &mdash; the individual element selected from the sampling frame.</li>
<li><strong>Sampling Error</strong> &mdash; the difference between a sample result and the true population value, arising because only a subset was studied.</li>
</ul>

<h3>6.3 Characteristics of a Good Sample</h3>
<ul>
<li>Representative of the population from which it is drawn.</li>
<li>Adequate in size to produce statistically reliable results.</li>
<li>Selected using a method that avoids systematic bias.</li>
<li>Practical and economical to draw and study within the available budget and time.</li>
</ul>

<h3>6.4 Sample Size and Sampling Plan</h3>
<p>Sample size depends on the desired level of precision, the population's variability, the confidence level required, and available resources. A sampling plan specifies the target population, the sampling frame, the sampling unit, the sampling technique, and the sample size before data collection begins.</p>

<h3>6.5 Advantages and Disadvantages of Sampling</h3>
<table class="compare">
<tr><th>Advantages</th><th>Disadvantages</th></tr>
<tr><td>Saves time and cost compared to a full census.</td><td>Introduces sampling error since not every unit is studied.</td></tr>
<tr><td>Makes large-scale studies practically feasible.</td><td>A poorly drawn sample can be unrepresentative and misleading.</td></tr>
<tr><td>Allows faster data collection and quicker results.</td><td>Requires sound statistical knowledge to design and interpret correctly.</td></tr>
</table>

<h3>6.6 Sampling Techniques/Methods</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Probability Sampling</h4>
<p>Every unit in the population has a known, non-zero chance of being selected, allowing formal statistical inference. Common methods include simple random sampling, systematic sampling, stratified sampling, and cluster sampling.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Non-Probability Sampling</h4>
<p>Units are selected based on researcher judgement or convenience rather than known probabilities. Common methods include convenience sampling, judgement/purposive sampling, quota sampling, and snowball sampling.</p>

<h3>6.7 Probability versus Non-Probability Sampling</h3>
<table class="compare">
<tr><th>Aspect</th><th>Probability Sampling</th><th>Non-Probability Sampling</th></tr>
<tr><td>Selection basis</td><td>Known chance of selection for every unit</td><td>Researcher judgement or convenience</td></tr>
<tr><td>Generalisability</td><td>Results can be statistically generalised</td><td>Limited generalisability</td></tr>
<tr><td>Cost and time</td><td>Generally higher</td><td>Generally lower, faster</td></tr>
<tr><td>Typical use</td><td>Conclusive, large-scale studies</td><td>Exploratory studies, limited resources</td></tr>
</table>
"""
terms = [
    ("Sampling", "The process of selecting a subset of a population so that conclusions from the subset can be generalised to the whole population."),
    ("Sampling Frame", "The actual list or source from which a sample is drawn."),
    ("Sampling Error", "The difference between a sample result and the true population value, arising because only a subset was studied."),
    ("Probability Sampling", "A sampling approach in which every population unit has a known, non-zero chance of selection."),
    ("Non-Probability Sampling", "A sampling approach in which units are selected based on judgement or convenience rather than known probabilities."),
]
examprep = [
    "Key terms: population, sample, sampling frame, sampling unit, sampling error.",
    "Good sample: representative, adequate size, unbiased selection, practical/economical.",
    "Sample size depends on: desired precision, population variability, confidence level, resources.",
    "Sampling advantages: saves time/cost, feasible at scale; disadvantage: introduces sampling error.",
    "Probability sampling (known selection chance, generalisable) vs non-probability (judgement/convenience, limited generalisability).",
]
questions = [
    ("Define sampling and explain the characteristics of a good sample.", "Sampling is the process of selecting a subset of a population so that conclusions drawn from the subset can be generalised to the whole population. A good sample is representative of the population, adequate in size for reliable results, selected through a method that avoids systematic bias, and practical and economical to draw within available resources."),
    ("Distinguish between probability and non-probability sampling.", "In probability sampling, every unit in the population has a known, non-zero chance of being selected, allowing results to be statistically generalised; examples include simple random, systematic, stratified and cluster sampling. In non-probability sampling, units are selected based on researcher judgement or convenience, which is faster and cheaper but limits how far results can be generalised; examples include convenience, judgement, quota and snowball sampling."),
    ("What factors determine sample size?", "Sample size is determined by the desired level of precision in the results, the variability of the population being studied, the confidence level required, and the time and budget available for the study."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 6 done")

U.write_index("Book: <em>Business Research Methods</em> (BA4205) &middot; Unit 3 covers data collection methods &mdash; primary data, questionnaires, observation, surveys, interviews, secondary data, and sampling.")
print("Unit 3 index done")
