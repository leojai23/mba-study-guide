# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Management-Concepts-and-Organisational-Behavior\units"
BOOK_HTML = "Book: <em>Management Concepts and Organisational Behaviour</em> (BA4102, Anna University MBA Sem I)"
BOOK_PLAIN = "Management Concepts and Organisational Behaviour (BA4102)"

TOPICS = [
    ("topic1-meaning-nature-functions-roles.html", "Management: Meaning, Nature, Functions and Roles"),
    ("topic2-evolution-of-management-thought.html", "Evolution of Management Thought"),
    ("topic3-taylor-scientific-management.html", "Classical Era &mdash; F.W. Taylor's Scientific Management"),
    ("topic4-fayol-weber-administrative-management.html", "Classical Era &mdash; Fayol's Administrative Management &amp; Weber's Bureaucracy"),
    ("topic5-mayo-hawthorne-experiments.html", "Neo-Classical Era &mdash; Mayo &amp; the Hawthorne Experiments"),
    ("topic6-systems-contingency-approach.html", "Modern Era &mdash; Systems and Contingency Approach"),
]

AMBER_THEME = dict(accent="#a1591f", accent_dark="#6b3a14", accent_light="#f7ebdd",
                    border="#e8d7c3", shadow="rgba(161,89,31,.14)")

