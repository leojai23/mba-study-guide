# -*- coding: utf-8 -*-
import build_unit1 as B

# ---------- Topic 2: Stakeholders in Business ----------
overview2 = ("Every organisation operates within a web of individuals and groups who affect, or are affected by, "
             "its activities. This topic covers who these stakeholders are, the different ways they can be classified, "
             "the roles they play in strategic decisions, and how their power and interest can be managed.")

notes2 = """
<h3>2.1 Meaning of Stakeholders</h3>
<p>A stakeholder is any individual or group that can affect, or is affected by, the achievement of an organisation's objectives (R. Edward Freeman: "a stakeholder is any group or individual who can affect or is affected by the achievement of an organisation's objectives"). B.R. Hisrich: a stakeholder is "a person or entity that is invested in the company, either financially or otherwise, and both affects and/or is affected by the outcome of the company's actions."</p>

<h3>2.2 Classification of Stakeholders</h3>
<table class="compare">
<tr><th>Internal Stakeholders</th><th>External Stakeholders</th></tr>
<tr><td>Shareholders/Owners, Board of Directors, Management, Employees</td><td>Customers, Suppliers, Creditors, Competitors, Government, Society/Community</td></tr>
</table>
<p>Internal stakeholders are inside the organisation and directly involved in decision-making; external stakeholders interact with the organisation from outside but still have a stake in its success.</p>

<h3>2.3 Roles of Stakeholders in Strategic Decision Making</h3>
<ul>
<li><strong>Voting and Decision-Making:</strong> Shareholders vote to elect the Board of Directors and vote on major proposals; Board members supervise top management on their behalf.</li>
<li><strong>Managing and Supervising Positions:</strong> Boards of Directors interact with senior management to set and monitor strategy.</li>
<li><strong>Employees:</strong> Contribute directly to executing strategy at the operational level and can also influence strategic decisions through internal channels.</li>
</ul>

<h3>2.4 Stakeholder's Power in Business</h3>
<p>Stakeholder power can be classified as <strong>Active/Passive</strong> and <strong>Support/Resistance</strong>, and rated Low/Medium/High:</p>
<table class="compare">
<tr><th>Power Level</th><th>Active</th><th>Passive</th></tr>
<tr><td>Support</td><td>Actively campaigns/advocates for the organisation</td><td>Generally favourable but not vocal</td></tr>
<tr><td>Resistance</td><td>Actively opposes and works against the organisation</td><td>Quietly unconvinced / low involvement</td></tr>
</table>
<p>High-power, high-interest stakeholders (e.g. major institutional investors) require the most active management; low-power stakeholders need only be monitored.</p>

<h3>2.5 Stakeholder Interest&ndash;Influence Grid</h3>
<p>Stakeholders can be mapped on two axes &mdash; <strong>Interest</strong> (how much they care about the outcome) and <strong>Influence</strong> (how much power they have to affect it):</p>
<ul>
<li><strong>High Interest, High Influence:</strong> Key players &mdash; manage closely, involve in decision-making.</li>
<li><strong>High Interest, Low Influence:</strong> Keep informed &mdash; they care but cannot act alone; good source of feedback.</li>
<li><strong>Low Interest, High Influence:</strong> Keep satisfied &mdash; they could become a threat if neglected, even though not currently engaged.</li>
<li><strong>Low Interest, Low Influence:</strong> Monitor with minimum effort.</li>
</ul>

<h3>2.6 Issues in Stakeholder Management</h3>
<ul>
<li><strong>Communication and Commitment:</strong> Poor or closed communication systems create major problems; open, two-way communication builds trust.</li>
<li><strong>Leadership:</strong> Strong leadership is essential to align stakeholders behind a shared direction.</li>
<li><strong>Perception and Impact:</strong> How stakeholders perceive the organisation's actions (positively or negatively) shapes their behaviour toward it.</li>
<li><strong>Influence and Interests:</strong> Different stakeholders' influence and interest levels change over time and must be re-assessed continuously.</li>
<li><strong>Aligning Values:</strong> Conflicts arise when stakeholder values/goals diverge from organisational goals; alignment reduces resistance to change.</li>
</ul>
"""

