# -*- coding: utf-8 -*-
import common

TOPICS = [
    ("topic1-business-environment.html", "Business Environment &amp; External Analysis"),
    ("topic2-industry-analysis.html", "Industry Analysis &amp; Porter's Five Forces"),
    ("topic3-competitor-analysis.html", "Competitor Analysis"),
    ("topic4-diamond-model-strategic-groups.html", "Porter's Diamond Model &amp; Strategic Groups"),
    ("topic5-internal-appraisal.html", "Internal Appraisal Techniques"),
    ("topic6-resources-and-capabilities.html", "Resources &amp; Capabilities"),
    ("topic7-core-competence-vrio.html", "Core Competence &amp; VRIO Framework"),
    ("topic8-competitive-advantage.html", "Competitive Advantage &amp; Generic Strategies"),
]

U = common.UnitBuilder(2, "Environmental Analysis &amp; Competitive Advantage", TOPICS)

def T(i):
    fname, title = TOPICS[i-1]
    prev_link = (TOPICS[i-2][0], TOPICS[i-2][1]) if i > 1 else None
    next_link = (TOPICS[i][0], TOPICS[i][1]) if i < len(TOPICS) else None
    return fname, title, prev_link, next_link

# ================= Topic 1 =================
fname, title, prev_link, next_link = T(1)
overview = ("This topic opens Unit 2 by defining the business environment that surrounds every organisation, "
            "and the systematic process (environmental appraisal) used to scan it for opportunities and threats.")
