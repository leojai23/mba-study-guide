# -*- coding: utf-8 -*-
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Banking-and-Financial-Services\units"
BOOK_HTML = "Book: <em>Banking and Financial Services</em> (BA4003, Anna University MBA Sem III) &mdash; Thakur Publication"
BOOK_PLAIN = "Banking and Financial Services (BA4003), Thakur Publication"
NAVY_THEME = dict(accent="#1e3a5f", accent_dark="#15293f", accent_light="#e8eef5",
                   border="#d6dfe8", shadow="rgba(30,58,95,.14)")

TOPICS = [
    ("topic1-payment-settlement-systems.html", "Payment &amp; Settlement Systems"),
    ("topic2-paper-and-electronic-payments.html", "Paper-Based &amp; Electronic Payments"),
    ("topic3-electronic-internet-banking.html", "Electronic &amp; Internet Banking"),
    ("topic4-plastic-money-cards.html", "Plastic Money &amp; Cards"),
    ("topic5-emoney-and-atms.html", "E-Money &amp; ATMs"),
    ("topic6-it-act-and-rbi-vision.html", "IT Act 2000 &amp; RBI's Digital Payments Vision"),
    ("topic7-security-threats-ebanking.html", "Security Threats in E-Banking"),
]

U = common.UnitBuilder(3, "Development in Banking Technology", TOPICS,
                        subject="Banking and Financial Services", subject_root=SUBJECT_ROOT,
                        book_html=BOOK_HTML, book_plain=BOOK_PLAIN, theme=NAVY_THEME)

def T(i):
    fname, title = TOPICS[i-1]
    prev_link = (TOPICS[i-2][0], TOPICS[i-2][1]) if i > 1 else None
    next_link = (TOPICS[i][0], TOPICS[i][1]) if i < len(TOPICS) else None
    return fname, title, prev_link, next_link

# ================= Topic 1: Payment & Settlement Systems =================
fname, title, prev_link, next_link = T(1)
overview = ("Unit 1 introduced NEFT and RTGS briefly as examples of electronic payment systems. This topic "
            "goes deeper into how India's payment and settlement infrastructure actually works, mechanically "
            "and step-by-step.")
