---
id: <auto>
title: "Accounts Payable Register Multiline Extract"
category: "reporting"
level: "intermediate"
estimated_time: "30-45 minutes"
tools:
  - ChatGPT / GPT-5
  - "Python 3.13 (.venv) with pandas + pypdf"
inputs:
  - "Accounts Payable register PDF exported from the ERP (one or more pages)"
  - "Chart-of-accounts or appropriation mapping (optional, for validation)"
outputs:
  - "Pandas DataFrame with one record per AP voucher, including multi-line fields"
  - "Optional CSV extract for downstream reconciliation or analytics"
video_url: https://youtu.be/<your-demo>
tags: [accounts-payable, pdf, data-extraction]
license: CC-BY-4.0
---

## Problem
Finance teams often receive Accounts Payable registers as PDF reports that wrap key fields such as appropriation descriptions and memo details across multiple lines. Copying these into spreadsheets is error-prone, breaks multi-line context, and makes downstream analytics impossible without extensive manual cleanup. The challenge is to convert semi-structured PDF output into a reliable tabular dataset while preserving long descriptions and appropriation narratives.

## Solution (at a glance)
1. Ask GenAI to inspect a sample register page and confirm the column order and wrapping behavior.
2. Use the provided Python parser to read the PDF, collapse multi-line appropriation and description fields, and emit structured rows.
3. Review the resulting DataFrame (or CSV) to confirm totals, spot-check multi-line joins, and reconcile with the source register.
4. Re-run the workflow whenever a new PDF is generated, updating the parser only if the layout meaningfully changes.

## Prompt
```text
You are "AP Register Parser" helping extract voucher data from a multi-line Accounts Payable PDF.

Context:
- The PDF follows the city register format with headers ending at the row labelled "PO #".
- Use Python with pandas and pypdf inside my `.venv` environment.
- Existing helper lives at `recipes/02-AP-multiline-file-extract/parse_accounts_payable_register.py` and already handles multi-line appropriation and description blocks.

When I provide a new PDF path:
1. Inspect the first page text to verify the header structure and whether the columns still match the expected pattern (date filed → APV number → payee → appropriation → amount → check number → description lines → check date → appropriation code → optional PO lines).
2. If the layout matches, show me the exact command to run the parser and advise on optional `--csv` output.
3. If the layout has changed, draft the updated parsing logic (reusing as much of the helper as possible) and explain the adjustments before writing code.

Response format:
- Section A: Layout confirmation or required adjustments.
- Section B: Command(s) or updated code snippet.
- Section C: Post-run validation checklist (totals, spot checks, PO coverage).
```

## Guardrails
- Treat AP registers as confidential; store PDFs and extracts on secured drives with least-privilege access.
- Validate parsed totals against the PDF grand total before posting or approving payments.
- Flag any rows where dates or amounts fail to parse; escalate to AP management before using the data.
- If the PDF layout changes, review the updated logic with a teammate before deploying to production workflows.

## Implementation Notes (optional)
- Parser entry point: `recipes/02-AP-multiline-file-extract/parse_accounts_payable_register.py` exposes `parse_accounts_payable_register` and an optional `--csv` CLI flag.
- Activate the project environment with `source .venv/bin/activate` (or prefix commands with `.venv/bin/python`).
- The script converts amount strings to floats and coerces date strings into `datetime64` columns for easier filtering or joins.

## Evaluation & Handoff (optional)
- Spot-check at least three vouchers with wrapped descriptions to confirm they render correctly in the DataFrame/CSV.
- Reconcile the sum of `amount` against the PDF grand total and your GL upload template.
- Share the CSV or DataFrame snapshot with FP&A or procurement teams that rely on spend analytics.

## Checklist
- [ ] Sample AP register parsed end-to-end with multi-line fields intact
- [ ] Amount totals reconciled to the PDF grand total
- [ ] Parser reviewed or updated after any layout change
- [ ] Demo video link recorded and added
- [ ] Prompt customized with organization-specific terminology (optional)