terms2 = [
    ("Stakeholder", "Any individual or group who can affect, or is affected by, the achievement of an organisation's objectives."),
    ("Internal Stakeholders", "Shareholders, Board of Directors, management, and employees &mdash; directly inside the organisation."),
    ("External Stakeholders", "Customers, suppliers, creditors, competitors, government, and society/community."),
    ("Interest&ndash;Influence Grid", "A 2x2 map used to decide how much attention and management effort each stakeholder group needs."),
]

examprep2 = [
    "Stakeholder = anyone who can affect, or is affected by, achieving the organisation's objectives (Freeman).",
    "Two broad groups: Internal (shareholders, BoD, management, employees) and External (customers, suppliers, creditors, competitors, government, society).",
    "Power can be Active/Passive x Support/Resistance; interest-influence grid sorts stakeholders into key players / keep informed / keep satisfied / monitor.",
    "Key management issues: communication &amp; commitment, leadership, perception &amp; impact, shifting influence/interest, and aligning values.",
]

questions2 = [
    ("Define 'stakeholder' and classify the different types of stakeholders.",
     "A stakeholder is any individual or group who can affect, or is affected by, the achievement of an organisation's objectives (Freeman). They are classified as Internal (shareholders, Board, management, employees) and External (customers, suppliers, creditors, competitors, government, society/community)."),
    ("Explain the stakeholder interest-influence grid and its use in strategic management.",
     "It maps stakeholders on Interest (how much they care) vs Influence (how much power they hold) to decide management priority: high-interest/high-influence = manage closely; high-interest/low-influence = keep informed; low-interest/high-influence = keep satisfied; low-interest/low-influence = monitor with minimum effort."),
    ("What are the key issues involved in managing stakeholders?",
     "Communication and commitment, leadership, stakeholders' perception of and impact on the organisation, the changing influence and interests of stakeholders over time, and aligning stakeholder values with organisational goals."),
]

B.write("topic2-stakeholders.html", B.page(
    "topic2-stakeholders.html", 2, "Stakeholders in Business", overview2, notes2, terms2, examprep2, questions2,
    prev_link=("topic1-strategy-and-strategic-management.html", "Strategy &amp; Strategic Management"),
    next_link=("topic3-intent-vision-mission.html", "Strategic Intent, Vision &amp; Mission"),
))

# ---------- Topic 3: Strategic Intent, Vision & Mission ----------
overview3 = ("Before an organisation can plan concrete strategies, it needs a clear sense of where it is headed. "
             "This topic covers Strategic Intent (the umbrella concept), and its two most important expressions: "
             "Vision (the future picture) and Mission (the current reason for existing).")

