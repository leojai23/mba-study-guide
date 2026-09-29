# -*- coding: utf-8 -*-
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Banking-and-Financial-Services\units"
BOOK_HTML = "Book: <em>Banking and Financial Services</em> (BA4003, Anna University MBA Sem III) &mdash; Thakur Publication"
BOOK_PLAIN = "Banking and Financial Services (BA4003), Thakur Publication"
NAVY_THEME = dict(accent="#1e3a5f", accent_dark="#15293f", accent_light="#e8eef5",
                   border="#d6dfe8", shadow="rgba(30,58,95,.14)")

TOPICS = [
    ("topic1-capital-adequacy-and-deposits.html", "Capital Adequacy &amp; Deposits"),
    ("topic2-loan-management.html", "Loan Management"),
    ("topic3-investment-management.html", "Investment Management"),
    ("topic4-asset-liability-management.html", "Asset-Liability Management (ALM)"),
    ("topic5-financial-distress.html", "Financial Distress &amp; Prediction Models"),
    ("topic6-risk-management-interest-rate-risk.html", "Risk Management &amp; Interest Rate Risk"),
    ("topic7-forex-and-credit-risk.html", "Forex Risk &amp; Credit Risk"),
    ("topic8-market-operational-solvency-risk.html", "Market, Operational &amp; Solvency Risk"),
    ("topic9-non-performing-assets.html", "Non-Performing Assets (NPAs)"),
    ("topic10-mergers-and-acquisitions.html", "Mergers &amp; Acquisitions of Banks"),
]

U = common.UnitBuilder(2, "Managing Bank Funds/Products &amp; Risk Management", TOPICS,
                        subject="Banking and Financial Services", subject_root=SUBJECT_ROOT,
                        book_html=BOOK_HTML, book_plain=BOOK_PLAIN, theme=NAVY_THEME)

def T(i):
    fname, title = TOPICS[i-1]
    prev_link = (TOPICS[i-2][0], TOPICS[i-2][1]) if i > 1 else None
    next_link = (TOPICS[i][0], TOPICS[i][1]) if i < len(TOPICS) else None
    return fname, title, prev_link, next_link

# ================= Topic 1: Capital Adequacy & Deposits =================
fname, title, prev_link, next_link = T(1)
overview = ("This topic opens Unit 2 with the two foundations of a bank's fund management: how much capital "
            "it must hold to stay safe (Capital Adequacy), and how it raises money from the public in the "
            "first place (Deposits and their pricing).")
