# GenAI Accounting Recipes

A public, community-friendly collection of **practical GenAI recipes for accountants**—companion repo to the forthcoming book.

- **Audience:** accountants, auditors, controllers, FP&A, and finance ops
- **Format:** each recipe includes a one-page overview, inputs/outputs, prompts, code (optional), and a short demo video
- **Licensing:** code is MIT; written content (recipes, docs) are CC BY 4.0

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
