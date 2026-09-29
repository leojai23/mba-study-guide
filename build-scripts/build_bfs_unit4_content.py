# -*- coding: utf-8 -*-
import common

SUBJECT_ROOT = r"G:\Leo-Workspace\MBA-Study-Guide\Banking-and-Financial-Services\units"
BOOK_HTML = "Book: <em>Banking and Financial Services</em> (BA4003, Anna University MBA Sem III) &mdash; Thakur Publication"
BOOK_PLAIN = "Banking and Financial Services (BA4003), Thakur Publication"
NAVY_THEME = dict(accent="#1e3a5f", accent_dark="#15293f", accent_light="#e8eef5",
                   border="#d6dfe8", shadow="rgba(30,58,95,.14)")

TOPICS = [
    ("topic1-asset-based-services-and-nbfcs.html", "Asset Based Financial Services &amp; NBFCs"),
    ("topic2-leasing-concepts-types-parties.html", "Leasing &mdash; Concepts, Types &amp; Parties"),
    ("topic3-leasing-financial-evaluation.html", "Leasing &mdash; Financial Evaluation"),
    ("topic4-hire-purchase.html", "Hire Purchase"),
    ("topic5-underwriting.html", "Underwriting"),
    ("topic6-mutual-funds-concept-structure-types.html", "Mutual Funds &mdash; Concept, Structure &amp; Types"),
    ("topic7-mutual-funds-classification-pros-cons.html", "Mutual Funds &mdash; Classification, Advantages &amp; Disadvantages"),
]

U = common.UnitBuilder(4, "Asset Based Financial Services", TOPICS,
                        subject="Banking and Financial Services", subject_root=SUBJECT_ROOT,
                        book_html=BOOK_HTML, book_plain=BOOK_PLAIN, theme=NAVY_THEME)

def T(i):
    fname, title = TOPICS[i-1]
    prev_link = (TOPICS[i-2][0], TOPICS[i-2][1]) if i > 1 else None
    next_link = (TOPICS[i][0], TOPICS[i][1]) if i < len(TOPICS) else None
    return fname, title, prev_link, next_link

# ================= Topic 1: Asset Based Financial Services & NBFCs =================
fname, title, prev_link, next_link = T(1)
overview = ("Unit 4 opens by placing asset-based financial services within India's wider financial services "
            "market, then introduces Non-Banking Financial Companies (NBFCs) &mdash; the institutions that "
            "deliver most of these services outside traditional banks.")