notes3 = """
<h3>3.1 Meaning of Strategic Intent</h3>
<p>Strategic Intent refers to a pre-defined future state that an organisation aspires to achieve. Prahalad &amp; Doz: strategic intent envisions a desired leadership position and establishes the criterion the organisation will use to chart its progress. It gives everyone in the organisation a target worth striving for.</p>

<h3>3.2 Hierarchy of Strategic Intent</h3>
<p>Strategic intent is expressed through a hierarchy, from most integrative (fewest in number) to most specific (greatest in number):</p>
<p style="text-align:center;font-weight:600;color:var(--accent-dark)">Vision &rarr; Mission &rarr; Purpose &rarr; Business Definition &rarr; Goals &rarr; Objectives</p>

<h3>3.3 Vision &mdash; Meaning</h3>
<p>Kotler: "Vision is a description of something in the future." It is a mental image of what an organisation wants to become, painted in vivid, aspirational language.</p>

<h3>3.4 Features of a Good Vision</h3>
<ul>
<li>Future-oriented and inspirational.</li>
<li>Requires careful thinking by top management (not a one-off statement).</li>
<li>Distinctive and specific to that organisation.</li>
<li>Gives employees a sense of purpose and responsibility.</li>
<li>Helps set a superlative (best-in-class) target market image.</li>
</ul>

<h3>3.5 Process of Envisioning</h3>
<ol>
<li>Understand the organisation (its history, capabilities, and culture).</li>
<li>Set the context for the vision requirements.</li>
<li>Create alternative future scenarios.</li>
<li>Formulate the final vision statement.</li>
<li>Narrow down the vision.</li>
<li>Conduct an audit of the vision statement against reality.</li>
</ol>

<h3>3.6 Significance &amp; Limitations of Vision</h3>
<p><strong>Significance:</strong> acts as a measure of excellence; motivates employees; overcomes the gap between current and desired position; creates a sense of urgency; guides strategic planning.</p>
<p><strong>Limitations:</strong> can be ambiguous/incomplete; may fail to motivate if not believed in; too wide-ranging to guide day-to-day work; does not itself guarantee success &mdash; execution still matters.</p>

<h3>3.7 Mission &mdash; Meaning</h3>
<p>A mission statement describes an organisation's current purpose, business, and primary reason for existing right now &mdash; as opposed to vision, which is about the future.</p>

<h3>3.8 Characteristics of a Good Mission Statement</h3>
<ul>
<li><strong>Feasible</strong> &mdash; realistically achievable.</li>
<li><strong>Precise</strong> &mdash; neither too narrow nor too broad; specific enough to be useful.</li>
<li><strong>Clear</strong> &mdash; understandable to all employees and stakeholders.</li>
</ul>

<h3>3.9 Components of a Mission Statement</h3>
<p>Products/services offered, target market, customers served, resources used, and the organisation's overall scope &mdash; typically distilled into one or two paragraphs that everyone in the company can recall and act on.</p>

<h3>3.10 Benefits of Mission Statements</h3>
<ul>
<li>Motivates employees by giving work larger meaning.</li>
<li>Promotes and guides organisational business activities.</li>
<li>Sets core values that direct decision-making.</li>
<li>Improves overall organisational performance and public image.</li>
</ul>

<h3>3.11 Vision vs Mission</h3>
<table class="compare">
<tr><th>Basis</th><th>Vision</th><th>Mission</th></tr>
<tr><td>Meaning</td><td>What the organisation wishes to achieve in future</td><td>Defines the organisation's current purpose and scope</td></tr>
<tr><td>Nature</td><td>Usually not changed/modified</td><td>Changed or modified when needed</td></tr>
<tr><td>Existence</td><td>Shows the future scenario of an organisation</td><td>Shows the present scenario of an organisation</td></tr>
<tr><td>Time</td><td>Outlines the long-term goals to achieve</td><td>Specifies the present objectives and features</td></tr>
<tr><td>Plan of Achievement</td><td>Lacks a plan of achieving the goal</td><td>Highlights the way to achieve the vision</td></tr>
</table>
"""

terms3 = [
    ("Strategic Intent", "A pre-defined future state an organisation aspires to achieve; sets the criterion for measuring progress toward leadership."),
    ("Vision", "A future-oriented, aspirational description of what an organisation wants to become."),
    ("Mission", "A statement of the organisation's current purpose, business, and reason for existing."),
    ("Hierarchy of Strategic Intent", "Vision &rarr; Mission &rarr; Purpose &rarr; Business Definition &rarr; Goals &rarr; Objectives, from most integrative to most specific."),
]

examprep3 = [
    "Strategic intent = envisioned future leadership position + the criterion to chart progress toward it (Prahalad &amp; Doz).",
    "Hierarchy: Vision (future) &rarr; Mission (present purpose) &rarr; Purpose &rarr; Business Definition &rarr; Goals &rarr; Objectives.",
    "Vision = future-oriented, inspirational, distinctive; built via a 6-step envisioning process.",
    "Mission = feasible, precise, clear; states products/services, market, customers, and scope.",
    "Key difference: Vision = future destination with no built-in plan; Mission = present purpose that shows the way to get there.",
]

questions3 = [
    ("Distinguish between Vision and Mission.",
     "Vision describes the future state the organisation wants to reach and is rarely changed; Mission describes its current purpose and scope, is revised as needed, and (unlike vision) points toward how that purpose is achieved."),
    ("What is strategic intent? Explain its hierarchy.",
     "Strategic intent is a pre-defined future state an organisation aspires to achieve, giving it a criterion to measure progress. Its hierarchy runs from the most integrative element (Vision) down to the most specific (Objectives): Vision &rarr; Mission &rarr; Purpose &rarr; Business Definition &rarr; Goals &rarr; Objectives."),
    ("Explain the process of envisioning.",
     "Six steps: understand the organisation, set the context for vision requirements, create alternative future scenarios, formulate the final vision statement, narrow it down, then audit it against reality."),
    ("What are the characteristics of a good mission statement?",
     "It should be feasible (realistically achievable), precise (neither too broad nor too narrow), and clear (understandable to employees and stakeholders)."),
]

