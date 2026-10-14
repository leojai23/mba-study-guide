# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Business-Research-Methods\units"
BOOK_HTML = "Book: <em>Business Research Methods</em> (BA4205, Anna University MBA Sem II, Regulation 2021)"
BOOK_PLAIN = "Business Research Methods (BA4205), Dr. T. Vetrivel &amp; Dr. P. Priyadarsini, Thakur Publication"

TOPICS = [
    ("topic1-data-preparation-and-processing.html", "Data Preparation and Processing"),
    ("topic2-data-analysis-meaning-and-types.html", "Data Analysis: Meaning and Types"),
    ("topic3-bivariate-analysis-correlation-and-regression.html", "Bi-variate Analysis: Correlation and Regression"),
    ("topic4-analysis-of-variance-anova.html", "Analysis of Variance (ANOVA)"),
    ("topic5-multivariate-analysis.html", "Multivariate Analysis"),
    ("topic6-hypothesis-testing.html", "Hypothesis Testing"),
]

WINE_THEME = dict(accent="#7a1f3d", accent_dark="#4d1326", accent_light="#faebf0",
                   border="#f0d7df", shadow="rgba(122,31,61,.14)")

U = common.UnitBuilder(4, "Data Preparation and Analysis", TOPICS,
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
overview = ("Raw data collected from the field is rarely ready for analysis. This topic covers the full "
            "sequence of operations &mdash; validation, editing, coding, classification, data entry and "
            "tabulation &mdash; that turn raw responses into analysis-ready data.")
notes = """
<h3>1.1 Introduction and Significance</h3>
<p>Data preparation and processing is the set of steps that convert raw, collected data into a clean, organised and structured form suitable for analysis. Skipping or rushing this stage risks introducing errors that undermine every conclusion drawn later.</p>

<h3>1.2 Operations in Data Preparation</h3>
<p>The typical sequence is: <strong>validation &rarr; editing &rarr; coding &rarr; classification &rarr; data entry &rarr; tabulation.</strong></p>

<h3>1.3 Validation</h3>
<p>Validation checks that each completed questionnaire/response was gathered honestly, from a qualified respondent, under proper conditions, and is complete enough to be usable.</p>

<h3>1.4 Editing</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Essentials of Editing</h4>
<p>Editing reviews completed data for accuracy, consistency, completeness and uniformity before coding begins.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Stages of Editing</h4>
<ul>
<li><strong>Field editing</strong> &mdash; a quick check done by the interviewer/investigator shortly after collection, while memory is fresh.</li>
<li><strong>Central/office editing</strong> &mdash; a thorough, uniform review conducted later by trained editors at a central location.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Handling Unsatisfactory Responses</h4>
<p>Options include contacting the respondent again, returning the questionnaire to the field for completion, inferring the missing answer from other responses, discarding the response, or treating it as missing data in analysis.</p>

<h3>1.5 Coding</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Principles of Coding</h4>
<p>Coding assigns a numerical or symbolic value to each possible response so it can be processed statistically; codes should be exhaustive (cover every possible answer), mutually exclusive, and consistently applied.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Procedure</h4>
<p>Develop a coding scheme/codebook from the questionnaire and a sample of responses, apply it consistently across all responses, and spot-check for coder errors.</p>

<h3>1.6 Classification</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Principles</h4>
<p>Classification groups data into categories that are relevant to the research objectives, exhaustive and mutually exclusive.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types</h4>
<ul>
<li><strong>Qualitative classification</strong> &mdash; by attribute or quality (e.g. gender, occupation).</li>
<li><strong>Quantitative classification</strong> &mdash; by numerical magnitude (e.g. income bands, age groups).</li>
<li><strong>Geographical classification</strong> &mdash; by location.</li>
<li><strong>Chronological classification</strong> &mdash; by time period.</li>
</ul>

<h3>1.7 Data Entry</h3>
<p>Coded data is entered into a spreadsheet or statistical software package (e.g. SPSS, Excel) for processing, with validation checks to catch entry errors.</p>

<h3>1.8 Tabulation</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Characteristics of a Good Table</h4>
<p>Clear title, properly labelled rows/columns, source noted, and footnotes for any necessary clarification.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Tabulation</h4>
<ul>
<li><strong>Simple tabulation</strong> &mdash; one variable at a time.</li>
<li><strong>Cross tabulation</strong> &mdash; two or more variables shown together.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Rules of Tabulation</h4>
<p>Keep tables simple and focused, use consistent units, round figures appropriately, and ensure totals are correctly shown.</p>
"""
terms = [
    ("Editing", "The review of completed data for accuracy, consistency, completeness and uniformity before coding."),
    ("Coding", "The process of assigning a numerical or symbolic value to each possible response so it can be processed statistically."),
    ("Classification", "The grouping of data into categories that are relevant, exhaustive and mutually exclusive."),
    ("Tabulation", "The systematic arrangement of classified data into rows and columns for easy reference and analysis."),
]
examprep = [
    "Data preparation sequence: validation &rarr; editing &rarr; coding &rarr; classification &rarr; data entry &rarr; tabulation.",
    "Editing stages: field editing (by interviewer, immediate) vs central editing (by trained editors, thorough).",
    "Coding rules: codes must be exhaustive and mutually exclusive.",
    "Classification types: qualitative, quantitative, geographical, chronological.",
    "Tabulation types: simple (one variable) vs cross tabulation (two or more variables).",
]
questions = [
    ("Describe the sequence of operations in data preparation.", "Data preparation typically follows a sequence of validation (checking the data was genuinely and properly collected), editing (reviewing for accuracy and completeness), coding (assigning numerical values to responses), classification (grouping into relevant categories), data entry (into software), and tabulation (arranging into summary tables)."),
    ("Differentiate between field editing and central editing.", "Field editing is a quick check performed by the interviewer or investigator shortly after data collection, while memory of the interaction is still fresh. Central (office) editing is a more thorough, uniform review carried out later by trained editors at a central location, applying consistent standards across all collected data."),
    ("What principles must be followed in coding and classification?", "Coding requires that codes assigned to responses be exhaustive, covering every possible answer, and mutually exclusive, with no overlap, and applied consistently across all responses. Classification follows similar principles, grouping data into categories that are relevant to the research objectives, exhaustive, and mutually exclusive."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("With clean, tabulated data in hand, the researcher moves to analysis. This topic surveys what "
            "data analysis involves, its objectives, its two broad types, and the role of statistical "
            "software in carrying it out.")
notes = """
<h3>2.1 Introduction to Data Analysis</h3>
<p>Data analysis is the process of inspecting, cleaning, transforming and modelling data to extract useful information, draw conclusions, and support decision-making regarding the research objectives.</p>

<h3>2.2 Objectives of Data Analysis</h3>
<ul>
<li>To summarise and describe the collected data meaningfully.</li>
<li>To identify patterns, relationships or differences among variables.</li>
<li>To test the hypotheses formulated at the start of the study.</li>
<li>To provide a sound basis for conclusions and managerial recommendations.</li>
</ul>

<h3>2.3 Types of Data Analysis</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Qualitative Analysis</strong></td><td>Interprets non-numerical data (text, images, observations) to identify themes and patterns.</td></tr>
<tr><td><strong>Quantitative Analysis</strong></td><td>Applies statistical and mathematical techniques to numerical data.</td></tr>
<tr><td><strong>Univariate Analysis</strong></td><td>Examines one variable at a time (e.g. mean, frequency distribution).</td></tr>
<tr><td><strong>Bivariate Analysis</strong></td><td>Examines the relationship between two variables (e.g. correlation, cross-tabulation).</td></tr>
<tr><td><strong>Multivariate Analysis</strong></td><td>Examines relationships among three or more variables simultaneously.</td></tr>
</table>

<h3>2.4 Phases of Data Analysis</h3>
<ol>
<li>Organising and cleaning the prepared data.</li>
<li>Choosing the appropriate statistical technique based on the data type and research objective.</li>
<li>Running the analysis, often using statistical software.</li>
<li>Interpreting the output in the context of the research problem.</li>
<li>Drawing conclusions and formulating recommendations.</li>
</ol>

<h3>2.5 Application of Statistical Software</h3>
<p>Modern business research relies heavily on statistical software to perform the calculations involved in analysis quickly and accurately:</p>
<table class="compare">
<tr><th>Software</th><th>Description</th></tr>
<tr><td><strong>SPSS</strong> (Statistical Package for the Social Sciences)</td><td>Widely used, menu-driven software popular for survey and social-science style business research.</td></tr>
<tr><td><strong>SAS</strong> (Statistical Analysis System)</td><td>A powerful system used heavily in large-scale corporate and analytics environments.</td></tr>
<tr><td><strong>STATA</strong></td><td>Popular in economics and econometrics-heavy research, combining a command language with menu-driven options.</td></tr>
</table>
"""
terms = [
    ("Data Analysis", "The process of inspecting, cleaning, transforming and modelling data to extract useful information and support conclusions."),
    ("Univariate Analysis", "Analysis that examines a single variable at a time."),
    ("Bivariate Analysis", "Analysis that examines the relationship between two variables."),
    ("Multivariate Analysis", "Analysis that examines relationships among three or more variables simultaneously."),
]
examprep = [
    "Data analysis objectives: summarise data, identify patterns/relationships, test hypotheses, support conclusions.",
    "Types by data: qualitative (non-numerical) vs quantitative (numerical/statistical).",
    "Types by variable count: univariate (1) &rarr; bivariate (2) &rarr; multivariate (3+).",
    "Analysis phases: organise/clean &rarr; choose technique &rarr; run analysis &rarr; interpret &rarr; conclude.",
    "Common software: SPSS (survey-focused), SAS (large-scale corporate analytics), STATA (econometrics).",
]
questions = [
    ("What are the objectives of data analysis?", "Data analysis aims to summarise and describe the collected data meaningfully, identify patterns and relationships or differences among variables, test the hypotheses formulated at the outset of the study, and provide a sound basis for conclusions and managerial recommendations."),
    ("Distinguish between univariate, bivariate and multivariate analysis.", "Univariate analysis examines a single variable at a time, such as its mean or frequency distribution. Bivariate analysis examines the relationship between exactly two variables, such as through correlation or cross-tabulation. Multivariate analysis examines the relationships among three or more variables simultaneously, such as through multiple regression or factor analysis."),
    ("Name and briefly describe three statistical software packages used in business research.", "SPSS (Statistical Package for the Social Sciences) is a widely used, menu-driven package popular for survey-based research. SAS (Statistical Analysis System) is a powerful system used in large-scale corporate and analytics environments. STATA is popular in economics and econometrics-heavy research, combining a command language with menu-driven options."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("This topic covers the two most common bi-variate statistical techniques: correlation, which "
            "measures the strength and direction of a relationship, and regression, which models that "
            "relationship so one variable can be predicted from another.")
notes = """
<h3>3.1 Cross Tabulation and Use of Percentages</h3>
<p>Cross tabulation displays the joint distribution of two variables in a grid, making it easy to see how categories of one variable relate to categories of another. Converting cell counts to percentages (row-wise, column-wise, or of the grand total) makes patterns easier to compare across groups of different sizes.</p>

<h3>3.2 Correlation Analysis</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Meaning</h4>
<p>Correlation measures the strength and direction of the linear relationship between two quantitative variables, expressed as a coefficient between &minus;1 and +1.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Correlation</h4>
<ul>
<li><strong>Positive correlation</strong> &mdash; both variables increase or decrease together.</li>
<li><strong>Negative correlation</strong> &mdash; one variable increases as the other decreases.</li>
<li><strong>Zero/no correlation</strong> &mdash; no consistent linear relationship between the variables.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Scatter Diagram</h4>
<p>A scatter diagram plots paired observations of the two variables on a graph, giving a visual first impression of whether a relationship exists and its approximate direction and strength.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Karl Pearson's Coefficient of Correlation</h4>
<p>The most widely used correlation measure for quantitative data, calculated as:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>r = &Sigma;(x &minus; x&#772;)(y &minus; y&#772;) &divide; &radic;[&Sigma;(x &minus; x&#772;)<sup>2</sup> &middot; &Sigma;(y &minus; y&#772;)<sup>2</sup>]</strong></p>
<p>r ranges from &minus;1 (perfect negative) to +1 (perfect positive), with 0 indicating no linear relationship.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Spearman's Rank Correlation</h4>
<p>Used for ranked (ordinal) data or when a non-parametric measure is preferred:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>&rho; = 1 &minus; [6&Sigma;d<sup>2</sup> &divide; n(n<sup>2</sup> &minus; 1)]</strong></p>
<p>where d is the difference between the ranks of each pair of observations and n is the number of pairs.</p>

<h3>3.3 Regression Analysis</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Meaning of Regression</h4>
<p>Regression analysis models the relationship between a dependent variable and one or more independent variables, allowing the dependent variable's value to be estimated/predicted.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Regression Coefficient</h4>
<p>For the simple linear regression equation <strong>Y = a + bX</strong>, b is the regression coefficient, representing the change in Y for a one-unit change in X.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Two Lines of Regression</h4>
<p>There are two regression lines &mdash; Y on X (predicting Y from X) and X on Y (predicting X from Y) &mdash; which coincide only when correlation is perfect (r = &plusmn;1).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Relationship between Correlation and Regression</h4>
<p>Correlation measures the degree of association between two variables, while regression goes further to express that relationship as an equation usable for prediction. The correlation coefficient is in fact the geometric mean of the two regression coefficients (byx and bxy).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Application and Difference</h4>
<p>Correlation is used simply to establish whether and how strongly two variables move together; regression is used when the goal is to predict or explain one variable's value using another.</p>
"""
terms = [
    ("Correlation", "A statistical measure of the strength and direction of the linear relationship between two quantitative variables."),
    ("Karl Pearson's Coefficient (r)", "A correlation coefficient ranging from -1 to +1 measuring the linear relationship between two quantitative variables."),
    ("Spearman's Rank Correlation", "A non-parametric correlation measure used for ranked (ordinal) data."),
    ("Regression Analysis", "A technique that models the relationship between a dependent and one or more independent variables for prediction."),
    ("Regression Coefficient", "In Y = a + bX, the value b representing the change in Y for a one-unit change in X."),
]
examprep = [
    "Correlation types: positive, negative, zero/no correlation; r ranges from -1 to +1.",
    "Pearson's r = Sigma(x-xbar)(y-ybar) / sqrt[Sigma(x-xbar)^2 . Sigma(y-ybar)^2].",
    "Spearman's rank correlation: rho = 1 - [6*Sigma(d^2) / n(n^2-1)], for ranked data.",
    "Regression equation: Y = a + bX; b = regression coefficient (change in Y per unit change in X).",
    "Correlation measures association strength; regression models the relationship for prediction. r = geometric mean of byx and bxy.",
]
questions = [
    ("Define correlation and explain its types.", "Correlation measures the strength and direction of the linear relationship between two quantitative variables. It can be positive (both variables move together), negative (one increases as the other decreases), or zero/no correlation (no consistent linear relationship)."),
    ("State Karl Pearson's formula for the coefficient of correlation and explain its range.", "Karl Pearson's coefficient of correlation is r = Sigma(x-xbar)(y-ybar) / sqrt[Sigma(x-xbar)^2 . Sigma(y-ybar)^2]. It ranges from -1 (perfect negative correlation) to +1 (perfect positive correlation), with 0 indicating no linear relationship."),
    ("Differentiate between correlation and regression analysis.", "Correlation measures the degree and direction of association between two variables without implying prediction. Regression goes further, expressing the relationship as an equation (Y = a + bX) that allows the value of the dependent variable to be predicted from the independent variable; the correlation coefficient is the geometric mean of the two regression coefficients."),
    ("What are the two lines of regression? When do they coincide?", "The two lines of regression are the regression of Y on X (used to predict Y from X) and the regression of X on Y (used to predict X from Y). These two lines coincide only when the correlation between the variables is perfect, i.e. r = +1 or r = -1."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("Analysis of Variance (ANOVA) extends hypothesis testing to compare the means of three or more "
            "groups simultaneously. This topic covers its assumptions, applications, and the one-way and "
            "two-way classifications."
            )
notes = """
<h3>4.1 Characteristics of Analysis of Variance (ANOVA)</h3>
<p>ANOVA tests whether the means of three or more groups are statistically different from one another by comparing the variation <em>between</em> group means to the variation <em>within</em> groups, rather than comparing means pair by pair.</p>

<h3>4.2 Assumptions of ANOVA</h3>
<ul>
<li>Observations are independent of one another.</li>
<li>Each group/population is approximately normally distributed.</li>
<li>The groups have approximately equal variances (homogeneity of variance).</li>
<li>The dependent variable is measured on an interval or ratio scale.</li>
</ul>

<h3>4.3 Applications of ANOVA</h3>
<ul>
<li>Comparing average sales performance across more than two sales regions.</li>
<li>Comparing customer satisfaction scores across more than two store formats.</li>
<li>Comparing the effectiveness of more than two advertising campaigns.</li>
</ul>

<h3>4.4 ANOVA Techniques</h3>
<p>ANOVA works by partitioning the total variation in the data into components: variation <em>between</em> groups (explained by the factor being studied) and variation <em>within</em> groups (random/error variation). The ratio of these two forms the <strong>F-statistic</strong>:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>F = (Variance Between Groups) &divide; (Variance Within Groups)</strong></p>
<p>A large F-value suggests the group means differ more than would be expected by chance alone.</p>

<h3>4.5 Analysis of Variance for One-Way Classification</h3>
<p>One-way ANOVA tests the effect of a single factor (e.g. "region") on a dependent variable (e.g. "sales"), comparing means across the factor's different levels/categories.</p>

<h3>4.6 Analysis of Variance for Two-Way Classification</h3>
<p>Two-way ANOVA tests the effect of two factors simultaneously (e.g. "region" and "season" on sales), and can also test whether the two factors interact &mdash; that is, whether the effect of one factor depends on the level of the other.</p>
<table class="compare">
<tr><th>Aspect</th><th>One-Way ANOVA</th><th>Two-Way ANOVA</th></tr>
<tr><td>Number of factors</td><td>One</td><td>Two</td></tr>
<tr><td>Can test interaction effects?</td><td>No</td><td>Yes</td></tr>
<tr><td>Example</td><td>Sales by region</td><td>Sales by region and season</td></tr>
</table>
"""
terms = [
    ("Analysis of Variance (ANOVA)", "A statistical technique that tests whether the means of three or more groups differ by comparing between-group and within-group variation."),
    ("F-Statistic", "The ratio of between-group variance to within-group variance used in ANOVA to test for significant differences."),
    ("One-Way ANOVA", "ANOVA used to test the effect of a single factor on a dependent variable across its different levels."),
    ("Two-Way ANOVA", "ANOVA used to test the effect of two factors, including any interaction between them, on a dependent variable."),
]
examprep = [
    "ANOVA compares means of 3+ groups via between-group vs within-group variance.",
    "Assumptions: independent observations, normal distribution, equal variances, interval/ratio data.",
    "F = Variance Between Groups / Variance Within Groups; large F suggests real group differences.",
    "One-way ANOVA: one factor. Two-way ANOVA: two factors, can test interaction effects.",
]
questions = [
    ("What is ANOVA and what assumptions underlie it?", "Analysis of Variance (ANOVA) tests whether the means of three or more groups differ significantly by comparing the variation between group means to the variation within groups. It assumes the observations are independent, each group is approximately normally distributed, the groups have roughly equal variances, and the dependent variable is measured on an interval or ratio scale."),
    ("Explain how the F-statistic is used in ANOVA.", "The F-statistic is the ratio of the variance between groups to the variance within groups. A large F-value indicates that the differences between group means are larger than would be expected from random variation alone, leading to rejection of the null hypothesis that all group means are equal."),
    ("Differentiate between one-way and two-way ANOVA.", "One-way ANOVA tests the effect of a single factor on a dependent variable across its different levels, such as sales across regions. Two-way ANOVA tests the effect of two factors simultaneously, such as region and season on sales, and can additionally test whether the two factors interact with each other."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("When a research problem involves many variables at once, multivariate techniques are needed. "
            "This topic surveys the major multivariate methods used in business research and what each is "
            "designed to achieve.")
notes = """
<h3>5.1 Introduction to Multivariate Analysis</h3>
<p>Multivariate analysis refers to statistical techniques that analyse relationships among three or more variables simultaneously, used when a business problem is too complex to be understood through univariate or bivariate methods alone.</p>

<h3>5.2 Multivariate Statistical Techniques: Overview</h3>
<table class="compare">
<tr><th>Technique</th><th>Objective</th></tr>
<tr><td><strong>Multiple Regression and Correlation</strong></td><td>Predicts a single dependent variable from two or more independent variables; multiple correlation measures the overall strength of that combined relationship.</td></tr>
<tr><td><strong>Discriminant Analysis</strong></td><td>Classifies observations into two or more pre-defined categories based on a set of predictor variables.</td></tr>
<tr><td><strong>Factor Analysis</strong></td><td>Reduces a large number of correlated variables into a smaller number of underlying "factors".</td></tr>
<tr><td><strong>Cluster Analysis</strong></td><td>Groups observations into clusters so that items within a cluster are similar and items in different clusters are dissimilar.</td></tr>
<tr><td><strong>Multi-Dimensional Scaling (MDS)</strong></td><td>Represents the perceived similarity or dissimilarity among objects visually in a low-dimensional space (a "perceptual map").</td></tr>
<tr><td><strong>Conjoint Analysis</strong></td><td>Determines the relative importance consumers place on different attributes of a product or service.</td></tr>
</table>

<h3>5.3 Multiple Regression and Correlation</h3>
<p>Multiple regression extends simple regression to two or more independent variables: <strong>Y = a + b&#8321;X&#8321; + b&#8322;X&#8322; + ... + b&#8344;X&#8344;</strong>. Multiple correlation (R) measures how well the full set of independent variables together predicts the dependent variable.</p>

<h3>5.4 Discriminant Analysis</h3>
<p><strong>Objectives:</strong> to identify which predictor variables best distinguish between groups, and to classify new observations into the correct group.<br>
<strong>Steps:</strong> define the groups, select predictor variables, estimate the discriminant function, and validate its classification accuracy.<br>
<strong>Applications:</strong> classifying customers as likely to churn or not, or classifying loan applicants as high or low credit risk.</p>

<h3>5.5 Factor Analysis</h3>
<p><strong>Objectives:</strong> to simplify a large set of correlated variables (e.g. many survey items) into a smaller number of meaningful underlying dimensions.<br>
<strong>Steps:</strong> compute the correlation matrix, extract factors, rotate factors for interpretability, and name/interpret the resulting factors.<br>
<strong>Applications:</strong> identifying the underlying dimensions of customer satisfaction from a long list of survey questions.</p>

<h3>5.6 Cluster Analysis</h3>
<p><strong>Objectives:</strong> to segment a set of observations into naturally occurring, homogeneous groups.<br>
<strong>Steps:</strong> choose a similarity/distance measure, select a clustering method, decide the number of clusters, and profile each cluster.<br>
<strong>Applications:</strong> market segmentation based on customer behaviour or demographics.</p>

<h3>5.7 Multi-Dimensional Scaling (MDS)</h3>
<p><strong>Objectives:</strong> to visually map how objects (e.g. competing brands) are perceived relative to one another.<br>
<strong>Procedure:</strong> collect similarity/preference data, apply the MDS algorithm to position objects in a low-dimensional space, and interpret the resulting map.<br>
<strong>Applications:</strong> competitive brand-positioning maps.</p>

<h3>5.8 Conjoint Analysis</h3>
<p><strong>Objectives:</strong> to measure how much each attribute of a product (e.g. price, brand, features) contributes to overall consumer preference.<br>
<strong>Procedure:</strong> select attributes to be tested, present respondents with combinations of attributes to rank or rate, and estimate each attribute's relative importance ("utility").<br>
<strong>Applications:</strong> new-product design and pricing decisions.</p>
"""
terms = [
    ("Multivariate Analysis", "Statistical techniques that analyse relationships among three or more variables simultaneously."),
    ("Multiple Regression", "Regression analysis that predicts a dependent variable from two or more independent variables."),
    ("Discriminant Analysis", "A technique that classifies observations into pre-defined categories based on predictor variables."),
    ("Factor Analysis", "A technique that reduces a large number of correlated variables into a smaller number of underlying factors."),
    ("Cluster Analysis", "A technique that groups observations into clusters of similar items."),
    ("Conjoint Analysis", "A technique that measures the relative importance consumers place on different product attributes."),
]
examprep = [
    "Multivariate techniques: multiple regression, discriminant analysis, factor analysis, cluster analysis, MDS, conjoint analysis.",
    "Multiple regression: Y = a + b1X1 + b2X2 + ... + bnXn; multiple correlation R = overall predictive strength.",
    "Discriminant analysis = classifies observations into pre-defined groups.",
    "Factor analysis = reduces many variables into fewer underlying factors.",
    "Cluster analysis = groups observations into similar segments (no pre-defined groups).",
    "Conjoint analysis = measures relative importance of product attributes to preference.",
]
questions = [
    ("What is multivariate analysis and when is it used?", "Multivariate analysis refers to statistical techniques that analyse relationships among three or more variables simultaneously. It is used when a business problem is too complex to be understood through examining one variable (univariate) or two variables (bivariate) at a time."),
    ("Differentiate between factor analysis and cluster analysis.", "Factor analysis reduces a large number of correlated variables into a smaller number of underlying factors, simplifying the variable set itself. Cluster analysis instead groups observations (such as customers) into homogeneous segments based on similarity across variables, without reducing the variables themselves."),
    ("Explain discriminant analysis with its objectives and an application.", "Discriminant analysis identifies which predictor variables best distinguish between pre-defined groups and classifies new observations into the correct group. A common application is classifying loan applicants as high or low credit risk based on variables such as income, credit history and debt level."),
    ("What is conjoint analysis used for in business research?", "Conjoint analysis measures how much each attribute of a product or service, such as price, brand and features, contributes to overall consumer preference, by having respondents evaluate combinations of attributes. It is commonly applied in new-product design and pricing decisions."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("The closing topic of this unit covers hypothesis testing &mdash; the formal statistical "
            "procedure for deciding, based on sample data, whether to accept or reject a hypothesis about "
            "a population.")
notes = """
<h3>6.1 Introduction to Hypothesis Testing</h3>
<p>Hypothesis testing is a statistical procedure that uses sample data to evaluate whether there is enough evidence to reject a stated hypothesis about a population, allowing researchers to make inferential decisions with a known level of risk.</p>

<h3>6.2 Hypothesis Decision Table</h3>
<table class="compare">
<tr><th></th><th>H&#8320; is actually True</th><th>H&#8320; is actually False</th></tr>
<tr><td><strong>Fail to Reject H&#8320;</strong></td><td>Correct decision</td><td>Type&nbsp;II Error (&beta;)</td></tr>
<tr><td><strong>Reject H&#8320;</strong></td><td>Type&nbsp;I Error (&alpha;)</td><td>Correct decision</td></tr>
</table>

<h3>6.3 Elements of Hypothesis Testing</h3>
<ul>
<li>Null hypothesis (H&#8320;) and alternative hypothesis (H&#8321;).</li>
<li>Test statistic appropriate to the data and hypothesis.</li>
<li>Level of significance (&alpha;).</li>
<li>Decision rule (critical value or p-value approach).</li>
</ul>

<h3>6.4 Steps in Testing a Hypothesis</h3>
<ol>
<li>State the null and alternative hypotheses.</li>
<li>Choose the level of significance (&alpha;).</li>
<li>Select the appropriate test statistic.</li>
<li>Determine the critical value/region or compute the p-value.</li>
<li>Calculate the test statistic from the sample data.</li>
<li>Compare the calculated value with the critical value (or p-value with &alpha;) and decide whether to reject H&#8320;.</li>
<li>State the conclusion in the context of the original business problem.</li>
</ol>

<h3>6.5 Importance and Limitations of the Tests of Hypothesis</h3>
<p>Hypothesis tests provide an objective, standardised way to decide whether an observed sample result reflects a real population effect or could plausibly be due to chance, which is essential for evidence-based decision-making. Their limitations include the risk of Type I/Type II errors, sensitivity to sample size, and the fact that statistical significance does not automatically imply practical/managerial significance.</p>

<h3>6.6 Important Terms in Hypothesis Testing</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Errors in Hypothesis Testing</h4>
<ul>
<li><strong>Type I Error (&alpha;)</strong> &mdash; rejecting a true null hypothesis (a "false positive").</li>
<li><strong>Type II Error (&beta;)</strong> &mdash; failing to reject a false null hypothesis (a "false negative").</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Level of Significance</h4>
<p>The probability of committing a Type I error that the researcher is willing to accept, commonly set at 0.05 (5%) or 0.01 (1%).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Degree of Freedom</h4>
<p>The number of independent values that are free to vary in a calculation, used to identify the correct reference distribution (e.g. for the t-test or chi-square test).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">One-Tailed and Two-Tailed Tests</h4>
<p>A <strong>one-tailed test</strong> places the entire rejection region in one direction (used when the hypothesis specifies a direction, e.g. "greater than"). A <strong>two-tailed test</strong> splits the rejection region between both ends (used when the hypothesis only states "different from", with no specified direction).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Measuring the Power of a Hypothesis Test</h4>
<p>The power of a test is the probability of correctly rejecting a false null hypothesis, equal to (1 &minus; &beta;). Higher power means a greater ability to detect a real effect when one exists; power increases with larger sample sizes.</p>
"""
terms = [
    ("Null Hypothesis (H0)", "A hypothesis stating there is no effect or difference, which hypothesis testing seeks to reject or fail to reject."),
    ("Type I Error", "Rejecting a null hypothesis that is actually true (a false positive), with probability alpha."),
    ("Type II Error", "Failing to reject a null hypothesis that is actually false (a false negative), with probability beta."),
    ("Level of Significance", "The probability of committing a Type I error that the researcher is willing to accept, commonly 0.05 or 0.01."),
    ("Power of a Test", "The probability of correctly rejecting a false null hypothesis, equal to 1 minus beta."),
]
examprep = [
    "Steps: state H0/H1 &rarr; choose alpha &rarr; select test statistic &rarr; find critical value/p-value &rarr; compute statistic &rarr; decide &rarr; conclude.",
    "Type I error (alpha) = reject true H0; Type II error (beta) = fail to reject false H0.",
    "Level of significance = acceptable probability of Type I error (commonly 0.05 or 0.01).",
    "One-tailed test = directional hypothesis; Two-tailed test = non-directional hypothesis.",
    "Power of test = 1 - beta = probability of correctly rejecting a false H0; increases with sample size.",
]
questions = [
    ("Explain Type I and Type II errors in hypothesis testing.", "A Type I error occurs when a true null hypothesis is incorrectly rejected (a false positive), with probability denoted alpha. A Type II error occurs when a false null hypothesis is incorrectly not rejected (a false negative), with probability denoted beta. There is generally a trade-off between the two: reducing one tends to increase the other for a fixed sample size."),
    ("Outline the steps involved in testing a hypothesis.", "Hypothesis testing proceeds by stating the null and alternative hypotheses, choosing the level of significance, selecting the appropriate test statistic, determining the critical value or p-value, calculating the test statistic from sample data, comparing it against the critical value or p-value to decide whether to reject the null hypothesis, and finally stating the conclusion in the context of the business problem."),
    ("Differentiate between one-tailed and two-tailed tests.", "A one-tailed test places the entire rejection region in one direction and is used when the alternative hypothesis specifies a direction, such as 'greater than'. A two-tailed test splits the rejection region between both ends of the distribution and is used when the alternative hypothesis simply states that a difference exists, without specifying its direction."),
    ("What is meant by the power of a hypothesis test?", "The power of a hypothesis test is the probability of correctly rejecting a null hypothesis that is actually false, calculated as 1 minus beta (the Type II error probability). Higher power means a greater ability to detect a real effect, and power generally increases as the sample size increases."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 6 done")

U.write_index("Book: <em>Business Research Methods</em> (BA4205) &middot; Unit 4 covers data preparation, data analysis types, bi-variate analysis (correlation/regression), ANOVA, multivariate analysis, and hypothesis testing.")
print("Unit 4 index done")
