# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Statistics-for-Management\units"
BOOK_HTML = "Book: <em>Statistics for Management</em> (BA4101, Anna University MBA Sem I, Regulation 2021)"
BOOK_PLAIN = "Statistics for Management (BA4101)"

TOPICS = [
    ("topic1-correlation-meaning-types-karl-pearson.html", "Correlation: Meaning, Types and Karl Pearson's Coefficient"),
    ("topic2-coefficient-of-determination-rank-correlation.html", "Coefficient of Determination and Rank Correlation"),
    ("topic3-regression-lines-least-squares.html", "Regression: Regression Lines and the Method of Least Squares"),
    ("topic4-estimation-of-regression-line.html", "Estimation of the Regression Line"),
    ("topic5-standard-error-of-estimate.html", "Standard Error of Estimate"),
]

BLUE_THEME = dict(accent="#2f5f8f", accent_dark="#1d3c57", accent_light="#e7eef5",
                   border="#d3dfea", shadow="rgba(47,95,143,.14)")

U = common.UnitBuilder(5, "Correlation and Regression", TOPICS,
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
overview = ("This closing unit moves from testing hypotheses about single variables to studying the "
            "relationship between two variables. This opening topic covers what correlation means, its "
            "types, and the most widely used measure of it: Karl Pearson's correlation coefficient.")
notes = """
<h3>1.1 Meaning of Correlation</h3>
<p>Correlation measures the strength and direction of the linear relationship between two numerical variables &mdash; whether, and how closely, they tend to move together.</p>

<h3>1.2 Types of Correlation</h3>
<table class="compare">
<tr><th>Basis</th><th>Types</th></tr>
<tr><td>Direction</td><td><strong>Positive Correlation</strong> (both variables increase or decrease together) vs <strong>Negative Correlation</strong> (one increases as the other decreases).</td></tr>
<tr><td>Number of Variables</td><td><strong>Simple Correlation</strong> (between two variables) vs <strong>Multiple Correlation</strong> (one variable and two or more others considered jointly).</td></tr>
<tr><td>Nature of Relationship</td><td><strong>Linear Correlation</strong> (the relationship approximates a straight line) vs <strong>Non-Linear (Curvilinear) Correlation</strong> (the relationship follows a curve).</td></tr>
</table>

<h3>1.3 Karl Pearson's Coefficient of Correlation</h3>
<p>Karl Pearson's coefficient, <strong>r</strong>, is the most widely used measure of linear correlation between two variables X and Y:</p>
<p style="text-align:center;font-size:1.05rem;"><strong>r = &Sigma;(X&minus;X&#772;)(Y&minus;Y&#772;) &divide; &radic;[&Sigma;(X&minus;X&#772;)&sup2; &times; &Sigma;(Y&minus;Y&#772;)&sup2;]</strong></p>
<p>An equivalent, computationally convenient form using raw sums is:</p>
<p style="text-align:center;font-size:1.05rem;"><strong>r = [n&Sigma;XY &minus; (&Sigma;X)(&Sigma;Y)] &divide; &radic;{[n&Sigma;X&sup2; &minus; (&Sigma;X)&sup2;][n&Sigma;Y&sup2; &minus; (&Sigma;Y)&sup2;]}</strong></p>

<h3>1.4 Properties of r</h3>
<ul>
<li><strong>r</strong> always lies between &minus;1 and +1 (inclusive): <strong>&minus;1 &le; r &le; +1</strong>.</li>
<li><strong>r = +1</strong> indicates perfect positive linear correlation.</li>
<li><strong>r = &minus;1</strong> indicates perfect negative linear correlation.</li>
<li><strong>r = 0</strong> indicates no linear correlation (the variables may still be related non-linearly).</li>
<li>r is independent of the units of measurement of X and Y.</li>
</ul>

<h3>1.5 Interpreting the Strength of r</h3>
<table class="compare">
<tr><th>Value of |r|</th><th>Strength</th></tr>
<tr><td>0.00 &ndash; 0.19</td><td>Very weak</td></tr>
<tr><td>0.20 &ndash; 0.39</td><td>Weak</td></tr>
<tr><td>0.40 &ndash; 0.69</td><td>Moderate</td></tr>
<tr><td>0.70 &ndash; 0.89</td><td>Strong</td></tr>
<tr><td>0.90 &ndash; 1.00</td><td>Very strong</td></tr>
</table>

<h3>1.6 Important Caveat: Correlation Is Not Causation</h3>
<p>A high correlation between two variables does not prove that one causes the other &mdash; the relationship could be coincidental, or both variables could be driven by a third, unmeasured factor. Correlation should always be interpreted carefully, and ideally alongside domain knowledge about the variables in question.</p>
"""
terms = [
    ("Correlation", "A measure of the strength and direction of the linear relationship between two numerical variables."),
    ("Karl Pearson's Coefficient of Correlation (r)", "The most widely used measure of linear correlation, ranging from -1 to +1."),
    ("Positive Correlation", "A relationship in which both variables tend to increase or decrease together."),
    ("Negative Correlation", "A relationship in which one variable tends to increase as the other decreases."),
]
examprep = [
    "Correlation = strength and direction of linear relationship between two variables.",
    "Types: Positive/Negative (direction); Simple/Multiple (number of variables); Linear/Non-Linear (nature of relationship).",
    "Karl Pearson's r = Sum[(X-Xbar)(Y-Ybar)] / sqrt{Sum(X-Xbar)^2 * Sum(Y-Ybar)^2}; range: -1 <= r <= +1.",
    "r = +1 perfect positive; r = -1 perfect negative; r = 0 no linear correlation.",
    "Correlation does not imply causation.",
]
questions = [
    ("Define correlation. Explain its types based on direction.", "Correlation measures the strength and direction of the linear relationship between two numerical variables. Based on direction, it is Positive (both variables increase or decrease together) or Negative (one increases as the other decreases)."),
    ("State Karl Pearson's coefficient of correlation formula and its properties.", "r = Sum[(X-Xbar)(Y-Ybar)] / sqrt{Sum(X-Xbar)^2 x Sum(Y-Ybar)^2}. Its properties: r always lies between -1 and +1; r = +1 is perfect positive correlation, r = -1 is perfect negative correlation, r = 0 indicates no linear correlation; and r is independent of the units of measurement."),
    ("Why is it said that 'correlation does not imply causation'?", "A high correlation between two variables shows they tend to move together, but does not prove one causes the other &mdash; the relationship could be coincidental, or both variables could be driven by a third, unmeasured factor, so correlation must be interpreted carefully alongside domain knowledge."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("This topic covers two further correlation concepts: the coefficient of determination, which "
            "gives correlation a direct, intuitive interpretation, and rank correlation, used when data is "
            "ordinal rather than precisely numerical.")
notes = """
<h3>2.1 Coefficient of Determination</h3>
<p>The coefficient of determination, <strong>r&sup2;</strong>, is simply the square of Karl Pearson's correlation coefficient. It gives a directly meaningful interpretation: the proportion of the total variation in one variable that is "explained by," or associated with, its linear relationship with the other variable.</p>
<p style="text-align:center;font-size:1.1rem;"><strong>r&sup2; = (Karl Pearson's r)&sup2;</strong></p>
<p>For example, if r = 0.8, then r&sup2; = 0.64, meaning 64% of the variation in one variable is associated with its linear relationship to the other variable (and the remaining 36% is associated with other factors).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Why r&sup2; Is Useful</h4>
<p>Because r&sup2; is always between 0 and 1 regardless of the sign of r, it gives a simpler, more intuitive sense of the strength of a relationship than r itself, and is the measure most commonly reported alongside, or instead of, regression results in the next topics.</p>

<h3>2.2 Rank Correlation (Spearman's Coefficient)</h3>
<p>Spearman's Rank Correlation Coefficient measures the strength and direction of association between two variables when the data is <strong>ranked</strong> (ordinal) rather than measured on a precise numerical scale, or when the relationship is monotonic but not necessarily linear.</p>
<p style="text-align:center;font-size:1.1rem;"><strong>&rho; = 1 &minus; [6&Sigma;d&sup2; &divide; n(n&sup2;&minus;1)]</strong></p>
<p>where d is the difference between the ranks assigned to each pair of observations (d = Rank of X &minus; Rank of Y), and n is the number of paired observations.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Procedure</h4>
<ol>
<li>Rank the X values from 1 to n (and separately, rank the Y values from 1 to n).</li>
<li>Calculate d for each pair, and then d&sup2;.</li>
<li>Sum d&sup2; across all pairs and substitute into the formula above.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Handling Tied Ranks</h4>
<p>When two or more values are tied, each is given the <strong>average</strong> of the ranks they would otherwise occupy, consistent with the tie-handling rule used in the Mann-Whitney and Kruskal-Wallis tests in Unit 4.</p>

<h3>2.3 Properties of Spearman's &rho;</h3>
<ul>
<li>&rho; also ranges from &minus;1 to +1, with the same interpretation of direction and strength as Karl Pearson's r.</li>
<li>It requires no assumption about the underlying distribution of the data, making it a non-parametric measure of association.</li>
<li>It is especially appropriate when data is already in ranked form (e.g. rankings by two different judges).</li>
</ul>

<h3>2.4 Karl Pearson's r vs Spearman's &rho;</h3>
<table class="compare">
<tr><th>Basis</th><th>Karl Pearson's r</th><th>Spearman's &rho;</th></tr>
<tr><td>Data required</td><td>Interval/ratio numerical data</td><td>Ordinal (ranked) data, or numerical data converted to ranks</td></tr>
<tr><td>Relationship detected</td><td>Linear relationships only</td><td>Any monotonic relationship (linear or not)</td></tr>
<tr><td>Sensitivity to outliers</td><td>More sensitive</td><td>Less sensitive, since it uses ranks rather than raw values</td></tr>
</table>
"""
terms = [
    ("Coefficient of Determination (r-squared)", "The square of Karl Pearson's correlation coefficient, giving the proportion of variation in one variable associated with its linear relationship to another."),
    ("Spearman's Rank Correlation Coefficient (rho)", "A non-parametric measure of association between two variables based on the ranks of the data rather than their raw values."),
]
examprep = [
    "r-squared (coefficient of determination) = (Karl Pearson's r)^2; proportion of variation in one variable associated with the other; always between 0 and 1.",
    "Spearman's rho = 1 - [6*Sum(d^2) / n(n^2-1)], where d = difference between paired ranks.",
    "Tied ranks: use average of the ranks they'd occupy.",
    "Pearson's r: linear relationships, numerical data, sensitive to outliers; Spearman's rho: any monotonic relationship, ranked data, non-parametric, less sensitive to outliers.",
]
questions = [
    ("What is the coefficient of determination? How is it calculated and interpreted?", "The coefficient of determination, r-squared, is the square of Karl Pearson's correlation coefficient. It represents the proportion of the total variation in one variable that is associated with its linear relationship to the other variable; for example, r-squared = 0.64 means 64% of the variation is explained by the relationship."),
    ("State the formula for Spearman's Rank Correlation Coefficient and explain its terms.", "rho = 1 - [6 x Sum(d^2) / n(n^2-1)], where d is the difference between the ranks assigned to X and Y for each pair of observations, and n is the number of paired observations."),
    ("Differentiate between Karl Pearson's correlation coefficient and Spearman's rank correlation coefficient.", "Karl Pearson's r requires interval/ratio numerical data and detects only linear relationships, and is more sensitive to outliers. Spearman's rho works with ordinal/ranked data (or numerical data converted to ranks), detects any monotonic relationship, is non-parametric, and is less sensitive to outliers since it uses ranks rather than raw values."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("While correlation measures how strongly two variables are related, regression goes further, "
            "providing an equation that can be used to predict one variable from the other. This topic "
            "introduces regression lines and the method used to fit them: Least Squares.")
notes = """
<h3>3.1 Meaning of Regression</h3>
<p>Regression analysis is a statistical technique for modelling the relationship between a <strong>dependent variable</strong> (Y, the variable being predicted) and one or more <strong>independent variables</strong> (X, the variable(s) used to make the prediction), expressed as a mathematical equation.</p>

<h3>3.2 Correlation vs Regression</h3>
<table class="compare">
<tr><th>Basis</th><th>Correlation</th><th>Regression</th></tr>
<tr><td>Purpose</td><td>Measures the strength and direction of association</td><td>Models the relationship to allow prediction</td></tr>
<tr><td>Variables</td><td>Symmetric &mdash; no distinction between X and Y</td><td>Asymmetric &mdash; a clear dependent (Y) and independent (X) variable</td></tr>
<tr><td>Output</td><td>A single coefficient (r)</td><td>An equation (regression line)</td></tr>
</table>

<h3>3.3 The Simple Linear Regression Line</h3>
<p>The regression of Y on X is expressed as a straight-line equation:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>Y = a + bX</strong></p>
<p>where <strong>a</strong> is the Y-intercept (the predicted value of Y when X = 0), and <strong>b</strong> is the slope (the regression coefficient, representing the average change in Y for a one-unit increase in X).</p>

<h3>3.4 The Method of Least Squares</h3>
<p>The Method of Least Squares is used to find the specific values of a and b that make the regression line the "best fit" to the data &mdash; specifically, the line that <strong>minimises the sum of squared vertical distances</strong> between each actual observed Y-value and the Y-value predicted by the line.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Formulas for a and b</h4>
<p style="text-align:center;font-size:1.05rem;"><strong>b = [n&Sigma;XY &minus; (&Sigma;X)(&Sigma;Y)] &divide; [n&Sigma;X&sup2; &minus; (&Sigma;X)&sup2;]</strong></p>
<p style="text-align:center;font-size:1.1rem;"><strong>a = Y&#772; &minus; bX&#772;</strong></p>
<p>where X&#772; and Y&#772; are the means of X and Y respectively.</p>

<h3>3.5 Two Regression Lines</h3>
<p>In general, there are <strong>two different regression lines</strong> for a given pair of variables: the regression of Y on X (used to predict Y from X, as above) and the regression of X on Y (used to predict X from Y). These two lines are generally different from each other, and only coincide exactly when r = &plusmn;1 (perfect correlation).</p>

<h3>3.6 Relationship Between r, and the Two Regression Coefficients</h3>
<p>If b<sub>YX</sub> is the slope of Y on X, and b<sub>XY</sub> is the slope of X on Y, then:</p>
<p style="text-align:center;font-size:1.1rem;"><strong>r&sup2; = b<sub>YX</sub> &times; b<sub>XY</sub></strong></p>
<p>This relationship is a useful check: since r&sup2; must lie between 0 and 1, the product of the two regression coefficients must also lie between 0 and 1.</p>
"""
terms = [
    ("Regression Analysis", "A statistical technique modelling the relationship between a dependent variable and one or more independent variables as an equation."),
    ("Dependent Variable (Y)", "The variable being predicted or explained in a regression model."),
    ("Independent Variable (X)", "The variable used to predict or explain the dependent variable in a regression model."),
    ("Method of Least Squares", "A method for fitting a regression line by minimising the sum of squared vertical distances between observed and predicted Y-values."),
    ("Regression Coefficient (b)", "The slope of a regression line, representing the average change in the dependent variable for a one-unit increase in the independent variable."),
]
examprep = [
    "Regression: dependent variable (Y, predicted) vs independent variable (X, predictor); models relationship as an equation, unlike correlation's single coefficient.",
    "Simple linear regression: Y = a + bX (a = intercept, b = slope).",
    "Least Squares: b = [nSumXY - (SumX)(SumY)] / [nSumX^2 - (SumX)^2]; a = Ybar - b*Xbar.",
    "Two regression lines exist (Y on X, X on Y); they coincide only when r = +/-1.",
    "r^2 = bYX * bXY (product of the two regression slopes equals r-squared).",
]
questions = [
    ("Differentiate between correlation and regression.", "Correlation measures the strength and direction of association between two variables symmetrically, producing a single coefficient. Regression models the relationship as an equation with a clear dependent (Y) and independent (X) variable, allowing prediction of Y from X."),
    ("Explain the method of least squares.", "The method of least squares finds the regression line values of a (intercept) and b (slope) that minimise the sum of squared vertical distances between each actual observed Y-value and the Y-value predicted by the line, giving the 'best fit' straight line to the data."),
    ("Why are there two regression lines for a pair of variables? When do they coincide?", "There is a regression of Y on X (predicting Y from X) and a regression of X on Y (predicting X from Y), which are generally different lines. They coincide exactly only when the correlation coefficient r = +1 or r = -1, i.e. when there is perfect correlation."),
    ("State the relationship between r-squared and the two regression coefficients.", "r-squared equals the product of the two regression coefficients: r^2 = bYX x bXY, where bYX is the slope of Y on X and bXY is the slope of X on Y."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("This topic focuses on how a fitted regression line is actually used to make predictions, "
            "working through the calculation steps and the important distinction between interpolation and "
            "extrapolation.")
notes = """
<h3>4.1 From Data to a Fitted Regression Equation</h3>
<p>Once a and b have been calculated using the Method of Least Squares (covered in the previous topic), the fitted regression equation &#374; = a + bX can be used to <strong>estimate</strong> the value of Y for any given value of X. The "hat" symbol on &#374; indicates this is a predicted (estimated) value, not an observed one.</p>

<h3>4.2 Steps to Estimate the Regression Line</h3>
<ol>
<li><strong>Calculate the Means:</strong> Find X&#772; and Y&#772; for the given data.</li>
<li><strong>Calculate the Slope (b):</strong> Using the least-squares formula from the previous topic.</li>
<li><strong>Calculate the Intercept (a):</strong> Using a = Y&#772; &minus; bX&#772;.</li>
<li><strong>Write the Fitted Equation:</strong> &#374; = a + bX.</li>
<li><strong>Use the Equation for Prediction:</strong> Substitute any specific value of X into the fitted equation to obtain the predicted &#374;.</li>
</ol>

<h3>4.3 Interpreting the Slope and Intercept</h3>
<ul>
<li><strong>Slope (b):</strong> For every one-unit increase in X, Y is predicted to change by b units (increase if b is positive, decrease if b is negative).</li>
<li><strong>Intercept (a):</strong> The predicted value of Y when X = 0; this is only practically meaningful if X = 0 is a realistic, observed value within the data's range.</li>
</ul>

<h3>4.4 Interpolation vs Extrapolation</h3>
<table class="compare">
<tr><th>Term</th><th>Meaning</th><th>Reliability</th></tr>
<tr><td><strong>Interpolation</strong></td><td>Predicting Y for an X-value that falls within the range of X-values actually observed in the data.</td><td>Generally reliable, since the fitted relationship is supported by nearby observed data.</td></tr>
<tr><td><strong>Extrapolation</strong></td><td>Predicting Y for an X-value that falls outside the range of X-values actually observed.</td><td>Riskier, since there is no guarantee the same linear relationship continues to hold beyond the observed range.</td></tr>
</table>
<p>As a general rule, extrapolation should be done cautiously, if at all, and any resulting prediction should be clearly flagged as less certain than an interpolated one.</p>

<h3>4.5 Checking the Regression Fit</h3>
<p>Before relying on a fitted regression line for prediction, it is good practice to check: the correlation coefficient r (and r&sup2;) for the strength of the linear relationship, a scatter plot of the data to visually confirm linearity, and whether any outliers may be unduly influencing the fitted line.</p>
"""
terms = [
    ("Fitted Regression Equation", "The specific regression line, with calculated values of a and b, used to predict the dependent variable from the independent variable."),
    ("Interpolation", "Predicting a value for an independent-variable value that falls within the range of data actually observed."),
    ("Extrapolation", "Predicting a value for an independent-variable value that falls outside the range of data actually observed, considered less reliable than interpolation."),
]
examprep = [
    "Steps: calculate means (Xbar, Ybar) &rarr; calculate slope b &rarr; calculate intercept a = Ybar - b*Xbar &rarr; write Y-hat = a + bX &rarr; substitute X to predict Y-hat.",
    "Slope b interpretation: Y changes by b units per 1-unit increase in X; Intercept a: predicted Y when X=0 (meaningful only if X=0 is realistic).",
    "Interpolation (within observed X range) = more reliable; Extrapolation (outside observed X range) = riskier, less reliable.",
    "Check regression fit via r/r-squared, a scatter plot for linearity, and checking for influential outliers.",
]
questions = [
    ("Outline the steps used to estimate and apply a regression line.", "Calculate the means of X and Y, calculate the slope b using the least-squares formula, calculate the intercept a = Ybar - b x Xbar, write the fitted equation Y-hat = a + bX, and substitute any specific X-value into this equation to obtain the predicted Y-hat."),
    ("How should the slope and intercept of a regression line be interpreted?", "The slope b indicates that for every one-unit increase in X, Y is predicted to change by b units (increasing if b is positive, decreasing if negative). The intercept a is the predicted value of Y when X = 0, which is only practically meaningful if X = 0 falls within a realistic range of the data."),
    ("Differentiate between interpolation and extrapolation. Why does this distinction matter?", "Interpolation predicts Y for an X-value within the range of data actually observed, and is generally reliable. Extrapolation predicts Y for an X-value outside the observed range, and is riskier because there is no guarantee the same linear relationship holds beyond the data actually collected; extrapolated predictions should be treated with more caution."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("This closing topic of the course covers the Standard Error of Estimate &mdash; a measure of how "
            "accurately a regression line actually predicts the dependent variable, completing the "
            "correlation and regression toolkit.")
notes = """
<h3>5.1 Why a Measure of Accuracy Is Needed</h3>
<p>A fitted regression line gives a single predicted value, &#374;, for each X &mdash; but the actual observed Y-values will not fall exactly on this line (unless the correlation is perfect). The <strong>Standard Error of Estimate</strong> quantifies, on average, how far the actual Y-values tend to deviate from the predicted values on the regression line.</p>

<h3>5.2 Formula for the Standard Error of Estimate</h3>
<p style="text-align:center;font-size:1.1rem;"><strong>S<sub>Y&middot;X</sub> = &radic;{&Sigma;(Y &minus; &#374;)&sup2; &divide; (n &minus; 2)}</strong></p>
<p>where Y is each actual observed value, &#374; is the corresponding value predicted by the regression line, and n is the number of paired observations. The denominator uses <strong>n &minus; 2</strong> (rather than n or n&minus;1) because two parameters, a and b, were already estimated from the data to fit the line.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">A Computationally Convenient Alternative Formula</h4>
<p style="text-align:center;font-size:1.05rem;"><strong>S<sub>Y&middot;X</sub> = &radic;{[&Sigma;Y&sup2; &minus; a&Sigma;Y &minus; b&Sigma;XY] &divide; (n &minus; 2)}</strong></p>

<h3>5.3 Interpreting the Standard Error of Estimate</h3>
<ul>
<li>A <strong>smaller</strong> S<sub>Y&middot;X</sub> means the actual data points lie closer to the regression line, indicating a more accurate, more useful predictive model.</li>
<li>A <strong>larger</strong> S<sub>Y&middot;X</sub> means the actual data points are more scattered around the regression line, indicating less precise predictions.</li>
<li>S<sub>Y&middot;X</sub> is measured in the same units as the dependent variable Y, making it directly interpretable (e.g. "predictions are typically off by about &#8377;500" if Y is measured in rupees).</li>
</ul>

<h3>5.4 Relationship Between Standard Error of Estimate and Correlation</h3>
<p>The Standard Error of Estimate and the correlation coefficient r are closely related: as |r| approaches 1 (a stronger linear relationship), S<sub>Y&middot;X</sub> approaches 0 (more accurate predictions), since the data points lie closer to a well-fitted line. When r = 0 (no linear relationship), S<sub>Y&middot;X</sub> is at its largest, roughly equal to the standard deviation of Y itself, since the regression line provides no real predictive advantage over simply using Y&#772; as the prediction for every case.</p>

<h3>5.5 Using the Standard Error of Estimate to Build Prediction Intervals</h3>
<p>Similar to the confidence intervals covered in Unit 2, S<sub>Y&middot;X</sub> can be used to construct a <strong>prediction interval</strong> around a specific predicted &#374; value, giving a plausible range (rather than a single point) for where an actual Y-value is likely to fall for a given X, at a chosen confidence level.</p>

<h3>5.6 Bringing the Unit Together</h3>
<p>Correlation (Topics 1&ndash;2) measures whether and how strongly two variables are related; Regression (Topics 3&ndash;4) builds a predictive equation from that relationship; and the Standard Error of Estimate (this topic) measures how trustworthy that equation's predictions actually are &mdash; together, these form a complete toolkit for using one variable to understand and predict another.</p>
"""
terms = [
    ("Standard Error of Estimate (S(Y.X))", "A measure of how far actual observed values of Y tend to deviate from the values predicted by a regression line."),
    ("Prediction Interval", "A range of values, built using the Standard Error of Estimate, within which an actual Y-value is likely to fall for a given X at a chosen confidence level."),
]
examprep = [
    "Standard Error of Estimate: S(Y.X) = sqrt{Sum(Y - Yhat)^2 / (n-2)}; uses n-2 df since a and b are both estimated from the data.",
    "Smaller S(Y.X) = more accurate predictions (points closer to the line); larger S(Y.X) = less accurate predictions.",
    "As |r| -> 1, S(Y.X) -> 0 (better fit); as r -> 0, S(Y.X) approaches the standard deviation of Y (regression adds no predictive value).",
    "S(Y.X) used to build prediction intervals around a specific Y-hat value.",
]
questions = [
    ("Define the Standard Error of Estimate. Write its formula.", "The Standard Error of Estimate measures how far actual observed Y-values tend to deviate from the values predicted by the regression line. S(Y.X) = sqrt{Sum(Y - Yhat)^2 / (n-2)}, where Y is the observed value, Yhat is the predicted value, and n is the number of paired observations."),
    ("Why is (n-2) used in the denominator of the Standard Error of Estimate formula rather than n or (n-1)?", "Because two parameters, the intercept a and the slope b, were already estimated from the sample data to fit the regression line, two degrees of freedom are used up, leaving n-2 degrees of freedom for estimating the error."),
    ("How is the Standard Error of Estimate related to the correlation coefficient r?", "As the magnitude of r approaches 1 (a stronger linear relationship), the Standard Error of Estimate approaches 0, since the data points lie closer to a well-fitted line. When r = 0, the Standard Error of Estimate is at its largest, roughly equal to the standard deviation of Y, since the regression line adds no real predictive advantage."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Five topics covering correlation and regression: correlation meaning/types/Karl Pearson's coefficient, the coefficient of determination and rank correlation, regression lines and the method of least squares, estimation of the regression line, and the standard error of estimate.")

print("Unit 5 (Statistics for Management) complete: all 5 topics + index written.")
