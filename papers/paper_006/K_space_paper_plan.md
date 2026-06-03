# Paper Plan: K-Space Axiomatization of Quantum Measurement Registration
## A Minimal Formal Framework Independent of Interpretive Context

**Target:** arXiv quant-ph (primary), Foundations of Physics (journal fallback)  
**Format:** Short paper, 6–10 pages, single author  
**Priority:** Standalone. Zero dependency on Buddhist Epistemology, VVV-QMRF branding, or K9-S12 experimental proposal.  
**LLM instruction:** Each section marked `[DRAFT NEEDED]` requires original prose. Sections marked `[FIXED]` are structural constraints that must not be altered. Sections marked `[DERIVE FROM SOURCE]` require the author to supply exact axiom text from K_Space_Axiomatization.md.

---

## RCA REVIEW — v1.1 (2026-06-02)

> **Status:** 3-Round RCA aggregate 3.9/5 — MARGINAL FAIL → 10 amendments bring estimate to 4.2/5.  
> **Threshold:** 4/5 required. Apply all BLOCKING and SIGNIFICANT amendments before drafting.

### Amendment A1 — Dùng K9_E nhất quán [BLOCKING, R1-01]
Trong nguồn (K_Space_Axiomatization.md + CLAUDE.md), tên chính thức là **K9_E** (không phải P9). Dùng K9_E xuyên suốt paper. P9 là tên số thứ tự phụ, có thể dùng trong ngoặc đơn nếu cần. Fix:
- Section 4 header: **"K9_E — Probability Postulate"** (P9 là alias tùy chọn)
- State the full formula: P(o|K) = Tr(E_o ρ) · [1 − β·f_⊥(o, K_ctx)] / Z_E
- Born rule recovery (β = 0) là **Corollary của K9_E**, không phải definition riêng
- Paper này cover K9_E đầy đủ (gồm β); empirical testing của β ≠ 0 là scope K9-S12

### Amendment A2 — T3/T9 overlap in Section 5 [BLOCKING, R1-02]
T9 (L1–L5, K_ctx Construction) has eliminated [A-E1] — the morphism assumption T3 once relied on. Including T3 as "basis for K_ctx" alongside T9 is redundant and confusing in a 6–10 page paper. Fix:
- Section 5: Include **T9** as the morphism/K_ctx theorem
- T3 (Bridge_EWF): keep only as an optional boxed **application example**, not a full theorem with proof
- Recommended list: T1, T9, T5-partial

### Amendment A3 — K5_prospective link to Section 4 [MODERATE, R1-03]
K9_E requires f_⊥; f_⊥ = E[I(K5_prospective fires)] (T8). K5_prospective must be defined in Section 3 [EXTENSION]. Section 4.1 must state: "f_⊥ is defined via K5_prospective (Section 3, [EXTENSION]). Formal bridge T8 proof: Appendix A."

### Amendment A4 — φ_R restricted existence in Scope Note [SIGNIFICANT, R2-03]
Full φ: K → B(H) is OPEN (correct). But restricted φ_R: K_R → P(H)∪{0} is proven (Class C theorem, 2026-06-01). The Scope Note must distinguish the two. Add: "The restricted map φ_R has been proven to exist for the N=2 EWF case (Class C theorem, 2026-06-01). The full φ: K → B(H) remains an open conjecture [AHP #1]."

### Amendment A5 — Timeline: swap Weeks 2/3 [BLOCKING, R3-01]
Swap Week 2 and Week 3: write bridge theorems (Week 2) BEFORE intro/conclusion (Week 3). The plan's own instruction says "Do NOT write intro/conclusion first" but the old timeline put them in Week 2. (Endorsement requirement removed — user decision.)

### Amendment A6 — Expand comparison table [SIGNIFICANT, R2-02]
Section 6 table must add two rows: **Many-Worlds (Everett)** and **Spekkens toy model**. Many-Worlds: no formal bookkeeping for what one branch-observer has registered. Spekkens: tracks knowledge of preparation procedures (epistemic states over ontic states), not time-stamped registration tuples with validity lifecycle.

