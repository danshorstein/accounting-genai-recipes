---
id: <auto>
title: "Accounts Payable Register Multiline Extract"
category: "reporting"
level: "intermediate"
estimated_time: "30-45 minutes"
tools:
  - OpenAI Codex (or similar coding agent)
  - "Python 3.8+ with pandas + pypdf"
inputs:
  - "Accounts Payable register PDF exported from the ERP (one or more pages)"
  - "Chart-of-accounts or appropriation mapping (optional, for validation)"
  - "PDF layout description (column order, multi-line wrapping behavior)"
outputs:
  - "Python parser script (parse_accounts_payable_register.py)"
  - "Pandas DataFrame with one record per AP voucher, including multi-line fields"
  - "Optional CSV extract for downstream reconciliation or analytics"
video_url: https://youtu.be/WmxZQpUWhLY
tags: [accounts-payable, pdf, data-extraction]
license: CC-BY-4.0
---

## Problem
Finance teams often receive Accounts Payable registers as PDF reports that wrap key fields such as appropriation descriptions and memo details across multiple lines. Copying these into spreadsheets is error-prone, breaks multi-line context, and makes downstream analytics impossible without extensive manual cleanup. Building a custom parser from scratch requires Python expertise and hours of debugging PDF layout quirks. The challenge is to quickly generate a reliable parser tailored to your specific AP register format without manual coding.

## Solution (at a glance)
1. Use OpenAI Codex (or another coding agent) to generate a custom Python parser for your AP register PDF format.
2. Provide the agent with a sample PDF page and describe the column layout and multi-line wrapping behavior.
3. The agent builds a parser script that reads the PDF, collapses multi-line appropriation and description fields, and emits structured rows.
4. Run the generated script to extract data, review the DataFrame (or CSV) output, and reconcile totals with the source register.
5. Re-use the parser monthly; ask the agent to update it if the PDF layout changes.

## Prompt
```text
I need you to build a Python parser for my Accounts Payable register PDF. The PDF has multi-line fields that need to be collapsed into single records.

CONTEXT:
- I receive monthly AP register PDFs from my ERP system
- Key fields wrap across multiple lines (appropriation descriptions, memo details)
- I need a clean DataFrame or CSV with one row per AP voucher
- This will be used for reconciliation, analytics, and GL validation

PDF LAYOUT:
[Describe your specific format, or use this example:]
- Headers end at the row labelled "PO #"
- Columns: Date Filed → APV Number → Payee → Appropriation → Amount → Check Number → Description (multi-line) → Check Date → Appropriation Code → PO # (optional)
- Multi-line fields: Appropriation and Description can span 2-5 lines

REQUIREMENTS:
1. Read PDF text using Python (pandas + pypdf or similar)
2. Identify record boundaries (detect when a new voucher starts)
3. Collapse multi-line appropriation and description fields into single strings
4. Output a DataFrame with columns: date_filed, apv_number, payee, appropriation, amount, check_number, description, check_date, appropriation_code, po_number
5. Convert amount strings to float, dates to datetime64
6. Provide a CLI interface with optional `--csv` flag for file export
7. Include error handling for malformed rows or missing fields

DELIVERABLES:
- Parser script: `parse_accounts_payable_register.py`
- Function: `parse_accounts_payable_register(pdf_path) -> pd.DataFrame`
- CLI: `python parse_accounts_payable_register.py <pdf_path> [--csv output.csv]`
- Basic validation: sum amounts, count records, flag parsing errors
- README section: how to run, expected format, troubleshooting

CONSTRAINTS:
- Python 3.8+ with minimal dependencies (pandas, pypdf or pdfplumber)
- Must work in a virtual environment
- No external APIs (all processing local)
- Handle PDFs with 1-50 pages

Please ask me questions about:
- My specific PDF layout (I can share a sample page or describe the format)
- Which fields are most important for my use case
- Any special formatting rules (date formats, currency symbols, etc.)
- Validation rules (totals, required fields, etc.)

Then build the parser step-by-step, explaining your approach before coding.
```

## Guardrails
- Treat AP registers as confidential; store PDFs and extracts on secured drives with least-privilege access.
- Run the parser on your local machine; never upload AP data to external services or cloud APIs.
- Validate parsed totals against the PDF grand total before posting or approving payments.
- Flag any rows where dates or amounts fail to parse; escalate to AP management before using the data.
- If the PDF layout changes, review the updated parser logic with a teammate before deploying to production workflows.
- The coding agent generates code based on your PDF description; review generated code for accuracy and security before running on live data.

## Implementation Notes (optional)
- The coding agent will generate: `parse_accounts_payable_register.py` with a function `parse_accounts_payable_register(pdf_path)` and CLI support with `--csv` flag.
- Create a virtual environment: `python -m venv .venv` and activate with `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows).
- Install dependencies: `pip install pandas pypdf` (or pdfplumber, depending on what the agent chooses).
- The generated script should convert amount strings to floats and coerce date strings into `datetime64` columns for easier filtering or joins.
- Run with: `python parse_accounts_payable_register.py path/to/register.pdf --csv output.csv`

## Evaluation & Handoff (optional)
- Spot-check at least three vouchers with wrapped descriptions to confirm they render correctly in the DataFrame/CSV.
- Reconcile the sum of `amount` against the PDF grand total and your GL upload template.
- Share the CSV or DataFrame snapshot with FP&A or procurement teams that rely on spend analytics.

## Checklist
- [ ] Coding agent generated parser script with all required functionality
- [ ] Sample AP register parsed end-to-end with multi-line fields intact
- [ ] Amount totals reconciled to the PDF grand total
- [ ] DataFrame/CSV output reviewed for accuracy (spot-check 3+ vouchers)
- [ ] Parser tested with edge cases (multi-page PDFs, missing PO numbers, long descriptions)
- [ ] Script integrated into monthly AP close workflow
- [ ] Prompt customized with organization-specific PDF layout and field names