B.write("topic3-intent-vision-mission.html", B.page(
    "topic3-intent-vision-mission.html", 3, "Strategic Intent, Vision &amp; Mission", overview3, notes3, terms3, examprep3, questions3,
    prev_link=("topic2-stakeholders.html", "Stakeholders in Business"),
    next_link=("topic4-purpose-and-business-definition.html", "Purpose &amp; Business Definition"),
))
print("Part 1 done (topics 2-3)")

# ---------- Topic 4: Purpose & Business Definition ----------
overview4 = ("Purpose explains why an organisation exists beyond making money, while Business Definition pins down "
             "exactly what business the organisation is in &mdash; which customers, which needs, and which technology. "
             "Together they narrow strategic intent from an abstract vision into a workable business concept.")

notes4 = """
<h3>4.1 Introduction to Purpose</h3>
<p>Purpose is the fundamental reason for an organisation's existence &mdash; its core ideology and the useful contribution it makes to the world, distinct from any single product/service or current strategy. Collins &amp; Porras' idea of core purpose: it should remain in existence throughout the organisation's life, guiding change while the specific strategies around it evolve.</p>

<h3>4.2 Factors Affecting Purpose</h3>
<ul>
<li><strong>Stakeholder Expectations:</strong> Different stakeholder groups (owners, employees, customers, government) have different expectations that shape and constrain purpose.</li>
<li><strong>Corporate Governance:</strong> Governance frameworks affect how purpose is set and pursued responsibly.</li>
<li><strong>Business Environment:</strong> External conditions (economic, legal, social) influence what purpose is realistic and acceptable.</li>
</ul>

<h3>4.3 Significance of Purpose</h3>
<ul>
<li>Gives grounds to move forward with a clear, motivating reason.</li>
<li>Gives strong continuity to business decisions over time.</li>
<li>Fosters collaborative working across teams united by a shared reason for being.</li>
<li>Helps in decision-making by providing a stable reference point that outlasts any one strategy.</li>
</ul>

<h3>4.4 Introduction to Business Definition</h3>
<p>Business Definition answers the practical question "what business are we in?" &mdash; described in terms of the customers served, the needs satisfied, and the technology/approach used to satisfy them, rather than just the physical product made.</p>

<h3>4.5 Abell's Three-Dimensional Business Definition Model</h3>
<p>Derek Abell proposed that a business should be defined along three dimensions:</p>
<ol>
<li><strong>Customer Groups</strong> &mdash; who is being served.</li>
<li><strong>Customer Needs/Functions</strong> &mdash; what need of the customer is being satisfied.</li>
<li><strong>Technology</strong> &mdash; how (with what technology/approach) that need is satisfied.</li>
</ol>
<p class="callout">Defining a business only by its product (e.g. "we make bicycles") is narrow; defining it by customer needs and technology (e.g. "we provide affordable personal transport for short urban trips") reveals a much wider competitive and growth landscape.</p>

<h3>4.6 Vital Aspects in Defining a Business</h3>
<ul>
<li>Who are the organisation's customers?</li>
<li>What functions/needs of the customer are being satisfied?</li>
<li>How are those needs satisfied (technology, channel, differentiation)?</li>
</ul>
"""

terms4 = [
    ("Purpose", "The fundamental, enduring reason an organisation exists, beyond any single product or strategy."),
    ("Business Definition", "A description of what business an organisation is in, framed around customers, needs, and technology rather than just the product made."),
    ("Abell's 3-D Model", "Defines a business along Customer Groups, Customer Needs/Functions, and Technology."),
]

examprep4 = [
    "Purpose = the enduring reason a company exists (Collins &amp; Porras' 'core purpose'), shaped by stakeholder expectations, governance, and the business environment.",
    "Business Definition answers 'what business are we in?' using customers + needs + technology, not just the product.",
    "Abell's 3-D model: Customer Groups (who), Customer Needs (what), Technology (how).",
    "Defining business narrowly by product risks missing growth opportunities that a needs-based definition reveals.",
]

