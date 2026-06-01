# Edit Requirements: main.tex — Remove VVV-QMRF Framework Dependencies

## Purpose

Strip all references to VVV-QMRF, K-space, K9_E, and Buddhist Pramāṇa epistemology from main.tex.
The paper must stand as a self-contained geometric null-test proposal, motivated entirely by
Bloch sphere geometry and the observed gap in EWF experimental literature.

The two claims that survive intact:
- Claim A: Equatorial Cancellation Theorem (Proposition 1) — keep verbatim, zero changes needed.
- Claim B: Single-waveplate protocol — keep verbatim, zero changes needed.

Everything else is scaffolding. Remove it.

---

## Section-by-Section Edit Instructions

---

### TITLE

Current:
> Have Optical Wigner's Friend Experiments Been Blind to a Geometric Degree of Freedom?

Action: KEEP. Title is self-contained and makes no reference to VVV-QMRF.

---

### ABSTRACT

Current problematic phrase:
> "a search parameter whose methodological role parallels SME coefficients (§ref{sec:why_class})"

Action: KEEP the SME analogy. It is legitimate and VVV-QMRF-free.

No other changes needed in abstract. The abstract already reads independently.

---

### SECTION 1 — Introduction

#### 1a. In brief paragraph

Current:
> "This paper makes no claim about the existence of overlap-dependent deformation in nature ---
> it proposes a null-test protocol analogous in method to the Standard Model Extension (§ref{sec:why_class})."

Action: KEEP. VVV-QMRF-free.

No changes needed in Section 1.

---

### SECTION 2 — Background

#### 2c. Subsection: "Overlap-Dependent Deformation: Why This Class?" (sec:why_class)

This subsection contains the main contamination. Apply the following edits:

**REMOVE block 1 — speculative physical context paragraph:**

Locate and delete the entire paragraph beginning with:
> "Physical context (speculative). In weak measurement [Aharonov1988], the weak value depends
> explicitly on the overlap between pre- and postselected states..."

and ending with:
> "...This is a speculative mechanism, not a derivation; a toy model and full discussion
> in Supplemental S3."

Reason: This paragraph traces the physical motivation back to a registration-layer mechanism
that is only meaningful within VVV-QMRF. Without that framework, the paragraph is circular
speculation. The SME analogy in the preceding paragraph is sufficient motivation.

**KEEP block 2 — Definition and motivation paragraph:**

The paragraph beginning "The basis overlap |<b|d>|² is the simplest scalar..." is
VVV-QMRF-free and provides legitimate geometric motivation. Keep verbatim.

**KEEP block 3 — Equation (2) and constraints (i)-(iii):**

The derivation of f_perp from rotation invariance, alignment limit, and monotonicity
is self-contained and does not require K-space. Keep verbatim.

**KEEP block 4 — Methodological role paragraph:**

The paragraph beginning "Equation (2) is a benchmark parametrization..." and the
SME analogy are VVV-QMRF-free. Keep verbatim.

**KEEP block 5 — Null test paragraph:**

"The experiment is a null test: standard QM predicts the same LF violation regardless
of θ..." Keep verbatim.

---

### SECTION 3 — Equatorial Cancellation Theorem

Action: KEEP entire section verbatim.

Proposition 1, Lemma 1, proof, and physical intuition are purely geometric.
Zero VVV-QMRF content. No changes needed.

---

### SECTION 4 — Experimental Protocol

Action: KEEP entire section verbatim.

The protocol is engineering. No framework references. No changes needed.

---

### SECTION 5 — Model-Independent QM Predictions

Action: KEEP entire section verbatim.

All numerical predictions are derived from standard QM density matrix formalism.
No VVV-QMRF content.

---

### SECTION 6 — Statistical Analysis

Action: KEEP entire section verbatim.

Pure statistics. No framework references.

---

### SECTION 7 — Robustness Summary

Action: KEEP entire section verbatim.

Engineering and statistics. No framework references.

---

### SECTION 8 — Discussion

#### 8a. Subsection: "Interpretation and Falsification"

Action: KEEP verbatim. Falsification criteria are experimental and self-contained.

#### 8b. Subsection: "Future Directions"

**REMOVE the following sentence:**

Locate and delete:
> "A generalization to N > 2 observers is outlined in Supplemental S3; rigorous derivation
> of the required bridge theorems is left for future work."

Reason: "bridge theorems" is K-space vocabulary. Replace with:

> "Extension to N > 2 observers is a natural next step; the geometric cancellation condition
> generalizes to multi-observer overlap products and is left for future work."

All other future directions (θ-sweep, platform independence, locality closure) are
VVV-QMRF-free. Keep verbatim.

---

### SECTION 9 — Conclusion

Action: KEEP verbatim. No VVV-QMRF references present.

---

### SUPPLEMENTAL REFERENCES IN MAIN TEXT

**REMOVE the following inline reference:**

Locate and delete every occurrence of the phrase:
> "(Supplemental S3)"

when it follows text about interpretations, GPT, or VVV-QMRF theory.

Specifically:
- In the abstract: "Supplemental material: S1 (literature search + algebraic proof), S2
  (numerical methods + statistical robustness), S3 (interpretations + General Probabilistic
  Theories (GPT) / weak-measurement development)."

  Replace with:
  "Supplemental material: S1 (literature search + algebraic proof), S2
  (numerical methods + statistical robustness)."

Reason: S3 as described contains VVV-QMRF interpretation material. If S3 is retained
in the supplemental file, it must be rewritten to contain only GPT and weak measurement
discussion without K-space references. Until that is done, do not advertise S3 in the
main text.

---

### BIBLIOGRAPHY

**REMOVE the following entry if present:**

Any self-citation to VVV-QMRF working paper, Zenodo DOI 10.5281/zenodo.20431310,
or vvvqmrf.com.

Reason: Self-citation to an unpublished, non-peer-reviewed framework paper will
flag the submission for skepticism. The experimental proposal stands without it.
The Zenodo timestamp remains as priority record regardless of whether it is cited.

**KEEP all other references.** The existing bibliography (Bong2020, Proietti2019,
Colladay1997, Aharonov1988, Wiseman2023, Giustina2015, Marsili2013, etc.) is
standard and appropriate.

---

### AUTHOR AFFILIATION

Current:
> VietVunVut (Viet -- Nguyen Xuan)
> viet@vvvqmrf.com
> https://vvvqmrf.com
> Independent Researcher, Vietnam

Action on email and homepage: OPTIONAL but recommended.

The vvvqmrf.com domain signals the framework to any reviewer who searches it.
Consider using a neutral email address for submission.
The affiliation "Independent Researcher, Vietnam" is fine and should be kept.
Do not fabricate an institutional affiliation.

---

## Summary of Changes

| Location | Action | Reason |
|---|---|---|
| sec:why_class — speculative mechanism paragraph | DELETE | Traces motivation to VVV-QMRF registration layer |
| sec:future — "bridge theorems" sentence | REPLACE | K-space vocabulary |
| Abstract — S3 description | SHORTEN | S3 as described contains VVV-QMRF material |
| Bibliography — VVV-QMRF self-citation | REMOVE | Unpublished, non-peer-reviewed, flags submission |
| Author homepage vvvqmrf.com | CONSIDER REPLACING | Signals framework to reviewers |
| All other sections | KEEP VERBATIM | VVV-QMRF-free, self-contained |

Total deletions: approximately 15-20 lines out of ~400 lines.
The paper requires minimal surgery. The core is already clean.

---

## What the Paper Looks Like After Edits

The edited paper makes exactly two claims:

**Claim A (Theorem):** Within the surveyed EWF literature, all optical implementations
have operated at equatorial geometry (θ = π/2), which is a geometric fixed point where
every overlap-dependent deformation of quantum statistics vanishes identically.
This is proven by Proposition 1 and is a consequence of Bloch sphere geometry alone.

**Claim B (Protocol):** Re-inserting one QWP into the Bong et al. (2020) apparatus
tilts the Superobserver measurement to θ = 31°, enabling the first experimental probe
of the overlap-only deformation class, with sensitivity β ~ 0.07 at 5σ while
preserving 8.6σ LF violation.

No K-space. No K9_E. No Buddhist epistemology. No VVV-QMRF.

These two claims are sufficient. They are correct. They are falsifiable.
They identify a genuine gap in the experimental literature.
That is enough for a Physical Review A submission.

---

## Recommended Submission Target

Primary: Physical Review A (full paper, ~8 pages two-column)
Alternative: Physical Review Letters (if condensed to ~4 pages)
Preprint: arXiv quant-ph (post before or simultaneously with journal submission)

Do not submit to journals that require institutional affiliation.
Physical Review A accepts independent researcher submissions.

---

*Generated from RCA analysis of VVV-QMRF Working Paper v3.0 and main.tex draft v95 — 2026-06-01*
