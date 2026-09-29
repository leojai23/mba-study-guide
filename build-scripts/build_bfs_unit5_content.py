# -*- coding: utf-8 -*-
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Banking-and-Financial-Services\units"
BOOK_HTML = "Book: <em>Banking and Financial Services</em> (BA4003, Anna University MBA Sem III) &mdash; Thakur Publication"
BOOK_PLAIN = "Banking and Financial Services (BA4003), Thakur Publication"
NAVY_THEME = dict(accent="#1e3a5f", accent_dark="#15293f", accent_light="#e8eef5",
                   border="#d6dfe8", shadow="rgba(30,58,95,.14)")

TOPICS = [
    ("topic1-insurance-concept-principles-types.html", "Insurance &mdash; Concept, Principles &amp; Types"),
    ("topic2-insurance-act-1938.html", "The Insurance Act, 1938"),
    ("topic3-irda.html", "IRDA (Insurance Regulatory &amp; Development Authority)"),
    ("topic4-venture-capital-financing.html", "Venture Capital Financing"),
    ("topic5-bills-discounting.html", "Bills Discounting"),
    ("topic6-factoring.html", "Factoring"),
    ("topic7-merchant-banking-functions-services.html", "Merchant Banking &mdash; Functions &amp; Services"),
    ("topic8-merchant-banking-regulation-challenges.html", "Merchant Banking &mdash; SEBI Regulation &amp; Industry Challenges"),
]

U = common.UnitBuilder(5, "Insurance and Other Fee Based Financial Services", TOPICS,
                        subject="Banking and Financial Services", subject_root=SUBJECT_ROOT,
                        book_html=BOOK_HTML, book_plain=BOOK_PLAIN, theme=NAVY_THEME)

def T(i):
    fname, title = TOPICS[i-1]
    prev_link = (TOPICS[i-2][0], TOPICS[i-2][1]) if i > 1 else None
    next_link = (TOPICS[i][0], TOPICS[i][1]) if i < len(TOPICS) else None
    return fname, title, prev_link, next_link

# ================= Topic 1: Insurance - Concept, Principles & Types =================
fname, title, prev_link, next_link = T(1)
overview = ("Unit 5 opens with Insurance &mdash; a fee-based financial service that protects against risk. "
            "This topic covers what insurance is, the core principles every insurance contract must satisfy, "
            "and the main types of insurance policies available.")
