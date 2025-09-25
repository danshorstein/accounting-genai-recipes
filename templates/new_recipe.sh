#!/usr/bin/env bash
set -euo pipefail
slug="$1"
dest="recipes/${slug}"
mkdir -p "$dest"
cp templates/recipe.md "$dest/recipe.md"
echo "Created $dest"
