# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Management-Concepts-and-Organisational-Behavior\units"
BOOK_HTML = "Book: <em>Management Concepts and Organisational Behaviour</em> (BA4102, Anna University MBA Sem I)"
BOOK_PLAIN = "Management Concepts and Organisational Behaviour (BA4102)"

TOPICS = [
    ("topic1-planning-meaning-types-process.html", "Planning: Meaning, Scope, Process and Types"),
    ("topic2-forecasting.html", "Forecasting: Meaning, Techniques and Methods"),
    ("topic3-mbo-policies-strategies.html", "Management by Objectives, Policies and Strategies"),
    ("topic4-decision-making.html", "Decision-Making: Types, Process and Approaches"),
    ("topic5-organising-delegation-centralisation.html", "Organising, Delegation and Centralisation/Decentralisation"),
    ("topic6-organisation-structure-types-control.html", "Organisation Structure, Formal/Informal Design and Control"),
]

AMBER_THEME = dict(accent="#a1591f", accent_dark="#6b3a14", accent_light="#f7ebdd",
                    border="#e8d7c3", shadow="rgba(161,89,31,.14)")

U = common.UnitBuilder(2, "Planning and Organising", TOPICS,
                        subject="Management Concepts and Organisational Behaviour",
                        subject_root=SUBJECT_ROOT,
                        book_html=BOOK_HTML, book_plain=BOOK_PLAIN, theme=AMBER_THEME)

def T(i):
    fname, title = TOPICS[i-1]
    prev_link = (TOPICS[i-2][0], TOPICS[i-2][1]) if i > 1 else None
    next_link = (TOPICS[i][0], TOPICS[i][1]) if i < len(TOPICS) else None
    return fname, title, prev_link, next_link

# ================= Topic 1 =================
fname, title, prev_link, next_link = T(1)
overview = ("Planning is the first and most fundamental function of management. This topic covers its "
            "meaning, nature and scope, the steps every planning process follows, the types of plans an "
            "organisation uses, and planning's benefits and limitations.")
