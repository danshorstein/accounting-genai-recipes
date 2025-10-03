---
id: <auto>
title: "Rule-Based Expense Analysis Tool"
category: "bookkeeping"
level: "intermediate"
estimated_time: "30-60 minutes"
tools:
  - Claude Code (or similar coding agent)
  - "Python 3.8+ with Flask, pandas, openpyxl, matplotlib, pytest"
inputs:
  - "Expense register (CSV or Excel) with columns: date, description/merchant, amount"
  - "Monthly budget by category (optional, for reconciliation)"
  - "Organization-specific rules, categories, and thresholds (or use defaults)"
outputs:
  - "Python web application with drag-and-drop file upload interface"
  - "Categorized expense data with transparent rule-based matching"
  - "Excel workbook with summary, transactions, category analysis, and flagged items"
  - "PDF summary report with visualizations"
  - "Monthly procedure document for recurring workflow"
video_url: https://youtu.be/l1d8MIBuf4c
tags: [bookkeeping, expense-analysis, automation, internal-audit]
license: CC-BY-4.0
---

## Problem
Accountants and bookkeepers process hundreds of expense transactions monthly, requiring manual categorization, policy compliance checks, and budget reconciliation. Existing solutions either use black-box machine learning (reducing auditability) or require extensive manual work. Teams need a transparent, rule-based system that automates categorization while maintaining full visibility into why each transaction was classified—and the flexibility to customize rules for their specific vendors and chart of accounts.

## Solution (at a glance)
1. Use Claude Code (or another coding agent) to generate a production-ready Python web application tailored to your organization's expense categories, compliance rules, and reporting needs.
2. The agent builds a Flask-based tool with rule-based pattern matching (regex), compliance flagging, budget reconciliation, and multi-format reporting—no machine learning, fully auditable.
3. Run the application locally, upload expense files via drag-and-drop, review categorizations and flags, and download Excel/PDF reports.
4. Customize merchant rules and thresholds as needed; run monthly as part of your close process.

## Prompt
```text
I need you to build a production-ready expense analysis web application. This is a real business tool for accountants, not a tutorial project.

AUDIENCE & SCALE:
- Python-savvy accountants and bookkeepers
- 50-500 expense transactions per month
- Transparent, auditable categorization required (NO black-box ML)
- Accuracy valued over full automation

CORE FEATURES:

1. EXPENSE CATEGORIZATION
   - Rule-based pattern matching (regex) against merchant names
   - Categories: [Ask me for my chart of accounts categories, or use: Travel, Meals & Entertainment, Office Supplies, Software & Subscriptions, Professional Services, Marketing, Utilities, Insurance, Equipment, Other]
   - Show users exactly why each transaction was categorized
   - Easy to add custom rules for specific merchants

2. COMPLIANCE FLAGS
   - Large transactions (ask my threshold, default >$5,000)
   - Capital expense threshold (ask my policy, default >$2,500 for equipment/furniture)
   - Duplicate detection (same merchant, amount, within 3 days)
   - Weekend spending patterns (>10% of transactions)
   - Uncategorized items requiring manual review

3. BUDGET RECONCILIATION (optional)
   - Compare actual vs budget by category
   - Calculate variances
   - Tax-aware features (50% meal deduction, etc.)
   - Journal entry suggestions

4. REPORTING
   - Excel workbook: summary stats, transactions, category analysis (pivot tables), monthly timeline, flagged items
   - Charts: pie (categories), bar (amounts over time)
   - PDF summary with visualizations
   - Professional formatting

5. WEB INTERFACE
   - Modern, clean design with card-based layout
   - Drag-and-drop file upload (CSV/Excel)
   - Real-time results display
   - Download buttons for reports
   - Mobile-responsive

6. DATA HANDLING
   - Support CSV and Excel (.xlsx, .xls)
   - Handle common column name variations (date/transaction_date, description/merchant, amount/total)
   - Validate data, handle missing values gracefully
   - File size limit: 16MB
   - Security: sanitize filenames, whitelist extensions

7. TESTING & QUALITY
   - Pytest test suite covering categorization, flags, financial calculations, edge cases
   - Type hints, error handling, PEP 8 compliance
   - Separation of concerns (routing, business logic, reporting)

TECHNICAL STACK:
- Backend: Python 3.8+, Flask
- Data: pandas, numpy
- Reporting: openpyxl, matplotlib
- Testing: pytest
- Frontend: HTML5, vanilla JavaScript, CSS3

DELIVERABLES:
1. Flask app (app.py) with REST endpoints
2. Core analysis engine (expense_analyzer.py)
3. Report generator (report_generator.py)
4. Test suite (test_expense_analyzer.py)
5. Web interface (HTML/CSS/JS in templates/)
6. Sample expense data (50 realistic transactions, 2-3 months, $35-50k total)
7. requirements.txt
8. README with quick start, demo script, extension ideas
9. Monthly procedure document (customized to my organization)

CONSTRAINTS:
- Must be rule-based (no ML/neural networks)
- All processing local (no external APIs)
- No database, authentication, or deployment configs
- File-based, single-user demo app
- <10 package dependencies
- Setup time <5 minutes
- Works offline (after pip install)

WHAT I VALUE:
- Code comments explain "why" not "what"
- Clear variable names (readability over brevity)
- Helpful error messages (non-technical)
- Precision and transparency (this is for accountants)

Please ask me questions about:
- My expense categories and chart of accounts structure
- Compliance thresholds and policies specific to my organization
- Any special merchant rules or patterns I need
- Reporting preferences and downstream systems
- Whether I need budget reconciliation features

Then build step-by-step:
1. Plan architecture and confirm approach
2. Build core analysis engine with tests
3. Add Flask web app
4. Create reporting functionality
5. Build web interface
6. Generate sample data
7. Write documentation and procedure doc
```

