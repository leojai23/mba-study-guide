# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Statistics-for-Management\units"
BOOK_HTML = "Book: <em>Statistics for Management</em> (BA4101, Anna University MBA Sem I, Regulation 2021)"
BOOK_PLAIN = "Statistics for Management (BA4101)"

TOPICS = [
    ("topic1-introduction-sign-test.html", "Introduction to Non-Parametric Tests and the Sign Test"),
    ("topic2-mann-whitney-u-test.html", "Rank Sum Test: Mann-Whitney U Test"),
    ("topic3-kruskal-wallis-test.html", "Kruskal-Wallis Test"),
    ("topic4-kolmogorov-smirnov-run-test.html", "Kolmogorov-Smirnov Test and One Sample Run Test"),
    ("topic5-chi-square-goodness-of-fit-variance.html", "Chi-Square Test for Goodness of Fit and Single Sample Standard Deviation"),
    ("topic6-chi-square-independence-of-attributes.html", "Chi-Square Test for Independence of Attributes"),
]

BLUE_THEME = dict(accent="#2f5f8f", accent_dark="#1d3c57", accent_light="#e7eef5",
                   border="#d3dfea", shadow="rgba(47,95,143,.14)")

U = common.UnitBuilder(4, "Non-Parametric Tests", TOPICS,
                        subject="Statistics for Management",
                        subject_root=SUBJECT_ROOT,
                        book_html=BOOK_HTML, book_plain=BOOK_PLAIN, theme=BLUE_THEME)

def T(i):
    fname, title = TOPICS[i-1]
    prev_link = (TOPICS[i-2][0], TOPICS[i-2][1]) if i > 1 else None
    next_link = (TOPICS[i][0], TOPICS[i][1]) if i < len(TOPICS) else None
    return fname, title, prev_link, next_link

# ================= Topic 1 =================
fname, title, prev_link, next_link = T(1)
overview = ("Unit 3's tests all assumed the population data followed a known distribution (usually normal). "
            "This unit covers non-parametric tests, which make far fewer assumptions. This opening topic "
            "introduces the sign test, one of the simplest non-parametric tests.")