questions4 = [
    ("What is 'purpose' in strategic management? What factors affect it?",
     "Purpose is the fundamental, enduring reason an organisation exists, beyond any one product or strategy. It is shaped by stakeholder expectations, corporate governance frameworks, and the broader business environment."),
    ("Explain Abell's three-dimensional model of business definition.",
     "Abell defines a business along three dimensions: Customer Groups (who is served), Customer Needs/Functions (what need is satisfied), and Technology (how it is satisfied) &mdash; giving a fuller definition than describing the business by its product alone."),
    ("Why is it important to define a business in terms of customer needs rather than just the product?",
     "A needs-based definition (e.g. 'affordable personal transport') reveals a wider competitive landscape and more growth opportunities than a product-based definition (e.g. 'we make bicycles'), which can blind the organisation to substitutes and adjacent markets."),
]

B.write("topic4-purpose-and-business-definition.html", B.page(
    "topic4-purpose-and-business-definition.html", 4, "Purpose &amp; Business Definition", overview4, notes4, terms4, examprep4, questions4,
    prev_link=("topic3-intent-vision-mission.html", "Strategic Intent, Vision &amp; Mission"),
    next_link=("topic5-goals-and-objectives.html", "Goals &amp; Objectives"),
))

# ---------- Topic 5: Goals & Objectives ----------
overview5 = ("Goals and Objectives translate mission and purpose into targets the organisation can actually work "
             "toward and measure. Goals are the broader aims; Objectives are their specific, quantified, time-bound versions.")

notes5 = """
<h3>5.1 Introduction to Goals</h3>
<p>Philip Kotler: "Goals are the ideal situations to which an organisation aspires." Goals are the desired end results toward which effort is directed.</p>

<h3>5.2 Features of Goals</h3>
<ul>
<li>Broad and general in nature.</li>
<li>Not usually quantified precisely.</li>
<li>Long or medium-term in orientation.</li>
<li>Provide overall direction rather than day-to-day targets.</li>
</ul>

<h3>5.3 Types of Goals</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Official Goals</strong></td><td>The formally stated, broad goals derived directly from the mission (published in reports, charters, etc.).</td></tr>
<tr><td><strong>Operative Goals</strong></td><td>The goals actually reflected in the day-to-day operating policies of the organisation &mdash; may differ from official goals in practice.</td></tr>
<tr><td><strong>Operational Goals</strong></td><td>Specific, measurable targets set by lower/middle management to guide particular activities.</td></tr>
</table>

<h3>5.4 Meaning of Objectives</h3>
<p>Robert L. Trewatha &amp; M. Gene Newport: Objectives are the ends toward which organisational and individual activities are directed. Unlike goals, objectives are specific, quantified, and verifiable.</p>

<h3>5.5 Features of Good Objectives</h3>
<ul>
<li><strong>Multiple</strong> &mdash; an organisation pursues several objectives simultaneously, not just one.</li>
<li><strong>Measurable</strong> &mdash; stated in terms that can be tracked (numbers, dates, percentages).</li>
<li><strong>Realistic</strong> &mdash; achievable given resources and environment.</li>
<li><strong>Priority-based</strong> &mdash; sequenced by importance.</li>
<li><strong>Time-bound</strong> &mdash; have a clear deadline or period.</li>
<li><strong>Connectivity</strong> &mdash; consistent with, and supportive of, one another.</li>
<li><strong>Flexible</strong> &mdash; adaptable if the environment changes.</li>
</ul>

<h3>5.6 Classification of Objectives</h3>
<table class="compare">
<tr><th>Basis</th><th>Types</th></tr>
<tr><td>Time</td><td>Long-term, Medium-term, Short-term Objectives</td></tr>
<tr><td>Priority</td><td>Primary (Strategic) Objectives, Secondary Objectives</td></tr>
<tr><td>Nature</td><td>Financial Objectives, Non-Financial Objectives</td></tr>
</table>

<h3>5.7 Process/Steps in Setting Objectives</h3>
<ol>
<li><strong>Review the formulated objectives</strong> against the mission and environment.</li>
<li><strong>Categorise the objectives</strong> (long/medium/short-term, financial/non-financial, etc.).</li>
<li><strong>Balance</strong> the objectives against available resources and stakeholder interests before finalising.</li>
</ol>
<p>Factors influencing the setting of objectives: internal factors (resources, capabilities of the organisation) and external factors (business environment, stakeholder power and interests, government policy).</p>

<h3>5.8 Goals vs Objectives</h3>
<table class="compare">
<tr><th>Basis</th><th>Goals</th><th>Objectives</th></tr>
<tr><td>Meaning</td><td>Ideal end-state the organisation aspires to</td><td>Specific, quantified targets that operationalise a goal</td></tr>
<tr><td>Nature</td><td>Abstract, general</td><td>Concrete, specific</td></tr>
<tr><td>Time-frame</td><td>Long-term, open-ended</td><td>Fixed, defined period</td></tr>
<tr><td>Specificity</td><td>Written in general terms</td><td>Written in specific, measurable terms</td></tr>
<tr><td>Measurement</td><td>Not easily/precisely measured</td><td>Directly measurable against a target figure</td></tr>
</table>
"""