notes = """
<h3>1.1 Asset Based Financial Services</h3>
<p>Asset-based financial services are those financial services that deal directly with the creation, use, or financing of an asset, rather than providing an unsecured loan. The five services listed under this category are: Leasing, Hire Purchase, Underwriting, and Mutual Funds (each covered in this unit), alongside the fee-based services covered in Unit 5.</p>

<h3>1.2 Nature of Financial Services</h3>
<ul>
<li><strong>Intangibility:</strong> Financial services are intangible in nature. The quality and innovation of the services provided determine the success of financial institutions in building customer trust and reliability.</li>
<li><strong>Customer Orientation:</strong> Financial institutions need to study their customers' needs in detail before designing and offering financial products/services.</li>
</ul>

<h3>1.3 Need for Financial Services</h3>
<ol>
<li><strong>Promotion of Investment and Savings:</strong> Financial services help mobilise savings from various sources and channel them into productive investment.</li>
<li><strong>Contribution to GDP:</strong> The financial sector's own earnings from services contribute meaningfully to the overall Gross Domestic Product.</li>
<li><strong>Provides Employment:</strong> The financial services sector requires various kinds of skilled manpower, contributing to employment in the country.</li>
<li><strong>Growth of Foreign Direct Investment (FDI):</strong> Financial services help attract and channel foreign direct investment into the country.</li>
<li><strong>Link between Savers and Investors:</strong> Financial services help bridge the gap between individual savers and institutional/individual investors who need funds.</li>
</ol>

<h3>1.4 Scope of Financial Services</h3>
<p>The scope of financial services is as follows: (1) Financial Services related to the Financial Market &mdash; institutions and instruments used to raise resources from the market; (2) Financial Services related to Asset Management &mdash; leasing, hire purchase, mutual funds, and related asset-based services; (3) Financial Services related to Fee-Based Advisory Services &mdash; merchant banking, credit rating, and other consultancy services.</p>

<h3>1.5 Objectives of Financial Services</h3>
<ol>
<li><strong>Fund Raising:</strong> To provide various types of financial instruments to enable both individuals and corporates to raise funds from the market.</li>
<li><strong>Funds Deployment:</strong> To ensure funds raised are deployed in the most productive way among competing uses.</li>
<li><strong>Specialised Services:</strong> To provide specialised services such as bill discounting, factoring, and securitisation of debt, to make the transfer of funds/assets easier.</li>
</ol>

<h3>1.6 Financial Services Market in India</h3>
<p>The financial services market can be divided into the wholesale market and the retail market. The wholesale market is used for converting financial products between institutions, while the retail market is used by individuals for retail financial products.</p>
<p>Traditional financial market segments include the Money Market (Treasury Bills, Commercial Papers, Certificates of Deposit) and the Capital Market (Stock Market, Bond Market). Modern financial services also include Fee-Based (Non-Fund Based) services such as Merchant Banking, Credit Rating, and Stock Broking, and Fund-Based services such as Leasing, Hire Purchase, Factoring, Forfaiting, Venture Capital, and Housing Finance.</p>

<h3>1.7 Meaning and Definition of NBFCs</h3>
<p>According to the Reserve Bank of India, a Non-Banking Financial Company (NBFC) is a company registered under the Companies Act, engaged in the business of loans and advances, acquisition of shares/stocks/bonds/debentures/securities, leasing, hire-purchase, insurance business, or chit-fund business, but does not include an institution whose principal business is agriculture, industrial activity, purchase/sale/construction of immovable property, or which is regulated by any other regulatory body under a specific statute.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Features of NBFCs</h4>
<ul>
<li>An NBFC cannot accept demand deposits (unlike a bank), though certain categories can accept term deposits.</li>
<li>NBFCs do not form part of the payment and settlement system, and cannot issue cheques drawn on themselves.</li>
<li>Deposit insurance (DICGC) facility is not available to depositors of NBFCs, unlike bank depositors.</li>
</ul>

<h3>1.8 Types of NBFCs</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Asset Finance Company (AFC)</strong></td><td>Financing physical assets like machinery, automobiles, generators, and material equipment, supporting productive/economic activity.</td></tr>
<tr><td><strong>Investment Company (IC)</strong></td><td>Engaged principally in the acquisition of securities.</td></tr>
<tr><td><strong>Loan Company (LC)</strong></td><td>Provides finance through loans/advances for purposes other than its own asset financing (e.g. working capital loans).</td></tr>
<tr><td><strong>Infrastructure Finance Company (IFC)</strong></td><td>Deploys the majority of its assets in infrastructure loans.</td></tr>
<tr><td><strong>Housing Finance Company (HFC)</strong></td><td>Principal business is financing acquisition/construction of houses.</td></tr>
<tr><td><strong>Micro Finance Institution (NBFC-MFI)</strong></td><td>Provides small-ticket loans to low-income households, typically without collateral.</td></tr>
<tr><td><strong>Residuary Non-Banking Company (RNBC)</strong></td><td>An NBFC whose principal business is receiving deposits under any scheme, but is not classified into any other specific category.</td></tr>
</table>

<h3>1.9 Difference between Banks and NBFCs</h3>
<table class="compare">
<tr><th>Basis</th><th>Banks</th><th>NBFCs</th></tr>
<tr><td>Deposits</td><td>Can accept demand deposits (savings/current accounts)</td><td>Cannot accept demand deposits, only certain types of term deposits</td></tr>
<tr><td>Payment System</td><td>Part of the payment and settlement system; can issue cheques on themselves</td><td>Not part of the payment system; cannot issue cheques drawn on themselves</td></tr>
<tr><td>Deposit Insurance</td><td>DICGC insurance available to depositors</td><td>Not available</td></tr>
<tr><td>Regulation</td><td>Regulated under the Banking Regulation Act, 1949</td><td>Regulated under Chapter III-B of the RBI Act, 1934</td></tr>
<tr><td>Reserve Requirements</td><td>Must maintain CRR and SLR</td><td>Not subject to CRR (though some liquidity norms apply)</td></tr>
</table>

<h3>1.10 RBI Regulatory Framework for NBFCs</h3>
<p>NBFCs are regulated by the Reserve Bank of India under Chapter III-B of the RBI Act, 1934. Key evolution: the NBFC regulatory framework was strengthened in 1997 (RBI (Amendment) Act) giving RBI more powers, and revised again in 2014 with a differentiated regulatory approach based on the size of NBFC deposits and assets (Systemically Important NBFCs, classified on the basis of an asset size threshold, face stricter prudential regulation similar to banks).</p>

<h3>1.11 Importance of NBFCs</h3>
<ul>
<li>Greater reach: NBFCs are present in remote areas of the country where banks may not have a presence, enabling wider access to finance.</li>
<li>Flexibility: NBFCs can offer more flexible/customised schemes suited to small and medium businesses.</li>
<li>Retail services: NBFCs help provide different types of financial services to small and medium enterprises that banks often overlook.</li>
</ul>

<h3>1.12 Challenges Facing NBFCs</h3>
<ul>
<li>Lack of investor awareness: Investors often do not know the full range of advantages NBFCs offer, compared to bank deposits.</li>
<li>Lack of recent data/transparency: NBFCs are expanding rapidly, but often lack the transparency and up-to-date data disclosure standards of banks.</li>
<li>Lack of qualified personnel: The various financial services offered require skilled employees, which can be a constraint for smaller NBFCs.</li>
<li>Lack of efficient work culture: Without having as robust a governance/work culture as banks, some NBFCs face operational inefficiencies.</li>
</ul>
"""
terms = [
    ("NBFC (Non-Banking Financial Company)", "A company registered under the Companies Act engaged in lending, investment, leasing, or hire-purchase business, but not accepting demand deposits like a bank."),
    ("Asset Finance Company (AFC)", "An NBFC that principally finances physical assets like machinery and equipment."),
    ("Housing Finance Company (HFC)", "An NBFC principally engaged in financing the acquisition or construction of houses."),
    ("Systemically Important NBFC", "An NBFC classified above a specified asset-size threshold, subject to stricter prudential regulation."),
]
examprep = [
    "Financial services scope: Financial Market services, Asset Management services (leasing/hire-purchase/mutual funds), Fee-Based Advisory services.",
    "NBFC = company doing lending/investment/leasing/hire-purchase business, cannot accept demand deposits, not part of the payment system, no DICGC insurance.",
    "NBFC types: AFC, Investment Company, Loan Company, IFC, HFC, NBFC-MFI, RNBC.",
    "Banks vs NBFCs: Banks accept demand deposits, are part of the payment system, DICGC-insured, regulated by Banking Regulation Act; NBFCs are none of these, regulated under RBI Act Chapter III-B.",
]
questions = [
    ("Define NBFC and explain its key features.", "An NBFC is a company registered under the Companies Act engaged in lending, investment, leasing, or hire-purchase business. Key features: it cannot accept demand deposits, is not part of the payment and settlement system, and its depositors are not covered by DICGC deposit insurance."),
    ("Explain the different types of NBFCs.", "Asset Finance Company (physical asset financing), Investment Company (securities acquisition), Loan Company (general loans), Infrastructure Finance Company, Housing Finance Company, NBFC-MFI (microfinance), and Residuary Non-Banking Company."),
    ("Distinguish between banks and NBFCs.", "Banks can accept demand deposits, are part of the payment system, offer DICGC-insured deposits, and are regulated under the Banking Regulation Act with CRR/SLR requirements. NBFCs cannot accept demand deposits, are outside the payment system, offer no deposit insurance, and are regulated under Chapter III-B of the RBI Act."),
    ("What challenges do NBFCs face in India?", "Lack of investor awareness about their offerings, limited transparency/data disclosure compared to banks, a shortage of qualified personnel, and generally less efficient work culture/governance structures than banks."),
]
U.write(fname, U.page(fname, 1, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 1 done")

# ================= Topic 2: Leasing - Concepts, Types & Parties =================
fname, title, prev_link, next_link = T(2)
overview = ("Leasing lets a business use an asset without buying it outright. This topic covers what leasing "
            "is, its key elements and parties, and the many types of lease arrangements used in practice.")
notes = """
<h3>2.1 Meaning and Definition of Leasing</h3>
<p>According to Miller, Hill, and C.W. Upton: "Leasing separates ownership and facilitates use as two contractual arrangements (lease agreement) which is no more than a contractual agreement between the lessor and lessee." In simple terms, a lease payment is the amount owed by the lessor (asset owner) to the lessee (asset user) for the temporary use of the asset, provided under a lease agreement.</p>

<h3>2.2 Characteristics of Leasing</h3>
<ol>
<li><strong>Two Parties:</strong> Both the parties involved in a leasing transaction, i.e. the lessor and lessee, are as follows.</li>
<li><strong>No Ownership Transfer:</strong> Leasing is a contractual arrangement whereby the lessor grants the lessee the right to use the property/equipment owned by the lessor for an agreed period without transferring ownership.</li>
<li><strong>Periodic Payment:</strong> The lessee pays a periodic payment (lease rental) to the lessor for the use of the leased asset over the lease period.</li>
<li><strong>Return of Asset:</strong> At the end of the lease period, the leased equipment is returned to the lessor, or (in some cases) an option to purchase or renew is provided.</li>
</ol>

<h3>2.3 Elements of Leasing</h3>
<ol>
<li><strong>Parties to the Contract:</strong> Following are the main parties to a leasing contract &mdash; Lessor (owner) and Lessee (user).</li>
<li><strong>Assets:</strong> The subject matter of a leasing agreement, from a hut/property to any type of movable/immovable asset, including plant, machinery, equipment, land, buildings, and durables.</li>
<li><strong>Ownership Separated from User:</strong> Ownership is retained by the lessor throughout, while economic use of the asset passes to the lessee for the lease period.</li>
<li><strong>Term of Lease:</strong> This is a defined period of time during which the agreement for use of the asset is operative; the lease may be renewed or terminated at the end of the term, or extended by the lessor, corresponding interest, risk factor, and maintenance charges involved.</li>
</ol>

<h3>2.4 Parties Involved in Leasing</h3>
<ul>
<li><strong>Lessor:</strong> The person who owns or rents out the property under a leasing contract. Such person may also be called the property owner, or (in the case of capital leases) a lender.</li>
<li><strong>Lessee:</strong> The main type of person engaged in a leasing contract. This is called a tenant, in the case of real estate leases, such person is known as a tenant.</li>
</ul>

<h3>2.5 Modes of Terminating a Lease</h3>
<ol>
<li>The lease may be renewed or followed by another lease.</li>
<li>The asset goes back to the lessor.</li>
<li>The lessor sells off the asset to a third party.</li>
</ol>

<h3>2.6 Types of Leasing</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Financial Lease</strong></td><td>A long-term, non-cancellable lease where the lessee bears most risks/rewards of ownership; the lease term generally covers most of the asset's economic life; rentals are calculated to fully recover the lessor's investment plus a return.</td></tr>
<tr><td><strong>Operating Lease</strong></td><td>A short-term, cancellable lease where the lessor bears the risks and provides maintenance; the lease term is much shorter than the asset's economic life, and the asset can be leased to multiple lessees over its life.</td></tr>
<tr><td><strong>Sale and Lease Back</strong></td><td>The owner of an asset (lessee) sells it to another party (lessor), and immediately leases it back, receiving immediate cash while retaining use of the asset.</td></tr>
<tr><td><strong>Direct Lease</strong></td><td>A direct lease transaction where the lessee acquires the right to use an asset from the manufacturer/owner directly, as either a bipartite (two-party) or tripartite (three-party, involving equipment supplier, lessor, lessee) lease.</td></tr>
<tr><td><strong>Leveraged Lease</strong></td><td>A lease involving three parties &mdash; lessor, lessee, and a lender &mdash; where the lessor borrows a large part of the purchase price of the asset from the lender, using the asset and lease rentals as collateral.</td></tr>
<tr><td><strong>Domestic Lease</strong></td><td>A lease where all parties involved belong to the same country.</td></tr>
<tr><td><strong>International/Cross-Border Lease</strong></td><td>A lease where the lessor and lessee belong to different countries.</td></tr>
<tr><td><strong>Single Investor Lease</strong></td><td>A two-party lease transaction between the lessor and lessee (no third-party lender involved), where the lessor's role is played by the leasing company itself.</td></tr>
</table>

<h3>2.7 Steps in Leasing Transactions</h3>
<ol>
<li>The lessee selects the asset/equipment needed and identifies the manufacturer/supplier.</li>
<li>The lessee approaches a leasing company (lessor) and negotiates the terms of the lease agreement.</li>
<li>The leasing company purchases the asset from the manufacturer/supplier, in its own name.</li>
<li>The leasing company delivers the asset to the lessee under the terms of the lease agreement.</li>
<li>The lessee pays periodic lease rentals to the lessor over the lease term.</li>
</ol>

<h3>2.8 Difference between Financial Lease and Operating Lease</h3>
<table class="compare">
<tr><th>Basis of Difference</th><th>Financial Lease</th><th>Operating Lease</th></tr>
<tr><td>Specificity</td><td>Asset is tailored to the lessee's specific needs</td><td>Generic asset, usable by multiple lessees</td></tr>
<tr><td>Cancellability</td><td>Non-cancellable during the primary lease period</td><td>Cancellable at short notice</td></tr>
<tr><td>Lease Period</td><td>Covers most or all of the asset's economic life</td><td>Much shorter than the asset's economic life</td></tr>
<tr><td>Risk</td><td>Borne by the lessee</td><td>Borne by the lessor</td></tr>
<tr><td>Ownership Risks</td><td>Obsolescence risk borne by the lessee</td><td>Obsolescence risk borne by the lessor</td></tr>
<tr><td>Maintenance</td><td>Lessee is responsible for maintenance/repairs</td><td>Lessor is responsible for maintenance/repairs</td></tr>
</table>
"""
terms = [
    ("Lessor", "The owner of an asset who grants another party the right to use it under a lease."),
    ("Lessee", "The party who obtains the right to use an asset from the lessor under a lease, in exchange for rental payments."),
    ("Financial Lease", "A long-term, non-cancellable lease where the lessee bears most risks/rewards of ownership over most of the asset's economic life."),
    ("Operating Lease", "A short-term, cancellable lease where the lessor retains ownership risk and provides maintenance."),
    ("Sale and Lease Back", "An arrangement where an asset owner sells the asset and immediately leases it back, gaining liquidity while retaining use."),
    ("Leveraged Lease", "A three-party lease (lessor, lessee, lender) where the lessor borrows most of the asset's purchase price."),
]
examprep = [
    "Leasing separates ownership (stays with lessor) from use (transferred to lessee) for a defined lease term, against periodic rentals.",
    "Types: Financial, Operating, Sale &amp; Lease Back, Direct (bipartite/tripartite), Leveraged, Domestic, International/Cross-Border, Single Investor.",
    "Financial Lease = long-term, non-cancellable, lessee bears risk, covers most of asset's life. Operating Lease = short-term, cancellable, lessor bears risk and maintenance.",
    "Steps: select asset &rarr; negotiate with lessor &rarr; lessor purchases asset &rarr; asset delivered to lessee &rarr; lessee pays periodic rentals.",
]
questions = [
    ("Define leasing and explain its key characteristics.", "Leasing is a contractual arrangement where the lessor grants the lessee the right to use an asset for an agreed period against periodic rental payments, without transferring ownership. Key characteristics: two parties (lessor/lessee), no ownership transfer, periodic payments, and return of the asset (or renewal/purchase option) at the end of the term."),
    ("Distinguish between financial lease and operating lease.", "A financial lease is long-term and non-cancellable, with the lessee bearing ownership-like risks over most of the asset's economic life. An operating lease is short-term and cancellable, with the lessor retaining risk and responsibility for maintenance, and the asset can be leased to multiple lessees."),
    ("Explain the different types of leasing arrangements.", "Financial Lease, Operating Lease, Sale and Lease Back (seller leases back the asset they sold), Direct Lease (bipartite/tripartite), Leveraged Lease (lessor borrows via a third-party lender), Domestic Lease, International/Cross-Border Lease, and Single Investor Lease."),
]
U.write(fname, U.page(fname, 2, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 2 done")

# ================= Topic 3: Leasing - Financial Evaluation =================
fname, title, prev_link, next_link = T(3)
overview = ("Should a business lease an asset or buy it outright? This topic covers the financial evaluation "
            "framework &mdash; from both the lessee's and lessor's point of view &mdash; and leasing's overall "
            "advantages and disadvantages.")
extra_note = '<div class="callout warn">The book works through full numerical NPV/IRR examples for lease evaluation. This page explains the method and formulas you need &mdash; apply them to whatever figures a problem gives you, rather than memorising the book\'s specific worked example.</div>'
notes = """
<h3>3.1 Financial Evaluation of Leasing</h3>
<p>The framework of financial evaluation of lease-purchase covers both the hirer's (lessee's) as well as the finance company's (lessor's) viewpoint.</p>

<h3>3.2 Lessee's Point of View</h3>
<p>The lessee's decision is essentially a "lease or buy" decision: should the asset be leased, or purchased using debt/equity financing? This is compared using one of two broad methods:</p>
<ol>
<li><strong>Net Present Value (NPV) Method:</strong> Compare the Present Value of Cash Outflows under leasing (lease rentals, net of tax shield on rentals) against the Present Value of Cash Outflows under buying (initial investment, less present value of depreciation tax shield, less present value of the eventual salvage value, plus present value of interest/maintenance where relevant). The alternative with the <strong>lower present value of cash outflow</strong> is preferred.</li>
<li><strong>Internal Rate of Return (IRR) Method:</strong> Calculate the discount rate at which the present value of cash inflows equals the present value of cash outflows for financing the asset by taking a loan (i.e. the implied "interest rate" of leasing versus borrowing). This is compared with the firm's cost of capital/borrowing rate to decide.</li>
</ol>
<p>Key steps in an NPV-based lease-or-buy analysis: (1) determine cash outflows under leasing (after-tax lease rentals); (2) determine cash outflows under buying (net of depreciation tax shield and salvage value); (3) discount both sets of cash flows to present value using an appropriate discount rate (usually the after-tax cost of debt); (4) select the option with the lower present value of outflow.</p>

<h3>3.3 Lessor's Point of View</h3>
<p>The lessor evaluates whether leasing the asset out is a worthwhile investment, from the following angles:</p>
<ol>
<li><strong>Cost of Equipment:</strong> The lessor's initial investment (cash outflow) in acquiring the asset to be leased.</li>
<li><strong>Net Cash Inflow:</strong> Lease rentals received (net of tax) form the primary cash inflow to the lessor over the lease term.</li>
<li><strong>Residual/Salvage Value:</strong> Any value recovered by the lessor when the asset is returned at the end of the lease term.</li>
<li><strong>Depreciation Tax Shield:</strong> Since the lessor retains ownership, they can claim depreciation on the asset, reducing their tax liability &mdash; this depreciation tax shield is a real cash benefit that must be included in the evaluation.</li>
</ol>
<p>The lessor typically evaluates the proposal using NPV (comparing the present value of net cash inflows, including the depreciation tax shield and salvage value, against the initial investment) or IRR (finding the discount rate that equates the present value of inflows to the investment, then comparing it to the lessor's required rate of return/cost of capital).</p>

<h3>3.4 Break-Even Lease Rental</h3>
<p>The lessor can also determine the minimum lease rental required to make the leasing proposal viable &mdash; the rental at which the Net Present Value of the transaction is exactly zero (i.e. the rental that would make the lessor indifferent between leasing the asset and not investing in it at all).</p>

<h3>3.5 Advantages of Leasing</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">To the Lessee</h4>
<ol>
<li><strong>Additional Source of Finance:</strong> Leasing allows a business to acquire the use of an asset without a large upfront capital outlay, making rentals payable from ongoing operating cash flow rather than existing capital.</li>
<li><strong>Less Expensive:</strong> Leasing can be less expensive than borrowing to buy, especially for a business without an established credit history, as it doesn't require the same level of collateral/security.</li>
<li><strong>Ownership Protected:</strong> Financial leases often dilute the promoters' control less than raising equity capital would, since it doesn't affect ownership/shareholding.</li>
<li><strong>Tax Benefit:</strong> Lease rentals are generally fully tax-deductible as a business expense, simplifying tax and documentation compared to owning and depreciating an asset.</li>
<li><strong>No Stringent Conditions:</strong> Unlike raising finance via debentures or loans, leasing typically involves fewer restrictive covenants/conditions on the lessee.</li>
<li><strong>High Profitability:</strong> Leasing frees up the lessee's own funds and borrowing capacity for other, potentially higher-return uses, since the asset itself needn't be purchased outright.</li>
</ol>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">To the Lessor</h4>
<ol>
<li><strong>Full Protection of Ownership:</strong> Since the lessor retains legal ownership, their interest is protected against the lessee's insolvency, unlike an unsecured loan.</li>
<li><strong>Tax Benefits:</strong> The lessor can claim depreciation on the leased asset, reducing tax liability.</li>
<li><strong>High Growth Potential:</strong> The leasing industry has significant growth potential as businesses seek asset-light financing options.</li>
</ol>

<h3>3.6 Disadvantages of Leasing</h3>
<ol>
<li><strong>No Ownership:</strong> Since the lessee never owns the asset (under an operating lease), they cannot claim depreciation benefits or build equity in the asset over time.</li>
<li><strong>Restrictive Terms/Conditions:</strong> Some lease agreements come with terms restricting the lessee's use, modification, or subletting of the asset.</li>
<li><strong>Loss on Termination:</strong> Early termination of a financial lease can involve substantial penalty payments to the lessor.</li>
<li><strong>Higher Cost over the Long Run:</strong> Over the full economic life of the asset, total lease payments can end up costing more than outright purchase, especially for financial leases.</li>
</ol>
"""
terms = [
    ("NPV Method (Lease Evaluation)", "Comparing the present value of cash outflows under leasing versus buying, preferring the option with the lower present value of outflow."),
    ("IRR Method (Lease Evaluation)", "Finding the discount rate that equates present value of cash inflows/outflows of the lease-versus-borrow decision, compared to the cost of capital."),
    ("Depreciation Tax Shield", "The tax saving a lessor gains from claiming depreciation on an asset it owns and leases out."),
    ("Break-Even Lease Rental", "The minimum lease rental at which the lessor's Net Present Value from the transaction is exactly zero."),
]
examprep = [
    "Lessee's lease-or-buy decision: compare PV of cash outflows (leasing vs buying) via NPV, or compare implied lease IRR to cost of capital.",
    "Lessor's evaluation: cost of equipment vs net cash inflows (after-tax rentals + depreciation tax shield + salvage value), via NPV or IRR.",
    "Break-even lease rental = rental at which lessor's NPV = 0.",
    "Leasing advantages (lessee): avoids large upfront outlay, less restrictive than loans, fully tax-deductible rentals, preserves borrowing capacity.",
    "Leasing disadvantages: no ownership/depreciation benefit to lessee, restrictive terms, termination penalties, potentially higher long-run cost.",
]
questions = [
    ("Explain the NPV method of evaluating a lease-or-buy decision from the lessee's point of view.", "The NPV method compares the present value of cash outflows under leasing (after-tax lease rentals) against the present value of cash outflows under buying (net of depreciation tax shield and salvage value), both discounted at an appropriate rate. The option with the lower present value of outflow is preferred."),
    ("What factors does a lessor consider when evaluating a leasing proposal?", "The initial cost of the equipment (investment), the net after-tax lease rentals receivable, the depreciation tax shield available since the lessor retains ownership, and the residual/salvage value expected at the end of the lease term &mdash; evaluated via NPV or IRR against the required rate of return."),
    ("What are the advantages of leasing to the lessee?", "It provides an additional source of finance without a large upfront outlay, is often less expensive than borrowing, doesn't dilute ownership/control, offers fully tax-deductible rentals, involves fewer restrictive conditions than loans, and frees up capital and borrowing capacity for other uses."),
    ("Discuss the disadvantages of leasing.", "The lessee gains no ownership or depreciation benefit (under an operating lease), may face restrictive terms on use of the asset, can incur significant penalties for early termination, and may end up paying more in total lease rentals than the asset would have cost to buy outright."),
]
U.write(fname, U.page(fname, 3, title, overview, notes, terms, examprep, questions, prev_link, next_link, extra_note=extra_note))
print("Topic 3 done")

# ================= Topic 4: Hire Purchase =================
fname, title, prev_link, next_link = T(4)
overview = ("Hire Purchase is another way to acquire an asset without full upfront payment, but unlike leasing "
            "it is designed to end in ownership. This topic covers its concept, parties, agreement, and how it "
            "differs from leasing.")
notes = """
<h3>4.1 Concept of Hire Purchase</h3>
<p>According to Pearce E.H. and Omrod R.C.: "a contract of hire purchase involves an element of both hire and purchase; the hirer, at the end of an agreed term, hire the asset on a fixed rental basis to be paid at agreed intervals, mutually agreed upon, and further the right to use the asset for financing capital assets, the owner in addition, letting the goods out, further requires financing beyond consumer goods."</p>
<p>As per Section 4 of the Hire-Purchase Act, 1972, every hire-purchase agreement should consist of the following contents:</p>
<ol>
<li>The cash price of the goods.</li>
<li>The hire-purchase price of the goods.</li>
<li>The date of commencement of the agreement.</li>
</ol>

<h3>4.2 Meaning and Definition of Hire Purchase Agreement</h3>
<p>A Hire Purchase Agreement is a legal agreement between the owner of the goods and the hirer, in which the owner provides the goods to the hirer for regular payment and also provides an option to the hirer to purchase the goods at the expiry of the hire period, in return for certain payment of hire, at the end of the agreement.</p>
<p>The Regional Transport Office (RTO) is informed of the hypothecation policy, since the vehicle (in a vehicle hire-purchase) will be registered with a note of the financing company's hypothecation on the R.C. book. This is cancelled and the endorsement duly deleted only upon completion of the instalment amount, in the R.C. book (Registration Certificate book) after the hypothecation policy is fully repaid.</p>

<h3>4.3 Features of Hire Purchase</h3>
<ol>
<li>A hire purchase contract has the following features: it is a legal contract for the acquisition of goods, purchase is made in instalments, and the hirer has the acceptance to purchase the goods.</li>
<li>The agreement can also be terminated at any time before the completion of the payment, with certain terms and conditions.</li>
<li>The consideration payable under the agreement is called the hire rental fee, and consists of the amount payable towards principal and interest charges.</li>
<li>The property in the goods passes to the hirer on payment of the last instalment.</li>
<li>The hirer is required to pay a down payment and the remaining instalments, over the remaining period of time, which is spread over the length of the loan, ranging from 20 to 25% of the total cost, in equal EMIs over 30 to 48 months.</li>
</ol>

<h3>4.4 Parties Involved in Hire Purchase</h3>
<ul>
<li><strong>Hire Vendor:</strong> The person who is the owner of the goods and lets them out on hire.</li>
<li><strong>Hire Purchaser:</strong> The person who takes possession of the goods and uses them, with the option to purchase them over a period of instalments.</li>
</ul>

<h3>4.5 Steps of Hire Purchase Transaction</h3>
<ol>
<li>Buyer is under obligation to pay equal amounts during the specified duration of time.</li>
<li>The ownership of the goods is transferred to the hire purchase customer upon payment of the last instalment.</li>
</ol>

<h3>4.6 Clauses/Contents of a Hire Purchase Agreement</h3>
<p>Following are the main features of a hire purchase agreement contract:</p>
<ol>
<li><strong>Nature of Agreement:</strong> The agreement specifies the nature and terms of the hire purchase, including the amount, date, and place of instalments.</li>
<li><strong>Delivery of Equipment:</strong> This part shows where the equipment is to be delivered to, the nature and location where delivery is to happen.</li>
<li><strong>Inspection:</strong> The hirer's obligation to allow the owner to inspect the equipment during the hire-purchase period.</li>
<li><strong>Repairs:</strong> The hirer is responsible for the maintenance of the equipment; if in breach of this duty, all legal requirements including delivered are to be borne by the hirer.</li>
<li><strong>Termination:</strong> If the hirer defaults, the hirer will not have any right to alter or dispose of the goods, and does not have the right to any legal requirements including obtaining prior approval of the owner.</li>
<li><strong>Alteration:</strong> The hirer cannot make alterations to the goods without the owner's prior approval.</li>
<li><strong>Risks:</strong> The hirer is responsible for the goods from the date of delivery, including risk of loss or damage caused by fire, theft, or accident.</li>
<li><strong>Registration and Fees:</strong> The hirer bears all legal requirements including registration and payment of the fees.</li>
</ol>

<h3>4.7 Types of Hire Purchase</h3>
<ol>
<li><strong>Consumer Instalment Credit:</strong> Hire purchase extended to individual consumers for goods such as household appliances.</li>
<li><strong>Industrial and Commercial Credit:</strong> Different forms of hire purchase agreements for industrial/commercial purposes, such as leasing/hiring machinery, financing, or agency collaborations.</li>
</ol>

<h3>4.8 Differences between Leasing and Hire Purchase</h3>
<table class="compare">
<tr><th>Basis of Differences</th><th>Leasing</th><th>Hire Purchase</th></tr>
<tr><td>Ownership</td><td>Ownership remains with the lessor throughout and after the lease term (unless a purchase option is separately exercised)</td><td>Ownership passes to the hirer automatically upon payment of the last instalment</td></tr>
<tr><td>Depreciation</td><td>Depreciation and other tax allowances (and its benefits) are claimed by the lessor</td><td>Depreciation is claimed by the hirer (hire purchaser), as they are the beneficial owner</td></tr>
<tr><td>Salvage Value</td><td>The lessor realises the salvage value of the asset at the end of the term</td><td>The hirer can claim salvage value once ownership passes to them</td></tr>
<tr><td>Magnitude</td><td>Usually used for financing larger assets</td><td>Usually used for financing smaller-value assets or consumer durables</td></tr>
<tr><td>Deductibility</td><td>The entire lease rental is a deductible expense for tax purposes</td><td>Only the interest component of the instalment is a deductible expense (the principal is a capital repayment)</td></tr>
<tr><td>Maintenance</td><td>Depends on the type of lease; often the lessor's responsibility (operating lease)</td><td>Generally the hirer's responsibility from the outset</td></tr>
</table>

<h3>4.9 Disadvantages of Hire Purchase</h3>
<ol>
<li><strong>High Growth Potential Not Guaranteed:</strong> The growth of the leasing/hire-purchase industry is affected by phases of economic recession or investment slowdown, which affects the sector's growth prospects.</li>
<li><strong>Ownership Delayed:</strong> The hirer does not own the asset until the very last instalment is paid, which can delay financing/refinancing options during the term.</li>
<li><strong>Cost of Delay:</strong> There may be delays in obtaining the confirmation certificate needed for the hirer to raise finance against the asset, as clearance from the financing company (owner) may take time.</li>
<li><strong>High Interest Cost:</strong> The interest embedded in hire-purchase instalments can be higher, in effective terms, than a straightforward bank loan for the same asset.</li>
</ol>

<h3>4.10 Advantages of Hire Purchase</h3>
<ol>
<li><strong>Easy Repayment:</strong> The hirer gets immediate possession of the asset while spreading payment over instalments, easing the cash-flow burden of a lump-sum purchase.</li>
<li><strong>Mortgage Alternative:</strong> Compared to a mortgage/secured loan, hire purchase can be simpler and faster to arrange, since the asset itself is generally sufficient security.</li>
</ol>

<h3>4.11 Financial Evaluation of Hire Purchase Finance</h3>
<p>Similar to leasing, hire purchase finance is evaluated from both the hirer's viewpoint (comparing the discounted cost of hire purchase against outright cash purchase or a bank loan, factoring in interest, tax shield on the interest component, and depreciation benefits) and the finance company's viewpoint (comparing the net cash inflow from interest/finance charges received against its cost of funds and administrative costs).</p>
"""
terms = [
    ("Hire Purchase Agreement", "A legal agreement where the owner lets goods out to a hirer for periodic payments, with an option/obligation to purchase at the end."),
    ("Hire Vendor", "The owner of goods let out on hire under a hire purchase agreement."),
    ("Hire Purchaser", "The person who takes possession and use of goods under hire purchase, gaining ownership upon final instalment."),
    ("Hypothecation", "A charge noted on an asset's registration (e.g. a vehicle's RC book) in favour of the financing company until the loan is repaid."),
]
examprep = [
    "Hire Purchase Act, 1972 (Sec. 4) requires: cash price, hire-purchase price, and date of commencement in every agreement.",
    "Ownership passes to the hirer ONLY on payment of the last instalment &mdash; this is the key distinction from leasing.",
    "Leasing vs Hire Purchase: Leasing = lessor keeps ownership + claims depreciation + full rental is deductible. Hire Purchase = hirer gets ownership eventually + hirer claims depreciation + only interest portion is deductible.",
    "Hire Purchase used more for smaller-value/consumer assets; Leasing more for larger assets.",
]
questions = [
    ("What is a hire purchase agreement? What must it contain as per the Hire Purchase Act, 1972?", "It is a legal agreement where the owner lets goods to a hirer for periodic payments with an option to purchase at the end. Under Section 4 of the Act, it must state the cash price of the goods, the hire-purchase price, and the date of commencement of the agreement."),
    ("Distinguish between leasing and hire purchase.", "In leasing, ownership stays with the lessor and the lessee never automatically owns the asset; the lessor claims depreciation and the full rental is tax-deductible. In hire purchase, ownership passes to the hirer upon the last instalment; the hirer claims depreciation, and only the interest portion of each instalment is tax-deductible."),
    ("Explain the advantages and disadvantages of hire purchase.", "Advantages: eases cash-flow pressure via instalments, and is often simpler to arrange than a mortgage/secured loan. Disadvantages: ownership (and financing flexibility) is delayed until the final instalment, there can be delays in obtaining clearance certificates, and effective interest costs can be higher than a standard bank loan."),
]
U.write(fname, U.page(fname, 4, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 4 done")

# ================= Topic 5: Underwriting =================
fname, title, prev_link, next_link = T(5)
overview = ("When a company issues shares or debentures to the public, underwriters guarantee that the issue "
            "will be subscribed. This topic covers what underwriting is, who can do it, its forms, and its "
            "advantages and disadvantages.")
notes = """
<h3>5.1 Meaning of Underwriting</h3>
<p>Underwriting is the agreement between the company and the underwriter, in which the latter agrees to subscribe the underwriter's guarantee to the company. An underwriter may be a person, firm, or institution engaged in guaranteeing that the shares/debentures offered by an issuing company will be subscribed to, in the event the public subscription falls short of the required amount.</p>

<h3>5.2 Conditions for Registration</h3>
<p>Following are the conditions for registration as an underwriter with SEBI:</p>
<ol>
<li>The underwriter may be a person or a firm required to obtain a certificate of registration from SEBI. However, if separate underwriting activity is done by an institution, that institution is already registered with SEBI in another category, they are exempted in certain cases.</li>
<li>The underwriter should have adequate infrastructure to perform the various functions of an underwriter, i.e. no lack of resources or infrastructure to fulfil obligations.</li>
<li>The underwriter should possess the necessary human resources with relevant experience in the securities market.</li>
<li>The applicant should not have been refused a certificate by SEBI (previously) and should not be involved in any pending legal/regulatory proceeding related to securities market violations.</li>
</ol>

<h3>5.3 Forms of Underwriting</h3>
<table class="compare">
<tr><th>Form</th><th>Description</th></tr>
<tr><td><strong>Full Underwriting</strong></td><td>Under this type of underwriting contract, the underwriter agrees to underwrite the whole issue, guaranteeing 100% of the shares/debentures offered will be subscribed.</td></tr>
<tr><td><strong>Partial Underwriting</strong></td><td>Under this type, the underwriter agrees to underwrite only a part of the issue, with the company (or other underwriters) bearing the risk for the remainder.</td></tr>
<tr><td><strong>Joint Underwriting</strong></td><td>Under this type, when the issue amount is very large, two or more underwriters jointly underwrite the issue, sharing the risk between them.</td></tr>
<tr><td><strong>Sub-Underwriting</strong></td><td>Under this type, the underwriter who has taken up the underwriting contract with the issuing company gets a part of the issue further underwritten by other sub-underwriters, distributing the risk further.</td></tr>
<tr><td><strong>Syndicate Underwriting</strong></td><td>Where the issue size is so large that a single underwriter cannot bear the entire risk, several underwriters come together (a syndicate) to jointly underwrite the issue.</td></tr>
</table>

<h3>5.4 Benefits of Underwriters</h3>
<ol>
<li>The underwriter has the right to appoint their own nominee to the board of the company for the purpose of protecting their interests until the shares/debentures underwritten are sold in the market.</li>
<li>The underwriting commission earned provides a source of income to the underwriter for the service and risk undertaken.</li>
<li>Underwriting also allows underwriters (particularly institutions) to build strategic relationships with issuing companies for future business.</li>
</ol>

<h3>5.5 Disadvantages of Underwriting</h3>
<ol>
<li><strong>Future Liability:</strong> An underwriter takes on a future contingent liability to subscribe to unsold shares/debentures if the public issue is undersubscribed, which can result in an unplanned, large cash outflow.</li>
<li><strong>Difficulty in Re-Sale:</strong> If the underwriter ends up holding a large quantum of unsold shares (due to being called upon to fulfil the underwriting commitment), it may be difficult to resell these shares in the market at a favourable price.</li>
<li><strong>Higher Investment Locked Down:</strong> A substantial amount of the underwriter's own funds may get tied up in shares taken up under the underwriting obligation, reducing liquidity.</li>
</ol>
"""
terms = [
    ("Underwriting", "An agreement where an underwriter guarantees to subscribe to unsold shares/debentures of a company's issue, for a commission."),
    ("Full Underwriting", "An underwriting contract covering 100% of an issue."),
    ("Partial Underwriting", "An underwriting contract covering only part of an issue."),
    ("Syndicate Underwriting", "Multiple underwriters jointly underwriting a very large issue to share the risk."),
]
examprep = [
    "Underwriting = an underwriter guarantees to subscribe to any unsold portion of a company's share/debenture issue, for a commission.",
    "SEBI registration conditions: adequate infrastructure, relevant human resources/experience, no prior refusal or pending violations.",
    "Forms: Full, Partial, Joint, Sub-Underwriting, Syndicate Underwriting.",
    "Underwriter benefits: board nominee right (to protect interest), underwriting commission income, strategic relationships.",
    "Underwriter risks: future contingent liability to buy unsold shares, difficulty reselling them, funds tied up.",
]
questions = [
    ("What is underwriting? Explain the conditions for registration as an underwriter with SEBI.", "Underwriting is an agreement where an underwriter guarantees to subscribe to any shares/debentures of an issue left unsold by the public, for a commission. To register with SEBI, the underwriter needs adequate infrastructure, relevant experienced human resources, and a clean regulatory record with no prior refusal or pending securities-law proceedings."),
    ("Explain the different forms of underwriting.", "Full Underwriting (100% of the issue), Partial Underwriting (only part of the issue), Joint Underwriting (two or more underwriters sharing a large issue), Sub-Underwriting (the primary underwriter passes part of the risk to sub-underwriters), and Syndicate Underwriting (a group of underwriters for very large issues)."),
    ("What are the disadvantages of underwriting to the underwriter?", "The underwriter takes on a contingent future liability to buy unsold shares if the issue is undersubscribed, may find it difficult to resell a large resulting shareholding at a good price, and can end up with a substantial amount of their own funds tied up in the underwritten shares."),
]
U.write(fname, U.page(fname, 5, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 5 done")

# ================= Topic 6: Mutual Funds - Concept, Structure & Types =================
fname, title, prev_link, next_link = T(6)
overview = ("Mutual funds pool money from many small investors to invest in a diversified portfolio, managed "
            "by a professional fund manager. This topic covers the concept, how a fund is structured, and the "
            "open-ended versus close-ended distinction.")
notes = """
<h3>6.1 Concept of Mutual Funds</h3>
<p>A mutual fund is a pool of money collected by a fund manager, representing the investors who have put in that money. The profits earned by a mutual fund are distributed among the individual investors, in the ratio of their level of investment, after deducting the applicable expenses, in the form of Net Asset Value (NAV). The NAV is calculated on a day-to-day basis by dividing the total net value of the fund by the number of outstanding units on that day.</p>

<h3>6.2 Objectives of Mutual Funds</h3>
<p>According to Weston J. Fred and Brigham Eugene F.: mutual funds are "Corporations which accept dollars from savers and then use these dollars to buy stocks, long-term bonds, short-term debt instruments issued by business or government units; these corporations pool funds and thus reduce risk by diversification."</p>
<ol>
<li><strong>Diversification:</strong> The significance of diversification is that it helps in reducing the overall risk taken by an investor, and also to help build a well-diversified portfolio of securities across companies and sectors.</li>
<li><strong>Growth of the Investor's Wealth:</strong> Over the long term, professional management and diversification are likely to lead to superior, more consistent returns compared to individual stock-picking, negatively or positively, suggests the growth potential for old and new investors.</li>
</ol>

<h3>6.3 Structure of Mutual Funds</h3>
<p>In India, the structure of mutual funds is governed by SEBI (Mutual Funds) Regulations, 1996, and involves the following parties:</p>
<ol>
<li><strong>Sponsor:</strong> The sponsor refers to the corporate body which is involved in the introduction of the mutual fund. Portfolio of the fund which has good market reputation and is working for more than 5 years.</li>
<li><strong>The Mutual Fund (Trust):</strong> The mutual fund itself is set up as a trust, according to the Indian Trusts Act, 1882, with the sponsor as its settlor. The Trustees hold the property (scripts) of the mutual fund for the benefit of the unit-holders.</li>
<li><strong>Trustees:</strong> The trustees need to be independent of the mutual fund and should keep the control of the securities which are bought by the different schemes. They should also take up the annual report to be submitted to SEBI.</li>
<li><strong>Asset Management Company (AMC):</strong> The AMC is the entity that is involved in the day-to-day management of the mutual fund. It manages funds of the various schemes and makes the investment decisions, but is not the owner of the fund's assets (the trustees hold those on behalf of unit-holders).</li>
<li><strong>Custodian:</strong> The custodian keeps custody of the securities of various schemes of the mutual fund, and also participates in any corporate action affecting those securities on behalf of the fund. The custodian should be registered with SEBI and cannot act as a sponsor of the same mutual fund.</li>
</ol>

<h3>6.4 Classification of Mutual Funds &mdash; Open-Ended vs Close-Ended</h3>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Open-Ended Schemes</h4>
<p>Mutual fund units under an open-ended scheme are available for subscription and repurchase on a continuous basis, at any time, at a price linked to the current NAV.</p>
<p><strong>Advantages:</strong> Liquidity (investors can enter/exit any time at current NAV), no fixed maturity, invested in and out over the fund's lifetime, redemption is always available.</p>
<p><strong>Disadvantages:</strong> Loss of the ability to hold within the fund manager's discretion for as long as they may prefer, since ongoing redemption pressure may force the sale of good securities to raise cash for redemptions.</p>
<h4 style="margin:14px 0 6px;color:var(--accent-dark);font-size:0.98rem;">Close-Ended Schemes</h4>
<p>Close-ended schemes have a stipulated maturity period (e.g. 3-15 years); investors can only invest during the initial launch (New Fund Offer, NFO) period, and thereafter the fund is closed for new subscriptions.</p>
<p><strong>Advantages:</strong> The fund manager can freely invest for the full defined term without redemption pressure, potentially achieving better yields; units of a close-ended fund are listed on a stock exchange, giving investors liquidity through secondary market trading (buying/selling among investors) even though the fund itself doesn't redeem before maturity.</p>
<p><strong>Disadvantages:</strong> Since units are traded on the secondary market rather than redeemed directly with the fund, their market price can diverge significantly from NAV (usually trading at a discount), and liquidity in the secondary market can be limited/thin.</p>

<h3>6.5 Difference between Open-Ended and Close-Ended Schemes</h3>
<table class="compare">
<tr><th>Basis of Difference</th><th>Open-Ended Fund</th><th>Close-Ended Fund</th></tr>
<tr><td>Maturity Period</td><td>No fixed maturity period</td><td>Fixed maturity period</td></tr>
<tr><td>Subscription/Withdrawal</td><td>Available continuously at current NAV</td><td>Available only during the NFO; fund is closed thereafter</td></tr>
<tr><td>Listing on Stock Exchange</td><td>Generally not listed (except a few)</td><td>Units are generally listed on a stock exchange</td></tr>
<tr><td>Price Determination</td><td>Priced strictly at NAV</td><td>Traded at market price, which can differ from NAV</td></tr>
<tr><td>Liquidity</td><td>High &mdash; redeem with the fund any time</td><td>Depends on secondary market trading volume</td></tr>
</table>

<h3>6.6 Broad Classification of Mutual Fund Schemes</h3>
<p>Various sub-categories of mutual funds are classified as follows:</p>
<ul>
<li><strong>Equity Funds:</strong> Growth Funds (aggressive, high-risk high-reward), Diversified Equity Funds (invest broadly across sectors), Sector-Specific Funds, Index Funds (tracking a market index), Tax-Saving Funds/ELSS (offering tax deduction under Section 80C, with a mandatory lock-in period).</li>
<li><strong>Debt/Income Funds:</strong> Focus on generating regular income by investing in fixed-income instruments (bonds, debentures, government securities).</li>
<li><strong>Balanced/Hybrid Funds:</strong> Invest in a mix of equity and debt instruments, balancing growth potential with income stability.</li>
<li><strong>Money Market/Liquid Funds:</strong> Invest in short-term money market instruments, offering high liquidity and low risk.</li>
</ul>
"""
terms = [
    ("Mutual Fund", "A pooled investment vehicle collecting money from many investors to invest in a diversified portfolio, managed by a professional fund manager."),
    ("Net Asset Value (NAV)", "The per-unit value of a mutual fund, calculated as total net fund value divided by outstanding units."),
    ("Sponsor", "The corporate entity that establishes a mutual fund."),
    ("Asset Management Company (AMC)", "The entity responsible for the day-to-day investment management of a mutual fund's schemes."),
    ("Custodian", "The entity holding physical/electronic custody of a mutual fund's securities on the fund's behalf."),
    ("Open-Ended Scheme", "A mutual fund scheme open for subscription/redemption continuously, with no fixed maturity."),
    ("Close-Ended Scheme", "A mutual fund scheme with a fixed maturity period, open for subscription only during its initial launch (NFO)."),
]
examprep = [
    "Mutual fund structure: Sponsor &rarr; Trust (the fund itself) &rarr; Trustees (oversight) &rarr; AMC (day-to-day management) &rarr; Custodian (holds securities).",
    "NAV = total net asset value of the fund / number of outstanding units.",
    "Open-Ended: no maturity, continuous subscription/redemption at NAV, high liquidity. Close-Ended: fixed maturity, subscription only during NFO, listed on exchange, trades at market price (often at a discount to NAV).",
    "Broad categories: Equity Funds (Growth/Diversified/Sector/Index/ELSS), Debt/Income Funds, Balanced/Hybrid Funds, Money Market/Liquid Funds.",
]
questions = [
    ("Explain the structure of a mutual fund in India.", "A Sponsor establishes the fund as a Trust under the Indian Trusts Act, 1882. Trustees hold the fund's securities for unit-holders and oversee compliance. The Asset Management Company (AMC) handles day-to-day investment decisions, while a SEBI-registered Custodian holds the fund's securities in safekeeping."),
    ("Distinguish between open-ended and close-ended mutual fund schemes.", "Open-ended schemes have no fixed maturity and allow continuous subscription/redemption at NAV, offering high liquidity. Close-ended schemes have a fixed maturity period, accept subscriptions only during their initial NFO, and are listed on a stock exchange where units trade at market price (often at a discount to NAV) rather than being redeemed directly with the fund."),
    ("What is NAV? How is it calculated?", "Net Asset Value is the per-unit value of a mutual fund scheme, calculated by dividing the total net value of the fund's assets (minus liabilities) by the number of outstanding units, computed on a day-to-day basis."),
]
U.write(fname, U.page(fname, 6, title, overview, notes, terms, examprep, questions, prev_link, next_link))
print("Topic 6 done")

# ================= Topic 7: Mutual Funds - Classification, Advantages & Disadvantages =================
fname, title, prev_link, next_link = T(7)
overview = ("Unit 4 closes with a deeper look at the many specialised categories of mutual funds available to "
            "investors today, and a weighing-up of what mutual fund investing offers and where it falls short.")
notes = """
<h3>7.1 Equity Fund Sub-Categories</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Growth Funds</strong></td><td>Aggressive funds investing primarily for capital appreciation, characterised by higher risk in exchange for potentially higher long-term returns.</td></tr>
<tr><td><strong>Diversified Equity Funds</strong></td><td>Invest across a broad spread of sectors/companies to reduce concentration risk, rather than betting on a single sector.</td></tr>
<tr><td><strong>Equity Income/Dividend Yield Funds</strong></td><td>Focus on stocks with a consistent history of paying dividends, aiming for steady income alongside moderate growth.</td></tr>
<tr><td><strong>Sector Funds</strong></td><td>Invest in a particular sector (e.g. IT, banking, pharma), carrying higher risk since performance is concentrated in one industry.</td></tr>
<tr><td><strong>Index Funds</strong></td><td>Track a specific market index (e.g. Nifty, Sensex) by holding the same securities in the same proportion &mdash; a passive investment strategy with typically lower fees.</td></tr>
<tr><td><strong>Value Funds</strong></td><td>Invest in stocks believed to be undervalued relative to their fundamentals, aiming to profit as the market corrects the mispricing.</td></tr>
<tr><td><strong>Tax-Saving Funds (ELSS)</strong></td><td>Equity-Linked Savings Schemes offering tax deduction under Section 80C, with a mandatory lock-in period (currently 3 years).</td></tr>
</table>

<h3>7.2 Debt/Income Fund Sub-Categories</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Income Funds</strong></td><td>Aim to provide a steady flow of income by investing in fixed-income instruments like bonds, debentures, and government securities.</td></tr>
<tr><td><strong>Liquid/Money Market Funds</strong></td><td>Invest in very short-term instruments (treasury bills, commercial paper, certificates of deposit), offering high liquidity and low risk, suited for parking surplus cash.</td></tr>
<tr><td><strong>Gilt Funds</strong></td><td>Invest exclusively in government securities, carrying no default (credit) risk, though still subject to interest-rate risk.</td></tr>
<tr><td><strong>Fixed Maturity Plans (FMPs)</strong></td><td>Close-ended debt funds with a defined maturity, investing in instruments maturing around the same time as the fund itself, reducing interest-rate risk.</td></tr>
</table>

<h3>7.3 Hybrid, Real Estate & Other Specialised Funds</h3>
<table class="compare">
<tr><th>Type</th><th>Description</th></tr>
<tr><td><strong>Balanced/Hybrid Funds</strong></td><td>Invest in a mix of equity and debt, aiming to balance growth with income stability.</td></tr>
<tr><td><strong>Exchange-Traded Funds (ETFs)</strong></td><td>Hybrid instruments that trade on a stock exchange like a share, typically tracking an index, commodity, or basket of assets, combining the diversification of a mutual fund with the tradability of a stock.</td></tr>
<tr><td><strong>Fund of Funds (FoFs)</strong></td><td>A mutual fund that invests in units of other mutual funds, rather than directly in securities, offering diversification across fund managers/strategies.</td></tr>
<tr><td><strong>Real Estate Funds</strong></td><td>Invest directly or indirectly in real estate assets/securities, offering exposure to property without directly owning physical real estate.</td></tr>
<tr><td><strong>Commodity Funds</strong></td><td>Invest in commodities (gold, agricultural products, metals, etc.) or commodity-linked instruments.</td></tr>
<tr><td><strong>Hedge Funds</strong></td><td>Actively-managed, typically for sophisticated investors, using diverse strategies (including leverage and derivatives) with the goal of generating positive returns in various market conditions.</td></tr>
</table>

<h3>7.4 Load, No-Load, Tax-Exempt & Tax-Non-Exempt Funds</h3>
<ul>
<li><strong>Load Funds:</strong> Charge a fee (entry load and/or exit load) when units are purchased or redeemed.</li>
<li><strong>No-Load Funds:</strong> Do not charge any load, so the entire invested amount goes toward purchasing fund units.</li>
<li><strong>Tax-Exempt Funds:</strong> Investment corpus qualifies for tax exemption/deduction (e.g. ELSS under Section 80C).</li>
<li><strong>Non-Tax-Exempt Funds:</strong> Most other mutual funds, where returns are taxed as per applicable capital gains/income tax rules.</li>
</ul>

<h3>7.5 Advantages/Merits of Mutual Funds</h3>
<ol>
<li><strong>Professional Management:</strong> Investors benefit from the expertise of professional fund managers who research and select securities on their behalf, saving individual investors the time and expertise required.</li>
<li><strong>Diversification:</strong> Even a small investment gets spread across a diversified portfolio of securities, reducing risk compared to holding a single stock.</li>
<li><strong>Convenience:</strong> Investing in a mutual fund is far more convenient than researching and directly managing a portfolio of individual stocks/bonds.</li>
<li><strong>Affordability:</strong> Due to the economies of scale of pooling many investors' money, mutual funds provide access to a diversified portfolio at a relatively low cost/minimum investment.</li>
<li><strong>Liquidity:</strong> Open-ended mutual fund units can be readily converted into cash at their current NAV, providing high liquidity.</li>
<li><strong>Flexibility:</strong> Investors can choose from a wide range of schemes (equity, debt, hybrid, sector, etc.) to match their own risk appetite and investment goals.</li>
<li><strong>Tax Benefits:</strong> Certain schemes (e.g. ELSS) offer tax deductions, and dividends/capital gains from mutual funds may be taxed favourably compared to some other instruments.</li>
</ol>

<h3>7.6 Disadvantages/Demerits of Mutual Funds</h3>
<ol>
<li><strong>No Guarantees:</strong> Like any market-linked investment, mutual fund returns are not guaranteed and depend on market performance.</li>
<li><strong>Fees and Expenses:</strong> Mutual funds charge management fees and other expenses (expense ratio) regardless of the fund's performance, which reduce net investor returns.</li>
<li><strong>Poor Trading/Execution:</strong> Since mutual fund transactions are processed once a day at the closing NAV, investors cannot react instantly to intraday market swings like a direct stock trader can.</li>
<li><strong>Loss of Control:</strong> Investors have no say in which specific securities the fund manager buys or sells within the fund's stated strategy.</li>
<li><strong>Dilution:</strong> A very diversified fund's gains from a few outstanding stocks may be diluted by the presence of many average-performing holdings.</li>
<li><strong>Cash/Liquidity Drag:</strong> Mutual funds often hold a portion of their corpus in cash to meet potential redemption requests, which can slightly drag down overall returns compared to being fully invested.</li>
</ol>
"""
terms = [
    ("Index Fund", "A passive mutual fund that replicates a specific market index."),
    ("Exchange-Traded Fund (ETF)", "A fund that trades on a stock exchange like a share, typically tracking an index or asset basket."),
    ("Fund of Funds (FoF)", "A mutual fund that invests in units of other mutual funds rather than directly in securities."),
    ("Expense Ratio", "The annual fee (as a percentage of assets) a mutual fund charges investors for management and operating costs."),
    ("Load Fund", "A mutual fund that charges a fee on purchase (entry load) or redemption (exit load) of units."),
]
examprep = [
    "Equity fund types: Growth, Diversified, Dividend Yield, Sector, Index, Value, ELSS (tax-saving).",
    "Debt fund types: Income Funds, Liquid/Money Market Funds, Gilt Funds, Fixed Maturity Plans.",
    "Other types: Balanced/Hybrid, ETFs, Fund of Funds, Real Estate Funds, Commodity Funds, Hedge Funds.",
    "Load vs No-Load Funds; Tax-Exempt (e.g. ELSS) vs Non-Tax-Exempt Funds.",
    "Advantages: professional management, diversification, convenience, affordability, liquidity, flexibility, tax benefits.",
    "Disadvantages: no guaranteed returns, fees/expense ratio, no intraday trading (NAV-based, once-daily pricing), no investor control over holdings, dilution, cash drag.",
]
questions = [
    ("Explain the different types of equity mutual funds.", "Growth Funds (aggressive capital appreciation), Diversified Equity Funds (spread across sectors), Dividend Yield Funds (consistent dividend payers), Sector Funds (single-industry focus), Index Funds (passively tracking an index), Value Funds (undervalued stocks), and ELSS/Tax-Saving Funds (Section 80C benefit with lock-in)."),
    ("What is an ETF? How does it differ from a regular mutual fund?", "An Exchange-Traded Fund is a fund that trades on a stock exchange like a share, typically tracking an index or basket of assets. Unlike a regular open-ended mutual fund (bought/sold at end-of-day NAV through the AMC), ETF units can be bought and sold throughout the trading day at real-time market prices."),
    ("Discuss the advantages and disadvantages of investing in mutual funds.", "Advantages include professional management, diversification even for small investments, convenience, affordability, liquidity, flexibility of scheme choice, and tax benefits on certain schemes. Disadvantages include no guaranteed returns, management fees/expense ratios, inability to trade intraday (priced once daily at NAV), lack of investor control over specific holdings, and a potential cash drag on returns."),
]
U.write(fname, U.page(fname, 7, title, overview, notes, terms, examprep, questions, prev_link, next_link))

U.write_index("Seven topics covering asset-based financial services: NBFCs, Leasing (concepts, types, and financial evaluation), Hire Purchase, Underwriting, and Mutual Funds (concept/structure/types and classification/advantages/disadvantages).")

print("Unit 4 (Banking & Financial Services) complete: all 7 topics + index written.")
