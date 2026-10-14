# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Statistics-for-Management\units"
BOOK_HTML = "Book: <em>Statistics for Management</em> (BA4101, Anna University MBA Sem I, Regulation 2021)"
BOOK_PLAIN = "Statistics for Management (BA4101)"

TOPICS = [
    ("topic1-basic-concepts-of-probability.html", "Basic Concepts of Probability"),
    ("topic2-counting-rules-sample-space-events.html", "Counting Rules, Sample Space and Events"),
    ("topic3-theorems-conditional-probability-bayes.html", "Theorems of Probability, Conditional Probability and Bayes' Theorem"),
    ("topic4-random-variables-probability-distributions.html", "Random Variables and Probability Distributions"),
    ("topic5-binomial-poisson-distributions.html", "Binomial and Poisson Distributions"),
    ("topic6-normal-distribution.html", "Normal Distribution"),
]

BLUE_THEME = dict(accent="#2f5f8f", accent_dark="#1d3c57", accent_light="#e7eef5",
                   border="#d3dfea", shadow="rgba(47,95,143,.14)")

U = common.UnitBuilder(1, "Probability and Probability Distributions", TOPICS,
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
overview = ("This opening topic introduces probability itself &mdash; what it means, how it is used in "
            "management decision-making, and the three approaches used to assign a probability value to an "
            "event.")
notes = """
<h3>1.1 Concept and Meaning of Probability</h3>
<p>Probability is a numerical measure, between 0 and 1, of the likelihood that a particular event will occur. A probability of 0 means the event is impossible; a probability of 1 means the event is certain.</p>
<p>For any event A, the probability is written <strong>P(A)</strong>, where <strong>0 &le; P(A) &le; 1</strong>.</p>

<h3>1.2 Characteristics of the Probability Function P(A)</h3>
<ul>
<li>The probability of any event lies between 0 and 1, inclusive.</li>
<li>The probability of the entire sample space (a certain event) is 1.</li>
<li>The probability of an impossible event is 0.</li>
<li>The sum of probabilities of all mutually exclusive outcomes in a sample space equals 1.</li>
</ul>

<h3>1.3 Applications of Probability in Decision-Making</h3>
<ul>
<li>Assessing the risk of a business decision before committing resources.</li>
<li>Quality control &mdash; estimating the chance of a defective item in a production batch.</li>
<li>Forecasting demand, sales or market outcomes under uncertainty.</li>
<li>Supporting decisions in finance, such as the likelihood of a project meeting its target return.</li>
</ul>

<h3>1.4 Uses and Rules of Probability</h3>
<p>Probability provides a disciplined way to quantify uncertainty so that decisions are not based purely on intuition. The basic rules that all probability values must satisfy are the characteristics listed in Section 1.2 above, and they form the foundation for every probability calculation covered later in this unit.</p>

<h3>1.5 Approaches to Probability Theory</h3>
<table class="compare">
<tr><th>Approach</th><th>Description</th></tr>
<tr><td><strong>Classical (A Priori) Probability</strong></td><td>Based on equally likely outcomes, calculated before any experiment is run: P(A) = (Number of favourable outcomes) &divide; (Total number of possible outcomes). Used when outcomes can be reasoned about in advance, e.g. a fair coin toss or die roll.</td></tr>
<tr><td><strong>Relative Frequency (Empirical) Probability</strong></td><td>Based on observed data from repeated trials: P(A) = (Number of times A occurred) &divide; (Total number of trials). Used when outcomes are determined from actual past experience or experimentation.</td></tr>
<tr><td><strong>Subjective Probability</strong></td><td>Based on personal judgement, experience, or belief, used when neither equally likely outcomes nor sufficient past data are available, e.g. a manager's estimate of the probability a new product will succeed.</td></tr>
</table>

<h3>1.6 Business Applications of Probability</h3>
<p>Businesses use probability to evaluate alternatives under uncertainty &mdash; for example, estimating the probability of various demand levels before setting a production quantity, or the probability that a supplier will deliver on time before finalising a procurement contract.</p>
"""
terms = [
    ("Probability", "A numerical measure between 0 and 1 of the likelihood that a particular event will occur."),
    ("Classical Probability", "Probability based on equally likely outcomes, calculated as favourable outcomes divided by total possible outcomes."),
    ("Empirical (Relative Frequency) Probability", "Probability based on the observed frequency of an event across repeated trials."),
    ("Subjective Probability", "Probability based on personal judgement or belief, used when equally likely outcomes or sufficient data are unavailable."),
]
examprep = [
    "Probability: 0 &le; P(A) &le; 1; P(certain event) = 1; P(impossible event) = 0; sum of all mutually exclusive outcomes = 1.",
    "Classical probability = favourable outcomes &divide; total outcomes (equally likely, a priori).",
    "Empirical probability = observed occurrences &divide; total trials (based on data).",
    "Subjective probability = based on personal judgement when neither of the above applies.",
]
questions = [
    ("Define probability. State its characteristics.", "Probability is a numerical measure between 0 and 1 of the likelihood an event will occur. Its characteristics: every probability lies between 0 and 1; a certain event has probability 1; an impossible event has probability 0; and the probabilities of all mutually exclusive outcomes in a sample space sum to 1."),
    ("Explain the three approaches to probability theory.", "Classical probability assumes equally likely outcomes and is calculated as favourable outcomes over total outcomes, before any experiment. Empirical (relative frequency) probability is based on the observed frequency of an event over repeated trials. Subjective probability is based on personal judgement or belief when neither equally likely outcomes nor sufficient data exist."),
    ("Discuss the applications of probability in business decision-making.", "Probability helps assess the risk of a decision before committing resources, supports quality control by estimating defect likelihood, aids demand forecasting under uncertainty, and supports financial decisions such as estimating the likelihood a project meets its target return."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("Before probability can be calculated for complex situations, a few basic building blocks are "
            "needed: the language of experiments, sample spaces and events, and the counting rules used to "
            "work out how many outcomes are possible in the first place.")
notes = """
<h3>2.1 Basic Concepts</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Experiment</h4>
<p>A random experiment is any process that produces one of several possible outcomes, where the specific outcome cannot be predicted with certainty in advance (e.g. tossing a coin, rolling a die).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Sample Space</h4>
<p>The sample space, denoted S, is the set of all possible outcomes of an experiment. For a single coin toss, S = {Head, Tail}.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Events</h4>
<p>An event is any subset of the sample space &mdash; a collection of one or more outcomes that are of interest. A <strong>simple event</strong> consists of exactly one outcome; a <strong>compound event</strong> consists of two or more outcomes.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Union and Intersection of Two or More Events</h4>
<ul>
<li><strong>Union (A &cup; B):</strong> The event that A occurs, or B occurs, or both occur.</li>
<li><strong>Intersection (A &cap; B):</strong> The event that both A and B occur together.</li>
<li><strong>Mutually Exclusive Events:</strong> Events that cannot occur at the same time, so A &cap; B = &empty; (the empty set).</li>
</ul>

<h3>2.2 Fundamental Rules of Counting</h3>
<p>Counting rules determine how many total outcomes exist in situations too complex to list out by hand, which is essential for calculating classical probability.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">The Multiplication Rule</h4>
<p>If one task can be done in <em>m</em> ways and a second, independent task can be done in <em>n</em> ways, the two tasks together can be done in <strong>m &times; n</strong> ways.</p>

<h3>2.3 Counting Rules for Permutations</h3>
<p>A <strong>permutation</strong> is an arrangement of objects in a specific order, where order matters.</p>
<p>The number of permutations of <em>n</em> distinct objects taken <em>r</em> at a time is:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>nPr = n! &divide; (n &minus; r)!</strong></p>
<p>where <em>n!</em> ("n factorial") = n &times; (n&minus;1) &times; (n&minus;2) &times; ... &times; 1.</p>

<h3>2.4 Counting Rules for Combinations</h3>
<p>A <strong>combination</strong> is a selection of objects where order does not matter.</p>
<p>The number of combinations of <em>n</em> distinct objects taken <em>r</em> at a time is:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>nCr = n! &divide; [r! (n &minus; r)!]</strong></p>
<p>Combinations are always smaller than or equal to permutations for the same n and r, since combinations do not count different orderings of the same selection separately.</p>
"""
terms = [
    ("Random Experiment", "A process that produces one of several possible outcomes, where the specific outcome cannot be predicted with certainty."),
    ("Sample Space (S)", "The set of all possible outcomes of an experiment."),
    ("Event", "Any subset of the sample space, representing one or more outcomes of interest."),
    ("Permutation (nPr)", "An arrangement of n objects taken r at a time where order matters, calculated as n! / (n-r)!."),
    ("Combination (nCr)", "A selection of n objects taken r at a time where order does not matter, calculated as n! / [r!(n-r)!]."),
]
examprep = [
    "Sample space S = set of all possible outcomes; Event = subset of S (simple = 1 outcome, compound = 2+ outcomes).",
    "Mutually exclusive events: A &cap; B = &empty; (cannot occur together).",
    "Multiplication rule: m ways x n ways = m x n total ways.",
    "Permutation (order matters): nPr = n! / (n-r)!",
    "Combination (order doesn't matter): nCr = n! / [r!(n-r)!]",
]
questions = [
    ("Define sample space and event, with an example.", "The sample space is the set of all possible outcomes of an experiment (e.g. S = {Head, Tail} for a coin toss). An event is any subset of the sample space of interest, such as 'getting a Head', which here is a simple event since it contains one outcome."),
    ("Differentiate between permutation and combination.", "A permutation is an arrangement of objects where order matters, calculated as nPr = n!/(n-r)!. A combination is a selection of objects where order does not matter, calculated as nCr = n!/[r!(n-r)!]. For the same n and r, the number of combinations is always smaller than or equal to the number of permutations."),
    ("Explain the multiplication rule of counting with an example.", "If one task can be completed in m ways and a second independent task in n ways, the two tasks together can be completed in m x n ways. For example, if a restaurant offers 4 starters and 3 main courses, a diner can choose a starter-and-main combination in 4 x 3 = 12 ways."),
    ("Calculate 5P2 and 5C2. Explain the difference in the results.", "5P2 = 5!/(5-2)! = 5!/3! = 5 x 4 = 20. 5C2 = 5!/[2!(5-2)!] = (5 x 4)/(2 x 1) = 10. The permutation count is higher because it counts each pair of chosen items in both possible orders, while the combination count treats each pair as a single selection regardless of order."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("This topic covers the two core theorems used to combine probabilities &mdash; addition and "
            "multiplication &mdash; followed by conditional probability and Bayes' Theorem, which lets "
            "probabilities be revised in light of new information.")
notes = """
<h3>3.1 Addition Theorem of Probability</h3>
<p>For any two events A and B:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>P(A &cup; B) = P(A) + P(B) &minus; P(A &cap; B)</strong></p>
<p>If A and B are <strong>mutually exclusive</strong> (cannot occur together), then P(A &cap; B) = 0, which simplifies the rule to:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>P(A &cup; B) = P(A) + P(B)</strong></p>

<h3>3.2 Multiplication Theorem of Probability</h3>
<p>For any two events A and B:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>P(A &cap; B) = P(A) &times; P(B | A)</strong></p>
<p>If A and B are <strong>independent</strong> (the occurrence of one does not affect the probability of the other), then P(B | A) = P(B), which simplifies the rule to:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>P(A &cap; B) = P(A) &times; P(B)</strong></p>

<h3>3.3 Conditional Probability</h3>
<p>Conditional probability is the probability that event B occurs, given that event A has already occurred, written <strong>P(B | A)</strong>:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>P(B | A) = P(A &cap; B) &divide; P(A)</strong>, provided P(A) &gt; 0</p>
<p>Conditional probability is the basis for understanding independence: A and B are independent exactly when P(B | A) = P(B), i.e. knowing A occurred does not change the probability of B.</p>

<h3>3.4 Bayes' Theorem</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Need for Bayes' Theorem</h4>
<p>In many real situations, we know the probability of an effect given a cause, but we actually want the reverse &mdash; the probability of a particular cause given that we have observed an effect. Bayes' Theorem provides a formal way to "invert" conditional probabilities to answer this kind of question.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Statement of Bayes' Theorem</h4>
<p>If B&#8321;, B&#8322;, &hellip;, B&#8345; are mutually exclusive and exhaustive events, and A is any event, then for a specific B&#7522;:</p>
<p style="text-align:center;font-size:1.05rem;"><strong>P(B&#7522; | A) = [P(B&#7522;) &times; P(A | B&#7522;)] &divide; &Sigma; [P(B&#7495;) &times; P(A | B&#7495;)]</strong></p>
<p>In words: the <strong>posterior probability</strong> of a cause B&#7522;, given that effect A was observed, is proportional to the <strong>prior probability</strong> of B&#7522; multiplied by the likelihood of observing A given B&#7522;, normalised by summing this product across all possible causes.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Applications of Bayes' Theorem</h4>
<ul>
<li>Revising the probability a product is defective, after a quality check gives a positive/negative signal.</li>
<li>Medical diagnosis &mdash; updating the probability of a disease given a test result.</li>
<li>Market research &mdash; updating the probability a customer segment will respond to a campaign, given early response data.</li>
<li>Credit risk assessment &mdash; updating the probability of default given new financial information about a borrower.</li>
</ul>
"""
terms = [
    ("Addition Theorem", "P(A &cup; B) = P(A) + P(B) - P(A &cap; B), simplifying to P(A) + P(B) for mutually exclusive events."),
    ("Multiplication Theorem", "P(A &cap; B) = P(A) x P(B|A), simplifying to P(A) x P(B) for independent events."),
    ("Conditional Probability", "The probability of event B occurring given that event A has already occurred, P(B|A) = P(A &cap; B) / P(A)."),
    ("Bayes' Theorem", "A rule for finding the posterior probability of a cause given an observed effect, based on prior probabilities and likelihoods."),
    ("Prior Probability", "The probability of an event assigned before new evidence is taken into account."),
    ("Posterior Probability", "The revised probability of an event after new evidence has been incorporated, calculated using Bayes' Theorem."),
]
examprep = [
    "Addition theorem: P(A&cup;B) = P(A) + P(B) - P(A&cap;B); mutually exclusive &rArr; P(A&cup;B) = P(A) + P(B).",
    "Multiplication theorem: P(A&cap;B) = P(A) x P(B|A); independent events &rArr; P(A&cap;B) = P(A) x P(B).",
    "Conditional probability: P(B|A) = P(A&cap;B) / P(A).",
    "Bayes' Theorem revises prior probabilities into posterior probabilities using observed evidence; used in quality control, diagnosis, market research, credit risk.",
]
questions = [
    ("State the addition theorem of probability. When does it simplify?", "P(A &cup; B) = P(A) + P(B) - P(A &cap; B). It simplifies to P(A) + P(B) when A and B are mutually exclusive, since P(A &cap; B) = 0 in that case."),
    ("State the multiplication theorem of probability. When does it simplify?", "P(A &cap; B) = P(A) x P(B|A). It simplifies to P(A) x P(B) when A and B are independent, since P(B|A) = P(B) in that case."),
    ("Define conditional probability with its formula.", "Conditional probability is the probability of event B occurring given that event A has already occurred: P(B|A) = P(A &cap; B) / P(A), provided P(A) > 0."),
    ("Why is Bayes' Theorem needed? State the theorem.", "Bayes' Theorem is needed because we often know the probability of an effect given a cause but want the reverse: the probability of a cause given an observed effect. For mutually exclusive, exhaustive events B1...Bn and event A: P(Bi|A) = [P(Bi) x P(A|Bi)] / Sum of [P(Bk) x P(A|Bk)] across all k."),
    ("State any two business applications of Bayes' Theorem.", "Bayes' Theorem is used in quality control to revise the probability a product is defective after a test result, and in credit risk assessment to update the probability of a borrower defaulting given new financial information."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("This topic bridges basic probability and probability distributions by introducing random "
            "variables &mdash; the way numerical outcomes are formally assigned to the results of a random "
            "experiment.")
notes = """
<h3>4.1 Random Variable &mdash; Concept</h3>
<p>A random variable is a variable whose value is a numerical outcome of a random experiment. It assigns a real number to every possible outcome in the sample space.</p>

<h3>4.2 Discrete Random Variables</h3>
<p>A discrete random variable can take only a countable number of distinct values (e.g. the number of defective items in a batch of 10, which can only be 0, 1, 2, &hellip;, 10).</p>

<h3>4.3 Continuous Random Variables</h3>
<p>A continuous random variable can take any value within a given range (e.g. the exact weight of a product, or the time taken to complete a task), rather than being restricted to specific countable values.</p>

<h3>4.4 Expected Value Concept</h3>
<p>The expected value of a random variable is its long-run average value across many repetitions, calculated as:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>E(X) = &Sigma; [x &times; P(x)]</strong></p>
<p>where the sum runs over every possible value x that the random variable X can take, weighted by its probability P(x). The expected value is also called the <strong>mean of the probability distribution</strong>, often denoted &mu;.</p>

<h3>4.5 Probability Mass Function (PMF)</h3>
<p>For a discrete random variable, the probability mass function gives the probability that the random variable takes each specific value: <strong>P(X = x)</strong>. Every PMF must satisfy P(x) &ge; 0 for all x, and &Sigma; P(x) = 1 across all possible values.</p>

<h3>4.6 Probability Density Function (PDF)</h3>
<p>For a continuous random variable, probability is described by a probability density function, where the probability of X falling within a given range is the area under the curve of the function over that range. Since a continuous variable has infinitely many possible values, the probability of it taking any single exact value is zero; only probabilities over an interval are meaningful.</p>

<h3>4.7 Types of Probability Distribution</h3>
<p>Probability distributions are classified as <strong>discrete</strong> (built from a PMF, e.g. Binomial and Poisson Distributions, covered in the next topic) or <strong>continuous</strong> (built from a PDF, e.g. the Normal Distribution, covered later in this unit).</p>
"""
terms = [
    ("Random Variable", "A variable whose value is a numerical outcome of a random experiment, assigning a real number to every outcome in the sample space."),
    ("Discrete Random Variable", "A random variable that can take only a countable number of distinct values."),
    ("Continuous Random Variable", "A random variable that can take any value within a given range."),
    ("Expected Value E(X)", "The long-run average value of a random variable, calculated as the sum of each value weighted by its probability."),
    ("Probability Mass Function (PMF)", "A function giving the probability that a discrete random variable takes each specific value."),
    ("Probability Density Function (PDF)", "A function describing the relative likelihood of a continuous random variable, where probability over a range equals the area under the curve."),
]
examprep = [
    "Random variable = numerical outcome of a random experiment; Discrete (countable values) vs Continuous (any value in a range).",
    "Expected value E(X) = Sum of [x * P(x)] = mean of the probability distribution (mu).",
    "PMF (discrete): P(X=x), with P(x) &ge; 0 and sum of all P(x) = 1.",
    "PDF (continuous): probability over a range = area under the curve; probability of an exact single value = 0.",
    "Discrete distributions: Binomial, Poisson; Continuous distribution: Normal.",
]
questions = [
    ("Define random variable. Differentiate between discrete and continuous random variables.", "A random variable is a variable whose value is a numerical outcome of a random experiment. A discrete random variable takes only a countable number of distinct values (e.g. number of defects), while a continuous random variable can take any value within a range (e.g. weight or time)."),
    ("What is the expected value of a random variable? Give its formula.", "The expected value is the long-run average value of a random variable across many repetitions, calculated as E(X) = Sum of [x x P(x)] across all possible values x. It is also called the mean of the probability distribution."),
    ("Differentiate between a probability mass function and a probability density function.", "A probability mass function (PMF) applies to discrete random variables and gives the probability of each specific value, P(X=x). A probability density function (PDF) applies to continuous random variables, where the probability of X falling in a range is the area under the curve over that range, and the probability of any single exact value is zero."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("Binomial and Poisson distributions are the two most widely used discrete probability "
            "distributions in management. This topic covers their definitions, assumptions, characteristics "
            "and applications.")
notes = """
<h3>5.1 Binomial Distribution</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">5.1.1 Definition and Probability Function</h4>
<p>The Binomial Distribution describes the number of "successes" in a fixed number of independent trials, each with the same probability of success. If X is the number of successes in <em>n</em> trials with probability of success <em>p</em> on each trial:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>P(X = x) = nCx &times; p<sup>x</sup> &times; q<sup>(n&minus;x)</sup></strong></p>
<p>where q = 1 &minus; p (probability of failure), and x = 0, 1, 2, &hellip;, n.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">5.1.2 Assumptions of the Binomial Distribution</h4>
<ul>
<li>There are a fixed number of trials, n.</li>
<li>Each trial has only two possible outcomes &mdash; success or failure.</li>
<li>The probability of success, p, is constant across all trials.</li>
<li>The trials are statistically independent of each other.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">5.1.3 Characteristics of the Binomial Distribution</h4>
<ul>
<li>Mean = n &times; p.</li>
<li>Variance = n &times; p &times; q.</li>
<li>The distribution is symmetric when p = 0.5, and skewed otherwise.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">5.1.4 &amp; 5.1.5 Fitting and Applications of the Binomial Distribution</h4>
<p>A binomial distribution is "fitted" to real data by estimating n and p from the context, then using the formula to generate expected frequencies for comparison with observed data. It is applied in quality control (number of defectives in a sample), market research (number of customers preferring a product in a survey), and any scenario with a fixed number of independent yes/no trials.</p>

<h3>5.2 Poisson Distribution</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">5.2.1 Definition and Probability Function</h4>
<p>The Poisson Distribution describes the number of times an event occurs in a fixed interval of time or space, when these events happen independently and at a constant average rate:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>P(X = x) = (e<sup>&minus;&lambda;</sup> &times; &lambda;<sup>x</sup>) &divide; x!</strong></p>
<p>where &lambda; (lambda) is the average number of occurrences in the interval, e &asymp; 2.71828, and x = 0, 1, 2, &hellip;</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">5.2.2 &amp; 5.2.3 Characteristics and Assumptions of the Poisson Distribution</h4>
<ul>
<li>Events occur independently of one another.</li>
<li>The average rate of occurrence, &lambda;, is constant over the interval.</li>
<li>Two events cannot occur at exactly the same instant.</li>
<li>Mean = &lambda; and Variance = &lambda; (the mean and variance are equal).</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">5.2.4 &amp; 5.2.5 Fitting and Applications of the Poisson Distribution</h4>
<p>The Poisson distribution is especially useful as an approximation to the Binomial distribution when n is large and p is small (rare events over many trials). Typical applications include the number of customer complaints per day, the number of machine breakdowns per week, the number of accidents at an intersection per month, and the number of calls arriving at a call centre per hour.</p>
"""
terms = [
    ("Binomial Distribution", "A discrete probability distribution for the number of successes in a fixed number of independent trials, each with the same success probability."),
    ("Poisson Distribution", "A discrete probability distribution for the number of times a rare, independent event occurs in a fixed interval of time or space."),
    ("Lambda (&lambda;)", "The average rate of occurrence of an event in a given interval, used as the parameter of the Poisson distribution."),
]
examprep = [
    "Binomial: P(X=x) = nCx * p^x * q^(n-x); Mean = np; Variance = npq; needs fixed n, two outcomes, constant p, independent trials.",
    "Poisson: P(X=x) = (e^-lambda * lambda^x) / x!; Mean = Variance = lambda; used for rare events over many trials (Binomial approximation when n large, p small).",
    "Binomial applications: quality control, survey preference counts; Poisson applications: complaints, breakdowns, accidents, call arrivals.",
]
questions = [
    ("State the probability function of the Binomial distribution and its assumptions.", "P(X=x) = nCx x p^x x q^(n-x), where q = 1-p. Assumptions: a fixed number of trials n, only two possible outcomes per trial, a constant probability of success p across trials, and statistically independent trials."),
    ("State the mean and variance of the Binomial distribution.", "Mean = n x p; Variance = n x p x q, where q = 1 - p."),
    ("State the probability function of the Poisson distribution. When is it used?", "P(X=x) = (e^-lambda x lambda^x) / x!, where lambda is the average rate of occurrence. It is used for the number of times a rare, independent event occurs in a fixed interval, and as an approximation to the Binomial distribution when n is large and p is small."),
    ("What is a special property of the Poisson distribution's mean and variance?", "For the Poisson distribution, the mean and variance are equal, both equal to lambda, the average rate of occurrence."),
    ("Give two practical applications each of the Binomial and Poisson distributions.", "Binomial: counting defective items in a quality-control sample, and counting customers who prefer a product in a market survey. Poisson: counting customer complaints received per day, and counting machine breakdowns per week."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("The Normal Distribution is the most important continuous probability distribution in "
            "statistics, underlying much of sampling theory and hypothesis testing covered in later units. "
            "This topic covers its definition, properties, and the Standard Normal Distribution.")
notes = """
<h3>6.1 Definition and Probability Function</h3>
<p>The Normal Distribution is a continuous probability distribution that is symmetric and bell-shaped, fully described by its mean (&mu;) and standard deviation (&sigma;). Its probability density function is:</p>
<p style="text-align:center;font-size:1.05rem;"><strong>f(x) = [1 &divide; (&sigma;&radic;(2&pi;))] &times; e<sup>&minus;(x&minus;&mu;)&sup2;/(2&sigma;&sup2;)</sup></strong></p>

<h3>6.2 Assumptions of the Normal Distribution</h3>
<ul>
<li>The underlying variable is continuous.</li>
<li>The distribution is symmetric about the mean.</li>
<li>The mean, median and mode of the distribution all coincide at the centre.</li>
</ul>

<h3>6.3 Characteristics of the Normal Distribution</h3>
<ul>
<li><strong>Bell-Shaped and Symmetric:</strong> The curve is a symmetric bell shape centred at the mean.</li>
<li><strong>Mean = Median = Mode:</strong> All three measures of central tendency are equal and located at the centre of the curve.</li>
<li><strong>Asymptotic Tails:</strong> The curve approaches, but never quite touches, the horizontal axis as it extends in either direction.</li>
<li><strong>Total Area = 1:</strong> The total area under the curve equals 1, representing all possible outcomes.</li>
<li><strong>Empirical Rule:</strong> Approximately 68% of values lie within &plusmn;1&sigma; of the mean, 95% within &plusmn;2&sigma;, and 99.7% within &plusmn;3&sigma;.</li>
</ul>

<h3>6.4 Standard Normal Distribution</h3>
<p>The Standard Normal Distribution is a special case of the Normal Distribution with mean &mu; = 0 and standard deviation &sigma; = 1. Any normal random variable X can be converted into the standard normal variable Z using the <strong>Z-score formula</strong>:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>Z = (X &minus; &mu;) &divide; &sigma;</strong></p>
<p>This conversion lets any normal distribution problem be solved using a single standard normal probability table, regardless of the original mean and standard deviation.</p>

<h3>6.5 Characteristics of the Standard Normal Curve</h3>
<ul>
<li>Centred at Z = 0, with a standard deviation of 1.</li>
<li>Symmetric about Z = 0, so P(Z &lt; 0) = P(Z &gt; 0) = 0.5.</li>
<li>The area under the entire curve equals 1, and probabilities for any range of Z can be read directly from standard normal tables.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Why the Normal Distribution Matters</h4>
<p>The Normal Distribution underlies the Central Limit Theorem, sampling distributions, confidence intervals, and most parametric hypothesis tests covered in the following units &mdash; making it the foundation on which the rest of inferential statistics in this course is built.</p>
"""
terms = [
    ("Normal Distribution", "A continuous, symmetric, bell-shaped probability distribution fully described by its mean and standard deviation."),
    ("Standard Normal Distribution", "A special case of the Normal Distribution with mean 0 and standard deviation 1."),
    ("Z-Score", "The number of standard deviations a value lies from the mean, calculated as Z = (X - mu) / sigma."),
    ("Empirical Rule", "The rule that approximately 68%, 95% and 99.7% of normally distributed values lie within 1, 2 and 3 standard deviations of the mean respectively."),
]
examprep = [
    "Normal distribution: continuous, symmetric, bell-shaped; Mean = Median = Mode; total area under curve = 1.",
    "Empirical rule: ~68% within +/-1 sigma, ~95% within +/-2 sigma, ~99.7% within +/-3 sigma.",
    "Standard Normal Distribution: mean = 0, standard deviation = 1; Z = (X - mu) / sigma converts any normal variable to standard normal.",
    "Normal distribution underlies sampling theory, confidence intervals, and parametric hypothesis tests in later units.",
]
questions = [
    ("State the characteristics of the Normal Distribution.", "It is bell-shaped and symmetric about the mean; mean, median and mode coincide; its tails are asymptotic to the horizontal axis; the total area under the curve is 1; and the Empirical Rule states about 68%, 95% and 99.7% of values fall within 1, 2 and 3 standard deviations of the mean respectively."),
    ("What is the Standard Normal Distribution? How is a normal variable converted to it?", "The Standard Normal Distribution is a Normal Distribution with mean 0 and standard deviation 1. Any normal variable X is converted to the standard normal variable Z using the Z-score formula: Z = (X - mu) / sigma."),
    ("Why is the Normal Distribution important in statistics?", "It underlies the Central Limit Theorem, sampling distributions, confidence interval estimation, and most parametric hypothesis tests, making it the foundation for the inferential statistics topics covered in later units of this course."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Six topics covering probability and probability distributions: basic concepts of probability, counting rules/sample space/events, theorems/conditional probability/Bayes' Theorem, random variables and probability distributions, Binomial and Poisson distributions, and the Normal distribution.")

print("Unit 1 (Statistics for Management) complete: all 6 topics + index written.")