terms5 = [
    ("Goal", "A broad, general, ideal end-state the organisation aspires to, usually not precisely quantified."),
    ("Objective", "A specific, measurable, time-bound target that operationalises a goal."),
    ("Official Goals", "Formally stated broad goals derived from the mission."),
    ("Operative Goals", "Goals actually reflected in day-to-day operating policy, sometimes differing from official goals."),
]

examprep5 = [
    "Goal = broad, general aspiration (Kotler); Objective = specific, quantified, verifiable version of a goal.",
    "Types of goals: Official (from the mission), Operative (reflected in actual day-to-day policy), Operational (specific lower-level targets).",
    "Good objectives are Multiple, Measurable, Realistic, Priority-based, Time-bound, Connected, and Flexible.",
    "Objectives classified by Time (long/medium/short), Priority (primary/secondary), and Nature (financial/non-financial).",
    "Setting objectives: review formulated objectives &rarr; categorise them &rarr; balance against resources and stakeholders.",
]

questions5 = [
    ("Differentiate between Goals and Objectives.",
     "Goals are broad, general, and not precisely quantified (e.g. 'become a market leader'); Objectives are specific, measurable, time-bound targets that operationalise a goal (e.g. 'increase market share by 5% within 12 months')."),
    ("Explain the features of good objectives.",
     "Good objectives are Multiple (an organisation pursues several at once), Measurable, Realistic, Priority-based, Time-bound, mutually Connected/consistent, and Flexible enough to adapt to a changing environment."),
    ("Describe the process of setting objectives in an organisation.",
     "Three steps: (1) review the objectives that have been formulated against the mission, (2) categorise them (by time-frame, priority, financial/non-financial), and (3) balance them against available resources, capabilities, and stakeholder interests before finalising."),
    ("What are the different types of goals?",
     "Official Goals (formally stated, derived from the mission), Operative Goals (actually reflected in day-to-day operating policy), and Operational Goals (specific measurable targets set by lower/middle management)."),
]

B.write("topic5-goals-and-objectives.html", B.page(
    "topic5-goals-and-objectives.html", 5, "Goals &amp; Objectives", overview5, notes5, terms5, examprep5, questions5,
    prev_link=("topic4-purpose-and-business-definition.html", "Purpose &amp; Business Definition"),
    next_link=("topic6-governance-and-csr.html", "Corporate Governance &amp; CSR"),
))

# ---------- Topic 6: Corporate Governance & CSR ----------
overview6 = ("As the final piece of Unit 1, this topic looks outward at how an organisation is directed and controlled "
             "(Corporate Governance) and at its self-imposed obligations toward society (Corporate Social Responsibility) "
             "&mdash; both increasingly central to how strategy is judged today.")