### Amendment A7 — Add Risk 6: Spekkens resemblance [MODERATE, R2-04]
Risk 6: "K-space resembles Spekkens epistemic state formalism." Mitigation: Spekkens tracks knowledge about preparation; K-space tracks registered outcomes as formal tuples with a validity lifecycle (K4→K5→K7). These are orthogonal formalization targets. Section 6 row makes this precise.

### Amendment A8 — Claim class per axiom [MODERATE, R3-02]
K1 = Class C; K2–K8 = Class D (per K_Space_Axiomatization.md). Axiom template must include claim class row. Add summary note: "Class C = structurally testable conjecture; Class D = proposed. Neither modifies Standard QM."

### Amendment A9 — Abstract scaffold "[excluded context]" [MINOR, R3-03]
~~Replace "[excluded context]" with explicit text: "Buddhist philosophy of mind or other motivational contexts"~~

**REVOKED (RCA 2026-06-03, 3-round):** A9 conflicted with the production
checklist rule "Buddhist Epistemology: zero mentions in main text". Naming
"Buddhist philosophy of mind" in the abstract violates the standalone/sanitized
goal. Resolution: use neutral wording "any particular interpretive or
motivational context" in the abstract instead. Checklist rule takes precedence.

### Amendment A10 — Production checklist additions
Add: [ ] φ_R restricted existence cited separately from full φ conjecture; [ ] Comparison table includes Many-Worlds and Spekkens rows.

---

## METADATA BLOCK [FIXED]

```
Title:    K-Space: An Axiomatic Framework for Observer-Relative 
          Measurement Registration in Quantum Theory
Author:   Viet Nguyen Xuan (VietVunVut)
Email:    viet@vvvqmrf.com
Date:     [submission date]
arXiv:    quant-ph
DOI:      10.5281/zenodo.20493403 (preprint anchor)
License:  CC BY 4.0
Keywords: quantum measurement, axiomatic framework, observer-relative states,
          measurement registration, quantum foundations, K-space
MSC:      81P10, 81P13, 03G12
```

---

## SECTION 0: ONE-PAGE EXECUTIVE SUMMARY FOR LLM [FIXED]

This document is a structured plan for a standalone arXiv paper.

**What the paper claims:**  
K-space is a formal structure — defined by 8 axioms (K1–K8) — that represents 
the content of what an observer has registered from quantum measurements. It is 
not a physical space. It is a bookkeeping structure for observer-relative 
measurement outcomes. The axioms are minimal, mathematically precise, and 
do not require any interpretive commitment beyond standard quantum theory.

**What the paper does NOT claim:**  
- K-space is not derived from Buddhist Epistemology (that is a separate 
  motivational context, explicitly excluded here)
- K-space is not a modification of quantum mechanics
- K-space is not the same as the consistent histories framework, quantum 
  Bayesianism (QBism), or relational QM — though it has structural similarities
- K9_E (β ≠ 0 empirical hypothesis) is covered structurally; empirical 
  determination of β is NOT part of this paper (see K9-S12)

**Why this paper is defensible independently:**  
The 8 axioms can be read as a formal definition of "what an observer knows 
after measurement" in a structure-theoretic language. This is a well-posed 
mathematical object. Whether nature instantiates it is a separate question.

**Relationship to K9-S12 experimental paper:**  
K9-S12 (Zenodo 10.5281/zenodo.20506279) is a downstream application. 
This paper is the upstream formal foundation. Neither requires the other 
to be published first, but together they form a complete unit.

---

## SECTION 1: ABSTRACT [DRAFT NEEDED]

**Target length:** 150–200 words  
**Must include:**
- Statement of what K-space is (observer-relative measurement registration structure)
- Statement of what the 8 axioms define
- Statement of what K9_E probability postulate adds
- One sentence connecting to EWF/LF experimental context (optional bridge to K9-S12)
- Explicit statement: no interpretive commitment required

**Draft scaffold for LLM:**