notes = """
<h3>1.1 Meaning &amp; Definition of Business Environment</h3>
<p>W.F. Glueck &amp; Lawrence R. Jauch: "Business environment includes the factors outside the firm that can lead to opportunities for or threats to the firm. Although there are many factors, the most important of the sectors are socio-economic, technological, supplier, competitor and government."</p>
<p>Keith Davis: "Business environment is the aggregate of all conditions, events, and influences that surround and affect it."</p>

<h3>1.2 Nature of Business Environment</h3>
<ul>
<li><strong>Inseparable from business:</strong> No business can function without its environment.</li>
<li><strong>Dynamic:</strong> Constantly changing due to technological, political, social, and economic factors.</li>
<li><strong>Uncertain:</strong> Future changes are difficult to predict precisely.</li>
<li><strong>Complex:</strong> Made up of many interrelated internal and external factors.</li>
<li><strong>Relative:</strong> Varies across regions/countries and over time.</li>
</ul>

<h3>1.3 Internal vs External Environment</h3>
<table class="compare">
<tr><th>Internal Environment</th><th>External Environment</th></tr>
<tr><td>Factors within the organisation's control (financial resources, HR, mission/vision, management structure)</td><td>Factors outside the organisation's control (Micro: suppliers, customers, competitors, public; Macro: economic, political, legal, social, technological, demographic, international)</td></tr>
</table>

<h3>1.4 Components of the External Business Environment</h3>
<p><strong>Micro-environment</strong> (immediate operating environment): Suppliers, Customers, Market Intermediaries, Competitors, Public.</p>
<p><strong>Macro-environment</strong> (broad forces): Economic, Political-Legal, Social, Technological, Demographic, International/Global Business Environment.</p>

<h3>1.5 Procedure of External Analysis (Abell's Steps)</h3>
<ol>
<li>Understand the nature of the external environment (its dynamism and complexity).</li>
<li>Identify the critical external factors relevant to the business.</li>
<li>Identify the past and future changes taking place in the environment.</li>
<li>Study the opportunities and threats that arise from the environment.</li>
<li>Analyse the industry and competitors.</li>
<li>Study the strategic position of the organisation in relation to its environment.</li>
</ol>

<h3>1.6 Significance of Environmental Appraisal</h3>
<ul>
<li>Helps identify opportunities and provides early warning signals of threats.</li>
<li>Helps tap useful resources from the environment.</li>
<li>Helps the organisation adapt to and cope with rapid environmental changes.</li>
<li>Provides a base for continuous learning and improvement.</li>
<li>Helps forecast productivity and effectiveness of strategies.</li>
</ul>
"""
terms = [
    ("Business Environment", "The aggregate of all external factors and conditions that surround and affect a business."),
    ("Micro-environment", "Immediate factors close to the business: suppliers, customers, intermediaries, competitors, and the public."),
    ("Macro-environment", "Broad societal forces: economic, political-legal, social, technological, demographic, and international factors."),
    ("Environmental Appraisal", "The systematic process of scanning and analysing the environment to identify opportunities and threats."),
]
examprep = [
    "Business environment = all external factors/conditions surrounding and affecting a business (Keith Davis).",
    "Nature: inseparable from business, dynamic, uncertain, complex, and relative to place/time.",
    "Micro-environment (suppliers, customers, intermediaries, competitors, public) vs Macro-environment (economic, political-legal, social, technological, demographic, international).",
    "External analysis procedure: understand environment &rarr; identify critical factors &rarr; track changes &rarr; study opportunities/threats &rarr; analyse industry/competitors &rarr; assess strategic position.",
]
questions = [
    ("Define business environment and explain its nature.", "Business environment is the aggregate of all external conditions and factors that surround and affect a business (Keith Davis). Its nature is inseparable from the business, dynamic, uncertain, complex, and relative to time and place."),
    ("Distinguish between micro and macro components of the business environment.", "Micro-environment consists of factors in the immediate operating environment &mdash; suppliers, customers, market intermediaries, competitors, and the public. Macro-environment consists of broader forces &mdash; economic, political-legal, social, technological, demographic, and international factors."),
    ("Explain the procedure followed in external environmental analysis.", "It involves understanding the nature of the environment, identifying critical external factors, tracking past and future changes, studying opportunities and threats, analysing the industry and competitors, and assessing the organisation's strategic position relative to its environment."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("Industry analysis zooms in from the broad environment to the specific industry an organisation "
            "competes in, using tools like the industry life cycle and Porter's Five Forces Model to judge "
            "how attractive and competitive that industry really is.")
notes = """
<h3>2.1 Levels of External Environment</h3>
<p>External analysis can be conducted at three levels: <strong>Macro Environment</strong> (broad, economy-wide factors), <strong>Industry Environment</strong> (the specific industry's structure and competitive forces), and <strong>Competitive Environment</strong> (direct rivals and their strategies).</p>

<h3>2.2 Industry Evolution &amp; the Industry Life Cycle</h3>
<p>Industries evolve through five stages, each with distinct competitive characteristics:</p>
<table class="compare">
<tr><th>Stage</th><th>Characteristics</th></tr>
<tr><td>1. Emerging (Embryonic)</td><td>New technology, low buyer awareness, uncertain market, high innovation.</td></tr>
<tr><td>2. Growth</td><td>Rapid demand increase, first-time buyers dominate, brand loyalty starts forming.</td></tr>
<tr><td>3. Shakeout</td><td>Growth slows, demand approaches saturation, weaker competitors are squeezed out.</td></tr>
<tr><td>4. Maturity</td><td>Market saturated, growth slow/flat, competition based on price and differentiation.</td></tr>
<tr><td>5. Decline</td><td>Demand falls due to substitution/obsolescence; firms exit or consolidate.</td></tr>
</table>

<h3>2.3 Industry Structure &amp; Attractiveness</h3>
<p>Industry attractiveness is judged using factors like market size and growth rate, degree of technological change, product differentiation, scale economies, and bargaining power along the value chain. Industry practices (pricing, promotion, distribution norms) and performance (profitability, growth) are also studied.</p>

<h3>2.4 Porter's Five Forces Model</h3>
<p>Michael Porter's model identifies five forces that determine the overall competitive intensity and attractiveness of an industry:</p>
<ol>
<li><strong>Threat of New Entrants:</strong> Governed by barriers to entry &mdash; economies of scale, capital requirements, brand identity, switching costs, access to distribution, expected retaliation.</li>
<li><strong>Bargaining Power of Suppliers:</strong> High when suppliers are concentrated, switching costs are high, the input is critical, or suppliers can threaten forward integration.</li>
<li><strong>Bargaining Power of Buyers:</strong> High when buyers are concentrated/large-volume, products are undifferentiated, switching costs are low, or buyers can threaten backward integration.</li>
<li><strong>Threat of Substitute Products:</strong> High when substitutes offer better price-performance trade-offs and buyer switching costs to the substitute are low.</li>
<li><strong>Rivalry Among Existing Competitors:</strong> Intensified by numerous/equally-balanced competitors, slow industry growth, high fixed costs, low differentiation, and high exit barriers.</li>
</ol>

<h3>2.5 Utility of Porter's Five Forces Model</h3>
<ul>
<li>Helps a firm decide which industries/segments to compete in.</li>
<li>Helps formulate strategy by revealing where competitive pressure is strongest.</li>
<li>Helps forecast future profitability of an industry.</li>
</ul>

<h3>2.6 Limitations of Porter's Five Forces Model</h3>
<ul>
<li>Assumes a relatively static industry structure; less useful in fast-changing/disruptive industries.</li>
<li>Does not fully account for complementors (firms whose products increase the value of your own).</li>
<li>Treats the industry as the unit of analysis, which can obscure differences between individual firms within it.</li>
</ul>

<h3>2.7 Factors Affecting Industry Analysis</h3>
<p>Industry trends, industry practices, industry performance, industry attractiveness, and the basic features/conditions of the industry together shape how attractive and how competitive an industry analysis will reveal it to be.</p>
"""
terms = [
    ("Industry Life Cycle", "The five stages an industry passes through: Emerging, Growth, Shakeout, Maturity, Decline."),
    ("Porter's Five Forces", "A framework analysing the intensity of competition via threat of new entrants, bargaining power of suppliers, bargaining power of buyers, threat of substitutes, and rivalry among existing firms."),
    ("Entry Barriers", "Factors (economies of scale, capital needs, brand identity, switching costs) that make it hard for new firms to enter an industry."),
    ("Industry Attractiveness", "A judgement of how profitable and competitive an industry is likely to be, based on its structure and the five forces."),
]
examprep = [
    "Industry Life Cycle: Emerging &rarr; Growth &rarr; Shakeout &rarr; Maturity &rarr; Decline.",
    "Porter's Five Forces: New Entrants, Supplier Power, Buyer Power, Substitutes, Rivalry &mdash; together determine industry attractiveness.",
    "High entry barriers + low buyer/supplier power + few substitutes + low rivalry = an attractive, more profitable industry.",
    "Limitation: Five Forces assumes a fairly static industry and can miss the role of complementors and fast disruption.",
]
questions = [
    ("Explain the five stages of the industry life cycle.", "Emerging (new technology, uncertain market), Growth (rapid demand increase, brand loyalty forms), Shakeout (growth slows, weak firms exit), Maturity (saturated demand, price-based competition), and Decline (falling demand due to substitution/obsolescence)."),
    ("Describe Porter's Five Forces Model and its utility to managers.", "It analyses Threat of New Entrants, Bargaining Power of Suppliers, Bargaining Power of Buyers, Threat of Substitutes, and Rivalry Among Existing Competitors. It helps managers decide which industries to compete in, formulate strategy around the strongest competitive pressures, and forecast future industry profitability."),
    ("What are the limitations of Porter's Five Forces Model?", "It assumes a relatively static industry structure, underplays the role of complementors, and treats the industry (rather than the individual firm) as the unit of analysis, which can obscure important differences between competitors."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("A firm cannot plan its own strategy without understanding its rivals. This topic covers where "
            "competitor information comes from and the systematic framework used to analyse a competitor's "
            "likely moves.")
notes = """
<h3>3.1 Introduction to Competitor Analysis</h3>
<p>Competitor analysis is the process of identifying key competitors, assessing their objectives, strategies, strengths and weaknesses, and predicting their responses &mdash; so the firm can formulate and adjust its own strategy accordingly.</p>

<h3>3.2 Sources of Information for Competitor Analysis</h3>
<table class="compare">
<tr><th>Recorded Data</th><th>Observable Data</th><th>Opportunistic Data</th></tr>
<tr><td>Published annual reports, government filings, press releases, patent filings</td><td>Products, pricing, advertising, hiring patterns, trade show presence</td><td>Information gathered informally through customers, suppliers, trade contacts, and industry conversations</td></tr>
</table>

<h3>3.3 Competitor Analysis Framework (Four Components)</h3>
<ol>
<li><strong>Competitor's Objectives:</strong> What financial and strategic goals is the competitor pursuing (growth, market share, profitability)?</li>
<li><strong>Competitor's Assumptions:</strong> What does the competitor believe about itself and the industry &mdash; including any blind spots or biases?</li>
<li><strong>Competitor's Strategy:</strong> What is the competitor actually doing to compete &mdash; pricing, product, promotion, distribution?</li>
<li><strong>Competitor's Resources &amp; Capabilities:</strong> What strengths and weaknesses does the competitor have in finance, marketing, operations, R&amp;D, and management?</li>
</ol>
<p>Together, these four elements build a "Competitor Response Profile" &mdash; a prediction of how the competitor is likely to react to industry changes or to the firm's own strategic moves.</p>

<h3>3.4 Factors Affecting Competition Analysis</h3>
<ul>
<li>Competitor's objectives and assumptions.</li>
<li>Competitor's current strategy and capabilities.</li>
<li>How dynamic and unpredictable the competitive environment is.</li>
</ul>

<h3>3.5 Steps in Competition Analysis</h3>
<ol>
<li>Define the competitors to be analysed.</li>
<li>Analyse competitors' strengths and weaknesses.</li>
<li>Study the market and its wants relative to competitors.</li>
<li>Build strategic plans to improve the firm's own competitive position.</li>
</ol>

<h3>3.6 Importance of Competition Analysis</h3>
<p>It helps a firm identify the strategic gaps and opportunities left open by competitors, build a strong marketplace position, and design offensive or defensive strategies with a clear, systematic knowledge of rivals rather than guesswork.</p>
"""
terms = [
    ("Competitor Analysis", "The systematic process of identifying competitors and assessing their objectives, assumptions, strategies, and capabilities."),
    ("Competitor Response Profile", "A prediction of how a competitor is likely to react, built from its objectives, assumptions, strategy, and resources/capabilities."),
    ("Recorded Data", "Formally published competitor information such as annual reports and regulatory filings."),
    ("Observable Data", "Competitor information gathered by directly observing their products, pricing, and market activity."),
]
examprep = [
    "Competitor analysis = identify rivals + assess their objectives, assumptions, strategy, resources/capabilities.",
    "Information sources: Recorded (annual reports, filings), Observable (products, pricing, ads), Opportunistic (informal trade contacts).",
    "Four-part framework builds a 'Competitor Response Profile' to predict how a rival will react.",
    "Steps: define competitors &rarr; analyse strengths/weaknesses &rarr; study the market &rarr; build a plan to improve competitive position.",
]
questions = [
    ("Explain the framework used for analysing a competitor.", "It examines four elements: the competitor's Objectives (financial/strategic goals), Assumptions (beliefs about itself and the industry), Strategy (current competitive actions), and Resources/Capabilities (strengths and weaknesses) &mdash; together forming a Competitor Response Profile."),
    ("What are the sources of information used in competitor analysis?", "Recorded data (annual reports, government filings, patents), Observable data (products, pricing, advertising, hiring), and Opportunistic data (informal information from customers, suppliers, and trade contacts)."),
    ("Describe the steps involved in competition analysis.", "Define which competitors to analyse, assess their strengths and weaknesses, study the market and customer wants relative to competitors, then build strategic plans to strengthen the firm's own competitive position."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("This topic looks at competitiveness beyond the single firm: Porter's Diamond Model explains why "
            "some nations become globally competitive in particular industries, while Strategic Group analysis "
            "explains why firms within the same industry can still face very different competitive pressures.")
notes = """
<h3>4.1 Porter's Diamond Model &mdash; Introduction</h3>
<p>Michael Porter researched why some nations become internationally competitive in specific industries (e.g. Japan in electronics, Switzerland in watches) while others do not. His National Competitive Advantage model identifies four interlinked determinants, shaped further by Government and Chance.</p>

<h3>4.2 Components of Porter's Diamond Model</h3>
<ol>
<li><strong>Factor Conditions:</strong> A nation's position in factors of production &mdash; skilled labour, infrastructure, capital &mdash; needed to compete in an industry.</li>
<li><strong>Demand Conditions:</strong> The nature and sophistication of home-market demand for the industry's product/service.</li>
<li><strong>Related &amp; Supporting Industries:</strong> The presence (or absence) of internationally competitive supplier and related industries.</li>
<li><strong>Firm Strategy, Structure &amp; Rivalry:</strong> The conditions governing how companies are created, organised, managed, and the nature of domestic rivalry.</li>
</ol>
<p>Two additional factors shape all four: <strong>Government</strong> (policy, regulation, subsidies) and <strong>Chance</strong> (wars, discoveries, external shocks).</p>

<h3>4.3 Stages of National Competitive Development</h3>
<table class="compare">
<tr><th>Stage</th><th>Driver</th><th>Example</th></tr>
<tr><td>Factor-Driven</td><td>Basic factors: unskilled labour, natural resources</td><td>Many developing economies</td></tr>
<tr><td>Investment-Driven</td><td>Aggressive investment in capacity and technology</td><td>Japan &amp; South Korea, 1960s-80s</td></tr>
<tr><td>Innovation-Driven</td><td>Innovation, advanced skills, R&amp;D</td><td>US, Germany, Japan today</td></tr>
<tr><td>Wealth-Driven</td><td>Existing wealth rather than new competitiveness &mdash; often leads to decline</td><td>Nations resting on past success</td></tr>
</table>

<h3>4.4 Limitations of Porter's Diamond Model</h3>
<ul>
<li>Cannot be generalised for all industries or firm sizes &mdash; developed mainly from large-firm, large-country cases.</li>
<li>Underplays the role of multinational activity and global value chains.</li>
<li>Treats "nation" as a fairly uniform unit, though conditions can vary hugely within a large country.</li>
</ul>

<h3>4.5 Strategic Groups &mdash; Meaning</h3>
<p>A strategic group is a cluster of firms within an industry that follow similar strategies along similar competitive dimensions (e.g. price, quality, distribution channels, geographic scope).</p>

<h3>4.6 Characteristics of Strategic Groups</h3>
<ul>
<li>Firms in the same strategic group are closer rivals to each other than to firms in other groups.</li>
<li>Different strategic groups can command different levels of bargaining power and face different entry/mobility barriers.</li>
<li>A firm's strategic group membership shapes the intensity of competition it actually experiences.</li>
</ul>

<h3>4.7 Mobility Barriers Between Strategic Groups</h3>
<p>Firms wishing to move from one strategic group to another face "mobility barriers" &mdash; similar in concept to industry entry barriers but specific to switching strategic position (e.g. building a new brand image, investing in new distribution, acquiring new technology).</p>

<h3>4.8 Strategic Groups as an Analytical Tool</h3>
<p>Mapping strategic groups (usually on two key competitive dimensions) helps a firm see clusters of close rivals, spot gaps in the market ("white space") not served by any group, and understand which barriers protect its own current position.</p>
"""
terms = [
    ("Porter's Diamond Model", "A framework explaining why nations become competitive in specific industries via Factor Conditions, Demand Conditions, Related/Supporting Industries, and Firm Strategy/Structure/Rivalry, shaped by Government and Chance."),
    ("Strategic Group", "A cluster of firms in an industry following similar strategies along similar competitive dimensions."),
    ("Mobility Barriers", "Obstacles that make it difficult for a firm to move from one strategic group to another within an industry."),
]
examprep = [
    "Porter's Diamond: Factor Conditions, Demand Conditions, Related &amp; Supporting Industries, Firm Strategy/Structure/Rivalry + Government &amp; Chance.",
    "National competitive development stages: Factor-driven &rarr; Investment-driven &rarr; Innovation-driven &rarr; Wealth-driven.",
    "Strategic Group = firms with similar strategies on similar dimensions; firms compete more directly within their own group.",
    "Mobility barriers prevent easy movement between strategic groups, similar to entry barriers but for switching strategic position.",
]
questions = [
    ("Explain the components of Porter's Diamond Model.", "Factor Conditions (production factors), Demand Conditions (nature of home demand), Related &amp; Supporting Industries (competitive local suppliers), and Firm Strategy/Structure/Rivalry (how firms are organised and compete domestically) &mdash; all further shaped by Government policy and Chance events."),
    ("What is a strategic group? Explain its significance.", "A strategic group is a cluster of firms in an industry following similar strategies along similar competitive dimensions. It matters because firms within the same group are each other's closest rivals, and different groups face different levels of bargaining power and profitability."),
    ("What are mobility barriers? How do they affect strategic groups?", "Mobility barriers are obstacles that make it difficult for a firm to shift from one strategic group to another (e.g. building a new brand or distribution network). They protect each group's competitive position much like industry entry barriers protect an industry."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("Having looked outward at the environment and competitors, this topic turns inward: how an "
            "organisation systematically audits its own strengths and weaknesses using recognised internal "
            "appraisal techniques.")
notes = """
<h3>5.1 Internal Appraisal &mdash; Framework</h3>
<p>Internal appraisal (or internal analysis) is the process of evaluating a corporation's resources, capabilities, and competencies against its objectives, to identify strengths to build on and weaknesses to correct.</p>

<h3>5.2 Key Success Factors (KSFs)</h3>
<p>Key Success Factors are the specific factors that are essential for a company to succeed in its particular industry (e.g. cost efficiency in commodities, brand image in FMCG, technology in electronics). The procedure of internal appraisal: recognise the strategic importance of KSFs for the industry &rarr; determine each factor's importance to the firm's own objectives &rarr; estimate the firm's strengths and weaknesses against each factor &rarr; match strengths to opportunities.</p>

<h3>5.3 Techniques Used for Internal Appraisal</h3>
<table class="compare">
<tr><th>Technique</th><th>What it does</th></tr>
<tr><td><strong>Value Chain Analysis</strong></td><td>Breaks the firm's activities into Primary Activities (inbound logistics, operations, outbound logistics, marketing &amp; sales, service) and Support Activities (procurement, technology development, HR management, firm infrastructure) to find where value and cost advantage are created.</td></tr>
<tr><td><strong>Benchmarking</strong></td><td>Compares the firm's practices, costs, and performance against "best practices" of the industry or of any excellent company, to find and close performance gaps.</td></tr>
<tr><td><strong>Balanced Scorecard</strong></td><td>Developed by Robert Kaplan &amp; David Norton in the early 1990s; evaluates performance across four perspectives (Financial, Customer, Internal Business Process, Learning &amp; Growth) instead of financial metrics alone.</td></tr>
<tr><td><strong>Financial (Quantitative) Analysis</strong></td><td>Examines objective, numerical data: ratios, cash flow, cost, profitability, employee turnover, etc.</td></tr>
<tr><td><strong>Non-Financial (Qualitative) Analysis</strong></td><td>Examines subjective factors like brand image, employee morale, and corporate culture that value-added accounting struggles to quantify.</td></tr>
</table>

<h3>5.4 Organisational Capability Profile (OCP)</h3>
<p>An OCP is a summary table that identifies, department by department (Marketing, Finance, Operations, HR, R&amp;D, Corporate/General Management), whether each area's capability is a Strength or a Weakness, and how significant it is to the organisation.</p>

<h3>5.5 Strategic Advantage Profile (SAP)</h3>
<p>The SAP represents the set of critical internal factors in which strengths and weaknesses are shown in detail, so the firm can compare itself against rival firms. It allows a step-by-step analysis of the areas critical for competitive advantage, in order to prepare this profile: identify the functional areas &rarr; assess each factor's significance to the organisation &rarr; rate each as Strong / Above Average / Average / Below Average / Weak.</p>

<h3>5.6 Structuring Internal Appraisal &mdash; SAP &amp; OCT/OCP Relationship</h3>
<p>The Strategic Advantage Profile is developed using the Organisational Capability Profile as its input: OCP identifies raw strengths/weaknesses per department; SAP then weighs each one by its strategic significance to build a decision-ready picture of the company's overall competitive position.</p>
"""
terms = [
    ("Key Success Factors (KSFs)", "The specific factors a firm must get right to succeed in its particular industry."),
    ("Value Chain Analysis", "A technique that breaks a firm's activities into primary and support activities to locate sources of cost and value advantage."),
    ("Benchmarking", "Comparing a firm's practices and performance against industry best practice to close performance gaps."),
    ("Balanced Scorecard", "A performance-evaluation framework (Kaplan &amp; Norton) using Financial, Customer, Internal Process, and Learning &amp; Growth perspectives."),
    ("Organisational Capability Profile (OCP)", "A department-by-department summary of an organisation's strengths and weaknesses."),
    ("Strategic Advantage Profile (SAP)", "A weighted profile of a firm's critical internal factors, used to compare its competitive position against rivals."),
]
examprep = [
    "Internal appraisal evaluates resources, capabilities, and competencies against objectives to find strengths/weaknesses.",
    "Key techniques: Value Chain Analysis, Benchmarking, Balanced Scorecard (Financial/Customer/Internal Process/Learning&amp;Growth), Financial (quantitative) and Non-Financial (qualitative) analysis.",
    "OCP = department-wise strength/weakness summary; SAP = weighted, competitor-compared profile built from the OCP.",
]
questions = [
    ("What are Key Success Factors? Explain the procedure for internal appraisal built around them.", "KSFs are the factors essential for success in a particular industry. The procedure: recognise the industry's KSFs, determine their importance to the firm's own objectives, estimate the firm's strengths/weaknesses against each factor, and match strengths to available opportunities."),
    ("Explain the Balanced Scorecard as a technique of internal appraisal.", "Developed by Kaplan &amp; Norton, it evaluates organisational performance across four perspectives &mdash; Financial, Customer, Internal Business Process, and Learning &amp; Growth &mdash; rather than relying on financial measures alone."),
    ("Distinguish between the Organisational Capability Profile (OCP) and the Strategic Advantage Profile (SAP).", "The OCP is a department-by-department (marketing, finance, operations, HR, R&amp;D) summary identifying strengths and weaknesses. The SAP builds on the OCP by weighting each factor's strategic significance and comparing the firm against rivals, giving a decision-ready competitive picture."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("Strategy ultimately rests on what an organisation has and what it can do. This topic distinguishes "
            "Resources (the assets a firm owns) from Capabilities (what it can actually do with them), and how "
            "the two interact.")
notes = """
<h3>6.1 Meaning of Resources</h3>
<p>Resources are the assets available to and controlled by a firm, which can be combined to create competitive advantage. A resource alone is worth little until a firm builds the capability to use it effectively.</p>

<h3>6.2 Types of Resources</h3>
<table class="compare">
<tr><th>Tangible Resources</th><th>Intangible Resources</th></tr>
<tr><td>Assets that can be seen, touched, and quantified &mdash; land, buildings, plant, machinery, financial assets, inventory. Easier to value and imitate.</td><td>Assets that cannot be seen or touched &mdash; brand reputation, patents, organisational culture, employee know-how, customer relationships. Harder to imitate; often a greater source of sustained advantage.</td></tr>
</table>

<h3>6.3 Criteria for Valuable Resources</h3>
<ul>
<li><strong>Value:</strong> The resource should give a very high perceived value.</li>
<li><strong>Uniqueness:</strong> It should be unique in comparison to competitors' resources.</li>
<li><strong>Difficult to Trade or Imitate:</strong> Intangible resources like reputation and culture are especially hard to trade or copy.</li>
<li><strong>Difficult to Substitute:</strong> Some resources are hard for competitors to substitute with alternatives.</li>
</ul>

<h3>6.4 Meaning of Capabilities</h3>
<p>Capabilities are developed by combining resources through organisational processes to perform a specific task or activity. Capabilities are intangible; they exist in the routines, skills, and know-how the organisation has built by using its resources over time.</p>

<h3>6.5 Types of Capabilities in Various Functional Areas</h3>
<ul>
<li><strong>Marketing Capability:</strong> Product, Pricing, Promotion, Place (distribution) skills.</li>
<li><strong>Human Resource Capability:</strong> Recruitment, selection, training, development, industrial relations.</li>
<li><strong>Financial Capability:</strong> Efficient allocation and utilisation of funds, budgeting, investment strategy.</li>
<li><strong>Operations Capability:</strong> Managing production, quality, cost, and efficiency of operations.</li>
<li><strong>R&amp;D Capability:</strong> Ability to research, develop, and commercialise new technologies/products.</li>
<li><strong>General Management Capability:</strong> Developing skills for general operations, strategy, and coordination.</li>
<li><strong>Information Management Capability:</strong> Acquisition, retention, transmission, and synthesis/use of data and information.</li>
</ul>

<h3>6.6 Relationship Between Resources &amp; Capabilities</h3>
<p>Resources and capabilities interact and depend on each other: a resource on its own generates little value; a capability needs resources to act on. Key dimensions of this relationship:</p>
<ul>
<li><strong>Measurement:</strong> Resources are relatively easy to measure; capabilities (being intangible) are hard to measure.</li>
<li><strong>Market Exchange:</strong> Resources can often be bought and sold on an open market; capabilities are embedded in the firm and cannot easily be bought/sold separately.</li>
<li><strong>Difficult to Imitate:</strong> Capabilities built over years through organisational learning are far harder for a rival to copy than a single resource.</li>
</ul>
"""
terms = [
    ("Resource", "An asset available to and controlled by a firm that can be combined to help create competitive advantage."),
    ("Tangible Resources", "Physical, quantifiable assets such as land, plant, machinery, and financial assets."),
    ("Intangible Resources", "Non-physical assets such as brand reputation, patents, culture, and know-how."),
    ("Capability", "What an organisation can actually do, built by combining resources through organisational processes."),
]
examprep = [
    "Resources = what a firm has (Tangible: physical/financial; Intangible: brand, culture, know-how, patents).",
    "Valuable resources are Valuable, Unique, hard to Trade/Imitate, and hard to Substitute.",
    "Capabilities = what a firm can do, built by combining resources via organisational processes; found across Marketing, HR, Finance, Operations, R&amp;D, General Management, and Information Management.",
    "Resources are easy to measure and can often be traded; capabilities are hard to measure, embedded in the firm, and far harder to imitate.",
]
questions = [
    ("Distinguish between tangible and intangible resources.", "Tangible resources are physical, quantifiable assets like land, buildings, and financial assets, which are relatively easy to value and imitate. Intangible resources such as brand reputation, patents, and culture cannot be seen or touched and are much harder for rivals to imitate."),
    ("What is a capability? Explain the different types of functional capabilities.", "A capability is what an organisation can actually do, created by combining resources through organisational processes. Types include Marketing, Human Resource, Financial, Operations, R&amp;D, General Management, and Information Management capabilities."),
    ("Explain the relationship between resources and capabilities.", "Resources and capabilities are interdependent: resources alone create little value without the capability to use them, while capabilities need resources to act on. Resources are easier to measure and can often be traded in the market; capabilities are intangible, embedded in the organisation, and much harder to imitate."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))

# ================= Topic 7 =================
fname, title, prev_link, next_link = T(7)
overview = ("This topic looks at what makes some capabilities more than just useful &mdash; genuinely rare and "
            "hard to copy. It introduces Core Competence and the VRIO framework, the standard tool for judging "
            "whether a resource or capability can actually deliver sustained competitive advantage.")
notes = """
<h3>7.1 VRIO Framework &mdash; Origin</h3>
<p>Developed by J.B. Barney (refined in 1995 from his earlier 1991 VRIN framework &mdash; Valuable, Rare, Inimitable, Non-substitutable). VRIO analyses a firm's internal resources and capabilities to determine which ones can be a genuine source of sustained competitive advantage.</p>

<h3>7.2 The Four VRIO Questions</h3>
<ol>
<li><strong>Valuable?</strong> Does the resource/capability allow the firm to exploit an opportunity or neutralise a threat? If <em>No</em> &rarr; Competitive Disadvantage.</li>
<li><strong>Rare?</strong> Is it possessed by few, if any, competing firms? If <em>No</em> &rarr; Competitive Parity.</li>
<li><strong>Costly to Imitate?</strong> Would it be difficult/costly for other firms to obtain or develop it? If <em>No</em> &rarr; Temporary Competitive Advantage.</li>
<li><strong>Organised to Capture Value?</strong> Is the firm organised (systems, processes, culture) to fully exploit the resource? If <em>Yes</em> to all four &rarr; Sustained Competitive Advantage.</li>
</ol>

<h3>7.3 VRIO Outcomes</h3>
<table class="compare">
<tr><th>Valuable</th><th>Rare</th><th>Costly to Imitate</th><th>Organised</th><th>Competitive Implication</th></tr>
<tr><td>No</td><td>&ndash;</td><td>&ndash;</td><td>&ndash;</td><td>Competitive Disadvantage</td></tr>
<tr><td>Yes</td><td>No</td><td>&ndash;</td><td>&ndash;</td><td>Competitive Parity</td></tr>
<tr><td>Yes</td><td>Yes</td><td>No</td><td>&ndash;</td><td>Temporary Competitive Advantage</td></tr>
<tr><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Sustained Competitive Advantage</td></tr>
</table>

<h3>7.4 Reasons a Resource May Be Costly to Imitate</h3>
<ul>
<li><strong>Historical Conditions:</strong> The resource was developed due to a unique, unrepeatable set of past events.</li>
<li><strong>Causal Ambiguity:</strong> It is difficult for rivals to identify exactly what causes the firm's advantage.</li>
<li><strong>Social Complexity:</strong> The resource is embedded in complex social phenomena (culture, relationships, reputation) that are very hard to engineer deliberately.</li>
</ul>

<h3>7.5 Meaning of Core Competence</h3>
<p>Prahalad &amp; Hamel (1990): "Core Competence is the collective learning in the organisation, especially how to coordinate diverse production skills and integrate multiple streams of technologies." Coyne, Hall &amp; Clifford: core competencies are a combination of complementary skills and knowledge bases embedded in a group or team that results in the ability to execute one or more critical processes to a world-class standard.</p>

<h3>7.6 Characteristics of Core Competencies</h3>
<ul>
<li><strong>Pervasive:</strong> Runs across multiple products/businesses of the organisation, not confined to just one.</li>
<li><strong>Valuable:</strong> Provides a real, meaningful benefit to customers.</li>
<li><strong>Difficult to Imitate:</strong> Hard for competitors to replicate.</li>
<li><strong>Non-Substitutable:</strong> Competitors cannot easily achieve the same benefit through an alternative competence.</li>
</ul>
<p>Conditions for a competence to be considered "core": it should be Rare, Valuable, hard to Imitate, and Non-substitutable (mirroring the VRIO logic).</p>

<h3>7.7 Building a Sustainable Core Competence</h3>
<p>Five elements: <strong>Knowledge and Requisite Technology</strong> in the specific area of operation; developed through <strong>Creating New Success Factors</strong> (differentiation, innovation); <strong>Product Innovation</strong> to introduce new features ahead of the competition; <strong>Establishing Relative Superiority</strong> over the resources/assets of competitors; and continuously <strong>Looking Toward the Future</strong> and anticipating unarticulated customer needs.</p>

<h3>7.8 Guidelines for Building &amp; Sustaining Core Competencies</h3>
<ul>
<li>Competencies should be looked at as valuable, firm-specific assets, not disposable resources.</li>
<li>They should be difficult for rivals to imitate or acquire similarly.</li>
<li>They should be valuable to several different markets, not just one narrow niche.</li>
<li>Dealing with new and unanticipated problems requires managerial flexibility, since rigid systems can lock in outdated competencies.</li>
</ul>
"""
terms = [
    ("VRIO Framework", "A tool (J.B. Barney) analysing whether a resource/capability is Valuable, Rare, costly to Imitate, and whether the firm is Organised to capture its value."),
    ("Sustained Competitive Advantage", "An advantage that persists because the underlying resource is Valuable, Rare, costly to Imitate, and the firm is Organised to exploit it."),
    ("Core Competence", "The collective learning of an organisation in coordinating diverse skills and integrating multiple technology streams (Prahalad &amp; Hamel)."),
    ("Causal Ambiguity", "The difficulty competitors face in identifying exactly what causes a firm's competitive advantage, making it hard to imitate."),
]
examprep = [
    "VRIO: Valuable? &rarr; Rare? &rarr; Costly to Imitate? &rarr; Organised to capture value? All four Yes = Sustained Competitive Advantage.",
    "Failing 'Valuable' = Disadvantage; failing 'Rare' = Parity; failing 'Costly to Imitate' = only Temporary Advantage.",
    "Resources are hard to imitate due to Historical Conditions, Causal Ambiguity, or Social Complexity.",
    "Core Competence (Prahalad &amp; Hamel) = collective organisational learning in coordinating skills/technology; must be Pervasive, Valuable, hard to Imitate, and Non-substitutable.",
]
questions = [
    ("Explain the VRIO framework and its four questions.", "VRIO (J.B. Barney) asks whether a resource is Valuable, Rare, Costly to Imitate, and whether the firm is Organised to exploit it. Depending on how many of these are satisfied, the outcome ranges from Competitive Disadvantage, through Parity and Temporary Advantage, up to Sustained Competitive Advantage when all four are met."),
    ("Why are some resources costly for competitors to imitate?", "Because of Historical Conditions (a unique, unrepeatable path of development), Causal Ambiguity (rivals cannot identify exactly what causes the advantage), and Social Complexity (the resource is embedded in culture or relationships that are very hard to engineer deliberately)."),
    ("Define core competence and explain its characteristics.", "Core competence is the collective learning of an organisation in coordinating diverse skills and integrating multiple technologies (Prahalad &amp; Hamel). It must be Pervasive (spans multiple products/businesses), Valuable to customers, Difficult to Imitate, and Non-substitutable."),
]
U.write(fname, U.page(fname, 7, title, overview, notes, terms, examprep, questions, prev_link, next_link))

# ================= Topic 8 =================
fname, title, prev_link, next_link = T(8)
overview = ("Unit 2 closes by tying everything together into Competitive Advantage &mdash; how a firm actually "
            "outperforms rivals, the generic strategies it can choose to achieve this, and how that advantage "
            "can be sustained (or lost) over time.")
notes = """
<h3>8.1 Introduction to Competitive Advantage</h3>
<p>Competitive advantage is created when a firm delivers the same benefits as competitors at a lower cost (cost advantage), or delivers benefits that exceed those of competing products (differentiation advantage). It allows a firm to create superior value for its customers and superior profits for itself.</p>

<h3>8.2 Porter's Generic Competitive Strategies</h3>
<p>Michael Porter proposed that a firm can attain above-average performance by choosing one of three generic strategies, based on Competitive Scope (broad vs narrow) and Competitive Advantage (low cost vs differentiation):</p>
<table class="compare">
<tr><th>Strategy</th><th>Idea</th><th>Conditions Favouring It</th></tr>
<tr><td><strong>Cost Leadership</strong></td><td>Becoming the lowest-cost producer in the industry, using price to compete.</td><td>Price-sensitive buyers, standardised products, economies of scale available (e.g. Walmart, ironsteel newcomers in India).</td></tr>
<tr><td><strong>Differentiation</strong></td><td>Offering products/services perceived as unique, commanding a premium price.</td><td>Buyers value uniqueness, brand loyalty is achievable, low price-sensitivity (e.g. L'Or&eacute;al's differentiated product lines).</td></tr>
<tr><td><strong>Focus</strong></td><td>Concentrating on a narrow market segment (niche), using either a cost or differentiation approach within it.</td><td>Segment has distinct needs, low competitor interest in the niche, industry entry barriers are low for a specialist (e.g. Mahindra Holidays in the timeshare segment).</td></tr>
</table>

<h3>8.3 Sources of Competitive Advantage Across Functional Areas</h3>
<ul>
<li><strong>Marketing:</strong> Launching new products, larger market share, brand image, effective promotional strategies.</li>
<li><strong>Research &amp; Development:</strong> Facilities, quality and depth of research, patents, technical/scientific skills.</li>
<li><strong>Manufacturing/Operations:</strong> Flexible and adaptable production capacity, cost reduction in production, improved productivity.</li>
<li><strong>Human Resources:</strong> Skills, knowledge, motivation, and experience of employees.</li>
<li><strong>Finance:</strong> Efficient cash flow, capable financial management, strong cost of capital position.</li>
<li><strong>Corporate/Overall Resources:</strong> Size of the company, quality of management, experienced board of directors.</li>
</ul>

<h3>8.4 Generic Building Blocks of Competitive Advantage</h3>
<ol>
<li><strong>Efficiency:</strong> Achieving optimum resource utilisation to reduce costs.</li>
<li><strong>Quality:</strong> Delivering superior, reliable products/services consistently.</li>
<li><strong>Innovation:</strong> Developing new products, processes, or technologies ahead of competitors.</li>
<li><strong>Customer Responsiveness:</strong> Identifying and meeting customer needs faster and better than rivals.</li>
</ol>

<h3>8.5 Durability of Competitive Advantage</h3>
<p>How long an advantage lasts depends on the height of Barriers to Imitation and the Capability of Competitors to imitate. Barriers to imitation include the firm's intellectual property, tacit know-how embedded in its people, and the complexity of its manufacturing/marketing processes.</p>

<h3>8.6 Avoiding Competitive Failure</h3>
<ul>
<li><strong>The Icarus Paradox:</strong> A concept from Greek mythology (Icarus's wax wings melted when he flew too close to the sun) &mdash; a firm's own past strengths, over-extended, can cause its downfall (e.g. becoming so committed to one winning formula that the firm fails to adapt).</li>
<li><strong>Organisational Inertia:</strong> Existing decision-makers, culture, and processes resist change, even when the competitive environment demands it.</li>
<li><strong>Industry Dynamism:</strong> Fast-changing industries (short product cycles, rapid technology change) erode competitive advantage faster than stable industries.</li>
</ul>

<h3>8.7 Guidelines for Sustaining Competitive Advantage</h3>
<ul>
<li>Continuously invest in developing new competencies rather than resting on existing ones.</li>
<li>Treat competitive advantage and corporate strategy as mutually supporting, not separate activities.</li>
<li>Maintain effective customer relationships that create switching costs for buyers.</li>
<li>Continuously innovate and reinvent the firm's product/service offerings.</li>
</ul>
"""
terms = [
    ("Competitive Advantage", "The ability of a firm to deliver the same benefits as competitors at lower cost, or benefits exceeding those of competitors, creating superior customer and firm value."),
    ("Cost Leadership", "A generic strategy of becoming the lowest-cost producer in an industry."),
    ("Differentiation", "A generic strategy of offering products/services perceived as unique, allowing a premium price."),
    ("Focus Strategy", "A generic strategy concentrating on a narrow market segment using either a cost or differentiation approach."),
    ("Icarus Paradox", "The idea that a firm's own past strengths, over-extended, can become the cause of its downfall."),
]
examprep = [
    "Porter's Generic Strategies: Cost Leadership, Differentiation, Focus &mdash; based on competitive scope and type of advantage sought.",
    "Generic building blocks of competitive advantage: Efficiency, Quality, Innovation, Customer Responsiveness.",
    "Durability of advantage depends on barriers to imitation and competitors' capability to imitate.",
    "Avoiding failure: beware the Icarus Paradox (past strengths overextended), organisational inertia, and fast industry dynamism.",
]
questions = [
    ("Explain Porter's three generic competitive strategies.", "Cost Leadership (becoming the lowest-cost producer), Differentiation (offering a uniquely valued product/service commanding a premium price), and Focus (concentrating on a narrow market segment using either a cost or differentiation approach within it)."),
    ("What are the generic building blocks of competitive advantage?", "Efficiency (optimum resource use), Quality (superior, reliable output), Innovation (new products/processes ahead of rivals), and Customer Responsiveness (meeting customer needs faster/better than competitors)."),
    ("Explain the Icarus Paradox with reference to sustaining competitive advantage.", "The Icarus Paradox describes how a firm's own past strengths, when over-extended or clung to rigidly, can become the very cause of its decline &mdash; much like Icarus's wings failing when he flew too close to the sun. It is a caution against organisational inertia and over-reliance on a single winning formula."),
]
U.write(fname, U.page(fname, 8, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Eight topics covering external environment through competitive advantage: business environment, industry analysis (Five Forces), competitor analysis, Porter's Diamond &amp; strategic groups, internal appraisal techniques, resources &amp; capabilities, core competence &amp; VRIO, and generic competitive strategies.")

print("Unit 2 complete: all 8 topics + index written.")



