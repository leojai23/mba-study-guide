# -*- coding: utf-8 -*-
import os
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Banking-and-Financial-Services\units"
BOOK_HTML = "Book: <em>Banking and Financial Services</em> (BA4003, Anna University MBA Sem III) &mdash; Thakur Publication"
BOOK_PLAIN = "Banking and Financial Services (BA4003), Thakur Publication"

TOPICS = [
    ("topic1-overview-of-indian-banking.html", "Overview of Indian Banking System"),
    ("topic2-functions-of-commercial-banks.html", "Functions of Commercial Banks"),
    ("topic3-cooperative-banks-payment-systems.html", "Co-operative Banks, NABARD &amp; Payment Systems"),
    ("topic4-rbi-and-key-regulations.html", "RBI &amp; Key Banking Regulations"),
    ("topic5-financial-statements-of-banks.html", "Overview of Financial Statements of Banks"),
    ("topic6-camels-rating-system.html", "CAMELS Rating System"),
]

NAVY_THEME = dict(accent="#1e3a5f", accent_dark="#15293f", accent_light="#e8eef5",
                   border="#d6dfe8", shadow="rgba(30,58,95,.14)")

U = common.UnitBuilder(1, "Introduction to Indian Banking System and Performance Evaluation", TOPICS,
                        subject="Banking and Financial Services", subject_root=SUBJECT_ROOT,
                        book_html=BOOK_HTML, book_plain=BOOK_PLAIN, theme=NAVY_THEME)

def T(i):
    fname, title = TOPICS[i-1]
    prev_link = (TOPICS[i-2][0], TOPICS[i-2][1]) if i > 1 else None
    next_link = (TOPICS[i][0], TOPICS[i][1]) if i < len(TOPICS) else None
    return fname, title, prev_link, next_link

# ================= Topic 1 =================
fname, title, prev_link, next_link = T(1)
overview = ("This opening topic introduces the Indian banking system: what a bank is, how it is legally "
            "defined, the different types of banks operating in India, and how the whole system is "
            "structured into scheduled and non-scheduled banks.")