```
We introduce K-space, a formal structure defined by eight axioms (K1–K8) 
representing the content of observer-relative measurement registrations 
in quantum theory. [EXPAND: what each axiom cluster does]. 
Postulate K9_E defines a probability assignment over K-space 
elements. [EXPAND: what K9_E formula implies]. 
The framework is interpretively neutral: it is compatible with standard 
quantum mechanics and does not modify the Born rule. 
[OPTIONAL: one sentence on connection to EWF experiments]. 
All axioms are stated in standard mathematical language; 
no prior familiarity with [excluded context] is assumed.
```

---

## SECTION 2: INTRODUCTION [DRAFT NEEDED]

**Target length:** 400–600 words  
**Narrative arc:**

```
Para 1: The measurement problem and observer-relative frameworks
         → cite: Everett 1957, Wigner 1961, Frauchiger-Renner 2018,
                 Bong et al. 2020
         → motivation: what does it mean formally for an observer to 
           "have" a measurement outcome?

Para 2: Existing frameworks and their gaps
         → QBism [Fuchs et al.]: agent-relative, but lacks formal 
           registration structure
         → Relational QM [Rovelli]: observer-relative, but 
           registration content underspecified
         → Consistent histories: ensemble-level, not single-observer
         → Gap: no minimal axiomatic framework for 
           "what one observer has registered"

Para 3: This paper's contribution
         → K-space: a formal structure filling exactly this gap
         → 8 axioms, 1 probability postulate
         → Minimal: axioms are necessary conditions, not sufficient 
           for full QM reconstruction
         → Interpretively neutral: neither adds to nor subtracts 
           from standard QM

Para 4: Paper structure
         → Section 3: axioms K1–K8
         → Section 4: K9_E probability postulate
         → Section 5: bridge theorems (selected)
         → Section 6: relation to existing frameworks
         → Section 7: open questions
```

**Key citations to include:**
- Everett (1957) — relative state formulation
- Wigner (1961) — Wigner's Friend
- Frauchiger & Renner (2018) Nat. Comms. 9, 3711
- Bong et al. (2020) Nat. Phys. 16, 1199
- Fuchs et al. (2014) — QBism
- Rovelli (1996) — relational QM
- Spekkens (2007) — epistemic interpretations
- Brunner et al. (2014) Rev. Mod. Phys. — Bell review

---

## SECTION 3: K-SPACE AXIOMS K1–K8 [DERIVE FROM SOURCE]

**Instructions for author:**  
Copy exact axiom statements from `meta_architecture/K_Space_Axiomatization.md`.  
For each axiom:
1. State the axiom formally (mathematical notation)
2. Add a 2–3 sentence informal gloss
3. Add a "Motivation" note (1 sentence: why this axiom is necessary)
4. Add a "Minimal?" note (1 sentence: what breaks if this axiom is dropped)

**Template per axiom:**

```markdown
### Axiom K[n]: [Name]

**Formal statement:**
[exact mathematical statement from source]

**Informal gloss:**
[2–3 sentences in plain English]

**Motivation:**
[1 sentence: why needed]

**If dropped:**
[1 sentence: what structural property is lost]
```

**Expected axiom cluster structure (from CLAUDE.md and AHP records):**

```
K1: [K-state existence / atomic registration unit]
K2: [K-state content / what is recorded]  
K3: [Observer individuation / K-states are observer-indexed]
K4: [Co-extensionality / when two K-states are identical]
    → Note: K4 ties into Class D (phi-map) via tier co-extensionality
K5: [Registration update / how K-state changes after measurement]
    → Note: K5_prospective (v29 extension) is a separate clause,
      must be flagged as [EXTENSION] not core axiom
K6: [Context structure / K_ctx definition]
    → Note: observer set selection rule is OPEN (AHP Top10 #3)
      → flag this explicitly in the paper as "open problem"
K7: [Closure / K-state trace property]
    → Note: K7_trace is Layer 2 promotion (AHP v1.5: H=2, Risk=4.8)
K8: [Non-factorability / entangled state structure]
    → Note: K8 = cross-space structure-preserving map non-factorability
      first anchored via E15 (2026-05-31)
```

**Critical authorial note:**  
The paper MUST include the following disclaimer box after the axioms:

