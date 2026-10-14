# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Management-Concepts-and-Organisational-Behavior\units"
BOOK_HTML = "Book: <em>Management Concepts and Organisational Behaviour</em> (BA4102, Anna University MBA Sem I)"
BOOK_PLAIN = "Management Concepts and Organisational Behaviour (BA4102)"

TOPICS = [
    ("topic1-comparative-management-japanese-practices.html", "Comparative Management Styles and Japanese Management Practices"),
    ("topic2-organisational-creativity-innovation.html", "Organisational Creativity and Innovation"),
    ("topic3-ob-across-cultures.html", "Organisational Behaviour Across Cultures"),
    ("topic4-managing-international-workforce.html", "Managing International Workforce and Cultural Contingencies"),
    ("topic5-cross-cultural-communication-diversity.html", "Cross-Cultural Communication and Managing Diversity"),
]

AMBER_THEME = dict(accent="#a1591f", accent_dark="#6b3a14", accent_light="#f7ebdd",
                    border="#e8d7c3", shadow="rgba(161,89,31,.14)")

U = common.UnitBuilder(5, "Emerging Aspects of Organisational Behaviour", TOPICS,
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
overview = ("This closing unit looks at emerging, global dimensions of management and OB. It opens by "
            "comparing management styles across countries, with Japanese management practices as a "
            "well-studied example of an alternative to Western approaches.")
notes = """
<h3>1.1 Comparative Management</h3>
<p>Comparative management studies how management practices, assumptions and effectiveness differ across countries and cultures, recognising that a management style effective in one national context may not transfer directly to another.</p>

<h3>1.2 Why Management Styles Differ Across Countries</h3>
<ul>
<li><strong>Cultural Values:</strong> Differing national attitudes toward authority, individualism, risk and time horizon shape what employees expect from managers.</li>
<li><strong>Economic Systems:</strong> The structure of a country's economy and labour market influences employment practices and incentives.</li>
<li><strong>Legal and Political Environment:</strong> Labour laws, regulation and political stability shape how organisations are structured and managed.</li>
<li><strong>Education and Social Structure:</strong> The availability of skilled labour and prevailing social hierarchies affect management approaches.</li>
</ul>

<h3>1.3 Japanese Management Practices</h3>
<p>Japanese management, which attracted global attention for its role in Japan's post-war economic success, is built on several distinctive features:</p>
<ol>
<li><strong>Lifetime Employment:</strong> Historically, large Japanese firms offered employees job security for their entire career, building strong loyalty and long-term thinking.</li>
<li><strong>Consensus Decision-Making (Ringi System):</strong> Decisions are made through a bottom-up process where a proposal circulates for agreement among all relevant parties before being finalised, rather than being imposed top-down.</li>
<li><strong>Seniority-Based Promotion and Pay:</strong> Advancement and compensation have traditionally been linked closely to length of service rather than purely to individual performance.</li>
<li><strong>Quality Circles:</strong> Small groups of employees who voluntarily meet to identify and solve work-related quality problems, contributing to continuous improvement (Kaizen).</li>
<li><strong>Strong Group Orientation:</strong> Emphasis on group harmony and collective responsibility over individual achievement and recognition.</li>
<li><strong>Enterprise Unions:</strong> Labour unions are organised around individual companies rather than across whole industries, promoting closer cooperation between management and workers.</li>
</ol>

<h3>1.4 Strengths and Limitations of Japanese Management</h3>
<ul>
<li><strong>Strengths:</strong> High employee loyalty, strong quality consciousness, effective continuous improvement, and smooth implementation once consensus is reached.</li>
<li><strong>Limitations:</strong> Consensus decision-making is slow; lifetime employment and seniority-based systems can reduce flexibility and make it harder to reward individual high performers; the model has had to adapt under global competitive and demographic pressures.</li>
</ul>

<h3>1.5 Applying Lessons from Comparative Management</h3>
<p>Rather than importing a foreign management model wholesale, organisations typically benefit most from selectively adapting practices &mdash; such as quality circles or consensus-building for major decisions &mdash; to fit their own cultural and organisational context.</p>
"""
terms = [
    ("Comparative Management", "The study of how management practices and their effectiveness differ across countries and cultures."),
    ("Ringi System", "A Japanese bottom-up consensus decision-making process in which a proposal circulates for agreement before being finalised."),
    ("Quality Circles", "Small groups of employees who voluntarily meet to identify and solve work-related quality problems."),
    ("Kaizen", "The Japanese philosophy of continuous, incremental improvement in processes and quality."),
]
examprep = [
    "Comparative management studies how practices differ across countries due to culture, economic system, legal/political environment, and education/social structure.",
    "Japanese management features: Lifetime Employment, Ringi (consensus) decision-making, Seniority-based promotion/pay, Quality Circles, Group Orientation, Enterprise Unions.",
    "Japanese management strengths: loyalty, quality focus, continuous improvement; limitations: slow decisions, reduced flexibility, pressure to adapt under global competition.",
]
questions = [
    ("Why do management styles differ across countries?", "They differ due to cultural values (attitudes toward authority, individualism, time), economic systems, the legal and political environment, and differences in education and social structure across countries."),
    ("Explain the key features of Japanese management practices.", "Lifetime employment building loyalty, consensus-based (Ringi) decision-making, seniority-based promotion and pay, Quality Circles for continuous improvement, a strong group orientation over individual recognition, and enterprise-level labour unions."),
    ("What are the strengths and limitations of Japanese management?", "Strengths include high employee loyalty, strong quality consciousness, and smooth implementation once consensus is reached. Limitations include slow decision-making, reduced flexibility from lifetime employment and seniority systems, and pressure to adapt under global competitive and demographic change."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("Organisational creativity and innovation are increasingly treated as something management can "
            "deliberately cultivate, not just something that happens by chance. This topic covers what "
            "drives creativity at work and how organisations convert ideas into innovation.")
notes = """
<h3>2.1 Meaning of Organisational Creativity</h3>
<p>Organisational creativity is the generation of novel and useful ideas by individuals or groups working together within an organisational context.</p>

<h3>2.2 Meaning of Innovation</h3>
<p>Innovation is the successful implementation of creative ideas &mdash; turning a novel idea into a new product, service, process or practice that creates value. Creativity is the starting point; innovation is creativity put into practice.</p>

<h3>2.3 Factors Influencing Organisational Creativity</h3>
<table class="compare">
<tr><th>Factor</th><th>Influence</th></tr>
<tr><td><strong>Individual Factors</strong></td><td>Expertise, creative thinking skills, and intrinsic motivation of employees.</td></tr>
<tr><td><strong>Organisational Climate</strong></td><td>A climate that tolerates reasonable risk-taking and failure encourages more creative effort.</td></tr>
<tr><td><strong>Leadership Support</strong></td><td>Leaders who encourage experimentation and new ideas rather than only rewarding conformity.</td></tr>
<tr><td><strong>Resources and Autonomy</strong></td><td>Giving employees enough time, resources and freedom to explore new approaches.</td></tr>
<tr><td><strong>Diversity</strong></td><td>Diverse teams bring varied perspectives that often spark more creative solutions.</td></tr>
</table>

<h3>2.4 The Innovation Process</h3>
<ol>
<li><strong>Idea Generation:</strong> Creating or discovering a new idea, often through creative individuals or teams.</li>
<li><strong>Idea Development:</strong> Refining and testing the idea to assess its practicality and value.</li>
<li><strong>Championing:</strong> An internal advocate promotes the idea and builds support for it.</li>
<li><strong>Implementation:</strong> The idea is put into practice as a new product, service or process.</li>
<li><strong>Diffusion:</strong> The innovation spreads throughout the organisation or market.</li>
</ol>

<h3>2.5 Barriers to Creativity and Innovation</h3>
<ul>
<li>A rigid, highly bureaucratic structure that discourages risk-taking.</li>
<li>A culture that punishes failure rather than treating it as part of learning.</li>
<li>Short-term performance pressure that crowds out exploratory thinking.</li>
<li>Insufficient resources, time, or autonomy given to employees.</li>
</ul>

<h3>2.6 Encouraging Creativity and Innovation</h3>
<ul>
<li>Creating psychological safety so employees feel safe proposing unconventional ideas.</li>
<li>Rewarding and recognising creative effort, not just successful outcomes.</li>
<li>Building diverse, cross-functional teams to generate a wider range of ideas.</li>
<li>Providing dedicated time or resources (e.g. innovation labs, hackathons) for exploratory work.</li>
</ul>
"""
terms = [
    ("Organisational Creativity", "The generation of novel and useful ideas by individuals or groups within an organisational context."),
    ("Innovation", "The successful implementation of creative ideas into a new product, service, process or practice that creates value."),
    ("Psychological Safety", "A climate in which employees feel safe to propose unconventional ideas or admit mistakes without fear of punishment."),
]
examprep = [
    "Creativity = generating novel, useful ideas; Innovation = successfully implementing those ideas.",
    "Factors influencing creativity: Individual factors, Organisational climate, Leadership support, Resources/Autonomy, Diversity.",
    "Innovation process: Idea Generation &rarr; Idea Development &rarr; Championing &rarr; Implementation &rarr; Diffusion.",
    "Barriers: rigid bureaucracy, fear of failure, short-term pressure, lack of resources/autonomy.",
]
questions = [
    ("Differentiate between creativity and innovation.", "Creativity is the generation of novel and useful ideas, while innovation is the successful implementation of those ideas into a new product, service, process or practice that creates value &mdash; creativity is the starting point, innovation is creativity put into practice."),
    ("What factors influence organisational creativity?", "Individual factors (expertise, creative skills, motivation), organisational climate (tolerance for risk and failure), leadership support for experimentation, adequate resources and autonomy, and team diversity bringing varied perspectives."),
    ("Explain the stages of the innovation process.", "Idea Generation creates a new idea; Idea Development refines and tests it; Championing has an internal advocate build support; Implementation puts the idea into practice; and Diffusion spreads the innovation through the organisation or market."),
];
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("As organisations operate across borders, understanding how culture shapes organisational "
            "behaviour becomes essential. This topic covers how OB differs across cultures and the "
            "conditions that affect cross-cultural organisational operations.")
notes = """
<h3>3.1 Organisational Behaviour Across Cultures</h3>
<p>Organisational Behaviour across cultures (Cross-Cultural OB) studies how national culture shapes employee attitudes, motivation, communication and management effectiveness, recognising that OB theories developed in one cultural context do not automatically apply everywhere.</p>

<h3>3.2 Hofstede's Cultural Dimensions</h3>
<p>Geert Hofstede's research identified key dimensions along which national cultures differ, with major implications for management:</p>
<table class="compare">
<tr><th>Dimension</th><th>Meaning</th></tr>
<tr><td><strong>Power Distance</strong></td><td>The degree to which a culture accepts unequal distribution of power between superiors and subordinates.</td></tr>
<tr><td><strong>Individualism vs Collectivism</strong></td><td>Whether people see themselves primarily as independent individuals or as part of a tightly-knit group.</td></tr>
<tr><td><strong>Uncertainty Avoidance</strong></td><td>The degree to which a culture feels threatened by ambiguous or uncertain situations and tries to avoid them through rules.</td></tr>
<tr><td><strong>Masculinity vs Femininity</strong></td><td>The degree to which a culture values assertiveness and achievement (masculine) versus cooperation and quality of life (feminine).</td></tr>
<tr><td><strong>Long-Term vs Short-Term Orientation</strong></td><td>Whether a culture emphasises future rewards like persistence and thrift, or values tradition and quick results.</td></tr>
</table>

<h3>3.3 Conditions Affecting Cross-Cultural Organisational Operations</h3>
<ul>
<li><strong>Legal and Regulatory Differences:</strong> Labour law, taxation and compliance requirements vary significantly by country.</li>
<li><strong>Economic Conditions:</strong> Wage levels, inflation and market maturity differ across the countries an organisation operates in.</li>
<li><strong>Political Stability:</strong> Political risk affects an organisation's ability to plan and operate confidently.</li>
<li><strong>Language and Communication Norms:</strong> Direct differences in language, and indirect differences in communication style (direct vs indirect, high-context vs low-context).</li>
<li><strong>Religious and Social Customs:</strong> Local customs around holidays, dress, gender roles and etiquette that an organisation must respect.</li>
</ul>

<h3>3.4 Implications for Management</h3>
<ul>
<li>Leadership and motivation approaches that work well in one culture may need to be adapted for another (e.g. individual-focused incentive pay may motivate less in a highly collectivist culture).</li>
<li>Decision-making style should be adjusted to local expectations around hierarchy and participation.</li>
<li>Managers operating internationally benefit from cultural-awareness training before taking on cross-border responsibilities.</li>
</ul>
"""
terms = [
    ("Cross-Cultural OB", "The study of how national culture shapes employee attitudes, motivation, communication and management effectiveness."),
    ("Power Distance", "Hofstede's cultural dimension measuring the degree to which a culture accepts unequal distribution of power."),
    ("Individualism vs Collectivism", "Hofstede's cultural dimension measuring whether people see themselves as independent individuals or as part of a tightly-knit group."),
    ("Uncertainty Avoidance", "Hofstede's cultural dimension measuring how threatened a culture feels by ambiguous situations."),
]
examprep = [
    "Cross-Cultural OB studies how national culture shapes attitudes, motivation, communication and management effectiveness.",
    "Hofstede's 5 dimensions: Power Distance, Individualism vs Collectivism, Uncertainty Avoidance, Masculinity vs Femininity, Long-Term vs Short-Term Orientation.",
    "Conditions affecting cross-cultural operations: legal/regulatory, economic, political stability, language/communication norms, religious/social customs.",
]
questions = [
    ("Explain Hofstede's cultural dimensions.", "Power Distance measures acceptance of unequal power distribution; Individualism vs Collectivism measures whether people identify as independent or as part of a group; Uncertainty Avoidance measures comfort with ambiguity; Masculinity vs Femininity measures emphasis on achievement versus quality of life; and Long-Term vs Short-Term Orientation measures emphasis on future rewards versus tradition and quick results."),
    ("What conditions affect cross-cultural organisational operations?", "Legal and regulatory differences, economic conditions, political stability, language and communication norms, and religious and social customs that vary across the countries an organisation operates in."),
    ("What are the management implications of cross-cultural differences?", "Leadership and motivation approaches may need adapting to local cultural expectations, decision-making style should reflect local norms around hierarchy and participation, and managers benefit from cultural-awareness training before taking on international responsibilities."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("Managing a workforce spread across countries adds a layer of complexity to every OB topic "
            "covered so far. This topic covers the challenges of managing an international workforce and "
            "how productivity itself is shaped by cultural contingencies.")
notes = """
<h3>4.1 Managing an International Workforce</h3>
<p>Organisations operating across borders must manage employees from different national backgrounds, often including expatriates (employees working outside their home country) alongside local staff (host-country nationals).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Categories of International Staff</h4>
<ul>
<li><strong>Parent-Country Nationals (PCNs):</strong> Employees from the organisation's home country, sent abroad.</li>
<li><strong>Host-Country Nationals (HCNs):</strong> Local employees hired in the country where the organisation operates.</li>
<li><strong>Third-Country Nationals (TCNs):</strong> Employees from a country other than the home or host country.</li>
</ul>

<h3>4.2 Challenges in Managing an International Workforce</h3>
<ul>
<li><strong>Cultural Adjustment:</strong> Expatriates and their families often face culture shock adapting to a new environment.</li>
<li><strong>Compensation Complexity:</strong> Designing fair pay structures across countries with very different cost-of-living and tax regimes.</li>
<li><strong>Training and Development:</strong> Preparing staff with the cross-cultural skills needed to work effectively across borders.</li>
<li><strong>Repatriation:</strong> Successfully reintegrating expatriates into the home organisation once an international assignment ends.</li>
<li><strong>Communication Across Time Zones and Languages:</strong> Coordinating work across dispersed, culturally diverse teams.</li>
</ul>

<h3>4.3 Productivity and Cultural Contingencies</h3>
<p>What drives productivity is not culturally universal &mdash; the contingency view holds that the most effective management practices for boosting productivity depend on the cultural context of the workforce.</p>
<table class="compare">
<tr><th>Cultural Context</th><th>Productivity Implication</th></tr>
<tr><td>High Power Distance</td><td>Clear, top-down direction and respect for hierarchy may boost productivity more than participative approaches.</td></tr>
<tr><td>Collectivist Culture</td><td>Team-based goals and group rewards tend to motivate more effectively than purely individual incentive pay.</td></tr>
<tr><td>High Uncertainty Avoidance</td><td>Clear rules, detailed procedures and job security tend to support higher productivity and lower anxiety.</td></tr>
<tr><td>Individualist Culture</td><td>Individual recognition, autonomy and performance-based pay tend to be more motivating.</td></tr>
</table>

<h3>4.4 Strategies for Managing International Workforce Effectively</h3>
<ul>
<li>Providing cross-cultural training before and during international assignments.</li>
<li>Designing compensation packages that are fair and competitive across different national contexts.</li>
<li>Building global mentoring and support networks for expatriates and their families.</li>
<li>Adapting management style to the cultural expectations of the local workforce rather than applying a single uniform approach everywhere.</li>
</ul>
"""
terms = [
    ("Expatriate", "An employee working in a country other than their home country on an international assignment."),
    ("Host-Country National (HCN)", "A local employee hired in the country where an international organisation operates."),
    ("Third-Country National (TCN)", "An employee from a country other than the organisation's home country or the host country where they are working."),
    ("Repatriation", "The process of reintegrating an expatriate employee back into the home organisation after an international assignment ends."),
]
examprep = [
    "3 categories of international staff: Parent-Country Nationals (PCNs), Host-Country Nationals (HCNs), Third-Country Nationals (TCNs).",
    "Challenges: cultural adjustment, compensation complexity, training/development, repatriation, cross-time-zone communication.",
    "Productivity is culturally contingent: high power distance favours top-down direction; collectivist cultures favour team rewards; high uncertainty avoidance favours clear rules; individualist cultures favour individual recognition/pay.",
]
questions = [
    ("Explain the categories of international staff.", "Parent-Country Nationals (PCNs) are employees from the organisation's home country sent abroad; Host-Country Nationals (HCNs) are local employees hired in the operating country; and Third-Country Nationals (TCNs) are employees from a country other than the home or host country."),
    ("What challenges arise in managing an international workforce?", "Cultural adjustment and culture shock for expatriates, compensation complexity across different cost-of-living and tax regimes, cross-cultural training needs, repatriation of returning expatriates, and communication across time zones and languages."),
    ("Explain the concept of productivity and cultural contingencies.", "Productivity is not driven the same way in every culture: high power-distance cultures respond better to clear top-down direction, collectivist cultures respond better to team-based rewards, high uncertainty-avoidance cultures respond better to clear rules and job security, and individualist cultures respond better to individual recognition and performance-based pay."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("The unit closes by examining cross-cultural communication specifically, and how organisations "
            "manage diversity &mdash; turning differences in background and culture into a genuine source of "
            "organisational strength.")
notes = """
<h3>5.1 Cross-Cultural Communication</h3>
<p>Cross-cultural communication is the exchange of information between people from different cultural backgrounds, where differences in language, norms and non-verbal cues can easily distort the intended meaning.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">High-Context vs Low-Context Cultures</h4>
<table class="compare">
<tr><th>Culture Type</th><th>Communication Style</th></tr>
<tr><td><strong>High-Context</strong></td><td>Much of the meaning is implicit, relying on shared context, relationships and non-verbal cues (common in many Asian, Middle Eastern and Latin American cultures).</td></tr>
<tr><td><strong>Low-Context</strong></td><td>Meaning is conveyed explicitly and directly through words themselves (common in many Western, especially North American and Northern European, cultures).</td></tr>
</table>

<h3>5.2 Barriers to Cross-Cultural Communication</h3>
<ul>
<li><strong>Language Differences:</strong> Direct translation issues and loss of nuance between languages.</li>
<li><strong>Differing Non-Verbal Cues:</strong> Gestures, eye contact and personal space norms vary and can be misread.</li>
<li><strong>Ethnocentrism:</strong> Judging another culture's communication style by the standards of one's own culture.</li>
<li><strong>Stereotyping:</strong> Assuming all members of a culture communicate identically, ignoring individual variation.</li>
</ul>

<h3>5.3 Improving Cross-Cultural Communication</h3>
<ul>
<li>Learning about the communication norms of the cultures one works with regularly.</li>
<li>Using clear, simple language and confirming understanding through feedback.</li>
<li>Being patient and observant, especially around non-verbal cues.</li>
<li>Avoiding idioms, slang and culturally specific references that may not translate well.</li>
</ul>

<h3>5.4 Management of Diversity</h3>
<p>Managing diversity is the deliberate process of creating an organisational environment where employees of different backgrounds &mdash; gender, ethnicity, age, nationality, ability and more &mdash; can all contribute and succeed.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Benefits of Managing Diversity Well</h4>
<ul>
<li>Brings a wider range of perspectives, supporting better problem-solving and innovation.</li>
<li>Improves an organisation's understanding of diverse customer markets.</li>
<li>Strengthens the organisation's ability to attract and retain talent from the widest possible pool.</li>
<li>Can improve organisational reputation and compliance with equal-opportunity expectations.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Challenges in Managing Diversity</h4>
<ul>
<li>Potential for misunderstanding or conflict arising from cultural differences if not well managed.</li>
<li>Risk of unconscious bias affecting hiring, evaluation and promotion decisions.</li>
<li>Need for sustained training and policy, since diversity initiatives often fail if treated as a one-time effort.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Strategies for Managing Diversity Effectively</h4>
<ul>
<li>Diversity and inclusion training for all employees, including leadership.</li>
<li>Fair, bias-aware recruitment, evaluation and promotion practices.</li>
<li>Employee resource groups that support specific communities within the organisation.</li>
<li>Leadership accountability for diversity outcomes, not just stated intentions.</li>
</ul>
"""
terms = [
    ("Cross-Cultural Communication", "The exchange of information between people from different cultural backgrounds, where language, norms and non-verbal cues can distort meaning."),
    ("High-Context Culture", "A culture where much communicated meaning is implicit, relying on shared context and non-verbal cues."),
    ("Low-Context Culture", "A culture where meaning is conveyed explicitly and directly through words themselves."),
    ("Managing Diversity", "The deliberate process of creating an organisational environment where employees of different backgrounds can all contribute and succeed."),
]
examprep = [
    "High-Context cultures rely on implicit meaning/shared context; Low-Context cultures rely on explicit, direct wording.",
    "Barriers to cross-cultural communication: language differences, differing non-verbal cues, ethnocentrism, stereotyping.",
    "Managing diversity = creating an environment where employees of all backgrounds can contribute and succeed; benefits: perspectives, market understanding, talent pool, reputation.",
    "Diversity strategies: training, bias-aware HR practices, employee resource groups, leadership accountability.",
]
questions = [
    ("Differentiate between high-context and low-context cultures.", "High-context cultures convey much of their meaning implicitly, relying on shared context, relationships and non-verbal cues. Low-context cultures convey meaning explicitly and directly through the words used, with less reliance on unstated context."),
    ("What are the barriers to cross-cultural communication?", "Language differences and translation loss, differing non-verbal cues (gestures, eye contact, personal space), ethnocentrism (judging other cultures by one's own standards), and stereotyping (assuming uniform communication style within a culture)."),
    ("What is meant by managing diversity? Explain its benefits.", "Managing diversity is the deliberate process of creating an environment where employees of different backgrounds can all contribute and succeed. Its benefits include wider perspectives for problem-solving and innovation, better understanding of diverse markets, access to a wider talent pool, and improved organisational reputation."),
    ("What strategies help an organisation manage diversity effectively?", "Diversity and inclusion training for all employees including leadership, fair and bias-aware recruitment/evaluation/promotion practices, employee resource groups supporting specific communities, and holding leadership accountable for diversity outcomes."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Five topics covering emerging aspects of organisational behaviour: comparative management styles and Japanese management practices, organisational creativity and innovation, OB across cultures, managing international workforce, and cross-cultural communication/managing diversity.")

print("Unit 5 (Management Concepts and OB) complete: all 5 topics + index written.")