notes = """
<h3>1.1 Overview of the Indian Banking System</h3>
<p>The modern banking system in India dates back to the establishment of the General Bank of India in 1786. After independence, the Reserve Bank of India (RBI), a private shareholders' bank established in 1935, was nationalised under the RBI (Transfer to Public Ownership) Act, 1948. In 1955, the Imperial Bank of India was nationalised and became the State Bank of India. In 1969, Indira Gandhi (Prime Minister) nationalised 14 major banks, and 6 more were nationalised in 1980 &mdash; by then approximately 80% of the country's banking business was under state control. Liberalisation from 1990 onwards saw private sector banks (e.g. ICICI Bank, HDFC Bank) re-enter and the sector become more competitive.</p>
<table class="compare">
<tr><th>Year</th><th>Key Event</th></tr>
<tr><td>1786</td><td>The General Bank of India, the first bank in India, was set up.</td></tr>
<tr><td>1949</td><td>The Reserve Bank of India was nationalised.</td></tr>
<tr><td>1955</td><td>The Imperial Bank of India was nationalised and became the State Bank of India.</td></tr>
<tr><td>1969</td><td>Nationalisation of 14 major banks.</td></tr>
<tr><td>1980</td><td>Nationalisation of 6 more banks.</td></tr>
<tr><td>1993</td><td>Dual exchange rate system was instituted.</td></tr>
<tr><td>1994</td><td>Full convertibility of the rupee was allowed on the current account.</td></tr>
<tr><td>2003</td><td>A new law enacted by parliament enables banks to see customers when they default on payments, by issuing notices; state-owned banks' stock prices surge in the stock market.</td></tr>
</table>

<h3>1.2 Meaning and Definition of Banking</h3>
<p>The word "bank" derives its meaning from the German word "banc", which means "bench" &mdash; the earliest bankers transacted their business at benches in a marketplace.</p>
<p><strong>Section 5(b) of the Banking Regulation Act, 1949</strong> defines banking as: "The accepting, for the purpose of lending or investment, of deposits of money from the public, repayable on demand or otherwise, and withdrawable by cheque, draft, order or otherwise."</p>
<p><strong>Section 5(c)</strong> defines a banking company as: "Any company which transacts the business of banking in India."</p>
<p>According to <strong>R.S. Sayers</strong>: "Banks are institutions whose debts (bank deposits) are widely accepted in final settlement of other people's debts."</p>
<p>According to <strong>Justice Holmes</strong>: "A bank is a shop for the sale of credit."</p>

<h3>1.3 Features of Banking</h3>
<p>Banks are financial intermediaries which transact and are engaged in the business of financial intermediaries, which are characterised by the following features:</p>
<ol>
<li>Acceptance of deposits of money from customers.</li>
<li>Lending or investing money in the business, borrowing and lending money to enterprises, businesses and companies.</li>
<li>Provides financial services, e.g. safety of money, ATM services, mobile banking, etc.</li>
<li>Repayable on demand or otherwise (withdrawable) &mdash; deposits are repayable to the depositor on demand or after an agreed period.</li>
<li>Acts as an agent to ensure economic stability and growth.</li>
</ol>

<h3>1.4 Types of Banks</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Commercial Bank</strong></td><td>A financial institution which works on a profit basis and provides deposit and loan services in general.</td></tr>
<tr><td><strong>Co-operative Bank</strong></td><td>Controlled by their own customers who are also its shareholders, formed under the co-operative societies laws.</td></tr>
<tr><td><strong>Central Bank</strong></td><td>The apex monetary institution which controls a country's whole banking system (in India, the RBI); acts as "lender of the last resort".</td></tr>
<tr><td><strong>Payments Bank</strong></td><td>Ensures the delivery of low-income group and small business banking services, especially for financial inclusion in rural areas.</td></tr>
<tr><td><strong>Small Bank</strong></td><td>Accepts deposits and grants loans on a small scale, especially aimed at unbanked/under-banked areas and small business units.</td></tr>
<tr><td><strong>Exchange Bank</strong></td><td>Promotes and finances foreign trade of a country by dealing in foreign exchange.</td></tr>
<tr><td><strong>Indigenous Bank</strong></td><td>Private moneylenders (sahukars, mahajans, sarafs, etc.) who lend their own money, mainly to the small and rural sector.</td></tr>
<tr><td><strong>Development Bank</strong></td><td>Provides medium- and long-term industrial finance and underwriting support to promote industrial development (e.g. IDBI).</td></tr>
<tr><td><strong>Export-Import Bank (EXIM Bank)</strong></td><td>Provides financial assistance to exporters and importers, incorporated on 1 January 1982 as a statutory corporation of the Government of India.</td></tr>
</table>

<h3>1.5 Structure of the Indian Banking System</h3>
<p>Banks in India are broadly classified into <strong>Scheduled Banks</strong> and <strong>Non-Scheduled Banks</strong>.</p>
<ul>
<li><strong>Scheduled Banks:</strong> Included in the Second Schedule of the RBI Act, 1934 &mdash; must have a paid-up capital of not less than &#8377;5 lakh and satisfy the RBI that their affairs are conducted in a manner not detrimental to depositors' interests. Scheduled banks are further divided into Commercial Banks (Public Sector, Private Sector, Foreign, Regional Rural Banks) and Co-operative Banks (State, Central, Primary Agricultural Credit Societies).</li>
<li><strong>Non-Scheduled Banks:</strong> Not included in the Second Schedule, are not required to comply with the various RBI/CRR requirements to the same extent, and are not fully controlled by the RBI.</li>
</ul>
"""
terms = [
    ("Bank (Sec. 5(b), Banking Regulation Act 1949)", "An institution accepting deposits of money from the public for lending or investment, repayable on demand or otherwise and withdrawable by cheque/draft/order."),
    ("Scheduled Bank", "A bank included in the Second Schedule of the RBI Act, 1934, meeting the RBI's minimum paid-up capital and conduct requirements."),
    ("Non-Scheduled Bank", "A bank not included in the Second Schedule of the RBI Act, subject to fewer RBI requirements."),
    ("Central Bank", "The apex monetary authority of a country (RBI in India) that regulates and controls the entire banking system."),
]
examprep = [
    "Banking (Sec. 5(b), Banking Regulation Act 1949) = accepting deposits for lending/investment, repayable on demand, withdrawable by cheque/draft/order.",
    "Key timeline: General Bank of India (1786) &rarr; RBI nationalised (1949) &rarr; Imperial Bank &rarr; SBI (1955) &rarr; 14 banks nationalised (1969) &rarr; 6 more (1980) &rarr; liberalisation (1990s).",
    "Types of banks: Commercial, Co-operative, Central, Payments, Small, Exchange, Indigenous, Development, EXIM.",
    "Structure: Scheduled Banks (in RBI Act's Second Schedule, min. &#8377;5 lakh paid-up capital) vs Non-Scheduled Banks.",
]
questions = [
    ("Define banking as per the Banking Regulation Act, 1949.", "Section 5(b) defines banking as the accepting, for the purpose of lending or investment, of deposits of money from the public, repayable on demand or otherwise, and withdrawable by cheque, draft, order, or otherwise."),
    ("What are the different types of banks in India?", "Commercial Banks, Co-operative Banks, Central Bank, Payments Banks, Small Banks, Exchange Banks, Indigenous Banks, Development Banks, and Export-Import (EXIM) Banks."),
    ("Distinguish between Scheduled and Non-Scheduled Banks.", "Scheduled Banks are listed in the Second Schedule of the RBI Act, 1934, must maintain a minimum paid-up capital of &#8377;5 lakh, and satisfy the RBI on the soundness of their affairs. Non-Scheduled Banks are not listed in this schedule and are subject to fewer RBI requirements."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2 =================
fname, title, prev_link, next_link = T(2)
overview = ("Commercial banks are the backbone of the banking system. This topic covers their primary "
            "functions (deposits and credit) and secondary functions (agency and utility services) in detail.")
notes = """
<h3>2.1 Commercial Banks</h3>
<p>A commercial bank is a financial institution which engages itself in all types of deposits, credit creation, granting of loans and advances, various agency functions, etc., as they are known as commercial banks.</p>

<h3>2.2 Primary Functions</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">2.2.1 Acceptance of Deposits</h4>
<p>Banks accept deposits from the public in different forms:</p>
<ol>
<li><strong>Fixed Deposit Account:</strong> Deposited for a fixed period; cannot be withdrawn before maturity without restriction/penalty; earns the highest rate of interest among the deposit types.</li>
<li><strong>Current Account:</strong> Meant for businessmen; any number of withdrawals allowed; does not yield interest to the depositor since the bank must keep enough cash to meet demands, generally used by traders/businessmen.</li>
<li><strong>Savings Bank Account:</strong> Promotes savings habits among the public; certain restrictions on number/amount of withdrawals in a given period; rate of interest is low.</li>
<li><strong>Recurring Deposit Account:</strong> A fixed sum of money is deposited every month for a fixed period; the depositor gets a lump sum amount (principal + interest) at the end.</li>
</ol>

<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">2.2.2 Advancing of Loans</h4>
<ol>
<li><strong>Overdraft:</strong> A facility to withdraw more than the balance in a current account, up to an agreed limit, with interest charged only on the overdrawn amount.</li>
<li><strong>Cash Credit:</strong> The borrower is allowed to withdraw a certain amount on a given security; interest is charged on the amount actually withdrawn, not the whole limit sanctioned.</li>
<li><strong>Consumer Credit:</strong> Loans given to consumers to purchase durables (e.g. household appliances), typically repaid in instalments.</li>
<li><strong>Term Loan:</strong> Loans given for a fixed period (short/medium/long-term) for capital expenditure such as purchase of machinery or land, usually repaid in instalments.</li>
<li><strong>Discounting Bills of Exchange:</strong> The holder of a bill can get it discounted (encashed before maturity) with the bank, which deducts a discount charge and credits the remaining amount.</li>
<li><strong>Money at Call:</strong> Very short-term loans (one day to a fortnight) given to other banks or dealers in the money market, repayable at very short notice.</li>
</ol>

<h3>2.3 Secondary Functions</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">2.3.1 Agency Functions</h4>
<p>Banks act as agents of their customers and perform several functions on their behalf, for a commission:</p>
<ol>
<li><strong>Collection of Cheques and Bills:</strong> Banks collect cheques and bills of exchange on behalf of their customers through the clearing system.</li>
<li><strong>Payment of Various Items:</strong> Banks make payments on standing instructions from customers &mdash; insurance premiums, rent, electricity/telephone bills, etc.</li>
<li><strong>Purchase and Sale of Securities:</strong> Banks purchase and sell shares/securities on behalf of customers, though they do not give advice on which securities to buy/sell.</li>
<li><strong>Collecting Dividends on Shares:</strong> Banks collect dividends, interest on debentures, and other periodic income due to customers on securities held.</li>
<li><strong>Acting as Trustee and Executor:</strong> Banks act as trustees and executors of the property/wills of their customers, on customers' instructions.</li>
<li><strong>Acting as Correspondent:</strong> Banks act as correspondents/representatives of their customers, other banks, and institutions, especially in obtaining passports, travel tickets, etc.</li>
</ol>

<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">2.3.2 Utility (General) Functions</h4>
<ol>
<li><strong>Issuing Letters of Credit:</strong> Banks issue letters of credit to certify the creditworthiness of their customers, especially useful in foreign trade.</li>
<li><strong>Underwriting Securities:</strong> Banks underwrite the shares and debentures issued by joint stock companies, by agreeing to buy shares not otherwise subscribed by the public.</li>
<li><strong>Dealing in Foreign Exchange:</strong> Banks deal in the purchase and sale of foreign exchange, facilitating international trade.</li>
<li><strong>Safe Deposit Locker:</strong> Banks provide lockers for the safe custody of valuable documents, jewellery, and other valuables of customers.</li>
<li><strong>Traveller's Cheques:</strong> Banks issue traveller's cheques to help travellers who need not carry cash and can encash them when needed.</li>
<li><strong>Collection of Statistics/Information:</strong> Banks collect and provide statistics/information related to trade, commerce, and industry, and advise customers on business matters.</li>
</ol>

<h3>2.4 Co-operative Banks</h3>
<p>Co-operative banks are formed under the Co-operative Societies Act and finance small-scale industries, agriculturists, and other economically weaker sections at concessional rates, mainly to promote thrift, self-help, and co-operation among members with common economic needs.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">2.4.1 Functions of Co-operative Banks</h4>
<ol>
<li>Providing banking facilities to small-scale industries and small businesses.</li>
<li>Providing financial assistance to rural areas for agricultural purposes.</li>
<li>Fulfilment of socio-economic objectives: elimination of poverty, decentralisation of certain socio-economic activities, and fulfilment of national policy objectives.</li>
</ol>

<h3>2.5 NABARD (National Bank for Agriculture and Rural Development)</h3>
<p>NABARD serves the functions of a link between the Central and State Governments and co-operative banks, and provides short-term and medium-term credit for agriculture through State Co-operative Banks and Regional Rural Banks. It provides refinance facilities to SCBs, RRBs, and DCCBs.</p>

<h3>2.6 Non-Scheduled Banks</h3>
<p>Non-scheduled banks are the banks which are not included in the Second Schedule of the RBI Act, 1934, and are not required to comply with the various provisions applicable to scheduled banks, though the RBI can still monitor them.</p>
"""
terms = [
    ("Overdraft", "A facility allowing withdrawal beyond the current account balance up to an agreed limit, with interest on the overdrawn amount only."),
    ("Cash Credit", "A credit facility where the borrower withdraws against a sanctioned limit secured by collateral, paying interest only on the amount actually used."),
    ("Discounting of Bills", "Encashing a bill of exchange with a bank before its maturity date, in exchange for a discount charge."),
    ("Co-operative Bank", "A bank formed under the Co-operative Societies Act, controlled by its own member-customers, mainly serving small-scale and agricultural credit needs."),
    ("NABARD", "National Bank for Agriculture and Rural Development &mdash; refinances and links Central/State Governments with co-operative and rural banks for agricultural credit."),
]
examprep = [
    "Primary functions: Deposits (Fixed, Current, Savings, Recurring) + Loans (Overdraft, Cash Credit, Consumer Credit, Term Loan, Bill Discounting, Money at Call).",
    "Secondary functions: Agency (collection of cheques/bills, standing payments, buying/selling securities, dividend collection, trustee/executor, correspondent) + Utility (letters of credit, underwriting, forex dealing, lockers, traveller's cheques, statistics).",
    "Co-operative banks serve small-scale industry/agriculture at concessional rates; NABARD refinances them for agricultural credit.",
]
questions = [
    ("Explain the primary functions of a commercial bank.", "Primary functions consist of Accepting Deposits (Fixed, Current, Savings, Recurring accounts) and Advancing Loans (Overdraft, Cash Credit, Consumer Credit, Term Loans, Discounting Bills, Money at Call)."),
    ("Differentiate between Overdraft and Cash Credit.", "Overdraft allows a current-account holder to withdraw beyond their balance up to an agreed limit, with interest on the overdrawn amount. Cash Credit is a separate credit facility secured against collateral, where the borrower draws up to a sanctioned limit and pays interest only on the amount actually withdrawn."),
    ("Explain the agency and utility (general) functions of commercial banks.", "Agency functions include collecting cheques/bills, making standing payments, buying/selling securities, collecting dividends, and acting as trustee/executor/correspondent. Utility functions include issuing letters of credit, underwriting securities, dealing in foreign exchange, providing safe deposit lockers, issuing traveller's cheques, and providing trade/business information."),
    ("What role does NABARD play in the Indian banking system?", "NABARD acts as a link between the Central/State Governments and co-operative banks, providing short- and medium-term agricultural credit and refinance facilities to State Co-operative Banks, Regional Rural Banks, and District Central Co-operative Banks."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3 =================
fname, title, prev_link, next_link = T(3)
overview = ("Beyond individual bank functions, this topic looks at financial intermediation as a system-wide "
            "process, the electronic payment infrastructure that moves money between banks, and how financial "
            "services are classified as either asset-based or fee-based.")
notes = """
<h3>3.1 Intermediation</h3>
<p>Financial intermediation is the process by which financial intermediaries (banks and other financial institutions) borrow surplus funds from savers (who are willing to lend) and channel them to borrowers who need funds, in an organised manner. Financial intermediaries have the benefit of getting a broad network of banks for mobilising funds and diverting them for the benefit and development of a country's financial system.</p>

<h3>3.2 Functions of the Indian Banking System</h3>
<p>The basic objective of putting in place a payment system is a robust, resilient, and efficient payment infrastructure. This foundation stone, essential for the development of a country's economy, is achieved through: accurate and timely settlement, safety and security of transactions, and overcoming various economic risks such as maturity mismatches (financial intermediaries borrow short-term and lend long-term, which creates a maturity mismatch that must be managed).</p>

<h3>3.3 Payment System</h3>
<p>Currency (cash) continues to be a popular mode of payment. However, the RBI and banks are working to increase the usage of the following kinds of electronic payment systems:</p>
<ol>
<li><strong>National Electronic Funds Transfer (NEFT):</strong> A nation-wide payment system facilitating one-to-one funds transfer between bank accounts. Transactions are settled in batches at fixed intervals throughout the day (deferred net settlement), unlike RTGS which settles instantly and individually.</li>
<li><strong>Real Time Gross Settlement (RTGS):</strong> A system where transfer of funds takes place from one bank to another on a "real time" and "gross" basis. Settlement is done individually and immediately (not batched), making it the fastest inter-bank money transfer system; typically used for high-value transactions above a minimum threshold.</li>
<li><strong>Negotiated Dealing System (NDS):</strong> An electronic platform for facilitating dealing in government securities and money market instruments among participants such as banks, financial institutions, and primary dealers, screen-based and paperless.</li>
<li><strong>Electronic Clearing Service (ECS):</strong> Used for bulk/repetitive payments such as dividends, interest, salary, or pension, transferred electronically from one bank account to many, or many to one (e.g. utility bill collection).</li>
<li><strong>Electronic Funds Transfer (EFT):</strong> The electronic transfer of money from one bank account to another, either within a single financial institution or across multiple institutions, without direct intervention of bank staff.</li>
</ol>

<h3>3.4 Asset-Based Financial Services</h3>
<p>Asset-based financial services deal directly with the creation of assets, instead of dealing in funds directly. They include leasing, hire purchase, factoring, forfaiting, and venture capital financing &mdash; each provides the use of an asset or funding tied to an underlying asset, rather than an unsecured loan.</p>

<h3>3.5 Fee/Non-Fund Based Financial Services</h3>
<p>Fee-based financial services do not create new assets but generate income through advice, management, and other specialised services in the areas of management, i.e. rendering various types of services on a fee basis, e.g. merchant banking, credit rating, portfolio management, and other consultancy activities. Traditional activities in this category include the underwriting of shares/debentures, and modern activities include stock broking, merchant banking, mutual funds, and other financial services offered by banks and non-banking financial companies.</p>
"""
terms = [
    ("Financial Intermediation", "The process of channelling surplus funds from savers to borrowers through financial institutions like banks."),
    ("NEFT", "National Electronic Funds Transfer &mdash; a deferred, batch-settled nation-wide electronic funds transfer system."),
    ("RTGS", "Real Time Gross Settlement &mdash; instant, individual (non-batched) high-value fund transfer system."),
    ("Asset-Based Financial Services", "Services (leasing, hire purchase, factoring, forfaiting, venture capital) tied to the creation or use of an asset rather than direct funding."),
    ("Fee-Based Financial Services", "Non-fund services generating income through advice/management, e.g. merchant banking, credit rating, portfolio management."),
]
examprep = [
    "Intermediation = channelling savers' surplus funds to borrowers via banks/financial institutions.",
    "Key electronic payment systems: NEFT (batched/deferred), RTGS (real-time/gross, high-value), NDS (govt securities dealing), ECS (bulk payments), EFT (general electronic transfer).",
    "Asset-Based Financial Services (leasing, hire purchase, factoring, forfaiting, venture capital) vs Fee-Based Financial Services (merchant banking, credit rating, portfolio management).",
]
questions = [
    ("Distinguish between NEFT and RTGS.", "NEFT settles transactions in batches at fixed intervals (deferred net settlement) and suits smaller-value transfers, while RTGS settles each transaction individually and instantly (real-time gross settlement), making it suited to high-value, time-critical transfers."),
    ("What is financial intermediation? Why is it important?", "Financial intermediation is the process by which banks and financial institutions channel surplus funds from savers to borrowers in an organised manner. It is important because it mobilises funds efficiently and channels them toward productive use, supporting a country's economic development."),
    ("Differentiate between asset-based and fee-based financial services.", "Asset-based financial services (leasing, hire purchase, factoring, forfaiting, venture capital) are tied to the creation or use of an underlying asset. Fee-based financial services (merchant banking, credit rating, portfolio management) generate income through advice and specialised services rather than funding an asset directly."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4 =================
fname, title, prev_link, next_link = T(4)
overview = ("The Reserve Bank of India is the central regulator of the entire banking system. This topic "
            "covers RBI's functions, the key Acts that govern Indian banking (the RBI Act, Banking Regulation "
            "Act, and Negotiable Instruments Act), and how banks classify and provide for bad loans (NPAs).")
extra_note = '<div class="callout warn">The Banking Regulation Act and Negotiable Instruments Act each run to dozens of numbered Sections in the book. Rather than listing every Section number, this topic summarises their purpose, structure, and the specific provisions most relevant for exams.</div>'
notes = """
<h3>4.1 Introduction to the RBI</h3>
<p>The Reserve Bank of India (RBI) was established on 1 April 1935 under the Reserve Bank of India Act, 1934, initially as a shareholders' bank. It was nationalised in 1949 and is now fully owned by the Government of India. The RBI is the central bank of India and is at the apex of the country's monetary and banking structure.</p>

<h3>4.2 Reasons for Nationalisation of the RBI</h3>
<ul>
<li>It was seen as unfair that various central banking functions of the country should be controlled by a bank owned by private shareholders.</li>
<li>Government felt currency and credit management were too important to be left under private control.</li>
<li>Nationalisation was required so that the Central Bank could pursue policy independent of the interests of its shareholders.</li>
</ul>

<h3>4.3 Functions of RBI</h3>
<table class="compare">
<tr><th>Category</th><th>Functions</th></tr>
<tr><td><strong>Monetary Functions</strong></td><td>Issue of currency notes, Banker to the Government, Banker's Bank, Lender of the Last Resort, Custodian of Foreign Exchange Reserves, Controller of Credit.</td></tr>
<tr><td><strong>Non-Monetary Functions</strong></td><td>Supervisory functions and Promotional functions.</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Monetary Functions in Detail</h4>
<ol>
<li><strong>Issue of Bank Notes:</strong> The RBI has the sole right to issue currency notes (except one-rupee notes/coins, issued by the Government) under the "Minimum Reserve System".</li>
<li><strong>Banker to Government:</strong> The RBI acts as banker to both Union and State Governments, receiving and paying money on their behalf, and manages their public debt.</li>
<li><strong>Banker's Bank:</strong> Every scheduled bank is required to keep a certain minimum cash reserve with the RBI (CRR/SLR requirements).</li>
<li><strong>Lender of the Last Resort:</strong> The RBI provides financial help to commercial banks during a financial crunch by rediscounting bills of exchange, providing emergency advances.</li>
<li><strong>Custodian of Foreign Exchange Reserves:</strong> The RBI keeps and manages the country's foreign exchange reserves and controls foreign exchange under FEMA regulations.</li>
<li><strong>Credit Control:</strong> The RBI controls the volume and direction of credit through quantitative (CRR, SLR, Bank Rate, Repo Rate) and qualitative (margin requirements, moral suasion) methods.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Non-Monetary (Supervisory &amp; Promotional) Functions</h4>
<ol>
<li><strong>Grant of Licence:</strong> The RBI has the right to issue licences for banks to commence banking business, and can cancel a licence if required.</li>
<li><strong>Regulation of Weak Banks:</strong> Under the Banking Regulation Act, RBI can call for information about banks and inspect/regulate weak banks, requiring stronger banks to merge with them if needed.</li>
<li><strong>Control over Bank Operations:</strong> Through licensing, branch expansion, liquidity of assets, management, and amalgamation, reconstruction, and liquidation.</li>
<li><strong>Periodical Review:</strong> RBI conducts periodic review/inspection of banks' functioning.</li>
<li><strong>Promotion of Banking Habits:</strong> RBI works to promote banking habits and spread banking to rural and unbanked areas.</li>
<li><strong>Training:</strong> RBI has set up training institutes for the banking sector, such as the National Institute of Bank Management (NIBM, Pune), College of Agricultural Banking (Pune), Bankers Training College (Mumbai), and various Zonal Training Centres.</li>
<li><strong>Collection and Furnishing of Credit Information:</strong> RBI collects credit information about borrowers and furnishes it to banks to help them assess a borrower's creditworthiness.</li>
</ol>

<h3>4.4 Scheme of the RBI Act, 1934</h3>
<p>The RBI Act consists of a short title, extent, and commencement, followed by several chapters covering (in brief): Incorporation, Capital, Management (Chapter II); Business of the Bank (Chapter III); General Provisions on deposits, reserve fund, and derivatives (Chapter IIIB-IV); Collection and Furnishing of Credit Information (Chapter IIIA); Provisions Relating to Non-Banking Institutions Receiving Deposits (Chapter IIIC); Prohibition of Acceptance of Deposits by Unincorporated Bodies (Chapter IIID); Regulation of Transactions in Derivatives, Money Market Instruments and Securities (Chapter IIIF); Penalties (Chapter V).</p>

<h3>4.5 Provisions Relating to CRR (Cash Reserve Ratio)</h3>
<p>Under Section 42(1) of the RBI Act, 1934, every scheduled bank is required to maintain a certain minimum cash reserve with the RBI, known as the Cash Reserve Ratio (CRR), calculated as a percentage of its Net Demand and Time Liabilities (NDTL). The RBI has the power to change the CRR requirement (within statutory limits) to influence liquidity in the banking system.</p>

<h3>4.6 Provision for Non-Performing Assets (NPAs)</h3>
<p>An asset, including a leased asset, becomes a Non-Performing Asset (NPA) when it ceases to generate income for the bank. Banks are required to classify their loan assets and make provisioning (setting aside funds to cover expected losses) as follows:</p>
<table class="compare">
<tr><th>Category</th><th>Meaning</th></tr>
<tr><td><strong>Standard Assets</strong></td><td>Assets that do not carry more than the normal risk attached to the business &mdash; not classified as an NPA.</td></tr>
<tr><td><strong>Sub-Standard Assets</strong></td><td>An asset classified as an NPA for a period not exceeding 12 months, where the current net worth of the borrower is inadequate.</td></tr>
<tr><td><strong>Doubtful Assets</strong></td><td>An asset that has remained in the sub-standard category for a period of 12 months; full recovery of the debt is doubtful.</td></tr>
<tr><td><strong>Loss Assets</strong></td><td>An asset where loss has been identified but the amount has not been written off wholly, considered uncollectible with very little realisable value.</td></tr>
</table>
<p>Provisioning norms require banks to make general provisions on standard assets (e.g. 0.25%-1% depending on sector) and progressively higher provisions on sub-standard, doubtful, and loss assets, in accordance with RBI's prudential guidelines.</p>

<h3>4.7 The Securitisation and Reconstruction of Financial Assets (SARFAESI) Act, 2002</h3>
<p>The SARFAESI Act empowers banks and financial institutions to recover their non-performing assets without the intervention of a court, through seizure and sale of secured assets, and enables the setting up of Asset Reconstruction Companies (ARCs) to acquire and resolve NPAs from banks.</p>

<h3>4.8 Banking Regulation Act, 1949 &mdash; Purpose and Key Themes</h3>
<p>This is a special Act primarily regulating the banking sector in India, providing a framework for the licensing, management, suspension, and winding-up of banking companies. Its key themes include:</p>
<ul>
<li>Licensing and permissible business activities of banking companies (which businesses a bank may/may not engage in).</li>
<li>Minimum paid-up capital and reserve requirements for banks.</li>
<li>Regulation of management &mdash; qualifications and restrictions on directors/chairpersons.</li>
<li>Provisions relating to acquisition, amalgamation, and winding-up of banking companies.</li>
<li>Powers of the RBI to inspect and issue directions to banks, and to regulate matters like moratoriums during a bank's financial distress.</li>
<li>Separate provisions applicable to Co-operative Banks and Private Sector/Public Sector Banks.</li>
</ul>

<h3>4.9 Negotiable Instruments Act, 1881 &mdash; Meaning and Features</h3>
<p>A negotiable instrument is a document that can be transferred, like cash, from one person to another. According to <strong>Section 13(1)</strong> of the Act, "A negotiable instrument means a promissory note, bill of exchange, or cheque payable either to order or to bearer."</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Features of Negotiable Instruments</h4>
<ol>
<li><strong>Writing and Signature:</strong> A negotiable instrument must be in writing and signed by the maker/drawer.</li>
<li><strong>Money:</strong> Negotiable instruments only relate to payment of money.</li>
<li><strong>Freely Transferable:</strong> It is possible to freely transfer a negotiable instrument, either by delivery or by endorsement and delivery.</li>
<li><strong>Title of Holder Free from All Defects:</strong> A holder in due course gets the instrument free from any defects in the title of the transferor.</li>
<li><strong>Right to Sue:</strong> The holder in due course can sue in their own name to recover the amount due.</li>
<li><strong>Notice Not Required:</strong> Transfer of a negotiable instrument does not require notice to the party liable to pay.</li>
<li><strong>Presumptions:</strong> Certain presumptions apply automatically to every negotiable instrument (e.g. presumption of consideration).</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Types of Negotiable Instruments</h4>
<p>Recognised by the Act: <strong>Promissory Notes</strong>, <strong>Bills of Exchange</strong>, and <strong>Cheques</strong>. Also recognised by custom/usage (not by the Act itself): Hundis, Share Warrants, Circular Notes, Bearer Debentures, and Dividend Warrants.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Key Provisions</h4>
<ul>
<li><strong>Holder:</strong> A person entitled in their own name to the possession of the instrument and to receive/recover the amount due.</li>
<li><strong>Holder in Due Course:</strong> A person who has obtained the instrument for consideration, in good faith, before maturity, and without knowledge of any defect in title.</li>
<li><strong>Endorsement:</strong> Signing a negotiable instrument (usually on the back) for the purpose of negotiation, transferring the right to the endorsee.</li>
<li><strong>Crossing of a Cheque:</strong> Drawing two parallel transverse lines on a cheque, directing the paying bank to pay only through a bank account (not over the counter), for safety.</li>
<li><strong>Dishonour:</strong> An instrument is dishonoured by non-acceptance (bill of exchange) or by non-payment (when the drawee/acceptor fails to pay on presentment).</li>
<li><strong>Liability of Parties:</strong> The maker (promissory note), drawer/acceptor (bill of exchange/cheque), and every endorser are each liable to a holder in due course, in the order they became parties, unless otherwise agreed.</li>
</ul>
"""
terms = [
    ("RBI Act, 1934", "The Act under which the Reserve Bank of India was established as India's central bank."),
    ("CRR (Cash Reserve Ratio)", "The minimum percentage of Net Demand and Time Liabilities that scheduled banks must keep as cash reserves with the RBI."),
    ("Non-Performing Asset (NPA)", "A loan asset that has stopped generating income for the bank, classified as Sub-Standard, Doubtful, or Loss depending on how long it has remained non-performing."),
    ("SARFAESI Act, 2002", "Allows banks to recover NPAs by seizing and selling secured assets without court intervention, and enables Asset Reconstruction Companies."),
    ("Negotiable Instrument", "A written, signed document (promissory note, bill of exchange, or cheque) that can be freely transferred like cash, as defined in Section 13(1) of the Negotiable Instruments Act, 1881."),
    ("Holder in Due Course", "A person who acquires a negotiable instrument for consideration, in good faith, before maturity, without notice of any defect in title."),
]
examprep = [
    "RBI (est. 1935, nationalised 1949) performs Monetary functions (currency issue, banker to govt, banker's bank, lender of last resort, forex custodian, credit control) and Non-Monetary functions (licensing, supervision, promotion, training).",
    "CRR (Sec. 42(1), RBI Act 1934) = minimum cash reserve scheduled banks must keep with RBI, as % of NDTL.",
    "NPA classification: Standard &rarr; Sub-Standard (up to 12 months) &rarr; Doubtful (over 12 months) &rarr; Loss (identified, uncollectible).",
    "SARFAESI Act 2002 lets banks recover NPAs without court intervention via seizure/sale of secured assets.",
    "Banking Regulation Act 1949 governs licensing, capital, management, and winding-up of banking companies.",
    "Negotiable Instruments Act 1881 (Sec. 13): covers Promissory Notes, Bills of Exchange, Cheques &mdash; freely transferable, holder-in-due-course gets clean title, no notice required for transfer.",
]
questions = [
    ("Explain the monetary functions of the RBI.", "Issue of currency notes (sole right under the Minimum Reserve System), Banker to Government, Banker's Bank (holding CRR/SLR of scheduled banks), Lender of the Last Resort, Custodian of Foreign Exchange Reserves, and Controller of Credit (via CRR, SLR, Bank Rate, Repo Rate, and qualitative controls)."),
    ("What is CRR? How is it governed under the RBI Act, 1934?", "CRR (Cash Reserve Ratio) is the minimum percentage of Net Demand and Time Liabilities that every scheduled bank must maintain as cash reserves with the RBI, under Section 42(1) of the RBI Act, 1934. The RBI can vary the CRR within statutory limits to manage liquidity."),
    ("Explain the classification of Non-Performing Assets (NPAs).", "Standard Assets carry normal risk and are not NPAs. Sub-Standard Assets have been NPAs for up to 12 months. Doubtful Assets have remained sub-standard for over 12 months, making full recovery doubtful. Loss Assets are identified as uncollectible, with the loss not yet written off."),
    ("What is a negotiable instrument? State its key features.", "As per Section 13(1) of the Negotiable Instruments Act, 1881, it is a promissory note, bill of exchange, or cheque payable to order or bearer. Key features: must be in writing and signed, relates only to payment of money, is freely transferable, gives a holder in due course a title free of defects, the right to sue in their own name, requires no notice for transfer, and carries certain automatic legal presumptions."),
    ("What is the significance of the SARFAESI Act, 2002?", "It empowers banks and financial institutions to recover non-performing assets without court intervention, by seizing and selling secured assets, and allows the formation of Asset Reconstruction Companies to acquire and resolve NPAs."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link, extra_note=extra_note))
print("Topic 4 done")

# ================= Topic 5 =================
fname, title, prev_link, next_link = T(5)
overview = ("Banks prepare two sets of financial statements each year: the Balance Sheet and the Profit & "
            "Loss Account. This topic covers their prescribed formats and what each line item represents.")
notes = """
<h3>5.1 Balance Sheet of a Bank</h3>
<p>The Balance Sheet records the assets, liabilities, and net worth of a bank at a particular point in time. As per Section 29 of the Banking Regulation Act, 1949, every banking company is required to prepare a Balance Sheet as on the last working day of the year, in Form 'A' of the Third Schedule.</p>
<p><strong>Capital and Net Worth:</strong> Capital is the owned funds of a bank's balance sheet, referring to the equity/right-hand side of the balance sheet. Liabilities are the amounts owed by the bank to others, and the assets are the properties owned by the bank. Net Worth is the difference between the bank's assets and liabilities, and should be equal to the summation of the difference between capital and reserves (Assets &minus; Liabilities = Capital + Reserves).</p>

<h3>5.2 Components of Liabilities</h3>
<ol>
<li><strong>Capital:</strong> Issued, subscribed, and paid-up capital of the bank &mdash; the highest amount of equity capital that can be issued, as per the Memorandum of Association. Authorised Capital is the highest amount a company can issue to the public; Issued Capital is the part of authorised capital actually issued; Subscribed Capital is the part of issued capital that is applied for by shareholders; Paid-Up Capital is the amount shareholders have actually paid.</li>
<li><strong>Reserves and Surplus:</strong> The Reserve Bank is bound to maintain a portion of its profits in a reserve account under the Banking Regulation Act, 1949. As per the Act, banks need to maintain their reserves at 20% of their profit, transferring it into other reserves like the Statutory Reserve, Capital Reserve, and Investment Fluctuation Reserve, until the accumulated reserve equals the paid-up capital.</li>
<li><strong>Deposits:</strong> The major part of a bank's fund is sourced from deposits &mdash; Demand Deposits (Current and Savings, repayable on demand) and Term Deposits (Fixed and recurring deposits with a fixed maturity).</li>
<li><strong>Other Liabilities and Provisions:</strong> Includes bills payable, interest accrued, and other provisions for bad and doubtful debts, taxation, etc.</li>
</ol>

<h3>5.3 Components of Assets</h3>
<ol>
<li><strong>Cash and Balances with Reserve Bank of India:</strong> Cash in hand (notes and coins) and balances the bank maintains with the RBI, including for CRR requirements.</li>
<li><strong>Balances with Banks and Money at Call:</strong> Balances held with other banks and short-notice/call money lent to other banks or the money market.</li>
<li><strong>Investments:</strong> Investments in government and other approved securities, shares, debentures, bonds, subsidiaries, and joint ventures, as part of SLR requirements and otherwise.</li>
<li><strong>Advances:</strong> The banker grants advances in the form of loans, cash credit, overdrafts, bills purchased and discounted &mdash; the main and most liquidating theory-following component of the assets, forming the main source of the bank's income.</li>
<li><strong>Fixed Assets:</strong> Premises, furniture and fixtures owned by the bank, shown net of accumulated depreciation.</li>
<li><strong>Other Assets:</strong> Interest accrued, tax paid in advance, stationery, stamps, non-banking assets acquired in satisfaction of claims, etc.</li>
</ol>

<h3>5.4 Profit and Loss Account</h3>
<p>The Profit and Loss account of any bank is prepared in Form 'B' of the Third Schedule of the Banking Regulation Act, 1949. It can be made in a vertical form as follows.</p>
<ol>
<li><strong>Income:</strong> Includes the following two important sections: <strong>Interest Earned</strong> (interest and discount on advances/bills, income on investments, interest on balances with RBI/other inter-bank funds) and <strong>Other Income</strong> (commission, exchange, brokerage, profit on sale of investments, profit on exchange transactions, etc.).</li>
<li><strong>Expenditure:</strong> Includes <strong>Interest Expended</strong> (interest paid on deposits, borrowings, and inter-bank borrowings), <strong>Operating Expenses</strong> (payments to and provisions for employees, rent/taxes/lighting, printing and stationery, advertisement, depreciation, director's fees, auditor's fees, law charges, postage, insurance, and other expenditure), and <strong>Provisions and Contingencies</strong> (for bad and doubtful debts, taxation, and other contingencies).</li>
<li><strong>Profit or Loss:</strong> This section discloses the difference between total income and total expenditure. If income exceeds expenses, it is a profit; if expenses exceed revenues, it is a loss.</li>
<li><strong>Appropriations:</strong> This shows how the profit for the year is appropriated &mdash; transfer to statutory reserves, other reserves, proposed dividends, and the balance carried forward to the Balance Sheet.</li>
</ol>

<h3>5.5 Schedules of the Balance Sheet and Income Statement</h3>
<p>The banks in India have to prepare their financial statements in accordance with the Third Schedule of the Banking Regulation Act, using a typical pattern of Schedules 1-16 (e.g. Schedule 1: Capital, Schedule 2: Reserves and Surplus, Schedule 3: Deposits, Schedule 6: Cash and Balances with RBI, Schedule 9: Advances, Schedule 13: Interest Earned, Schedule 16: Operating Expenses), accompanied by notes to accounts and significant accounting policies, as typically also required by RBI disclosure norms.</p>
"""
terms = [
    ("Balance Sheet (Bank)", "A statement of a bank's assets, liabilities, and net worth as of a specific date, prepared in Form 'A' of the Third Schedule under Section 29 of the Banking Regulation Act, 1949."),
    ("Net Worth", "The difference between a bank's total assets and total liabilities, equal to capital plus reserves."),
    ("Profit and Loss Account (Bank)", "A statement of a bank's income and expenditure for a year, prepared in Form 'B' of the Third Schedule of the Banking Regulation Act, 1949."),
    ("Advances", "Loans, cash credit, overdrafts, and bills purchased/discounted &mdash; the main income-generating asset of a bank."),
]
examprep = [
    "Balance Sheet: Form 'A', Third Schedule, Sec. 29 Banking Regulation Act 1949; Assets = Liabilities + Net Worth.",
    "Liabilities: Capital, Reserves &amp; Surplus, Deposits (Demand/Term), Other Liabilities &amp; Provisions.",
    "Assets: Cash &amp; Balances with RBI, Balances with Banks/Money at Call, Investments, Advances, Fixed Assets, Other Assets.",
    "P&amp;L: Form 'B', Third Schedule; Income (Interest Earned + Other Income) minus Expenditure (Interest Expended + Operating Expenses + Provisions) = Profit/Loss, then Appropriations.",
]
questions = [
    ("What are the main components of a bank's Balance Sheet liabilities?", "Capital (issued/subscribed/paid-up), Reserves and Surplus, Deposits (Demand and Term deposits), and Other Liabilities and Provisions."),
    ("Explain the components of a bank's assets.", "Cash and Balances with RBI, Balances with Banks and Money at Call, Investments, Advances (loans, cash credit, overdrafts, bills purchased/discounted), Fixed Assets, and Other Assets."),
    ("Describe the format of a bank's Profit and Loss Account.", "Prepared in Form 'B' of the Third Schedule, it shows Income (Interest Earned + Other Income), Expenditure (Interest Expended + Operating Expenses + Provisions and Contingencies), the resulting Profit or Loss, and finally the Appropriations of that profit."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6 =================
fname, title, prev_link, next_link = T(6)
overview = ("CAMELS is the international rating framework used by regulators to assess the overall soundness "
            "of a bank across six dimensions. This closing topic covers each component and the key ratios used "
            "to measure it.")
notes = """
<h3>6.1 Introduction to CAMELS</h3>
<p>In order to strengthen the banking sector and make it sound and efficient, and to link it to the real economic reforms introduced in 1991, a natural framework of such policy, investment, and growth has undergone phase-of-restructuring reforms &mdash; the banking sector has been introduced with the CAMELS framework. This framework is applied in India as it is also referred to as "Capital adequacy, Asset quality, Management, Earnings, Liquidity, and Sensitivity to market risk" (CAMELS).</p>

<h3>6.2 CAMELS Rating System</h3>
<p>CAMELS is a rating system used by supervisory authorities to rate banks based on six factors, represented by the acronym. Each component is rated on a scale of 1 to 5, and a composite rating is then assigned:</p>
<table class="compare">
<tr><th>Rating</th><th>Range</th><th>Interpretation</th></tr>
<tr><td>1</td><td>1.0 &ndash; 1.4</td><td>Strong &mdash; sound in almost all aspects.</td></tr>
<tr><td>2</td><td>1.5 &ndash; 2.4</td><td>Satisfactory &mdash; fundamentally sound with modest weaknesses.</td></tr>
<tr><td>3</td><td>2.5 &ndash; 3.4</td><td>Fair &mdash; combination of weaknesses if not addressed could worsen.</td></tr>
<tr><td>4</td><td>3.5 &ndash; 4.4</td><td>Marginal &mdash; immoderate to severe weaknesses, unsatisfactory practices.</td></tr>
<tr><td>5</td><td>4.5 &ndash; 5.0</td><td>Unsatisfactory &mdash; critically deficient performance, high near-term failure probability.</td></tr>
</table>
<p>On the other hand, the extreme degree of financial concern requires ratings of 3, 4, or 5 to require a moderate to intense degree of supervisory concern. The interpretation of the composite rating of a financial institution can be summarised as under, so the lower the rating, the lower the degree of supervisory concern, and vice versa.</p>

<h3>6.3 Components of CAMELS</h3>
<ol>
<li><strong>Capital Adequacy (C):</strong> The letter "C" in CAMELS stands for "Capital Adequacy". This examiner measures the capital adequacy of a bank with respect to: the volume of risky assets, the growth experience, plans and prospects of the bank, and the volume of marginal and inferior quality of assets.</li>
<li><strong>Asset Quality (A):</strong> The letter "A" stands for "Asset Quality". This component evaluates the quality of a bank's assets, examining factors like: the level and severity of classified assets, the level and composition of Non-Performing Loans (NPL) as a percentage of total loans, the adequacy of provisions, and the ability of management to administer and collect problem loans.</li>
<li><strong>Management (M):</strong> "M" stands for "Management Capability". This component evaluates the management's ability to identify, measure, and control risks in a safe and sound manner. Factors examined include: technical competence, leadership and administrative ability, compliance with banking regulations and internal controls, adequacy of policies and plans made by the board, and succession planning.</li>
<li><strong>Earnings (E):</strong> The letter "E" stands for "Earnings". This component evaluates a bank's earnings, including growth, stability, composition of net income, and how earnings compare with peers, since earnings represent the first line of defence against risk exposure.</li>
<li><strong>Liquidity (L):</strong> The letter "L" stands for "Liquidity". This component evaluates the adequacy of a bank's liquidity sources compared to its needs, and the availability of assets readily convertible to cash without undue loss.</li>
<li><strong>Sensitivity to Market Risk (S):</strong> The letter "S" stands for "Sensitivity". This component evaluates the degree to which changes in interest rates, exchange rates, commodity prices, or equity prices can adversely affect a bank's earnings and capital.</li>
</ol>

<h3>6.4 Key Ratios Involved in CAMELS Rating</h3>
<table class="compare">
<tr><th>Component</th><th>Key Ratios</th></tr>
<tr><td>Capital Adequacy</td><td>Capital Adequacy Ratio (CAR) &mdash; capital as a percentage of risk-weighted assets, as per RBI/Basel norms.</td></tr>
<tr><td>Asset Quality</td><td>Gross NPA to Total Advances; Net NPA to Net Advances; percentage change in NPAs year-on-year.</td></tr>
<tr><td>Management</td><td>Total Advances to Total Deposits; Business (Deposits + Advances) per Employee; Profit per Employee.</td></tr>
<tr><td>Earnings</td><td>Operating Profit to Average Working Funds; Net Profit to Average Assets (Return on Assets, ROA); Interest Income to Total Income; Spread Ratio (Interest Earned &minus; Interest Expended) / Working Funds.</td></tr>
<tr><td>Liquidity</td><td>Liquid Assets to Total Assets; Liquid Assets to Demand Deposits (LADD); Liquid Assets to Total Deposits (LATD); Approved Securities to Total Assets; Government Securities to Total Assets.</td></tr>
<tr><td>Sensitivity to Market Risk</td><td>Ratios examining exposure to interest rate risk, foreign exchange risk, and derivatives (swaps, options) held by the bank.</td></tr>
</table>
"""
terms = [
    ("CAMELS", "A six-component bank rating framework: Capital Adequacy, Asset Quality, Management, Earnings, Liquidity, and Sensitivity to market risk."),
    ("Capital Adequacy Ratio (CAR)", "The ratio of a bank's capital to its risk-weighted assets, as prescribed by RBI/Basel norms."),
    ("Return on Assets (ROA)", "Net profit as a percentage of average total assets, a key Earnings-component ratio in CAMELS."),
    ("Sensitivity to Market Risk", "The 'S' in CAMELS &mdash; how much changes in interest rates, exchange rates, or asset prices can affect a bank's earnings and capital."),
]
examprep = [
    "CAMELS = Capital Adequacy, Asset Quality, Management, Earnings, Liquidity, Sensitivity to Market Risk &mdash; each rated 1 (strong) to 5 (unsatisfactory).",
    "Composite rating interpretation: 1 = Strong, 2 = Satisfactory, 3 = Fair, 4 = Marginal, 5 = Unsatisfactory (higher number = more supervisory concern).",
    "Key ratios: CAR (Capital Adequacy), Gross/Net NPA ratios (Asset Quality), Business/Profit per Employee (Management), ROA/Spread Ratio (Earnings), LADD/LATD (Liquidity).",
]
questions = [
    ("What does the acronym CAMELS stand for? Explain briefly.", "Capital Adequacy, Asset Quality, Management, Earnings, Liquidity, and Sensitivity to market risk &mdash; six components used by regulators to rate a bank's overall soundness, each scored 1 (strong) to 5 (unsatisfactory)."),
    ("Explain the components of CAMEL's model used to analyse bank performance.", "Capital Adequacy assesses capital relative to risky assets; Asset Quality assesses NPL levels and provisioning adequacy; Management assesses leadership, compliance, and planning ability; Earnings assesses profitability and its stability; Liquidity assesses the bank's ability to meet its obligations; Sensitivity to Market Risk assesses exposure to interest rate, forex, and price movements."),
    ("State the key ratios used in CAMELS rating for Asset Quality and Earnings.", "Asset Quality: Gross NPA to Total Advances, Net NPA to Net Advances. Earnings: Return on Assets (Net Profit to Average Assets), Operating Profit to Average Working Funds, and the Spread Ratio."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Six topics covering the foundations of Indian banking: overview and structure, commercial bank functions, co-operative banks/NABARD/payment systems, RBI and key regulations, financial statements of banks, and the CAMELS rating system.")

print("Unit 1 (Banking & Financial Services) complete: all 6 topics + index written.")