notes6 = """
<h3>6.1 Meaning &amp; Definition of Corporate Governance</h3>
<p>Corporate Governance is the system by which companies are directed and controlled. It is not only about complying with laws and regulations but also about the overall governance system followed by the Board of Directors, management, employees, and their duties towards achieving the goals and objectives of the organisation while being accountable to shareholders and other stakeholders.</p>

<h3>6.2 Nature of Corporate Governance</h3>
<ul>
<li>Ethical &mdash; based on honesty, fairness, and accountability.</li>
<li>Wide in scope &mdash; almost universally emphasised across industries and countries.</li>
<li>Systematic &mdash; involves formal rules, regulations, and structures adopted by the Board.</li>
<li>Holistic &mdash; covers relationships with shareholders and the entire community affected by the company.</li>
</ul>

<h3>6.3 Objectives &amp; Goals of Corporate Governance</h3>
<ul>
<li>Ensures shareholders' rights are protected and can be exercised meaningfully.</li>
<li>Provides a legitimate direction for major decisions taken by the organisation.</li>
<li>Legitimises the business by demonstrating fairness/transparency to all stakeholders.</li>
<li>Helps establish good coordination between the Board and management.</li>
<li>Builds trust, which increases the company's ability to attract investment.</li>
</ul>

<h3>6.4 Constituents of Corporate Governance</h3>
<ul>
<li><strong>Board of Directors (BoDs):</strong> Make most major decisions on strategies, structure, and policies; are accountable to shareholders.</li>
<li><strong>Management:</strong> Manage day-to-day activities and report to and are supervised by the Board.</li>
<li><strong>Shareholders/Investors:</strong> Provide capital and vote on major decisions; are entitled to accurate, timely disclosure of information.</li>
</ul>

<h3>6.5 Mechanisms of Corporate Governance</h3>
<table class="compare">
<tr><th>Internal Mechanisms</th><th>External Mechanisms</th></tr>
<tr>
<td>Board of Directors; Audit Committees (financial reporting oversight); Remuneration Committees (executive pay); internal compliance/whistle-blower policies.</td>
<td>Government laws and regulations; Debt covenants imposed by lenders; the external labour market (managerial reputation); the external auditor market.</td>
</tr>
</table>

<h3>6.6 Benefits of Corporate Governance</h3>
<ul>
<li>Enhances the value of corporations and shareholder confidence.</li>
<li>Provides a competitive advantage by building investor and market trust.</li>
<li>Prevents malpractices and fraud through checks and oversight.</li>
<li>Improves overall organisational performance and efficient use of resources.</li>
<li>Facilitates access to global capital markets on better terms.</li>
<li>Protects the interests of minority and institutional shareholders alike.</li>
</ul>

<h3>6.7 Limitations/Issues in Corporate Governance</h3>
<ul>
<li>Ambiguity over the precise roles of the Board versus the CEO.</li>
<li>Whether the Chairperson and CEO positions should be separated.</li>
<li>Composition of the Board &mdash; the right balance of independent directors and expertise.</li>
<li>Related-party transactions and executive remuneration that may not align with shareholder interests.</li>
<li>Whether institutional investors are sufficiently active in holding management accountable.</li>
</ul>

<h3>6.8 Meaning, Nature &amp; Objectives of CSR</h3>
<p>Corporate Social Responsibility (CSR) is a self-imposed responsibility that goes beyond legal obligation &mdash; companies voluntarily integrate social and environmental concerns into their operations and stakeholder relations. It is multi-faceted, involving economic, legal, ethical, and discretionary responsibilities. Objectives include enhancing corporate reputation, avoiding stricter government regulation, securing goodwill/resources from the community, and improving relationships with all stakeholders.</p>

<h3>6.9 Responsibility Towards Different Stakeholders</h3>
<table class="compare">
<tr><th>Stakeholder</th><th>Responsibility</th></tr>
<tr><td>Owners/Shareholders</td><td>Fair returns, transparent and accurate financial information.</td></tr>
<tr><td>Employees</td><td>Fair wages, safe working conditions, welfare and growth opportunities.</td></tr>
<tr><td>Customers</td><td>Quality goods/services at fair prices; honest advertising.</td></tr>
<tr><td>Suppliers</td><td>Fair terms, timely payment, ethical dealing.</td></tr>
<tr><td>Creditors</td><td>Timely repayment and honest financial disclosure.</td></tr>
<tr><td>Government</td><td>Compliance with laws, timely and honest tax payment.</td></tr>
<tr><td>Society/Community</td><td>Environmental protection, community welfare and development.</td></tr>
</table>

<h3>6.10 Types of CSR</h3>
<ul>
<li><strong>Human Rights-Related CSR:</strong> Fair labour practices, no exploitation, safe working conditions.</li>
<li><strong>Environmental CSR:</strong> Reducing pollution, restoring the environment, sustainable resource use.</li>
<li><strong>Financial CSR:</strong> Accurate reporting, avoiding fraud and manipulation, protecting investor trust.</li>
<li><strong>Political CSR:</strong> Ethical conduct in lobbying, avoiding undue influence over public policy.</li>
</ul>

<h3>6.11 Arguments For and Against CSR</h3>
<table class="compare">
<tr><th>Arguments For CSR</th><th>Arguments Against CSR</th></tr>
<tr>
<td>
Builds public goodwill and brand reputation;<br>
Avoids/minimises stricter government regulation;<br>
Improves the business environment overall;<br>
Attracts and retains talented employees;<br>
Is simply the socially responsible/moral thing to do;<br>
Creates enhanced long-term business viability.
</td>
<td>
Dilutes the profit-maximisation objective of the firm;<br>
Increases costs and can reduce price competitiveness;<br>
Managers may lack the social skills to handle CSR well;<br>
Spreads resources over too many social objectives;<br>
Raises concerns about who CSR spending is really accountable to.
</td>
</tr>
</table>
"""

