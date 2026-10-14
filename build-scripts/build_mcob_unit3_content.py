# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Management-Concepts-and-Organisational-Behavior\units"
BOOK_HTML = "Book: <em>Management Concepts and Organisational Behaviour</em> (BA4102, Anna University MBA Sem I)"
BOOK_PLAIN = "Management Concepts and Organisational Behaviour (BA4102)"

TOPICS = [
    ("topic1-introduction-to-ob.html", "Introduction to Organisational Behaviour"),
    ("topic2-perception-and-learning.html", "Perception and Learning"),
    ("topic3-personality-and-individual-differences.html", "Personality and Individual Differences"),
    ("topic4-attitudes-values-beliefs.html", "Attitudes, Values and Beliefs"),
    ("topic5-motivation-theories-job-performance.html", "Motivation Theories and Job Performance"),
    ("topic6-communication.html", "Communication: Types, Process and Barriers"),
]

AMBER_THEME = dict(accent="#a1591f", accent_dark="#6b3a14", accent_light="#f7ebdd",
                    border="#e8d7c3", shadow="rgba(161,89,31,.14)")

U = common.UnitBuilder(3, "Individual Behaviour", TOPICS,
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
overview = ("This opening topic of Unit 3 defines Organisational Behaviour (OB), the disciplines it draws "
            "from, and why understanding how individuals behave at work matters for managers.")
notes = """
<h3>1.1 Meaning and Definition of Organisational Behaviour</h3>
<p>Organisational Behaviour (OB) is the systematic study of the actions and attitudes of individuals and groups within an organisation, and how that behaviour affects the organisation's performance. It examines behaviour at three levels: the individual, the group, and the organisation as a whole.</p>

<h3>1.2 Nature of Organisational Behaviour</h3>
<ul>
<li><strong>A Field of Study:</strong> OB is a distinct field of study, not a discipline in the formal, established sense, since it draws heavily on other disciplines.</li>
<li><strong>Interdisciplinary:</strong> It applies knowledge from psychology, sociology, social psychology, anthropology and political science to workplace behaviour.</li>
<li><strong>Applied Science:</strong> OB knowledge is applied to solve real organisational and managerial problems.</li>
<li><strong>Normative and Value-Centred:</strong> OB offers explanations of how things are, and also judgements about how to improve workplace outcomes for both people and the organisation.</li>
<li><strong>Human-Centred:</strong> Its core concern is understanding, predicting and influencing human behaviour at work.</li>
</ul>

<h3>1.3 Contributing Disciplines of Organisational Behaviour</h3>
<table class="compare">
<tr><th>Discipline</th><th>Contribution to OB</th></tr>
<tr><td><strong>Psychology</strong></td><td>Understanding individual behaviour &mdash; learning, motivation, personality, perception, attitudes, job satisfaction, decision-making, and training.</td></tr>
<tr><td><strong>Sociology</strong></td><td>Understanding group behaviour within organisations &mdash; group dynamics, organisational culture, formal organisation theory, and organisational change.</td></tr>
<tr><td><strong>Social Psychology</strong></td><td>Blending psychology and sociology to study how individuals influence and are influenced by groups &mdash; attitude change, communication patterns, and group decision-making.</td></tr>
<tr><td><strong>Anthropology</strong></td><td>Studying the influence of culture and the environment on the values, attitudes and behaviour of people across societies, relevant to comparative and cross-cultural management.</td></tr>
<tr><td><strong>Political Science</strong></td><td>Studying the behaviour of individuals and groups in a political environment &mdash; power, conflict, and organisational politics.</td></tr>
</table>

<h3>1.4 Importance of Organisational Behaviour</h3>
<ul>
<li>Helps managers understand why employees behave the way they do, enabling better people-management decisions.</li>
<li>Improves a manager's ability to predict, explain and influence behaviour toward organisational goals.</li>
<li>Supports better leadership, motivation, communication and conflict-resolution practices.</li>
<li>Helps build a more positive organisational climate and culture, improving both performance and employee well-being.</li>
</ul>

<h3>1.5 Levels of Analysis in OB</h3>
<table class="compare">
<tr><th>Level</th><th>Focus</th></tr>
<tr><td><strong>Individual Level</strong></td><td>Perception, learning, personality, attitudes, values, motivation and individual decision-making.</td></tr>
<tr><td><strong>Group Level</strong></td><td>Group dynamics, teams, leadership, power and politics, conflict and communication within and between groups.</td></tr>
<tr><td><strong>Organisational Level</strong></td><td>Organisational structure, culture, change and development, and how the organisation as a whole functions.</td></tr>
</table>
"""
terms = [
    ("Organisational Behaviour (OB)", "The systematic study of the actions and attitudes of individuals and groups within an organisation, and their effect on organisational performance."),
    ("Social Psychology", "A discipline blending psychology and sociology, studying how individuals influence and are influenced by groups."),
    ("Levels of Analysis in OB", "The individual, group, and organisational levels at which organisational behaviour is studied."),
]
examprep = [
    "OB = systematic study of individual/group actions and attitudes within an organisation and their effect on performance.",
    "5 contributing disciplines: Psychology (individual behaviour), Sociology (group behaviour), Social Psychology (individual-group interaction), Anthropology (culture), Political Science (power/politics).",
    "3 levels of OB analysis: Individual, Group, Organisational.",
]
questions = [
    ("Define Organisational Behaviour. Explain its nature.", "OB is the systematic study of the actions and attitudes of individuals and groups within an organisation and how that behaviour affects performance. Its nature: it is an interdisciplinary field of study, an applied science, both normative and value-centred, and fundamentally human-centred."),
    ("Explain the disciplines that contribute to Organisational Behaviour.", "Psychology contributes understanding of individual behaviour (learning, motivation, personality); Sociology contributes understanding of group behaviour and organisational structure; Social Psychology studies how individuals and groups influence each other; Anthropology studies the influence of culture on behaviour; and Political Science studies power, conflict and politics within organisations."),
    ("Why is the study of OB important to a manager?", "It helps managers understand why employees behave as they do, improves their ability to predict and influence behaviour toward organisational goals, supports better leadership, motivation and conflict resolution, and helps build a more positive organisational climate."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("Perception and learning are two fundamental psychological processes that shape how employees "
            "interpret their workplace and how their behaviour changes with experience over time.")
notes = """
<h3>2.1 Meaning and Definition of Perception</h3>
<p>Perception is the process by which individuals select, organise and interpret sensory information to give meaning to their environment. Two people can perceive the same event very differently, because perception is shaped by the perceiver, not just by the raw stimulus itself.</p>

<h3>2.2 The Perceptual Process</h3>
<ol>
<li><strong>Receiving Stimuli:</strong> The senses receive raw information from the environment.</li>
<li><strong>Selecting:</strong> The individual selectively attends to some stimuli and ignores others.</li>
<li><strong>Organising:</strong> The selected information is organised into a meaningful pattern.</li>
<li><strong>Interpreting:</strong> Meaning is assigned to the organised information, based on the individual's own experience and expectations.</li>
<li><strong>Responding:</strong> The individual reacts based on their interpretation.</li>
</ol>

<h3>2.3 Factors Influencing Perception</h3>
<table class="compare">
<tr><th>Category</th><th>Factors</th></tr>
<tr><td><strong>Characteristics of the Perceiver</strong></td><td>Attitudes, motives, interests, past experience, and expectations.</td></tr>
<tr><td><strong>Characteristics of the Target</strong></td><td>Novelty, motion, sounds, size, and other attributes of the thing being perceived.</td></tr>
<tr><td><strong>Characteristics of the Situation</strong></td><td>Time, work setting, and social context in which the perception occurs.</td></tr>
</table>

<h3>2.4 Perceptual Errors and Distortions</h3>
<ul>
<li><strong>Stereotyping:</strong> Judging someone based on the perception of the group they belong to, rather than their individual characteristics.</li>
<li><strong>Halo Effect:</strong> Forming an overall impression of a person based on a single trait.</li>
<li><strong>Selective Perception:</strong> Interpreting what is seen selectively, based on the perceiver's own interests, background and attitudes.</li>
<li><strong>Projection:</strong> Attributing one's own characteristics or feelings to other people.</li>
<li><strong>Contrast Effect:</strong> Evaluating a person's characteristics in comparison to other people recently encountered, rather than on their own merits.</li>
</ul>

<h3>2.5 Meaning and Definition of Learning</h3>
<p>Learning is any relatively permanent change in behaviour that occurs as a result of experience or practice.</p>

<h3>2.6 The Learning Process and Theories</h3>
<table class="compare">
<tr><th>Theory</th><th>Core Idea</th></tr>
<tr><td><strong>Classical Conditioning</strong> (Pavlov)</td><td>A conditioned stimulus is paired with an unconditioned stimulus until the conditioned stimulus alone triggers the response.</td></tr>
<tr><td><strong>Operant Conditioning</strong> (Skinner)</td><td>Behaviour is a function of its consequences &mdash; behaviour followed by a pleasant consequence (reinforcement) is more likely to be repeated.</td></tr>
<tr><td><strong>Social Learning Theory</strong> (Bandura)</td><td>People learn by observing and imitating the behaviour of others (role models), not only through their own direct experience.</td></tr>
</table>

<h3>2.7 Characteristics of Learning</h3>
<ul>
<li>Learning involves change in behaviour, for better or worse.</li>
<li>The change must be relatively permanent, distinguishing true learning from temporary fluctuations (e.g. fatigue).</li>
<li>Learning occurs through experience, practice, or training.</li>
<li>Learning can be shown through actual or potential behaviour change.</li>
</ul>
"""
terms = [
    ("Perception", "The process by which individuals select, organise and interpret sensory information to give meaning to their environment."),
    ("Halo Effect", "A perceptual error in which an overall impression of a person is formed based on a single trait."),
    ("Stereotyping", "Judging a person based on the perception of the group they belong to, rather than their own individual characteristics."),
    ("Learning", "Any relatively permanent change in behaviour that occurs as a result of experience or practice."),
    ("Operant Conditioning", "A learning theory holding that behaviour is a function of its consequences, with reinforced behaviour more likely to be repeated."),
]
examprep = [
    "Perceptual process: Receiving Stimuli &rarr; Selecting &rarr; Organising &rarr; Interpreting &rarr; Responding.",
    "Factors influencing perception: Perceiver's characteristics, Target's characteristics, Situation's characteristics.",
    "Perceptual errors: Stereotyping, Halo Effect, Selective Perception, Projection, Contrast Effect.",
    "Learning = relatively permanent behaviour change from experience; theories: Classical Conditioning (Pavlov), Operant Conditioning (Skinner), Social Learning Theory (Bandura).",
]
questions = [
    ("Define perception. Explain the perceptual process.", "Perception is the process of selecting, organising and interpreting sensory information to give meaning to the environment. The process runs: receiving stimuli, selectively attending to some of them, organising the selected information, interpreting it based on personal experience, and responding."),
    ("Explain the factors influencing perception.", "Factors related to the perceiver (attitudes, motives, past experience), factors related to the target being perceived (novelty, size, motion), and factors related to the situation (time, setting, social context)."),
    ("Explain common perceptual errors with examples.", "Stereotyping judges someone by their group rather than individually; the Halo Effect forms a whole impression from one trait; Selective Perception interprets information based on one's own interests; Projection attributes one's own feelings to others; and the Contrast Effect judges someone relative to others recently encountered."),
    ("Define learning. Explain any two theories of learning.", "Learning is any relatively permanent change in behaviour resulting from experience. Classical Conditioning (Pavlov) pairs a conditioned stimulus with an unconditioned stimulus until it alone triggers a response. Operant Conditioning (Skinner) holds that behaviour followed by a pleasant consequence is more likely to be repeated."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("Personality shapes how each employee characteristically thinks, feels and behaves. This topic "
            "covers what determines personality, the major theories used to describe it, and why individual "
            "differences matter for managing people at work.")
notes = """
<h3>3.1 Meaning and Definition of Personality</h3>
<p>Personality is the relatively stable set of psychological characteristics and behavioural tendencies that make a person's pattern of responses to situations distinct from other people.</p>

<h3>3.2 Determinants of Personality</h3>
<table class="compare">
<tr><th>Factor</th><th>Influence</th></tr>
<tr><td><strong>Heredity</strong></td><td>Genetic factors inherited from parents, influencing physical traits and some behavioural tendencies.</td></tr>
<tr><td><strong>Environment</strong></td><td>Culture, family upbringing, social norms and life experiences that shape personality over time.</td></tr>
<tr><td><strong>Situation</strong></td><td>The specific context a person is in, which can bring out different aspects of their personality.</td></tr>
</table>

<h3>3.3 Theories of Personality</h3>
<ol>
<li><strong>Trait Theory:</strong> Describes personality as a combination of measurable traits (the "Big Five": Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism) that remain relatively stable across situations.</li>
<li><strong>Psychoanalytic Theory (Freud):</strong> Views personality as shaped by unconscious drives, structured into the Id (instinctual desires), Ego (rational mediator), and Superego (internalised moral standards).</li>
<li><strong>Humanistic Theory (Maslow, Rogers):</strong> Emphasises personal growth, self-actualisation and the individual's inherent drive toward realising their full potential.</li>
<li><strong>Social-Cognitive Theory (Bandura):</strong> Views personality as developing through the continuous interaction between a person, their behaviour, and their environment.</li>
</ol>

<h3>3.4 Personality Traits Relevant to Work</h3>
<ul>
<li><strong>Locus of Control:</strong> The degree to which people believe they control events affecting them (internal) versus believe outside forces are in control (external).</li>
<li><strong>Self-Esteem:</strong> The degree to which individuals like or dislike themselves, affecting confidence and risk-taking at work.</li>
<li><strong>Self-Monitoring:</strong> The ability to adjust one's behaviour to external, situational factors.</li>
<li><strong>Risk-Taking Propensity:</strong> How willing a person is to take chances, relevant to decision speed and quality.</li>
</ul>

<h3>3.5 Individual Differences</h3>
<p>Individual differences refer to the ways people vary from one another &mdash; in ability, personality, values, perception and motivation &mdash; and why no single management style works equally well for everyone.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Why Individual Differences Matter</h4>
<ul>
<li>They explain why employees respond differently to the same job, leadership style, or incentive.</li>
<li>They help managers match people to roles that suit their particular strengths.</li>
<li>They highlight the need for flexible, individualised approaches to motivation and development.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Individual Differences Influencing Work Behaviour</h4>
<ul>
<li><strong>Ability:</strong> Intellectual and physical capacity to perform tasks.</li>
<li><strong>Personality:</strong> Stable traits affecting how a person approaches work and relationships.</li>
<li><strong>Perception:</strong> How a person interprets their job, colleagues and feedback.</li>
<li><strong>Values and Attitudes:</strong> What a person considers important, shaping their motivation and job satisfaction.</li>
</ul>
"""
terms = [
    ("Personality", "The relatively stable set of psychological characteristics and behavioural tendencies that distinguish one person's pattern of responses from another's."),
    ("Big Five Personality Traits", "A trait-theory model of personality: Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism."),
    ("Locus of Control", "The degree to which a person believes they (internal) or outside forces (external) control the events that affect them."),
    ("Individual Differences", "The ways people vary from one another in ability, personality, values, perception and motivation."),
]
examprep = [
    "Personality determinants: Heredity, Environment, Situation.",
    "Personality theories: Trait (Big Five), Psychoanalytic (Freud's Id/Ego/Superego), Humanistic (Maslow/Rogers), Social-Cognitive (Bandura).",
    "Work-relevant traits: Locus of Control, Self-Esteem, Self-Monitoring, Risk-Taking Propensity.",
    "Individual differences (ability, personality, perception, values) explain why the same job/style affects different employees differently.",
]
questions = [
    ("Define personality. Explain its determinants.", "Personality is the relatively stable set of psychological characteristics that make a person's responses distinct from others'. It is determined by heredity (genetic inheritance), environment (culture, upbringing, experience), and the specific situation a person is in."),
    ("Explain any two theories of personality.", "Trait Theory describes personality through measurable, stable traits such as the Big Five (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism). Psychoanalytic Theory (Freud) views personality as shaped by unconscious drives structured into the Id, Ego and Superego."),
    ("What is meant by individual differences? Why are they important at work?", "Individual differences are the ways people vary in ability, personality, values, perception and motivation. They matter because they explain why employees respond differently to the same job or leadership style, helping managers match people to suitable roles and adopt more flexible management approaches."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("Attitudes, values and beliefs together shape how employees evaluate their work and workplace, "
            "and ultimately influence their behaviour, satisfaction and performance.")
notes = """
<h3>4.1 Meaning and Definition of Attitude</h3>
<p>An attitude is a relatively stable evaluative statement or judgement &mdash; favourable or unfavourable &mdash; about a person, object or event.</p>

<h3>4.2 Components of Attitude</h3>
<table class="compare">
<tr><th>Component</th><th>Description</th></tr>
<tr><td><strong>Cognitive Component</strong></td><td>The beliefs, opinions and knowledge a person holds about the attitude object.</td></tr>
<tr><td><strong>Affective Component</strong></td><td>The emotional or feeling part of an attitude &mdash; how the person feels about the object.</td></tr>
<tr><td><strong>Behavioural Component</strong></td><td>The intention to behave in a particular way toward the attitude object.</td></tr>
</table>

<h3>4.3 Formation of Attitudes</h3>
<ul>
<li><strong>Direct Experience:</strong> Attitudes often form from personal interactions and experiences.</li>
<li><strong>Social Learning:</strong> Attitudes are learned from family, peers, teachers and other role models.</li>
<li><strong>Classical/Operant Conditioning:</strong> Attitudes can be shaped through association and reinforcement, similar to learned behaviours.</li>
</ul>

<h3>4.4 Attitude and Behaviour at Work</h3>
<p>Key work-related attitudes include <strong>Job Satisfaction</strong> (a positive feeling about one's job resulting from an evaluation of its characteristics), <strong>Job Involvement</strong> (the degree of psychological identification with one's job), and <strong>Organisational Commitment</strong> (identifying with and wanting to remain part of a particular organisation). Positive work attitudes are generally associated with lower absenteeism and turnover, and better citizenship behaviour.</p>

<h3>4.5 Meaning and Definition of Values</h3>
<p>Values are broad, enduring beliefs about what is important and desirable, guiding a person's judgement of right and wrong across situations. Unlike attitudes, which are more specific and situational, values are more general and stable over a lifetime.</p>

<h3>4.6 Sources and Types of Values</h3>
<ul>
<li><strong>Sources:</strong> Family upbringing, culture, religion, education and significant life experiences.</li>
<li><strong>Terminal Values:</strong> Desirable end-states of existence, the goals a person would like to achieve in their lifetime (e.g. a comfortable life, wisdom, self-respect).</li>
<li><strong>Instrumental Values:</strong> Preferable modes of behaviour, or the means of achieving the terminal values (e.g. honesty, ambition, responsibility).</li>
</ul>

<h3>4.7 Importance of Values</h3>
<ul>
<li>Shape a person's perception of what is fair, good and right at work.</li>
<li>Influence motivation and the kinds of rewards an employee finds meaningful.</li>
<li>Underlie organisational culture when shared widely across the workforce.</li>
</ul>

<h3>4.8 Beliefs</h3>
<p>A belief is a conviction about the truth of something, often formed without complete objective evidence. In the workplace, beliefs shape how employees interpret events and the trust (or distrust) they place in management's intentions.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Relationship Between Attitude and Belief</h4>
<p>Beliefs form the cognitive foundation on which attitudes are built &mdash; what a person believes to be true about something strongly shapes how favourably or unfavourably they come to feel about it.</p>
"""
terms = [
    ("Attitude", "A relatively stable evaluative statement or judgement, favourable or unfavourable, about a person, object or event."),
    ("Job Satisfaction", "A positive feeling about one's job resulting from an evaluation of its characteristics."),
    ("Values", "Broad, enduring beliefs about what is important and desirable, guiding judgements of right and wrong."),
    ("Terminal Values", "Desirable end-states of existence that a person wants to achieve in their lifetime."),
    ("Instrumental Values", "Preferable modes of behaviour that serve as the means of achieving terminal values."),
]
examprep = [
    "Attitude = stable evaluative judgement; 3 components: Cognitive (belief), Affective (feeling), Behavioural (intention to act).",
    "Attitude formation: direct experience, social learning, conditioning.",
    "Key work attitudes: Job Satisfaction, Job Involvement, Organisational Commitment.",
    "Values = broad enduring beliefs about what is desirable; Terminal Values (end-states) vs Instrumental Values (means/behaviours).",
    "Beliefs form the cognitive basis on which attitudes are built.",
]
questions = [
    ("Define attitude. Explain its components.", "An attitude is a relatively stable evaluative judgement about a person, object or event. It has three components: Cognitive (the beliefs held about the object), Affective (the feelings toward it), and Behavioural (the intention to act toward it)."),
    ("How are attitudes formed? Explain their relevance to work behaviour.", "Attitudes form through direct experience, social learning from role models, and conditioning/association. At work, attitudes such as job satisfaction, job involvement and organisational commitment influence absenteeism, turnover and citizenship behaviour."),
    ("Define values. Differentiate between terminal and instrumental values.", "Values are broad, enduring beliefs about what is important and desirable. Terminal values are the desirable end-states a person wants to achieve (e.g. a comfortable life), while instrumental values are the preferred modes of behaviour used to achieve those end-states (e.g. honesty, ambition)."),
    ("What is the relationship between beliefs and attitudes?", "Beliefs are convictions about the truth of something, and they form the cognitive foundation on which attitudes are built &mdash; what a person believes to be true about an object strongly shapes how favourably or unfavourably they come to feel about it."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("Motivation explains why employees put in effort at work. This topic covers the meaning and "
            "elements of motivation, the major content and process theories, and how motivation links to "
            "job performance.")
notes = """
<h3>5.1 Meaning and Definition of Motivation</h3>
<p>Motivation is the set of forces that initiate, direct and sustain effort toward achieving a goal. At work, it is what drives an employee to put in effort toward organisational objectives.</p>

<h3>5.2 Nature and Elements of Motivation</h3>
<ul>
<li><strong>Intensity:</strong> How much effort a person puts in.</li>
<li><strong>Direction:</strong> Whether that effort is channelled toward the organisation's goals.</li>
<li><strong>Persistence:</strong> How long a person sustains that effort.</li>
</ul>
<p>Motivation is internal to the individual (it cannot be directly observed, only inferred from behaviour), goal-directed, and varies in strength both between people and within the same person over time.</p>

<h3>5.3 Importance of Motivation</h3>
<ul>
<li>Higher motivation is generally associated with higher productivity and quality of work.</li>
<li>Improves employee satisfaction, reducing absenteeism and turnover.</li>
<li>Encourages initiative, creativity and willingness to go beyond the minimum required.</li>
</ul>

<h3>5.4 Content Theories of Motivation</h3>
<table class="compare">
<tr><th>Theory</th><th>Core Idea</th></tr>
<tr><td><strong>Maslow's Need Hierarchy Theory</strong></td><td>Needs are arranged in a hierarchy &mdash; Physiological, Safety, Social, Esteem, Self-Actualisation &mdash; and a satisfied lower need stops motivating, pushing the person toward the next level up.</td></tr>
<tr><td><strong>Herzberg's Two-Factor Theory</strong></td><td>Distinguishes Hygiene Factors (pay, working conditions &mdash; prevent dissatisfaction but don't motivate) from Motivators (achievement, recognition, growth &mdash; create genuine satisfaction and motivation).</td></tr>
<tr><td><strong>McClelland's Needs Theory</strong></td><td>People are driven by three learned needs in varying degrees: Need for Achievement (nAch), Need for Power (nPow), and Need for Affiliation (nAff).</td></tr>
<tr><td><strong>Alderfer's ERG Theory</strong></td><td>Condenses Maslow's hierarchy into three needs &mdash; Existence, Relatedness, Growth &mdash; and allows more than one need to be active at once, unlike Maslow's strict hierarchy.</td></tr>
</table>

<h3>5.5 Process Theories of Motivation</h3>
<table class="compare">
<tr><th>Theory</th><th>Core Idea</th></tr>
<tr><td><strong>McGregor's Theory X and Theory Y</strong></td><td>Theory X assumes employees are inherently lazy and need close control; Theory Y assumes employees are self-motivated and seek responsibility &mdash; a manager's assumptions shape their management style.</td></tr>
<tr><td><strong>Vroom's Expectancy Theory</strong></td><td>Motivation depends on three beliefs multiplied together: Expectancy (effort leads to performance), Instrumentality (performance leads to reward), and Valence (the reward is valued).</td></tr>
<tr><td><strong>Porter and Lawler Model</strong></td><td>Extends expectancy theory, showing that performance leads to both intrinsic and extrinsic rewards, which, filtered through perceived fairness, determine satisfaction.</td></tr>
</table>

<h3>5.6 Motivation and Job Performance</h3>
<p>Job performance is generally understood as a function of <strong>Ability &times; Motivation &times; Opportunity</strong> &mdash; even a highly skilled employee will underperform if they lack motivation, and even a highly motivated employee needs the right ability and opportunity to translate effort into results. This is why management practice pairs motivation theory with training (building ability) and well-designed jobs and resources (providing opportunity).</p>
"""
terms = [
    ("Motivation", "The set of internal forces that initiate, direct and sustain effort toward achieving a goal."),
    ("Maslow's Need Hierarchy", "A theory arranging human needs in five levels &mdash; Physiological, Safety, Social, Esteem, Self-Actualisation &mdash; with satisfied lower needs ceasing to motivate."),
    ("Herzberg's Two-Factor Theory", "A motivation theory distinguishing Hygiene Factors (prevent dissatisfaction) from Motivators (create genuine satisfaction)."),
    ("Vroom's Expectancy Theory", "A theory holding that motivation depends on Expectancy, Instrumentality and Valence multiplied together."),
    ("Theory X and Theory Y", "McGregor's contrasting sets of managerial assumptions about employees &mdash; inherently lazy (X) versus self-motivated (Y)."),
]
examprep = [
    "Motivation = internal forces that initiate, direct and sustain effort; elements: Intensity, Direction, Persistence.",
    "Content theories: Maslow's Need Hierarchy, Herzberg's Two-Factor Theory, McClelland's Needs Theory (nAch/nPow/nAff), Alderfer's ERG Theory.",
    "Process theories: McGregor's Theory X/Y, Vroom's Expectancy Theory, Porter and Lawler Model.",
    "Job Performance = f(Ability x Motivation x Opportunity).",
]
questions = [
    ("Define motivation. Explain its elements.", "Motivation is the set of internal forces that initiate, direct and sustain effort toward a goal. Its elements are Intensity (how much effort), Direction (whether effort targets the right goals), and Persistence (how long the effort is sustained)."),
    ("Explain Maslow's Need Hierarchy Theory.", "Maslow arranged human needs into five levels &mdash; Physiological, Safety, Social, Esteem, and Self-Actualisation. Once a lower-level need is satisfied, it stops motivating behaviour, and the individual is driven to satisfy the next level up."),
    ("Explain Herzberg's Two-Factor Theory.", "Herzberg distinguished Hygiene Factors (pay, working conditions, policies) which prevent dissatisfaction but don't motivate, from Motivators (achievement, recognition, growth) which create genuine satisfaction and drive motivation."),
    ("Explain Vroom's Expectancy Theory.", "Motivation is the product of three beliefs: Expectancy (that effort will lead to performance), Instrumentality (that performance will lead to a reward), and Valence (that the reward is personally valued). If any factor is zero, motivation is zero."),
    ("How is job performance related to motivation?", "Job performance is commonly expressed as a function of Ability, Motivation, and Opportunity (Performance = f(Ability x Motivation x Opportunity)) &mdash; a skilled but unmotivated employee, or a motivated but unskilled one, will both underperform, showing that all three elements must be present together."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("Communication is the thread that connects every other OB topic in this unit. This closing topic "
            "covers the communication process, its types, the barriers that distort it, and how to make "
            "communication more effective.")
notes = """
<h3>6.1 Meaning and Definition of Communication</h3>
<p>Communication is the process of transmitting information and understanding from one person or group to another, so that the meaning intended by the sender is accurately received and understood by the receiver.</p>

<h3>6.2 Importance of Communication</h3>
<ul>
<li>Coordinates the efforts of individuals and departments toward common goals.</li>
<li>Enables managers to plan, organise, direct and control effectively.</li>
<li>Builds trust and relationships between management and employees.</li>
<li>Supports better, more informed decision-making.</li>
</ul>

<h3>6.3 Process of Communication</h3>
<ol>
<li><strong>Sender:</strong> The person who originates and wants to share a message.</li>
<li><strong>Encoding:</strong> Converting the idea into words, symbols, or gestures.</li>
<li><strong>Message:</strong> The actual content being communicated.</li>
<li><strong>Channel/Medium:</strong> The method used to transmit the message (spoken, written, electronic).</li>
<li><strong>Receiver:</strong> The person who receives the message.</li>
<li><strong>Decoding:</strong> The receiver interpreting the message to extract meaning.</li>
<li><strong>Feedback:</strong> The receiver's response, confirming whether the message was understood as intended.</li>
<li><strong>Noise:</strong> Anything that distorts the message at any stage of the process.</li>
</ol>

<h3>6.4 Types of Communication</h3>
<table class="compare">
<tr><th>Basis</th><th>Types</th></tr>
<tr><td>Mode</td><td><strong>Verbal</strong> (spoken or written words) vs <strong>Non-Verbal</strong> (body language, tone, facial expressions).</td></tr>
<tr><td>Direction</td><td><strong>Downward</strong> (manager to subordinate), <strong>Upward</strong> (subordinate to manager), <strong>Horizontal</strong> (between peers), and <strong>Diagonal</strong> (across levels and departments).</td></tr>
<tr><td>Formality</td><td><strong>Formal</strong> (through official organisational channels) vs <strong>Informal</strong> (through the grapevine).</td></tr>
</table>

<h3>6.5 Barriers to Effective Communication</h3>
<ul>
<li><strong>Semantic Barriers:</strong> Words or symbols meaning different things to different people, causing misunderstanding.</li>
<li><strong>Psychological Barriers:</strong> Emotional states, prejudice, or distrust that distort how a message is received.</li>
<li><strong>Organisational Barriers:</strong> Long hierarchies, unclear authority, or information overload within a large structure.</li>
<li><strong>Physical/Mechanical Barriers:</strong> Noise, distance, or faulty equipment that disrupts transmission.</li>
<li><strong>Cultural Barriers:</strong> Differences in language, norms and non-verbal cues across cultures.</li>
</ul>

<h3>6.6 Techniques to Overcome Barriers to Communication</h3>
<ul>
<li>Use clear, simple language appropriate to the receiver.</li>
<li>Actively seek and use feedback to confirm the message was understood.</li>
<li>Choose the most appropriate channel for the message and the audience.</li>
<li>Practise active listening rather than merely hearing.</li>
<li>Be sensitive to the receiver's emotional state and cultural background.</li>
<li>Follow up important messages in writing to reduce ambiguity.</li>
</ul>
"""
terms = [
    ("Communication", "The process of transmitting information and understanding from a sender to a receiver so the intended meaning is accurately received."),
    ("Encoding", "Converting an idea into words, symbols or gestures to be communicated."),
    ("Noise (Communication)", "Anything that distorts a message at any stage of the communication process."),
    ("Semantic Barrier", "A communication barrier arising when words or symbols mean different things to different people."),
    ("Grapevine", "The informal channel through which information flows outside official organisational communication channels."),
]
examprep = [
    "Communication process: Sender &rarr; Encoding &rarr; Message &rarr; Channel &rarr; Receiver &rarr; Decoding &rarr; Feedback, with Noise able to distort any stage.",
    "Types of communication: Verbal/Non-Verbal; Downward/Upward/Horizontal/Diagonal; Formal/Informal (grapevine).",
    "Barriers: Semantic, Psychological, Organisational, Physical/Mechanical, Cultural.",
    "Overcoming barriers: clear language, seeking feedback, choosing the right channel, active listening, cultural sensitivity, written follow-up.",
]
questions = [
    ("Explain the process of communication.", "Communication flows from a Sender, who encodes an idea into a Message, sent through a Channel to a Receiver, who decodes it and provides Feedback confirming understanding &mdash; with Noise able to distort the message at any stage."),
    ("Explain the types of communication.", "By mode: Verbal (spoken/written) and Non-Verbal (body language, tone). By direction: Downward, Upward, Horizontal and Diagonal. By formality: Formal (official channels) and Informal (the grapevine)."),
    ("What are the barriers to effective communication?", "Semantic barriers (words meaning different things to different people), Psychological barriers (emotions, prejudice, distrust), Organisational barriers (long hierarchies, information overload), Physical/Mechanical barriers (noise, distance, faulty equipment), and Cultural barriers (differences in language and norms)."),
    ("Suggest techniques for making communication effective.", "Use clear and simple language, actively seek feedback, choose the channel best suited to the message and audience, practise active listening, be sensitive to the receiver's emotional and cultural context, and follow up important messages in writing."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Six topics covering individual behaviour: introduction to OB and its contributing disciplines, perception and learning, personality and individual differences, attitudes/values/beliefs, motivation theories and job performance, and communication.")

print("Unit 3 (Management Concepts and OB) complete: all 6 topics + index written.")