notes = """
<h3>1.1 What Are Non-Parametric Tests?</h3>
<p>Non-parametric tests are hypothesis tests that do not require the population to follow a specific distribution (such as normal), and often work directly with the ranks or signs of data rather than the raw numerical values themselves.</p>

<h3>1.2 When to Use Non-Parametric Tests</h3>
<ul>
<li>When the population distribution is unknown or clearly not normal.</li>
<li>When the sample size is very small, making it hard to verify normality.</li>
<li>When the data is ordinal (ranked) rather than truly numerical/interval-scaled.</li>
<li>When the data contains outliers that would distort a parametric test like the t-test.</li>
</ul>

<h3>1.3 Non-Parametric vs Parametric Tests</h3>
<table class="compare">
<tr><th>Basis</th><th>Parametric Tests</th><th>Non-Parametric Tests</th></tr>
<tr><td>Distribution Assumption</td><td>Requires a known distribution (usually normal)</td><td>Makes no (or very few) distributional assumptions</td></tr>
<tr><td>Data Type</td><td>Interval/ratio-scaled numerical data</td><td>Works with ordinal data, ranks, or signs too</td></tr>
<tr><td>Statistical Power</td><td>Generally more powerful when assumptions hold</td><td>Generally less powerful, but more robust when assumptions fail</td></tr>
<tr><td>Examples</td><td>Z-test, t-test, F-test, ANOVA</td><td>Sign test, Mann-Whitney U, Kruskal-Wallis, Chi-Square</td></tr>
</table>

<h3>1.4 The Sign Test &mdash; Single Sample</h3>
<p>The single-sample sign test checks whether a population median equals a hypothesised value, using only the <strong>sign</strong> (+ or &minus;) of each observation's deviation from that hypothesised median, ignoring the actual magnitude of the deviation.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Procedure</h4>
<ol>
<li>State H&#8320;: population median = a specified value.</li>
<li>For each observation, record a "+" if it is above the hypothesised median, a "&minus;" if below, and discard any observation exactly equal to it.</li>
<li>Count the number of plus signs and minus signs.</li>
<li>Under H&#8320;, the number of plus signs follows a Binomial distribution with p = 0.5; this Binomial (or its normal approximation for larger n) is used to test whether the observed split is consistent with chance.</li>
</ol>

<h3>1.5 The Sign Test &mdash; Paired Data</h3>
<p>The paired sign test is the non-parametric counterpart to the paired t-test from Unit 3, used to compare two related/matched samples (e.g. "before" and "after" scores) without assuming the differences are normally distributed.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Procedure</h4>
<ol>
<li>For each pair, calculate the difference and record only its sign (+ if the second value is greater, &minus; if smaller, discard ties).</li>
<li>Test whether the resulting mix of plus and minus signs is consistent with there being no systematic difference between the paired conditions (H&#8320;: equal numbers of + and &minus; signs are equally likely, i.e. p = 0.5).</li>
</ol>

<h3>1.6 Advantages and Limitations of the Sign Test</h3>
<ul>
<li><strong>Advantage:</strong> Extremely simple to apply and requires no distributional assumptions.</li>
<li><strong>Limitation:</strong> Because it discards the magnitude of each difference and uses only its sign, it is less statistically powerful than tests (parametric or non-parametric) that use more information from the data.</li>
</ul>
"""
terms = [
    ("Non-Parametric Test", "A hypothesis test that does not require the population to follow a specific distribution, often working with ranks or signs rather than raw values."),
    ("Sign Test", "A non-parametric test that uses only the sign (+ or -) of each observation's deviation from a hypothesised value, ignoring magnitude."),
    ("Paired Sign Test", "A non-parametric test comparing two related samples using only the sign of the difference within each matched pair."),
]
examprep = [
    "Non-parametric tests make no/few distributional assumptions; used for unknown/non-normal distributions, ordinal data, small samples, or outlier-prone data.",
    "Parametric (Z/t/F/ANOVA) vs Non-parametric (Sign, Mann-Whitney, Kruskal-Wallis, Chi-Square): distributional assumptions vs none; generally more power vs more robustness.",
    "Single-sample sign test: counts +/- signs of deviations from hypothesised median; under H0, number of + signs ~ Binomial(n, 0.5).",
    "Paired sign test: non-parametric counterpart to paired t-test, uses sign of each pair's difference only.",
    "Sign test advantage: simple, few assumptions; limitation: ignores magnitude, so less powerful than tests using full data.",
]
questions = [
    ("When are non-parametric tests preferred over parametric tests?", "Non-parametric tests are preferred when the population distribution is unknown or clearly not normal, when sample sizes are too small to verify normality, when data is ordinal rather than truly numerical, or when outliers would distort a parametric test."),
    ("Explain the procedure of the single-sample sign test.", "State H0 that the population median equals a specified value; record a plus sign for each observation above that value and a minus sign for each below (discarding ties); count the pluses and minuses; since the number of plus signs follows a Binomial(n, 0.5) distribution under H0, test whether the observed split is consistent with this."),
    ("What is the paired sign test used for?", "It is the non-parametric counterpart to the paired t-test, used to compare two related/matched samples (such as before-and-after scores) by looking only at the sign of the difference within each pair, without assuming the differences are normally distributed."),
    ("State an advantage and a limitation of the sign test.", "Advantage: it is extremely simple to apply and requires no distributional assumptions. Limitation: because it discards the magnitude of each difference and uses only its sign, it is less statistically powerful than tests that use more information from the data."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("The Mann-Whitney U Test is the non-parametric counterpart to the independent two-sample t-test, "
            "used to compare two independent groups when the data is ranked rather than normally "
            "distributed.")
notes = """
<h3>2.1 Purpose of the Mann-Whitney U Test</h3>
<p>The Mann-Whitney U Test (also called the Rank Sum Test or Wilcoxon-Mann-Whitney Test) compares two independent samples to determine whether they come from populations with the same distribution, without assuming normality. It is the non-parametric equivalent of the independent two-sample t-test.</p>

<h3>2.2 Hypotheses</h3>
<p>H&#8320;: The two populations have identical distributions (no difference between the groups).<br>
H&#8321;: The two populations differ (one tends to produce larger values than the other).</p>

<h3>2.3 Procedure</h3>
<ol>
<li><strong>Combine and Rank:</strong> Combine both samples into a single group and rank all observations together from smallest (rank 1) to largest, regardless of which sample each value came from.</li>
<li><strong>Sum the Ranks:</strong> Sum the ranks separately for each original sample, giving R&#8321; and R&#8322;.</li>
<li><strong>Calculate the U-Statistics:</strong></li>
</ol>
<p style="text-align:center;font-size:1.05rem;"><strong>U&#8321; = n&#8321;n&#8322; + [n&#8321;(n&#8321;+1) &divide; 2] &minus; R&#8321;</strong></p>
<p style="text-align:center;font-size:1.05rem;"><strong>U&#8322; = n&#8321;n&#8322; &minus; U&#8321;</strong></p>
<p>where n&#8321;, n&#8322; are the two sample sizes. The smaller of U&#8321; and U&#8322; is used as the test statistic, U.</p>
<ol start="4">
<li><strong>Compare and Decide:</strong> For small samples, U is compared against critical values from Mann-Whitney U tables. For larger samples, U can be converted to an approximately normal Z-statistic and compared against standard normal critical values.</li>
</ol>

<h3>2.4 Handling Tied Ranks</h3>
<p>When two or more observations have the same value, each is assigned the <strong>average</strong> of the ranks they would have occupied (e.g. if two values tie for ranks 3 and 4, both receive rank 3.5).</p>

<h3>2.5 When to Use the Mann-Whitney U Test</h3>
<ul>
<li>Comparing two independent groups when the data is ordinal, or numerical but not normally distributed.</li>
<li>Comparing two independent groups when sample sizes are too small to assess normality reliably.</li>
<li>As a more robust alternative to the two-sample t-test when outliers are present.</li>
</ul>
"""
terms = [
    ("Mann-Whitney U Test", "A non-parametric test comparing two independent samples by ranking all observations together, used as an alternative to the independent two-sample t-test."),
    ("U-Statistic", "The test statistic in the Mann-Whitney U Test, based on the sum of ranks for each sample; the smaller of U1 and U2 is used."),
    ("Tied Ranks", "Ranks assigned when two or more observations have equal values, calculated as the average of the ranks the tied values would otherwise occupy."),
]
examprep = [
    "Mann-Whitney U = non-parametric alternative to independent two-sample t-test; H0: identical distributions; H1: distributions differ.",
    "Procedure: combine and rank all observations together &rarr; sum ranks per sample (R1, R2) &rarr; calculate U1 = n1n2 + n1(n1+1)/2 - R1, U2 = n1n2 - U1 &rarr; use smaller U.",
    "Tied values: assign the average of the ranks they would occupy.",
    "Used for ordinal data, non-normal data, small samples, or when outliers would distort a t-test.",
]
questions = [
    ("What is the Mann-Whitney U Test used for?", "It is used to compare two independent samples to determine whether they come from populations with the same distribution, without assuming normality; it is the non-parametric equivalent of the independent two-sample t-test."),
    ("Explain the procedure for conducting the Mann-Whitney U Test.", "Combine both samples and rank all observations together from smallest to largest; sum the ranks separately for each sample (R1 and R2); calculate U1 = n1n2 + n1(n1+1)/2 - R1 and U2 = n1n2 - U1; use the smaller of U1 and U2 as the test statistic and compare it against critical values (or a normal approximation for larger samples)."),
    ("How are tied ranks handled in the Mann-Whitney U Test?", "When two or more observations have the same value, each is assigned the average of the ranks they would have occupied had they not been tied."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("The Kruskal-Wallis Test extends the logic of the Mann-Whitney U Test from two groups to three "
            "or more, serving as the non-parametric counterpart to One-Way ANOVA.")
notes = """
<h3>3.1 Purpose of the Kruskal-Wallis Test</h3>
<p>The Kruskal-Wallis Test compares three or more independent samples to determine whether they come from populations with the same distribution, without assuming normality. It is the non-parametric equivalent of One-Way ANOVA.</p>

<h3>3.2 Hypotheses</h3>
<p>H&#8320;: All k populations have identical distributions (no difference among the groups).<br>
H&#8321;: At least one population differs from the others.</p>

<h3>3.3 Procedure</h3>
<ol>
<li><strong>Combine and Rank:</strong> Combine all k samples into one group and rank all observations together from smallest to largest, using average ranks for ties.</li>
<li><strong>Sum the Ranks per Group:</strong> Calculate the sum of ranks R&#8321;, R&#8322;, &hellip;, R<sub>k</sub> for each of the k groups.</li>
<li><strong>Calculate the Test Statistic, H:</strong></li>
</ol>
<p style="text-align:center;font-size:1.05rem;"><strong>H = [12 &divide; N(N+1)] &times; &Sigma;(R<sub>i</sub>&sup2; &divide; n<sub>i</sub>) &minus; 3(N+1)</strong></p>
<p>where N is the total number of observations across all groups, n<sub>i</sub> is the sample size of group i, and R<sub>i</sub> is the rank sum of group i.</p>

<h3>3.4 Distribution of the Test Statistic</h3>
<p>For reasonably sized samples, H approximately follows a <strong>Chi-Square (&chi;&sup2;) distribution</strong> with <strong>df = k &minus; 1</strong> degrees of freedom, where k is the number of groups.</p>

<h3>3.5 Decision Rule</h3>
<p>The calculated H is compared against the critical &chi;&sup2; value at the chosen significance level with df = k &minus; 1. If H exceeds this critical value, H&#8320; is rejected, concluding that at least one group's distribution differs from the others.</p>

<h3>3.6 Kruskal-Wallis vs One-Way ANOVA</h3>
<table class="compare">
<tr><th>Basis</th><th>One-Way ANOVA</th><th>Kruskal-Wallis Test</th></tr>
<tr><td>Data required</td><td>Interval/ratio, approximately normal within groups</td><td>Ordinal, or numerical without a normality assumption</td></tr>
<tr><td>Works on</td><td>Actual values (via means)</td><td>Ranks of the combined data</td></tr>
<tr><td>Test statistic</td><td>F</td><td>H (approximately &chi;&sup2;)</td></tr>
</table>
<p>As with ANOVA, a significant Kruskal-Wallis result indicates that at least one group differs, but does not by itself identify which group(s); a follow-up test is needed for that.</p>
"""
terms = [
    ("Kruskal-Wallis Test", "A non-parametric test comparing three or more independent samples using ranks, equivalent to One-Way ANOVA."),
    ("H-Statistic", "The test statistic of the Kruskal-Wallis Test, which approximately follows a Chi-Square distribution with k-1 degrees of freedom."),
]
examprep = [
    "Kruskal-Wallis = non-parametric alternative to One-Way ANOVA, for 3+ independent groups; H0: all groups have identical distributions.",
    "Procedure: combine and rank all observations &rarr; sum ranks per group &rarr; H = [12/N(N+1)] * Sum(Ri^2/ni) - 3(N+1).",
    "H approximately follows Chi-Square distribution with df = k-1 (k = number of groups).",
    "Reject H0 if H(calculated) > critical Chi-Square value; doesn't identify which specific group(s) differ.",
]
questions = [
    ("What is the Kruskal-Wallis Test used for? What test is it the non-parametric equivalent of?", "It is used to compare three or more independent samples to determine whether they come from populations with the same distribution, without assuming normality. It is the non-parametric equivalent of One-Way ANOVA."),
    ("Write the formula for the Kruskal-Wallis H-statistic and explain its terms.", "H = [12 / N(N+1)] x Sum(Ri^2/ni) - 3(N+1), where N is the total number of observations across all groups, ni is the sample size of group i, and Ri is the sum of ranks for group i."),
    ("What distribution does the Kruskal-Wallis H-statistic follow, and what is its decision rule?", "H approximately follows a Chi-Square distribution with df = k-1 degrees of freedom, where k is the number of groups. If the calculated H exceeds the critical Chi-Square value at the chosen significance level, H0 is rejected, concluding at least one group's distribution differs from the others."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("This topic covers two further non-parametric tests: the Kolmogorov-Smirnov test, which checks "
            "how well a sample fits a hypothesised distribution, and the One Sample Run Test, which checks "
            "whether a sequence of data is genuinely random.")
notes = """
<h3>4.1 Kolmogorov-Smirnov (K-S) Test &mdash; Purpose</h3>
<p>The Kolmogorov-Smirnov test checks whether a sample's data is consistent with coming from a specific hypothesised distribution (a "goodness of fit" test), or whether two independent samples come from the same distribution (a two-sample version).</p>

<h3>4.2 One-Sample K-S Test &mdash; Procedure</h3>
<ol>
<li>State H&#8320;: the sample comes from the specified theoretical distribution (e.g. normal).</li>
<li>Calculate the sample's <strong>empirical cumulative distribution function (ECDF)</strong>, the proportion of observations at or below each value.</li>
<li>Calculate the <strong>theoretical cumulative distribution function (CDF)</strong> implied by the hypothesised distribution, at the same values.</li>
<li>Find <strong>D</strong>, the maximum absolute difference between the empirical and theoretical CDFs across all observed values.</li>
<li>Compare D against the critical D-value from K-S tables for the given sample size and significance level; if D exceeds the critical value, H&#8320; is rejected.</li>
</ol>

<h3>4.3 Comparing the K-S Test and the Chi-Square Goodness-of-Fit Test</h3>
<p>Both tests assess how well data fits a hypothesised distribution, but the K-S test works directly with individual, ungrouped data values (comparing cumulative distributions), while the Chi-Square test (covered in the next topic) works with data grouped into categories or class intervals. The K-S test is often considered more powerful for continuous data, since it does not lose information through grouping.</p>

<h3>4.4 One Sample Run Test &mdash; Purpose</h3>
<p>The One Sample Run Test (Wald-Wolfowitz Runs Test) checks whether a sequence of binary outcomes (e.g. above/below the median, success/failure) occurs in a <strong>genuinely random order</strong>, rather than following a pattern.</p>

<h3>4.5 Concept of a "Run"</h3>
<p>A <strong>run</strong> is a maximal sequence of consecutive identical symbols. For example, in the sequence A A B B B A B, there are 4 runs: (AA), (BBB), (A), (B).</p>

<h3>4.6 Procedure for the Run Test</h3>
<ol>
<li>State H&#8320;: the sequence of outcomes is random.</li>
<li>Count n&#8321; (number of one type of outcome), n&#8322; (number of the other type), and R (the total number of runs observed).</li>
<li>Too few runs suggests the data follows a pattern or trend (clustering); too many runs suggests an unusual, overly alternating pattern &mdash; both are evidence against randomness.</li>
<li>For small samples, R is compared against critical values from Run Test tables; for larger samples, R can be converted to an approximately normal Z-statistic.</li>
</ol>

<h3>4.7 Applications of the Run Test</h3>
<ul>
<li>Checking whether a production process is producing defects randomly, or in a detectable, non-random pattern (a signal of a systematic problem).</li>
<li>Checking whether stock price movements (up/down) over time appear random, relevant to market efficiency testing.</li>
<li>Verifying that a sequence of survey or experimental responses was not influenced by some uncontrolled ordering effect.</li>
</ul>
"""
terms = [
    ("Kolmogorov-Smirnov (K-S) Test", "A non-parametric test checking whether sample data is consistent with a specific hypothesised distribution, using the maximum difference between empirical and theoretical cumulative distributions."),
    ("D-Statistic", "The test statistic in the K-S test, the maximum absolute difference between the empirical and theoretical cumulative distribution functions."),
    ("One Sample Run Test", "A non-parametric test checking whether a sequence of binary outcomes occurs in a genuinely random order."),
    ("Run", "A maximal sequence of consecutive identical symbols or outcomes within a data sequence."),
]
examprep = [
    "K-S test: goodness-of-fit test comparing a sample's empirical CDF to a hypothesised theoretical CDF; D = max absolute difference between the two; reject H0 if D > critical value.",
    "K-S works on ungrouped/individual data (vs Chi-Square's grouped/categorical data) &mdash; often more powerful for continuous data.",
    "Run Test: checks if a binary sequence is random; Run = maximal sequence of consecutive identical symbols; too few or too many runs both indicate non-randomness.",
    "Run Test applications: process defect patterns, stock price movement randomness, survey response ordering effects.",
]
questions = [
    ("What is the Kolmogorov-Smirnov test used for? Explain its procedure.", "It tests whether sample data is consistent with coming from a hypothesised distribution. The procedure compares the sample's empirical cumulative distribution function to the theoretical CDF of the hypothesised distribution, finds D (the maximum absolute difference between them), and compares D to a critical value from K-S tables; if D exceeds the critical value, H0 is rejected."),
    ("Differentiate between the Kolmogorov-Smirnov test and the Chi-Square goodness-of-fit test.", "The K-S test works directly with individual, ungrouped data values by comparing cumulative distributions, while the Chi-Square test works with data grouped into categories or class intervals. The K-S test is often considered more powerful for continuous data since it avoids the information loss from grouping."),
    ("What is a 'run' in the context of the One Sample Run Test? What does the test check for?", "A run is a maximal sequence of consecutive identical symbols or outcomes in a data sequence. The One Sample Run Test checks whether a sequence of binary outcomes occurs in a genuinely random order; too few runs suggest clustering/patterning, and too many runs suggest unusual over-alternation, both indicating the sequence is not random."),
    ("State two applications of the One Sample Run Test.", "Checking whether a production process generates defects randomly or in a detectable non-random pattern, and checking whether stock price movements over time appear random, which is relevant to testing market efficiency."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("The Chi-Square distribution underlies several important non-parametric tests. This topic covers "
            "two of them: testing whether observed data fits an expected distribution (goodness of fit), "
            "and testing a claimed value for a single population's variance or standard deviation.")
notes = """
<h3>5.1 Chi-Square Test for Goodness of Fit &mdash; Purpose</h3>
<p>The Chi-Square Goodness of Fit Test checks whether observed categorical data matches an expected (hypothesised) distribution across several categories.</p>

<h3>5.2 Hypotheses</h3>
<p>H&#8320;: The observed frequencies match the expected (hypothesised) frequencies.<br>
H&#8321;: The observed frequencies do not match the expected frequencies.</p>

<h3>5.3 The Chi-Square Statistic</h3>
<p style="text-align:center;font-size:1.1rem;"><strong>&chi;&sup2; = &Sigma; [(O<sub>i</sub> &minus; E<sub>i</sub>)&sup2; &divide; E<sub>i</sub>]</strong></p>
<p>where O<sub>i</sub> is the observed frequency in category i, and E<sub>i</sub> is the expected frequency in category i under H&#8320;, summed across all categories.</p>
<p><strong>Degrees of freedom:</strong> df = (number of categories) &minus; 1.</p>

<h3>5.4 Decision Rule</h3>
<p>The calculated &chi;&sup2; is compared against the critical &chi;&sup2; value for the chosen significance level and df. If calculated &chi;&sup2; exceeds the critical value, H&#8320; is rejected &mdash; the observed data does not fit the hypothesised distribution well.</p>

<h3>5.5 Conditions for Using the Chi-Square Test</h3>
<ul>
<li>Data must be in the form of frequencies (counts), not percentages or raw scores.</li>
<li>Observations should be independent of one another.</li>
<li>Expected frequencies in each category should generally be 5 or more for the approximation to be reliable; categories may need to be combined if this is not met.</li>
</ul>

<h3>5.6 Chi-Square Test for a Single Sample's Standard Deviation (Variance)</h3>
<p>This test checks whether a population's variance (or standard deviation) equals a specific claimed value, using a sample.</p>
<p>H&#8320;: &sigma;&sup2; = &sigma;&#8320;&sup2; (the population variance equals the claimed value)</p>
<p style="text-align:center;font-size:1.1rem;"><strong>&chi;&sup2; = [(n &minus; 1) &times; s&sup2;] &divide; &sigma;&#8320;&sup2;</strong></p>
<p>where n is the sample size, s&sup2; is the sample variance, and &sigma;&#8320;&sup2; is the claimed population variance under H&#8320;, with <strong>df = n &minus; 1</strong>.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Decision Rule</h4>
<p>This test can be one-tailed or two-tailed depending on H&#8321;. The calculated &chi;&sup2; is compared against the appropriate critical &chi;&sup2; value(s) from &chi;&sup2; tables with df = n &minus; 1, and H&#8320; is rejected if the calculated value falls in the rejection region.</p>
"""
terms = [
    ("Chi-Square Goodness of Fit Test", "A test checking whether observed categorical frequencies match an expected (hypothesised) distribution, using the Chi-Square statistic."),
    ("Chi-Square Statistic", "The test statistic Sum of [(Observed - Expected)^2 / Expected] across categories, used in several Chi-Square-based tests."),
    ("Chi-Square Test for Variance", "A test checking whether a population's variance equals a claimed value, using (n-1)s^2 / sigma0^2 as the test statistic."),
]
examprep = [
    "Chi-Square Goodness of Fit: chi^2 = Sum[(Oi - Ei)^2 / Ei], df = (number of categories) - 1.",
    "Conditions: data as frequencies/counts, independent observations, expected frequency >= 5 per category (combine categories if not).",
    "Chi-Square test for variance: chi^2 = (n-1)s^2 / sigma0^2, df = n-1, tests H0: sigma^2 = sigma0^2.",
    "Reject H0 if calculated chi^2 exceeds the critical chi^2 value at the chosen df and significance level.",
]
questions = [
    ("State the formula for the Chi-Square Goodness of Fit test and its degrees of freedom.", "chi^2 = Sum of [(Oi - Ei)^2 / Ei], where Oi and Ei are the observed and expected frequencies in category i. Degrees of freedom = (number of categories) - 1."),
    ("State the conditions required for using the Chi-Square test.", "Data must be in the form of frequencies (counts), observations must be independent, and expected frequencies in each category should generally be 5 or more, with categories combined if this condition is not met."),
    ("State the formula used to test a population variance using the Chi-Square distribution.", "chi^2 = [(n-1) x s^2] / sigma0^2, where n is the sample size, s^2 is the sample variance, and sigma0^2 is the claimed population variance under H0, with degrees of freedom df = n - 1."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("This closing topic of Unit 4 covers the Chi-Square Test for Independence, used to determine "
            "whether two categorical attributes (e.g. gender and product preference) are statistically "
            "related or independent of each other.")
notes = """
<h3>6.1 Purpose of the Test</h3>
<p>The Chi-Square Test for Independence determines whether two categorical variables (attributes) are statistically independent of each other, or whether there is a significant association between them, based on data in a <strong>contingency table</strong> (also called a cross-tabulation).</p>

<h3>6.2 Hypotheses</h3>
<p>H&#8320;: The two attributes are independent (no association between them).<br>
H&#8321;: The two attributes are not independent (there is an association between them).</p>

<h3>6.3 Contingency Table</h3>
<p>Data is arranged in a table with the categories of one attribute as rows and the categories of the other as columns, with each cell showing the observed frequency (count) of items falling into that combination of categories.</p>

<h3>6.4 Calculating Expected Frequencies</h3>
<p>Under the assumption of independence (H&#8320;), the expected frequency for each cell is:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>E = (Row Total &times; Column Total) &divide; Grand Total</strong></p>

<h3>6.5 The Chi-Square Statistic</h3>
<p style="text-align:center;font-size:1.1rem;"><strong>&chi;&sup2; = &Sigma; [(O &minus; E)&sup2; &divide; E]</strong></p>
<p>summed across every cell in the contingency table, where O is the observed frequency and E is the expected frequency (calculated as above) for that cell.</p>

<h3>6.6 Degrees of Freedom</h3>
<p style="text-align:center;font-size:1.1rem;"><strong>df = (r &minus; 1) &times; (c &minus; 1)</strong></p>
<p>where r is the number of rows (categories of the first attribute) and c is the number of columns (categories of the second attribute) in the contingency table.</p>

<h3>6.7 Decision Rule</h3>
<p>The calculated &chi;&sup2; is compared against the critical &chi;&sup2; value for the chosen significance level and df = (r&minus;1)(c&minus;1). If calculated &chi;&sup2; exceeds the critical value, H&#8320; is rejected, concluding there is a statistically significant association between the two attributes.</p>

<h3>6.8 Applications in Management</h3>
<ul>
<li>Testing whether customer satisfaction level is associated with the store branch visited.</li>
<li>Testing whether employee department is associated with preferred training format.</li>
<li>Testing whether product defect type is associated with the production shift during which the item was made.</li>
<li>Market research &mdash; testing whether brand preference is associated with demographic categories such as age group or region.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Important Caveat</h4>
<p>A statistically significant Chi-Square result shows an association exists, but it does not by itself indicate the <strong>strength</strong> or the <strong>direction</strong> of that association &mdash; further measures (such as Cramer's V) or examination of the contingency table itself are needed for that.</p>
"""
terms = [
    ("Chi-Square Test for Independence", "A test determining whether two categorical attributes are statistically independent, based on data in a contingency table."),
    ("Contingency Table", "A table cross-tabulating the observed frequencies of two categorical attributes, with one attribute's categories as rows and the other's as columns."),
    ("Expected Frequency (Independence Test)", "The frequency expected in a contingency table cell under the assumption of independence, calculated as (Row Total x Column Total) / Grand Total."),
]
examprep = [
    "Chi-Square Test for Independence: H0 = two attributes are independent; uses a contingency table (rows x columns).",
    "Expected frequency per cell: E = (Row Total x Column Total) / Grand Total.",
    "chi^2 = Sum[(O-E)^2/E] across all cells; df = (r-1)(c-1).",
    "Significant result = association exists, but doesn't show strength/direction by itself.",
]
questions = [
    ("What does the Chi-Square Test for Independence check for?", "It checks whether two categorical attributes (such as gender and product preference) are statistically independent of each other, or whether there is a significant association between them, using data arranged in a contingency table."),
    ("How is the expected frequency calculated for a cell in a contingency table?", "E = (Row Total x Column Total) / Grand Total, calculated under the assumption that the two attributes are independent."),
    ("State the formula for degrees of freedom in the Chi-Square Test for Independence.", "df = (r - 1) x (c - 1), where r is the number of rows (categories of the first attribute) and c is the number of columns (categories of the second attribute) in the contingency table."),
    ("Give two management applications of the Chi-Square Test for Independence.", "Testing whether customer satisfaction level is associated with the store branch visited, and testing whether brand preference is associated with a demographic category such as age group, in market research."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Six topics covering non-parametric tests: introduction to non-parametric tests and the sign test, the Mann-Whitney U Test, the Kruskal-Wallis Test, the Kolmogorov-Smirnov Test and One Sample Run Test, the Chi-Square test for goodness of fit/variance, and the Chi-Square test for independence of attributes.")

print("Unit 4 (Statistics for Management) complete: all 6 topics + index written.")
