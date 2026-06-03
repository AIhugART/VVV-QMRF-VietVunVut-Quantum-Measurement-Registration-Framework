#!/usr/bin/env bash
# Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet
#
# build.sh — Atomic "build from source" for the paper_002 arXiv package.
#
# RCA (2026-06-03): the shipped PNGs/PDF are DERIVED artifacts. A prior session
# edited main.tex (v97 Bell-state fix, v99 theta-grid) but did NOT regenerate the
# figures or recompile the PDF, so both drifted silently. This script makes
# "regenerate figures -> recompile" a SINGLE atomic step that MUST be run before
# any submission, so the artifacts can never lag the source again.
#
# Usage (from anywhere):  bash build.sh
# Requires: python (matplotlib, numpy) + a LaTeX toolchain (latexmk/pdflatex).

set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
FIGSCRIPT="$HERE/../../supplemental/regenerate_figures.py"

echo "=== [1/3] Regenerating figures from source (regenerate_figures.py) ==="
python "$FIGSCRIPT"

echo "=== [2/3] Compiling main.tex -> main.pdf ==="
cd "$HERE"
# -g forces a fresh compile even if latexmk thinks the PDF is up-to-date
# (deterministic figures can be byte-identical, which would otherwise skip the
# rebuild and leave main.pdf with an mtime older than the PNGs).
if command -v latexmk >/dev/null 2>&1; then
    latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex
    latexmk -g -pdf -interaction=nonstopmode -halt-on-error supplemental.tex
else
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error supplemental.tex
fi

echo "=== [3/3] Build complete ==="
echo "Verify before submit:"
echo "  - main.pdf mtime is NEWER than main.tex and all fig*.png"
echo "  - figures match the current main.tex data (theta-grid, beta domain, Bell state)"
ls -la main.pdf supplemental.pdf 2>/dev/null || true