notes = """
<h3>1.1 Payment and Settlement System in India</h3>
<p>Payment and Settlement Systems in India are covered by, and used, both by electronic and paper-based instruments. They are regulated by the Payment and Settlement Systems Act, 2007 and supervised by the Board for Regulation and Supervision of Payment and Settlement Systems (BPSS), a sub-committee of the RBI's Central Board.</p>
<p>Systems used for payment and settlement in India include: Paper Clearing, Retail Electronic Clearing (ECS, NEFT), Large Value Clearing (RTGS), Card Payment Networks, Prepaid Payment Instruments (PPIs), National Electronic Toll Collection (NETC), the National Automated Clearing House (NACH), and Unified Payments Interface (UPI).</p>

<h3>1.2 Features of RTGS</h3>
<ol>
<li>RTGS is a large-value funds transfer system where transactions are settled individually, continuously, in "real time" (not batched), and are final and irrevocable once settled.</li>
<li>The minimum amount to be remitted through RTGS is &#8377;2 lakh; there is no upper ceiling.</li>
<li>Transactions are settled in the books of the RBI, providing the highest form of settlement finality.</li>
<li>Charges may be levied by the RBI on outward transactions, per a prescribed schedule.</li>
</ol>

<h3>1.3 Objectives of RTGS</h3>
<ul>
<li>To provide real-time gross settlement to reduce risks in the interbank settlement system.</li>
<li>To widen the range of services available to include multiple value-dated transactions (as far as intangible/tangible services are concerned).</li>
<li>To bring the existing and future settlement systems on par with international standards.</li>
</ul>

<h3>1.4 Process of RTGS</h3>
<ol>
<li>The remitting customer fills in the RTGS request form providing the beneficiary's details.</li>
<li>The remitting bank prepares a message and sends it to the Reserve Bank of India, which handles it centrally.</li>
<li>After a due process step (message and settlement), the identity of the beneficiary is verified along with instructions and message details, and the amount is credited to the beneficiary's account.</li>
</ol>

<h3>1.5 Advantages and Disadvantages of RTGS</h3>
<p><strong>Advantages:</strong> Certainty in the movement of funds within RTGS since the fund transfer is final and irrevocable; faster collection of funds credited (real-time, not deferred); reduced credit and liquidity risk since settlement is transaction-by-transaction.</p>
<p><strong>Disadvantages:</strong> Higher processing charges than NEFT for smaller amounts; a minimum threshold amount is required; less cost-effective for very small-value, high-frequency transactions.</p>

<h3>1.6 National Electronic Funds Transfer (NEFT) &mdash; Process and Features</h3>
<p>NEFT refers to an electronic payment system where a person can transfer funds from an account at one bank to an account of another individual or firm/company held at any other participating bank branch. NEFT operates in hourly settlement batches (earlier half-hourly), and has moved to a 24x7 basis in recent years, unlike RTGS's continuous settlement.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Process of Sending Money via NEFT</h4>
<ol>
<li>Step 1: Customer fills in an NEFT application form authorising a bank branch to debit their account and remit a specified amount to the beneficiary.</li>
<li>Step 2: The originating bank branch prepares a message and sends it to its NEFT service centre.</li>
<li>Step 3: The NEFT Clearing Centre (National Clearing Cell of the RBI) sorts messages by destination bank and forwards them accordingly.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Role of Sending Bank, Clearing Centre &amp; Receiving Bank</h4>
<p>The Sending Bank debits the remitter's account and generates the outward message; the Clearing Centre (NCC/National Payments Corporation) processes and routes messages to the destination bank; the Receiving Bank credits the beneficiary's account upon receipt, or returns the transaction if the account/details do not match.</p>

<h3>1.7 RTGS vs NEFT</h3>
<table class="compare">
<tr><th>Basis</th><th>RTGS</th><th>NEFT</th></tr>
<tr><td>Full Form</td><td>Real Time Gross Settlement</td><td>National Electronic Funds Transfer</td></tr>
<tr><td>Settlement</td><td>Real-time, transaction-by-transaction (gross)</td><td>Batch-wise, deferred net settlement</td></tr>
<tr><td>Amount</td><td>Minimum &#8377;2 lakh, no upper limit</td><td>No minimum or maximum limit (typically used for smaller amounts)</td></tr>
<tr><td>Speed</td><td>Immediate/near-immediate</td><td>Within the current settlement batch (near real-time since the move to 24x7)</td></tr>
<tr><td>Best suited for</td><td>High-value, time-critical transfers</td><td>Retail, smaller-value transfers</td></tr>
</table>

<h3>1.8 Disadvantages of Electronic Fund Transfer (EFT) Systems</h3>
<ul>
<li>Expense associated with instituting the electronic infrastructure.</li>
<li>No physical, tangible instrument (e.g. cheque) is produced, which some users/businesses find inconvenient for record-keeping.</li>
<li>Fear of technical/system errors, delays, or fraud.</li>
<li>Loss of control by the user over the exact date/time of payment once authorised.</li>
</ul>
"""
terms = [
    ("RTGS (Real Time Gross Settlement)", "A payment system settling large-value transactions individually and immediately, with a minimum transfer amount of &#8377;2 lakh."),
    ("NEFT (National Electronic Funds Transfer)", "A nation-wide, batch-settled electronic funds transfer system, now operating on a near-24x7 basis."),
    ("BPSS", "The Board for Regulation and Supervision of Payment and Settlement Systems, a sub-committee of the RBI Central Board."),
    ("Payment and Settlement Systems Act, 2007", "The legislation regulating payment and settlement systems in India."),
]
examprep = [
    "Payment/settlement systems regulated by the Payment and Settlement Systems Act, 2007, supervised by BPSS (RBI sub-committee).",
    "RTGS: real-time, gross (individual) settlement, min. &#8377;2 lakh, no upper limit, final &amp; irrevocable.",
    "NEFT: batch-settled (now near 24x7), no minimum/maximum, suited to smaller retail transfers.",
    "RTGS vs NEFT: RTGS = high-value/time-critical; NEFT = retail/smaller-value.",
]
questions = [
    ("Explain the process of RTGS.", "The remitting customer submits an RTGS request with beneficiary details; the remitting bank prepares and sends a settlement message to the RBI; after verification, the RBI settles the transaction and the beneficiary's account is credited in real time."),
    ("Distinguish between RTGS and NEFT.", "RTGS settles each transaction individually and immediately (gross settlement) with a minimum amount of &#8377;2 lakh, suited to high-value transfers. NEFT settles transactions in batches (now near 24x7) with no minimum/maximum amount, suited to smaller retail transfers."),
    ("What are the disadvantages of electronic fund transfer systems?", "The expense of building electronic infrastructure, absence of a physical instrument for record-keeping, fear of technical errors/fraud, and the user's loss of control over the exact payment timing once authorised."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2: Paper-Based & Electronic Payments =================
fname, title, prev_link, next_link = T(2)
overview = ("Before India's shift to digital payments, paper-based instruments dominated. This topic contrasts "
            "traditional paper payments with electronic alternatives like ECS, and the general shift underway.")
notes = """
<h3>2.1 Paper-Based Payments</h3>
<p>Paper-based instruments have been the traditionally dominant mode of payment in India, accounting for nearly 60% of the volume of total non-cash transactions in the country as of the mid-2000s, though this share has since fallen sharply with the rise of digital payments.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Paper-Based Payments</h4>
<ol>
<li><strong>Cheques:</strong> A negotiable instrument instructing a bank to pay a specific amount from the drawer's account to the person named, or to the bearer.</li>
<li><strong>Demand Drafts:</strong> A prepaid negotiable instrument issued by a bank, where the bank itself undertakes to make payment in full when the instrument is presented for payment.</li>
<li><strong>Payment Orders or Banker's Cheques:</strong> An instrument issued by a bank to make payment on its own behalf, typically for a local transaction, similar to a demand draft but used within the same city/clearing zone.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Disadvantages of Paper-Based Payments</h4>
<ul>
<li>Instruments have extra costs of printing, and administrative costs of processing, verifying, and clearing paper.</li>
<li>Low commissions/float are earned by banks on paper-based instruments compared to electronic ones.</li>
<li>Physical presentation and movement of paper introduces delays, and is vulnerable to loss, theft, and fraud during handling.</li>
</ul>

<h3>2.2 Introduction to Electronic Payments</h3>
<p>According to a survey, the ratio of paper-based transactions to electronic transactions has considerably increased over a period of time between 2004 and 2008. This has happened as a result of increasing awareness of technology and increasing efficiency in facilitating e-payments for banks to route high-value transactions and also bringing the whole consumer base into compulsory intersect and non-cash mobile transactions.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of E-Payment in India</h4>
<ol>
<li>Electronic Clearing Services (ECS)</li>
<li>Electronic Funds Transfer (EFT) / National Electronic Funds Transfer (NEFT)</li>
<li>Real-Time Gross Settlement (RTGS)</li>
<li>National Electronic Toll Collection (NETC)</li>
<li>Immediate Payment Service (IMPS)</li>
<li>Unified Payments Interface (UPI)</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Disadvantages of E-Payment</h4>
<ul>
<li>Risk of being phished, cyber-attacked, or of one's password/PIN being stolen.</li>
<li>Requires a computer terminal or access to the internet, which is not universally available.</li>
<li>Lack of impulse buying behaviour, since e-payment methods make some consumers more deliberate/cautious in some cases.</li>
</ul>

<h3>2.3 Electronic Clearing Service (ECS)</h3>
<p>ECS is a mode of electronic funds transfer from one bank account to another, used for bulk/repetitive transactions, mandated by the RBI in October 2008. ECS has two variants:</p>
<table class="compare">
<tr><th>ECS Debit</th><th>ECS Credit</th></tr>
<tr><td>An account holder can give an authority letter to a utility/biller to debit their account for a payment (e.g. EMI, insurance premium, utility bills).</td><td>Used for making bulk/repetitive payments to a large number of beneficiaries, like dividend, interest, salary, or pension payments.</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Working of ECS Credit System</h4>
<p>The User institution (e.g. a company paying dividends) submits data on beneficiaries and amounts to the sponsor bank, which passes it to the ECS Centre (managed by the RBI/National Clearing Cell). Amounts are then credited to the accounts of the beneficiaries maintained with different participating banks across the country.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Advantages of ECS</h4>
<ul>
<li>Eliminates the delays and paperwork of physical instruments.</li>
<li>Beneficiaries' accounts are credited on the exact same day across the country, ensuring speed and reliability.</li>
<li>Reduces the scope for loss/fraud/theft of physical instruments in transit.</li>
</ul>

<h3>2.4 Electronic Funds Transfer (EFT)</h3>
<p>EFT is the electronic transfer of money from one bank account to another, either within a single financial institution or across multiple institutions, via computer-based systems, without the direct intervention of bank staff.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of EFT</h4>
<ol>
<li><strong>Direct Deposit:</strong> Funds transferred electronically into a recipient's bank account, commonly used for salary payments.</li>
<li><strong>Wire Transfer:</strong> A method of electronic funds transfer from one person/entity to another, through a network of banks or transfer agencies.</li>
<li><strong>Electronic Bill Payment:</strong> Paying bills (utility, telephone, etc.) electronically instead of by cheque.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Disadvantages of EFT</h4>
<ul>
<li>Some technical glitches can delay a transaction unexpectedly.</li>
<li>There is a risk of fraud if login credentials are compromised.</li>
<li>Not all beneficiaries may have bank accounts capable of receiving EFT.</li>
</ul>
"""
terms = [
    ("Demand Draft", "A prepaid negotiable instrument issued by a bank, guaranteeing payment when presented."),
    ("Electronic Clearing Service (ECS)", "A bulk/repetitive electronic funds transfer system, in Debit (utility billing) and Credit (dividends/salary) variants."),
    ("Electronic Funds Transfer (EFT)", "The electronic movement of money between bank accounts without manual bank staff intervention."),
]
examprep = [
    "Paper-based payments: Cheques, Demand Drafts, Payment Orders/Banker's Cheques &mdash; costly to process and vulnerable to delay/fraud.",
    "E-Payment types in India: ECS, EFT/NEFT, RTGS, NETC, IMPS, UPI.",
    "ECS Debit (biller debits customer for bills/EMIs) vs ECS Credit (bulk credit payments like dividends/salary).",
    "EFT types: Direct Deposit, Wire Transfer, Electronic Bill Payment.",
]
questions = [
    ("What are the disadvantages of paper-based payment instruments?", "They incur printing and processing costs, offer banks lower commission/float compared to electronic instruments, and are vulnerable to delay, loss, and fraud during physical handling and clearing."),
    ("Distinguish between ECS Debit and ECS Credit.", "ECS Debit allows a biller/utility to debit a customer's account on authorisation (e.g. EMIs, insurance premiums). ECS Credit is used for bulk credit payments to many beneficiaries at once, such as dividends, interest, salary, or pensions."),
    ("What is Electronic Funds Transfer (EFT)? Explain its types.", "EFT is the electronic movement of money between bank accounts without direct bank staff involvement. Its types include Direct Deposit (e.g. salary), Wire Transfer, and Electronic Bill Payment."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3: Electronic & Internet Banking =================
fname, title, prev_link, next_link = T(3)
overview = ("Internet/electronic banking transformed how customers interact with banks. This topic covers what "
            "e-banking is, its features and uses, and its advantages and disadvantages for both banks and "
            "customers.")
notes = """
<h3>3.1 Concept of E-Banking</h3>
<p>E-Banking, Online banking, or Net Banking refers to a system that enables bank customers to access accounts and general information on bank products and services through a personal computer, mobile, or other intelligent device, without the need to visit a physical branch of the bank.</p>
<p>The concept of internet banking is somewhat different from how it originated in the current scenario of Modern Economies (E-Banking). The overall growing use of technology in banking industry is in the process of undergoing radical changes, powered by emerging market economies (EMEs), and organisations like SWIFT (Society for Worldwide Interbank Financial Telecommunication).</p>

<h3>3.2 Objectives of E-Banking</h3>
<ul>
<li>Provides a secure, convenient, and effective method of banking.</li>
<li>To offer customers a wide range of financial and non-financial banking services at any time and place, effectively for the customer's convenience.</li>
</ul>

<h3>3.3 Features of E-Banking</h3>
<ol>
<li>A brick and mortar bank branch is no longer needed for carrying out withdrawals, deposits, and transactions.</li>
<li>Internet is used as a delivery channel of various services offered by a bank.</li>
<li>Access your bank account via mobile/internet banking, anytime and anywhere without any restriction.</li>
<li>Track and manage bank statements, transactions, balance, etc., online.</li>
<li>Password access to financial and non-financial banking services.</li>
<li>Process bill payments online via NEFT, RTGS, IMPS, etc.</li>
</ol>

<h3>3.4 Uses of E-Banking</h3>
<ol>
<li><strong>Bill Payment Service:</strong> Customers can register their various bills (electricity, telephone, insurance premiums, etc.) for online payment through the bank's portal.</li>
<li><strong>Fund Transfer:</strong> A customer can transfer funds from their account to another account with the same or a different bank, anywhere in India, using NEFT/RTGS/IMPS.</li>
<li><strong>Investing through Internet Banking:</strong> A customer can open a fixed deposit account online, apply for an IPO, or purchase/redeem mutual fund units through internet banking.</li>
<li><strong>Credit Card Customers:</strong> View credit card statements online, apply for a card, and make bill payments online.</li>
<li><strong>Recharging Prepaid Phone:</strong> Customers can recharge their prepaid mobile phones online through their bank account.</li>
<li><strong>Shopping:</strong> Customers can make purchases from e-retailers and make payments through their bank accounts.</li>
</ol>

<h3>3.5 Advantages of E-Banking</h3>
<ol>
<li><strong>Convenient:</strong> Carrying out banking transactions is convenient, since the customer's office or residence can be used.</li>
<li><strong>No Time Boundation:</strong> There is no time boundation for performing internet banking transactions, unlike a traditional bank branch that has limited hours.</li>
<li><strong>Unlimited Convenience:</strong> Carrying out any number of transactions through internet banking is easy since they are not tied to a queue or line at a physical branch.</li>
<li><strong>Easy Payment Bill:</strong> Bill payment through internet banking is easy in respect of convenience of doing so without needing to visit a bank/office.</li>
<li><strong>Easy Access to Bank Records:</strong> There are no bank records that are stored physically, which can be accessed easily/anytime online instead.</li>
</ol>

<h3>3.6 Disadvantages of E-Banking</h3>
<ol>
<li><strong>Trust Aspect:</strong> Even today, customers hesitate to adopt internet banking, since they are afraid of default frauds and are more comfortable with in-person bank staff.</li>
<li><strong>Learning Curve:</strong> The overall use of a customer's bank website takes time to get familiarised with the site's tutorials/reading materials before the customer can go on to fully understand the various methods and features of e-banking.</li>
<li><strong>Time Taking in Start-Up:</strong> For the first-time user, registration and initial set-up steps can be a lengthy process to complete.</li>
<li><strong>Efficient and Effective Internet Requirement:</strong> Various advantages and disadvantages of e-banking differ from one bank to another depending on the internet connectivity and the security scenario, effectiveness in carrying out a financial transaction in an organised manner.</li>
</ol>
"""
terms = [
    ("E-Banking (Internet Banking)", "A system enabling bank customers to access accounts and banking services electronically without visiting a physical branch."),
    ("SWIFT", "Society for Worldwide Interbank Financial Telecommunication, an organisation facilitating global electronic financial messaging."),
]
examprep = [
    "E-Banking = electronic access to bank accounts/services via computer, mobile, or other device, without visiting a branch.",
    "Uses: bill payment, fund transfer, investing (FD/IPO/mutual funds), credit card management, mobile recharge, online shopping.",
    "Advantages: convenience, no time boundation, unlimited transactions, easy bill payment, easy record access.",
    "Disadvantages: trust/fraud concerns, learning curve, lengthy initial set-up, dependence on reliable internet connectivity.",
]
questions = [
    ("What are the main uses of e-banking for a customer?", "Bill payment, fund transfer (NEFT/RTGS/IMPS), investing (fixed deposits, IPOs, mutual funds), managing credit card accounts, mobile recharge, and online shopping payments."),
    ("Explain the advantages of e-banking.", "It offers convenience (banking from anywhere), no time boundation (24x7 access), unlimited transactions without queuing, easy bill payment, and easy access to bank records online."),
    ("What are the disadvantages of e-banking?", "Customer trust/fraud concerns, a learning curve to use the bank's website effectively, a time-consuming initial registration/set-up process, and dependence on reliable internet connectivity."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4: Plastic Money & Cards =================
fname, title, prev_link, next_link = T(4)
overview = ("Plastic money transformed everyday payments. This topic covers the different card types banks "
            "issue, their features, and the key differences between the two most common cards: debit and "
            "credit.")
notes = """
<h3>4.1 Concept of Plastic Money</h3>
<p>Plastic money or polymer money is a new and easier way of paying for goods and services. Plastic money was first introduced in the 1950s and is now an essential form of ready payment, used in place of cash.</p>

<h3>4.2 Features of Plastic Money</h3>
<ol>
<li><strong>Eliminates the Need for Carrying Huge Cash:</strong> A plastic card eliminates the need to carry huge sums of cash for making payments.</li>
<li><strong>No Paperwork Required:</strong> Since plastic money does not require any paperwork to be made for carrying huge sums of cash, it is a very convenient option.</li>
<li><strong>Fixed Interest Rates:</strong> Almost every plastic money product has introduced credit cards with certain deviations in fixed price levels &mdash; a fixed credit card interest rate. But if the market evaluates like a new product, people would use the standard interest rate on cash borrowings.</li>
</ol>

<h3>4.3 Types of Plastic Money</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>ATM Card</strong></td><td>A card used to withdraw cash from a bank's automated teller machine (ATM).</td></tr>
<tr><td><strong>Debit Card</strong></td><td>Debits the cardholder's own bank account directly and immediately at the time of purchase or ATM withdrawal.</td></tr>
<tr><td><strong>Credit Card</strong></td><td>A credit card allows the customer to borrow money from the issuing institution, up to a pre-approved limit, for purchases now and pay for it later.</td></tr>
<tr><td><strong>Smart Card</strong></td><td>A card embedded with a computer chip that stores and transacts data, offering additional security and functionality (e.g. loyalty programs).</td></tr>
<tr><td><strong>Photo Card</strong></td><td>A card with a photograph of the cardholder printed on it, adding an additional layer of identity verification for the merchant.</td></tr>
<tr><td><strong>Charge Card</strong></td><td>Similar to a credit card, but the full balance must be paid off each month/billing period; no interest is charged, but late payment penalties can be severe.</td></tr>
<tr><td><strong>Affinity Card</strong></td><td>A credit card issued in partnership with an organisation (e.g. a charity or club); a portion of purchases is donated/credited to the partner organisation.</td></tr>
<tr><td><strong>Co-Branded Card</strong></td><td>Jointly issued by a bank and another company (e.g. an airline or retailer), offering rewards/benefits specific to that partner brand.</td></tr>
<tr><td><strong>Gold Card</strong></td><td>A premium credit card category, issued to customers meeting a higher income/creditworthiness threshold, with enhanced benefits.</td></tr>
<tr><td><strong>Store Card</strong></td><td>Issued by a specific retailer, usable only at that retailer's own outlets.</td></tr>
</table>

<h3>4.4 Advantages and Disadvantages of Plastic Money</h3>
<p><strong>Advantages:</strong> Reduced risk of loss/theft compared to cash; limited options for overspending (with credit limits); convenient, widely accepted globally.</p>
<p><strong>Disadvantages:</strong> Risk of loss or theft of the card itself (and resulting fraud); too much reliance on credit can lead to overspending and debt accumulation; various charges/fees (annual fees, late payment fees, foreign transaction fees) apply.</p>

<h3>4.5 Credit Cards</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Features of Credit Cards</h4>
<ul>
<li>Allows the cardholder to make purchases and pay for them later, within an interest-free period if the balance is paid in full.</li>
<li>Comes with a pre-approved credit limit set by the issuing bank based on the cardholder's creditworthiness.</li>
<li>Cardholders can also access cash via a cash advance facility (usually at a higher interest rate with no interest-free period).</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Credit Cards</h4>
<ol>
<li><strong>Bank Credit Card:</strong> Issued directly by a bank (e.g. Visa, MasterCard branded).</li>
<li><strong>Gold Cards:</strong> Premium cards with a higher credit limit and additional privileges.</li>
<li><strong>Japan Credit Bureau (JCB) Cards:</strong> Issued by the Japan Credit Bureau, mostly used in the Asia-Pacific region.</li>
<li><strong>Add-On Cards:</strong> Supplementary cards issued to family members under the primary cardholder's account.</li>
<li><strong>Fuel Cards:</strong> Co-branded with fuel companies, offering discounts/rewards on fuel purchases.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Advantages of Credit Cards</h4>
<ul>
<li>Convenient for making purchases (even expensive/impulse ones) online and offline.</li>
<li>Various reward programs (cashback, points, air miles) attached to spending.</li>
<li>Builds a credit history when used and repaid responsibly.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Disadvantages of Credit Cards</h4>
<ul>
<li>High interest rates charged if the outstanding balance is not paid in full each month.</li>
<li>Risk of overspending beyond one's means, due to the ease of using credit.</li>
<li>Various charges: annual fees, late payment fees, over-limit fees, foreign transaction fees.</li>
</ul>

<h3>4.6 Debit Cards</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Features of Debit Cards</h4>
<ul>
<li>Directly linked to the cardholder's bank account; the amount is debited immediately upon use.</li>
<li>Can be used at ATMs for cash withdrawal, and at merchant outlets for purchases (Point of Sale, POS).</li>
<li>No credit is extended; the cardholder can only spend what is available in the linked account.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Debit Cards</h4>
<ol>
<li><strong>Online Debit Card:</strong> Requires PIN entry for every transaction; funds are debited in real-time.</li>
<li><strong>Offline Debit Card:</strong> Processed like a credit card transaction (signature-based); funds are debited with a slight delay.</li>
<li><strong>Prepaid Debit Card:</strong> Loaded with a fixed amount of money in advance; not directly linked to a bank account.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Advantages of Debit Cards</h4>
<ul>
<li>Reduces the risk of overspending since only available funds can be used.</li>
<li>No interest charges since it is not a borrowing instrument.</li>
<li>Widely accepted, and convenient for both ATM withdrawal and purchases.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Disadvantages of Debit Cards</h4>
<ul>
<li>No interest-free credit period, unlike a credit card.</li>
<li>Lower fraud protection compared to credit cards in some cases.</li>
<li>Overdraft charges may apply if a transaction exceeds the available account balance.</li>
</ul>

<h3>4.7 Difference between Debit Cards and Credit Cards</h3>
<table class="compare">
<tr><th>Basis</th><th>Debit Card</th><th>Credit Card</th></tr>
<tr><td>Nature</td><td>"Pay Now" &mdash; money is debited from the cardholder's own account instantly.</td><td>"Pay Later" &mdash; money is essentially borrowed from the issuer, to be repaid later.</td></tr>
<tr><td>Mode of Operation</td><td>Real-time debit from a linked bank account.</td><td>Credit facility drawn from a pre-approved credit limit.</td></tr>
</table>
"""
terms = [
    ("Plastic Money", "Payment cards (ATM, debit, credit, and other card types) used in place of physical cash."),
    ("Debit Card", "A card that debits the cardholder's own bank account immediately upon use &mdash; a 'pay now' instrument."),
    ("Credit Card", "A card allowing the cardholder to borrow up to a pre-approved limit and repay later &mdash; a 'pay later' instrument."),
    ("Charge Card", "Similar to a credit card, but the full balance must be repaid each billing period, with no revolving interest."),
    ("Affinity Card", "A card issued in partnership with an organisation, where a portion of spending benefits that partner."),
]
examprep = [
    "Plastic money eliminates the need to carry cash, requires no paperwork, and often carries fixed interest structures.",
    "Card types: ATM, Debit, Credit, Smart, Photo, Charge, Affinity, Co-Branded, Gold, Store.",
    "Credit Card = 'Pay Later' (borrow up to a limit); Debit Card = 'Pay Now' (debits own account instantly).",
    "Debit Card types: Online (PIN, real-time), Offline (signature, delayed debit), Prepaid (pre-loaded, not account-linked).",
]
questions = [
    ("Distinguish between a debit card and a credit card.", "A debit card is a 'Pay Now' instrument that debits money directly and instantly from the cardholder's own bank account. A credit card is a 'Pay Later' instrument that lets the cardholder borrow up to a pre-approved limit from the issuer, to be repaid later, often with interest if not paid in full."),
    ("Explain the various types of credit cards.", "Bank Credit Cards (issued directly by banks), Gold Cards (premium, higher limits), JCB Cards (Asia-Pacific focused), Add-On Cards (for family members under a primary account), and Fuel Cards (co-branded with fuel companies for rewards)."),
    ("What are the advantages and disadvantages of plastic money?", "Advantages include not needing to carry cash, convenience, and wide acceptance. Disadvantages include the risk of loss/theft leading to fraud, the temptation to overspend on credit, and various fees (annual, late payment, foreign transaction) that can apply."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5: E-Money & ATMs =================
fname, title, prev_link, next_link = T(5)
overview = ("Beyond cards, this topic covers E-Money (fully digital value stored electronically) and ATMs "
            "(Automated Teller Machines), including how they work and their advantages and disadvantages for "
            "both banks and customers.")
notes = """
<h3>5.1 Concept of E-Money</h3>
<p>E-Money or electronic money refers to money or a monetary value that is stored electronically, representing a claim on the issuer, used for making payments electronically. E-Money is backed by a physical currency and can be transferred easily using computer networks, mobile phones, or a banking device.</p>

<h3>5.2 Features of E-Money</h3>
<ol>
<li><strong>Medium of Exchange:</strong> Electronic money is used as a medium of exchange, just like physical paper currency, to pay for goods and/or services.</li>
<li><strong>Standard of Deferred Payment:</strong> Electronic money is used as a means to record deferred payment, i.e. the value of the money can be transacted physically at a later date.</li>
<li><strong>Unit of Account:</strong> Electronic money is used as a common unit of value between different currencies. Let's take an example: a smartphone or a banking device is used to represent value while transacting online.</li>
</ol>

<h3>5.3 Types of E-Money</h3>
<ol>
<li><strong>Hardware-Based E-Money:</strong> Value is stored on a physical device such as a smart card or a magnetic-stripe card, which the user carries and uses at compatible terminals.</li>
<li><strong>Software-Based E-Money:</strong> Value is stored electronically on a computer system or specialised software, used to store and transfer electronic value (e.g. digital wallets and e-money accounts accessed via apps).</li>
</ol>
<p>E-Money currencies include Bitcoin and other cryptocurrencies (also called "electronic currency"), which are reversible or non-reversible, and used across various online systems and platforms outside traditional banking networks.</p>

<h3>5.4 Introduction to ATMs</h3>
<p>An Automated Teller Machine (ATM) is a computerised machine that provides the customers of a bank with the facility of accessing their bank account for a diverse range of financial transactions, without the need for a human bank teller to be physically present.</p>

<h3>5.5 Types of ATMs</h3>
<ol>
<li><strong>Onsite ATM:</strong> Installed within the premises of a bank branch.</li>
<li><strong>Offsite ATM:</strong> Installed outside the bank's own premises, at locations like shopping malls, railway stations, airports, etc., to reach a wider customer base.</li>
<li><strong>Mobile ATM:</strong> A vehicle equipped as an ATM that travels to locations to provide banking access, often used for events or temporary needs.</li>
<li><strong>Cash Dispenser:</strong> A basic ATM that offers cash withdrawal only, and does not provide other services like mini-statements or deposits.</li>
</ol>

<h3>5.6 Working of ATMs</h3>
<p>Typically, an ATM has the capacity to hold 200,000 to 200,000+ notes and can dispense up to Rs. 2.5 lakh (or more) in cash, depending on configuration. The internal cassettes are refilled by bank staff or cash management companies. ATMs are equipped with a card reader, cash dispensing mechanism, and secure network connectivity to verify the customer's PIN and account balance before processing a transaction.</p>

<h3>5.7 Features of ATMs</h3>
<ol>
<li>24x7 availability (subject to individual machine refilling/maintenance schedules).</li>
<li>Enables withdrawal, deposit, balance enquiry, mini-statements, and fund transfers.</li>
<li>Ample number of services available &mdash; PIN change, mobile recharge, and cheque book requests at many machines.</li>
<li>Confidential and secure &mdash; PIN-based authentication for each transaction.</li>
</ol>

<h3>5.8 Advantages of ATMs</h3>
<ul>
<li><strong>Convenience for Customers:</strong> Customers can withdraw cash beyond the hours of the bank branch, at any time, including holidays.</li>
<li><strong>Efficient Cash Management:</strong> Reduces the workload of bank tellers by handling routine transactions like withdrawals.</li>
<li><strong>Wide Reach:</strong> Offsite ATMs extend the bank's presence to more geographic areas without setting up full branches.</li>
</ul>

<h3>5.9 Disadvantages of ATMs</h3>
<ul>
<li><strong>To the Banks:</strong> Installation and maintenance costs (hardware, cash replenishment, network, security) can be substantial.</li>
<li><strong>Large Number of Requests:</strong> Difficulty predicting cash demand accurately can lead to a machine running out of cash or holding excess idle cash.</li>
<li><strong>Operating in Multiple Currencies:</strong> Cross-border ATM operations bring in currency conversion complications and additional charges for customers.</li>
</ul>

<h3>5.10 Forecasting Cash Demand at ATMs</h3>
<p>Efficient cash demand forecasting models are generally based on non-stationary behaviour of an ATM's historical cash withdrawal patterns and identification of unexpected demands, such as overlaid with non-stationary factors like payday cycles, weekly, monthly, and annual cycles.</p>
"""
terms = [
    ("E-Money", "Electronically stored monetary value, representing a claim on the issuer, used to make digital payments."),
    ("Hardware-Based E-Money", "E-money stored on a physical device such as a smart/magnetic-stripe card."),
    ("Software-Based E-Money", "E-money stored and transacted via computer systems or apps (e.g. digital wallets)."),
    ("ATM (Automated Teller Machine)", "A computerised machine allowing customers to perform banking transactions without a human teller."),
    ("Onsite/Offsite ATM", "ATMs located within a bank branch's own premises (onsite) or at external public locations (offsite)."),
]
examprep = [
    "E-Money features: medium of exchange, standard of deferred payment, unit of account.",
    "E-Money types: Hardware-based (cards) vs Software-based (digital wallets/apps); cryptocurrencies also count as e-money.",
    "ATM types: Onsite, Offsite, Mobile, Cash Dispenser.",
    "ATM advantages: 24x7 convenience, reduced teller workload, wider geographic reach.",
    "ATM disadvantages: installation/maintenance cost, unpredictable cash demand, cross-currency complications.",
]
questions = [
    ("What is e-money? Explain its features.", "E-money is monetary value stored electronically, representing a claim on the issuer, used for digital payments. Its features are: it serves as a medium of exchange, a standard of deferred payment, and a unit of account."),
    ("Distinguish between hardware-based and software-based e-money.", "Hardware-based e-money stores value on a physical device such as a smart card or magnetic-stripe card. Software-based e-money stores value electronically on a computer system or app, such as a digital wallet."),
    ("Explain the different types of ATMs.", "Onsite ATMs (within a bank branch), Offsite ATMs (at external public locations like malls/stations), Mobile ATMs (vehicle-based, for temporary access), and Cash Dispensers (cash withdrawal only, no other services)."),
    ("What are the advantages and disadvantages of ATMs?", "Advantages include 24x7 customer convenience, reduced workload for bank tellers, and wider geographic reach via offsite ATMs. Disadvantages include high installation/maintenance costs, difficulty forecasting cash demand accurately, and complications when operating across different currencies."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6: IT Act 2000 & RBI's Digital Payments Vision =================
fname, title, prev_link, next_link = T(6)
overview = ("Digital banking needs a legal backbone. This topic covers India's Information Technology Act, "
            "2000 (the law governing electronic transactions and digital signatures), and the RBI's forward-"
            "looking Payments Vision documents guiding the future of digital payments in India.")
notes = """
<h3>6.1 Introduction to the Information Technology Act, 2000</h3>
<p>The Information Technology Bill was passed by both houses of the Indian Parliament in May 2000, and after receiving the President's assent on 17 October 2000, it came to be known as the Information Technology Act, 2000. India became the 12th country in the world to enact cyber law, providing legal recognition to electronic records and digital signatures, and reinforcing e-commerce in the digital economy.</p>

<h3>6.2 Salient Features of the IT Act, 2000</h3>
<ol>
<li>All electronic contracts made through secure electronic channels are legally valid and enforceable.</li>
<li>Legal recognition is given to digital signatures for authentication of electronic records.</li>
<li>Security procedures for electronic records and digital signatures are defined.</li>
<li>Provisions for the appointment of a Controller of Certifying Authorities to license and regulate Certifying Authorities that issue Digital Signature Certificates.</li>
<li>The Act gives legal recognition to electronic filing of documents with government agencies, as well as electronic fund transfers between institutions/banks.</li>
<li>It also proposes a penalty and punishment for perpetrators of cybercrimes.</li>
</ol>

<h3>6.3 Objectives of the IT Act, 2000</h3>
<ul>
<li>To provide legal recognition for transactions carried out through electronic data interchange, and other means of electronic communication ("electronic commerce"), involving the use of alternatives to paper-based methods of communication.</li>
<li>To facilitate electronic filing of documents with government departments.</li>
<li>To give legal sanction and facilitate electronic storage of data.</li>
<li>To amend certain acts (Indian Penal Code, Indian Evidence Act 1872, Bankers' Books Evidence Act 1891, and the Reserve Bank of India Act 1934) to reflect this recognition of digital transactions.</li>
</ul>

<h3>6.4 Scope and Application of the IT Act, 2000</h3>
<p>The Act extends to whole of India and also applies to any offence committed outside India by any person, in violation of any provision of the Act, if the offence involves a computer, computer system, or computer network located in India. Certain instruments are excluded from the Act's application, including negotiable instruments (other than cheques), a power-of-attorney, a trust deed, a will, and any contract for the sale of immovable property.</p>

<h3>6.5 Key Definitions under the IT Act (Section 2)</h3>
<table class="compare">
<tr><th>Term</th><th>Meaning</th></tr>
<tr><td>Digital Signature</td><td>Authentication of an electronic record using an asymmetric crypto-system and hash function.</td></tr>
<tr><td>Electronic Signature</td><td>Authentication of an electronic record by any electronic technique specified in the Second Schedule.</td></tr>
<tr><td>Cyber Cafe</td><td>Any facility offering the public the facility for accessing the internet.</td></tr>
<tr><td>Computer Network</td><td>The interconnection of computers/communication devices through satellite, microwave, terrestrial, or other communication media.</td></tr>
<tr><td>Certifying Authority</td><td>A person/entity granted a licence to issue Digital Signature Certificates.</td></tr>
<tr><td>Key Pair</td><td>An asymmetric crypto-system's private key and public key, mathematically related such that the public key can verify a digital signature created by the private key.</td></tr>
</table>

<h3>6.6 RBI's Payments Vision Documents</h3>
<p>The RBI's Payments Vision documents set out the strategic direction and implementation plan for the development of India's payments ecosystem, focusing on making payment systems safe, secure, accessible, and affordable.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Goalposts of Payments Vision 2025</h4>
<ul>
<li><strong>Integrity:</strong> Weave in alternate authentication mechanisms for transactions.</li>
<li><strong>Inclusion:</strong> Enable participation of all eligible institutions/PSPs in the payments system.</li>
<li><strong>Innovation:</strong> Introduce new payment systems and products to keep pace with technology.</li>
<li><strong>Institutionalisation:</strong> Strengthen and expand the governance and regulatory framework for payments.</li>
<li><strong>Internationalisation:</strong> Enable the cross-border reach of India's domestic payment systems (like UPI, RuPay).</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Key Targets under Payments Vision 2025</h4>
<ul>
<li>Increase in registered customer base for mobile-based transactions.</li>
<li>Reduction of cash in circulation (CIC) as a percentage of GDP.</li>
<li>UPI to register average annualised growth of 50% in volume.</li>
<li>Debit card usage to surpass credit card usage in terms of value.</li>
<li>Increase in the number of PPI (Prepaid Payment Instrument) transactions.</li>
</ul>
"""
terms = [
    ("Information Technology Act, 2000", "India's cyber law giving legal recognition to electronic records and digital signatures, enacted 17 October 2000."),
    ("Digital Signature", "Authentication of an electronic record using an asymmetric crypto-system and hash function."),
    ("Certifying Authority", "An entity licensed to issue Digital Signature Certificates under the IT Act."),
    ("Payments Vision 2025", "The RBI's strategic roadmap document for developing India's digital payments ecosystem around Integrity, Inclusion, Innovation, Institutionalisation, and Internationalisation."),
]
examprep = [
    "IT Act, 2000: gives legal recognition to electronic records/digital signatures; India's 12th-in-world cyber law.",
    "IT Act objectives: legal recognition for e-commerce, facilitate e-filing, legal sanction for electronic data storage, amend related Acts (IPC, Evidence Act, RBI Act).",
    "IT Act excludes: negotiable instruments (except cheques), power-of-attorney, trust deeds, wills, immovable property sale contracts.",
    "RBI Payments Vision 2025: 5 goalposts (Integrity, Inclusion, Innovation, Institutionalisation, Internationalisation).",
]
questions = [
    ("What are the salient features of the IT Act, 2000?", "Legal validity for electronic contracts, legal recognition of digital signatures, defined security procedures for electronic records, provision for a Controller of Certifying Authorities, legal recognition of e-filing and electronic fund transfers, and penalties for cybercrimes."),
    ("What are the objectives of the IT Act, 2000?", "To give legal recognition to electronic commerce and communication, facilitate e-filing with government departments, sanction electronic storage of data, and amend related Acts (Indian Penal Code, Evidence Act, Bankers' Books Evidence Act, RBI Act) to reflect digital transactions."),
    ("Explain the goalposts of the RBI's Payments Vision 2025.", "Integrity (alternate authentication mechanisms), Inclusion (participation of all eligible institutions), Innovation (new payment products), Institutionalisation (stronger governance/regulation), and Internationalisation (cross-border reach of India's payment systems)."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 6 done")

# ================= Topic 7: Security Threats in E-Banking =================
fname, title, prev_link, next_link = T(7)
overview = ("The digital convenience of e-banking comes with new risks. This closing topic of Unit 3 catalogues "
            "the major cyber-security threats facing e-banking customers and banks, and the countermeasures "
            "and RBI initiatives used to tackle them.")
notes = """
<h3>7.1 Security Threats in E-Banking</h3>
<p>As technology continues to transform the banking landscape, cybercrimes have also become a significant challenge. Scammers pretend to be a trustworthy officer of the bank to trick customers into revealing sensitive information.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Threats</h4>
<ol>
<li><strong>Phishing:</strong> A scam where the fraudster sends fake emails/messages pretending to be from the bank, to trick users into revealing login credentials or card details.</li>
<li><strong>Pharming:</strong> Under this type of fraud, the attacker redirects a user from a legitimate website to a fake, fraudulent website without the user's knowledge, to capture their login details.</li>
<li><strong>Vishing:</strong> Similar to phishing, but conducted over the phone (voice), where a fraudster impersonates a bank official to extract sensitive information.</li>
<li><strong>Malware:</strong> Malicious software installed on a device (often without the user's knowledge) that can capture or corrupt data, or provide unauthorised access to an attacker.</li>
<li><strong>Trojan Horse/Trojan:</strong> A malicious program disguised as legitimate software, which the user installs voluntarily, allowing the attacker to access the system without the user's knowledge, in the guise of an antivirus or other trusted software.</li>
<li><strong>Virus:</strong> A malicious program that copies itself and spreads through the internet, potentially damaging files and stealing personal information from the infected system.</li>
<li><strong>Worm:</strong> Similar to a virus, but a worm can replicate itself and spread across a network without needing to attach itself to a host file or program.</li>
<li><strong>Keystroke Logger (Keylogger):</strong> Software or hardware that captures and logs every keystroke typed by a user, including passwords, and sends this data to the attacker.</li>
<li><strong>Identity Theft:</strong> Under this crime, the fraudster obtains and uses another person's personal/financial information to commit fraud, such as opening accounts or making purchases in the victim's name.</li>
<li><strong>Card Skimming:</strong> Attaching a small device (skimmer) to an ATM or POS terminal to steal card data (and a hidden camera to capture the PIN) as the card is used.</li>
<li><strong>Denial of Service (DoS) Attack:</strong> An attack aimed at making an online service/website unavailable to its legitimate users, by overwhelming it with excessive traffic.</li>
<li><strong>Password Cracking:</strong> Using techniques (brute-force, common-word dictionaries, etc.) to guess/decrypt a user's password.</li>
<li><strong>Packet Sniffers:</strong> Tools that intercept and capture data packets travelling across a network, potentially exposing sensitive information if not encrypted.</li>
<li><strong>Lottery Fraud:</strong> A scam where a victim is told they've won a lottery/prize, and is asked to pay a "processing fee" or share bank details to claim it.</li>
<li><strong>Social Engineering:</strong> Manipulating people psychologically into divulging confidential information, rather than technically breaking into a system.</li>
</ol>

<h3>7.2 RBI's Initiatives in Tackling Security Threats</h3>
<p>The RBI has mandated several security measures for banks to protect their customers, including:</p>
<ol>
<li><strong>Two-Factor Authentication (2FA):</strong> Requiring two independent forms of identification (e.g. password + OTP) before authorising a transaction.</li>
<li><strong>Encrypted Data:</strong> Mandating that sensitive data (passwords, card numbers) is encrypted, both in transit and storage, so that it is unreadable if intercepted.</li>
<li><strong>Login Details:</strong> Advising customers to never share their login credentials, PINs, or OTPs with anyone, including bank staff.</li>
<li><strong>Digital Certificates:</strong> Requiring secure website certificates (SSL/TLS) to encrypt the connection between the customer's browser and the bank's servers.</li>
<li><strong>Virtual Keyboard:</strong> Offering an on-screen virtual keyboard for entering passwords, to defeat keystroke loggers.</li>
<li><strong>Session Timeout:</strong> Automatically logging a user out after a period of inactivity, to prevent unauthorised access if a device is left unattended.</li>
<li><strong>Insta-Alerts:</strong> Sending instant SMS/email alerts for every transaction, so customers can quickly identify unauthorised activity.</li>
<li><strong>Extended Validation (EV) SSL Certificates:</strong> Providing a higher level of website authentication, visibly identifying a genuine bank site to users.</li>
</ol>

<h3>7.3 Security Measures Available to Customers</h3>
<ul>
<li>Enable transaction/login alerts, use strong and unique passwords, and change them periodically.</li>
<li>Never click on suspicious links or share OTPs/PINs over phone or email.</li>
<li>Use only official banking apps and secure (HTTPS) websites.</li>
<li>Regularly monitor bank statements for unauthorised transactions and report them immediately.</li>
</ul>
"""
terms = [
    ("Phishing", "A scam using fake emails/messages impersonating a bank to steal login credentials."),
    ("Pharming", "Redirecting a user to a fraudulent website without their knowledge to capture login details."),
    ("Vishing", "Voice-based phishing conducted over a phone call."),
    ("Card Skimming", "Using a hidden device to steal card data (and a camera for the PIN) at an ATM/POS terminal."),
    ("Two-Factor Authentication (2FA)", "Requiring two independent forms of identity verification before authorising a transaction."),
]
examprep = [
    "Key e-banking threats: Phishing, Pharming, Vishing, Malware, Trojan, Virus, Worm, Keylogger, Identity Theft, Card Skimming, DoS Attack, Password Cracking, Packet Sniffers, Lottery Fraud, Social Engineering.",
    "RBI countermeasures: Two-Factor Authentication, Data Encryption, secure login practices, Digital/SSL Certificates, Virtual Keyboards, Session Timeouts, Insta-Alerts, EV SSL Certificates.",
    "Customer-side precautions: strong unique passwords, avoiding suspicious links, using official apps/HTTPS sites, monitoring statements regularly.",
]
questions = [
    ("Explain any five common security threats in e-banking.", "Phishing (fake bank emails to steal credentials), Pharming (redirecting to a fake website), Vishing (phone-based phishing), Card Skimming (device stealing card data at ATMs/POS), and Keystroke Logging (capturing typed passwords)."),
    ("What measures has the RBI mandated to tackle e-banking security threats?", "Two-Factor Authentication, mandatory data encryption, guidance against sharing login credentials, secure SSL/digital certificates for banking websites, virtual keyboards to defeat keyloggers, automatic session timeouts, and instant transaction alerts."),
    ("What precautions should a customer take to stay safe while using e-banking?", "Use strong, unique, regularly-changed passwords; avoid clicking suspicious links or sharing OTPs/PINs; use only official banking apps and secure (HTTPS) websites; and regularly monitor bank statements to catch unauthorised transactions early."),
]
U.write(fname, U.page(fname, 7, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Seven topics covering how banking technology and digital payments work in India: payment &amp; settlement systems, paper vs electronic payments, electronic/internet banking, plastic money &amp; cards, e-money &amp; ATMs, the IT Act 2000 &amp; RBI's digital payments vision, and e-banking security threats.")

print("Unit 3 (Banking & Financial Services) complete: all 7 topics + index written.")