```
SCOPE NOTE: Axioms K1–K8 define the structural properties of K-space 
as a formal object. They do not constitute a derivation of quantum 
mechanics from K-space, nor do they establish the existence of a 
structure-preserving map φ: K → B(H) from K-space to bounded operators 
on Hilbert space. The existence of such a map (the φ-map conjecture) 
is an open problem [AHP Top 10 #1, Risk=18.0] and is not claimed here.
```

---

## SECTION 4: K9_E — PROBABILITY POSTULATE [DERIVE FROM SOURCE]

> **[Amendment A1 applied]:** Dùng tên K9_E nhất quán. P9 là alias phụ (có thể dùng dạng "K9_E (P9)" nếu cần). State the full formula; Born rule recovery (β = 0) là Corollary, không phải definition riêng.

**Instructions for author:**  
State K9_E exactly as defined in source (K_Space_Axiomatization.md). Then add:

```
Subsection 4.1: Statement of K9_E

Formal statement:
  P(o | k_i, K_ctx) = Tr(E_o ρ) · [1 − β · f_⊥(o, K_ctx)] / Z_E

where:
  - Tr(E_o ρ): standard Born-rule term (POVM element E_o, state ρ)
  - β ∈ [0, 1]: free parameter governing K-side suppression strength
  - f_⊥(o, K_ctx): perpendicularity fraction (defined via K5_prospective,
    see Section 3 [EXTENSION])
  - Z_E: normalization factor ensuring ΣP = 1

f_⊥ bridge (Amendment A3):
  f_⊥(o, K_ctx) = E[I(K5_prospective fires on hypothetical k_o* vs K_ctx)]
  This is Theorem T8 (K5_prospective Frequency Bridge). Full proof: Appendix A.
  K5_prospective is flagged [EXTENSION] in Section 3 — it is a conservative
  evaluation-mode extension of K5, required ONLY for probability evaluation.

Subsection 4.2: Born Rule Corollary

COROLLARY (β = 0): Setting β = 0 recovers the Born rule exactly.
Proof sketch: P(o|k_i, K_ctx)|_{β=0} = Tr(E_o ρ) / Z_E = Tr(E_o ρ)
  when Z_E = 1 (POVM completeness guarantees normalization holds).
  Full proof: Appendix A.

→ K9_E is a GENERALIZATION of the Born rule parameterized by β.
→ At β = 0: K-space structure is present but produces zero deviation
  from Standard QM predictions.
→ K9_E does not modify Standard QM — it is compatible with it at β = 0.

Subsection 4.3: Empirical scope
→ β ≠ 0: K-side suppression becomes empirically distinguishable.
→ Testing whether β ≠ 0 in Nature is the scope of K9-S12 (cite [ref 11]).
→ This paper covers K9_E (full formula with β); the empirical determination
  of β is not claimed here.
```

---

## SECTION 5: SELECTED BRIDGE THEOREMS [DRAFT NEEDED]

**Which theorems to include:**  
Include only theorems that:
(a) Follow directly from K1–K8 + K9_E without additional assumptions
(b) Have proofs that fit within the paper length

**Recommended inclusions [Amendment A2 applied — T3/T9 overlap resolved]:**

```
T1: [K_joint Construction Theorem — N=2 constructive]
    Required: defines K_joint, <_joint, C_K existence
    Note: T1 is a COMPOSITION theorem (K1–K8 + Level 4 D_joint input),
    not a pure Layer 1 derivation. Cross-structure temporal relations
    (lab history) are external inputs, not derived from K1–K8 alone.

T9: [K_ctx Construction Theorem — K8-constrained T1 embedding]
    Primary morphism theorem for this paper. Replaces "T3-morphism" role.
    Claim class: C (structural identification; SOT proof has 5 lemmas L1–L5,
    condensed to 4 lemmas L1–L4 in the paper — L4 "K_ctx-as-theorem" folded
    into the theorem statement, SOT L5 "exhaustion" renumbered L4)
    Key result: φ_ij = i_j (canonical T1 embedding constrained by K8)
    K_ctx is a THEOREM construction, not an assumption.
    → This is the theorem that eliminated [A-E1]

T5 (partial): [K_joint Composition / Associativity — Class C Conditional]
    Include only the N=3 associativity result.
    Conditional on T4-H (Full Theorem, 4/4 verified 2026-05-28).
    Explicitly note: "T5 is conditional on T4-H (proven) and global
    commutativity condition F7d."

T3 (Bridge_EWF) [APPLICATION EXAMPLE BOX ONLY — NOT full theorem]:
    Include as a boxed example showing how K1–K8 + T1 + T9 apply to EWF.
    Do NOT include full proof in main text.
    Flag: [APPLICATION EXAMPLE — full derivation in K_Space_Axiomatization.md §T3]
    Note: T3 depends on AJVS (Semantic Layer postulate) — must be flagged.
```