notes = """
<h3>1.1 Capital Adequacy</h3>
<p>Capital adequacy is a prerequisite for banks to improve the quality and stable resonance of a bank's portfolio. Adequate capital allows banks to absorb any losses arising from risks in the overall management of funds in its business.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">1.1.1 Identification of Capital Requirements for Maintenance and New Projects</h4>
<ul>
<li>Depreciation and new project requirements are estimated for a regular basis (budgeting cycle) for a larger capital spending plan.</li>
<li>Larger organisations and new projects for developing a plan for retrieval of assets and funding this into the information industry as changing situations demand.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">1.1.2 Capital Adequacy Norms</h4>
<p>The traditional approach to sufficiency of capital assets does not capture the risk elements in various types of assets on the balance sheet as well as in the off-balance sheet business. The Basel Committee for Bank Supervision (BCBS) has prescribed a set of norms for the capital adequacy requirement for the banks in 1988, known as Basel I; these have since been revised through Basel II and Basel III.</p>
<p><strong>Capital Adequacy Ratio (CAR):</strong></p>
<p style="text-align:center;font-weight:600;color:var(--accent-dark)">CAR = (Tier I Capital + Tier II Capital) &divide; Risk-Weighted Assets</p>
<ul>
<li><strong>Tier I Capital:</strong> The core capital of a bank &mdash; equity capital and disclosed reserves &mdash; considered the least insolvency risk.</li>
<li><strong>Tier II Capital:</strong> Undisclosed reserves, revaluation reserves, general provisions, hybrid instruments, and subordinated term debt &mdash; supplementary capital, riskier than Tier I.</li>
</ul>
<p>The Basel III norms mandate a minimum CAR of 8%, and for Indian scheduled commercial banks the RBI mandates it be maintained at 9% (and 12% for public sector banks, as per RBI direction).</p>

<h3>1.2 Deposits</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">1.2.1 Meaning of Deposits</h4>
<p>One of the important functions of deposits for the bank is to accept deposits from the public for the purpose of lending or investment. Opening an account is the most common form of the bank's service to the customer, and deposits are the main source of funds for a bank.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">1.2.2 Features of Deposits</h4>
<ul>
<li>Bank deposits are used for a variety of purposes.</li>
<li>There is a ceiling on the interest rate on savings deposits set by the RBI (though largely deregulated on term deposits since liberalisation).</li>
<li>Deposits in a savings/current account are payable on demand, or after a fixed term (fixed/recurring deposits).</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">1.2.3 Types of Deposit Accounts</h4>
<table class="compare">
<tr><th>Type</th><th>Key Features</th></tr>
<tr><td><strong>Fixed Deposit</strong></td><td>Deposited for a fixed period ranging from a few months to years; early withdrawal attracts a penalty; highest interest rate among deposit types; a Fixed Deposit Certificate is issued.</td></tr>
<tr><td><strong>Savings Deposit</strong></td><td>Promotes savings habits; some restrictions on number/amount of withdrawals; moderate interest rate; minimum balance often required.</td></tr>
<tr><td><strong>Current Deposit</strong></td><td>Meant for businessmen; unlimited withdrawals allowed; usually no interest paid; the bank charges for services rendered instead.</td></tr>
<tr><td><strong>Recurring Deposit</strong></td><td>A fixed sum deposited every month for a fixed period; depositor receives a lump sum (principal + interest) at maturity; interest rate higher than savings but lower than fixed deposits.</td></tr>
</table>
<p>There is also a special category for <strong>Non-Resident Indians (NRIs)</strong>, allowing them to open accounts to channel funds for investment needs, quick transfers, and safety, in local or foreign currency, with the flexibility to repatriate funds abroad.</p>

<h3>1.3 Non-Deposit Sources of Funds</h3>
<p>Larger banking institutions also rely on non-deposit sources of short-term money to meet loan demand and unexpected cash emergencies, especially when it is a mismatch between deposit inflows and lending outflows (the "funding gap").</p>
<ul>
<li><strong>Borrowing from the Central Bank:</strong> Banks can borrow short-term cash from the central bank (RBI) at the Bank Rate, typically as a last resort, against collateral.</li>
<li><strong>Certificate of Deposits (CDs):</strong> Negotiable, unsecured money market instruments issued at a discount to face value, with a short-to-medium term to maturity.</li>
<li><strong>Commercial Papers (CPs):</strong> Short-term, unsecured promissory notes issued by highly-rated corporates and financial institutions to raise working capital.</li>
<li><strong>Other Money Market Borrowings:</strong> From other banks, institutions, brokers, dealers, and business houses.</li>
</ul>

<h3>1.4 Pricing of Deposit Sources of Services</h3>
<table class="compare">
<tr><th>Pricing Method</th><th>Approach</th></tr>
<tr><td><strong>Cost-Plus Margin Deposit Pricing</strong></td><td>Sets the price of a product by determining the sum of the cost of producing/offering the product plus a target profit margin.</td></tr>
<tr><td><strong>Marginal Cost Approach</strong></td><td>Prices deposits based on the marginal (incremental) cost of raising each additional rupee of deposits.</td></tr>
<tr><td><strong>Market Penetration Deposit Pricing</strong></td><td>Sets a lower price initially to attract new customers and build market share, aiming to encourage the desired penetration.</td></tr>
<tr><td><strong>Relationship Pricing</strong></td><td>Prices deposits based on the value of the overall "total customer relationship" a client has with the bank, rather than a single product/account in isolation.</td></tr>
<tr><td><strong>Upscale Target Pricing</strong></td><td>Prices a standardised product targeted at high-value customers who rely on professional, high-service banking, at a premium.</td></tr>
</table>
"""
terms = [
    ("Capital Adequacy Ratio (CAR)", "The ratio of a bank's Tier I + Tier II capital to its risk-weighted assets, mandated at a minimum by the Basel Committee/RBI."),
    ("Tier I Capital", "Core capital &mdash; equity capital and disclosed reserves &mdash; carrying the least insolvency risk."),
    ("Tier II Capital", "Supplementary capital &mdash; undisclosed reserves, revaluation reserves, hybrid instruments, subordinated debt."),
    ("Certificate of Deposit (CD)", "A negotiable, unsecured money market instrument issued at a discount by banks to raise short-term funds."),
    ("Commercial Paper (CP)", "A short-term, unsecured promissory note issued by highly-rated corporates to raise working capital."),
]
examprep = [
    "CAR = (Tier I + Tier II Capital) / Risk-Weighted Assets; Basel III minimum 8%, RBI mandates 9% for Indian scheduled banks.",
    "Deposit types: Fixed (highest interest, penalty on early withdrawal), Savings (restricted withdrawals), Current (unlimited withdrawals, no interest), Recurring (monthly instalments to a lump sum).",
    "Non-deposit sources: borrowing from RBI, Certificates of Deposit, Commercial Papers, other money market borrowings.",
    "Deposit pricing methods: Cost-Plus Margin, Marginal Cost, Market Penetration, Relationship Pricing, Upscale Target Pricing.",
]
questions = [
    ("What is the Capital Adequacy Ratio? How is it calculated?", "CAR measures a bank's capital relative to its risk-weighted assets: CAR = (Tier I Capital + Tier II Capital) / Risk-Weighted Assets. Basel III sets a minimum of 8%, while the RBI mandates Indian scheduled commercial banks maintain at least 9%."),
    ("Explain the different types of deposit accounts offered by banks.", "Fixed Deposits (fixed period, highest interest, penalty on early withdrawal), Savings Deposits (restricted withdrawals, moderate interest), Current Deposits (unlimited withdrawals, no interest, for businesses), and Recurring Deposits (fixed monthly instalments maturing into a lump sum)."),
    ("What are the non-deposit sources of bank funds?", "Borrowing from the Central Bank (RBI), Certificates of Deposit (CDs), Commercial Papers (CPs), and other money market borrowings from banks, institutions, and dealers."),
    ("Explain any three methods of pricing deposit products.", "Cost-Plus Margin Pricing (cost of the product plus target margin), Marginal Cost Approach (based on the incremental cost of raising more deposits), and Relationship Pricing (based on the value of a customer's total relationship with the bank rather than a single account)."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2: Loan Management =================
fname, title, prev_link, next_link = T(2)
overview = ("Loans are a bank's primary income-generating asset. This topic covers how banks classify loans, "
            "structure their lending policy, price loans, and manage lending through changing conditions like "
            "the COVID-19 pandemic.")
notes = """
<h3>2.1 Introduction to Loan Management</h3>
<p>A loan is an amount of money, property, or other tangible goods given by a lender to a borrower in exchange for future repayment of the loan value, along with interest or finance charges. A loan may be provided for a specific one-time amount, or as an open-ended line of credit up to a set maximum ("open-ended loan", e.g. a credit card).</p>

<h3>2.2 Types of Loans and their Features</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Secured Loan</strong></td><td>Backed by collateral (property, car, or asset pledged); the asset can be seized if the loan is defaulted upon; typically lower interest rates due to lower risk for the lender.</td></tr>
<tr><td><strong>Unsecured Loan</strong></td><td>Not backed by any collateral (e.g. personal loans, credit card debt); the lender charges a higher interest rate to compensate for the higher risk of default.</td></tr>
</table>
<p>Other classifications include: Demand Loans (repayable on demand), Term Loans (fixed repayment schedule).</p>

<h3>2.3 Major Components of a Loan Policy Document</h3>
<ol>
<li><strong>Establish a Lending Authority:</strong> It should clearly define who is authorised to make lending decisions and to what limit.</li>
<li><strong>Statement of Lending Policy:</strong> The bank's policy on the types of loans and the overall portfolio of the bank's lending should be clearly defined.</li>
<li><strong>Establish Lines of Responsibility:</strong> It should clearly define the responsibilities for reviewing, evaluating, and making decisions on loan applications.</li>
<li><strong>Required Documentation:</strong> All documents required for every loan application must be clearly specified.</li>
<li><strong>Lines of Authority and Amount:</strong> Lines of authority for approving loans and amounts should be well defined.</li>
<li><strong>Guidelines for Establishing Interest Rates and Fees:</strong> Policies and procedures for establishing credit fees, interest rates, etc. must be established.</li>
</ol>

<h3>2.4 Types of Lending</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">2.4.1 Fund-Based Lending</h4>
<p>This is the traditional and most popular form of bank lending, which involves an outflow of funds from the bank to the borrower.</p>
<ul>
<li><strong>Cash Credit:</strong> A running account facility with a sanctioned limit against which the borrower draws funds as needed, interest charged only on the amount drawn.</li>
<li><strong>Overdraft:</strong> Withdrawal beyond the credit balance in a current account, up to an agreed limit.</li>
<li><strong>Bills Purchase and Discounted:</strong> The bank purchases/discounts a bill of exchange, crediting the holder with the discounted value before maturity.</li>
<li><strong>Term Loans:</strong> Loans with a fixed repayment period for financing capital assets or working capital, secured or unsecured.</li>
</ul>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">2.4.2 Non-Fund Based Lending</h4>
<p>The bank does not actually lend out its own funds, but makes a commitment on behalf of the customer, which remains contingent unless invoked.</p>
<ul>
<li><strong>Letter of Credit:</strong> An instrument issued by a bank guaranteeing payment to a seller on a buyer's behalf, up to a stated amount, provided conditions are met; commonly used in international trade.</li>
<li><strong>Bank Guarantee:</strong> A guarantee issued by a bank on behalf of a customer promising to cover a loss if the customer fails to fulfil a contractual obligation.</li>
<li><strong>Project Finance:</strong> Financing of long-term projects (e.g. highways, infrastructure) based on the projected cash flows of the project, often through a Special Purpose Vehicle (SPV).</li>
<li><strong>Asset-Based Lending:</strong> Loans secured against a company's assets (inventory, accounts receivable, equipment, or property).</li>
</ul>

<h3>2.5 Loan Management in Indian Banks &mdash; Pre and Post COVID-19</h3>
<p>Before COVID-19, borrowing patterns had already started shifting towards digital and app-based borrowing, rather than the traditional medical/education/home-related purposes. During the pandemic, moratoriums and relaxations provided by the government and RBI provided some breather, though non-performing assets driven by the pandemic rose sharply as borrowers struggled to repay.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Issues and Trends in Loan Management</h4>
<ul>
<li><strong>Machine Learning &amp; Digital Underwriting:</strong> Banks are increasingly using Machine Learning and digital credit-assessment models (Customer KYC, video KYC) leveraging Aadhaar-enabled and other digital data to make faster lending decisions.</li>
<li><strong>Government Schemes:</strong> Schemes like the RBI's push towards a 59-minute loan approval process for MSMEs improve turnaround time for credit.</li>
<li><strong>Small Ticket, Digital-First Loans:</strong> A shift toward small-ticket, digital-first, need-based borrowing (for medical, essential, or education needs) rather than large indulgence-based personal loans.</li>
<li><strong>Rise of Bad Loans (NPAs):</strong> Banks and their lending systems will continue to see increased risk of NPAs unless underwriting practices are improved to accurately assess a borrower's credit quality and repayment capacity.</li>
</ul>

<h3>2.6 Pricing of Loans</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">2.6.1 Fixed and Floating Rate Loans</h4>
<p>Fixed Rate Loans carry an interest rate fixed for the entire term. Floating Rate Loans have an interest rate that varies with the market (e.g. linked to the bank's benchmark rate), which became popular post-COVID-19 as it is easier for banks to price risk into these rates and keep pace with market and economic changes.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">2.6.2 Loan Pricing Methods</h4>
<table class="compare">
<tr><th>Method</th><th>Approach</th></tr>
<tr><td><strong>Cost-Plus Loan Pricing</strong></td><td>Loan Rate = Cost of Funds + Operating Costs + Risk Premium + Profit Margin.</td></tr>
<tr><td><strong>Cost-Benefit Approach</strong></td><td>Marginal Cost Pricing: New Interest Rate = Marginal Cost of Funds &times; % of Loan Funded by Borrowed Funds, plus other components.</td></tr>
<tr><td><strong>Historical Average Cost Approach</strong></td><td>Prices a loan based on the bank's historical average cost of funds, rather than the current marginal cost.</td></tr>
<tr><td><strong>Customer Profitability Analysis (CPA)</strong></td><td>Looks at all revenue and costs from a particular customer relationship (across all products/services) rather than just a single loan, to determine the overall rate.</td></tr>
<tr><td><strong>Risk-Based Pricing</strong></td><td>Under this scheme, a bank charges a higher (or lower) interest rate based on a borrower's credit risk profile &mdash; riskier borrowers pay more.</td></tr>
</table>
"""
terms = [
    ("Secured Loan", "A loan backed by collateral, which the lender may seize if the borrower defaults."),
    ("Unsecured Loan", "A loan not backed by collateral, carrying a higher interest rate to compensate the lender's higher risk."),
    ("Fund-Based Lending", "Lending that involves an actual outflow of bank funds, e.g. cash credit, overdraft, term loans."),
    ("Non-Fund Based Lending", "Lending where the bank makes a contingent commitment (e.g. Letter of Credit, Bank Guarantee) without an immediate outflow of funds."),
    ("Risk-Based Pricing", "Charging loan interest rates according to a borrower's credit risk profile &mdash; riskier borrowers pay higher rates."),
]
examprep = [
    "Secured Loans (collateral-backed, lower rate) vs Unsecured Loans (no collateral, higher rate).",
    "Fund-Based Lending (Cash Credit, Overdraft, Bills Purchase/Discount, Term Loans) vs Non-Fund Based Lending (Letter of Credit, Bank Guarantee, Project Finance, Asset-Based Lending).",
    "Loan policy document components: lending authority, policy statement, lines of responsibility, documentation, approval limits, interest/fee guidelines.",
    "Loan pricing methods: Cost-Plus, Cost-Benefit/Marginal Cost, Historical Average Cost, Customer Profitability Analysis, Risk-Based Pricing.",
    "Post-COVID trend: shift to digital-first, small-ticket, need-based lending using ML-based underwriting and faster KYC.",
]
questions = [
    ("Distinguish between fund-based and non-fund based lending.", "Fund-based lending involves an actual outflow of bank funds to the borrower (Cash Credit, Overdraft, Bills Discounting, Term Loans). Non-fund based lending involves the bank making a contingent commitment on the customer's behalf without an immediate outflow of funds (Letter of Credit, Bank Guarantee), which only becomes a fund outflow if invoked."),
    ("What are the major components of a bank's loan policy document?", "Establishing a lending authority, a statement of lending policy, lines of responsibility for loan decisions, required documentation, lines of authority and approval limits, and guidelines for establishing interest rates and fees."),
    ("Explain the different methods of loan pricing.", "Cost-Plus Pricing (cost of funds + operating costs + risk premium + margin), Cost-Benefit/Marginal Cost Pricing, Historical Average Cost Approach, Customer Profitability Analysis (based on the whole customer relationship), and Risk-Based Pricing (rate varies with the borrower's credit risk)."),
    ("Discuss the recent trends and issues in loan management in Indian banks.", "A shift toward digital-first, small-ticket, need-based lending; increased use of Machine Learning and digital KYC for faster underwriting; government schemes like the 59-minute MSME loan approval process; and a continuing risk of rising NPAs unless underwriting quality improves."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3: Investment Management =================
fname, title, prev_link, next_link = T(3)
overview = ("Beyond lending, banks invest a portion of their funds in securities. This topic covers why banks "
            "invest, what they invest in, and the balance between safety, liquidity, and profitability that "
            "governs every investment decision.")
notes = """
<h3>3.1 Meaning of Bank Investment</h3>
<p>Bank investment management is the process of managing investors' money on behalf of banking products and services. An investment means the purchase of goods that are not consumed today but are used in the future to create wealth. In general, an investment is any mechanism used for generating future income, in the form of interest, dividends, or appreciation of the value of the instrument.</p>

<h3>3.2 Nature of Bank Investment</h3>
<p>Every investor invests in a bank with some appetite for risk and expects some degree of benefits for that risk. Depending on the life stage and risk appetite of the investor, every investment has its own unique set of benefits and risks. The important objectives of investment in banks are:</p>
<ol>
<li><strong>Safety:</strong> While no investment option is completely safe, some are safer than others. Investors should choose safe, less risky products, though a low degree of risk often means lower returns as well.</li>
<li><strong>Liquidity:</strong> Some investment products can be sold and converted to cash easily during emergencies, while others cannot; investors need to balance the two.</li>
<li><strong>Income (Returns):</strong> Many investors invest in options for a source of preferred regular income, though this often trades off against safety/liquidity.</li>
<li><strong>Growth:</strong> Some investors prioritise capital appreciation over time (growth), even accepting non-fixed, variable returns, by investing more heavily in equities or equity-linked instruments.</li>
</ol>

<h3>3.3 Functions of Bank Investments</h3>
<ol>
<li><strong>Income Function:</strong> One important objective of generating income &mdash; interest, dividends, and capital gains, is the primary function of bank investment.</li>
<li><strong>Liquidity Function:</strong> Many investment instruments include gilt-edged securities (government securities) and other liquid, easily-tradeable instruments that can be used during periods when the bank needs cash quickly.</li>
<li><strong>Other Objectives:</strong> Reducing overall tax liability through certain tax-exempt instruments, and diversification of the bank's assets and risks.</li>
</ol>

<h3>3.4 Forms of Bank Investment</h3>
<p>Banks are required to invest a portion of their deposits under Statutory Liquidity Ratio (SLR) requirements. This gives rise to two broad categories:</p>
<table class="compare">
<tr><th>SLR Investments</th><th>Non-SLR Investments</th></tr>
<tr>
<td>Investments in Government and other approved securities that count towards a bank's statutory SLR requirement (e.g. Central/State Government securities, Treasury Bills), kept in mind for safety and to meet the regulatory minimum.</td>
<td>Investments in shares, debentures, bonds, mutual funds, commercial paper, and other instruments not eligible for SLR &mdash; carry higher risk-reward and are made based on the bank's own risk appetite, in associate/subsidiary companies, PSU bonds, and Venture Capital Funds/Funds of Funds, among others.</td>
</tr>
</table>
<p>Preferred investment types among these include Government Securities (very safe, at the beginning of the fiscal year, preferred by RBI policy), Corporate Bonds, and other instruments allowed for banks' portfolios subject to prudential norms.</p>
"""
terms = [
    ("Bank Investment", "The process of a bank deploying part of its funds into securities to earn income, maintain liquidity, and diversify risk."),
    ("SLR (Statutory Liquidity Ratio) Investments", "Investments in government and other approved securities that satisfy a bank's statutory SLR requirement."),
    ("Non-SLR Investments", "Investments in shares, debentures, bonds, and other instruments beyond the SLR requirement, taken on for additional returns."),
    ("Safety, Liquidity, Profitability", "The three competing objectives that guide every bank investment decision."),
]
examprep = [
    "Bank investment aims to balance Safety, Liquidity, Income, and Growth.",
    "Functions of bank investment: Income (interest/dividends/capital gains), Liquidity (easily tradeable instruments), and other objectives (tax reduction, diversification).",
    "SLR Investments (government/approved securities, meet statutory requirement) vs Non-SLR Investments (shares, debentures, bonds &mdash; higher risk/reward).",
]
questions = [
    ("What are the important objectives of bank investment?", "Safety (minimising risk of loss), Liquidity (ability to convert to cash quickly), Income (regular returns), and Growth (capital appreciation over time) &mdash; these often trade off against one another."),
    ("Distinguish between SLR and Non-SLR investments.", "SLR Investments are in government and other approved securities that satisfy a bank's Statutory Liquidity Ratio requirement, prioritising safety. Non-SLR Investments are in shares, debentures, bonds, and other instruments beyond the SLR requirement, taken on for higher returns at higher risk."),
    ("Explain the functions of bank investment.", "The Income function generates interest, dividends, and capital gains; the Liquidity function ensures the bank holds easily-tradeable instruments for emergencies; and other functions include reducing tax liability and diversifying the bank's overall risk."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 3 done")

# ================= Topic 4: Asset-Liability Management (ALM) =================
fname, title, prev_link, next_link = T(4)
overview = ("Asset-Liability Management (ALM) is how a bank manages the risk that arises from mismatches "
            "between what it owns (assets) and what it owes (liabilities). This topic covers ALM's meaning, "
            "components, organisational structure, and the process banks follow to manage it.")
notes = """
<h3>4.1 Introduction to ALM</h3>
<p>Management of assets and liabilities (or "Surplus Liability Management") is essentially a risk management technique designed to earn an adequate return while maintaining a comfortable surplus of assets beyond liabilities. It takes into consideration the interest rates, earning power, and degree of willingness to take on risk, considering all the different ways under which ALM has evolved. In the last decade, Asset-Liability Management (ALM) can be termed as a risk management technique designed to manage the mismatch between assets and liabilities on a bank's balance sheet.</p>

<h3>4.2 Need for Asset-Liability Management</h3>
<p>ALM is the practice of managing risks that arise due to mismatches between the assets and liabilities of a bank. Banks face several risks from such mismatches:</p>
<ol>
<li><strong>Liquidity Risk:</strong> Arising from the difference in the volume of assets and liabilities that need to be paid or received within a given period.</li>
<li><strong>Interest Rate Risk:</strong> Arising from the mismatch in the interest-rate sensitivity of assets versus liabilities.</li>
<li><strong>Managing Risk Effectively:</strong> Since banks operate with a mix of assets and liabilities of different maturities, currencies, and interest-rate structures, they need a formal process to manage these mismatches.</li>
</ol>

<h3>4.3 Components of ALM</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">4.3.1 Bank Assets</h4>
<p>Retail Personal Loans, Retail Credit-Card Receivables, Retail Mortgages, and other retail/wholesale advances form the asset side of a bank's ALM.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">4.3.2 Bank Liabilities</h4>
<p>Deposits from commercial customers, deposits from retail customers (checking/savings), bonds issued by the bank, and other borrowed funds form the liability side.</p>

<h3>4.4 ALM Organisation</h3>
<p>The Board has overall responsibility for management of risks and is expected to decide the risk management policy and set limits for liquidity, interest-rate, foreign exchange, and equity price risks.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">4.4.1 Composition of ALCO (Asset-Liability Committee)</h4>
<p>ALCO is a decision-making unit responsible for balance sheet planning from a risk-return perspective, including strategic management of interest-rate and liquidity risks. Each bank should decide on the role of its ALCO, its responsibility, as well as the decisions to be taken by it. The business and risk management strategy of the bank should ensure that the operations remain within the Board's/ALCO's risk tolerance limits.</p>
<p>Typically, the organisational structure includes the Head of Banking, Head of Corporate Banking, Head of Treasury, Head of Credit, Head of Operations, and a Chief Financial Officer, all responsible for ALM.</p>

<h3>4.5 Procedure of Asset-Liability Management</h3>
<p>Step 1: <strong>Preparing Internal Control Questionnaire</strong> &mdash; the board of directors and management should be consistent in their duties and responsibilities.</p>
<p>Step 2: <strong>Determine the efficiency of Asset-Liability Management</strong> &mdash; assess whether a mechanism to co-ordinate asset and liability decisions exists.</p>
<p>Step 3: <strong>Review the bank's future development and expansion plans</strong> &mdash; with a focus on the bank's budget projections for funding needs.</p>
<p>Step 4: <strong>Assess the bank's ability to react to changes</strong> &mdash; whether internal management reports on liquidity and interest-rate exposure are reviewed regularly.</p>
<p>Step 5: <strong>Reviewing the bank's plan of liquidity management</strong> &mdash; assessing sensitivity to interest rate risk and the adequacy of the bank's liquidity funding needs, in terms of its projected funding needs.</p>
<p>Step 6: <strong>Preparing an annual audit report</strong> that should include a review of the board and management's liquidity management policies.</p>

<h3>4.6 Emerging Issues of ALM in India</h3>
<ul>
<li>With the onset of liberalisation, Indian banks are now more exposed to global competition, which makes ALM systems inadequate and inefficient to manage the increased complexity.</li>
<li>Net Interest Income (NII) and Net Interest Margin (NIM), within a given level of risk tolerance, are being sought by banks to remain competitive.</li>
<li>There is a growing need for interest-rate risk management systems that can be aligned with regulatory (RBI) guidelines while also focusing on the bank's own strategic goals.</li>
</ul>
"""
terms = [
    ("Asset-Liability Management (ALM)", "A risk-management technique designed to manage mismatches between a bank's assets and liabilities, earning adequate returns while maintaining a comfortable liquidity surplus."),
    ("ALCO (Asset-Liability Committee)", "The decision-making unit responsible for balance sheet planning from a risk-return perspective, managing interest-rate and liquidity risk."),
    ("Net Interest Margin (NIM)", "The difference between interest income generated and interest paid out, relative to interest-earning assets."),
    ("Liquidity Risk (in ALM context)", "The risk arising from a mismatch in the volume/timing of assets and liabilities due for payment or receipt."),
]
examprep = [
    "ALM = risk-management technique to manage asset-liability mismatches, balancing return against liquidity/interest-rate risk.",
    "Key risks addressed by ALM: Liquidity Risk and Interest Rate Risk from asset-liability mismatches.",
    "ALM Components: Bank Assets (loans, credit-card receivables, mortgages) vs Bank Liabilities (deposits, bonds issued, borrowings).",
    "ALCO is the decision-making body for ALM; Board sets overall risk policy and limits.",
    "ALM procedure: prepare internal control questionnaire &rarr; assess ALM efficiency &rarr; review expansion plans &rarr; assess responsiveness to change &rarr; review liquidity plan &rarr; prepare annual audit report.",
]
questions = [
    ("What is Asset-Liability Management? Why is it needed?", "ALM is a risk-management technique that manages mismatches between a bank's assets and liabilities, to earn adequate returns while maintaining sufficient liquidity. It is needed because banks face Liquidity Risk and Interest Rate Risk whenever the maturity, currency, or rate-sensitivity of their assets doesn't match their liabilities."),
    ("Explain the role and composition of ALCO.", "ALCO (Asset-Liability Committee) is the decision-making unit responsible for balance sheet planning from a risk-return perspective, managing interest-rate and liquidity risk strategically. It typically includes the Heads of Banking, Corporate Banking, Treasury, Credit, Operations, and the CFO, operating within risk limits set by the Board."),
    ("Describe the procedure followed in Asset-Liability Management.", "Preparing an internal control questionnaire, determining the efficiency of existing ALM co-ordination, reviewing the bank's expansion plans, assessing the bank's ability to react to change, reviewing the liquidity management plan, and preparing an annual audit report."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5: Financial Distress =================
fname, title, prev_link, next_link = T(5)
overview = ("When a bank's financial condition deteriorates, early warning matters. This topic covers what "
            "financial distress is, statistical models used to predict it, and the strategies used to "
            "rehabilitate a distressed institution.")
notes = """
<h3>5.1 Concept of Financial Distress</h3>
<p>The term "financial distress" refers to a situation where a bank fails to honour, or has difficulty honouring, its financial obligations to its creditors, due to a decline in earnings and/or asset values. As an increasing proportion of investments is considered risky or "toxic" assets, financial distress results in a situation of facing bankruptcy.</p>

<h3>5.2 Causes of Financial Distress in Banks</h3>
<ul>
<li><strong>High amounts of debt</strong> relative to the bank's asset base and equity.</li>
<li><strong>Fixed/high operating costs</strong> that don't fall even when revenue does.</li>
<li><strong>An asset-liability mismatch</strong> &mdash; illiquid assets funded by short-term liabilities.</li>
<li><strong>Poor management decisions</strong> regarding risk-taking, lending quality, and investments.</li>
<li><strong>Economic downturns</strong> that increase defaults across the loan portfolio.</li>
</ul>
<p>Some indicators of the likelihood of financial distress in banks: high debt, low or declining revenue, poor cash flow, rising NPAs, and declining credit ratings.</p>

<h3>5.3 Prediction Models of Financial Distress</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">5.3.1 Z-Score Model</h4>
<p>The Z-score model, introduced by <strong>Edward Altman</strong>, is a clear, well-tested model for predicting financial distress that shows a firm's financial health using distinct accounting and market-value ratios, combined into a single score. A low Z-score value indicates a firm is at risk of bankruptcy; a high value indicates financial health.</p>
<p><strong>Agrawal and Taffler</strong> studied Z-score model performance over 25 years and found it retains a fairly consistent ability to give clear, early prediction of a company's distress, agreeing that the accounting-ratio-based Z-score model is superior to certain alternative approaches, though other approaches also add value.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">5.3.2 Hazard Model</h4>
<p>The Hazard model, developed by researchers including <strong>Shumway</strong>, treats bankruptcy prediction as a hazard/survival-analysis problem &mdash; combining both accounting and market-based variables over the life of the firm, rather than a single cut-off point in time (as the Z-score does). <strong>Chava and Jarrow</strong> further developed hazard models, adding industry effects, and found that a firm's data over multiple years, not just a single snapshot, improves prediction accuracy.</p>

<h3>5.4 Methods/Strategies for Rehabilitation of Financial Distress</h3>
<table class="compare">
<tr><th>Strategy</th><th>Approach</th></tr>
<tr><td><strong>Turnaround Strategies</strong></td><td>Restructuring (Operations, Asset, Financial): cutting costs, improving working capital management, and re-focusing the business to return the distressed firm to profitability.</td></tr>
<tr><td><strong>Private Workout</strong></td><td>A voluntary agreement between the distressed firm/venture and its creditors to restructure the existing terms of debt (interest, maturity, principal), without going to court.</td></tr>
<tr><td><strong>Financial Restructuring</strong></td><td>Changing the composition of the venture's existing debt claims against the firm, or reorganising the contractual terms of existing debt.</td></tr>
<tr><td><strong>File for Legal Bankruptcy (Liquidation)</strong></td><td>If a private/voluntary resolution is not feasible, a bankruptcy court determines that the firm must be liquidated. A liquidation proceeds via a public auction or private sale, and the proceeds are distributed to creditors per the priority of their claims.</td></tr>
<tr><td><strong>Reorganisation (Legal Bankruptcy):</strong></td><td>Instead of liquidation, the bankruptcy court may approve a reorganisation plan that restructures the firm's debt/equity claims while it continues to operate.</td></tr>
</table>

<h3>5.5 Signals to Borrowers &amp; Rehabilitation Process</h3>
<p>Signals of sickness that lenders/bankers watch for include: frequent requests for extension of repayment schedules, decreasing amount of business handled, and irregular servicing of interest and principal.</p>
<p>The rehabilitation process typically proceeds through stages: (1) the borrower is issued a confirmation of sickness in an industrial unit, (2) the bank/DRS conducts a viability study, (3) formulation of a detailed rehabilitation package/Draft Rehabilitation Scheme (DRS), (4) approval of the DRS by the appropriate authority and lenders, and (5) implementation with continued monitoring until compliance and viability are restored.</p>
"""
terms = [
    ("Financial Distress", "A situation where a firm/bank fails to honour, or struggles to honour, its financial obligations due to declining earnings/asset values."),
    ("Z-Score Model", "Edward Altman's model predicting bankruptcy risk using a weighted combination of financial ratios into a single score."),
    ("Hazard Model", "A bankruptcy-prediction model (Shumway et al.) using survival analysis over a firm's life, combining accounting and market variables."),
    ("Private Workout", "A voluntary, out-of-court agreement between a distressed firm and its creditors to restructure debt terms."),
    ("Turnaround Strategy", "A restructuring approach (operational, asset, or financial) aimed at returning a distressed firm to profitability."),
]
examprep = [
    "Financial distress = difficulty honouring financial obligations due to declining earnings/asset values.",
    "Prediction models: Z-Score (Altman, ratio-based single score) vs Hazard Model (Shumway, survival-analysis over time using accounting + market variables).",
    "Rehabilitation strategies: Turnaround (restructuring), Private Workout (voluntary out-of-court), Financial Restructuring, or Legal Bankruptcy (Liquidation or Reorganisation).",
    "Warning signals: repeated repayment extension requests, declining business volume, irregular interest/principal servicing.",
]
questions = [
    ("Explain the Z-Score model of predicting financial distress.", "Developed by Edward Altman, the Z-score model combines several accounting and market-value financial ratios into a single score to predict bankruptcy risk &mdash; a low score signals distress, a high score signals financial health. Studies by Agrawal and Taffler found it retains reasonably consistent predictive power over decades."),
    ("Distinguish between the Z-Score model and the Hazard model.", "The Z-score model gives a single-point prediction based on a weighted combination of ratios at one point in time. The Hazard model (Shumway) treats bankruptcy as a survival/hazard problem, using both accounting and market-based variables tracked over the firm's life, generally improving prediction accuracy over a single-period Z-score."),
    ("What strategies can a financially distressed bank/firm adopt?", "Turnaround strategies (operational/asset/financial restructuring), a Private Workout (voluntary out-of-court debt restructuring with creditors), Financial Restructuring of existing debt claims, or filing for Legal Bankruptcy, which can result in either Liquidation or a court-approved Reorganisation."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6: Risk Management & Interest Rate Risk =================
fname, title, prev_link, next_link = T(6)
overview = ("This topic introduces risk management in banks generally &mdash; how risk is defined, measured, "
            "and mitigated &mdash; before focusing on the first specific risk type: Interest Rate Risk.")
notes = """
<h3>6.1 Meaning of Risk</h3>
<p>Risk refers to the probability of occurrence of specific unforeseen events. Technically, the concept of risk is different from the concept of value or benefit, though in common parlance the two are often used interchangeably. Risk in banking may result in adverse negative impact on a specific financial event.</p>

<h3>6.2 Types of Risks in Banks</h3>
<table class="compare">
<tr><th>Risk</th><th>Meaning</th></tr>
<tr><td><strong>Credit Risk</strong></td><td>Risk of loss arising when borrowers or counterparties fail to meet their contractual obligations, e.g. defaults on loans, credit cards, and fixed-income securities.</td></tr>
<tr><td><strong>Interest Rate Risk</strong></td><td>Risk to a bank's earnings and capital value arising from adverse movements in interest rates that affect the bank's positions.</td></tr>
<tr><td><strong>Liquidity Risk</strong></td><td>Risk arising when a bank is unable to meet its obligations as they fall due, without incurring unacceptable losses.</td></tr>
<tr><td><strong>Market Risk</strong></td><td>Risk of losses in on- and off-balance sheet positions arising from movements in market prices (interest rates, forex rates, equity/commodity prices).</td></tr>
<tr><td><strong>Operational Risk</strong></td><td>Risk of loss from inadequate or failed internal processes, people, and systems, or from external events.</td></tr>
</table>

<h3>6.3 Risk Management Strategies and Tools</h3>
<ol>
<li><strong>Realistic Operating or Business Plan:</strong> A statement of business goals and objectives should be realistic, with careful monitoring and control functions built in.</li>
<li><strong>System for Assessing the Risks:</strong> To help protect against risks and to ensure long-term viability, each institution must have long-term methods and facilities that reflect the risk characteristics that are unique to its own business.</li>
<li><strong>Securitisation:</strong> Securitisation of loss (or expected loss) is used as an important risk management tool, since it transfers risk to another party for a fee or consideration.</li>
<li><strong>Adequate Loss Reserves:</strong> Setting aside adequate reserves for expected credit losses.</li>
<li><strong>Insurance Transfer:</strong> Transferring risk to a third party (an insurer) by paying an insurance premium.</li>
<li><strong>Contract:</strong> Another method of transferring risk to safeguard the activities which includes risk retention, i.e. it may involve an option to pass the risk of loss to the other party through contractual clauses.</li>
<li><strong>Risk Retention (Retaining Risk):</strong> Since it is not cost-effective or practically possible to eliminate all types of risk, banks internally retain some level of risk within tolerable limits, as it is affected by the volatility of loss.</li>
</ol>

<h3>6.4 Risk Measurement and Management Process</h3>
<ol>
<li><strong>Risk Identification:</strong> Identification of the risk as it arises at the transaction level and at the portfolio level.</li>
<li><strong>Risk Measurement:</strong> Risk measurement relies on quantitative measures like standard deviation, Value at Risk (VaR), sensitivity/volatility, and downside potential.</li>
<li><strong>Risk Pricing:</strong> Banks should price risks in banking transactions so that the capital required to absorb risk is not without adequate reward, at all levels of the organisation.</li>
</ol>

<h3>6.5 Role of RBI in Risk Management in Indian Banking</h3>
<p>The RBI has recommended sound financial systems and risk management guidelines, particularly following the 1991 economic reforms and the adoption of CAMELS-based supervision from 1997 onwards, and has evaluated the tools used to assess the six CAMELS components, of which "Sensitivity to market risk" was added as the sixth component in 1997.</p>

<h3>6.6 Meaning of Interest Rate Risk (IRR)</h3>
<p>Interest Rate Risk (IRR) refers to potential changes in a bank's Net Interest Income (NII) or Market Value of Equity (MVE) arising from changes in market interest rates, especially due to a mismatch between the interest-rate sensitivity of assets and liabilities (repricing dates).</p>

<h3>6.7 Types of Interest Rate Risk</h3>
<ol>
<li><strong>Gap or Mismatch Risk:</strong> Arises from holding assets and liabilities with different maturity/repricing dates, causing a change in interest rates to affect them differently.</li>
<li><strong>Basis Risk:</strong> Market interest rates on different instruments seldom change by the same degree; when interest rates change, the same degree of change in interest rates on assets and liabilities may not be identical, resulting in an adverse change in the spread between lending and borrowing rates.</li>
<li><strong>Embedded Option Risk:</strong> Significant changes in interest rates have an effect on the exercise of options embedded in a bank's assets, liabilities, or off-balance sheet books (e.g. borrowers prepaying loans, or depositors withdrawing deposits before maturity when interest rates change).</li>
<li><strong>Yield Curve Risk:</strong> A floating interest rate that changes with market conditions, in a movement in interest rates can also alter the shape and slope of the yield curve, causing an adverse impact on a bank's income or economic value.</li>
<li><strong>Price Risk:</strong> Price risk occurs when assets are sold before their stated maturity date; bond prices and yields are inversely related, and the price is dependent on the maturity of the instrument.</li>
<li><strong>Reinvestment Risk:</strong> Uncertainty with regard to interest rate at which future cash flows could be reinvested.</li>
</ol>

<h3>6.8 Managing Interest Rate Risk</h3>
<p>Two commonly used perspectives to measure and manage interest rate risk:</p>
<ul>
<li><strong>Earnings Perspective:</strong> Analysing the impact of changes in interest rates on accrual or reported earnings in the near term, typically through Net Interest Income (NII) or Net Interest Margin (NIM) analysis, i.e. Gap Analysis.</li>
<li><strong>Economic Value Perspective:</strong> Analysing the impact of interest-rate changes on the market value of a bank's assets, liabilities, and off-balance sheet positions, reflecting the sensitivity of the net worth of the bank to changes in interest rates.</li>
</ul>
<p>Banks measure this mismatch primarily using the Traditional Gap analysis method, splitting assets and liabilities into different maturity/repricing time buckets and calculating the gap in each, to assess the impact of rate movements on NII.</p>
"""
terms = [
    ("Interest Rate Risk (IRR)", "The risk to a bank's earnings/capital value from adverse movements in market interest rates, due to asset-liability repricing mismatches."),
    ("Gap/Mismatch Risk", "IRR arising because assets and liabilities have different maturities or repricing dates."),
    ("Basis Risk", "The risk that interest rates on different instruments don't move by the same degree, altering the spread between lending and borrowing rates."),
    ("Net Interest Margin (NIM)", "Net interest income expressed as a percentage of interest-earning assets, a key earnings-perspective IRR metric."),
    ("Value at Risk (VaR)", "A quantitative measure estimating the potential loss in value of a risky asset/portfolio over a defined period at a given confidence level."),
]
examprep = [
    "Risk types in banks: Credit, Interest Rate, Liquidity, Market, Operational.",
    "Risk management strategies: realistic business planning, risk assessment systems, securitisation, loss reserves, insurance transfer, contractual risk transfer, and risk retention.",
    "Risk management process: Identification &rarr; Measurement (VaR, sensitivity, volatility) &rarr; Pricing.",
    "CAMELS added 'Sensitivity to market risk' as its sixth component in 1997.",
    "Types of IRR: Gap/Mismatch, Basis, Embedded Option, Yield Curve, Price, Reinvestment.",
    "IRR managed via Earnings Perspective (NII/NIM, Gap Analysis) and Economic Value Perspective (market value sensitivity).",
]
questions = [
    ("Define risk and explain the major types of risk faced by banks.", "Risk is the probability of occurrence of specific unforeseen events causing an adverse financial impact. Banks face Credit Risk (borrower default), Interest Rate Risk (adverse rate movements), Liquidity Risk (inability to meet obligations), Market Risk (adverse price movements), and Operational Risk (failed processes/people/systems)."),
    ("Explain the different types of Interest Rate Risk.", "Gap/Mismatch Risk (differing asset-liability maturities), Basis Risk (uneven rate movements across instruments), Embedded Option Risk (prepayment/early withdrawal behaviour), Yield Curve Risk (shape/slope changes), Price Risk (bond price-yield sensitivity), and Reinvestment Risk (uncertain reinvestment rates)."),
    ("How is Interest Rate Risk measured and managed?", "Through the Earnings Perspective (analysing near-term impact on Net Interest Income/Margin via Gap Analysis) and the Economic Value Perspective (analysing the impact on the market value of assets, liabilities, and net worth)."),
    ("Describe the risk management process followed by banks.", "Risk Identification at the transaction and portfolio level, Risk Measurement using quantitative tools like Value at Risk and sensitivity analysis, and Risk Pricing to ensure capital held against risk is adequately rewarded."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 6 done")

# ================= Topic 7: Forex Risk & Credit Risk =================
fname, title, prev_link, next_link = T(7)
overview = ("Two more major risk categories for banks: Foreign Exchange (Forex) Risk, arising from currency "
            "fluctuations, and Credit Risk, arising when a borrower or counterparty fails to honour their "
            "obligations.")
notes = """
<h3>7.1 Meaning of Forex (Foreign Exchange) Risk</h3>
<p>Foreign exchange risk is the possibility of a gain or loss to a firm that occurs due to unanticipated changes in the cash flows, assets, liabilities, or operating income caused by a currency exchange rate fluctuation. It is measured by the variance of the domestic-currency value of assets, liabilities, or operating income that is attributable to unanticipated changes in exchange rates.</p>

<h3>7.2 Types of Forex Risks</h3>
<table class="compare">
<tr><th>Type</th><th>Meaning</th></tr>
<tr><td><strong>Transaction Risk/Exposure</strong></td><td>Arises when a firm's contractual cash flows (receivables/payables) are denominated in a foreign currency; the risk that the exchange rate will change before the transaction settles.</td></tr>
<tr><td><strong>Translation Risk/Exposure</strong></td><td>The risk that a company's foreign-currency-denominated assets/liabilities change in value (in home-currency terms) when translated into the home currency for consolidated financial statements, due to exchange rate movements.</td></tr>
<tr><td><strong>Economic (Operating) Exposure</strong></td><td>The risk that a firm's future cash flows and market value will be affected by unexpected exchange rate changes over the long term, impacting its competitive position.</td></tr>
</table>

<h3>7.3 Managing Transaction Risk</h3>
<p>Banks and companies use several techniques to hedge transaction exposure:</p>
<ol>
<li><strong>Forward Market Hedge:</strong> Locking in an exchange rate today for a transaction that will occur at a future date, via a forward contract.</li>
<li><strong>Money Market Hedge:</strong> Borrowing/lending in the money market in one currency to offset a future foreign-currency cash flow.</li>
<li><strong>Options Market Hedge:</strong> Using a currency option (a right, not obligation) to buy/sell a currency at a specified price, offering protection against adverse moves while allowing benefit from favourable moves (for a premium).</li>
<li><strong>Swaps:</strong> A swap of one currency's principal and/or interest payments for another's, allowing firms to obtain more attractive financing while managing currency exposure.</li>
<li><strong>Exposure Netting:</strong> Offsetting exposures in one currency with exposures in the same or another currency, so that gains/losses on the two positions offset each other.</li>
<li><strong>Leading and Lagging:</strong> Adjusting the timing of a foreign-currency payment/receipt (paying early = "leading", delaying = "lagging") to take advantage of expected exchange rate movements.</li>
<li><strong>Invoicing/Billing in the Desired Currency:</strong> Invoicing exports/imports in the firm's home currency to shift the exchange rate risk to the counterparty.</li>
</ol>

<h3>7.4 Managing Translation Risk</h3>
<p>Translation exposure can be managed via a <strong>Balance-Sheet Hedge</strong>: matching the amount of exposed foreign-currency assets to exposed foreign-currency liabilities on the balance sheet, so that a change in exchange rate affects both sides similarly, minimising the net translation gain/loss.</p>

<h3>7.5 Meaning of Credit Risk</h3>
<p>Credit risk is the possibility of a loss resulting from a borrower's failure to repay a loan or meet contractual obligations. Traditionally, it refers to the risk that a lender may not receive the owed principal and interest, resulting in an interruption of cash flows and increased costs for collection.</p>

<h3>7.6 Types of Credit Risk</h3>
<ol>
<li><strong>Default Risk:</strong> The risk that a borrower will be unable to make the required payments on their debt obligation.</li>
<li><strong>Downgrade Risk:</strong> The risk that a bond's credit rating will be downgraded, causing its price to decline due to the increased risk perceived by investors.</li>
<li><strong>Credit Spread Risk:</strong> The risk that the yield spread (the difference between the yield on a risky bond and a benchmark/government bond) between two bonds changes, affecting the relative price of the riskier bond.</li>
</ol>

<h3>7.7 Methods of Mitigating Credit Risk</h3>
<ol>
<li><strong>Risk-Based Pricing:</strong> Lenders may charge a higher interest rate to borrowers who are more likely to default, based on an assessment of the applicant's credit risk (via credit scoring, rating agencies, etc.).</li>
<li><strong>Covenants:</strong> Lenders may write covenants (conditions) into loan agreements, such as requiring the borrower to maintain certain financial ratios or restricting further borrowing.</li>
<li><strong>Credit Insurance and Credit Derivatives:</strong> Transferring credit risk to a third-party insurer, or using credit derivatives to hedge against default.</li>
<li><strong>Tightening/Diversification:</strong> Reducing the amount of credit extended overall, or diversifying the loan portfolio across borrowers/sectors to reduce concentration risk.</li>
</ol>
"""
terms = [
    ("Forex (Foreign Exchange) Risk", "The possibility of gain or loss from unanticipated changes in exchange rates affecting a firm's cash flows, assets, or liabilities."),
    ("Transaction Exposure", "Forex risk arising from contractual foreign-currency cash flows before they settle."),
    ("Translation Exposure", "Forex risk arising when foreign-currency assets/liabilities are translated into the home currency for financial statements."),
    ("Credit Risk", "The risk of loss from a borrower's failure to repay a loan or meet contractual obligations."),
    ("Downgrade Risk", "The risk that a bond issuer's credit rating is downgraded, reducing the bond's price."),
]
examprep = [
    "Forex Risk types: Transaction (contractual cash flows), Translation (balance sheet consolidation), Economic (long-term competitive position).",
    "Managing Transaction Risk: forward/money-market/options hedges, swaps, exposure netting, leading/lagging, invoicing in home currency.",
    "Translation Risk managed via a Balance-Sheet Hedge (matching exposed foreign assets to foreign liabilities).",
    "Credit Risk types: Default Risk, Downgrade Risk, Credit Spread Risk.",
    "Credit risk mitigation: risk-based pricing, loan covenants, credit insurance/derivatives, tightening/diversification.",
]
questions = [
    ("Explain the different types of foreign exchange risk.", "Transaction Risk (from contractual foreign-currency cash flows before settlement), Translation Risk (from restating foreign-currency assets/liabilities into the home currency for financial statements), and Economic Exposure (long-term impact of exchange rate changes on a firm's cash flows and competitive position)."),
    ("How can a firm manage transaction exposure to forex risk?", "Through forward market hedges, money market hedges, options hedges, currency swaps, exposure netting, adjusting payment timing (leading/lagging), and invoicing transactions in the firm's home currency."),
    ("What is credit risk? Explain its types.", "Credit risk is the risk of loss from a borrower's failure to meet contractual obligations. Its types are Default Risk (failure to pay), Downgrade Risk (credit rating decline reducing bond price), and Credit Spread Risk (widening yield spread relative to a benchmark)."),
    ("What methods can banks use to mitigate credit risk?", "Risk-based pricing (charging riskier borrowers more), loan covenants, credit insurance and credit derivatives, and tightening or diversifying the loan portfolio to reduce concentration."),
]
U.write(fname, U.page(fname, 7, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 7 done")

# ================= Topic 8: Market, Operational & Solvency Risk =================
fname, title, prev_link, next_link = T(8)
overview = ("This topic rounds off the risk-types coverage with Market Risk (from price/rate movements), "
            "Operational Risk (from failed internal processes), and Solvency Risk (a bank's ability to meet "
            "its long-term obligations).")
notes = """
<h3>8.1 Meaning of Market Risk</h3>
<p>Market risk encompasses the risk of losses of financial assets due to adverse movements in market variables. Market risk arises out of all types of market activities, and cannot be avoided by any institution engaged in these activities. Unlike credit risk (specific to a borrower), market risk affects most or all firms simultaneously, since it originates from broad economic/financial factors.</p>

<h3>8.2 Types of Market Risk</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">8.2.1 Price Risk</h4>
<ul>
<li><strong>Symmetrical Risk:</strong> An increase or decrease in a security's price has a corresponding, proportional impact in either direction.</li>
<li><strong>Unsymmetrical Risk:</strong> A change in price in one direction leads to a disproportionate impact (positive or negative) in the value of a position, as with options.</li>
</ul>
<ul style="margin-top:10px">
<li><strong>Foreign Exchange Risk:</strong> Risk from movements in exchange rates affecting the value of foreign-currency assets and liabilities.</li>
<li><strong>Systemic Risk:</strong> The risk of failure of a large financial institution triggering a collapse across an entire financial system.</li>
<li><strong>Absolute Risk versus Relative Risk:</strong> Absolute risk measures the total potential loss, while Relative Risk measures a portfolio's risk relative to a benchmark.</li>
</ul>

<h3>8.3 Methods of Mitigating Market Risk</h3>
<ol>
<li><strong>Value at Risk (VaR):</strong> A statistical technique estimating the maximum potential loss on a portfolio over a specific time period at a given confidence level.</li>
<li><strong>Stress Testing:</strong> Simulating extreme market scenarios to determine the resilience of a bank's portfolio under adverse conditions.</li>
<li><strong>Diversification:</strong> Holding a range of assets/exposures so that losses in one are offset by gains (or smaller losses) in others.</li>
<li><strong>Effective Systems:</strong> Building customised models, data collection, and performing sophisticated analysis to analyse, rank, and manage various financial risks.</li>
</ol>

<h3>8.4 Meaning of Operational Risk</h3>
<p>Operational risk is the risk of loss resulting from inadequate or failed internal processes, people, and systems, or from external events. Operational risk can result in direct financial loss, or indirect losses through reputational damage or destruction of property.</p>

<h3>8.5 Types of Operational Risk</h3>
<ol>
<li><strong>People Risk:</strong> Risk from insufficient staff training and development, human error, fraud, dishonesty, or a failure to comply with internal policies, and incentives that are not aligned with the institution's overall risk management objectives.</li>
<li><strong>System Risk:</strong> Risk arising from technology becoming increasingly integral to business processes and infrastructure, including system failures, data breaches, cyber security incidents, and loss of critical business data.</li>
<li><strong>Event Risk:</strong> Risk from unforeseen external events (natural disasters, regulatory changes, political events) that can significantly impact business operations.</li>
</ol>

<h3>8.6 Management of Operational Risk</h3>
<ol>
<li><strong>Risk Identification and Assessment:</strong> Identifying and assessing the various sources of operational risk, both internal and external, that could impact the organisation.</li>
<li><strong>Risk Assessment:</strong> Assessing existing controls and their adequacy for identified risks, and determining the residual risk exposure.</li>
<li><strong>Risk Monitoring and Control:</strong> Establishing an adequate system to monitor operational risk exposures and material losses, with regular reviews and appropriate reporting to senior management/board.</li>
</ol>

<h3>8.7 Solvency Risk</h3>
<p>Solvency risk is the risk that a bank will be unable to meet its long-term financial obligations, i.e. that its liabilities exceed its assets. A firm is insolvent if it cannot maintain a positive net worth beyond a given level, and creditors/shareholders perceive the low equity capital as a signal that a bank is more likely to fail. Capital risk (having too little equity capital relative to a bank's assets) is a key indicator of solvency risk &mdash; the greater a bank's equity capital, the greater the bank's cushion of protection against insolvency.</p>

<h3>8.8 Non-Performing Assets (NPAs) &mdash; Concept</h3>
<p>The Securitisation and Reconstruction of Financial Assets and Enforcement of Security Interest Act (SARFAESI) defines Non-Performing Assets (NPAs) as an "asset or account of a borrower, which has been classified by a bank or financial institution as sub-standard, doubtful, or loss asset". Once a loan account has remained overdue for a period of 90 days, it is classified as an NPA.</p>
"""
terms = [
    ("Market Risk", "The risk of loss from adverse movements in market prices, rates, and other broad economic/financial variables."),
    ("Value at Risk (VaR)", "A statistical measure of the maximum expected loss on a portfolio over a given time horizon at a specified confidence level."),
    ("Operational Risk", "The risk of loss from inadequate or failed internal processes, people, and systems, or from external events."),
    ("Solvency Risk", "The risk that a bank's liabilities will exceed its assets, threatening its ability to meet long-term obligations."),
]
examprep = [
    "Market Risk types: Price Risk (symmetrical/unsymmetrical), Forex Risk, Systemic Risk, Absolute vs Relative Risk.",
    "Market risk mitigation: VaR, Stress Testing, Diversification, effective risk-analysis systems.",
    "Operational Risk types: People Risk, System Risk, Event Risk; managed via identification, assessment, and monitoring/control.",
    "Solvency Risk = liabilities exceeding assets; higher equity capital = greater cushion against insolvency.",
    "NPA (per SARFAESI) = an asset/account classified as sub-standard, doubtful, or loss, generally after 90 days overdue.",
]
questions = [
    ("What is market risk? Explain its types.", "Market risk is the risk of loss from adverse movements in market prices/rates, affecting most institutions simultaneously. Its types include Price Risk (symmetrical/unsymmetrical), Foreign Exchange Risk, Systemic Risk, and Absolute versus Relative Risk."),
    ("Explain the types of operational risk in banks.", "People Risk (staff error, fraud, misaligned incentives), System Risk (technology failures, cyber security, data loss), and Event Risk (unforeseen external events like natural disasters or regulatory changes)."),
    ("What is solvency risk? How is it related to a bank's capital?", "Solvency risk is the risk that a bank's liabilities exceed its assets, threatening its ability to meet long-term obligations. A bank's equity capital acts as a cushion against insolvency &mdash; the greater the capital relative to assets, the lower the solvency risk."),
    ("Define Non-Performing Asset (NPA) as per SARFAESI.", "Under the SARFAESI Act, an NPA is an asset or account of a borrower classified by a bank or financial institution as sub-standard, doubtful, or loss, generally once the account has remained overdue for 90 days."),
]
U.write(fname, U.page(fname, 8, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 8 done")

# ================= Topic 9: Non-Performing Assets (NPAs) =================
fname, title, prev_link, next_link = T(9)
overview = ("NPAs are one of the most closely watched indicators of a bank's health. This topic covers how "
            "loan assets are classified, how provisioning and NPA ratios are calculated, what causes NPAs to "
            "rise, and the methods banks use to recover them.")
notes = """
<h3>9.1 Concept of NPA</h3>
<p>The Securitisation and Reconstruction of Financial Assets and Enforcement of Security Interest Act, 2002 (SARFAESI) defines a Non-Performing Asset (NPA) as "an asset or account of a borrower, which has been classified by a bank or financial institution as sub-standard, doubtful, or loss asset". This happens once a loan account has remained overdue for 90 days from the due date.</p>

<h3>9.2 Categories of NPA Assets</h3>
<table class="compare">
<tr><th>Category</th><th>Meaning</th></tr>
<tr><td><strong>Standard Assets</strong></td><td>Loans/advances that do not carry more than the normal risk; not classified as an NPA. Provisioning: 0.4% (Direct Advances to Agriculture &amp; SME) or 0.25%-1% depending on sector.</td></tr>
<tr><td><strong>Sub-Standard Assets</strong></td><td>An asset that has remained an NPA for a period less than or equal to 12 months. Collateral value is insufficient to fully cover the outstanding amount if it becomes NPA.</td></tr>
<tr><td><strong>Doubtful Assets</strong></td><td>An asset that has remained in the sub-standard category for more than 12 months. Full recovery of the loan is highly questionable.</td></tr>
<tr><td><strong>Loss Assets</strong></td><td>An asset identified as a loss by the bank, auditors, or RBI inspection, but not yet written off wholly. Considered uncollectible with negligible realisable value.</td></tr>
</table>

<h3>9.3 Provisioning Norms</h3>
<p>Banks must maintain provisions for loan losses depending on the asset category, as recommended by the RBI:</p>
<table class="compare">
<tr><th>Asset Category</th><th>Minimum Provisioning</th></tr>
<tr><td>Standard Assets</td><td>0.25% &ndash; 1% (varies by sector; 0.40% for direct advances to Agriculture and SME sectors)</td></tr>
<tr><td>Sub-Standard Assets</td><td>15% of the outstanding amount for secured advances; 25% for the unsecured exposure portion</td></tr>
<tr><td>Doubtful Assets</td><td>Ranges from 25%-100% depending on how long the asset has been doubtful and whether it is secured/unsecured (higher provisioning for older or unsecured doubtful assets)</td></tr>
<tr><td>Loss Assets</td><td>100% of the outstanding amount</td></tr>
</table>

<h3>9.4 Calculation of NPAs</h3>
<p><strong>Gross NPA:</strong> The sum of all loan assets that have been classified as NPA as per RBI guidelines, without deducting any provisions made. Gross NPA reflects the quality of a bank's loans.</p>
<p style="text-align:center;font-weight:600;color:var(--accent-dark)">Gross NPA Ratio = Gross NPAs &divide; Total Advances &times; 100</p>
<p><strong>Net NPA:</strong> Gross NPA minus the provisions held for that account (interest in suspense account, part payment received and kept in suspense, and DICGC/ECGC claims received and held).</p>
<p style="text-align:center;font-weight:600;color:var(--accent-dark)">Net NPA Ratio = (Gross NPAs &minus; Provisions) &divide; (Total Advances &minus; Provisions) &times; 100</p>
<p>The difference between Gross and Net NPA is the amount of provisions held in respect of NPA accounts. Net NPA reflects the actual burden the bank carries after providing for expected losses.</p>

<h3>9.5 Causes of Rise in NPAs</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">9.5.1 Internal Causes</h4>
<ol>
<li><strong>Defective Lending Process:</strong> Every bank has its own lending policy based on three cardinal principles: Principle of Safety, Principle of Liquidity, and Principle of Profitability, and any negligence in following these results in NPAs.</li>
<li><strong>Inappropriate Technology:</strong> Banks not constantly updating technology for real-time credit monitoring and management.</li>
<li><strong>Managerial Deficiencies:</strong> The banker should always ensure before granting credit that the borrower is technically feasible, financially viable, and economically viable.</li>
<li><strong>Absence of Regular Industrial Visits:</strong> Lack of periodic visits to assess how the loan is being used.</li>
<li><strong>Poor Credit Appraisal System:</strong> Deficiencies in the appraisal of proposals before sanctioning credit facilities.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">9.5.2 External Causes</h4>
<ol>
<li><strong>Industrial Sickness:</strong> Genuine problems faced by industries, e.g. shortage of raw materials, power, and infrastructure.</li>
<li><strong>Change in Government Policies:</strong> Sudden policy changes can significantly affect industries and their ability to repay loans.</li>
<li><strong>Natural Calamities:</strong> Droughts, floods, cyclones, etc., are a significant cause of rising NPAs in agriculture-linked lending.</li>
<li><strong>Wilful Defaults:</strong> Borrowers who have the capacity to repay but wilfully avoid repaying the loan.</li>
<li><strong>Lack of Demand:</strong> A slowdown in demand can leave businesses unable to service debt from expected revenue.</li>
</ol>

<h3>9.6 Methods of Recovery of NPAs</h3>
<table class="compare">
<tr><th>Method</th><th>Description</th></tr>
<tr><td><strong>Securitisation (SARFAESI Act)</strong></td><td>Banks can transfer NPAs to Asset Reconstruction Companies (ARCs) or Securitisation Companies (SCs) via issue of security receipts, or recover dues by seizing/selling secured assets without court intervention.</td></tr>
<tr><td><strong>Compromise/One Time Settlement (OTS)</strong></td><td>A negotiated settlement where the borrower pays a lump sum less than the full outstanding amount, resolving the account and avoiding lengthy litigation.</td></tr>
<tr><td><strong>Debt Recovery Tribunals (DRTs)</strong></td><td>Established under the Debt Recovery Tribunal Act to facilitate speedy recovery of loans, with dedicated tribunals hearing bank recovery suits.</td></tr>
<tr><td><strong>Lok Adalat</strong></td><td>A legal platform to facilitate the speedy settlement of small loan disputes (typically up to &#8377;20 lakh) between banks and defaulters, outside regular courts.</td></tr>
<tr><td><strong>Recovery Camps</strong></td><td>Camps set up by banks in branches/villages to encourage settlement with defaulters through direct engagement.</td></tr>
<tr><td><strong>Suit Filing</strong></td><td>Filing a civil suit in court to recover the outstanding dues when other methods fail.</td></tr>
<tr><td><strong>Technical Write-Off</strong></td><td>Writing off a fully-provided NPA from the bank's books for accounting purposes, though recovery efforts against the borrower continue.</td></tr>
</table>
<p><strong>Remedial Strategies:</strong> Asset Reconstruction (transferring or selling stressed assets), Recovery through Credit Guarantee Schemes/Debt Recovery Tribunals, and Compromise Proposals (negotiated reduced settlement).</p>
"""
terms = [
    ("Non-Performing Asset (NPA)", "A loan asset classified as sub-standard, doubtful, or loss (per SARFAESI), typically once overdue for 90 days."),
    ("Gross NPA", "The total of all loan assets classified as NPA, before deducting provisions."),
    ("Net NPA", "Gross NPA minus provisions held against those accounts, reflecting the bank's actual residual exposure."),
    ("SARFAESI Act, 2002", "Allows banks to recover NPAs by seizing/selling secured assets without court intervention, and enables Asset Reconstruction Companies."),
    ("One Time Settlement (OTS)", "A negotiated lump-sum settlement between a bank and a defaulting borrower for less than the full outstanding amount."),
    ("Debt Recovery Tribunal (DRT)", "A specialised tribunal for the speedy recovery of bank loan dues."),
]
examprep = [
    "NPA categories: Standard &rarr; Sub-Standard (&le;12 months NPA) &rarr; Doubtful (&gt;12 months) &rarr; Loss (identified uncollectible).",
    "Provisioning: Standard 0.25-1%, Sub-Standard 15% (secured)/25% (unsecured), Doubtful 25-100%, Loss 100%.",
    "Gross NPA Ratio = Gross NPAs/Total Advances x 100; Net NPA Ratio = (Gross NPA - Provisions)/(Total Advances - Provisions) x 100.",
    "Internal causes of NPAs: defective lending, outdated technology, managerial deficiencies, no industrial visits, poor credit appraisal.",
    "External causes: industrial sickness, government policy changes, natural calamities, wilful default, demand slowdown.",
    "Recovery methods: SARFAESI/Securitisation, One Time Settlement, DRTs, Lok Adalat, Recovery Camps, Suit Filing, Technical Write-Off.",
]
questions = [
    ("Explain the categories of NPA assets with their provisioning requirements.", "Standard Assets (normal risk, 0.25-1% provisioning), Sub-Standard Assets (NPA up to 12 months, 15% secured/25% unsecured provisioning), Doubtful Assets (NPA over 12 months, 25-100% provisioning), and Loss Assets (identified as uncollectible, 100% provisioning)."),
    ("Distinguish between Gross NPA and Net NPA.", "Gross NPA is the total of all loan assets classified as NPA without deducting provisions, reflecting overall loan quality. Net NPA is Gross NPA minus provisions held, reflecting the bank's actual residual exposure after accounting for expected losses."),
    ("Discuss the internal and external causes of rising NPAs.", "Internal causes include defective lending processes, outdated technology, managerial deficiencies in assessing borrowers, absence of regular industrial visits, and poor credit appraisal systems. External causes include industrial sickness, changes in government policy, natural calamities, wilful default, and demand slowdowns."),
    ("Explain the various methods available to banks for recovery of NPAs.", "Securitisation under the SARFAESI Act, Compromise/One Time Settlement, Debt Recovery Tribunals, Lok Adalat for small disputes, Recovery Camps, filing civil suits, and Technical Write-Off of fully-provided accounts."),
]
U.write(fname, U.page(fname, 9, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 9 done")

# ================= Topic 10: Mergers & Acquisitions of Banks =================
fname, title, prev_link, next_link = T(10)
overview = ("Unit 2 closes by looking outward at how banks themselves combine and consolidate through "
            "mergers and acquisitions, the different forms these take, and the regulatory guidelines that "
            "govern them in India.")
notes = """
<h3>10.1 Introduction to Bank Mergers</h3>
<p>A merger refers to combining two or more bank companies, in order to reduce risks by diversifying, or for other reasons like increasing efficiency. Banks are taking place in the world economy at a rapid rate for any economy, the most crucial concern in market competition. Obviously there are risks in this analysis, banks need to balance the risk of every country and diversify their financial systems and national consolidation of regional and other financial systems and products, for which banks are going for mergers, to balance the deposit and credit portfolios, around the world.</p>

<h3>10.2 Types of Mergers</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Horizontal Merger</strong></td><td>A merger between two banks in the same line of business, combining similar products/services (e.g. two commercial banks merging), typically to reduce competition and gain economies of scale.</td></tr>
<tr><td><strong>Vertical Merger</strong></td><td>A merger between firms at different stages of the value chain that supply raw materials/services to one another, aimed at reducing costs through combined operations.</td></tr>
<tr><td><strong>Conglomerate Merger</strong></td><td>A merger between firms engaged in entirely unrelated business activities, often to diversify into new markets.</td></tr>
<tr><td><strong>Market Extension Merger</strong></td><td>A merger between firms selling the same products/services but in different markets, expanding market extension/reach.</td></tr>
<tr><td><strong>Product Extension Merger</strong></td><td>A merger of firms selling different but related products in the same market, expanding the combined firm's product line.</td></tr>
</table>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Other Kinds of Mergers</h4>
<ul>
<li><strong>Cash Merger:</strong> Shareholders of the target company receive cash in exchange for their shares, rather than shares in the surviving company.</li>
<li><strong>Short-Form Merger:</strong> A simplified merger process available when the parent company already owns a very high percentage of the subsidiary's shares (a de facto merger).</li>
<li><strong>Reverse Merger:</strong> A private company acquires a public company (often as a route to going public without an IPO).</li>
<li><strong>De Facto Merger:</strong> The acquisition of assets of one firm by another in legal form, but which is treated as a merger in substance.</li>
</ul>

<h3>10.3 Advantages of Mergers with Smaller Banks</h3>
<ul>
<li>Helps smaller banks that would otherwise struggle to compete and survive independently gain a wider capital base.</li>
<li>Increases access to funds, technology, and a broader customer base for the smaller institution.</li>
<li>Facilitates faster growth through combined resources rather than organic expansion alone.</li>
</ul>

<h3>10.4 Disadvantages of Mergers with Smaller Banks</h3>
<ul>
<li>Smaller banks lose their local/community character, which many customers value.</li>
<li>Weakens the PSB's/smaller bank's independence and may lead to job losses in redundant positions.</li>
<li>Career growth for staff may be affected as promotions/senior positions consolidate at the larger merged entity.</li>
<li>Regulatory scrutiny (by agencies like the FDIC/RBI) may make the merger process difficult and time-consuming to complete.</li>
</ul>

<h3>10.5 Recent Trends of Mergers and Acquisitions in Banks</h3>
<p>Recent trends and activities in the banking industry are causing some bank executives to look into the possibility of new mergers and acquisitions. Investor groups are forming and looking for opportunities to invest in a minority stake in banking businesses, with the intent to expand or capitalise on emerging financial technologies.</p>

<h3>10.6 Introduction to Acquisitions</h3>
<p>An acquisition is also known as a "takeover". A takeover happens when an acquiring company purchases either the shares or the assets of a target company, by paying cash, stock, or both, without necessarily combining the entities into a wholly new company (as a merger typically does).</p>

<h3>10.7 Types of Acquisitions</h3>
<ol>
<li><strong>Friendly Takeover:</strong> Where the target company's management and board agree to and support the acquisition.</li>
<li><strong>Hostile Takeover:</strong> Where the acquirer proceeds with the acquisition against the wishes of the target company's management, often by directly appealing to shareholders.</li>
<li><strong>Back-Flip Takeover:</strong> A rare form where the acquiring company becomes a subsidiary of the acquired (target) company.</li>
<li><strong>Reverse Takeover:</strong> A private company acquires a public company, becoming publicly listed without going through the traditional IPO process.</li>
</ol>

<h3>10.8 Disadvantages of Acquisition of Securities Firms</h3>
<ul>
<li>Cultural and integration challenges between the acquiring and target firm's operations and employees.</li>
<li>Overpaying for the target based on overly optimistic growth projections.</li>
<li>Regulatory and compliance complications, especially when acquiring firms operating in tightly regulated securities markets.</li>
</ul>

<h3>10.9 RBI Guidelines on Mergers and Acquisitions of Banks</h3>
<p>The RBI has laid down guidelines requiring prior approval for voluntary amalgamation of banking companies, requiring a viability/due-diligence assessment, safeguarding depositor interests, ensuring adequate capital adequacy of the merged entity, and requiring fair valuation and exchange ratio determination for shareholders of both entities before a merger or acquisition of a banking company can be approved.</p>
"""
terms = [
    ("Horizontal Merger", "A merger between two banks in the same line of business, typically to reduce competition and gain scale."),
    ("Hostile Takeover", "An acquisition pursued against the wishes of the target company's management, often via direct shareholder appeal."),
    ("Reverse Takeover", "A private company acquiring a public company to become listed without an IPO."),
    ("One Time Settlement (OTS)", "See Topic 9 &mdash; also relevant when a struggling bank's bad-debt position is a factor motivating a merger."),
]
examprep = [
    "Merger types: Horizontal, Vertical, Conglomerate, Market Extension, Product Extension; also Cash, Short-Form, Reverse, De Facto mergers.",
    "Mergers with smaller banks: pros = wider capital base, access to funds/tech; cons = loss of local character, job losses, regulatory scrutiny.",
    "Acquisition = takeover of shares/assets, without necessarily forming a new combined entity as in a merger.",
    "Takeover types: Friendly, Hostile, Back-Flip, Reverse.",
    "RBI mandates prior approval, viability assessment, depositor-interest safeguards, capital adequacy, and fair valuation for bank M&amp;A.",
]
questions = [
    ("Explain the different types of bank mergers.", "Horizontal (same business line), Vertical (different value-chain stages), Conglomerate (unrelated businesses), Market Extension (same product, different markets), and Product Extension (different but related products, same market) mergers, along with Cash, Short-Form, Reverse, and De Facto merger structures."),
    ("Discuss the advantages and disadvantages of mergers with smaller banks.", "Advantages include a wider capital base, better access to funds and technology, and faster growth. Disadvantages include loss of local/community character, job losses, reduced career growth opportunities for staff, and difficulty passing regulatory scrutiny."),
    ("Distinguish between a merger and an acquisition.", "A merger typically combines two companies into a new, unified entity by mutual agreement. An acquisition (takeover) involves one company purchasing another's shares or assets, without necessarily forming an entirely new combined company."),
    ("Explain the different types of takeovers.", "Friendly Takeover (target management supports it), Hostile Takeover (pursued against target management's wishes), Back-Flip Takeover (acquirer becomes a subsidiary of the target), and Reverse Takeover (a private company acquires a public one to become listed)."),
]
U.write(fname, U.page(fname, 10, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Ten topics covering fund management and risk in Indian banks: capital adequacy and deposits, loan management, investment management, asset-liability management, financial distress, general risk management and interest rate risk, forex and credit risk, market/operational/solvency risk, non-performing assets, and bank mergers &amp; acquisitions.")

print("Unit 2 (Banking & Financial Services) complete: all 10 topics + index written.")
