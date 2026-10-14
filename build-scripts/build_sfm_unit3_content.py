# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Statistics-for-Management\units"
BOOK_HTML = "Book: <em>Statistics for Management</em> (BA4101, Anna University MBA Sem I, Regulation 2021)"
BOOK_PLAIN = "Statistics for Management (BA4101)"

TOPICS = [
    ("topic1-introduction-to-hypothesis-testing.html", "Introduction to Hypothesis Testing"),
    ("topic2-z-tests-means-proportions-large-samples.html", "Z-Tests for Means and Proportions (Large Samples)"),
    ("topic3-t-tests-means-small-samples.html", "T-Tests for Means (Small Samples)"),
    ("topic4-f-test-two-sample-standard-deviations.html", "F-Test for Two Sample Standard Deviations"),
    ("topic5-anova-one-way.html", "ANOVA &mdash; One Way"),
    ("topic6-anova-two-way.html", "ANOVA &mdash; Two Way"),
]

BLUE_THEME = dict(accent="#2f5f8f", accent_dark="#1d3c57", accent_light="#e7eef5",
                   border="#d3dfea", shadow="rgba(47,95,143,.14)")

U = common.UnitBuilder(3, "Testing of Hypothesis - Parametric Tests", TOPICS,
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
overview = ("Hypothesis testing is the formal statistical procedure for deciding whether sample evidence is "
            "strong enough to challenge an existing claim about a population. This topic covers its "
            "vocabulary, logic, and the general step-by-step procedure used throughout this unit.")
notes = """
<h3>1.1 Meaning of Hypothesis Testing</h3>
<p>Hypothesis testing is a statistical procedure that uses sample data to evaluate whether there is enough evidence to reject a stated claim (hypothesis) about a population parameter.</p>

<h3>1.2 Null and Alternative Hypothesis</h3>
<table class="compare">
<tr><th>Hypothesis</th><th>Meaning</th></tr>
<tr><td><strong>Null Hypothesis (H&#8320;)</strong></td><td>The default claim of "no difference" or "no effect," assumed true unless the sample data provides strong evidence against it.</td></tr>
<tr><td><strong>Alternative Hypothesis (H&#8321;)</strong></td><td>The claim that contradicts the null hypothesis &mdash; what the test is trying to find evidence for.</td></tr>
</table>
<p>A test is <strong>two-tailed</strong> when H&#8321; states the parameter is simply "not equal to" a value, and <strong>one-tailed</strong> when H&#8321; specifies a direction ("greater than" or "less than").</p>

<h3>1.3 Type I and Type II Errors</h3>
<table class="compare">
<tr><th></th><th>H&#8320; is actually True</th><th>H&#8320; is actually False</th></tr>
<tr><td><strong>Reject H&#8320;</strong></td><td>Type I Error (probability = &alpha;)</td><td>Correct Decision</td></tr>
<tr><td><strong>Fail to Reject H&#8320;</strong></td><td>Correct Decision</td><td>Type II Error (probability = &beta;)</td></tr>
</table>
<ul>
<li><strong>Type I Error:</strong> Rejecting a true null hypothesis (a "false positive"). Its probability is the <strong>significance level, &alpha;</strong>, commonly set at 0.05 or 0.01.</li>
<li><strong>Type II Error:</strong> Failing to reject a false null hypothesis (a "false negative"). Its probability is denoted &beta;.</li>
</ul>

<h3>1.4 Level of Significance and Critical Region</h3>
<p>The <strong>level of significance (&alpha;)</strong> is the probability of making a Type I error that the researcher is willing to accept, typically chosen before the test is conducted. The <strong>critical region</strong> (or rejection region) is the range of test-statistic values for which H&#8320; is rejected; the <strong>critical value</strong> is the boundary of this region.</p>

<h3>1.5 General Steps in Hypothesis Testing</h3>
<ol>
<li><strong>State the Null and Alternative Hypotheses</strong> (H&#8320; and H&#8321;).</li>
<li><strong>Choose the Level of Significance</strong> (&alpha;), typically 0.05 or 0.01.</li>
<li><strong>Select the Appropriate Test Statistic</strong> (Z, t, F, or &chi;&sup2;, depending on the situation).</li>
<li><strong>Determine the Critical Value(s)</strong> from the relevant statistical table.</li>
<li><strong>Calculate the Test Statistic</strong> from the sample data.</li>
<li><strong>Compare and Decide:</strong> If the calculated test statistic falls in the critical region (or if the p-value is less than &alpha;), reject H&#8320;; otherwise, fail to reject H&#8320;.</li>
<li><strong>State the Conclusion</strong> in the context of the original business or research question.</li>
</ol>

<h3>1.6 The p-Value Approach</h3>
<p>The <strong>p-value</strong> is the probability of obtaining a test statistic at least as extreme as the one calculated, assuming H&#8320; is true. If the p-value is less than &alpha;, H&#8320; is rejected; this approach is equivalent to the critical-value approach but is more commonly reported by statistical software.</p>
"""
terms = [
    ("Null Hypothesis (H0)", "The default claim of no difference or no effect, assumed true unless sample evidence strongly contradicts it."),
    ("Alternative Hypothesis (H1)", "The claim that contradicts the null hypothesis, which the test seeks evidence for."),
    ("Type I Error", "Rejecting a true null hypothesis; its probability is the significance level, alpha."),
    ("Type II Error", "Failing to reject a false null hypothesis; its probability is denoted beta."),
    ("Level of Significance (alpha)", "The probability of a Type I error that a researcher is willing to accept, commonly 0.05 or 0.01."),
    ("p-Value", "The probability of obtaining a test statistic at least as extreme as the one observed, assuming the null hypothesis is true."),
]
examprep = [
    "H0 = default/no-difference claim; H1 = contradicting claim being tested for.",
    "Type I error = reject true H0 (probability alpha); Type II error = fail to reject false H0 (probability beta).",
    "7 steps: State H0/H1 &rarr; Choose alpha &rarr; Select test statistic &rarr; Find critical value &rarr; Calculate test statistic &rarr; Compare &amp; decide &rarr; Conclude.",
    "p-value < alpha &rArr; reject H0 (p-value approach, equivalent to critical-value approach).",
]
questions = [
    ("Define null and alternative hypothesis with an example.", "The null hypothesis (H0) is the default claim of no difference, e.g. 'the mean delivery time is 30 minutes.' The alternative hypothesis (H1) is the contradicting claim being tested for, e.g. 'the mean delivery time is not 30 minutes.'"),
    ("Differentiate between Type I and Type II errors.", "A Type I error is rejecting a true null hypothesis (a false positive), with probability alpha (the significance level). A Type II error is failing to reject a false null hypothesis (a false negative), with probability beta."),
    ("Explain the general steps involved in hypothesis testing.", "State H0 and H1, choose the significance level alpha, select the appropriate test statistic, determine the critical value from statistical tables, calculate the test statistic from sample data, compare the calculated value to the critical value (or the p-value to alpha) to decide whether to reject H0, and state the conclusion in context."),
    ("What is a p-value? How is it used to make a decision?", "The p-value is the probability of obtaining a test statistic at least as extreme as the one calculated, assuming the null hypothesis is true. If the p-value is less than the chosen significance level alpha, the null hypothesis is rejected; otherwise, it is not rejected."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("For large samples, the Z-test is used to test hypotheses about means and proportions, for both "
            "a single sample compared to a claimed value, and two samples compared to each other.")
notes = """
<h3>2.1 One-Sample Z-Test for the Mean</h3>
<p>Used to test whether a population mean equals a specific claimed value, when the sample size is large (n &ge; 30) or the population standard deviation &sigma; is known.</p>
<p style="text-align:center;font-size:1.1rem;"><strong>Z = (x&#772; &minus; &mu;&#8320;) &divide; (&sigma; &divide; &radic;n)</strong></p>
<p>where x&#772; is the sample mean, &mu;&#8320; is the hypothesised population mean under H&#8320;, &sigma; is the population (or large-sample estimated) standard deviation, and n is the sample size.</p>

<h3>2.2 Two-Sample Z-Test for Means</h3>
<p>Used to test whether two independent population means are equal, based on two large samples.</p>
<p style="text-align:center;font-size:1.1rem;"><strong>Z = (x&#772;&#8321; &minus; x&#772;&#8322;) &divide; &radic;[(&sigma;&#8321;&sup2;/n&#8321;) + (&sigma;&#8322;&sup2;/n&#8322;)]</strong></p>
<p>where x&#772;&#8321;, x&#772;&#8322; are the two sample means, &sigma;&#8321;&sup2;, &sigma;&#8322;&sup2; are the (known or large-sample estimated) population variances, and n&#8321;, n&#8322; are the two sample sizes.</p>

<h3>2.3 One-Sample Z-Test for the Proportion</h3>
<p>Used to test whether a population proportion equals a specific claimed value.</p>
<p style="text-align:center;font-size:1.1rem;"><strong>Z = (p&#773; &minus; p&#8320;) &divide; &radic;[p&#8320;(1&minus;p&#8320;) &divide; n]</strong></p>
<p>where p&#773; is the sample proportion and p&#8320; is the hypothesised population proportion under H&#8320;.</p>

<h3>2.4 Two-Sample Z-Test for Proportions</h3>
<p>Used to test whether two independent population proportions are equal.</p>
<p style="text-align:center;font-size:1.1rem;"><strong>Z = (p&#773;&#8321; &minus; p&#773;&#8322;) &divide; &radic;[p&#773;(1&minus;p&#773;)(1/n&#8321; + 1/n&#8322;)]</strong></p>
<p>where p&#773; is the <strong>pooled proportion</strong>, combining both samples: p&#773; = (x&#8321; + x&#8322;) &divide; (n&#8321; + n&#8322;), with x&#8321;, x&#8322; the number of successes in each sample.</p>

<h3>2.5 Decision Rule</h3>
<p>For a two-tailed test at &alpha; = 0.05, the critical Z-value is &plusmn;1.96; for a one-tailed test at &alpha; = 0.05, it is &plusmn;1.645. If the calculated |Z| exceeds the critical value, H&#8320; is rejected.</p>
"""
terms = [
    ("One-Sample Z-Test", "A hypothesis test comparing a single large sample's mean or proportion against a claimed population value."),
    ("Two-Sample Z-Test", "A hypothesis test comparing the means or proportions of two independent large samples against each other."),
    ("Pooled Proportion", "The combined proportion from two samples, used in the two-sample Z-test for proportions, calculated as total successes divided by total sample size."),
]
examprep = [
    "One-sample Z (mean): Z = (x-bar - mu0) / (sigma/sqrt(n)).",
    "Two-sample Z (means): Z = (x-bar1 - x-bar2) / sqrt[(sigma1^2/n1) + (sigma2^2/n2)].",
    "One-sample Z (proportion): Z = (p-hat - p0) / sqrt[p0(1-p0)/n].",
    "Two-sample Z (proportions): Z = (p-hat1 - p-hat2) / sqrt[p-bar(1-p-bar)(1/n1 + 1/n2)], using pooled proportion p-bar.",
    "Decision: two-tailed critical Z at alpha=0.05 is +/-1.96; one-tailed is +/-1.645; reject H0 if |Z calculated| > critical Z.",
]
questions = [
    ("Write the formula for the one-sample Z-test for the mean, and explain each term.", "Z = (x-bar - mu0) / (sigma/sqrt(n)), where x-bar is the sample mean, mu0 is the hypothesised population mean under H0, sigma is the population standard deviation, and n is the sample size."),
    ("Write the formula for the two-sample Z-test for means.", "Z = (x-bar1 - x-bar2) / sqrt[(sigma1^2/n1) + (sigma2^2/n2)], comparing the means of two independent large samples with known or large-sample-estimated variances."),
    ("What is a pooled proportion? Why is it used in the two-sample Z-test for proportions?", "The pooled proportion combines the successes from both samples into a single estimate, p-bar = (x1 + x2)/(n1 + n2). It is used because, under H0, both samples are assumed to come from populations with the same proportion, so pooling gives a better combined estimate of that common proportion for the standard error calculation."),
    ("State the decision rule for a two-tailed Z-test at the 5% level of significance.", "For a two-tailed test at alpha = 0.05, the critical Z-values are +/-1.96. If the calculated |Z| exceeds 1.96, the null hypothesis is rejected; otherwise, it is not rejected."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("When the sample size is small, the t-test replaces the Z-test for hypotheses about means, using "
            "the t-distribution introduced in Unit 2 to properly account for the extra uncertainty of a "
            "small sample.")
notes = """
<h3>3.1 When to Use the t-Test</h3>
<p>The t-test is used to test hypotheses about a population mean when the sample size is small (commonly n &lt; 30) and the population standard deviation &sigma; is unknown, so the sample standard deviation s must be used instead.</p>

<h3>3.2 One-Sample t-Test</h3>
<p style="text-align:center;font-size:1.1rem;"><strong>t = (x&#772; &minus; &mu;&#8320;) &divide; (s &divide; &radic;n)</strong></p>
<p>with degrees of freedom <strong>df = n &minus; 1</strong>. The calculated t-value is compared against the critical t-value from t-tables at the chosen significance level and df.</p>

<h3>3.3 Two-Sample t-Test (Independent Samples, Equal Variances Assumed)</h3>
<p>First, the <strong>pooled variance</strong> combining both samples is calculated:</p>
<p style="text-align:center;font-size:1.05rem;"><strong>s<sub>p</sub>&sup2; = [(n&#8321;&minus;1)s&#8321;&sup2; + (n&#8322;&minus;1)s&#8322;&sup2;] &divide; (n&#8321; + n&#8322; &minus; 2)</strong></p>
<p>Then the test statistic is:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>t = (x&#772;&#8321; &minus; x&#772;&#8322;) &divide; &radic;[s<sub>p</sub>&sup2;(1/n&#8321; + 1/n&#8322;)]</strong></p>
<p>with degrees of freedom <strong>df = n&#8321; + n&#8322; &minus; 2</strong>.</p>

<h3>3.4 Paired-Sample t-Test</h3>
<p>Used when the two samples are not independent, but are paired/matched observations (e.g. the same employees' performance before and after a training programme). The test works on the differences, d, between each pair:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>t = d&#772; &divide; (s<sub>d</sub> &divide; &radic;n)</strong></p>
<p>where d&#772; is the mean of the paired differences, s<sub>d</sub> is the standard deviation of the differences, and n is the number of pairs, with df = n &minus; 1.</p>

<h3>3.5 Comparing the t-Test and Z-Test</h3>
<table class="compare">
<tr><th>Basis</th><th>Z-Test</th><th>t-Test</th></tr>
<tr><td>Sample size</td><td>Large (n &ge; 30)</td><td>Small (n &lt; 30)</td></tr>
<tr><td>Population &sigma;</td><td>Known, or estimated from a large sample</td><td>Unknown; sample s used instead</td></tr>
<tr><td>Distribution used</td><td>Standard Normal (Z)</td><td>t-distribution (depends on df)</td></tr>
</table>
"""
terms = [
    ("One-Sample t-Test", "A test for whether a small sample's mean differs from a claimed population mean, using the sample standard deviation and t-distribution."),
    ("Pooled Variance", "A combined estimate of variance from two independent samples, used in the two-sample t-test assuming equal population variances."),
    ("Paired-Sample t-Test", "A t-test used for two related/matched samples, working on the differences between each pair of observations."),
]
examprep = [
    "One-sample t: t = (x-bar - mu0) / (s/sqrt(n)), df = n-1.",
    "Two-sample t (independent, equal variances): pooled variance sp^2 = [(n1-1)s1^2 + (n2-1)s2^2] / (n1+n2-2); t = (x-bar1 - x-bar2) / sqrt[sp^2(1/n1 + 1/n2)], df = n1+n2-2.",
    "Paired t-test: t = d-bar / (sd/sqrt(n)), df = n-1, works on differences between matched pairs.",
    "t-test used instead of Z-test when n is small and sigma is unknown.",
]
questions = [
    ("When is the t-test used instead of the Z-test?", "The t-test is used when the sample size is small (commonly n < 30) and the population standard deviation is unknown, so the sample standard deviation must be used, which the t-distribution's heavier tails account for."),
    ("Write the formula for the one-sample t-test and state its degrees of freedom.", "t = (x-bar - mu0) / (s/sqrt(n)), with degrees of freedom df = n - 1."),
    ("Explain the paired-sample t-test. When is it used?", "The paired-sample t-test is used when two samples consist of matched or related observations, such as the same subjects measured before and after a treatment. It works on the differences d between each pair, using t = d-bar / (sd/sqrt(n)), with df = n - 1, where n is the number of pairs."),
    ("Differentiate between the Z-test and the t-test.", "The Z-test is used for large samples (n >= 30) with a known or large-sample-estimated population standard deviation, using the standard normal distribution. The t-test is used for small samples (n < 30) with an unknown population standard deviation, using the sample standard deviation and the t-distribution, whose shape depends on degrees of freedom."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("The F-test compares the variability (not the mean) of two samples, and is also the foundation "
            "of the ANOVA technique covered in the next two topics.")
notes = """
<h3>4.1 Purpose of the F-Test</h3>
<p>The F-test is used to test whether two populations have equal variances (or standard deviations), based on two independent samples. It is also a prerequisite check before using the equal-variance, two-sample t-test from the previous topic, and is the test statistic underlying ANOVA.</p>

<h3>4.2 Hypotheses for the F-Test</h3>
<p>H&#8320;: &sigma;&#8321;&sup2; = &sigma;&#8322;&sup2; (the two population variances are equal)<br>
H&#8321;: &sigma;&#8321;&sup2; &ne; &sigma;&#8322;&sup2; (the two population variances are not equal)</p>

<h3>4.3 The F-Statistic</h3>
<p style="text-align:center;font-size:1.1rem;"><strong>F = s&#8321;&sup2; &divide; s&#8322;&sup2;</strong></p>
<p>where s&#8321;&sup2; is the larger of the two sample variances, and s&#8322;&sup2; is the smaller &mdash; by convention, the larger variance is always placed in the numerator, so the calculated F-value is always &ge; 1.</p>

<h3>4.4 Degrees of Freedom</h3>
<p>The F-distribution has two separate degrees of freedom: df&#8321; = n&#8321; &minus; 1 (numerator, from the sample with the larger variance), and df&#8322; = n&#8322; &minus; 1 (denominator, from the sample with the smaller variance).</p>

<h3>4.5 Decision Rule</h3>
<p>The calculated F-value is compared against the critical F-value from F-tables, found using df&#8321;, df&#8322;, and the chosen significance level &alpha;. If the calculated F exceeds the critical F, H&#8320; is rejected, meaning there is evidence the two population variances are not equal.</p>

<h3>4.6 Characteristics of the F-Distribution</h3>
<ul>
<li>The F-distribution is not symmetric &mdash; it is positively skewed.</li>
<li>F-values are always non-negative, since they are a ratio of two variances (which cannot be negative).</li>
<li>Its exact shape depends on both df&#8321; and df&#8322;.</li>
</ul>
"""
terms = [
    ("F-Test", "A hypothesis test comparing the variances of two independent populations using the ratio of their sample variances."),
    ("F-Statistic", "The ratio of the larger sample variance to the smaller sample variance, F = s1^2 / s2^2."),
    ("F-Distribution", "A positively skewed, non-negative probability distribution used for the F-test, with two separate degrees of freedom (numerator and denominator)."),
]
examprep = [
    "F-test H0: sigma1^2 = sigma2^2 (equal variances); H1: sigma1^2 != sigma2^2.",
    "F = s1^2 / s2^2, with the larger variance always placed in the numerator so F >= 1.",
    "df1 = n1-1 (numerator, larger-variance sample), df2 = n2-1 (denominator, smaller-variance sample).",
    "F-distribution: positively skewed, non-negative; reject H0 if calculated F > critical F.",
]
questions = [
    ("What is the purpose of the F-test?", "The F-test is used to test whether two populations have equal variances, based on two independent samples. It serves as a check before using the equal-variance two-sample t-test, and underlies the ANOVA technique."),
    ("State the F-statistic formula and explain the convention used.", "F = s1^2 / s2^2, where by convention the larger sample variance is always placed in the numerator and the smaller in the denominator, ensuring the calculated F-value is always greater than or equal to 1."),
    ("State the degrees of freedom used in the F-test.", "The F-distribution has two degrees of freedom: df1 = n1 - 1 for the numerator (the sample with the larger variance), and df2 = n2 - 1 for the denominator (the sample with the smaller variance)."),
    ("State the characteristics of the F-distribution.", "The F-distribution is positively skewed rather than symmetric, its values are always non-negative since it is a ratio of variances, and its exact shape depends on both the numerator and denominator degrees of freedom."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("While a t-test compares two group means, One-Way ANOVA (Analysis of Variance) extends the "
            "comparison to three or more groups at once, testing whether at least one group's mean differs "
            "from the others.")
notes = """
<h3>5.1 Why ANOVA Is Needed</h3>
<p>Running repeated t-tests on every possible pair among three or more groups inflates the overall chance of a Type I error. One-Way ANOVA instead tests all group means simultaneously in a single test, comparing variation <em>between</em> groups to variation <em>within</em> groups.</p>

<h3>5.2 Hypotheses for One-Way ANOVA</h3>
<p>H&#8320;: &mu;&#8321; = &mu;&#8322; = &mu;&#8323; = &hellip; = &mu;<sub>k</sub> (all k population means are equal)<br>
H&#8321;: At least one population mean is different from the others.</p>

<h3>5.3 The Logic of ANOVA</h3>
<p>ANOVA partitions the total variability in the data into two sources:</p>
<ul>
<li><strong>Between-Group Variation (SSB):</strong> Variation due to differences between the group means themselves.</li>
<li><strong>Within-Group Variation (SSW):</strong> Variation among individual observations within each group, around their own group mean (random/error variation).</li>
</ul>
<p>If the between-group variation is large relative to the within-group variation, this suggests the group means genuinely differ.</p>

<h3>5.4 The F-Statistic for ANOVA</h3>
<p style="text-align:center;font-size:1.1rem;"><strong>F = MSB &divide; MSW</strong></p>
<p>where <strong>MSB</strong> (Mean Square Between) = SSB &divide; (k &minus; 1), and <strong>MSW</strong> (Mean Square Within) = SSW &divide; (N &minus; k), with k = number of groups and N = total number of observations across all groups.</p>

<h3>5.5 The ANOVA Table</h3>
<table class="compare">
<tr><th>Source of Variation</th><th>Sum of Squares</th><th>df</th><th>Mean Square</th></tr>
<tr><td>Between Groups</td><td>SSB</td><td>k &minus; 1</td><td>MSB = SSB/(k&minus;1)</td></tr>
<tr><td>Within Groups</td><td>SSW</td><td>N &minus; k</td><td>MSW = SSW/(N&minus;k)</td></tr>
<tr><td>Total</td><td>SST = SSB + SSW</td><td>N &minus; 1</td><td>&mdash;</td></tr>
</table>

<h3>5.6 Decision Rule and Interpretation</h3>
<p>The calculated F is compared to the critical F-value (using df&#8321; = k&minus;1 and df&#8322; = N&minus;k). If F<sub>calculated</sub> &gt; F<sub>critical</sub>, H&#8320; is rejected, concluding that at least one group mean differs significantly from the others. ANOVA itself does not identify <em>which</em> group(s) differ &mdash; that requires a follow-up post-hoc test.</p>

<h3>5.7 Assumptions of ANOVA</h3>
<ul>
<li>Observations are independent, both within and between groups.</li>
<li>Each population from which the groups are drawn is approximately normally distributed.</li>
<li>The populations have approximately equal variances (homogeneity of variance), which can be checked using the F-test from the previous topic.</li>
</ul>
"""
terms = [
    ("One-Way ANOVA", "A statistical test comparing the means of three or more groups simultaneously by comparing between-group and within-group variation."),
    ("Between-Group Variation (SSB)", "The portion of total variability in ANOVA due to differences between the group means."),
    ("Within-Group Variation (SSW)", "The portion of total variability in ANOVA due to differences among individual observations within each group."),
    ("Mean Square", "A sum of squares divided by its corresponding degrees of freedom, used to calculate the F-statistic in ANOVA."),
]
examprep = [
    "ANOVA tests H0: all group means equal, vs H1: at least one group mean differs; avoids inflated Type I error from repeated t-tests.",
    "Total variation = Between-Group (SSB) + Within-Group (SSW).",
    "F = MSB / MSW, where MSB = SSB/(k-1) and MSW = SSW/(N-k); k = number of groups, N = total observations.",
    "Reject H0 if F(calculated) > F(critical); ANOVA alone doesn't say which group(s) differ (needs post-hoc test).",
    "Assumptions: independence, approximate normality within each group, homogeneity of variance across groups.",
]
questions = [
    ("Why is ANOVA used instead of multiple t-tests when comparing more than two groups?", "Running repeated t-tests on every pair of groups inflates the overall probability of a Type I error. ANOVA tests all group means simultaneously in a single test, avoiding this inflation."),
    ("State the hypotheses for One-Way ANOVA.", "H0: mu1 = mu2 = mu3 = ... = muk (all population means are equal). H1: at least one population mean differs from the others."),
    ("Explain the logic behind the ANOVA F-statistic.", "ANOVA partitions total variability into between-group variation (differences between group means) and within-group variation (random variation within each group). The F-statistic is the ratio of Mean Square Between to Mean Square Within; a large F suggests the group means differ more than would be expected from random variation alone."),
    ("State the assumptions of One-Way ANOVA.", "Observations must be independent, each group's population should be approximately normally distributed, and the populations should have approximately equal variances (homogeneity of variance)."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("Two-Way ANOVA extends One-Way ANOVA to examine the effect of two different factors "
            "simultaneously, and whether they interact with each other in their effect on the outcome.")
notes = """
<h3>6.1 When Two-Way ANOVA Is Used</h3>
<p>Two-Way ANOVA is used when data is classified by <strong>two independent factors</strong> at once (e.g. testing both the effect of three different training methods <em>and</em> three different regions on sales performance), rather than just one factor as in One-Way ANOVA.</p>

<h3>6.2 Hypotheses for Two-Way ANOVA</h3>
<p>Two-Way ANOVA tests three separate hypotheses at once:</p>
<ol>
<li><strong>Main Effect of Factor A:</strong> H&#8320;: all levels of Factor A have equal means.</li>
<li><strong>Main Effect of Factor B:</strong> H&#8320;: all levels of Factor B have equal means.</li>
<li><strong>Interaction Effect (A &times; B):</strong> H&#8320;: there is no interaction between Factor A and Factor B (the effect of one factor does not depend on the level of the other).</li>
</ol>

<h3>6.3 Partitioning Total Variation</h3>
<p>Two-Way ANOVA splits the total variation (SST) into four components:</p>
<ul>
<li><strong>SSA:</strong> Variation due to Factor A.</li>
<li><strong>SSB:</strong> Variation due to Factor B.</li>
<li><strong>SSAB:</strong> Variation due to the interaction between Factor A and Factor B.</li>
<li><strong>SSE:</strong> Residual/error (within-cell) variation, not explained by either factor or their interaction.</li>
</ul>
<p>SST = SSA + SSB + SSAB + SSE</p>

<h3>6.4 The Two-Way ANOVA Table</h3>
<table class="compare">
<tr><th>Source</th><th>df</th><th>Mean Square</th><th>F</th></tr>
<tr><td>Factor A</td><td>a &minus; 1</td><td>MSA = SSA/(a&minus;1)</td><td>MSA/MSE</td></tr>
<tr><td>Factor B</td><td>b &minus; 1</td><td>MSB = SSB/(b&minus;1)</td><td>MSB/MSE</td></tr>
<tr><td>Interaction (A&times;B)</td><td>(a&minus;1)(b&minus;1)</td><td>MSAB = SSAB/[(a&minus;1)(b&minus;1)]</td><td>MSAB/MSE</td></tr>
<tr><td>Error</td><td>N &minus; ab</td><td>MSE = SSE/(N&minus;ab)</td><td>&mdash;</td></tr>
</table>
<p>where a = number of levels of Factor A, b = number of levels of Factor B, and N = total number of observations.</p>

<h3>6.5 Interpreting the Results</h3>
<p>Each F-ratio is compared against its own critical F-value (using the relevant degrees of freedom). An important practical point: if the <strong>interaction effect</strong> is found to be statistically significant, the two main effects should be interpreted cautiously, since the effect of one factor genuinely depends on the level of the other &mdash; the interaction should usually be examined and discussed first.</p>

<h3>6.6 Why Two-Way ANOVA Matters for Management</h3>
<p>Two-Way ANOVA lets managers test two business variables and their interaction in one study rather than two separate ones &mdash; for example, simultaneously assessing the effect of advertising medium and target age group on campaign response, including whether certain media work better for certain age groups specifically.</p>
"""
terms = [
    ("Two-Way ANOVA", "An ANOVA test examining the effect of two independent factors, and their interaction, on an outcome."),
    ("Main Effect", "The effect of a single factor on the outcome, averaged across the levels of the other factor, in Two-Way ANOVA."),
    ("Interaction Effect", "The extent to which the effect of one factor on the outcome depends on the level of the other factor."),
]
examprep = [
    "Two-Way ANOVA tests two factors (A, B) plus their interaction (A x B) at once; 3 sets of hypotheses: Factor A main effect, Factor B main effect, A x B interaction.",
    "Total variation SST = SSA + SSB + SSAB + SSE.",
    "Each effect's F = its Mean Square / MSE (Mean Square Error); compared to its own critical F value.",
    "If interaction is significant, interpret main effects cautiously &mdash; examine the interaction first.",
]
questions = [
    ("When is Two-Way ANOVA used instead of One-Way ANOVA?", "Two-Way ANOVA is used when data is classified by two independent factors simultaneously, allowing the researcher to test the main effect of each factor as well as whether the two factors interact in their effect on the outcome, rather than examining just one factor at a time."),
    ("State the three hypotheses tested in Two-Way ANOVA.", "The main effect of Factor A (H0: all levels of Factor A have equal means), the main effect of Factor B (H0: all levels of Factor B have equal means), and the interaction effect (H0: there is no interaction between Factor A and Factor B)."),
    ("How is total variation partitioned in Two-Way ANOVA?", "Total variation (SST) is partitioned into SSA (due to Factor A), SSB (due to Factor B), SSAB (due to the interaction between A and B), and SSE (residual error variation), such that SST = SSA + SSB + SSAB + SSE."),
    ("Why should a significant interaction effect be interpreted before the main effects?", "If the interaction effect is statistically significant, it means the effect of one factor genuinely depends on the level of the other factor, so interpreting either main effect alone (as if it applied uniformly) could be misleading; the interaction should be examined first to understand the fuller picture."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Six topics covering parametric hypothesis testing: introduction to hypothesis testing, Z-tests for means/proportions (large samples), t-tests for means (small samples), the F-test for two sample standard deviations, One-Way ANOVA, and Two-Way ANOVA.")

print("Unit 3 (Statistics for Management) complete: all 6 topics + index written.")