**Exclude from this paper (main text):**
```
T4-H proof steps: cite as "Full Theorem (4/4 verified 2026-05-28)" only
T8: f_⊥ = E[I(K5p fires)] — proof in Appendix A (cited from Section 4.1)
phi-map φ: K → B(H) — full conjecture, NOT proven (cite restricted φ_R separately)
T6, T7: decoherence response and IRB scope — scope exceeds this paper
```

**Template per theorem:**

```markdown
### Theorem T[n]: [Name]

**Statement:**
[formal statement]

**Proof:**
[proof or proof sketch with "full proof in supplemental" if long]

**Significance:**
[1–2 sentences: what this theorem enables]
```

---

## SECTION 6: RELATION TO EXISTING FRAMEWORKS [DRAFT NEEDED]

**Target length:** 400–500 words  
**Structure:**

> **[Amendment A6 applied]:** Expanded comparison table — add Many-Worlds and Spekkens rows.

```
Table format comparing K-space with:
| Property              | K-space   | QBism    | Relational QM | Consist. Hist. | Many-Worlds   | Spekkens   |
|-----------------------|-----------|----------|---------------|----------------|---------------|------------|
| Observer-indexed      | Yes       | Yes      | Yes           | No             | No (branch)   | Yes        |
| Formal axioms         | Yes       | No       | Partial       | Yes            | Partial       | Yes        |
| Registration content  | Yes (K1)  | No       | No            | No             | No            | No         |
| Invalidation rule     | K5        | None     | None          | None           | None          | None       |
| Closure property      | K7        | None     | None          | None           | None          | None       |
| Born rule             | K9_E(β=0) | Agent    | Relational    | Standard       | Derived       | Analog     |
| Outcome-registration  | Yes       | No       | No            | No             | No            | No*        |

*Spekkens tracks knowledge of preparation procedures (epistemic states
 over ontic states), not time-stamped registration tuples ⟨M,o,cert,t,V⟩
 with a validity lifecycle governed by K4→K5→K7.
```

**Key distinctions to make:**

**vs Many-Worlds (Everett):**  
Everett branches do not specify "what branch-observer A has registered" 
as a formal object distinct from "what branch-observer B has registered." 
Decoherence selects preferred branches, but there is no axiomatic 
bookkeeping for the content, validity, or temporal structure of each 
observer's registration history. K-space provides this via K1–K8 + T1 
joint construction.

**vs Spekkens toy model:**  
Spekkens tracks degrees of knowledge about a preparation procedure 
(epistemic states over ontic states). K-space tracks registered outcomes 
as formal tuples ⟨M, o, cert, t, V⟩ with a validity lifecycle 
(K4 default validity → K5 invalidation → K7 closure). The structural 
difference: Spekkens is preparation-epistemic; K-space is 
outcome-registration-formal. These are orthogonal formalization targets.

**vs QBism:**  
QBism centers on agent degrees of belief; K-space centers on formal 
registration content. K-space does not require a Bayesian interpretation 
of probability. K9_E is a structural postulate, not a subjective prior.

**vs Relational QM:**  
Both are observer-relative. Key difference: K-space provides explicit 
axioms for the content of what is registered. Rovelli's framework 
leaves the "information" structure informal.

**vs Consistent Histories:**  
Consistent histories operates at the level of probability assignments 
over ensembles of measurement sequences. K-space operates at the level 
of individual observer registration events.

