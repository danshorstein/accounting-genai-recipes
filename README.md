# GenAI Accounting Recipes

A public, community-friendly collection of **practical GenAI recipes for accountants**—companion repo to the forthcoming book.

- **Audience:** accountants, auditors, controllers, FP&A, and finance ops
- **Format:** each recipe includes a one-page overview, inputs/outputs, prompts, code (optional), and a short demo video
- **Licensing:** code is MIT; written content (recipes, docs) are CC BY 4.0

## Published Recipes

### 01. [Third-Party SOC 2 Review Assistant](recipes/01-soc2-review-assistant/recipe.md)
**Category:** Audit | **Level:** Intermediate | **Time:** 45-60 minutes

Automate the review of SOC 2 Type 2 reports for third-party service providers. Use a custom GPT to extract control gaps, generate client questions for user entity controls, and produce risk memos—saving hours of manual report analysis while maintaining audit quality.

[📺 Watch Demo](https://youtu.be/w9rqjeFXxSY)

---

### 02. [Accounts Payable Register Multiline Extract](recipes/02-AP-multiline-file-extract/recipe.md)
**Category:** Reporting | **Level:** Intermediate | **Time:** 30-45 minutes

Use a coding agent (OpenAI Codex or similar) to generate a custom Python parser that extracts AP voucher data from PDF registers with multi-line fields. Converts semi-structured PDF output into clean DataFrames or CSV files for reconciliation and analytics.

[📺 Watch Demo](https://youtu.be/WmxZQpUWhLY)

---

### 03. [Rule-Based Expense Analysis Tool](recipes/03-expense-categorization-tool/recipe.md)
**Category:** Bookkeeping | **Level:** Intermediate | **Time:** 30-60 minutes

Use Claude Code (or similar coding agent) to build a production-ready Python web application for transparent, auditable expense categorization. Features rule-based pattern matching, compliance flags, budget reconciliation, and multi-format reporting—no black-box ML.

[📺 Watch Demo](https://youtu.be/l1d8MIBuf4c)

## Quick Start

1. Clone:
   ```bash
   git clone https://github.com/<your-username>/genai-accounting-recipes.git
   cd genai-accounting-recipes
   ```
2. Create a new recipe from the template:
   ```bash
   bash templates/new_recipe.sh "03-bank-reconciliation"
   ```
3. Edit the `recipe.md` and add your assets in the new folder.
4. (Optional) Add code or a notebook under `code/`.
5. Record a short walkthrough video (2–5 min). Upload to YouTube (unlisted) and paste the link in the recipe.
6. Commit and push:
   ```bash
   git add .
   git commit -m "Add 03-bank-reconciliation recipe"
   git push origin main
   ```

## Docs Site

This repository is configured to publish a searchable docs site via **MkDocs** + GitHub Pages.
- Configure Pages under repo **Settings → Pages → Build and deployment → GitHub Actions**.
- On push to `main`, the site will build automatically.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Use Issues and Discussions for ideas and questions.