## Guardrails
- Process all expense data locally; never upload to external services or cloud APIs.
- All categorizations are suggestions—always review flagged transactions and large amounts before posting to the general ledger.
- Consult your tax advisor for meal deduction percentages and capitalization thresholds applicable in your jurisdiction.
- Test the tool with sample data before using it on live expense files.
- The coding agent generates code based on your inputs; review generated code for security and compliance before running in production.
- This tool supports internal analysis and bookkeeping; any compliance or tax reporting relying on categorizations must be reviewed by a qualified accountant.

## Implementation Notes (optional)
- The coding agent will generate a complete file structure: `app.py`, `expense_analyzer.py`, `report_generator.py`, `test_expense_analyzer.py`, `templates/index.html`, `static/style.css`, `requirements.txt`, and sample data.
- Standard dependencies: `flask`, `pandas`, `openpyxl`, `matplotlib`, `pytest` (agent may suggest additional libraries based on your requirements).
- Activate the virtual environment with `source .venv/bin/activate` (or `.venv\Scripts\activate` on Windows) before running `pip install -r requirements.txt`.
- Run the app with `python app.py` and navigate to `http://localhost:5000` in your browser.
- To customize merchant rules, edit the regex patterns in `expense_analyzer.py` (the agent should make this section clearly documented).
- The generated procedure document will outline the monthly workflow: export expenses → upload to tool → review flags → download reports → post adjustments to GL.

## Evaluation & Handoff (optional)
- Test with sample data first: verify categorizations, check that all flags trigger correctly, and confirm report formats.
- Reconcile category totals in the Excel output against your source system (QuickBooks, Xero, NetSuite, etc.).
- Spot-check at least 10 categorized transactions to confirm rule logic is accurate.
- Review the generated procedure document with your team and adjust for your specific close process.
- Share Excel reports with FP&A, department managers, or auditors as needed.

## Checklist
- [ ] Claude Code (or coding agent) generated full application with all deliverables
- [ ] Sample expense data processed end-to-end with accurate categorizations
- [ ] All compliance flags working (large amounts, duplicates, capitalization, weekend patterns)
- [ ] Excel and PDF reports generated successfully with charts and formatting
- [ ] All tests passing (18+ tests covering edge cases)
- [ ] Custom merchant rules added for your key vendors
- [ ] Monthly procedure document customized to your organization
- [ ] Demo completed with team or stakeholders (using video as reference)