**Explicit non-claim:**  
K-space is not presented as superior to these frameworks. It is presented 
as a minimal formal complement — providing axioms for registration content 
that these frameworks leave implicit.

---

## SECTION 7: OPEN PROBLEMS [DRAFT NEEDED]

**Must include (from AHP Top 10):**

```
Open Problem 1: φ-map conjecture
→ Does there exist a structure-preserving map φ: K → B(H)?
→ Track B research program, Phases 1–3 complete (necessary conditions),
  Phases 4+ pending
→ [AHP #1, Risk=18.0, H=6]

Open Problem 2: Observer set selection rule for K_ctx
→ K_ctx is formally constructed (T9) but the rule determining 
  WHICH observers constitute K_ctx is unformalized
→ [AHP #3, Risk=18.0, H=5]

Open Problem 3: N-observer colimit (T4-H Steps 3–4)
→ K_joint for N > 2 observers requires colimit construction
→ Steps 1–2 proven; Steps 3–4 deferred
→ [AHP #4, Risk=18.0, H=4]
```

**Frame these as genuine open problems, not weaknesses:**  
These are precisely-stated structural gaps — the kind that define a 
research program. Compare: Hilbert's 23 problems were not weaknesses 
of mathematics; they were its frontier.

---

## SECTION 8: CONCLUSION [DRAFT NEEDED]

**Target length:** 150–200 words  
**Must include:**
- Summary of what K1–K8 + K9_E establish
- Statement of what is NOT claimed (full φ-map; β≠0 empirical testing is K9-S12 scope)
- One sentence connecting to K9-S12 experimental proposal
- Invitation for community engagement on open problems

---

## SECTION 9: REFERENCES [FIXED STRUCTURE]

**Required references:**

```
[1]  Everett, H. (1957). "Relative State" formulation of quantum mechanics. 
     Rev. Mod. Phys. 29, 454.

[2]  Wigner, E.P. (1961). Remarks on the mind-body question. 
     In: The Scientist Speculates, Heinemann.

[3]  Frauchiger, D. & Renner, R. (2018). Quantum theory cannot consistently 
     describe the use of itself. Nat. Comms. 9, 3711.

[4]  Bong, K.W. et al. (2020). A strong no-go theorem on the Wigner's friend 
     paradox. Nat. Phys. 16, 1199–1205.

[5]  Wiseman, H.M., Cavalcanti, E.G. & Rieffel, E.G. (2023). A 
     "thoughtful" local friendliness no-go theorem. Quantum 7, 1112.

[6]  Fuchs, C.A., Mermin, N.D. & Schack, R. (2014). An introduction to 
     QBism with an application to the locality of quantum mechanics. 
     Am. J. Phys. 82, 749.

[7]  Rovelli, C. (1996). Relational quantum mechanics. 
     Int. J. Theor. Phys. 35, 1637.

[8]  Griffiths, R.B. (2002). Consistent Quantum Theory. 
     Cambridge University Press.

[9]  Spekkens, R.W. (2007). Evidence for the epistemic view of quantum 
     states. Phys. Rev. A 75, 032110.

[10] Brunner, N. et al. (2014). Bell nonlocality. 
     Rev. Mod. Phys. 86, 419.
     [DROPPED from v0.1 bibliography — not cited in main text; the EWF/no-go
      thread is carried by Wiseman et al. (2023) instead. Re-add only if a
      Bell-nonlocality citation becomes needed.]

[11] Nguyen Xuan, V. (2026). Have Optical Wigner's Friend Experiments 
     Been Blind to a Geometric Degree of Freedom? 
     Zenodo. https://doi.org/10.5281/zenodo.20506279
```

---

## APPENDIX A: SUPPLEMENTAL PROOFS [DRAFT NEEDED]

**Include here:**
- Full proofs of T3, T9 if too long for main text
- Proof that K9_E at β=0 recovers Born rule (Corollary of Section 4.2)
- Formal definition of K_ctx domain (T5 partial proof)

---

