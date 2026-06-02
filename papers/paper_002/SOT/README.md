Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# paper_002 SOT (Source of Truth) Directory

**Purpose:** Internal reference -- K9_E completeness and provenance for Paper 002.
**Created:** 2026-05-25
**Last updated:** 2026-06-02 (RCA K9_E Completeness 3-round 4.7/5 PASS; +Section 17 φ_R I.2, +Section 18 Falsification Hierarchy, +version lineage v21-v95)
**Audience:** Internal (VietVunVut + collaborators). NOT for publication.

---

## File Inventory

| File | Type | Purpose |
|------|------|---------|
| `paper_002_SOT.md` | Synthesis | **PRIMARY SOT** -- synthesizes best content from all versions (v4-v95). Full K9_E context (18 sections), VVV-QMRF language, corrected numbers (v12+, v93-v94), φ_R restricted existence (I.2), Falsification Hierarchy (v95). Use this when revising the paper. |
| `draft_v1.md` | Provenance document | **HISTORICAL ORIGIN** -- K9-S12 proposal draft v4 (2026-05-24). Contains the original experimental design, angle optimization, and K9_E postulate as first formulated. NUMBERS ARE PRE-FIX (v12 corrected Eq.(12) thresholds). Use this only for tracing the origin of concepts. |
| `README.md` | Index | This file. |

---

## Relationship Between Files

```
draft_v1.md (v4)          manuscript.md (v95)       phi_restricted_existence_v1_0.md
  K9-S12 proposal           Public-facing paper        φ_R THEOREM (2026-06-01)
  K9_E = central identity   K9_E = sanitized Eq.2-3   Layer 2/3 context
  Numbers: BUG (pre-v12)    Numbers: corrected v12+    Class C THEOREM
       \                         /                        /
        \                       /                        /
         \                     /                        /
          paper_002_SOT.md (synthesis, 18 sections)
            K9_E = central identity (K9_E Completeness direction)
            Numbers = corrected (v12+, v93-v94)
            Academic depth = v53-v95 watershed decisions
            VVV-QMRF language = preserved
            φ_R restricted existence = Section 17
            Falsification Hierarchy = Section 18
```

---

## When to Use Which File

| If you want to... | Read... |
|-------------------|---------|
| Understand K9_E completely (postulate, architecture, predictions, history) | `paper_002_SOT.md` Sections 1-3 |
| Trace the original K9-S12 experimental design | `draft_v1.md` |
| Write/revise the public-facing paper | `manuscript.md` (v95) + `paper_002_SOT.md` for K9_E context |
| Check K9_E numbers (beta thresholds, deltas, FOM) | `paper_002_SOT.md` Section 16 |
| Understand what changed across versions (v4-v95) | `paper_002_SOT.md` Section 14 (14.1 + 14.2) + `../CHANGELOG.md` |
| Map SOT content to manuscript sections | `paper_002_SOT.md` Section 15 |
| Understand φ_R restricted existence (Layer 2/3 context) | `paper_002_SOT.md` Section 17 |
| Understand Falsification Hierarchy scope (Level 0 vs 1-3) | `paper_002_SOT.md` Section 18 |
| Reproduce numerical predictions | `../supplemental/K9S12_proposal.py` |
| Verify novelty claim | `../supplemental/S1_search_audit.md` |

---

## Key Warnings

1. **draft_v1.md has WRONG numbers.** The analytical |cos theta|/2 approximation was corrected in v12. Always use `paper_002_SOT.md` or `manuscript.md` v21 for numerical values.
2. **paper_002_SOT.md uses VVV-QMRF language.** This is intentional -- the SOT preserves framework context removed from the public manuscript. Do NOT copy VVV-QMRF sections directly into the manuscript without translation.
3. **SOT is internal only.** Do not include this directory in arXiv submission or share with external reviewers.

---

*Created 2026-05-25. Update when new synthesis versions are added.*