U = common.UnitBuilder(1, "Nature and Theories of Management", TOPICS,
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
overview = ("This opening topic defines management itself &mdash; what it means, why it is considered both a "
            "science and an art, the levels at which it operates, and the functions and roles every manager "
            "performs regardless of level.")
notes = """
<h3>1.1 Meaning and Definition of Management</h3>
<p>Management is the process of getting things done through and with people, by directing and coordinating the efforts of a group toward common goals, using the available resources effectively and efficiently.</p>
<table class="compare">
<tr><th>Thinker</th><th>Definition</th></tr>
<tr><td><strong>Koontz and O'Donnel</strong></td><td>Management is the creation and maintenance of an internal environment in an enterprise where individuals, working in groups, can perform efficiently and effectively toward the attainment of group goals.</td></tr>
<tr><td><strong>James D. Mooney and Allan C. Reiley</strong></td><td>Management is the art of directing and inspiring people.</td></tr>
<tr><td><strong>Peter Drucker</strong></td><td>Management is a multipurpose organ that manages a business, manages managers, and manages workers and work.</td></tr>
<tr><td><strong>Louis Allen</strong></td><td>Management is what a manager does.</td></tr>
</table>

<h3>1.2 Nature of Management</h3>
<p>Management can be understood through the following characteristics:</p>
<ol>
<li><strong>Management is Universal:</strong> It applies to every kind of organisation &mdash; business, government, charitable or religious &mdash; wherever people work together toward a goal.</li>
<li><strong>Management is a Human Activity:</strong> It directs and coordinates the human and material resources of an organisation; without people, there is nothing to manage.</li>
<li><strong>Management is Goal-Oriented:</strong> Every managerial activity is carried out to achieve predetermined objectives.</li>
<li><strong>Management is a Continuous Process:</strong> It is a never-ending series of functions &mdash; planning, organising, staffing, directing and controlling &mdash; performed continuously, not once and for all.</li>
<li><strong>Management is a Career:</strong> It offers interesting, stimulating and lucrative career opportunities across functions like marketing, finance, HR, and operations.</li>
<li><strong>Management Denotes Authority:</strong> Authority and responsibility flow through every level of the organisational hierarchy, from top to bottom.</li>
<li><strong>Management is Dynamic:</strong> It must adapt to a constantly changing environment &mdash; markets, technology and people all change, and management adapts with them.</li>
<li><strong>Management is Primarily a Discipline/Profession:</strong> It requires specialised knowledge and training, though it is still evolving toward the formal status of a full profession.</li>
<li><strong>Management is a Science as well as an Art:</strong> It has a systematic body of knowledge (science) but also requires skilled, situational judgement in application (art).</li>
</ol>

<h3>1.3 Scope of Management</h3>
<p>Management as a discipline covers a wide range of activities and practices, broadly grouped under the functional areas of a business:</p>
<ul>
<li><strong>Production Management:</strong> Planning, organising and controlling production activities, machines and processes.</li>
<li><strong>Marketing Management:</strong> Deals with marketing mix components &mdash; product, pricing, promotion, warehousing, distribution channels, etc.</li>
<li><strong>Financial Management:</strong> Involves financial planning, budgeting, costing and statistical control.</li>
<li><strong>Personnel Management:</strong> Recruiting, training and developing employees, keeping records, and maintaining social welfare.</li>
<li><strong>Purchasing Management:</strong> Procurement of materials &mdash; inviting tenders, selecting vendors, negotiating and terminating contracts.</li>
<li><strong>Maintenance Management:</strong> Inspection and upkeep of plant, buildings and equipment.</li>
<li><strong>Office Management:</strong> Office layout, staffing, equipment and information flow.</li>
<li><strong>Development Management:</strong> Research and development to improve products, processes and methods.</li>
<li><strong>Management as an Inter-Disciplinary Approach:</strong> Management principles draw on economics, psychology, sociology and mathematics, making it a genuinely inter-disciplinary field of study and practice.</li>
</ul>

<h3>1.4 Functions of Management</h3>
<p>Henri Fayol identified five core functions that together form the management process:</p>
<ol>
<li><strong>Planning:</strong> Deciding in advance what is to be done, when, how and by whom &mdash; preparing objectives and the course of action to achieve them.</li>
<li><strong>Organising:</strong> Arranging resources (people, materials, equipment) and establishing authority relationships so the plan can be carried out efficiently.</li>
<li><strong>Staffing:</strong> Filling and keeping filled the positions in the organisation structure through recruitment, selection, training and development.</li>
<li><strong>Directing:</strong> Guiding, motivating and supervising subordinates so they work willingly and effectively toward organisational goals.</li>
<li><strong>Controlling:</strong> Measuring actual performance against planned performance and taking corrective action where deviations are found.</li>
</ol>
<p>Beyond these five, management also performs supporting functional activities: Financial Management, Purchasing Management, Personnel Management, Production Management, Maintenance Management, and Office Management.</p>

<h3>1.5 Managerial Roles (Henry Mintzberg)</h3>
<p>Mintzberg identified ten roles every manager plays, grouped into three categories:</p>
<table class="compare">
<tr><th>Category</th><th>Roles</th></tr>
<tr><td><strong>Interpersonal Roles</strong></td><td><strong>Figurehead</strong> &mdash; performs ceremonial/symbolic duties; <strong>Leader</strong> &mdash; motivates and directs subordinates; <strong>Liaison</strong> &mdash; maintains a network of outside contacts.</td></tr>
<tr><td><strong>Informational Roles</strong></td><td><strong>Monitor</strong> &mdash; collects information from inside and outside the organisation; <strong>Disseminator</strong> &mdash; shares information with subordinates; <strong>Spokesperson</strong> &mdash; shares information outside the organisation.</td></tr>
<tr><td><strong>Decisional Roles</strong></td><td><strong>Entrepreneur</strong> &mdash; initiates change and new projects; <strong>Disturbance Handler</strong> &mdash; resolves conflicts and unexpected problems; <strong>Resource Allocator</strong> &mdash; decides how resources are distributed; <strong>Negotiator</strong> &mdash; represents the organisation in negotiations.</td></tr>
</table>

<h3>1.6 Levels of Management</h3>
<table class="compare">
<tr><th>Level</th><th>Who</th><th>Primary Concern</th></tr>
<tr><td><strong>Top Management</strong></td><td>Board of Directors, CEO, General Managers</td><td>Setting overall objectives, policies and long-term direction &mdash; conceptual (thinking) skills matter most here.</td></tr>
<tr><td><strong>Middle Management</strong></td><td>Departmental/Divisional Heads</td><td>Translating top management's plans into departmental goals and coordinating lower-level work &mdash; needs a balance of all three skill types.</td></tr>
<tr><td><strong>Lower/Supervisory Management</strong></td><td>Foremen, Supervisors, Section Officers</td><td>Directly overseeing day-to-day operational work of the workforce &mdash; technical skills matter most here.</td></tr>
</table>

<h3>1.7 Management as an Art, Science and Profession</h3>
<ul>
<li><strong>As a Science:</strong> Management has a systematic body of knowledge, principles and techniques that can be taught and applied, and its outcomes can be tested and verified &mdash; though, unlike physical sciences, it deals with unpredictable human behaviour, so it is better described as a "soft" or social science.</li>
<li><strong>As an Art:</strong> Applying management knowledge skilfully to a specific, real-world situation requires creativity, judgement and personal skill &mdash; which is why two managers with the same knowledge can still get different results.</li>
<li><strong>As a Profession:</strong> Management is moving toward professional status &mdash; it requires specialised knowledge, formal education, and (increasingly) adherence to a code of conduct &mdash; though it still lacks the universal licensing/certification requirements of established professions like law or medicine.</li>
</ul>

<h3>1.8 Managerial Skills (Robert L. Katz)</h3>
<table class="compare">
<tr><th>Skill</th><th>Meaning</th><th>Most Important At</th></tr>
<tr><td><strong>Technical Skill</strong></td><td>Knowledge of and proficiency in a specific activity involving methods, processes and procedures.</td><td>Lower/Supervisory level</td></tr>
<tr><td><strong>Human Skill</strong></td><td>The ability to work with, understand and motivate other people, individually and in groups.</td><td>Equally important at every level</td></tr>
<tr><td><strong>Conceptual Skill</strong></td><td>The ability to see the organisation as a whole and understand how its parts interrelate.</td><td>Top level</td></tr>
</table>
"""
terms = [
    ("Management", "The process of getting things done through and with people by directing and coordinating group effort toward common goals, using resources efficiently and effectively."),
    ("Planning", "Deciding in advance what is to be done, when, how and by whom; the first function of management."),
    ("Mintzberg's Managerial Roles", "Ten roles every manager plays, grouped into Interpersonal, Informational and Decisional categories."),
    ("Conceptual Skill", "The ability to see the organisation as a whole and understand how its parts interrelate; most critical at top management level."),
    ("Levels of Management", "The hierarchy of Top, Middle and Lower (Supervisory) management, each with a different primary concern and skill mix."),
]
examprep = [
    "Management = getting things done through people, directing/coordinating group effort toward common goals.",
    "Nine traits of management's nature: Universal, Human Activity, Goal-Oriented, Continuous Process, Career, Denotes Authority, Dynamic, Discipline/Profession, Science as well as Art.",
    "Fayol's 5 functions: Planning, Organising, Staffing, Directing, Controlling.",
    "Mintzberg's 10 roles in 3 groups: Interpersonal (Figurehead, Leader, Liaison); Informational (Monitor, Disseminator, Spokesperson); Decisional (Entrepreneur, Disturbance Handler, Resource Allocator, Negotiator).",
    "3 levels of management: Top (conceptual skill), Middle (balanced skills), Lower/Supervisory (technical skill).",
    "Katz's 3 managerial skills: Technical, Human, Conceptual &mdash; human skill matters equally at every level.",
]
questions = [
    ("Define management. State any two definitions given by different thinkers.", "Management is the process of getting things done through and with people, directing and coordinating group effort toward common goals. Koontz and O'Donnel define it as the creation and maintenance of an internal environment where people working in groups can perform efficiently toward group goals; Peter Drucker calls it a multipurpose organ that manages a business, manages managers, and manages workers and work."),
    ("Explain the nature of management.", "Management is universal (applies to every kind of organisation), a human activity, goal-oriented, a continuous process, offers career opportunities, denotes authority flowing through the hierarchy, is dynamic (adapts to change), is primarily a discipline/profession, and is both a science (systematic body of knowledge) and an art (skilled application)."),
    ("Explain the functions of management as given by Henri Fayol.", "Planning (deciding in advance what to do), Organising (arranging resources and authority relationships), Staffing (filling positions through recruitment and training), Directing (guiding and motivating subordinates), and Controlling (measuring performance against plans and correcting deviations)."),
    ("Explain Mintzberg's managerial roles.", "Ten roles in three categories: Interpersonal (Figurehead, Leader, Liaison), Informational (Monitor, Disseminator, Spokesperson), and Decisional (Entrepreneur, Disturbance Handler, Resource Allocator, Negotiator)."),
    ("Describe the levels of management and the skills required at each.", "Top management sets overall objectives and needs conceptual skill; Middle management translates plans into departmental goals and needs a balance of technical, human and conceptual skill; Lower/Supervisory management oversees day-to-day operational work and needs technical skill most. Human skill matters equally at every level."),
    ("Is management a science, an art, or a profession? Explain.", "Management has elements of all three: it is a science because it has a systematic, testable body of knowledge; an art because applying that knowledge to a specific situation requires skill and judgement; and it is moving toward a profession because it increasingly requires specialised education, though it still lacks the universal licensing of established professions."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("Management thought has evolved through several competing schools of theory. This topic surveys "
            "how writers have classified these schools &mdash; famously described as a 'management theory "
            "jungle' &mdash; before the next topics examine the Classical, Neo-Classical and Modern eras in detail.")
notes = """
<h3>2.1 Why Management Thought Evolved</h3>
<p>As organisations grew larger and more complex through the Industrial Revolution and into the 20th century, thinkers from different backgrounds &mdash; engineers, sociologists, psychologists, and mathematicians &mdash; each approached the problem of managing people and work from their own discipline. This produced several distinct, sometimes competing, schools of management thought rather than one single theory.</p>

<h3>2.2 The Management Theory Jungle (Harold Koontz)</h3>
<p>Writing in the 1960s, Professor Harold Koontz observed that the proliferation of management theories had created a confusing "jungle" of overlapping schools of thought, each using different terms and definitions to describe similar ideas. He identified several schools, including:</p>
<ol>
<li><strong>The Management Process School:</strong> Views management as a universal process of planning, organising, staffing, directing and controlling, applicable to any kind of enterprise.</li>
<li><strong>The Empirical School:</strong> Studies management through the analysis of actual managerial experience and case studies, believing that lessons can be drawn from what successful managers have done.</li>
<li><strong>The Human Behaviour School:</strong> Focuses on interpersonal relationships, treating management essentially as getting things done through people, drawing heavily on psychology.</li>
<li><strong>The Social System School:</strong> Views the organisation as a system of cultural interrelationships, drawing on sociology to study how groups and individuals cooperate within it.</li>
<li><strong>The Decision Theory School:</strong> Centres on rational decision-making as the core of management, studying the process, techniques and people involved in making organisational decisions.</li>
<li><strong>The Mathematical School:</strong> Treats management as a system of mathematical models and processes, using quantitative techniques to represent and solve managerial problems.</li>
</ol>

<h3>2.3 Broad Classification of Approaches</h3>
<p>For practical purposes, these schools are usually grouped into three broad approaches, which also correspond to three historical eras of management theory:</p>
<table class="compare">
<tr><th>Approach</th><th>Core Idea</th><th>Key Contributors</th></tr>
<tr><td><strong>Classical Approach</strong></td><td>Focuses on structure, efficiency and formal principles of organising work.</td><td>F.W. Taylor (Scientific Management), Henri Fayol (Administrative Management), Max Weber (Bureaucracy)</td></tr>
<tr><td><strong>Behavioural (Neo-Classical) Approach</strong></td><td>Focuses on people &mdash; their needs, motivation and social behaviour at work.</td><td>Elton Mayo and the Hawthorne Experiments</td></tr>
<tr><td><strong>Management Science / Modern Approach</strong></td><td>Applies quantitative methods, systems thinking and situational analysis to management problems.</td><td>Systems Approach, Contingency Approach</td></tr>
</table>

<h3>2.4 Why This Classification Matters</h3>
<p>No single school fully explains management on its own &mdash; each contributes a partial but valuable lens. The Classical approach gives structure and efficiency, the Behavioural approach restores attention to people, and the Modern approaches add flexibility and rigour for dealing with complex, changing environments. The remaining topics in this unit examine each era's key contributions in turn.</p>
"""
terms = [
    ("Management Theory Jungle", "Harold Koontz's term for the confusing proliferation of overlapping management theories and schools of thought."),
    ("Management Process School", "Views management as a universal process built from the functions of planning, organising, staffing, directing and controlling."),
    ("Classical Approach", "An early school of management thought focused on structure, efficiency and formal principles of organising work."),
    ("Behavioural (Neo-Classical) Approach", "A school of management thought focused on people, their needs, motivation and social behaviour at work."),
]
examprep = [
    "Koontz's 'management theory jungle' identifies several overlapping schools: Management Process, Empirical, Human Behaviour, Social System, Decision Theory, Mathematical.",
    "Three broad approaches/eras: Classical (structure/efficiency: Taylor, Fayol, Weber), Behavioural/Neo-Classical (people: Mayo/Hawthorne), Modern (Systems &amp; Contingency).",
    "No single school is complete on its own; each contributes a partial but valuable lens on management.",
]
questions = [
    ("What did Harold Koontz mean by the 'management theory jungle'?", "He used the term to describe how, by the 1960s, so many overlapping schools of management thought had developed &mdash; each with its own terminology &mdash; that the field had become confusing to navigate, like a jungle."),
    ("List and briefly explain any three schools identified in the management theory jungle.", "The Management Process School views management as a universal process of planning, organising, staffing, directing and controlling. The Human Behaviour School focuses on interpersonal relationships and getting things done through people. The Decision Theory School centres on rational decision-making as the core of management."),
    ("What are the three broad approaches/eras of management thought?", "The Classical Approach (structure and efficiency, e.g. Taylor, Fayol, Weber), the Behavioural/Neo-Classical Approach (people and motivation, e.g. Mayo and the Hawthorne Experiments), and the Modern/Management Science Approach (systems and contingency thinking)."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("Frederick Winslow Taylor pioneered Scientific Management in the early 1900s, applying systematic, "
            "measured methods to work design in place of informal 'rule of thumb' practices. This topic covers "
            "his principles, techniques, and the system's strengths and criticisms.")
notes = """
<h3>3.1 Introduction to the Classical Era</h3>
<p>The Classical Era of management thought emerged during the Industrial Revolution, as factories grew large enough that informal, rule-of-thumb management could no longer coordinate work efficiently. Classical theorists sought systematic, formal principles for structuring work and organisations. F.W. Taylor's Scientific Management, developed from the early 1900s, was one of its first and most influential contributions.</p>

<h3>3.2 Principles of Scientific Management</h3>
<ol>
<li><strong>Science, Not Rule of Thumb:</strong> Replace informal, traditional "rule of thumb" work methods with methods developed through scientific study and measurement.</li>
<li><strong>Harmony in Group Action:</strong> Replace conflict between workers with harmony, achieved through cooperative study of the work rather than adversarial bargaining.</li>
<li><strong>Cooperation Between Workers and Management:</strong> Management and workers should cooperate closely to ensure work is carried out in line with the scientifically developed methods, rather than leaving workers to decide for themselves.</li>
<li><strong>Maximum Output in Place of Restricted Output:</strong> Both management and workers should aim to maximise output and productivity rather than deliberately restricting it.</li>
<li><strong>Development of Workers to the Fullest Extent:</strong> Select and train each worker scientifically for the job they are best suited to, and develop their skills to their fullest capacity.</li>
</ol>

<h3>3.3 Techniques of Scientific Management</h3>
<ol>
<li><strong>Time Study:</strong> Observing and timing a worker's movements for a specific task to determine the standard time required to complete it at a fair pace.</li>
<li><strong>Motion Study:</strong> Breaking a job down into its basic elementary movements, eliminating unnecessary motions, and identifying the most efficient way to perform the task.</li>
<li><strong>Fatigue Study:</strong> Determining the amount and frequency of rest required for workers to perform a task without undue fatigue, so output can be sustained.</li>
<li><strong>Standard Task (Standard Task Setting):</strong> Using time and motion study findings to set a standard, achievable task/output level for an average worker, used as the basis for planning and wage payment.</li>
<li><strong>Differential Piece Rate Plan:</strong> A wage incentive scheme where workers who meet or exceed the standard task are paid a higher piece rate, while those below standard are paid a lower rate &mdash; rewarding efficiency directly.</li>
<li><strong>Functional Foremanship:</strong> Dividing supervisory responsibility among several specialist foremen (e.g. for speed, quality, repairs) rather than one foreman handling everything, so each supervisory function gets expert attention.</li>
<li><strong>Standardisation:</strong> Standardising tools, equipment, materials and working conditions to eliminate inefficient variation and support consistent, high-quality output.</li>
</ol>

<h3>3.4 Strengths of Scientific Management</h3>
<ul>
<li>Introduced objective, data-driven methods for designing work, replacing guesswork.</li>
<li>Improved productivity and efficiency through standardisation and systematic training.</li>
<li>Linked pay directly to performance through the differential piece rate, motivating higher output.</li>
</ul>

<h3>3.5 Criticisms of Scientific Management</h3>
<ul>
<li>Treated workers mechanically, focusing on physical efficiency while largely ignoring psychological and social needs.</li>
<li>The intense focus on standard tasks and time study was seen by workers and unions as exploitative, increasing pressure and monotony.</li>
<li>Functional foremanship, in practice, could create confusion from reporting to multiple supervisors at once.</li>
<li>Its narrow focus on the shop floor ignored the human-relations and motivational factors that later Neo-Classical thinkers like Elton Mayo would highlight.</li>
</ul>
"""
terms = [
    ("Scientific Management", "F.W. Taylor's approach to management based on scientific study of work methods, standardisation, and training, replacing informal rule-of-thumb practice."),
    ("Time Study", "Observing and timing a worker's task movements to determine the standard time needed to complete it."),
    ("Motion Study", "Breaking a job into elementary movements to eliminate wasted motion and find the most efficient method."),
    ("Differential Piece Rate Plan", "A wage system paying a higher piece rate to workers who meet or exceed the standard task, and a lower rate to those who fall short."),
    ("Functional Foremanship", "Dividing supervisory responsibility among several specialist foremen instead of one all-purpose supervisor."),
]
examprep = [
    "Taylor's 5 principles: Science not Rule of Thumb; Harmony in Group Action; Cooperation between Workers and Management; Maximum (not Restricted) Output; Development of Workers to the Fullest.",
    "Taylor's techniques: Time Study, Motion Study, Fatigue Study, Standard Task, Differential Piece Rate, Functional Foremanship, Standardisation.",
    "Main criticism: treats workers mechanically, ignoring psychological/social needs &mdash; the gap later Neo-Classical theorists addressed.",
]
questions = [
    ("Explain the principles of Scientific Management given by F.W. Taylor.", "Science, not rule of thumb (scientifically study work methods); harmony in group action; cooperation between workers and management; maximum output in place of restricted output; and development of workers to the fullest extent through scientific selection and training."),
    ("Describe the techniques of Scientific Management.", "Time study (timing task movements), motion study (eliminating wasted movement), fatigue study (determining needed rest), standard task setting, the differential piece rate wage plan, functional foremanship (specialist supervisors), and standardisation of tools and conditions."),
    ("What is the differential piece rate plan? How does it motivate workers?", "It is a wage scheme where workers meeting or exceeding the scientifically set standard task are paid a higher rate per piece, while those falling short are paid a lower rate &mdash; directly rewarding efficient workers and encouraging everyone to reach the standard."),
    ("What are the main criticisms of Scientific Management?", "It treats workers mechanically and largely ignores their psychological and social needs; intense time/motion study was seen as exploitative by workers; functional foremanship could cause confusion from multiple reporting lines; and it ignores human-relations factors later highlighted by the Neo-Classical school."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("Alongside Taylor's shop-floor focus, Henri Fayol developed principles for managing the whole "
            "organisation from the top down, while Max Weber described the ideal rational-legal bureaucracy. "
            "Together they complete the Classical Era's picture of formal organisational structure.")
notes = """
<h3>4.1 Henri Fayol &mdash; Administrative Management</h3>
<p>Henri Fayol, a French mining engineer and Managing Director of a large mining company, approached management from the top management's point of view &mdash; the opposite of Taylor's shop-floor focus. He explained his ideas in "Administration Industrielle et Generale," published in French in 1916 and later translated into English in 1929 as "General and Industrial Management."</p>

<h3>4.2 Fayol's Functions of Management</h3>
<p>Fayol identified five functions of management: <strong>Planning</strong>, <strong>Organisation</strong>, <strong>Command</strong>, <strong>Co-ordination</strong>, and <strong>Control</strong> &mdash; the forerunner of the Planning/Organising/Staffing/Directing/Controlling framework used today.</p>

<h3>4.3 Fayol's 14 Principles of Management</h3>
<ol>
<li><strong>Division of Labour:</strong> Specialisation of work increases efficiency and output.</li>
<li><strong>Authority and Responsibility:</strong> Authority (the right to give orders) and responsibility (accountability for results) must go hand in hand.</li>
<li><strong>Discipline:</strong> Obedience and respect for the organisation's rules and agreements are essential for smooth functioning.</li>
<li><strong>Unity of Command:</strong> Every employee should receive orders from only one superior to avoid confusion.</li>
<li><strong>Unity of Direction:</strong> Activities with the same objective should be directed by one manager using one plan.</li>
<li><strong>Subordination of Individual Interest to General Interest:</strong> The interest of the organisation should prevail over the interest of any individual employee.</li>
<li><strong>Fair Remuneration to Employees:</strong> Pay should be fair, satisfying both employees and the organisation.</li>
<li><strong>Centralisation and Decentralisation:</strong> The degree to which decision-making authority is concentrated or dispersed should be balanced appropriately for the situation.</li>
<li><strong>Scalar Chain:</strong> A clear, unbroken chain of authority runs from the top of the organisation to the bottom (though a "gang plank" can shortcut communication between peers at the same level when urgent).</li>
<li><strong>Order:</strong> There should be a fixed, proper place for every person and every thing in the organisation.</li>
<li><strong>Equity:</strong> Managers should treat employees with kindness and justice, applying rules fairly.</li>
<li><strong>Stability of Tenure of Personnel:</strong> High employee turnover is inefficient; management should minimise unnecessary staff turnover.</li>
<li><strong>Initiative:</strong> Employees should be encouraged to develop and carry out their own plans and ideas within their area of work.</li>
<li><strong>Esprit de Corps:</strong> Management should promote team spirit, unity and harmony among employees.</li>
</ol>

<h3>4.4 Max Weber &mdash; Bureaucracy</h3>
<p>Max Weber, a German sociologist, contributed the theory of Bureaucracy as the ideal, most rational and efficient form of organisation for large-scale administration.</p>

<h3>4.5 Features of Bureaucracy</h3>
<ol>
<li><strong>Division of Work:</strong> Jobs are broken down into specialised tasks, with a clear division of labour.</li>
<li><strong>Hierarchy of Positions:</strong> A clear, well-defined hierarchy of authority exists, with each lower position controlled and supervised by a higher one.</li>
<li><strong>Rules and Regulations:</strong> Formal rules and procedures govern operations and decisions, ensuring consistency.</li>
<li><strong>Impersonal Conduct:</strong> Members conduct their official business impersonally, without regard to personal feelings or relationships; another "depersonalisation" aspect means members do not have a personal claim on their positions &mdash; they belong to the organisation, not to the individual.</li>
<li><strong>Staffing:</strong> Employees are hired and promoted based on technical competence and qualifications, not favouritism.</li>
</ol>

<h3>4.6 Weber's Three Types of Authority</h3>
<table class="compare">
<tr><th>Type</th><th>Basis</th></tr>
<tr><td><strong>Traditional Authority</strong></td><td>Derived from custom, tradition, or hereditary position (e.g. a monarchy or family business).</td></tr>
<tr><td><strong>Charismatic Authority</strong></td><td>Derived from the exceptional personal qualities or charisma of an individual leader.</td></tr>
<tr><td><strong>Rational-Legal Authority</strong></td><td>Derived from a formal system of legally established rules and office &mdash; the basis of modern bureaucratic organisations.</td></tr>
</table>
"""
terms = [
    ("Fayol's 14 Principles of Management", "General guidelines for administration proposed by Henri Fayol, covering division of labour, authority, discipline, unity of command, and ten others."),
    ("Scalar Chain", "The unbroken chain of authority and communication running from the top of an organisation to the bottom."),
    ("Esprit de Corps", "Fayol's principle that management should promote team spirit, unity and harmony among employees."),
    ("Bureaucracy", "Max Weber's ideal form of rational, rule-based organisation characterised by division of work, hierarchy, formal rules, impersonal conduct, and merit-based staffing."),
    ("Rational-Legal Authority", "Authority derived from a formal system of legally established rules and office, the basis of bureaucratic organisations."),
]
examprep = [
    "Fayol studied management from the top-management view; his 5 functions: Planning, Organisation, Command, Co-ordination, Control.",
    "Fayol's 14 principles: Division of Labour, Authority &amp; Responsibility, Discipline, Unity of Command, Unity of Direction, Subordination of Individual to General Interest, Fair Remuneration, Centralisation/Decentralisation, Scalar Chain, Order, Equity, Stability of Tenure, Initiative, Esprit de Corps.",
    "Weber's Bureaucracy features: Division of Work, Hierarchy of Positions, Rules &amp; Regulations, Impersonal Conduct, Merit-based Staffing.",
    "Weber's 3 types of authority: Traditional, Charismatic, Rational-Legal (basis of bureaucracy).",
]
questions = [
    ("Explain any five of Fayol's 14 principles of management.", "Division of Labour (specialisation increases efficiency); Unity of Command (one superior per employee); Scalar Chain (unbroken chain of authority top to bottom); Equity (fair, kind treatment of employees); and Esprit de Corps (promoting team spirit and unity)."),
    ("Differentiate between the approaches of Taylor and Fayol.", "Taylor approached management from the shop floor upward, focusing on worker efficiency through scientific study of tasks. Fayol approached management from the top management's point of view, focusing on general administrative principles applicable to managing the whole organisation."),
    ("Explain the features of bureaucracy as described by Max Weber.", "Division of work into specialised tasks, a clear hierarchy of positions with each level supervised by the one above, formal rules and regulations governing decisions, impersonal conduct of official business, and staffing based on technical competence rather than favouritism."),
    ("Explain Weber's three types of authority.", "Traditional Authority, based on custom or hereditary position; Charismatic Authority, based on a leader's exceptional personal qualities; and Rational-Legal Authority, based on a formal system of legally established rules and office, which underpins modern bureaucratic organisations."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("The Hawthorne Experiments, led by Elton Mayo at the Western Electric Company, revealed that social "
            "and psychological factors &mdash; not just physical working conditions &mdash; strongly influence "
            "worker productivity, launching the Neo-Classical, human-relations era of management thought.")
notes = """
<h3>5.1 Background to the Hawthorne Experiments</h3>
<p>The Hawthorne Experiments were a series of studies conducted at the Western Electric Company's Hawthorne Works in the late 1920s and early 1930s, initially to study the effect of physical working conditions (like lighting) on worker productivity. Elton Mayo and his research team led the studies, and the surprising results shifted management thinking away from Scientific Management's purely mechanical view of workers.</p>

<h3>5.2 The Experiments</h3>
<ol>
<li><strong>Illumination Experiments:</strong> Researchers varied the lighting levels for groups of workers to study the effect on productivity. Surprisingly, output increased for both the group whose lighting was improved and the control group whose lighting was unchanged &mdash; showing that some factor other than physical lighting was influencing productivity.</li>
<li><strong>Relay Room Experiments (Relay Assembly Test Room):</strong> A small group of workers was separated, and researchers systematically varied rest pauses, working hours and other conditions. Productivity rose steadily throughout, including when conditions were later returned to the original harsher levels &mdash; suggesting the workers responded to the special attention they received rather than to the physical changes themselves.</li>
<li><strong>Bank Wiring Observation Room Experiment:</strong> Researchers observed a group of workers without changing their conditions, to study the influence of informal group dynamics. They found that the group had developed its own informal production norms and would deliberately restrict output to match them, regardless of what management's incentive scheme encouraged.</li>
<li><strong>Interview Programme:</strong> Around 20,000 employees were interviewed about their attitudes toward their work, supervisors and the company. Interviewers found that it was less important to give employees direct answers than to allow them to express their views and feelings freely &mdash; employees valued simply being listened to.</li>
</ol>

<h3>5.3 Key Findings of the Hawthorne Experiments</h3>
<ol>
<li><strong>Social Factors Govern Workers:</strong> Workers are motivated as much by social and psychological needs &mdash; belonging, recognition, security &mdash; as by physical working conditions or pay.</li>
<li><strong>Group Influence:</strong> Informal groups form naturally among workers and strongly influence individual behaviour and productivity, sometimes more than formal management directives do.</li>
<li><strong>Supervision:</strong> The style and quality of supervision (attentive, participative) affects morale and output.</li>
<li><strong>Communication:</strong> Effective two-way communication between management and workers helps resolve problems and build trust.</li>
<li><strong>Conflicts:</strong> Conflicts between formal organisational goals and the informal group's own norms can arise and affect output.</li>
<li><strong>Leadership:</strong> Good informal leadership within a work group can positively influence morale and performance alongside formal supervision.</li>
</ol>

<h3>5.4 Implications of the Hawthorne Experiments</h3>
<p>The findings are often summarised as the "Hawthorne Effect" &mdash; the tendency for people to improve their behaviour or performance simply because they know they are being observed or because they are receiving special attention. The implications for management include:</p>
<ul>
<li>Recognising workers as social beings with psychological and social needs, not just economic units responding to pay.</li>
<li>Involving workers in decisions and listening to their views improves motivation and cooperation.</li>
<li>Good leadership and effective communication matter as much as physical working conditions.</li>
<li>Informal groups and their norms must be understood and worked with, not ignored, since they can support or undermine formal goals.</li>
</ul>
<p>These findings launched the Human Relations (Neo-Classical) movement in management thought, directly addressing the psychological and social dimensions that the Classical Era's Scientific Management approach had largely overlooked.</p>
"""
terms = [
    ("Hawthorne Experiments", "A series of studies at Western Electric's Hawthorne Works led by Elton Mayo, which found that social and psychological factors strongly influence worker productivity."),
    ("Hawthorne Effect", "The tendency for people to change or improve their behaviour because they know they are being observed or are receiving special attention."),
    ("Informal Group", "A naturally forming social group among workers, not created by management, which develops its own norms and can strongly influence productivity."),
    ("Human Relations Movement", "The Neo-Classical school of management thought, launched by the Hawthorne findings, focused on the social and psychological needs of workers."),
]
examprep = [
    "Hawthorne Experiments (Western Electric, Elton Mayo): Illumination, Relay Room, Bank Wiring Observation Room, Interview Programme.",
    "Key finding: social/psychological factors (not just physical conditions or pay) drive productivity &mdash; the 'Hawthorne Effect' of workers responding to attention.",
    "Bank Wiring Room showed informal groups set their own output norms, sometimes restricting output against management's incentive scheme.",
    "Findings launched the Human Relations (Neo-Classical) movement, correcting Scientific Management's narrow, mechanical view of workers.",
]
questions = [
    ("What were the Hawthorne Experiments? Who conducted them?", "A series of studies at the Western Electric Company's Hawthorne Works in the late 1920s/early 1930s, led by Elton Mayo, originally intended to study the effect of physical working conditions (like lighting) on productivity."),
    ("Explain the findings of the Illumination and Relay Room experiments.", "In the Illumination Experiments, productivity rose for both the test group and the control group regardless of lighting changes, suggesting a non-physical factor was at work. In the Relay Room experiments, productivity kept rising even when conditions were returned to their original state, suggesting workers responded to the special attention they received rather than the physical changes themselves."),
    ("What did the Bank Wiring Observation Room experiment reveal?", "It revealed that workers form informal groups with their own production norms, and that the group would deliberately restrict output to match these norms regardless of management's formal incentive scheme."),
    ("What is the 'Hawthorne Effect'?", "The tendency for people to change or improve their behaviour or performance simply because they know they are being observed or are receiving special attention, rather than because of any actual change in physical working conditions."),
    ("What are the main implications of the Hawthorne Experiments for management?", "Workers are social beings motivated by psychological and social needs as well as pay; involving and listening to workers improves motivation; good leadership and communication matter; and informal groups must be understood and worked with, since they can support or undermine formal organisational goals."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("The Modern Era moves beyond the Classical and Neo-Classical schools to view organisations as "
            "open systems interacting with their environment, and argues that there is no single best way to "
            "manage &mdash; the right approach depends on the situation.")
notes = """
<h3>6.1 The Systems Approach</h3>
<p>The Systems Approach views an organisation as an open system &mdash; a set of interrelated parts working together, taking inputs from the external environment, converting them through a transformation process, and releasing outputs back into the environment, with feedback flowing back in.</p>
<p>A typical open system model has four elements: <strong>Inputs</strong> (human, financial, material, information resources) &rarr; <strong>Transformation/Conversion Process</strong> &rarr; <strong>Outputs</strong> (goods, services, other results) &rarr; with <strong>Feedback</strong> flowing from outputs back to inputs, all interacting with the external environment.</p>

<h3>6.2 Types of Systems</h3>
<ol>
<li><strong>Physical/Mechanical Systems:</strong> Systems composed of equipment, machines, and similar physical elements; these are relatively closed and influenced by few external variables.</li>
<li><strong>Biological Systems:</strong> Systems that control and define the life cycle of living beings, such as birth, growth, maturity and death.</li>
<li><strong>Social Systems:</strong> Systems concerned with human beings and the interrelationships between individuals, formal and informal organisations, and economic, social and political factors.</li>
</ol>

<h3>6.3 Strengths of the Systems Approach</h3>
<ul>
<li>Provides a strong foundation for analysing the organisation as a whole, rather than studying its parts in isolation.</li>
<li>Helps managers understand the interdependence between sub-systems (departments) within the organisation.</li>
<li>Facilitates the smooth functioning of the overall organisational system by highlighting how a change in one part affects others.</li>
<li>Recognises that organisations must interact with, and adapt to, their external environment to survive.</li>
</ul>

<h3>6.4 Weaknesses of the Systems Approach</h3>
<ul>
<li>It is considered a theory of thinking rather than a specific, actionable managerial tool &mdash; it is conceptual rather than fully practical.</li>
<li>The approach can be vague and abstract, making it difficult to apply directly to concrete, day-to-day management problems.</li>
<li>It does not provide specific techniques for analysing or integrating sub-systems on its own &mdash; it describes what should be considered, more than how to do it.</li>
</ul>

<h3>6.5 The Contingency Approach</h3>
<p>The Contingency Approach developed as a reaction to the idea that there is "one best way" to manage in every situation. It argues that the most appropriate management action depends on ("is contingent upon") the specific situation &mdash; the organisation's size, environment, technology, and the people involved &mdash; rather than any single universal set of principles.</p>
<p>Contingency theorists study the relationship between different situations and the management practices/theories that work best in them, so that managers can tailor their approach to the particular circumstances they face, instead of mechanically applying one fixed theory everywhere.</p>

<h3>6.6 Merits of the Contingency Approach</h3>
<ol>
<li><strong>Practice-Oriented:</strong> It encourages managers to diagnose their specific situation and select the approach best suited to it, making it highly practical.</li>
<li><strong>Encourages Situational Analysis:</strong> It increases the scope for managers to examine and analyse each situation on its own merits before acting.</li>
<li><strong>Flexibility:</strong> It gives managers the freedom to adopt a more flexible, situation-specific style of leadership and decision-making rather than a rigid, one-size-fits-all rule.</li>
<li><strong>Helps Predict Outcomes:</strong> By studying what has worked in similar past situations, it helps managers better predict the likely outcome of a given approach in a new but comparable situation.</li>
</ol>
"""
terms = [
    ("Systems Approach", "A management theory that views an organisation as an open system of interrelated parts, taking inputs, transforming them, producing outputs, and receiving feedback, while interacting with its environment."),
    ("Open System", "A system that interacts with and is influenced by its external environment, continuously exchanging inputs and outputs with it."),
    ("Contingency Approach", "A management theory holding that the best management action depends on the specific situation at hand, rather than any single universal set of principles."),
    ("Feedback (Systems)", "Information about a system's outputs that flows back to influence its future inputs or transformation process."),
]
examprep = [
    "Systems Approach: organisation = open system of Inputs &rarr; Transformation Process &rarr; Outputs &rarr; Feedback, interacting with the environment.",
    "3 types of systems: Physical/Mechanical, Biological, Social.",
    "Systems Approach strength: whole-organisation view, shows sub-system interdependence; weakness: conceptual/vague, not a specific actionable tool.",
    "Contingency Approach: no 'one best way' &mdash; the right management action depends on the specific situation (size, environment, technology, people).",
    "Contingency merits: practice-oriented, encourages situational analysis, adds flexibility, helps predict outcomes from similar past situations.",
]
questions = [
    ("Explain the Systems Approach to management.", "It views an organisation as an open system made up of interrelated parts &mdash; taking inputs (human, financial, material, information) from the environment, converting them through a transformation process into outputs (goods/services), with feedback flowing back to inputs, all while continuously interacting with the external environment."),
    ("What are the three types of systems? Give an example of each.", "Physical/Mechanical systems (e.g. machines and equipment), Biological systems (the life cycle of living beings &mdash; birth, growth, maturity, death), and Social systems (human beings and their interrelationships within organisations and society)."),
    ("State the strengths and weaknesses of the Systems Approach.", "Strengths: gives a whole-organisation view, highlights interdependence between sub-systems, and recognises the need to adapt to the environment. Weaknesses: it is more a way of thinking than a specific actionable tool, and can be too abstract/vague for direct application to concrete problems."),
    ("Explain the Contingency Approach to management. Why did it develop?", "It holds that the right management action depends on the specific situation &mdash; the organisation's size, environment, technology and people &mdash; rather than any single universal theory. It developed as a reaction against the Classical and Human Relations schools' assumption that one best way to manage exists for every situation."),
    ("What are the merits of the Contingency Approach?", "It is practice-oriented (managers diagnose their situation before acting), encourages detailed situational analysis, gives managers flexibility to adapt their style to circumstances, and helps predict likely outcomes by drawing on what has worked in similar past situations."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Six topics covering the foundations of management: meaning, nature, functions and roles, the evolution of management thought, Taylor's Scientific Management, Fayol's Administrative Management and Weber's Bureaucracy, the Hawthorne Experiments, and the Systems/Contingency approach.")

print("Unit 1 (Management Concepts and Organisational Behaviour) complete: all 6 topics + index written.")