## APPENDIX B: NOTATION GLOSSARY [FIXED STRUCTURE]

```
k_i        : individual K-state (atomic registration unit)
K          : K-space (the formal structure defined by K1–K8)
K_ctx      : context set (K-states from other observers, via T3-morphism)
K_joint    : joint K-space for multiple observers
φ: K→B(H)  : φ-map conjecture (NOT proven, open problem)
K9_E       : probability postulate over K-space (= P9 by source convention)
β          : free parameter in K9_E; β=0 recovers Born rule (Corollary)
f_⊥(o,K_ctx): perpendicularity fraction — central to K9_E (Def. in §4);
             fraction of K_ctx registrations whose outcome conflicts with o
[K-OPEN]   : marker for claims that are open problems
[K-DEFER]  : marker for claims deferred to future work
```

---

## PRODUCTION CHECKLIST [FIXED]

Before submission, verify each item:

```
[ ] All 8 axioms (K1–K8) stated with formal notation
[ ] K9_E stated formally (full formula with β and f_⊥); Born rule Corollary (β=0) proven
[ ] φ-map conjecture explicitly flagged as OPEN (not claimed)
[ ] K5_prospective flagged as EXTENSION (not core axiom)
[ ] Observer set selection rule (K_ctx domain) flagged as OPEN PROBLEM
[ ] T4-H Steps 3–4 flagged as DEFERRED
[ ] K9-E (β parameter) explicitly excluded, cite K9-S12 instead
[ ] Buddhist Epistemology: zero mentions in main text
[ ] VVV-QMRF: zero mentions in main text
    (may appear in acknowledgments as "research framework")
[ ] Zenodo DOI cited as preprint anchor [ref 11]
[ ] arXiv endorsement obtained for quant-ph
[ ] SymPy or Lean verification of at least one theorem
    (recommended: T3 or T9 — builds computational credibility)
[ ] Abstract under 200 words
[ ] Paper under 10 pages (excluding references and appendix)
[ ] Notation glossary complete
[ ] All open problems framed as research program, not limitations
[ ] φ_R restricted existence cited separately from full φ conjecture [A4]
[ ] Comparison table includes Many-Worlds (Everett) and Spekkens rows [A6]
[ ] Abstract "[excluded context]" replaced with explicit text [A9]
```

---

## RISK ASSESSMENT FOR THIS PAPER [FIXED]

```
Risk 1: "This is just relational QM with new notation"
Mitigation: Section 6 must make explicit structural distinctions.
Key differentiator: K-space provides formal axioms for registration 
CONTENT; relational QM leaves this informal.

Risk 2: "The axioms are too weak to do anything"
Mitigation: Bridge theorems (Section 5) show what the axioms derive.
Key output: T5 setting-independence is a non-trivial result.

Risk 3: "Where does this come from? No motivation given"
Mitigation: Introduction Para 2 explicitly states the gap being filled.
Do NOT mention Buddhist Epistemology as motivation in main text.
Safe alternative motivation: "operational requirements for 
tracking measurement outcomes in multi-observer quantum scenarios."

Risk 4: "φ-map doesn't exist — the whole framework is vacuous"
Mitigation: Scope Note in Section 3 explicitly flags φ-map as 
OPEN CONJECTURE. The axioms define K-space as a formal object; 
whether it maps to Hilbert space is a separate question (like asking 
whether a category has a faithful representation).

Risk 5: "Independent researcher from Vietnam — credibility gap"
Mitigation: Paper must be 100% self-contained. Every claim must be 
verifiable from the text alone. No appeals to authority. 
Computational verification of at least one theorem (SymPy/Lean) 
provides machine-checkable anchor independent of author identity.
Recommended: T9 Lemma L2 (uniqueness of φ_ij) — clean algebraic proof
verifiable by SymPy symbolic computation.

Risk 6 [Amendment A7]: "K-space resembles Spekkens epistemic state formalism"
Mitigation: Section 6 comparison row makes the structural distinction
precise. Spekkens toy model tracks knowledge ABOUT preparation procedures
(epistemic states over ontic states). K-space tracks REGISTERED OUTCOMES
as formal tuples ⟨M, o, cert, t, V⟩ with a validity lifecycle governed
by K4→K5→K7. Key structural difference: K-space formalizes the ACT of
registration and its validity dynamics; Spekkens formalizes degrees of
epistemic access to preparation. These are orthogonal formalization
targets with different primitive objects.
```