terms6 = [
    ("Corporate Governance", "The system by which companies are directed and controlled, covering the roles and accountability of the Board, management, and shareholders."),
    ("Board of Directors (BoD)", "The body that makes most major strategic decisions and is accountable to shareholders."),
    ("CSR (Corporate Social Responsibility)", "A company's self-imposed responsibility to integrate social and environmental concerns into its operations, beyond legal obligation."),
    ("Internal Governance Mechanisms", "Board of Directors, audit committees, and remuneration committees."),
    ("External Governance Mechanisms", "Government regulation, debt covenants, and external labour/auditor markets."),
]

examprep6 = [
    "Corporate Governance = system by which companies are directed and controlled; constituents are the Board, Management, and Shareholders.",
    "Governance mechanisms: Internal (Board, Audit &amp; Remuneration Committees) vs External (govt regulation, debt covenants, external auditor/labour markets).",
    "Benefits: shareholder value, competitive advantage, fraud prevention, better access to capital markets.",
    "CSR = voluntary responsibility beyond legal obligation, owed to owners, employees, customers, suppliers, creditors, government, and society.",
    "Types of CSR: Human Rights-related, Environmental, Financial, Political.",
    "For CSR: goodwill, avoids regulation, better business environment. Against CSR: dilutes profit motive, raises costs, accountability concerns.",
]

questions6 = [
    ("Define Corporate Governance and explain its constituents.",
     "Corporate Governance is the system by which companies are directed and controlled. Its main constituents are the Board of Directors (who make major decisions and are accountable to shareholders), Management (who run day-to-day operations under Board oversight), and Shareholders/Investors (who provide capital and vote on key decisions)."),
    ("Distinguish between internal and external mechanisms of corporate governance.",
     "Internal mechanisms include the Board of Directors, Audit Committees, and Remuneration Committees, all operating within the company. External mechanisms include government laws and regulations, debt covenants imposed by lenders, and the external labour and auditor markets."),
    ("What is CSR? Explain its different types.",
     "CSR is a company's self-imposed responsibility, beyond legal obligation, to integrate social and environmental concerns into its business. Its types include Human Rights-related CSR (fair labour practices), Environmental CSR (pollution control, sustainability), Financial CSR (honest reporting), and Political CSR (ethical lobbying)."),
    ("Discuss the arguments for and against CSR.",
     "Arguments for CSR include building goodwill, avoiding stricter regulation, improving the business environment, and being the ethically right thing to do. Arguments against CSR include diluting the profit-maximisation objective, raising costs, spreading resources too thin, and raising questions about managerial accountability for social spending."),
]

B.write("topic6-governance-and-csr.html", B.page(
    "topic6-governance-and-csr.html", 6, "Corporate Governance &amp; CSR", overview6, notes6, terms6, examprep6, questions6,
    prev_link=("topic5-goals-and-objectives.html", "Goals &amp; Objectives"),
    next_link=None,
))

print("All Unit 1 topic pages written.")
