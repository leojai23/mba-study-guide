# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Statistics-for-Management\units"
BOOK_HTML = "Book: <em>Statistics for Management</em> (BA4101, Anna University MBA Sem I, Regulation 2021)"
BOOK_PLAIN = "Statistics for Management (BA4101)"

TOPICS = [
    ("topic1-sampling-distributions-introduction.html", "Introduction to Sampling Distributions"),
    ("topic2-sampling-distribution-mean-proportion-clt.html", "Sampling Distribution of Mean and Proportion, and the Central Limit Theorem"),
    ("topic3-sampling-techniques.html", "Sampling Techniques"),
    ("topic4-point-interval-estimation-large-samples.html", "Point and Interval Estimation for Large Samples"),
    ("topic5-interval-estimation-small-samples-sample-size.html", "Interval Estimation for Small Samples and Determining Sample Size"),
]

BLUE_THEME = dict(accent="#2f5f8f", accent_dark="#1d3c57", accent_light="#e7eef5",
                   border="#d3dfea", shadow="rgba(47,95,143,.14)")

U = common.UnitBuilder(2, "Sampling Distribution and Estimation", TOPICS,
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
overview = ("This unit moves from probability theory to statistical inference &mdash; using a sample to draw "
            "conclusions about a population. This opening topic introduces the key idea that makes this "
            "possible: the sampling distribution.")
notes = """
<h3>1.1 Population and Sample</h3>
<p>A <strong>population</strong> is the complete set of all items or individuals of interest in a study. A <strong>sample</strong> is a subset of the population actually observed and measured. Since studying an entire population is often impractical, statistics uses samples to estimate population characteristics.</p>

<h3>1.2 Parameter and Statistic</h3>
<table class="compare">
<tr><th>Term</th><th>Meaning</th><th>Example Symbol</th></tr>
<tr><td><strong>Parameter</strong></td><td>A numerical characteristic of a population (usually unknown).</td><td>Population mean &mu;, population standard deviation &sigma;</td></tr>
<tr><td><strong>Statistic</strong></td><td>A numerical characteristic calculated from a sample, used to estimate the corresponding parameter.</td><td>Sample mean x&#772;, sample standard deviation s</td></tr>
</table>

<h3>1.3 Introduction to Sampling Distributions</h3>
<p>If repeated samples of the same size are drawn from a population, the value of a statistic (such as the sample mean) will differ from sample to sample. The <strong>sampling distribution</strong> of a statistic is the probability distribution of that statistic across all possible samples of a given size drawn from the population.</p>
<p>Sampling distributions are the theoretical bridge that lets us use a single sample's statistic to make a probability-based inference about the unknown population parameter &mdash; the entire logic of hypothesis testing and interval estimation in the next units rests on this idea.</p>

<h3>1.4 Sampling Error</h3>
<p>Sampling error is the difference between a sample statistic and the true population parameter, arising purely because a sample (rather than the whole population) was observed. Sampling error decreases, on average, as sample size increases.</p>

<h3>1.5 Standard Error</h3>
<p>The standard error of a statistic is the standard deviation of its sampling distribution &mdash; it measures how much the statistic is expected to vary from sample to sample. A smaller standard error means the sample statistic is likely to be closer to the true population parameter.</p>
"""
terms = [
    ("Population", "The complete set of all items or individuals of interest in a study."),
    ("Sample", "A subset of the population that is actually observed and measured."),
    ("Parameter", "A numerical characteristic of a population, usually unknown, such as the population mean mu."),
    ("Statistic", "A numerical characteristic calculated from a sample, used to estimate a population parameter."),
    ("Sampling Distribution", "The probability distribution of a statistic across all possible samples of a given size drawn from a population."),
    ("Standard Error", "The standard deviation of the sampling distribution of a statistic, measuring how much it varies from sample to sample."),
]
examprep = [
    "Population = entire group of interest; Sample = subset actually observed.",
    "Parameter (population, e.g. mu) vs Statistic (sample, e.g. x-bar, used to estimate the parameter).",
    "Sampling distribution = probability distribution of a statistic across all possible samples of a given size.",
    "Sampling error = difference between sample statistic and true population parameter; decreases as sample size increases.",
    "Standard error = standard deviation of the sampling distribution; smaller standard error = more precise estimate.",
]
questions = [
    ("Differentiate between a parameter and a statistic.", "A parameter is a numerical characteristic of a population, usually unknown, such as the population mean (mu). A statistic is a numerical characteristic calculated from a sample, such as the sample mean (x-bar), used to estimate the corresponding population parameter."),
    ("What is a sampling distribution? Why is it important?", "A sampling distribution is the probability distribution of a statistic (such as the sample mean) across all possible samples of a given size drawn from a population. It is important because it provides the theoretical basis for using a single sample's statistic to make probability-based inferences about an unknown population parameter."),
    ("Define sampling error and standard error.", "Sampling error is the difference between a sample statistic and the true population parameter, arising because a sample rather than the whole population was observed; it decreases as sample size increases. Standard error is the standard deviation of the sampling distribution of a statistic, measuring how much the statistic is expected to vary from sample to sample."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("This topic covers the sampling distributions of two of the most commonly used statistics "
            "&mdash; the sample mean and the sample proportion &mdash; and the Central Limit Theorem, one of "
            "the most important results in all of statistics.")
notes = """
<h3>2.1 Sampling Distribution of the Mean</h3>
<p>If repeated random samples of size n are drawn from a population with mean &mu; and standard deviation &sigma;, the sampling distribution of the sample mean x&#772; has:</p>
<ul>
<li><strong>Mean of the sampling distribution:</strong> equal to the population mean, &mu;<sub>x&#772;</sub> = &mu;.</li>
<li><strong>Standard Error of the Mean:</strong> &sigma;<sub>x&#772;</sub> = &sigma; &divide; &radic;n</li>
</ul>
<p>Notice that as the sample size n increases, the standard error decreases &mdash; larger samples give more precise (less variable) estimates of the population mean.</p>

<h3>2.2 The Central Limit Theorem (CLT)</h3>
<p>The Central Limit Theorem states that, for a sufficiently large sample size n (commonly, n &ge; 30), the sampling distribution of the sample mean x&#772; will be <strong>approximately normally distributed</strong>, regardless of the shape of the population distribution from which the sample is drawn.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Why the CLT Matters</h4>
<ul>
<li>It allows the normal distribution (and the Z-score method from Unit 1) to be used for inference about the sample mean, even when the population itself is not normally distributed.</li>
<li>It is the theoretical foundation for virtually all large-sample hypothesis tests and confidence intervals covered in the remaining units.</li>
<li>The larger the sample size, the closer the sampling distribution of x&#772; gets to a perfect normal shape.</li>
</ul>

<h3>2.3 Sampling Distribution of the Proportion</h3>
<p>When a population proportion p (e.g. the proportion of defective items) is being estimated from a sample, the sample proportion is denoted <strong>p&#773;</strong> (p-hat). For a sufficiently large sample size, the sampling distribution of p&#773; is also approximately normal, with:</p>
<ul>
<li><strong>Mean:</strong> &mu;<sub>p&#773;</sub> = p</li>
<li><strong>Standard Error of the Proportion:</strong> &sigma;<sub>p&#773;</sub> = &radic;[p(1&minus;p) &divide; n]</li>
</ul>
<p>As with the mean, the standard error of the proportion decreases as the sample size n increases, giving a more precise estimate of the true population proportion.</p>
"""
terms = [
    ("Standard Error of the Mean", "The standard deviation of the sampling distribution of the sample mean, equal to sigma divided by the square root of n."),
    ("Central Limit Theorem (CLT)", "The theorem stating that, for a sufficiently large sample size, the sampling distribution of the sample mean is approximately normal regardless of the population's shape."),
    ("Sample Proportion (p-hat)", "The proportion of a characteristic observed in a sample, used to estimate the population proportion p."),
]
examprep = [
    "Sampling distribution of the mean: mean = mu, standard error = sigma / sqrt(n).",
    "Central Limit Theorem: for n >= 30 (roughly), sampling distribution of x-bar is approximately normal regardless of the population's shape.",
    "Sampling distribution of the proportion: mean = p, standard error = sqrt[p(1-p)/n].",
    "Standard error (of mean or proportion) decreases as sample size n increases.",
]
questions = [
    ("State the mean and standard error of the sampling distribution of the sample mean.", "The mean of the sampling distribution of the sample mean equals the population mean, mu. The standard error is sigma / sqrt(n), where sigma is the population standard deviation and n is the sample size."),
    ("State the Central Limit Theorem. Why is it important?", "For a sufficiently large sample size (commonly n >= 30), the sampling distribution of the sample mean is approximately normally distributed, regardless of the shape of the population distribution. It is important because it allows normal-distribution-based methods to be used for inference about the sample mean even when the underlying population is not normal, and it underlies most large-sample hypothesis tests and confidence intervals."),
    ("State the mean and standard error of the sampling distribution of the sample proportion.", "The mean of the sampling distribution of the sample proportion p-hat equals the population proportion p. The standard error is the square root of [p(1-p)/n]."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("How a sample is selected affects how well it represents the population. This topic covers the "
            "main sampling techniques used in management research, divided into probability and "
            "non-probability methods.")
notes = """
<h3>3.1 Probability Sampling Techniques</h3>
<p>In probability sampling, every unit in the population has a known, non-zero chance of being selected, which allows sampling error to be objectively measured.</p>
<ol>
<li><strong>Simple Random Sampling:</strong> Every unit in the population has an equal chance of being selected, typically using random number generation.</li>
<li><strong>Systematic Sampling:</strong> Units are selected at a fixed interval from a randomly chosen starting point (e.g. every 10th customer).</li>
<li><strong>Stratified Sampling:</strong> The population is divided into relevant sub-groups (strata), and a random sample is drawn from each stratum, ensuring every sub-group is represented proportionally.</li>
<li><strong>Cluster Sampling:</strong> The population is divided into clusters (often geographic), a random sample of clusters is selected, and all (or a sample of) units within the chosen clusters are studied.</li>
</ol>

<h3>3.2 Non-Probability Sampling Techniques</h3>
<p>In non-probability sampling, units are selected based on convenience or judgement rather than random chance, so the probability of selection is unknown and sampling error cannot be objectively calculated.</p>
<ol>
<li><strong>Convenience Sampling:</strong> Units are selected simply because they are easy to access (e.g. surveying shoppers at a nearby mall).</li>
<li><strong>Judgemental (Purposive) Sampling:</strong> The researcher deliberately selects units believed to be most representative or informative.</li>
<li><strong>Quota Sampling:</strong> The researcher ensures certain sub-group quotas are filled, but without randomly selecting within each sub-group.</li>
<li><strong>Snowball Sampling:</strong> Existing study participants recruit future participants from among their own acquaintances, often used for hard-to-reach populations.</li>
</ol>

<h3>3.3 Choosing a Sampling Technique</h3>
<p>Probability sampling methods are generally preferred for formal statistical inference, since they allow sampling error to be measured and confidence intervals to be constructed validly. Non-probability methods are often used when they are faster, cheaper, or the only practical option, but any conclusions drawn carry greater risk of bias.</p>
"""
terms = [
    ("Probability Sampling", "A sampling method in which every unit in the population has a known, non-zero chance of selection."),
    ("Stratified Sampling", "A probability sampling method in which the population is divided into sub-groups (strata), and a random sample is drawn from each."),
    ("Cluster Sampling", "A probability sampling method in which the population is divided into clusters, a sample of clusters is randomly chosen, and units within those clusters are studied."),
    ("Non-Probability Sampling", "A sampling method in which units are selected based on convenience or judgement, so the probability of selection is unknown."),
]
examprep = [
    "Probability sampling (known selection chance): Simple Random, Systematic, Stratified, Cluster.",
    "Non-probability sampling (unknown selection chance): Convenience, Judgemental/Purposive, Quota, Snowball.",
    "Probability sampling preferred for formal statistical inference since sampling error can be measured.",
]
questions = [
    ("Explain the main probability sampling techniques.", "Simple Random Sampling gives every unit an equal chance of selection; Systematic Sampling selects units at a fixed interval from a random start; Stratified Sampling divides the population into sub-groups and samples randomly from each; Cluster Sampling selects whole clusters at random and studies units within them."),
    ("Explain the main non-probability sampling techniques.", "Convenience Sampling selects units that are easy to access; Judgemental (Purposive) Sampling deliberately selects units believed to be representative; Quota Sampling fills sub-group quotas without random selection within them; Snowball Sampling has existing participants recruit further participants, useful for hard-to-reach populations."),
    ("Why is probability sampling generally preferred for statistical inference?", "Because every unit has a known chance of selection, probability sampling allows sampling error to be objectively measured and valid confidence intervals to be constructed, whereas non-probability sampling carries unknown and potentially greater bias."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("Estimation uses sample data to infer the value of an unknown population parameter. This topic "
            "covers point estimation, and interval estimation for large samples using the normal "
            "distribution.")
notes = """
<h3>4.1 Point Estimation</h3>
<p>A point estimate is a single value, calculated from sample data, used as the best guess for an unknown population parameter. For example, the sample mean x&#772; is the point estimate of the population mean &mu;, and the sample proportion p&#773; is the point estimate of the population proportion p.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Properties of a Good Estimator</h4>
<ul>
<li><strong>Unbiasedness:</strong> The expected value of the estimator equals the true population parameter.</li>
<li><strong>Efficiency:</strong> Among unbiased estimators, the one with the smallest variance is preferred.</li>
<li><strong>Consistency:</strong> As sample size increases, the estimator converges toward the true population value.</li>
</ul>

<h3>4.2 Interval Estimation (Confidence Intervals)</h3>
<p>Because a point estimate alone gives no sense of its likely accuracy, an <strong>interval estimate</strong> (confidence interval) provides a range of values, together with a confidence level, within which the true population parameter is expected to lie.</p>

<h3>4.3 Confidence Interval for the Population Mean (Large Sample, n &ge; 30)</h3>
<p style="text-align:center;font-size:1.1rem;"><strong>x&#772; &plusmn; Z<sub>&alpha;/2</sub> &times; (&sigma; &divide; &radic;n)</strong></p>
<p>where x&#772; is the sample mean, Z<sub>&alpha;/2</sub> is the Z-value corresponding to the desired confidence level (1.96 for 95% confidence, 2.58 for 99% confidence), &sigma; is the population standard deviation (or the sample standard deviation s, if &sigma; is unknown and n is large), and n is the sample size.</p>

<h3>4.4 Confidence Interval for the Population Proportion (Large Sample)</h3>
<p style="text-align:center;font-size:1.1rem;"><strong>p&#773; &plusmn; Z<sub>&alpha;/2</sub> &times; &radic;[p&#773;(1&minus;p&#773;) &divide; n]</strong></p>
<p>where p&#773; is the sample proportion.</p>

<h3>4.5 Interpreting a Confidence Interval</h3>
<p>A 95% confidence interval does <em>not</em> mean there is a 95% probability the true parameter lies in this specific interval. It means that if the same sampling procedure were repeated many times, approximately 95% of the resulting intervals would contain the true population parameter.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Factors Affecting Confidence Interval Width</h4>
<ul>
<li>A higher confidence level (e.g. 99% vs 95%) produces a <strong>wider</strong> interval.</li>
<li>A larger sample size produces a <strong>narrower</strong> interval, since the standard error decreases.</li>
<li>Greater variability in the data (larger &sigma;) produces a <strong>wider</strong> interval.</li>
</ul>
"""
terms = [
    ("Point Estimate", "A single value calculated from sample data, used as the best guess for an unknown population parameter."),
    ("Interval Estimate (Confidence Interval)", "A range of values, with an associated confidence level, within which a population parameter is expected to lie."),
    ("Confidence Level", "The long-run proportion of repeated confidence intervals that would be expected to contain the true population parameter."),
    ("Unbiased Estimator", "An estimator whose expected value equals the true population parameter being estimated."),
]
examprep = [
    "Point estimate = single best-guess value (e.g. x-bar estimates mu); properties of a good estimator: unbiasedness, efficiency, consistency.",
    "CI for mean (large sample): x-bar +/- Z(alpha/2) x (sigma / sqrt(n)); common Z-values: 1.96 (95%), 2.58 (99%).",
    "CI for proportion (large sample): p-hat +/- Z(alpha/2) x sqrt[p-hat(1-p-hat)/n].",
    "Higher confidence level = wider interval; larger sample size = narrower interval; more variability = wider interval.",
]
questions = [
    ("What is a point estimate? State the properties of a good estimator.", "A point estimate is a single value from sample data used as the best guess for a population parameter, such as the sample mean estimating the population mean. A good estimator should be unbiased (expected value equals the true parameter), efficient (smallest variance among unbiased estimators), and consistent (converges to the true value as sample size grows)."),
    ("Write the formula for the confidence interval of the population mean for a large sample.", "x-bar +/- Z(alpha/2) x (sigma / sqrt(n)), where x-bar is the sample mean, Z(alpha/2) is the Z-value for the desired confidence level, sigma is the population (or large-sample estimate of the) standard deviation, and n is the sample size."),
    ("How does sample size and confidence level affect the width of a confidence interval?", "A larger sample size narrows the confidence interval because the standard error decreases, giving a more precise estimate. A higher confidence level (e.g. 99% instead of 95%) widens the interval, since a wider range is needed to be more confident of capturing the true parameter."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("This closing topic of Unit 2 covers interval estimation when the sample size is small, which "
            "requires the t-distribution rather than the normal distribution, and how to determine the "
            "sample size needed before data collection even begins.")
notes = """
<h3>5.1 Why Small Samples Need a Different Approach</h3>
<p>When the sample size is small (commonly, n &lt; 30) and the population standard deviation &sigma; is unknown, the sample standard deviation s is a less reliable estimate of &sigma;. Using the normal Z-distribution in this situation understates the true uncertainty, so the <strong>t-distribution</strong> is used instead.</p>

<h3>5.2 The t-Distribution</h3>
<p>The t-distribution is similar in shape to the normal distribution &mdash; symmetric and bell-shaped &mdash; but with heavier tails, reflecting the extra uncertainty from estimating &sigma; with a small sample. Its exact shape depends on the <strong>degrees of freedom (df)</strong>, df = n &minus; 1 for a single sample. As the sample size increases, the t-distribution approaches the normal distribution.</p>

<h3>5.3 Confidence Interval for the Mean (Small Sample)</h3>
<p style="text-align:center;font-size:1.1rem;"><strong>x&#772; &plusmn; t<sub>&alpha;/2, df</sub> &times; (s &divide; &radic;n)</strong></p>
<p>where t<sub>&alpha;/2, df</sub> is the critical t-value for the desired confidence level with df = n &minus; 1 degrees of freedom, taken from t-distribution tables, and s is the sample standard deviation.</p>

<h3>5.4 Determining the Sample Size</h3>
<p>Before collecting data, researchers often need to determine the minimum sample size required to estimate a parameter within a desired margin of error, E, at a given confidence level.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Sample Size for Estimating a Mean</h4>
<p style="text-align:center;font-size:1.1rem;"><strong>n = (Z<sub>&alpha;/2</sub> &times; &sigma; &divide; E)&sup2;</strong></p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Sample Size for Estimating a Proportion</h4>
<p style="text-align:center;font-size:1.1rem;"><strong>n = [Z<sub>&alpha;/2</sub>&sup2; &times; p(1&minus;p)] &divide; E&sup2;</strong></p>
<p>where E is the desired margin of error. If no prior estimate of p is available, <strong>p = 0.5</strong> is used, since this produces the most conservative (largest) required sample size.</p>

<h3>5.5 Factors Affecting Required Sample Size</h3>
<ul>
<li>A smaller desired margin of error E requires a <strong>larger</strong> sample size.</li>
<li>A higher confidence level requires a <strong>larger</strong> sample size (larger Z<sub>&alpha;/2</sub>).</li>
<li>Greater population variability (larger &sigma;, or p closer to 0.5) requires a <strong>larger</strong> sample size.</li>
</ul>
"""
terms = [
    ("t-Distribution", "A probability distribution similar to the normal distribution but with heavier tails, used for small-sample inference when the population standard deviation is unknown."),
    ("Degrees of Freedom (df)", "A parameter of the t-distribution, equal to n - 1 for a single-sample confidence interval, that determines its exact shape."),
    ("Margin of Error (E)", "The maximum expected difference between a point estimate and the true population parameter, used when determining required sample size."),
]
examprep = [
    "Small sample (n < 30), sigma unknown: use t-distribution instead of Z; df = n - 1; t-distribution has heavier tails than normal, approaches normal as n grows.",
    "CI for mean (small sample): x-bar +/- t(alpha/2, df) x (s / sqrt(n)).",
    "Sample size for mean: n = (Z(alpha/2) x sigma / E)^2.",
    "Sample size for proportion: n = [Z(alpha/2)^2 x p(1-p)] / E^2; use p = 0.5 if no prior estimate (most conservative, largest n).",
    "Smaller margin of error, higher confidence level, or greater variability all increase the required sample size.",
]
questions = [
    ("Why is the t-distribution used instead of the normal distribution for small samples?", "When the sample size is small (commonly n < 30) and the population standard deviation is unknown, the sample standard deviation is a less reliable estimate, so using the normal distribution would understate the true uncertainty. The t-distribution, with its heavier tails that reflect this extra uncertainty, is used instead, with the exact shape depending on the degrees of freedom (df = n - 1)."),
    ("Write the formula for the confidence interval of the mean for a small sample.", "x-bar +/- t(alpha/2, df) x (s / sqrt(n)), where t(alpha/2, df) is the critical t-value for the desired confidence level with df = n - 1 degrees of freedom, and s is the sample standard deviation."),
    ("How is the required sample size determined for estimating a population mean?", "Using n = (Z(alpha/2) x sigma / E)^2, where E is the desired margin of error, sigma is the population standard deviation (or an estimate), and Z(alpha/2) is the Z-value for the desired confidence level."),
    ("What value of p is used when determining sample size for a proportion if no prior estimate exists? Why?", "p = 0.5 is used, because p(1-p) is maximised at p = 0.5, which produces the largest (most conservative) required sample size, ensuring the sample is large enough regardless of the true proportion."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Five topics covering sampling distribution and estimation: introduction to sampling distributions, sampling distribution of mean/proportion and the Central Limit Theorem, sampling techniques, point/interval estimation for large samples, and interval estimation for small samples/determining sample size.")

print("Unit 2 (Statistics for Management) complete: all 5 topics + index written.")
