# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Management-Concepts-and-Organisational-Behavior\units"
BOOK_HTML = "Book: <em>Management Concepts and Organisational Behaviour</em> (BA4102, Anna University MBA Sem I)"
BOOK_PLAIN = "Management Concepts and Organisational Behaviour (BA4102)"

TOPICS = [
    ("topic1-groups-and-teams.html", "Groups and Teams: Definition, Difference and Types"),
    ("topic2-group-development-cohesiveness-dynamics.html", "Stages of Group Development, Cohesiveness and Dynamics"),
    ("topic3-organisational-climate-and-culture.html", "Organisational Climate and Culture"),
    ("topic4-leadership-styles-power-politics.html", "Leadership: Styles, Approaches, Power and Politics"),
    ("topic5-conflict-management.html", "Conflict: Concept, Sources, Types and Management"),
    ("topic6-organisational-change-and-development.html", "Organisational Change and Development"),
]

AMBER_THEME = dict(accent="#a1591f", accent_dark="#6b3a14", accent_light="#f7ebdd",
                    border="#e8d7c3", shadow="rgba(161,89,31,.14)")

U = common.UnitBuilder(4, "Group Behaviour", TOPICS,
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
overview = ("Unit 4 shifts focus from the individual to the group. This opening topic defines what a group "
            "and a team are, how they differ, and the various types of teams found in organisations.")
notes = """
<h3>1.1 Meaning and Definition of a Group</h3>
<p>A group is two or more individuals, interacting and interdependent, who have come together to achieve particular objectives.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Groups</h4>
<ul>
<li><strong>Formal Groups:</strong> Deliberately created by the organisation to perform specific tasks (e.g. a department, a project committee).</li>
<li><strong>Informal Groups:</strong> Formed naturally by members for social or psychological reasons, not officially structured by the organisation.</li>
<li><strong>Command Group:</strong> A formal group defined by the organisation chart, consisting of a manager and their direct subordinates.</li>
<li><strong>Task Group:</strong> A formal group of people working together to complete a specific job or project, which may cross reporting lines.</li>
<li><strong>Interest Group:</strong> An informal group that forms around members sharing a common interest or goal.</li>
<li><strong>Friendship Group:</strong> An informal group that forms because members share common characteristics or simply enjoy each other's company.</li>
</ul>

<h3>1.2 Meaning and Definition of a Team</h3>
<p>A team is a small number of people with complementary skills who are committed to a common purpose, a set of performance goals, and an approach for which they hold themselves mutually accountable.</p>

<h3>1.3 Difference Between Groups and Teams</h3>
<table class="compare">
<tr><th>Basis</th><th>Group</th><th>Team</th></tr>
<tr><td>Goal</td><td>Share information, members have individual goals</td><td>Collective performance, shared common goals</td></tr>
<tr><td>Accountability</td><td>Individual accountability</td><td>Individual and mutual accountability</td></tr>
<tr><td>Skills</td><td>May be random or overlapping</td><td>Complementary skills, deliberately combined</td></tr>
<tr><td>Synergy</td><td>Neutral, sometimes negative</td><td>Positive synergy &mdash; the whole exceeds the sum of individual efforts</td></tr>
<tr><td>Leadership</td><td>Often a single strong leader</td><td>Shared or rotating leadership roles</td></tr>
</table>

<h3>1.4 Types of Teams</h3>
<ol>
<li><strong>Problem-Solving Teams:</strong> Employees from the same department meeting to discuss ways to improve quality, efficiency or the work environment.</li>
<li><strong>Self-Managed (Self-Directed) Teams:</strong> Teams that operate without a manager and take on traditional managerial responsibilities such as planning and scheduling their own work.</li>
<li><strong>Cross-Functional Teams:</strong> Teams made up of employees from different departments working together on a common task.</li>
<li><strong>Virtual Teams:</strong> Teams that use technology to work together despite being physically dispersed, communicating across distance.</li>
<li><strong>Project Teams:</strong> Temporary teams assembled for the duration of a specific project and disbanded once it is complete.</li>
</ol>
"""
terms = [
    ("Group", "Two or more individuals, interacting and interdependent, who come together to achieve particular objectives."),
    ("Team", "A small number of people with complementary skills, committed to a common purpose and goals, holding themselves mutually accountable."),
    ("Self-Managed Team", "A team that operates without a manager, taking on traditional managerial responsibilities such as planning its own work."),
    ("Cross-Functional Team", "A team made up of employees from different departments, working together on a common task."),
]
examprep = [
    "Group = 2+ interacting, interdependent individuals pursuing objectives; types: Formal (Command, Task) and Informal (Interest, Friendship).",
    "Team = small group with complementary skills, common purpose, mutual accountability, and positive synergy.",
    "Group vs Team: individual goals/accountability vs collective goals/mutual accountability; neutral synergy vs positive synergy.",
    "Types of teams: Problem-Solving, Self-Managed, Cross-Functional, Virtual, Project.",
]
questions = [
    ("Define a group. Explain its types.", "A group is two or more interacting, interdependent individuals who come together to achieve particular objectives. Formal groups (Command groups defined by the org chart, Task groups formed for a specific job) are deliberately created by the organisation, while Informal groups (Interest groups, Friendship groups) form naturally for social reasons."),
    ("Differentiate between a group and a team.", "A group's members often pursue individual goals with individual accountability and neutral synergy, while a team shares a common goal, holds mutual accountability, combines complementary skills deliberately, and produces positive synergy where the collective output exceeds the sum of individual efforts."),
    ("Explain the various types of teams found in organisations.", "Problem-Solving Teams discuss improvements within a department; Self-Managed Teams operate without a manager, handling their own planning; Cross-Functional Teams bring together people from different departments; Virtual Teams use technology to collaborate across distance; and Project Teams are temporary, assembled for a specific project's duration."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("Groups don't function effectively from the moment they are formed &mdash; they develop through "
            "predictable stages. This topic covers that development process, what makes a group cohesive, "
            "and the dynamics that shape how a group actually behaves.")
notes = """
<h3>2.1 Stages of Group Development (Bruce Tuckman)</h3>
<ol>
<li><strong>Forming:</strong> Members get to know each other, testing boundaries and establishing ground rules; characterised by uncertainty about the group's purpose and structure.</li>
<li><strong>Storming:</strong> Conflict emerges as members resist the constraints the group places on their individuality, and disagreements surface over leadership and direction.</li>
<li><strong>Norming:</strong> The group develops close relationships, cohesiveness increases, and norms for acceptable behaviour emerge and are accepted.</li>
<li><strong>Performing:</strong> The group structure is fully functional and accepted; energy has moved from getting to know one another to actually performing the task.</li>
<li><strong>Adjourning:</strong> For temporary groups/teams, this final stage involves wrapping up activities and disbanding, rather than high performance.</li>
</ol>
<p>Not every group experiences these stages in strict sequence &mdash; some move back and forth between storming and norming as new challenges or members arise.</p>

<h3>2.2 Group Cohesiveness</h3>
<p>Group cohesiveness is the degree to which members are attracted to the group and motivated to remain part of it.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Factors Affecting Cohesiveness</h4>
<ul>
<li>Time spent together and shared experiences.</li>
<li>Severity of initiation into the group.</li>
<li>Group size (smaller groups tend to be more cohesive).</li>
<li>External threats, which often increase internal cohesiveness.</li>
<li>Past success, which reinforces members' desire to stay in the group.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Consequences of Cohesiveness</h4>
<p>Highly cohesive groups with goals aligned to the organisation's goals tend to be more productive. However, a highly cohesive group whose goals are not aligned with the organisation's goals can actually become less productive, since the group's energy is directed away from organisational objectives. Excessive cohesiveness can also lead to <strong>groupthink</strong> &mdash; a tendency to suppress dissenting views in favour of consensus and harmony.</p>

<h3>2.3 Group Dynamics</h3>
<p>Group dynamics refers to the pattern of interactions, processes and forces operating within and between groups &mdash; how members influence and are influenced by each other, including roles, norms, status, and communication patterns.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Elements of Group Dynamics</h4>
<ul>
<li><strong>Roles:</strong> The set of expected behaviour patterns attributed to a particular position within the group.</li>
<li><strong>Norms:</strong> The acceptable standards of behaviour shared by group members.</li>
<li><strong>Status:</strong> The socially defined position or rank given to a group or its members by others.</li>
<li><strong>Group Size:</strong> Affects overall group behaviour &mdash; larger groups are good for gathering diverse input, smaller groups for taking action quickly.</li>
<li><strong>Group Composition:</strong> The mix of skills, backgrounds and characteristics among members, which affects group performance.</li>
</ul>
"""
terms = [
    ("Tuckman's Five Stages", "The stages of group development: Forming, Storming, Norming, Performing, and Adjourning."),
    ("Group Cohesiveness", "The degree to which members are attracted to a group and motivated to remain part of it."),
    ("Groupthink", "A tendency within a highly cohesive group to suppress dissenting views in favour of consensus and harmony."),
    ("Group Dynamics", "The pattern of interactions, processes and forces operating within and between groups."),
    ("Norms", "The acceptable standards of behaviour that are shared and enforced by members of a group."),
]
examprep = [
    "Tuckman's 5 stages: Forming &rarr; Storming &rarr; Norming &rarr; Performing &rarr; Adjourning.",
    "Group cohesiveness = attraction to and motivation to remain in a group; factors: time together, initiation severity, size, external threats, past success.",
    "Highly cohesive + goals aligned with organisation = high productivity; highly cohesive + misaligned goals = can reduce productivity; excess cohesiveness risks groupthink.",
    "Group dynamics elements: Roles, Norms, Status, Group Size, Group Composition.",
]
questions = [
    ("Explain the stages of group development.", "Forming (members get acquainted, uncertain about purpose), Storming (conflict over leadership and direction), Norming (cohesiveness builds, norms accepted), Performing (fully functional, task-focused), and Adjourning (wrapping up and disbanding, for temporary groups)."),
    ("What is group cohesiveness? What factors affect it?", "Group cohesiveness is the degree to which members are attracted to the group and motivated to stay in it. It is affected by time spent together, the severity of initiation, group size, external threats, and the group's past success."),
    ("What is groupthink? Why is it a risk?", "Groupthink is the tendency within a highly cohesive group to suppress dissenting opinions in favour of consensus and harmony. It is a risk because it can lead to poor decisions, since alternative viewpoints and critical evaluation are discouraged."),
    ("Explain the key elements of group dynamics.", "Roles (expected behaviour patterns for a position), Norms (shared standards of acceptable behaviour), Status (socially defined rank within the group), Group Size, and Group Composition (the mix of skills and backgrounds among members)."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("Organisational climate and culture together shape how things are done in a workplace, "
            "influencing everything from employee morale to strategic execution.")
notes = """
<h3>3.1 Meaning and Definition of Organisational Climate</h3>
<p>Organisational climate is employees' shared perception of the work environment &mdash; how it feels to work in the organisation at a given point in time. It reflects relatively short-term, surface-level conditions such as morale, communication quality, and management style.</p>

<h3>3.2 Dimensions of Organisational Climate</h3>
<ul>
<li><strong>Structure:</strong> The degree of formality, rules and red tape employees perceive.</li>
<li><strong>Responsibility:</strong> The degree of autonomy employees feel they have.</li>
<li><strong>Reward:</strong> How fairly employees feel they are recognised and compensated.</li>
<li><strong>Warmth and Support:</strong> The perceived friendliness and helpfulness among colleagues and from management.</li>
<li><strong>Conflict:</strong> How openly disagreements are expressed and resolved.</li>
</ul>

<h3>3.3 Meaning and Definition of Organisational Culture</h3>
<p>Organisational culture is the shared system of values, beliefs, assumptions and norms that governs how members of an organisation think, feel and behave. Unlike climate, culture is deeper, more stable, and develops over a much longer period.</p>

<h3>3.4 Characteristics of Organisational Culture</h3>
<ul>
<li><strong>Shared:</strong> Held in common by most members of the organisation.</li>
<li><strong>Learned:</strong> Transmitted to new members through socialisation.</li>
<li><strong>Stable:</strong> Resistant to change once established.</li>
<li><strong>Implicit:</strong> Often operates below conscious awareness, guiding behaviour without members realising it.</li>
</ul>

<h3>3.5 Difference Between Climate and Culture</h3>
<table class="compare">
<tr><th>Basis</th><th>Organisational Climate</th><th>Organisational Culture</th></tr>
<tr><td>Nature</td><td>Surface-level, perceptual</td><td>Deep-rooted, foundational</td></tr>
<tr><td>Stability</td><td>Relatively short-term, can shift quickly</td><td>Long-term, changes slowly</td></tr>
<tr><td>Measurement</td><td>Measured through employee perception surveys</td><td>Inferred from shared values, stories, rituals and artefacts</td></tr>
<tr><td>Scope</td><td>Can vary across departments within one culture</td><td>Usually more uniform across the whole organisation</td></tr>
</table>

<h3>3.6 Factors Affecting Organisational Climate and Culture</h3>
<ul>
<li>Leadership style and the example set by top management.</li>
<li>Organisational structure and the degree of formalisation.</li>
<li>Communication practices and transparency.</li>
<li>Reward and recognition systems.</li>
<li>The organisation's founding history and the values of its founders.</li>
</ul>

<h3>3.7 Building and Maintaining a Positive Climate and Culture</h3>
<ul>
<li>Leaders modelling the desired values consistently in their own behaviour.</li>
<li>Recognising and rewarding behaviour consistent with the desired culture.</li>
<li>Communicating openly and regularly with employees at every level.</li>
<li>Using onboarding and training to socialise new members into the culture.</li>
</ul>
"""
terms = [
    ("Organisational Climate", "Employees' shared perception of the work environment at a given point in time &mdash; a relatively short-term, surface-level condition."),
    ("Organisational Culture", "The shared system of values, beliefs, assumptions and norms that governs how members of an organisation think, feel and behave."),
]
examprep = [
    "Climate = shared perception of the work environment (surface-level, short-term); Culture = shared values/beliefs/norms (deep, long-term).",
    "Climate dimensions: Structure, Responsibility, Reward, Warmth/Support, Conflict.",
    "Culture characteristics: Shared, Learned, Stable, Implicit.",
    "Climate vs Culture: short-term/surveyed vs long-term/inferred from values and artefacts.",
]
questions = [
    ("Define organisational climate. What are its dimensions?", "Organisational climate is employees' shared perception of their work environment at a given time. Its dimensions include Structure, Responsibility, Reward, Warmth and Support, and Conflict."),
    ("Define organisational culture. Explain its characteristics.", "Organisational culture is the shared system of values, beliefs, assumptions and norms governing how members think, feel and behave. It is shared across members, learned through socialisation, stable over time, and often implicit, operating below conscious awareness."),
    ("Differentiate between organisational climate and culture.", "Climate is a surface-level, short-term perception of the work environment that can vary across departments, while culture is a deep-rooted, long-term, usually organisation-wide system of shared values and beliefs that is harder and slower to change."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("Leadership determines how well a group's or team's efforts are directed, while power and "
            "politics describe the underlying currents that shape influence within an organisation. This "
            "topic covers all three together.")
notes = """
<h3>4.1 Meaning and Definition of Leadership</h3>
<p>Leadership is the ability to influence a group toward the achievement of a vision or set of goals.</p>

<h3>4.2 Leadership Styles</h3>
<table class="compare">
<tr><th>Style</th><th>Description</th></tr>
<tr><td><strong>Autocratic</strong></td><td>The leader makes decisions unilaterally, with little input from subordinates.</td></tr>
<tr><td><strong>Democratic (Participative)</strong></td><td>The leader involves subordinates in decision-making, seeking their input before deciding.</td></tr>
<tr><td><strong>Laissez-Faire (Free-Rein)</strong></td><td>The leader gives subordinates near-complete freedom to make decisions and complete work on their own.</td></tr>
<tr><td><strong>Transactional</strong></td><td>The leader motivates through a system of rewards and punishments tied to performance.</td></tr>
<tr><td><strong>Transformational</strong></td><td>The leader inspires and motivates followers by appealing to a shared vision, higher ideals and values, encouraging followers to exceed their own self-interest for the group.</td></tr>
</table>

<h3>4.3 Approaches/Theories to Leadership</h3>
<ol>
<li><strong>Trait Theory:</strong> Early approach assuming effective leaders possess certain inborn personal traits (intelligence, confidence, integrity).</li>
<li><strong>Behavioural Theory:</strong> Focuses on what leaders actually do &mdash; their observable behaviour &mdash; rather than their traits (e.g. task-oriented vs people-oriented behaviour).</li>
<li><strong>Contingency/Situational Theory:</strong> Holds that the most effective leadership style depends on the specific situation &mdash; the task, the followers, and the environment.</li>
<li><strong>Transformational/Charismatic Theory:</strong> Focuses on leaders who inspire extraordinary commitment and performance by connecting followers to a compelling vision.</li>
</ol>

<h3>4.4 Power</h3>
<p>Power is the capacity to influence the behaviour of others so that they act in accordance with one's wishes.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Sources/Bases of Power (French and Raven)</h4>
<ul>
<li><strong>Legitimate Power:</strong> Derived from a person's formal position or role in the organisation.</li>
<li><strong>Reward Power:</strong> Derived from the ability to give valued rewards to others.</li>
<li><strong>Coercive Power:</strong> Derived from the ability to punish or withhold something of value.</li>
<li><strong>Expert Power:</strong> Derived from specialised knowledge or skill that others need.</li>
<li><strong>Referent Power:</strong> Derived from being liked, admired, or respected by others.</li>
</ul>

<h3>4.5 Organisational Politics</h3>
<p>Organisational politics refers to activities carried out to acquire, develop and use power and other resources to obtain one's preferred outcomes in situations where there is uncertainty or disagreement. It is not inherently negative &mdash; it becomes problematic mainly when it is used purely for self-interest at the expense of organisational goals.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Why Organisational Politics Occurs</h4>
<ul>
<li>Limited resources that different individuals or departments compete for.</li>
<li>Ambiguous goals or unclear performance criteria that leave room for interpretation and influence.</li>
<li>Organisational change, which creates uncertainty and opportunities to gain or lose influence.</li>
<li>Differences in values, goals and perspectives across departments and individuals.</li>
</ul>
"""
terms = [
    ("Leadership", "The ability to influence a group toward the achievement of a vision or set of goals."),
    ("Transformational Leadership", "A leadership style that inspires followers by appealing to a shared vision and higher ideals, encouraging them to exceed their own self-interest."),
    ("Power", "The capacity to influence the behaviour of others so that they act in accordance with one's wishes."),
    ("Legitimate Power", "Power derived from a person's formal position or role within the organisation."),
    ("Organisational Politics", "Activities carried out to acquire and use power to obtain preferred outcomes in situations of uncertainty or disagreement."),
]
examprep = [
    "Leadership styles: Autocratic, Democratic/Participative, Laissez-Faire, Transactional, Transformational.",
    "Leadership approaches: Trait Theory, Behavioural Theory, Contingency/Situational Theory, Transformational/Charismatic Theory.",
    "5 bases of power (French and Raven): Legitimate, Reward, Coercive, Expert, Referent.",
    "Organisational politics occurs due to limited resources, ambiguous goals, organisational change, and differing values &mdash; not inherently negative.",
]
questions = [
    ("Explain the various styles of leadership.", "Autocratic (unilateral decisions), Democratic/Participative (involves subordinates), Laissez-Faire (gives subordinates freedom), Transactional (motivates through rewards/punishment), and Transformational (inspires through vision and higher ideals)."),
    ("Explain the approaches to the study of leadership.", "Trait Theory looks at inborn personal traits of effective leaders; Behavioural Theory looks at what leaders actually do; Contingency/Situational Theory holds that the best style depends on the situation; and Transformational/Charismatic Theory focuses on leaders who inspire extraordinary commitment through a compelling vision."),
    ("Explain the bases of power identified by French and Raven.", "Legitimate Power from formal position, Reward Power from the ability to give rewards, Coercive Power from the ability to punish, Expert Power from specialised knowledge, and Referent Power from being liked or admired by others."),
    ("What is organisational politics? Why does it occur?", "Organisational politics is the use of power and resources to obtain preferred outcomes amid uncertainty or disagreement. It occurs due to limited resources, ambiguous goals, organisational change, and differing values and perspectives across the organisation; it is not inherently negative unless used purely for self-interest."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("Wherever people and groups with different goals interact, conflict is inevitable. This topic "
            "covers what conflict is, where it comes from, its types and levels, and how it can be managed "
            "constructively.")
notes = """
<h3>5.1 Concept and Meaning of Conflict</h3>
<p>Conflict is a process that begins when one party perceives that another party has negatively affected, or is about to negatively affect, something the first party cares about.</p>

<h3>5.2 Sources of Conflict</h3>
<ul>
<li><strong>Communication Factors:</strong> Misunderstandings, semantic difficulties, and insufficient information exchange.</li>
<li><strong>Structural Factors:</strong> Competition for limited resources, interdependence between departments, and ambiguous jurisdictions.</li>
<li><strong>Personal Factors:</strong> Differences in values, personality clashes, and individual goals that differ from others'.</li>
</ul>

<h3>5.3 Types/Levels of Conflict</h3>
<table class="compare">
<tr><th>Level</th><th>Description</th></tr>
<tr><td><strong>Intrapersonal Conflict</strong></td><td>Conflict within a single individual, often due to competing goals or roles.</td></tr>
<tr><td><strong>Interpersonal Conflict</strong></td><td>Conflict between two or more individuals.</td></tr>
<tr><td><strong>Intragroup Conflict</strong></td><td>Conflict among members within the same group or team.</td></tr>
<tr><td><strong>Intergroup Conflict</strong></td><td>Conflict between two or more groups or departments.</td></tr>
<tr><td><strong>Organisational Conflict</strong></td><td>Conflict that is broader and involves multiple groups across the organisation, often over policy or strategic direction.</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Functional vs Dysfunctional Conflict</h4>
<p><strong>Functional conflict</strong> supports the group's goals and improves performance, for example by surfacing better ideas through healthy debate. <strong>Dysfunctional conflict</strong> hinders group performance, for example by damaging relationships or distracting from the task at hand.</p>

<h3>5.4 The Conflict Process</h3>
<ol>
<li><strong>Potential Opposition/Incompatibility:</strong> The underlying conditions (communication, structure, personal factors) that create the possibility for conflict.</li>
<li><strong>Cognition and Personalisation:</strong> One or both parties become aware of and emotionally invested in the conflict.</li>
<li><strong>Intentions:</strong> The parties decide how to respond &mdash; competing, collaborating, compromising, avoiding, or accommodating.</li>
<li><strong>Behaviour:</strong> The conflict becomes visible through statements, actions and reactions.</li>
<li><strong>Outcomes:</strong> The conflict is resolved (or not), producing functional or dysfunctional results for the group.</li>
</ol>

<h3>5.5 Management of Conflict</h3>
<table class="compare">
<tr><th>Style</th><th>When Appropriate</th></tr>
<tr><td><strong>Competing</strong></td><td>Quick, decisive action is needed, or on important issues where unpopular action must be taken.</td></tr>
<tr><td><strong>Collaborating</strong></td><td>Both parties' concerns are too important to compromise; aims for a win-win solution.</td></tr>
<tr><td><strong>Compromising</strong></td><td>Goals are moderately important but not worth the disruption of more assertive approaches.</td></tr>
<tr><td><strong>Avoiding</strong></td><td>The issue is trivial, or more information is needed before acting.</td></tr>
<tr><td><strong>Accommodating</strong></td><td>Preserving harmony matters more than the issue itself, or when one realises they are wrong.</td></tr>
</table>
"""
terms = [
    ("Conflict", "A process that begins when one party perceives that another party has negatively affected, or is about to affect, something the first party cares about."),
    ("Functional Conflict", "Conflict that supports a group's goals and improves its performance."),
    ("Dysfunctional Conflict", "Conflict that hinders a group's performance, for instance by damaging relationships or distracting from the task."),
    ("Intergroup Conflict", "Conflict occurring between two or more groups or departments within an organisation."),
]
examprep = [
    "Conflict = process beginning when one party perceives another has negatively affected something they care about.",
    "Sources: Communication factors, Structural factors (limited resources, interdependence), Personal factors (values, personality).",
    "Levels: Intrapersonal, Interpersonal, Intragroup, Intergroup, Organisational.",
    "Conflict process: Potential Opposition &rarr; Cognition/Personalisation &rarr; Intentions &rarr; Behaviour &rarr; Outcomes.",
    "5 conflict-handling styles: Competing, Collaborating, Compromising, Avoiding, Accommodating.",
]
questions = [
    ("What is conflict? Explain its sources.", "Conflict is a process beginning when one party perceives another has negatively affected something they care about. Its sources include communication factors (misunderstandings), structural factors (competition for resources, interdependence), and personal factors (differing values and personalities)."),
    ("Explain the levels/types of conflict.", "Intrapersonal (within an individual), Interpersonal (between individuals), Intragroup (within a group), Intergroup (between groups), and Organisational (broader, involving multiple groups over policy or strategy)."),
    ("Differentiate between functional and dysfunctional conflict.", "Functional conflict supports a group's goals and improves performance, for example through healthy debate that surfaces better ideas. Dysfunctional conflict hinders performance, for example by damaging relationships or distracting the group from its task."),
    ("Explain the styles of conflict management.", "Competing suits urgent, important issues needing quick action; Collaborating seeks a win-win when both parties' concerns matter; Compromising suits moderately important goals; Avoiding suits trivial issues or when more information is needed; and Accommodating suits situations where preserving harmony matters more than winning the point."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("This closing topic of Unit 4 covers how organisations deliberately manage change, and the "
            "broader discipline of Organisational Development (OD) used to build an organisation's long-term "
            "capacity to adapt.")
notes = """
<h3>6.1 Meaning and Definition of Organisational Change</h3>
<p>Organisational change is any alteration in people, structure, or technology within an organisation, undertaken to improve its effectiveness or adapt to a changing environment.</p>

<h3>6.2 Forces for Change</h3>
<ul>
<li><strong>External Forces:</strong> Changes in technology, market competition, government regulation, and economic conditions.</li>
<li><strong>Internal Forces:</strong> Changes in organisational strategy, workforce composition, employee attitudes, and new equipment or processes.</li>
</ul>

<h3>6.3 Lewin's Three-Step Model of Change</h3>
<ol>
<li><strong>Unfreezing:</strong> Preparing the organisation for change by overcoming resistance and individual/group inertia in the current state.</li>
<li><strong>Changing (Moving):</strong> Actually implementing the change &mdash; moving the organisation toward the desired new state.</li>
<li><strong>Refreezing:</strong> Stabilising the new state by reinforcing the new behaviours, so the change becomes the new normal rather than reverting.</li>
</ol>

<h3>6.4 Resistance to Change</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Why People Resist Change</h4>
<ul>
<li>Fear of the unknown and loss of job security.</li>
<li>Habit and comfort with established routines.</li>
<li>Concern over loss of status, power, or established relationships.</li>
<li>Lack of trust in management's reasons for the change.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Overcoming Resistance</h4>
<ul>
<li>Communicating openly about the reasons for and nature of the change.</li>
<li>Involving affected employees in planning and implementing the change.</li>
<li>Providing training and support to build confidence in new ways of working.</li>
<li>Negotiating and, where appropriate, offering incentives to ease the transition.</li>
</ul>

<h3>6.5 Organisational Development (OD)</h3>
<p>Organisational Development is a planned, systematic effort, supported by top management, that uses behavioural-science knowledge to improve an organisation's health and effectiveness through planned interventions in its processes.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Characteristics of OD</h4>
<ul>
<li>Planned and long-term, not a one-time quick fix.</li>
<li>Oriented toward the whole organisational system, not just isolated parts.</li>
<li>Relies on collaboration between change agents and organisation members.</li>
<li>Draws on behavioural science theory and research.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Common OD Interventions</h4>
<ul>
<li><strong>Survey Feedback:</strong> Collecting employee attitude data and feeding it back to work groups to diagnose and solve problems.</li>
<li><strong>Team Building:</strong> Activities to improve trust, openness and collaboration within work teams.</li>
<li><strong>Process Consultation:</strong> An outside consultant helps managers perceive and understand the process events happening around them.</li>
<li><strong>Sensitivity Training:</strong> Unstructured group sessions aimed at increasing members' insight into their own and others' behaviour.</li>
</ul>
"""
terms = [
    ("Organisational Change", "Any alteration in an organisation's people, structure, or technology, undertaken to improve effectiveness or adapt to the environment."),
    ("Lewin's Three-Step Model", "A change model consisting of Unfreezing (preparing for change), Changing (implementing it), and Refreezing (stabilising the new state)."),
    ("Organisational Development (OD)", "A planned, systematic, top-management-supported effort using behavioural-science knowledge to improve organisational health and effectiveness."),
    ("Survey Feedback", "An OD intervention that collects employee attitude data and feeds it back to work groups to diagnose and solve problems."),
]
examprep = [
    "Organisational change = alteration in people/structure/technology to improve effectiveness or adapt to environment; forces: External (tech, market, regulation) and Internal (strategy, workforce, process).",
    "Lewin's 3-step model: Unfreezing &rarr; Changing (Moving) &rarr; Refreezing.",
    "Resistance to change: fear of unknown, habit, loss of status/power, lack of trust; overcome via communication, involvement, training, negotiation.",
    "OD = planned, systematic, top-management-supported, whole-system, behavioural-science-based effort; interventions: Survey Feedback, Team Building, Process Consultation, Sensitivity Training.",
]
questions = [
    ("Explain Lewin's three-step model of change.", "Unfreezing prepares the organisation by overcoming resistance and inertia in the current state; Changing (Moving) implements the actual change toward the desired new state; Refreezing stabilises the new state by reinforcing new behaviours so the change sticks."),
    ("Why do employees resist change? How can resistance be overcome?", "Employees resist change due to fear of the unknown, comfort with habit, concern over losing status or power, and lack of trust in management. Resistance can be reduced through open communication, involving employees in the change process, providing training and support, and negotiating or offering incentives."),
    ("What is Organisational Development (OD)? Explain its characteristics.", "OD is a planned, systematic effort supported by top management, using behavioural-science knowledge to improve organisational effectiveness. It is long-term rather than a quick fix, focused on the whole system, collaborative between change agents and members, and grounded in behavioural science."),
    ("Explain any two OD interventions.", "Survey Feedback collects employee attitude data and feeds it back to work groups to diagnose and solve problems. Team Building uses structured activities to improve trust, openness and collaboration within a work team."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Six topics covering group behaviour: groups and teams, stages of group development/cohesiveness/dynamics, organisational climate and culture, leadership/power/politics, conflict management, and organisational change and development.")

print("Unit 4 (Management Concepts and OB) complete: all 6 topics + index written.")