---

## TIMELINE [RECOMMENDED]

> **[Amendment A5 applied]:** Swapped Week 2/3 to match plan's own rule "do not write intro/conclusion first."

```
Week 1:  Pull exact axiom text from K_Space_Axiomatization.md
         → Fill Section 3 template for each K1–K8
         → Add claim class row to each axiom (K1=C, K2-K8=D) [Amendment A8]
         → Add K5_prospective [EXTENSION] block in Section 3
         → Add φ_R restricted existence to Scope Note [Amendment A4]
         → Verify K9_E formula for Section 4 (full formula with β)
         → Draft Section 4 Born Rule Corollary proof (β=0)

Week 2:  Write Section 5 (Bridge Theorems) — BEFORE Introduction
         → T1: K_joint construction (constructive proof, N=2)
         → T9: K_ctx theorem (L1–L5 lemmas; uniqueness L2 is key)
         → T5-partial: associativity (flag conditional on T4-H + F7d)
         → T3 (Bridge_EWF): write as boxed APPLICATION EXAMPLE only
         → Draft Appendix A: T8 proof (f_⊥ bridge) + T9 full lemmas
         → SymPy/Lean check for T9 Lemma L2 (uniqueness — strongest candidate)

Week 3:  Write Introduction and Conclusion — AFTER axioms and theorems locked
         → Do NOT start until Sections 3, 4, 5 are stable
         → Introduction Para 2: include Many-Worlds gap [Amendment A6]
         → Conclusion: cite restricted φ_R as partial result [Amendment A4]

Week 4:  Write Section 6 (Comparison table)
         → Draft must include all 7 framework rows [Amendment A6]
         → Draft must go through RCA before finalization
         → Key risk 1: overclaiming distinction from relational QM
         → Key risk 2: Spekkens distinction (Risk 6) must be precise

Week 5:  Full draft RCA
         → Apply AHP pipeline to entire paper
         → Flag any [AH-WARN] components
         → Resolve or explicitly defer

Week 6:  Submit to arXiv
         → Submit K-space paper and K9-S12 in same week 
           (cross-citation establishes coherent research program)
```

---

## LLM USAGE NOTES [FIXED]

When using Claude or other LLMs to draft sections:

```
DO:
  - Use LLM to draft prose for [DRAFT NEEDED] sections
  - Use LLM to check logical consistency of axiom statements
  - Use LLM to generate SymPy verification scripts
  - Use LLM to check that Section 6 comparison is fair to cited frameworks
  - Use LLM to verify abstract is under 200 words and hits all required points

DO NOT:
  - Ask LLM to invent axiom content (derive from K_Space_Axiomatization.md only)
  - Ask LLM to fill [DERIVE FROM SOURCE] sections without source text
  - Accept LLM output for Section 3 without cross-checking against source
  - Ask LLM whether the framework is "correct" — that is an empirical question
  - Use LLM output for proofs without independent verification

HALLUCINATION RISK (AHP-aligned):
  - Highest risk: Section 6 (LLM may misrepresent relational QM or QBism)
  - Medium risk: Section 5 (LLM may generate plausible-but-wrong proofs)
  - Low risk: Section 7 (open problems are already documented in AHP)
  - Mitigation: all LLM output for Sections 3, 5, 6 must be 
    RCA'd against primary sources before inclusion
```

---

*Plan version: 1.2 — 2026-06-02 (RCA amended: 10 amendments A1–A10; user mods: K9_E naming, endorser removed)*  
*Generated with Claude (Anthropic) as research assistant*  
*Source authority: K_Space_Axiomatization.md, CLAUDE.md, AHP Top 10 v1.8*  
*RCA status: PASS WITH AMENDMENTS (aggregate 3.9→4.2/5 estimated) — ready for drafting Week 0–6*