notes = """
<h3>1.1 Concept of Insurance</h3>
<p>Insurance is a legal contract between two parties whereby one party (the insurer) undertakes to pay a fixed amount of money on the happening of a certain event (a peril or contingency), in exchange for a sum of money (the premium) paid by the other party (the insured). It is a tool which manages the financial risk of a person or property.</p>

<h3>1.2 Features of Insurance</h3>
<ol>
<li><strong>Risk Sharing:</strong> Insurance is a device to share the financial loss of a few among many exposed to a similar risk.</li>
<li><strong>Cooperative Device:</strong> The insurance business works on the principle of cooperation &mdash; many people exposed to a similar risk pool their contributions to compensate those who actually suffer a loss.</li>
<li><strong>Payment at the Time of Contingency:</strong> The insurer pays a sum of money to the insured only when the specified event (peril) covered under the policy actually occurs.</li>
<li><strong>Risk Assessment:</strong> The insurer assesses the probability of loss for a given peril before determining the premium to charge.</li>
</ol>

<h3>1.3 Principles of Insurance</h3>
<ol>
<li><strong>Principle of Utmost Good Faith:</strong> Both the insurer and the insured must disclose all material facts relevant to the contract honestly, since insurance contracts are based on trust in the absence of full inspection.</li>
<li><strong>Principle of Insurable Interest:</strong> The insured must have an insurable interest in the subject matter of insurance &mdash; i.e. they must stand to suffer a genuine financial loss if the insured event occurs.</li>
<li><strong>Principle of Indemnity:</strong> The insurer agrees to pay no more than the actual amount of loss suffered, so that the insured cannot profit from an insurance claim (does not apply to life insurance, which pays a fixed sum).</li>
<li><strong>Principle of Contribution:</strong> Where the same risk is insured with more than one insurer, each insurer contributes proportionately toward the loss, so the insured does not recover more than the actual loss in total.</li>
<li><strong>Principle of Subrogation:</strong> Once the insurer has compensated the insured for a loss, the insurer is entitled to step into the insured's shoes and pursue any rights of recovery against a third party responsible for the loss.</li>
<li><strong>Principle of Loss Minimisation:</strong> The insured is expected to take all reasonable steps to minimise the loss, just as if the property were uninsured, rather than being careless because it is insured.</li>
</ol>

<h3>1.4 Types/Classification of Insurance</h3>
<p>Insurance policies are broadly classified into <strong>Life Insurance</strong> and <strong>General Insurance</strong>.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Life Insurance &mdash; Types</h4>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Term Policy</strong></td><td>Provides life cover for a specific, limited term; pays out only if death occurs during the policy term; no maturity benefit if the insured survives the term.</td></tr>
<tr><td><strong>Whole Life Policy</strong></td><td>Covers the insured for their entire lifetime; the sum assured is paid to the nominee whenever death occurs.</td></tr>
<tr><td><strong>Endowment Policy</strong></td><td>Pays the sum assured either on death during the policy term, or on survival to the end of the term (maturity benefit) &mdash; combines protection with savings.</td></tr>
<tr><td><strong>Money Back Policy</strong></td><td>Pays periodic survival benefits at fixed intervals during the policy term, in addition to the full sum assured on death.</td></tr>
<tr><td><strong>Unit-Linked Insurance Plan (ULIP)</strong></td><td>Combines life insurance cover with market-linked investment, where premiums (after charges) are invested in equity/debt funds chosen by the policyholder.</td></tr>
<tr><td><strong>Annuity</strong></td><td>Pays a regular income to the insured, either immediately or from a future date, in exchange for a lump-sum premium.</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">General Insurance &mdash; Types</h4>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Fire Insurance</strong></td><td>Covers loss/damage to property caused by fire.</td></tr>
<tr><td><strong>Marine Insurance</strong></td><td>Covers loss of ships and/or cargo during marine transport.</td></tr>
<tr><td><strong>Motor Insurance</strong></td><td>Covers damage to a vehicle and third-party liability arising from an accident (compulsory by law for third-party cover in India).</td></tr>
<tr><td><strong>Health Insurance</strong></td><td>Covers medical/hospitalisation expenses of the insured.</td></tr>
<tr><td><strong>Accident Insurance</strong></td><td>Provides compensation for injury, disability, or death resulting from an accident.</td></tr>
<tr><td><strong>Property/Casualty Insurance</strong></td><td>Covers loss to property from various perils (theft, burglary, etc.).</td></tr>
<tr><td><strong>Liability Insurance</strong></td><td>Covers the insured's legal liability to pay compensation to a third party.</td></tr>
<tr><td><strong>Credit Insurance</strong></td><td>Protects a lender against a borrower's default or inability to repay.</td></tr>
</table>

<h3>1.5 Merits of Insurance</h3>
<ol>
<li><strong>Protection Against Risk of Loss:</strong> The primary purpose and function of insurance is to provide financial protection against uncertain loss.</li>
<li><strong>Cooperation:</strong> Insurance spreads the burden of loss across a large pool of policyholders through the cooperative principle.</li>
<li><strong>Risk Assessment:</strong> The process of underwriting in insurance requires a careful assessment of the probability and potential severity of a loss.</li>
<li><strong>Payment at the Time of Contingency:</strong> Provides a payout precisely when it is needed most &mdash; when the insured event occurs.</li>
<li><strong>Advancement of Small Savings:</strong> Life insurance in particular encourages small, regular savings which are otherwise difficult to accumulate.</li>
<li><strong>Mobilisation of Savings:</strong> Insurance mobilises the small savings made by people into large aggregated pools, invested in industrial and other productive uses of the economy.</li>
<li><strong>Formation of Capital:</strong> The large sums accumulated by insurance companies provide an important source of capital for investment purposes without offering protection against business losses alone.</li>
<li><strong>Social Security:</strong> Insurance helps in providing a sense of social security by protecting individuals/families from unforeseen financial hardship.</li>
</ol>

<h3>1.6 Demerits of Insurance</h3>
<ol>
<li><strong>Distribution of Risk:</strong> The insurer transfers risk to a number of individuals, but if the loss is widespread (e.g. a catastrophe affecting many policyholders at once), it can strain the insurer's own ability to pay.</li>
<li><strong>Capability of Facing Cut-Throat Competition:</strong> Insurance businesses have to work under massive competition, which can lead to underpricing of risk and financial instability.</li>
<li><strong>Specialisation:</strong> Insurance requires specialisation in assessing and pricing very specific types of risk, which not every insurer may have developed the expertise to do well.</li>
<li><strong>Optimum Utilisation of Capital:</strong> An insurance business needs to devote significant capital reserves purely for solvency purposes, rather than more productive business uses.</li>
</ol>
"""
terms = [
    ("Insurance", "A legal contract where an insurer agrees to compensate the insured for a specified loss, in exchange for a premium."),
    ("Principle of Indemnity", "The insurer pays no more than the actual loss suffered, so the insured cannot profit from a claim."),
    ("Principle of Insurable Interest", "The insured must stand to suffer a genuine financial loss from the insured event."),
    ("Principle of Subrogation", "The insurer's right to recover from a third party responsible for a loss, after compensating the insured."),
    ("Endowment Policy", "A life insurance policy paying the sum assured on death during the term, or on survival to maturity."),
]
examprep = [
    "Insurance principles: Utmost Good Faith, Insurable Interest, Indemnity, Contribution, Subrogation, Loss Minimisation.",
    "Life Insurance types: Term, Whole Life, Endowment, Money Back, ULIP, Annuity.",
    "General Insurance types: Fire, Marine, Motor, Health, Accident, Property/Casualty, Liability, Credit.",
    "Merits: risk protection, cooperation, risk assessment, timely payout, promotes small savings, mobilises savings into capital, social security.",
]
questions = [
    ("Explain the principles of insurance.", "Utmost Good Faith (honest disclosure by both parties), Insurable Interest (insured must have a genuine financial stake), Indemnity (compensation limited to actual loss), Contribution (multiple insurers share a loss proportionately), Subrogation (insurer's right to recover from a responsible third party), and Loss Minimisation (insured must act to limit the loss)."),
    ("Distinguish between Term Policy and Endowment Policy.", "A Term Policy provides life cover for a fixed period and pays out only if death occurs during that term, with no maturity benefit. An Endowment Policy pays the sum assured either on death during the term or on survival to maturity, combining life cover with a savings/investment element."),
    ("Explain the merits and demerits of insurance.", "Merits include protection against financial loss, risk-sharing through cooperation, disciplined risk assessment, timely payouts, promotion of small savings, capital formation, and social security. Demerits include the strain of widespread/catastrophic losses on insurers, cut-throat industry competition, the need for deep specialisation in risk assessment, and capital tied up purely for solvency."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2: The Insurance Act, 1938 =================
fname, title, prev_link, next_link = T(2)
overview = ("The Insurance Act, 1938 is the foundational law regulating insurance business in India. Like the "
            "Banking Regulation Act in Unit 1, this topic summarises its purpose and key provisions rather than "
            "listing every numbered Section.")
extra_note = '<div class="callout warn">The book lists many individual Sections of the Insurance Act with detailed sub-clauses. This page summarises the purpose and key provisions relevant for exams, rather than reproducing every Section number.</div>'
notes = """
<h3>2.1 Introduction to the Insurance Act, 1938</h3>
<p>The Insurance Act was the first legislation governing insurance business in India, enacted in 1938 to regulate the insurance sector, protect policyholders' interests, and ensure orderly growth of the industry. It has since been amended several times, including by the Insurance Laws (Amendment) Act, 2015, and works alongside the Life Insurance Corporation (Nationalisation) Act, 1956, the General Insurance Business (Nationalisation) Act, 1972, and the LIC Act, to govern all forms of insurance business in India up to and including the establishment of the IRDA.</p>

<h3>2.2 Scope and Application</h3>
<p>The Act applies to all types of insurance business in India, including life insurance, general insurance, and reinsurance, and is applicable to insurance companies, cooperative societies transacting insurance business, and other insurers as defined under the Act.</p>

<h3>2.3 Key Provisions of the Act</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Requirements as to Capital</h4>
<p>No insurer shall be registered or allowed to carry on the business of insurance in India unless it satisfies the minimum paid-up capital requirements specified under the Act, and deposits a specified sum with the RBI as security for policyholders.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Registration</h4>
<p>Every insurer must register with the Controller/Authority before commencing insurance business in India, providing a certified copy of the Memorandum and Articles of Association, particulars of its Directors, and other prescribed documents.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Maintenance of Register of Members</h4>
<p>Every insurer must maintain a register of policyholders in India, showing their names, addresses, and other prescribed particulars, and this register must be maintained within India.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Returns by Insurers</h4>
<p>Every insurer must submit annual returns (including balance sheet, profit &amp; loss account, and other prescribed statements) to the regulatory authority, certified as required by the Act.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Prohibition of Rebates and Restriction on Commission</h4>
<p>No person is allowed to offer a rebate on the premium payable, whether wholly or partly, as an inducement to take out a policy (except to the extent shown in the published prospectus/table). The Act also restricts the amount of commission payable to insurance agents (e.g. limiting first-year commission to a maximum percentage of the first year's premium, and lower percentages for renewal-year commissions).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Licensing of Agents</h4>
<p>No person can act as an insurance agent unless they hold a valid licence issued under the Act; the Act also lists grounds on which the licence of an agent can be cancelled (e.g. misconduct, fraud, or conviction of a relevant offence).</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Investment of Assets</h4>
<p>The Act regulates how insurers can invest the funds held against their policy liabilities, requiring a certain proportion to be held in approved government and other secure securities to protect policyholders.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Powers of the Controller/Authority</h4>
<p>The Controller (now the IRDA) is empowered to investigate the affairs of an insurer, call for information, direct amalgamations, and cancel registration if an insurer fails to comply with the Act's requirements or if it becomes insolvent or otherwise unfit to continue business.</p>

<h3>2.4 Reasons for Enacting the Insurance Act</h3>
<ul>
<li>To provide legislation regulating all forms of insurance business in a uniform manner.</li>
<li>To protect the interests of policyholders through minimum capital, registration, and reporting standards.</li>
<li>To ensure orderly and sound growth of the insurance industry.</li>
<li>To control unfair trade practices like rebating and excessive agent commissions.</li>
</ul>
"""
terms = [
    ("Insurance Act, 1938", "India's foundational insurance legislation, regulating registration, capital, agents, investment, and supervision of insurers."),
    ("Rebate", "An unauthorised discount on premium offered as an inducement to buy a policy, prohibited under the Act."),
    ("Controller of Insurance", "The regulatory authority under the Act (functions now performed by the IRDA) empowered to register, inspect, and regulate insurers."),
]
examprep = [
    "Insurance Act, 1938 = India's founding insurance law; regulates capital, registration, agent licensing, investment, and returns.",
    "Key provisions: minimum capital/deposit requirements, mandatory registration, register of policyholders, annual returns, ban on premium rebates, commission caps on agents, licensing of agents, restricted investment of insurer assets.",
    "The Controller (now IRDA) can investigate, inspect, and cancel registration of non-compliant insurers.",
]
questions = [
    ("What are the objectives of the Insurance Act, 1938?", "To regulate insurance business uniformly across India, protect policyholders' interests through capital/registration/reporting standards, ensure the orderly growth of the insurance industry, and curb unfair practices like premium rebating and excessive agent commissions."),
    ("Explain the key provisions of the Insurance Act relating to registration and capital.", "No insurer can commence business in India without meeting minimum paid-up capital requirements and depositing a prescribed security sum, and must register with the Controller by submitting its Memorandum/Articles of Association, Director details, and other prescribed documents."),
    ("What restrictions does the Act place on insurance agents and premium rebates?", "No rebate on premium may be offered as an inducement to buy a policy, except as shown in the published prospectus. Commission payable to agents is capped by percentage in the first year and lower percentages in renewal years, and agents must hold a valid licence, which can be cancelled for misconduct or fraud."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link, extra_note=extra_note))
print("Topic 2 done")

# ================= Topic 3: IRDA =================
fname, title, prev_link, next_link = T(3)
overview = ("The Insurance Regulatory and Development Authority (IRDA) is India's dedicated insurance "
            "regulator. This topic covers why it was created, its powers and functions, and its regulations "
            "protecting policyholders.")
notes = """
<h3>3.1 Introduction to IRDA</h3>
<p>The Insurance Regulatory and Development Authority (IRDA) was constituted under the IRDA Act, 1999, to provide legislation for the establishment of an Authority to protect the interests of holders of insurance policies, to regulate, promote, and ensure orderly growth of the insurance industry, and for matters connected therewith or incidental thereto. It also amended the Insurance Act, 1938, the LIC Act, 1956, and the General Insurance Business (Nationalisation) Act, 1972.</p>

<h3>3.2 Features of the IRDA Act</h3>
<ol>
<li>The main features of the Act are as follows: IRDA consists of a Chairman, five whole-time members, and four part-time members.</li>
<li>To protect the interest of policyholders.</li>
<li>To set the benchmarks for the insurance industry.</li>
<li>To bring speedy and orderly growth of the insurance industry to benefit the common citizen.</li>
<li>To ensure speedy settlement of genuine claims and prevent malpractices.</li>
</ol>

<h3>3.3 Objectives of IRDA</h3>
<ol>
<li>To protect the interest of and secure fair treatment to policyholders.</li>
<li>To bring about speedy and orderly growth of the insurance industry for the benefit of the common citizen and to provide a wide range of products at competitive prices.</li>
<li>To ensure speedy settlement of genuine claims, to prevent insurance frauds, and to put in place effective grievance-redressal machinery.</li>
<li>To promote fairness, transparency, and orderly conduct in financial markets dealing with insurance, and build a reliable management information system to enforce high standards of financial soundness among market players.</li>
</ol>

<h3>3.4 Role of IRDA as a Regulator</h3>
<p>IRDA regulates and audits the functioning of insurance companies. It formulates regulations on capital requirements, solvency margins, investment norms, and product approval, and monitors compliance across the industry.</p>

<h3>3.5 Functions/Powers of IRDA</h3>
<ol>
<li>Issuing certificates of registration to insurers, and renewing, modifying, withdrawing, suspending, or cancelling such registration.</li>
<li>Protection of policyholders' interests, in matters concerning assignment of policy, nomination, insurable interest, settlement of claims, surrender value, and other contract terms.</li>
<li>Specifying qualifications, code of conduct, and practical training for insurance intermediaries and agents.</li>
<li>Specifying the code of conduct for surveyors and loss assessors.</li>
<li>Promoting efficiency in the conduct of insurance business.</li>
<li>Regulating rates, terms, and conditions offered by insurers not covered under the Tariff Advisory Committee.</li>
<li>Levying fees and other charges for carrying out the purposes of the Act.</li>
<li>Calling for information, undertaking inspection, and conducting enquiries/investigations, including audit, of insurers, intermediaries, and other market participants.</li>
<li>Specifying the percentage of premium income to be spent on insurance business in rural and social sectors.</li>
<li>Regulating investment of funds by insurance companies.</li>
<li>Adjudicating disputes between insurers and intermediaries/agents.</li>
</ol>

<h3>3.6 Composition/Administration of IRDA</h3>
<p>The Authority consists of the following whole-time and part-time members:</p>
<ol>
<li>A Chairperson.</li>
<li>Not more than five whole-time members.</li>
<li>Not more than four part-time members. All appointed by the Central Government.</li>
</ol>

<h3>3.7 IRDA Regulations (Protection of Policyholders' Interests), 2002</h3>
<p>These regulations were issued to explain the various clauses of the insurance product to the extent of what is covered under the policy, what benefits/riders are participating/non-participating, the profit share (if applicable), and other terms and conditions in a clear and understandable manner to prospective policyholders.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Key Highlights</h4>
<ul>
<li>Insurers must provide a clear, plain-language proposal form for insurance, in languages recognised under the Constitution of India.</li>
<li>Insurers must not insist on a cover note being issued only against payment of the full premium in advance.</li>
<li>Every policyholder is entitled to a "free-look period" (currently 15 days from receipt of the policy document) during which they may review the policy terms and, if dissatisfied, return the policy for cancellation and a refund (less certain deductions).</li>
</ul>

<h3>3.8 IRDA Regulations for Life and General Insurance</h3>
<p>IRDA has issued separate regulations tailored to Life Insurance (covering products such as ULIPs, with specific disclosure and charge-structure norms) and General Insurance (covering fire, marine, motor, and other classes), including detailed guidelines on premium calculation, policy wordings, and claims settlement timelines specific to each type of business.</p>
"""
terms = [
    ("IRDA (Insurance Regulatory and Development Authority)", "India's insurance regulator, established under the IRDA Act, 1999, to protect policyholders and ensure orderly industry growth."),
    ("Free-Look Period", "A window (15 days) after receiving a life insurance policy during which the policyholder can review and cancel it for a refund."),
    ("Tariff Advisory Committee", "A body that historically set standard rates/terms for certain classes of general insurance."),
]
examprep = [
    "IRDA established under the IRDA Act, 1999, to protect policyholders and regulate/promote orderly insurance industry growth.",
    "Composition: 1 Chairperson + up to 5 whole-time members + up to 4 part-time members, all Central Government appointees.",
    "Key powers: registration of insurers, policyholder protection, agent/intermediary licensing standards, rate regulation, investigation/audit powers, investment regulation, dispute adjudication.",
    "Protection of Policyholders' Interests Regulations, 2002: plain-language proposal forms, no advance-payment-only cover notes, 15-day free-look period.",
]
questions = [
    ("What is IRDA? Explain its objectives.", "IRDA (Insurance Regulatory and Development Authority) was established under the IRDA Act, 1999 to protect policyholders' interests, ensure orderly and speedy growth of the insurance industry, promote fair competitive pricing, and ensure genuine claims are settled speedily while preventing fraud."),
    ("Explain the functions and powers of IRDA.", "Registering and regulating insurers, protecting policyholders on matters like nomination and claims settlement, setting standards for agents/intermediaries and surveyors, regulating rates and investment of insurer funds, levying fees, conducting inspections/investigations, mandating rural/social sector spending, and adjudicating disputes."),
    ("What is the 'free-look period' under IRDA regulations?", "A window of 15 days from receiving a life insurance policy document during which the policyholder can review its terms and, if dissatisfied, return the policy for cancellation and a refund (subject to certain deductions)."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4: Venture Capital Financing =================
fname, title, prev_link, next_link = T(4)
overview = ("Venture Capital funds new, high-potential businesses that traditional lenders consider too risky. "
            "This topic covers what venture capital is, how it's structured across stages, how investors exit, "
            "and how a venture's value is evaluated.")
notes = """
<h3>4.1 Meaning and Definition of Venture Capital</h3>
<p>The term "venture" in the broader sense consists of two words: venture capital involves a new business project or venture in which the entrepreneur puts in a new business project seeking finance to convert a promising idea into a going concern. In the narrower sense, venture capital deals with financing new and high-risk ventures, offering funding to growing companies with uncertain outcomes, including the risk of loss in return for the possibility of significant gains.</p>

<h3>4.2 Objectives of Venture Capital</h3>
<ol>
<li>To promote and assist small technology-based enterprises and companies with commercial applications.</li>
<li>To make funds available for high-growth businesses which may otherwise be unable to access finance.</li>
<li>To aid in the development and growth of indigenous technology, ensuring returns are attractive enough to justify the risk.</li>
</ol>

<h3>4.3 Methods of Financing Venture Capital</h3>
<ol>
<li><strong>Equity Financing:</strong> The venture capitalist takes an equity stake in the company, becoming a part-owner, generally not exceeding a certain percentage as agreed.</li>
<li><strong>Conditional Loan:</strong> The venture capitalist provides a loan which is repayable in the form of a royalty on the sales of the venture, once it starts earning revenue, instead of interest and principal in the conventional sense.</li>
<li><strong>Income Notes:</strong> A hybrid of a conventional loan and conditional loan, where the venture pays both interest and a royalty on sales, but at a lower rate than either alone.</li>
</ol>

<h3>4.4 Financing Pattern Under Venture Capital &mdash; Stages</h3>
<p>Venture capital financing follows the specific plan used by venture capitalists to reach successive stages of the firm as its business grows, corresponding to the establishment stage, up-and-running stage, and emerging stages, according to which risk is reduced with the help of the venture capitalist.</p>
<table class="compare">
<tr><th>Stage</th><th>Description</th></tr>
<tr><td><strong>Early Stage Financing</strong></td><td>Covers Seed Capital (converting an idea into a project for the first stage of project development) and Start-Up Capital (required by the entrepreneur to actually convert the idea into a business).</td></tr>
<tr><td><strong>Establishment/Second-Round Financing</strong></td><td>The venture is ready for early expansion, having proven the business concept at a small scale; finance is needed for full commercial production and marketing.</td></tr>
<tr><td><strong>Last Stage Financing</strong></td><td>Required at the point when the firm is about to achieve the break-even point and needs finance for further growth. Types include Development Capital, Bridge/Expansion Capital, and Buy-out Financing.</td></tr>
<tr><td><strong>Other Financing Methods</strong></td><td>Debentures (fixed interest, converted to equity later), Participating Debentures (interest charged in stages linked to the firm's operations), and other structured instruments.</td></tr>
</table>

<h3>4.5 Exit Mechanism of Venture Capital</h3>
<p>A venture capitalist plans an exit route from the outset, to realise the gains from their investment. The main exit methods:</p>
<ol>
<li><strong>Initial Public Offering (IPO):</strong> The venture capital-backed company lists its shares on a stock exchange, and the venture capitalist sells their shares to the public at the listing/market price.</li>
<li><strong>Repurchase by the Investee Company:</strong> The company itself buys back the venture capitalist's shareholding, if it has the resources to do so.</li>
<li><strong>Acquisition by Another Company:</strong> Another company acquires the entire investee company, and the venture capitalist's stake is bought out as part of the deal.</li>
<li><strong>Purchase of VC's Share by a Third Party:</strong> Another investor purchases the venture capitalist's shareholding directly, without the underlying company itself being acquired.</li>
</ol>

<h3>4.6 Process of Venture Capital Investment</h3>
<ol>
<li><strong>Deal Sourcing/Origination:</strong> Venture capital firms need a continuous flow of prospective deal proposals for potential investment; sourcing methods include referrals from industry contacts, entrepreneurs, and other VCs.</li>
<li><strong>Screening:</strong> VCs use a broad screening basis (e.g. technology, industry, geographical scope, stage of financing) to narrow down proposals.</li>
<li><strong>Evaluation or Due Diligence:</strong> Detailed evaluation of the business plan, management team, market potential, technology risk, and financial projections before proceeding.</li>
<li><strong>Deal Structuring/Making a Deal:</strong> Once approved for investment, the VC and entrepreneur negotiate the terms of the deal (amount, instrument, valuation, board rights, exit clauses etc.), formalised in a legal agreement.</li>
<li><strong>Post-Investment Activities:</strong> The venture capital firm typically works closely with the investee company after the deal is signed, providing guidance/mentorship, monitoring performance, and helping the company execute its business plan.</li>
</ol>

<h3>4.7 Methods of Evaluation of Venture Capital</h3>
<table class="compare">
<tr><th>Method</th><th>Approach</th></tr>
<tr><td><strong>Conventional Valuation Method</strong></td><td>Present Value of Venture Capital = Expected Future Value &times; Discounting Factor.</td></tr>
<tr><td><strong>Revenue Multiplier Method</strong></td><td>Value of the venture = Expected Revenue &times; an appropriate Revenue Multiplier for that industry.</td></tr>
<tr><td><strong>Minimum Percentage of Ownership</strong></td><td>Determines the minimum equity stake the VC requires, based on the venture's expected future value and the VC's required return.</td></tr>
<tr><td><strong>Earnings Multiplier Method</strong></td><td>Value = Expected earnings level &times; an appropriate P/E multiple used for similar companies.</td></tr>
<tr><td><strong>First Chicago Method</strong></td><td>Considers multiple future outcomes (success, moderate performance, failure) for a venture and calculates a probability-weighted valuation across the range of scenarios.</td></tr>
</table>

<h3>4.8 Advantages of Venture Capital</h3>
<ol>
<li>Venture capital helps entrepreneurs turn new and innovative ideas into commercially-viable businesses, which may not otherwise obtain funding from lack of a track record.</li>
<li>Venture capitalists also participate in mentoring the business, offering strategic guidance and industry connections, beyond just funding.</li>
<li>It encourages innovation by giving entrepreneurs the ability to take risks with new/untested business ideas.</li>
</ol>

<h3>4.9 Disadvantages of Venture Capital</h3>
<ol>
<li>Venture capital funding can often involve large amounts, expertise, and revenue-sharing expectations, which can be difficult for a young business to meet.</li>
<li>Venture capitalists typically also seek significant ownership/control in exchange for their investment, which can dilute the founder's control over key decisions.</li>
</ol>
"""
terms = [
    ("Venture Capital", "Equity/near-equity financing provided to new, high-growth, high-risk businesses in exchange for an ownership stake."),
    ("Seed Capital", "Very early-stage venture capital used to convert a business idea into a viable project."),
    ("Conditional Loan", "Venture financing repayable as a royalty on the venture's future sales, rather than fixed interest."),
    ("Exit Mechanism", "The route (IPO, buyback, acquisition, or third-party sale) by which a venture capitalist realises returns and exits an investment."),
    ("First Chicago Method", "A venture valuation method using probability-weighted outcomes across multiple future scenarios."),
]
examprep = [
    "VC financing methods: Equity Financing, Conditional Loan (royalty-based), Income Notes (hybrid of interest + royalty).",
    "Financing stages: Early Stage (Seed + Start-Up) &rarr; Establishment/Second-Round &rarr; Last Stage (Development/Bridge/Buy-out).",
    "Exit routes: IPO, Repurchase by the company, Acquisition by another company, Sale of VC's stake to a third party.",
    "VC investment process: Deal Sourcing &rarr; Screening &rarr; Due Diligence &rarr; Deal Structuring &rarr; Post-Investment support.",
    "Evaluation methods: Conventional (PV), Revenue Multiplier, Minimum Ownership %, Earnings Multiplier, First Chicago (probability-weighted).",
]
questions = [
    ("Explain the different stages of venture capital financing.", "Early Stage Financing (Seed Capital to develop the idea, Start-Up Capital to launch the business), Establishment/Second-Round Financing (for early commercial expansion), and Last Stage Financing (Development/Bridge/Buy-out Financing as the venture nears break-even)."),
    ("What are the various exit mechanisms available to a venture capitalist?", "Initial Public Offering (listing the company and selling shares to the public), Repurchase by the investee company, Acquisition of the company by another firm, and Sale of the VC's shareholding directly to a third party."),
    ("Describe the process of venture capital investment.", "Deal Sourcing/Origination (finding prospective deals), Screening (narrowing proposals by set criteria), Evaluation/Due Diligence (assessing the business plan and team in detail), Deal Structuring (negotiating and formalising terms), and Post-Investment Activities (ongoing mentoring and monitoring)."),
    ("Explain the First Chicago Method of venture capital valuation.", "It values a venture by considering multiple future outcome scenarios (e.g. success, moderate performance, failure), assigning a probability to each, and calculating a probability-weighted valuation across the range of scenarios, rather than relying on a single projected outcome."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5: Bills Discounting =================
fname, title, prev_link, next_link = T(5)
overview = ("Bills Discounting lets a business get paid immediately for a bill of exchange, instead of waiting "
            "for it to mature. This topic covers the different types of bills, how the discounting system "
            "works, and its advantages and disadvantages.")
notes = """
<h3>5.1 Meaning and Definition of Bill Discounting</h3>
<p>According to the Indian Negotiable Instruments Act: "A bill of exchange involves three parties, the drawer, the drawee, and the payee." A bill of exchange is an unconditional order in writing, signed by the maker, directing a certain person to pay a certain sum of money to, or to the order of, a certain person, or to the bearer of the instrument. Bill discounting involves a bank purchasing a bill before its maturity date, and paying the holder the bill's value minus a discount charge, converting it to a clean bill.</p>

<h3>5.2 Types of Bills</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Demand Bills</strong></td><td>Bills payable "on demand," or "at sight," or "on presentment," with no fixed time period mentioned in the instrument.</td></tr>
<tr><td><strong>Usance Bills</strong></td><td>Bills payable after a specified time period from the date of the bill or the date of acceptance.</td></tr>
<tr><td><strong>Documentary Bills</strong></td><td>Bills accompanied by documents of title to goods (e.g. bill of lading), which may be Documents against Acceptance (D/A) or Documents against Payment (D/P). Under D/A bills, documents are delivered once the drawee accepts the bill. Under D/P bills, documents are delivered only once the drawee actually pays.</td></tr>
<tr><td><strong>Clean Bills</strong></td><td>Bills that do not have documents of title to goods attached, since these are usually supported by other trade arrangements.</td></tr>
<tr><td><strong>Inland Bills</strong></td><td>Bills drawn and payable within India, or drawn on a person resident in India, even if payable outside India.</td></tr>
<tr><td><strong>Foreign Bills</strong></td><td>Bills drawn outside India and payable either in or outside India, or drawn in India but payable outside India.</td></tr>
<tr><td><strong>Supply Bills</strong></td><td>Bills drawn by a supplier or contractor for goods supplied to government departments; not negotiable instruments since government departments do not accept these as suitable for negotiability.</td></tr>
<tr><td><strong>Accommodation Bills</strong></td><td>Bills drawn and accepted without any actual trade transaction behind them, purely to raise finance; used when the sole purpose is temporary financial assistance between the parties.</td></tr>
</table>

<h3>5.3 Bills Systems</h3>
<p>Two systems exist in different countries for handling bills of exchange:</p>
<ol>
<li><strong>Drawer Bill System:</strong> Followed in some countries, where the drawer of the bill draws it for purchasing goods from the seller of goods.</li>
<li><strong>Acceptance Credit System:</strong> This is the one followed in India, where the banker accepts the bill on behalf of the drawee, essentially substituting the bank's own creditworthiness for the drawee's.</li>
</ol>

<h3>5.4 Working of Bills Discounting</h3>
<ol>
<li><strong>Examination of Bill:</strong> The bank examines the bill for genuineness and the creditworthiness of the parties involved before discounting.</li>
<li><strong>Sending Bills for Collection:</strong> As per the guidelines to keep the ratio between bills discounted and bills sent for collection balanced, banks also send some bills purely for collection (not discounting) when the drawer/drawee relationship isn't yet well established.</li>
<li><strong>Crediting Customer Accounts:</strong> The bank credits the drawer's/customer's account with the discounted value of the bill (face value minus discount charge) upon accepting it for discounting.</li>
<li><strong>Control over Accounts:</strong> The bank maintains a bills discounted register to keep track of the due dates, amounts, and status of every bill in its books.</li>
<li><strong>Dishonour:</strong> If the bill is dishonoured (drawee fails to pay at maturity), the bank recovers the amount along with related interest/penal charges from the drawer/customer who got the bill discounted.</li>
</ol>

<h3>5.5 Advantages of Bills Discounting</h3>
<ol>
<li><strong>Immediate Availability of Cash:</strong> Discounting facility provides immediate access to cash before the bill's actual maturity, improving working capital for the business.</li>
<li><strong>Limit Against Repayment:</strong> Banks generally set a limit against which bills can be discounted, providing structured, ongoing access to short-term finance.</li>
<li><strong>No Extra Security Needed:</strong> Discounting facility does not require additional security beyond the bill itself, since the bill and the underlying trade transaction serve as security.</li>
<li><strong>Nature of Liability for Repayment:</strong> The drawer's liability is only contingent (arises only if the bill is dishonoured), unlike a regular loan.</li>
<li><strong>Refinance Facility:</strong> Banks that have discounted bills can, in turn, get such discounted bills "re-discounted" with the Reserve Bank of India or other refinancing institutions, known as the "Due bill" facility.</li>
<li><strong>Higher Yield:</strong> The discounting of bills may provide a higher rate of return to the discounting bank compared to some other short-term lending, due to fluctuation in prices and other market circumstances.</li>
</ol>

<h3>5.6 Disadvantages of Bills Discounting</h3>
<ol>
<li><strong>No Security Against the Amount of Payment:</strong> Banks discount bills largely on trust in the creditworthiness of the parties, without any collateral security beyond the bill itself.</li>
<li><strong>Immediate Availability of Cash May Be Misused:</strong> Since cash is credited instantly, there is a risk of businesses misusing this facility for purposes unrelated to genuine trade transactions.</li>
<li><strong>Facility Is Subject to the Creditworthiness of Parties:</strong> Banks generally have to consider the customer's creditworthiness before extending this facility, which can be a barrier for newer or smaller businesses.</li>
<li><strong>Additional Burden for Non-Payment:</strong> If the bill is dishonoured, the additional burden (interest, penal charges) falls on the drawer/customer, in addition to repaying the discounted amount itself.</li>
</ol>
"""
terms = [
    ("Bill of Exchange", "An unconditional written order signed by the maker directing payment of a certain sum to a specified person or bearer."),
    ("Bill Discounting", "A bank purchasing a bill of exchange before maturity, paying the holder its value minus a discount charge."),
    ("Usance Bill", "A bill payable after a specified period from its date or acceptance (as opposed to a demand bill)."),
    ("Documents against Acceptance (D/A)", "Documentary bill terms where title documents are released once the drawee accepts the bill."),
    ("Documents against Payment (D/P)", "Documentary bill terms where title documents are released only once the drawee pays."),
    ("Accommodation Bill", "A bill drawn/accepted without an underlying trade transaction, purely to raise finance."),
]
examprep = [
    "Bill discounting = bank buys a bill before maturity, pays face value minus discount, becomes holder in due course.",
    "Bill types: Demand, Usance, Documentary (D/A vs D/P), Clean, Inland, Foreign, Supply, Accommodation.",
    "India follows the Acceptance Credit System for bills.",
    "Advantages: immediate cash, no extra security needed, only contingent liability for the drawer, banks can re-discount with RBI.",
    "Disadvantages: no collateral security, risk of misuse, dependent on party creditworthiness, dishonour burden falls on the drawer.",
]
questions = [
    ("What is bill discounting? Explain the process.", "Bill discounting is when a bank purchases a bill of exchange from its holder before maturity, crediting the discounted value (face value minus discount charge) immediately. The bank examines the bill's genuineness and parties' creditworthiness, credits the customer's account, tracks the bill until maturity, and recovers dues (plus penal charges) from the drawer if the bill is dishonoured."),
    ("Explain the different types of bills of exchange.", "Demand Bills (payable on sight/demand), Usance Bills (payable after a specified period), Documentary Bills (D/A and D/P variants, accompanied by title documents), Clean Bills (no documents attached), Inland and Foreign Bills (based on country of drawing/payment), Supply Bills (for government supplies), and Accommodation Bills (raised without an underlying trade transaction)."),
    ("What are the advantages and disadvantages of bill discounting?", "Advantages include immediate cash availability, no extra collateral needed, only contingent liability for the drawer, and the ability for banks to re-discount bills with the RBI. Disadvantages include reliance on trust rather than security, risk of the facility being misused, dependence on the parties' creditworthiness, and the burden of penal charges falling on the drawer if the bill is dishonoured."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6: Factoring =================
fname, title, prev_link, next_link = T(6)
overview = ("Factoring lets a business convert its accounts receivable into immediate cash by selling them to "
            "a specialist financial institution (a factor). This topic covers its types, mechanism, and how it "
            "compares to bills discounting.")
notes = """
<h3>6.1 Meaning and Definition of Factoring</h3>
<p>"Factoring" is derived from the Latin word "Factor", which means "the one who does". In simple terms, factoring means a financial transaction which involves a firm selling its invoices or accounts receivable to a third party (called a "Factor"), at a discount, in order to receive cash immediately instead of waiting for payment at the instant maturity date. Factoring is a kind of arrangement providing collection services, which reduces the additional burden incurred by the client in maintaining its sales ledger, and protection against bad debts is prevented in developing countries.</p>

<h3>6.2 Types of Factoring Arrangements</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Recourse Factoring</strong></td><td>Under recourse factoring, the factor buys trade receivables and provides collection services, but if the debtor defaults, then the client (seller), not the factor, remains responsible for the bad debt.</td></tr>
<tr><td><strong>Non-Recourse Factoring</strong></td><td>This kind of arrangement is provided for the sale of accounts receivable in which the risk of bad debt is prevented/transferred to the factor, who bears the loss if the debtor fails to pay.</td></tr>
<tr><td><strong>Notified and Unnotified Factoring</strong></td><td>Under Notified Factoring, the debtor is informed that the receivable has been assigned to a factor and must pay the factor directly. Under Unnotified (Confidential) Factoring, the debtor is not told; the client collects payment as normal and then remits it to the factor.</td></tr>
<tr><td><strong>Bank Participation Factoring</strong></td><td>A type of factoring where a bank provides an advance to the client against a factoring arrangement, in addition to the amount available from the factor.</td></tr>
<tr><td><strong>Advance Factoring</strong></td><td>The factor pays the client an advance portion (typically up to 80% or more of the invoice value) at the time of purchase of the receivables, before the actual collection date.</td></tr>
<tr><td><strong>Maturity Factoring</strong></td><td>The factor pays the client only on the guaranteed payment date or on collection, whichever is earlier, rather than in advance.</td></tr>
<tr><td><strong>Full Factoring</strong></td><td>Combines all the services of factoring: financing, collection, sales-ledger administration, and credit protection.</td></tr>
<tr><td><strong>Buy-Back Factoring</strong></td><td>Under this arrangement, the factor purchases the goods/receivables and offers the client the option to buy back the receivables if the debtor defaults, essentially another form of recourse.</td></tr>
<tr><td><strong>Cross-Border/Export Factoring</strong></td><td>Factoring arrangements for export receivables, generally involving both an export factor (in the exporter's country) and an import factor (in the importer's country), each handling their respective side of the transaction.</td></tr>
<tr><td><strong>Invoice Discounting</strong></td><td>A financing-only arrangement (similar to factoring) where the client retains responsibility for collection and sales-ledger management, borrowing against the value of unpaid invoices.</td></tr>
</table>

<h3>6.3 Working Mechanism of Factoring</h3>
<ol>
<li>The client (seller) sells goods/services to the customer (buyer) on credit and generates an invoice.</li>
<li>The client assigns/sells this invoice (receivable) to the factor.</li>
<li>The factor pays the client an agreed percentage of the invoice value (advance payment) immediately, typically 75-90%.</li>
<li>The factor collects the full amount from the customer on the due date.</li>
<li>The factor pays the client the balance amount (less factoring fees/commission) after collection.</li>
</ol>

<h3>6.4 Role of Commercial Bank in Factoring</h3>
<p>Commercial banks provide factoring services in various ways, functioning as a factor themselves in the following areas:</p>
<ol>
<li><strong>Credit Function:</strong> As factoring means providing favourable assistance to the various entrepreneurs, banks also provide short-term credit to businesses/entrepreneurs to get the invoices required.</li>
<li><strong>Collection of Accounts:</strong> The bank maintains proper accounts of the invoices in the sales ledger, done by the commercial bank on behalf of the client.</li>
<li><strong>Advisory Function:</strong> As factoring involves advising its clients on the various services related to factoring, banks also give suggestions on managing accounts receivable more efficiently.</li>
<li><strong>Maintenance of Accounts:</strong> The factor (bank) maintains proper accounts of the invoices in the sales ledger for the client and provides periodic statement of accounts.</li>
<li><strong>Confidentiality of Invoices:</strong> Selling its invoices in the factoring arrangement made by a third party. So the commercial banker maintains confidentiality where done by client so that the terms and details involved in the factoring don't have adverse impact on the parties involved.</li>
</ol>

<h3>6.5 Advantages of Factoring</h3>
<ol>
<li><strong>Immediate Cash Flow:</strong> The client is able to receive cash immediately instead of waiting till the due date of the invoice, and thus is able to provide better credit terms to buyers, using the offered credit period as a sales tool.</li>
<li><strong>Credit Investigation Function:</strong> The factor makes the necessary statement of accounts of the invoice along with the differential payment to the client.</li>
<li><strong>Advance Payment:</strong> Factors typically provide advance payment up to 80 percent of the value of the invoice.</li>
<li><strong>Maintenance of Accounts:</strong> The factor maintains proper accounts of the invoices in the sales ledger, purchase ledger, etc.</li>
<li><strong>Collection of Invoices:</strong> The client is able to save time by not having to wait till the due date for collection of accounts receivables, as they are required to do from factoring arrangements.</li>
</ol>

<h3>6.6 Disadvantages of Factoring</h3>
<ol>
<li><strong>Costly:</strong> Such charges are levied on the factoring arrangement in the form of fees, which are a cost of the arrangement carried out by the firm.</li>
<li><strong>Effect on Creditworthiness:</strong> It has certain drawbacks impact of the notification to the customer about assignment of debts, which can affect how the buyer perceives the seller's creditworthiness.</li>
<li><strong>Difficult to Find the Agreement:</strong> Various legalities involved in factoring may be difficult to negotiate for a small business, as factors may be reluctant to work with certain sales-ledger patterns or industries.</li>
<li><strong>Reliance on Factor:</strong> The business may develop a negative or excessive dependence on this type of arrangement instead of building its own working capital/collections discipline.</li>
</ol>

<h3>6.7 Difference between Factoring and Bills Discounting</h3>
<table class="compare">
<tr><th>Basis</th><th>Factoring</th><th>Bills Discounting</th></tr>
<tr><td>Nature</td><td>Sale of the entire accounts receivable, generally an ongoing arrangement over a client's whole sales ledger</td><td>Discounting of a specific, individual bill of exchange</td></tr>
<tr><td>Notification</td><td>Debtor is generally notified (except in confidential factoring)</td><td>Not necessarily notified to any third party</td></tr>
<tr><td>Services Provided</td><td>Can include collection, sales-ledger administration, credit protection, and advisory services</td><td>Purely a financing arrangement, no additional services</td></tr>
<tr><td>Recourse</td><td>Can be with or without recourse (non-recourse transfers bad-debt risk to the factor)</td><td>Always with recourse to the drawer if the bill is dishonoured</td></tr>
<tr><td>Documentation</td><td>Based on invoices/accounts receivable, no negotiable instrument required</td><td>Requires a formal negotiable instrument (the bill of exchange)</td></tr>
</table>
"""
terms = [
    ("Factoring", "A financial arrangement where a business sells its accounts receivable to a factor at a discount for immediate cash."),
    ("Recourse Factoring", "Factoring where the client remains liable for bad debts if the debtor defaults."),
    ("Non-Recourse Factoring", "Factoring where the factor bears the risk of bad debt if the debtor defaults."),
    ("Notified Factoring", "Factoring where the debtor is informed of the assignment and pays the factor directly."),
    ("Advance Factoring", "Factoring where the factor pays a large advance (e.g. 80%) of the invoice value upfront."),
]
examprep = [
    "Factoring = selling accounts receivable to a factor at a discount for immediate cash.",
    "Types: Recourse vs Non-Recourse, Notified vs Unnotified, Bank Participation, Advance vs Maturity, Full, Buy-Back, Cross-Border/Export, Invoice Discounting.",
    "Mechanism: sell on credit &rarr; assign invoice to factor &rarr; factor advances ~75-90% &rarr; factor collects from buyer &rarr; factor pays balance (less fees).",
    "Advantages: immediate cash flow, advance payment, sales-ledger maintenance, saved collection time.",
    "Disadvantages: cost/fees, possible creditworthiness perception impact from notification, difficulty for small businesses to arrange, over-reliance risk.",
    "Factoring vs Bills Discounting: Factoring = whole receivables ledger, often notified, can include extra services, can be non-recourse. Bills Discounting = single bill, always with recourse, financing-only, needs a negotiable instrument.",
]
questions = [
    ("What is factoring? Explain its types.", "Factoring is a financial arrangement where a business sells its accounts receivable to a factor at a discount for immediate cash. Types include Recourse (client liable for bad debt) vs Non-Recourse (factor bears bad-debt risk), Notified vs Unnotified (confidential), Advance vs Maturity Factoring, Full Factoring, Buy-Back Factoring, and Cross-Border/Export Factoring."),
    ("Explain the working mechanism of factoring.", "The client sells goods on credit and raises an invoice, then assigns/sells that invoice to a factor. The factor advances a large percentage (75-90%) of the invoice value immediately, collects the full amount from the customer on the due date, and pays the client the remaining balance minus its fees."),
    ("Distinguish between factoring and bills discounting.", "Factoring involves selling the entire accounts receivable ledger on an ongoing basis, can involve notification to the debtor, may include collection/ledger/advisory services, and can be with or without recourse. Bills discounting involves a single bill of exchange, is always with recourse to the drawer, is purely a financing arrangement, and requires a formal negotiable instrument."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 6 done")

# ================= Topic 7: Merchant Banking - Functions & Services =================
fname, title, prev_link, next_link = T(7)
overview = ("Merchant banks provide specialised financial advisory and issue-management services to "
            "corporations. This topic covers what merchant banking is, its objectives, the various roles it "
            "plays, and the range of services it offers.")
notes = """
<h3>7.1 Meaning and Definition of Merchant Banking</h3>
<p>A merchant bank is best defined as a financial institution conducting money-market activities, and the lending, underwriting, and financial advice, and portfolio management services for both institutions and individuals, but not providing normal banking services to the general public.</p>
<p>According to <strong>D.C.Cox</strong>: "Merchant banks are the financial institutions providing specialist services which generally include the acceptance of bills of exchange, corporate finance, portfolio management and other banking services."</p>
<p>According to the <strong>SEBI (Merchant Bankers) Rules, 1992</strong>: "Merchant Banker means any person who is engaged in the business of issue management either by making arrangements regarding selling, buying, or subscribing to securities as manager, consultant, advisor, or rendering corporate advisory services in relation to such issue management."</p>

<h3>7.2 Objectives of Merchant Banking</h3>
<ol>
<li>To facilitate corporations, industrial and financial institutions in the mobilisation of funds.</li>
<li>Merchant banks play an important role in the Indian financial sector by facilitating capital market activities, which are the forces behind the industry's growth.</li>
<li>To provide various financial services pertaining to the issue, including the acceptance of bills of exchange, portfolio management, and merchant banking services.</li>
<li>Underwriters extend various services to industrial concerns, encourages the industrial development in our country.</li>
</ol>

<h3>7.3 Functions/Role of Merchant Banks</h3>
<p>Merchant banks perform several roles depending on the requirements of the issue and the client, as shown in the functions/roles of merchant banking:</p>
<ol>
<li><strong>Underwriters:</strong> Underwriters may be defined as a group of financial institutions/entities which undertake to subscribe to securities offered for sale to the public, in case of failure of the issue to get fully subscribed by the public.</li>
<li><strong>Portfolio Managers:</strong> Portfolio Manager refers to the management of an investment portfolio on behalf of a client under a discretionary or non-discretionary arrangement.</li>
<li><strong>Brokers:</strong> Merchant banks are individuals/institutions who perform the function of obtaining prospective investors to subscribe to an issue, suitably engaged in the business of obtaining subscriptions to an issue by approaching the primary or secondary market.</li>
<li><strong>Registrar:</strong> Appointment of Registrar to an Issue is mandatory in cases of public issue offering to raise money from the public, on a fixed date and time; they process the applications, allotments, and refunds.</li>
<li><strong>Debenture Trustee:</strong> Debenture Trustees are appointed to protect the interests of debenture holders, monitoring the issuer's compliance with the terms of the debenture agreement.</li>
<li><strong>Banker to the Issue:</strong> Bankers to an issue are typically appointed at the primary market function, collecting application money from investors during a public issue on behalf of the company.</li>
<li><strong>Advisor:</strong> Before undertaking issue management, merchant bankers assess the appropriate financial instruments, quantum, and timing of the issue in consultation with the issuer.</li>
</ol>

<h3>7.4 Services of Merchant Banks</h3>
<ol>
<li><strong>Corporate Counselling:</strong> Corporate counselling is a comprehensive service covering all the activities of a company, aimed at improving overall performance by giving suggestions to management for organisational improvement.</li>
<li><strong>Project Counselling:</strong> This involves preparation of project reports, deciding upon the financing pattern, and to finalise the arrangement for raising the finance required in the project, at the pre-investment stage, including feasibility study.</li>
<li><strong>Loan Syndication:</strong> Under Loan Syndication, a merchant banker arranges finance from a group of banks/financial institutions for a large project which cannot be financed by a single lender alone, by identifying the sources, preparing loan applications, and negotiating terms on behalf of the borrower.</li>
<li><strong>Corporate Advisory Services:</strong> Merchant bankers provide corporate advisory services related to mergers and acquisitions, amalgamations, disinvestments, and takeovers.</li>
<li><strong>Portfolio Management:</strong> Merchant bankers manage the investment portfolio of mutual funds, corporates, and individuals, through active buying/selling of securities to maximise returns.</li>
<li><strong>Issue Management:</strong> Managing an entire public issue of shares/debentures &mdash; drafting the prospectus, obtaining regulatory approvals, coordinating with other intermediaries, and ensuring compliance.</li>
<li><strong>Foreign Currency Financing:</strong> Helping companies structure and arrange foreign currency loans, export/import finance, and venture capital financing in foreign currency, at times helping with syndicated loans.</li>
<li><strong>Leasing:</strong> Some merchant bankers also provide advice and arrangement services related to leasing as a source of finance.</li>
<li><strong>Consultancy Services:</strong> Merchant bankers offer general consultancy on various corporate financial matters, including restructuring, business valuation, and financial planning.</li>
</ol>
"""
terms = [
    ("Merchant Bank", "A specialist financial institution providing corporate advisory, issue-management, underwriting, and portfolio management services, without regular retail banking."),
    ("Underwriter (Merchant Banking Context)", "An entity that guarantees to subscribe to the unsold portion of a public issue."),
    ("Loan Syndication", "A merchant banker arranging finance for a large project from a group of banks/financial institutions."),
    ("Registrar to an Issue", "The entity handling applications, allotments, and refunds in a public issue."),
    ("Debenture Trustee", "An entity appointed to protect the interests of debenture holders and monitor issuer compliance."),
]
examprep = [
    "Merchant banking (SEBI 1992) = issue management via selling/buying/subscribing securities as manager/consultant/advisor.",
    "Roles: Underwriter, Portfolio Manager, Broker, Registrar, Debenture Trustee, Banker to the Issue, Advisor.",
    "Services: Corporate Counselling, Project Counselling, Loan Syndication, Corporate Advisory (M&amp;A), Portfolio Management, Issue Management, Foreign Currency Financing, Leasing advice, Consultancy.",
]
questions = [
    ("Define merchant banking and explain its objectives.", "A merchant bank is a specialist financial institution providing issue-management, underwriting, corporate advisory, and portfolio management services without conducting regular retail banking. Its objectives include mobilising funds for corporations, supporting capital market development, and facilitating industrial growth through specialist financial services."),
    ("Explain the various roles played by a merchant banker.", "Underwriter (guaranteeing subscription of an issue), Portfolio Manager (managing client investments), Broker (obtaining subscribers), Registrar (processing applications/allotments), Debenture Trustee (protecting debenture holders), Banker to the Issue (collecting application money), and Advisor (guiding on instrument choice, quantum, and timing of an issue)."),
    ("What services do merchant banks provide to corporate clients?", "Corporate Counselling, Project Counselling (feasibility and financing pattern), Loan Syndication, Corporate Advisory on mergers/acquisitions, Portfolio Management, Issue Management, Foreign Currency Financing, leasing advice, and general financial consultancy."),
]
U.write(fname, U.page(fname, 7, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 7 done")

# ================= Topic 8: Merchant Banking - SEBI Regulation & Industry Challenges =================
fname, title, prev_link, next_link = T(8)
overview = ("Unit 5 closes by covering the pros and cons of merchant banking as an industry, the challenges it "
            "faces in India, and how it is regulated under the SEBI (Merchant Bankers) Regulations, 1992.")
notes = """
<h3>8.1 Advantages of Merchant Banking</h3>
<ol>
<li><strong>Facilitating Their Clients:</strong> Merchant bankers make the process of issuing securities and raising finance considerably easier for corporate clients, who may lack the in-house expertise to manage a public issue.</li>
<li><strong>Providing Various Types of Financial Services:</strong> Merchant banks offer a range of specialised services from corporate advisory to loan syndication under one roof.</li>
<li><strong>Supporting Management:</strong> They provide valuable strategic guidance to management on financial structuring, restructuring, and growth strategy.</li>
</ol>

<h3>8.2 Disadvantages of Merchant Banking</h3>
<ol>
<li><strong>Comparing Clients to Others:</strong> The costs and fees of merchant banking services are likely to be higher, which may be out of reach for smaller businesses/entities.</li>
<li><strong>Assessing the Suitable Combination of Products:</strong> Determining the ideal financial structure/instrument for a client requires deep expertise, and mistakes can be costly.</li>
<li><strong>Management Oversight and Individually Held Representations:</strong> Since merchant bankers deal with large and complex transactions, there is a risk that individual entities within the process may not act with the required diligence.</li>
</ol>

<h3>8.3 Challenges Faced by Merchant Banking in India</h3>
<ol>
<li><strong>Regulatory Compliance:</strong> Merchant banks operate in a system of guidelines set by regulators (SEBI, RBI, Basel III, anti-money-laundering norms) affecting how it applies to the affairs of merchant banking, requiring dedicated compliance resources.</li>
<li><strong>Management Risk:</strong> The cases in which a client's business is likely to face large corporate clients or smaller entities, individually held risk affects how various relationships are managed.</li>
<li><strong>Infrastructure of Banks:</strong> The infrastructure requirement for merchant banking businesses can be intensive (personnel, technology, office space) that they are likely to need in the field of Merchant Banking.</li>
</ol>

<h3>8.4 The SEBI (Merchant Bankers) Regulations, 1992</h3>
<p>Purpose for the regulation of merchant bankers working in the primary market:</p>
<ol>
<li>To make sure that the issuer bears minimum cost in the efficient offering of securities to the public.</li>
<li>To ensure the merchant bankers act in a fair and honest way, protecting the interest of investors.</li>
</ol>

<h3>8.5 SEBI's Rights to Inspect</h3>
<p>The SEBI can appoint one or more persons to inspect the books of accounts, records, and documents of the merchant banker for the following:</p>
<ol>
<li>To make sure the books of accounts are being maintained in the required manner.</li>
<li>For safeguarding the interests of investors.</li>
<li>The book of accounts.</li>
<li>Records, and documents of inspection.</li>
</ol>

<h3>8.6 Procedure for Registration</h3>
<p>The procedure for registration comprises of the following:</p>
<ol>
<li>If the applicant does not fall in any category to be given the exemption in Section 12 of the Act, application should be submitted to SEBI in the prescribed format.</li>
<li>The applicant should have the necessary infrastructure like adequate office space, equipment, and manpower.</li>
<li>The applicant should be a body corporate.</li>
<li>The applicant should have at least two employees with prior experience in merchant banking.</li>
<li>Any associate company, group company, subsidiary, or interconnected company of the applicant should not have been a merchant banker registered with SEBI whose registration has been cancelled.</li>
</ol>
<p>The minimum net worth of an applicant company seeking registration as a merchant banker is &#8377;5 crore.</p>

<h3>8.7 Submission of Reports to SEBI</h3>
<p>The merchant banker needs to submit reports to SEBI, including half-yearly reports on their activities and financial position, as per SEBI's regulations, to help SEBI monitor the affairs of the merchant banking industry.</p>

<h3>8.8 Action in Case of Default: Show-Cause Notice, Suspension &amp; Cancellation</h3>
<ol>
<li><strong>Show-Cause Notice:</strong> If SEBI believes a merchant banker has violated regulations, it issues a show-cause notice, giving them an opportunity to respond, before any final action against the merchant banker is initiated.</li>
<li><strong>Suspension of Registration:</strong> Registration may be suspended if the merchant banker fails to comply with SEBI rules, engages in fraud or unfair practices, or does not provide requested information to SEBI.</li>
<li><strong>Cancellation of Registration:</strong> SEBI can cancel a merchant banker's registration for repeated or serious violations, in accordance with the Act's procedure, after the merchant banker has been given a reasonable opportunity to be heard.</li>
<li><strong>Effect of Suspension/Cancellation:</strong> The merchant banker cannot take up any new assignment/business during suspension, and must cease all merchant banking activities entirely upon cancellation.</li>
<li><strong>Appeal to the Securities Appellate Tribunal:</strong> Any person aggrieved by an order of SEBI (Merchant Bankers) Regulations, 1992, can appeal to a Securities Appellate Tribunal within the prescribed time period.</li>
</ol>
"""
terms = [
    ("SEBI (Merchant Bankers) Regulations, 1992", "The regulations governing registration, conduct, inspection, and penalties for merchant bankers in India."),
    ("Show-Cause Notice", "A notice giving a merchant banker the opportunity to respond before SEBI takes disciplinary action."),
    ("Securities Appellate Tribunal (SAT)", "The tribunal where a party aggrieved by a SEBI order can appeal."),
]
examprep = [
    "Merchant banking advantages: eases fundraising for clients, one-stop specialised services, strategic management support.",
    "Merchant banking disadvantages: high cost (barrier for small firms), complexity of structuring, oversight/diligence risk on large deals.",
    "Challenges in India: regulatory compliance burden, client/relationship risk management, infrastructure requirements.",
    "SEBI (Merchant Bankers) Regulations, 1992: registration requires body corporate status, adequate infrastructure, experienced staff, min. &#8377;5 crore net worth.",
    "SEBI actions on default: Show-Cause Notice &rarr; Suspension &rarr; Cancellation, with appeal rights to the Securities Appellate Tribunal.",
]
questions = [
    ("What are the advantages and disadvantages of merchant banking?", "Advantages: eases fundraising for corporate clients, provides a range of specialist financial services under one roof, and supports management with strategic guidance. Disadvantages: relatively high cost of services (a barrier for smaller firms), the complexity of determining the right financial structure, and the risk of inadequate diligence on large, complex transactions."),
    ("Explain the registration requirements for a merchant banker under SEBI regulations.", "The applicant must be a body corporate with adequate infrastructure (office, equipment, manpower), at least two employees experienced in merchant banking, a minimum net worth of &#8377;5 crore, and no history of registration cancellation among its associate/group companies."),
    ("Explain SEBI's powers of suspension and cancellation of a merchant banker's registration.", "SEBI first issues a Show-Cause Notice giving the merchant banker a chance to respond. If violations are confirmed, SEBI can suspend the registration (barring new business) or, for serious/repeated violations, cancel it entirely after a hearing. The merchant banker can appeal any such order to the Securities Appellate Tribunal."),
]
U.write(fname, U.page(fname, 8, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Eight topics closing out the Banking &amp; Financial Services syllabus: Insurance (concept/principles/types), the Insurance Act 1938, IRDA, Venture Capital Financing, Bills Discounting, Factoring, and Merchant Banking (functions/services, and SEBI regulation/industry challenges).")

print("Unit 5 (Banking & Financial Services) complete: all 8 topics + index written.")
