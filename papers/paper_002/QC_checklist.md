# Paper QC Checklist -- K9-S12 Single-Waveplate Test

**Date:** 2026-05-31 | **Paper:** manuscript.md (v95) | **QC:** 15/15 PASS
**v95 note:** §8.1 post-submission addition — Level 0 null ≠ Levels 1–3 boundary sentence (3-round RCA 4.1/5). Does not affect any QC criterion; no new claims, equations, or figures.

## Quality Gates

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 1 | Every symbol defined at first use | PASS | K9_E, f_perp, beta, Gen LF 1: Sections 2–3 |
| 2 | Every number has uncertainty | PASS | All correlators: sigma column. Gen LF 1: +-0.0103 |
| 3 | Every figure has self-contained caption | PASS | Figs 1–5: captions + embedded images |
| 4 | All 5 loopholes (Section 8) | PASS | Locality, Detection, Freedom, Superobserver, K9_E scope |
| 5 | Decision criteria: 4 outcomes (Section 5.5) | PASS | Joint/LF-only/calibration/null |
| 6 | Code runnable by third party | PASS | K9S12_proposal.py self-contained |
| 7 | Abstract: no undefined acronyms | PASS | EWF, LF, QWP expanded |
| 8 | References complete + consistent | PASS | 18 refs, consistent format |
| 9 | FOM consistent across Sections 5–7 | PASS | FOM=8.6–8.8 throughout |
| 10 | Section 7.5: actual values, not placeholders | PASS | mu>=0.86, eta>=0.91, dtheta<=+-5 deg |

## Content Gates

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 11 | v31 status accurate | PASS | Section 2.3: qualified, P10-NOISE, K9E-PAT |
| 12 | "First test" framing | PASS | Sections 1, 9.4, 10 |
| 13 | Theorem proof complete | PASS | Section 3.2 |
| 14 | K9_E model clearly defined | PASS | Section 2.3: P9, f_perp, beta |
| 15 | No overclaim about empirical status | PASS | "empirically UNCONFIRMED" |

## Build / Anti-Drift Gate (added 2026-06-03)

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 16 | **Artifacts rebuilt from source this revision** | **MANDATORY** | Before any (re)submit, run `bash arxiv/blind_equator_ArxivR/build.sh` (= `regenerate_figures.py` + `latexmk`). Verify `main.pdf` mtime is **newer** than `main.tex` and all `fig*.png`. Root cause of v97/v99 drift: PNG/PDF are derived artifacts that lagged `main.tex`. Never hand-edit a PNG or ship a stale PDF. |

> **Rule:** `fig*.png`, `main.pdf`, `supplemental.pdf` are DERIVED. Any change to `main.tex` / `supplemental.tex` / figure data ⇒ re-run `build.sh` in the same session. See `arxiv/blind_equator_ArxivR/README.md` → "Build Procedure".

## Remaining

| Item | Priority | Notes |
|------|----------|-------|
| LaTeX conversion | COMPLETED | arXiv format |
| arXiv submit | COMPLETED | Submitted 2026-05-27 |

**Verdict: 15/15 PASS + Gate 16 (build-from-source) added. Re-run build.sh before next submit.**