notes = """
<h3>1.1 Concept and Nature of Planning</h3>
<p>Planning is the process of deciding in advance what is to be done, when it is to be done, how it is to be done, and who is to do it. It bridges where an organisation is now and where it wants to be in the future.</p>
<ul>
<li><strong>Intellectual Process:</strong> Planning requires thinking, forecasting and decision-making before action is taken.</li>
<li><strong>Goal-Oriented:</strong> Every plan is prepared to achieve specific organisational objectives.</li>
<li><strong>Pervasive:</strong> Planning is done at every level of management, though its scope and detail differ by level.</li>
<li><strong>Continuous:</strong> Plans are regularly reviewed and revised as circumstances change.</li>
<li><strong>Futuristic:</strong> Planning always looks ahead and deals with an uncertain future.</li>
<li><strong>Flexible:</strong> A good plan should be capable of adjustment as conditions change.</li>
</ul>

<h3>1.2 Scope of Planning</h3>
<p>Planning is pervasive &mdash; it is carried out at every level of the organisation (corporate, business and functional) and across every department (production, marketing, finance, personnel), though top management handles broader, long-range planning while lower levels handle narrower, short-range operational planning.</p>

<h3>1.3 Objectives/Purpose of Planning</h3>
<ul>
<li>To provide direction and a clear sense of purpose to organisational activities.</li>
<li>To reduce the risks of uncertainty by anticipating change.</li>
<li>To minimise wasteful and overlapping activities by coordinating efforts in advance.</li>
<li>To facilitate control, since actual performance can only be measured against a plan.</li>
<li>To encourage innovative thinking, since planning forces managers to consider alternative courses of action.</li>
</ul>

<h3>1.4 Steps in the Planning Process</h3>
<ol>
<li><strong>Awareness of Opportunities:</strong> Identifying the opportunities and challenges that make planning necessary.</li>
<li><strong>Setting Objectives:</strong> Deciding what is to be achieved, for the organisation as a whole and for each sub-unit.</li>
<li><strong>Developing Premises:</strong> Establishing the assumptions (about the environment, economy, competition) on which the plan will be based.</li>
<li><strong>Identifying Alternatives:</strong> Searching for and listing the alternative courses of action available.</li>
<li><strong>Evaluating Alternatives:</strong> Weighing each alternative against the objectives and premises.</li>
<li><strong>Selecting an Alternative:</strong> Choosing the course of action to actually be adopted.</li>
<li><strong>Formulating Supporting Plans:</strong> Developing derivative plans to support the main plan.</li>
<li><strong>Implementing the Plan (Numberising):</strong> Converting plans into budgets and figures to make them meaningful for execution and control.</li>
</ol>

<h3>1.5 Types of Plans</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Objectives/Goals</strong></td><td>The end results an organisation seeks to achieve.</td></tr>
<tr><td><strong>Strategies</strong></td><td>Broad programmes of action for deploying resources to achieve objectives in a competitive environment.</td></tr>
<tr><td><strong>Policies</strong></td><td>General statements that guide thinking and decision-making within an area.</td></tr>
<tr><td><strong>Procedures</strong></td><td>Chronological sequences of required actions for handling recurring activities.</td></tr>
<tr><td><strong>Rules</strong></td><td>Specific, definite requirements that leave no discretion (e.g. "No smoking").</td></tr>
<tr><td><strong>Programmes</strong></td><td>A complex set of goals, policies, procedures and resource allocations needed to carry out a given course of action.</td></tr>
<tr><td><strong>Budgets</strong></td><td>A statement of expected results expressed in numerical (usually financial) terms.</td></tr>
</table>
<p>Plans can also be classified by time horizon as <strong>Long-term</strong> (multi-year, strategic), <strong>Medium-term</strong>, and <strong>Short-term</strong> (operational, often annual) plans.</p>

<h3>1.6 Importance of Planning</h3>
<ul>
<li>Gives direction to organisational effort and reduces aimless activity.</li>
<li>Reduces the impact of uncertainty and change by anticipating future conditions.</li>
<li>Minimises waste and redundancy by coordinating activities in advance.</li>
<li>Establishes the standards used for effective control.</li>
</ul>

<h3>1.7 Limitations of Planning</h3>
<ul>
<li>Planning is based on forecasts and assumptions about the future, which can turn out to be wrong.</li>
<li>It involves time and cost, which can be substantial for large organisations.</li>
<li>Rigid plans can reduce an organisation's ability to respond quickly to sudden change.</li>
<li>Internal resistance from employees who are comfortable with existing ways of working can limit a plan's effectiveness.</li>
</ul>

<h3>1.8 Essentials of Effective Planning</h3>
<ul>
<li>Plans should be clear, simple and based on well-defined objectives.</li>
<li>Plans should be flexible enough to accommodate change.</li>
<li>Plans should be practical and based on a realistic assessment of resources and the environment.</li>
<li>Plans should involve the people who will be responsible for carrying them out.</li>
</ul>
"""
terms = [
    ("Planning", "The process of deciding in advance what is to be done, when, how and by whom, to achieve a predetermined objective."),
    ("Policy", "A general statement that guides thinking and decision-making within a particular area of the organisation."),
    ("Procedure", "A chronological sequence of required actions for handling a recurring type of activity."),
    ("Budget", "A plan expressed in numerical, usually financial, terms, stating expected results."),
]
examprep = [
    "Planning = deciding in advance what, when, how, and by whom; intellectual, goal-oriented, pervasive, continuous, futuristic, flexible.",
    "8 steps in the planning process: Awareness of Opportunities, Setting Objectives, Developing Premises, Identifying Alternatives, Evaluating Alternatives, Selecting an Alternative, Formulating Supporting Plans, Numberising (budgeting).",
    "Types of plans: Objectives, Strategies, Policies, Procedures, Rules, Programmes, Budgets &mdash; also classified by time horizon as long/medium/short-term.",
    "Limitations: based on uncertain forecasts, costly in time/money, can create rigidity, may face internal resistance.",
]
questions = [
    ("Define planning. Explain its nature.", "Planning is the process of deciding in advance what is to be done, when, how and by whom. Its nature is: an intellectual process, goal-oriented, pervasive across all levels, continuous, futuristic, and flexible enough to adjust to change."),
    ("Explain the steps involved in the planning process.", "Awareness of opportunities, setting objectives, developing planning premises, identifying alternative courses of action, evaluating those alternatives, selecting the best one, formulating supporting (derivative) plans, and finally numberising the plan through budgets."),
    ("Explain the various types of plans.", "Objectives (end results sought), Strategies (broad resource-deployment programmes), Policies (guides to decision-making), Procedures (sequences for recurring activities), Rules (specific requirements with no discretion), Programmes (a complete set of goals/policies/procedures for a course of action), and Budgets (numerical statements of expected results)."),
    ("What are the limitations of planning?", "Planning depends on forecasts and assumptions that can prove wrong; it takes significant time and cost; it can create rigidity that slows response to sudden change; and it may face internal resistance from employees comfortable with existing practices."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("Forecasting predicts future business conditions so that planning can be grounded in realistic "
            "expectations. This topic covers why forecasting matters and the qualitative and quantitative "
            "techniques used to produce a forecast.")
notes = """
<h3>2.1 Meaning and Definition of Forecasting</h3>
<p>Business forecasting is the process of analysing current and past data, trends and other relevant information to make predictions about future business conditions &mdash; such as demand, sales, costs or economic activity &mdash; so that managers can plan with more confidence.</p>

<h3>2.2 Importance of Forecasting</h3>
<ul>
<li>Reduces the uncertainty managers face when setting objectives and plans.</li>
<li>Helps anticipate changes in demand, enabling better production and inventory planning.</li>
<li>Supports budgeting and financial planning with realistic revenue and cost estimates.</li>
<li>Helps identify risks and opportunities early enough to respond to them.</li>
</ul>

<h3>2.3 Essentials of Effective Forecasting</h3>
<ul>
<li>Should be based on accurate, relevant and sufficient data.</li>
<li>Should use a method appropriate to the type of decision being supported.</li>
<li>Should be reviewed and updated periodically as new information becomes available.</li>
<li>Should be communicated clearly to the managers who will use it.</li>
</ul>

<h3>2.4 Qualitative Techniques (Opinion Polling / Judgemental Methods)</h3>
<p>Qualitative techniques rely on judgement, experience and opinion rather than historical numerical data, and are especially useful when past data is limited or unavailable.</p>
<ol>
<li><strong>Executive/Jury of Opinion Method:</strong> Senior executives pool their judgement and experience to arrive at a forecast.</li>
<li><strong>Sales Force Composite Method:</strong> Forecasts are built up from the individual estimates of salespeople who are closest to customers.</li>
<li><strong>Delphi Method:</strong> A panel of experts answers questionnaires anonymously over several rounds, converging toward a consensus forecast.</li>
<li><strong>Consumer/Market Survey Method:</strong> Customers are directly surveyed about their future purchase intentions.</li>
</ol>

<h3>2.5 Quantitative Techniques (Statistical/Analytical Methods)</h3>
<ol>
<li><strong>Time Series Analysis:</strong> Uses historical data over time to identify trends, seasonal patterns and cycles, projecting them forward.</li>
<li><strong>Trend Projection:</strong> Fits a mathematical trend line to historical data and extends it into the future.</li>
<li><strong>Regression Analysis:</strong> Studies the statistical relationship between the variable being forecast and one or more related variables.</li>
<li><strong>Moving Averages:</strong> Averages data over a recent fixed number of periods, smoothing out short-term fluctuations to reveal the underlying trend.</li>
<li><strong>Exponential Smoothing:</strong> A weighted-average forecasting technique that gives more weight to recent observations.</li>
</ol>

<h3>2.6 Choosing a Forecasting Method</h3>
<p>Qualitative methods are preferred when historical data is scarce, the situation is new, or judgement from experienced people is especially valuable (e.g. launching a new product). Quantitative methods are preferred when sufficient reliable historical data exists and the pattern is expected to continue with reasonable stability.</p>
"""
terms = [
    ("Forecasting", "The process of analysing current and past data to predict future business conditions and support planning."),
    ("Delphi Method", "A qualitative forecasting technique where a panel of experts gives anonymous opinions over several rounds, converging toward a consensus."),
    ("Time Series Analysis", "A quantitative forecasting technique that projects historical trends, seasonal patterns and cycles into the future."),
    ("Moving Average", "A forecasting technique that averages data over a recent fixed number of periods to smooth out short-term fluctuations."),
]
examprep = [
    "Forecasting = predicting future business conditions from current/past data, to support planning.",
    "Qualitative (judgemental) methods: Executive/Jury of Opinion, Sales Force Composite, Delphi Method, Consumer/Market Survey.",
    "Quantitative (statistical) methods: Time Series Analysis, Trend Projection, Regression Analysis, Moving Averages, Exponential Smoothing.",
    "Choose qualitative when data is scarce/situation is new; choose quantitative when reliable historical data exists.",
]
questions = [
    ("What is business forecasting? Why is it important?", "Business forecasting is the process of analysing current and past data to predict future business conditions such as demand or sales. It is important because it reduces uncertainty, supports better production, inventory and financial planning, and helps managers spot risks and opportunities early."),
    ("Explain the qualitative techniques of forecasting.", "The Executive/Jury of Opinion method pools senior executives' judgement; the Sales Force Composite method builds forecasts from salespeople's individual estimates; the Delphi method gathers anonymous expert opinion over several rounds to reach consensus; and the Consumer/Market Survey method directly asks customers about their future purchase intentions."),
    ("Explain the quantitative techniques of forecasting.", "Time Series Analysis projects historical trends and patterns forward; Trend Projection fits a mathematical trend line to past data; Regression Analysis studies the relationship between the forecast variable and related variables; Moving Averages smooth out short-term fluctuations; and Exponential Smoothing weights recent observations more heavily."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("This topic covers Management by Objectives (MBO), a goal-setting system developed by Peter "
            "Drucker, along with policies and strategies &mdash; two of the main types of plans introduced "
            "in Topic 1, examined here in greater depth.")
notes = """
<h3>3.1 Management by Objectives (MBO) &mdash; Introduction</h3>
<p>Management by Objectives, a concept popularised by Peter Drucker, is a management system in which managers and employees jointly define objectives, agree on what each person is responsible for, and use those objectives as the standard for measuring and rewarding performance.</p>

<h3>3.2 Process of MBO</h3>
<ol>
<li><strong>Setting Organisational Objectives:</strong> Top management defines overall objectives for the organisation.</li>
<li><strong>Cascading Objectives:</strong> Objectives are cascaded down and translated into objectives for each department and individual.</li>
<li><strong>Joint Goal Setting:</strong> Managers and subordinates jointly agree on individual objectives, ensuring they align with and support the higher-level goals.</li>
<li><strong>Action Planning:</strong> Specific action plans are developed for achieving the agreed objectives.</li>
<li><strong>Periodic Review:</strong> Progress is reviewed periodically, and corrective action is taken where needed.</li>
<li><strong>Performance Appraisal:</strong> Final performance is appraised against the originally agreed objectives.</li>
</ol>

<h3>3.3 Features of MBO</h3>
<ul>
<li>Objectives are set jointly by superior and subordinate, not imposed unilaterally.</li>
<li>Objectives are specific, measurable and time-bound wherever possible.</li>
<li>Performance is reviewed periodically against these objectives, with feedback provided.</li>
<li>It links individual goals directly to organisational goals.</li>
</ul>

<h3>3.4 Advantages of MBO</h3>
<ul>
<li>Improves clarity about what is expected of each employee.</li>
<li>Increases motivation and commitment, since employees participate in setting their own goals.</li>
<li>Improves communication between managers and subordinates.</li>
<li>Provides clear, objective criteria for performance appraisal.</li>
</ul>

<h3>3.5 Disadvantages of MBO</h3>
<ul>
<li>Can be time-consuming to administer, with extensive goal-setting and review meetings.</li>
<li>May overemphasise quantifiable, short-term objectives at the expense of qualitative, long-term goals.</li>
<li>Requires sustained top-management commitment to be effective; it tends to fail if treated as a one-off exercise.</li>
</ul>

<h3>3.6 Policies</h3>
<p>A policy is a general statement or guideline that channels thinking and decision-making toward achieving an objective, without specifying the exact action to be taken in every situation.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Policies</h4>
<ul>
<li><strong>Originated Policies:</strong> Formally established by top management as official guidance.</li>
<li><strong>Appealed Policies:</strong> Created in response to a specific situation referred upward for a decision, which then becomes precedent.</li>
<li><strong>Implied Policies:</strong> Not formally stated, but inferred from the organisation's consistent pattern of behaviour over time.</li>
<li><strong>Externally Imposed Policies:</strong> Imposed by external bodies such as government regulations, trade associations, or trade unions.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Guidelines for Effective Policy-Making</h4>
<ul>
<li>Policies should be clearly and simply worded to avoid misinterpretation.</li>
<li>Policies should be consistent with organisational objectives and with each other.</li>
<li>Policies should be flexible enough to accommodate reasonable exceptions.</li>
<li>Policies should be communicated clearly to everyone who needs to apply them.</li>
</ul>

<h3>3.7 Strategy</h3>
<p>A strategy is a broad programme for deploying resources to achieve an organisation's objectives, formulated in light of the competitive environment the organisation faces.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Levels of Strategy</h4>
<table class="compare">
<tr><th>Level</th><th>Focus</th></tr>
<tr><td><strong>Corporate-Level Strategy</strong></td><td>Which businesses/industries the organisation should compete in as a whole.</td></tr>
<tr><td><strong>Business-Level Strategy</strong></td><td>How a specific business unit should compete within its industry.</td></tr>
<tr><td><strong>Functional-Level Strategy</strong></td><td>How individual departments (marketing, finance, operations) support the business-level strategy.</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Characteristics of Strategy</h4>
<ul>
<li>Long-term in orientation and significant in its impact on the organisation.</li>
<li>Formulated at the top level but implemented across the organisation.</li>
<li>Deals with the organisation's relationship to its external competitive environment.</li>
<li>Involves a significant commitment of resources that is not easily reversed.</li>
</ul>
"""
terms = [
    ("Management by Objectives (MBO)", "A management system where managers and subordinates jointly set objectives and use them as the standard for measuring and rewarding performance."),
    ("Policy", "A general statement that guides decision-making toward an objective without specifying the exact action for every situation."),
    ("Strategy", "A broad programme for deploying resources to achieve objectives, formulated considering the competitive environment."),
    ("Corporate-Level Strategy", "The level of strategy concerned with which businesses or industries an organisation should compete in as a whole."),
]
examprep = [
    "MBO (Peter Drucker): joint goal-setting between manager and subordinate, used as the standard for appraisal.",
    "MBO process: Set organisational objectives &rarr; cascade down &rarr; joint goal setting &rarr; action planning &rarr; periodic review &rarr; performance appraisal.",
    "MBO advantages: clarity, motivation, communication, objective appraisal; disadvantages: time-consuming, over-emphasises short-term/quantifiable goals, needs sustained top-management commitment.",
    "4 types of policy: Originated, Appealed, Implied, Externally Imposed.",
    "3 levels of strategy: Corporate, Business, Functional.",
]
questions = [
    ("What is MBO? Explain its process.", "Management by Objectives is a system where managers and subordinates jointly define objectives used as the standard for measuring performance. Its process: set organisational objectives, cascade them down to departments/individuals, jointly set individual goals, develop action plans, review progress periodically, and appraise final performance against the agreed objectives."),
    ("State the advantages and disadvantages of MBO.", "Advantages: clarity of expectations, higher motivation from participation, better communication, and objective appraisal criteria. Disadvantages: time-consuming administration, overemphasis on short-term quantifiable goals, and a need for sustained top-management commitment to succeed."),
    ("What is a policy? Explain its types.", "A policy is a general statement guiding decision-making toward an objective. Types include Originated Policies (set formally by top management), Appealed Policies (arising from a referred decision that becomes precedent), Implied Policies (inferred from consistent past behaviour), and Externally Imposed Policies (required by government or other outside bodies)."),
    ("Explain the levels of strategy in an organisation.", "Corporate-level strategy decides which businesses or industries the organisation competes in; Business-level strategy decides how a specific business unit competes within its industry; Functional-level strategy decides how individual departments support the business-level strategy."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("Decision-making runs through every management function. This topic covers what a decision is, "
            "the types of decisions managers make, the rational decision-making process, and the factors "
            "that influence how decisions are actually made.")
notes = """
<h3>4.1 Concept of Decision-Making</h3>
<p>Decision-making is the process of identifying a problem or opportunity and selecting the best course of action from among the available alternatives to resolve or capture it.</p>

<h3>4.2 Types of Decisions</h3>
<table class="compare">
<tr><th>Basis</th><th>Types</th></tr>
<tr><td>Nature of the problem</td><td><strong>Programmed Decisions</strong> (routine, recurring, handled by established rules/procedures) vs <strong>Non-Programmed Decisions</strong> (novel, unstructured, requiring judgement).</td></tr>
<tr><td>Importance/Level</td><td><strong>Strategic Decisions</strong> (top management, long-term, far-reaching) vs <strong>Tactical/Operational Decisions</strong> (lower levels, short-term, routine).</td></tr>
<tr><td>Certainty of outcome</td><td><strong>Decisions under Certainty, Risk,</strong> and <strong>Uncertainty</strong>, depending on how confidently the outcomes of each alternative can be predicted.</td></tr>
<tr><td>Who decides</td><td><strong>Individual Decisions</strong> vs <strong>Group Decisions</strong>, depending on whether one manager or a group of people makes the choice.</td></tr>
</table>

<h3>4.3 Rational Approach to Decision-Making (Decision-Making Process)</h3>
<ol>
<li><strong>Identifying the Problem:</strong> Recognising that a decision is needed and clearly defining the problem.</li>
<li><strong>Analysing the Problem:</strong> Gathering relevant information and understanding the causes and scope of the problem.</li>
<li><strong>Developing Alternatives:</strong> Generating a reasonable range of possible courses of action.</li>
<li><strong>Evaluating Alternatives:</strong> Weighing each alternative's costs, benefits and risks against the decision criteria.</li>
<li><strong>Selecting the Best Alternative:</strong> Choosing the alternative that best satisfies the objectives.</li>
<li><strong>Implementing the Decision:</strong> Putting the chosen alternative into action.</li>
<li><strong>Follow-Up and Evaluation:</strong> Monitoring the results and taking corrective action if the decision does not produce the expected outcome.</li>
</ol>

<h3>4.4 Factors Affecting Decision-Making</h3>
<ul>
<li><strong>Availability of Information:</strong> Better, more complete information generally supports better decisions.</li>
<li><strong>Time Pressure:</strong> Urgent situations may force a faster, less thorough decision process.</li>
<li><strong>Organisational Policies:</strong> Existing policies can constrain which alternatives are actually available.</li>
<li><strong>Risk Tolerance of the Decision-Maker:</strong> A manager's personal attitude toward risk shapes which alternatives seem acceptable.</li>
<li><strong>Group Dynamics:</strong> Where decisions are made in groups, group pressures and politics can influence the outcome.</li>
<li><strong>Past Experience:</strong> Managers often lean on precedent and experience from similar past decisions.</li>
</ul>

<h3>4.5 Techniques of Decision-Making</h3>
<ul>
<li><strong>Marginal Analysis:</strong> Comparing the additional cost of an alternative against its additional benefit.</li>
<li><strong>Cost-Benefit Analysis:</strong> Comparing the total expected costs and benefits of each alternative.</li>
<li><strong>Decision Tree Analysis:</strong> Mapping out alternatives, possible outcomes and their probabilities in a tree diagram.</li>
<li><strong>Brainstorming:</strong> A group technique for generating a wide range of alternative ideas without immediate criticism.</li>
</ul>
"""
terms = [
    ("Decision-Making", "The process of identifying a problem or opportunity and selecting the best course of action from the available alternatives."),
    ("Programmed Decision", "A routine, recurring decision handled through established rules or procedures."),
    ("Non-Programmed Decision", "A novel, unstructured decision that requires judgement because no established procedure applies."),
    ("Decision Tree Analysis", "A decision-making technique that maps out alternatives, possible outcomes and their probabilities in a tree diagram."),
]
examprep = [
    "Decision-making = identifying a problem/opportunity and selecting the best alternative.",
    "Types of decisions: Programmed vs Non-Programmed; Strategic vs Tactical/Operational; Certainty/Risk/Uncertainty; Individual vs Group.",
    "7-step rational decision process: Identify Problem &rarr; Analyse &rarr; Develop Alternatives &rarr; Evaluate Alternatives &rarr; Select Best &rarr; Implement &rarr; Follow-Up.",
    "Factors affecting decisions: information availability, time pressure, policies, risk tolerance, group dynamics, past experience.",
]
questions = [
    ("Explain the types of decisions a manager makes.", "Programmed decisions are routine and handled by established procedures, while Non-Programmed decisions are novel and require judgement. Decisions also vary by level (Strategic vs Tactical/Operational), by certainty of outcome (Certainty, Risk, Uncertainty), and by who decides (Individual vs Group)."),
    ("Explain the rational decision-making process.", "Identifying the problem, analysing it by gathering relevant information, developing a range of alternatives, evaluating each alternative against the decision criteria, selecting the best one, implementing the decision, and finally following up to evaluate whether it produced the expected results."),
    ("What factors affect decision-making?", "Availability and quality of information, time pressure, existing organisational policies, the decision-maker's personal risk tolerance, group dynamics where decisions are made collectively, and the decision-maker's past experience with similar situations."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("Organising turns a plan into a working structure of people, authority and responsibility. This "
            "topic covers the organising process, why and how authority is delegated, and the trade-offs "
            "between centralised and decentralised decision-making.")
notes = """
<h3>5.1 Nature and Process of Organising</h3>
<p>Organising is the management function of identifying and grouping the work to be done, defining and delegating authority and responsibility, and establishing relationships so that people can work together effectively toward common objectives.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Process of Organising</h4>
<ol>
<li><strong>Identifying and Dividing Work:</strong> Breaking the total work of the organisation into manageable activities.</li>
<li><strong>Grouping Activities (Departmentation):</strong> Clustering related activities into departments or units.</li>
<li><strong>Assigning Duties:</strong> Allocating specific activities to specific individuals or positions.</li>
<li><strong>Delegating Authority:</strong> Granting the authority necessary for each person to carry out their assigned duties.</li>
<li><strong>Establishing Relationships:</strong> Defining reporting lines so that authority and responsibility are clear throughout the structure.</li>
</ol>

<h3>5.2 Importance of Organising</h3>
<ul>
<li>Facilitates administration by clarifying who is responsible for what.</li>
<li>Facilitates growth and diversification by providing a structure that can expand.</li>
<li>Ensures optimum use of resources and avoids duplication of effort.</li>
<li>Encourages efficient coordination between departments.</li>
</ul>

<h3>5.3 Delegation of Authority</h3>
<p>Delegation is the process by which a manager assigns part of their work and the authority needed to accomplish it to a subordinate, while still remaining accountable for the overall outcome.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Elements of Delegation</h4>
<ul>
<li><strong>Authority:</strong> The right to make decisions and direct the work of others, which is delegated.</li>
<li><strong>Responsibility:</strong> The obligation to perform the assigned task, which is created when a subordinate accepts a delegation.</li>
<li><strong>Accountability:</strong> The ultimate answerability for results, which can never itself be delegated away &mdash; the manager remains accountable even after delegating authority and responsibility.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Barriers to Effective Delegation</h4>
<ul>
<li>A manager's reluctance to let go of control ("I can do it better myself" attitude).</li>
<li>Lack of confidence in a subordinate's ability or willingness to accept responsibility.</li>
<li>Absence of clear controls that would let a manager safely delegate and still monitor results.</li>
<li>Fear, on the subordinate's side, of criticism for mistakes made while exercising delegated authority.</li>
</ul>

<h3>5.4 Centralisation and Decentralisation</h3>
<p><strong>Centralisation</strong> is the systematic retention of decision-making authority at the upper levels of management. <strong>Decentralisation</strong> is the systematic delegation of decision-making authority throughout the lower levels of the organisation.</p>
<table class="compare">
<tr><th>Basis</th><th>Centralisation</th><th>Decentralisation</th></tr>
<tr><td>Decision-making</td><td>Concentrated at the top</td><td>Spread across levels</td></tr>
<tr><td>Speed of local decisions</td><td>Slower (must refer upward)</td><td>Faster (decided locally)</td></tr>
<tr><td>Uniformity</td><td>Easier to maintain</td><td>Harder to maintain</td></tr>
<tr><td>Suits</td><td>Small organisations, situations needing tight control</td><td>Large, diversified organisations needing local responsiveness</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Advantages of Decentralisation</h4>
<ul>
<li>Faster decisions closer to where problems actually occur.</li>
<li>Develops decision-making skills in middle and lower managers.</li>
<li>Reduces the burden on top management, freeing it for strategic matters.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Disadvantages of Decentralisation</h4>
<ul>
<li>Can lead to a lack of uniformity in decisions across the organisation.</li>
<li>Requires capable managers at lower levels, which takes time and investment to develop.</li>
<li>Can make coordination across units more difficult.</li>
</ul>
"""
terms = [
    ("Organising", "The management function of dividing work, grouping activities, and establishing authority relationships so people can work together toward common objectives."),
    ("Delegation of Authority", "The process by which a manager assigns part of their work and the necessary authority to a subordinate, while remaining accountable for the result."),
    ("Accountability", "The ultimate answerability for results, which cannot itself be delegated away even when authority and responsibility are."),
    ("Centralisation", "The systematic retention of decision-making authority at the upper levels of management."),
    ("Decentralisation", "The systematic delegation of decision-making authority throughout the lower levels of an organisation."),
]
examprep = [
    "Organising process: Divide Work &rarr; Group Activities (Departmentation) &rarr; Assign Duties &rarr; Delegate Authority &rarr; Establish Relationships.",
    "Delegation's 3 elements: Authority (delegated), Responsibility (created), Accountability (never delegated away).",
    "Barriers to delegation: manager's reluctance, lack of confidence in subordinate, no clear controls, subordinate's fear of criticism.",
    "Centralisation = authority concentrated at top; Decentralisation = authority spread to lower levels; decentralisation gives speed/local responsiveness at the cost of uniformity.",
]
questions = [
    ("Explain the process of organising.", "Identifying and dividing the total work into activities, grouping related activities into departments, assigning specific duties to positions, delegating the authority needed to carry them out, and establishing clear reporting relationships."),
    ("What is delegation of authority? Explain its elements.", "Delegation is the process by which a manager assigns part of their work and the authority to accomplish it to a subordinate. Its elements are Authority (the right delegated), Responsibility (the obligation created in the subordinate), and Accountability (the ultimate answerability, which the manager can never fully delegate away)."),
    ("What are the barriers to effective delegation?", "A manager's reluctance to give up control, lack of confidence in a subordinate's ability, absence of clear controls to monitor delegated work, and the subordinate's fear of criticism for mistakes."),
    ("Differentiate between centralisation and decentralisation.", "Centralisation concentrates decision-making authority at the top of the organisation, giving tighter control and uniformity but slower local decisions. Decentralisation spreads authority to lower levels, giving faster, more locally responsive decisions and developing lower-level managers, at the cost of uniformity and coordination ease."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("This closing topic covers the two broad types of organisation structure &mdash; formal and "
            "informal &mdash; the major structural forms an organisation can adopt, and the final function "
            "of management, control, which closes the planning-organising-controlling loop.")
notes = """
<h3>6.1 Formal and Informal Organisation</h3>
<table class="compare">
<tr><th>Basis</th><th>Formal Organisation</th><th>Informal Organisation</th></tr>
<tr><td>Origin</td><td>Deliberately designed by management</td><td>Spontaneously formed by employees</td></tr>
<tr><td>Structure</td><td>Defined hierarchy, official rules</td><td>No official structure; based on personal relationships</td></tr>
<tr><td>Communication</td><td>Follows official channels</td><td>Follows the "grapevine," faster but less reliable</td></tr>
<tr><td>Purpose</td><td>Achieving organisational objectives</td><td>Satisfying social, psychological needs of members</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Advantages and Disadvantages</h4>
<ul>
<li><strong>Formal Organisation:</strong> Advantage &mdash; clarity of roles and accountability; Disadvantage &mdash; can be rigid and slow to adapt.</li>
<li><strong>Informal Organisation:</strong> Advantage &mdash; fast communication and strong social support; Disadvantage &mdash; can spread rumours and resist formal change if its norms conflict with management's goals.</li>
</ul>

<h3>6.2 Types of Organisation Structure</h3>
<table class="compare">
<tr><th>Structure</th><th>Description</th></tr>
<tr><td><strong>Simple Structure</strong></td><td>Flat structure with one owner-manager making most decisions directly; suits small organisations.</td></tr>
<tr><td><strong>Functional Structure</strong></td><td>Departments grouped by specialism (production, marketing, finance), each led by a functional expert reporting to a central head.</td></tr>
<tr><td><strong>Divisional Structure</strong></td><td>Self-contained divisions organised around products, markets or regions, each with its own functions.</td></tr>
<tr><td><strong>Matrix Structure</strong></td><td>Staff report to both a functional manager and a project/product manager at the same time.</td></tr>
<tr><td><strong>Team-Based Structure</strong></td><td>Built around cross-functional teams rather than fixed departments.</td></tr>
<tr><td><strong>Network/Virtual Structure</strong></td><td>A small core organisation outsources most activities to a network of external partners.</td></tr>
<tr><td><strong>Boundaryless Organisation</strong></td><td>Minimises internal and external structural barriers, relying on technology and flexible teams instead of rigid reporting lines.</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Mechanistic vs Organic Structures</h4>
<p><strong>Mechanistic structures</strong> are rigid, highly formalised and centralised, suited to stable environments where efficiency matters most (similar to a Functional structure). <strong>Organic structures</strong> are flexible, loosely defined and decentralised, suited to changing environments where adaptability matters most (similar to Matrix or Network structures).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Impact of Technology on Organisational Design</h4>
<p>Modern information technology reduces the need for layers of middle management to pass information up and down the hierarchy, enabling flatter structures, remote and virtual teams, and faster coordination across departments and even across organisations.</p>

<h3>6.3 Control &mdash; Meaning and Function</h3>
<p>Control is the management function of measuring actual performance against planned performance and taking corrective action to ensure organisational objectives are achieved. It closes the loop with planning: planning sets the standard, and control checks whether that standard is being met.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Process of Control</h4>
<ol>
<li><strong>Setting Standards:</strong> Establishing the performance standards derived from the organisation's plans.</li>
<li><strong>Measuring Actual Performance:</strong> Tracking what is actually being achieved.</li>
<li><strong>Comparing Performance with Standards:</strong> Identifying any deviation between actual and planned performance.</li>
<li><strong>Analysing Deviations:</strong> Investigating the causes of significant deviations.</li>
<li><strong>Taking Corrective Action:</strong> Adjusting operations, or occasionally the plan itself, to bring performance back on track.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Characteristics of a Good Control System</h4>
<ul>
<li>Should be simple to understand and economical to operate.</li>
<li>Should be timely, flagging deviations quickly enough for corrective action to matter.</li>
<li>Should be flexible enough to adapt to changing plans and circumstances.</li>
<li>Should point directly to where and why performance is off-track, not just that it is.</li>
</ul>
"""
terms = [
    ("Formal Organisation", "A deliberately designed structure with an official hierarchy, rules and communication channels, built to achieve organisational objectives."),
    ("Informal Organisation", "A spontaneously formed network of relationships among employees, based on personal connections rather than official structure."),
    ("Mechanistic Structure", "A rigid, highly formalised and centralised organisational structure suited to stable environments."),
    ("Organic Structure", "A flexible, loosely defined and decentralised organisational structure suited to changing environments."),
    ("Control", "The management function of measuring actual performance against planned performance and taking corrective action."),
]
examprep = [
    "Formal organisation = deliberately designed, official channels; Informal = spontaneous, grapevine communication, social needs.",
    "Structure types: Simple, Functional, Divisional, Matrix, Team-Based, Network/Virtual, Boundaryless.",
    "Mechanistic (rigid, stable environment) vs Organic (flexible, changing environment) structures.",
    "Control process: Set Standards &rarr; Measure Performance &rarr; Compare with Standards &rarr; Analyse Deviations &rarr; Take Corrective Action.",
]
questions = [
    ("Differentiate between formal and informal organisation.", "Formal organisation is deliberately designed by management with an official hierarchy and communication channels, aimed at achieving organisational objectives. Informal organisation forms spontaneously among employees based on personal relationships, communicates through the grapevine, and mainly serves members' social and psychological needs."),
    ("Explain the major types of organisation structure.", "Simple structure suits small firms with one decision-maker; Functional structure groups departments by specialism; Divisional structure creates self-contained units by product/market/region; Matrix structure has dual reporting to functional and project managers; Team-Based structure organises around cross-functional teams; Network/Virtual structure outsources most activities to partners; and Boundaryless organisations minimise structural barriers using technology."),
    ("Differentiate between mechanistic and organic organisation structures.", "Mechanistic structures are rigid, highly formalised and centralised, suited to stable environments where efficiency matters most. Organic structures are flexible, loosely defined and decentralised, suited to changing environments where adaptability matters most."),
    ("Explain the process of control in management.", "Setting performance standards derived from plans, measuring actual performance, comparing it against the standards to find deviations, analysing the causes of significant deviations, and taking corrective action to bring performance back in line with the plan."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Six topics covering planning and organising: the planning process and types of plans, forecasting, MBO/policies/strategies, decision-making, organising/delegation/centralisation, and organisation structure/control.")

print("Unit 2 (Management Concepts and OB) complete: all 6 topics + index written.")
