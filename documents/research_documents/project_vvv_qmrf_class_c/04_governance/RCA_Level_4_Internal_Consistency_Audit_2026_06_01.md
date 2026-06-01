Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA — Level 4 Internal Consistency Audit: D_joint, AdmJoint, requires_K_joint

**Date:** 2026-06-01
**Method:** 3-Round RCA × 5-Why × Scoring threshold 4/5
**Scope:** VVV-QMRF Level 4 predicates; VVV-QMRF-EX as compass (not cargo)
**Status:** COMPLETE + ALL FIXES APPLIED (2026-06-01) — 7/7 candidates resolved: 2 structural defects FIXED (v50), 3 thin-definition gaps RESOLVED (v51), 2 benign (no action). Level 4 freeze MAINTAINED.
**Fix commits:** (1) `96078b3` — I-01 `scope(D_joint; Arch)` formal definition + I-03 C_K-sphere/scope relationship added to K6. (2) I-02 D_joint structural criterion + I-06 Arch parameter note + I-07 object/methodology separation added to K5 C_K definition block. Both peer copies updated, PEER-SYNC verified.
**Cross-reference:** `RCA_P3_P4_Relationship_Blockers_2026_06_01.md` (for B_PHI C_K/D_joint category boundary)

> **DISCLAIMER:** VVV-QMRF is independent Class C/D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use.

---

## MASTER CONTEXT BLOCK

```
RCA SESSION — LEVEL 4 INTERNAL CONSISTENCY AUDIT — 2026-06-01

STARTING STATE:
  Level 4 is declared "frozen" (2026-05-31, 3-Round RCA 4.69/5).
  Level 4 contains 6 predicates: D_joint, requires_K_joint, AdmJoint, bot_K, Bridge_EWF, ODC_K.
  This audit checks the first three (as requested): D_joint, AdmJoint, requires_K_joint.

  SOT HIERARCHY:
    Primary SOT: WP v3.0 section 6.3 (published Zenodo 2026-05-28)
    Reference SOT: WP v2.0 section 4.3 (published Zenodo)
    Derived reference: K_Space_Axiomatization.md (v2.6, both canonical + Class C copies)
    Registry: VVV_QMRF_research_terminology.md (F-EWF-000, F-EWF-002, C-010, C-011)

  SOURCES AUDITED:
    [S1] papers/paper_003/VVV-QMRF_Working_Paper_v3.0.md section 6.3 (PUBLISHED SOT)
    [S2] papers/Testable_Prediction_Section/.../VVV-QMRF_Working_Paper_v2.0.md section 4.3 (PUBLISHED REFERENCE)
    [S3] documents/.../project_vvv_qmrf_class_c/01_axiomatization/K_Space_Axiomatization.md (v2.6, WORKING COPY)
    [S4] documents/.../meta_architecture/K_Space_Axiomatization.md (v2.6, CANONICAL COPY)
    [S5] documents/.../project_vvv_qmrf_class_c/06_references/VVV_QMRF_research_terminology.md
    [S6] documents/.../meta_architecture/phi_O5_n_observer_extension_v0_1.md (v0.7)
    [S7] documents/.../project_vvv_qmrf_class_c/09_Fitting_Baumann_Brukner/BB_VVV_fit_plan.md (v1.4)

  KEY QUESTIONS:
    Q1: Are D_joint, AdmJoint, and requires_K_joint internally consistent with each other?
    Q2: Are there undefined concepts used in formal definitions?
    Q3: Are there inconsistencies between published SOT and working documents?
    Q4: Does the definitional chain have any circularities?
```

---

## 0. EXECUTIVE SUMMARY / TOM TAT

**7 inconsistency candidates identified. 2 confirmed structural defects, 3 thin-definition gaps, 2 benign.**

| ID | Candidate | Severity | RCA Score | Verdict |
|----|-----------|----------|-----------|---------|
| **I-01** | `scope(D_joint)` undefined in all SOTs | **HIGH** | 4.7/5 | **CONFIRMED STRUCTURAL DEFECT** — K6(c) depends on undefined concept; must be resolved |
| **I-02** | D_joint formal thinness / definitional loop with requires_K_joint | **MEDIUM** | 4.2/5 | **THIN-DEFINITION GAP** — D_joint is a label, not a definition; operationalized only through requires_K_joint |
| **I-03** | C_K-sphere(k) vs scope(D_joint) — dual membership without explicit relationship | **MEDIUM** | 4.3/5 | **CONFIRMED STRUCTURAL DEFECT** — two membership concepts used in same axiom (K6) without stated relationship |
| **I-04** | K6(c) asymmetric: only k1 in scope(D_joint), not k2 | **LOW** | 3.2/5 | **BENIGN** — asymmetry is structurally justified (direction of authority is from k2 to k1) but justification not documented |
| **I-05** | AdmJoint (ii)/(iii) redundancy (Condition 4 covered twice) | **LOW** | 2.8/5 | **BENIGN** — intentional redundancy; self-certification is architecturally central |
| **I-06** | D_joint Arch parameter: explicit in v2.0, implicit in v3.0 | **MEDIUM** | 4.0/5 | **THIN-DEFINITION GAP** — parameter drift across versions; Arch is still conceptually present but notationally dropped |
| **I-07** | requires_K_joint condition 5: definitional self-reference | **LOW** | 3.5/5 | **THIN-DEFINITION GAP** — condition is definitional, not causal; structurally coherent but notationally imprecise |

**Overall Audit Score: 4.1/5** — Level 4 is structurally coherent with 2 confirmed defects that are fixable without unfreezing K1-K8 axioms.

**Decision:** Level 4 remains frozen. No semantic revision needed — the 2 confirmed defects are in K6's use of Level 4 concepts, not in Level 4 definitions themselves. Fix strategy: (1) define `scope(D_joint)` formally in the axiomatization or WP; (2) clarify C_K-sphere vs scope(D_joint) relationship.

---

## PART A — REFERENCE DEFINITIONS (FROM SOT)

Before the RCA, here are the exact definitions from the published SOT.

### A.1 D_joint — Shared Validity Demand

**From WP v2.0 section 4.3 [S2]:**
```
D_joint(A, B, Arch) in {0, 1}

Evaluates to 1 when Arch demands that A and B support one shared
registration-validity claim. The comparison architecture Arch is
specified by the experimental design. D_joint is not imposed by any
single observer; it is a structural feature of the comparison architecture.
```

**From WP v3.0 section 6.3 [S1]:** D_joint is referenced within requires_K_joint definition but not given a separate formal block. The v3.0 text says: "A and B are brought under a shared validity demand D_joint."

**From terminology registry [S5] (C-010):**
```
D_joint: Shared validity demand requiring two K-side registration
structures to be assessed under one comparison architecture.
```

### A.2 requires_K_joint — Joint K-Side Check Predicate

**From WP v3.0 section 6.3 [S1] (PUBLISHED SOT):**
```
requires_K_joint(A, B) = 1
  iff  A and B are each valid or provisionally valid within their own K-side
  AND  A and B are brought under a shared validity demand D_joint
  AND  D_joint requires both to be assessed as parts of the same registration target,
       history, counterfactual claim, or validity claim
  AND  truth of D_joint cannot be evaluated while leaving A and B in fully independent K-sides
  AND  preserving D_joint requires a K_joint in which A and B are jointly valid.

requires_K_joint(A, B) = 0
  iff  no shared D_joint is imposed, or D_joint can be evaluated without embedding A and B
       into one candidate K_joint.
```

Operational sufficient conditions A-E for =1 and C-E for =0 are provided (Conditions A, B, B2 for =1; C, D, E for =0).

### A.3 AdmJoint — Admissible Joint K-Space

**From WP v3.0 section 6.3 [S1] (PUBLISHED SOT):**
```
AdmJoint(K_joint; A, B) = 1
  iff  there exist embeddings i_A: A -> K_joint and i_B: B -> K_joint such that:
    (i)   embeddings preserve act, outcome, cert, registration time/order, validity;
    (ii)  self-certification remains intrinsic to each embedded act;
    (iii) Conditions 1-6 remain satisfied for each embedded structure;
    (iv)  no required registration-state update in K_joint invalidates either embedded
          structure while both are still claimed as jointly valid;
    (v)   K_joint does not import an external certifier as source of self-certification.
```

**Conditions 1-6 (Valid Registered Measurement, from WP v2.0 section 3):**
1. Physical (rho-side occurrence)
2. Admission (crosses K-side boundary)
3. Process membership (in R)
4. Self-certification (sigma_R(M_X) = 1)
5. Default validity (V(M_X) = 1)
6. Non-invalidation (no later M' contradicts M_X)

### A.4 K6 Condition (c) — The scope(D_joint) Reference

**From K_Space_Axiomatization.md [S3, S4] (K6 formal block):**
```
Auth(k2 -> k1, C_K) = 1  iff  all of:
  (a)  C_K-sphere(k1) = C_K-sphere(k2)      [both belong to same C_K]
  (b)  V(k2) = 1                             [k2 not invalidated at check time]
  (c)  k1 in scope(D_joint)                  [k1's claim falls within D_joint scope]

  where:
    C_K-sphere(k) is the comparison context that k belongs to.
    scope(D_joint) is the set of registration acts whose claims D_joint demands
    joint validity evaluation for.
```

### A.5 C_K Definition

**From WP v3.0 section 6.3 [S1]:**
```
C_K is a minimal shared frame in which two registration acts are evaluated
for compatibility. C_K requires:
  (a) both acts admitted into the same comparison domain;
  (b) both indexed to the same registration target;
  (c) comparison does not presuppose joint validity.

C_K is strictly weaker than AdmJoint: it enables comparison without requiring
that joint validity be preserved. AdmJoint requires C_K but adds preservation
of Conditions 1-6 and validity for both sides.
```

---

## PART B — ROUND 1: INCONSISTENCY CANDIDATE IDENTIFICATION

### B.1 Define — What Are We Auditing?

We are auditing the internal consistency of three Level 4 concepts: D_joint, AdmJoint conditions (i)-(v), and requires_K_joint predicate. "Internal consistency" means: no undefined term is used in a definition; no two definitions contradict each other; no definitional circularity exists; and the same concept has the same meaning across all SOT documents.

### B.2 Trace — Systematic Cross-Reference Scan

The following table traces every use of D_joint, AdmJoint, and requires_K_joint across SOT documents:

| Concept | [S1] v3.0 section 6.3 | [S2] v2.0 section 4.3 | [S3/S4] K_Space_Axiom | [S5] Registry | Notes |
|---------|----------------------|----------------------|----------------------|--------------|-------|
| D_joint formal def | Implicit (in rKJ) | Explicit (3-arg predicate) | Referenced only | 1-line summary | **Arch param dropped in v3.0** |
| requires_K_joint | 5 conditions | 5 conditions + EWF variant | Referenced (L4 section 4.3) | F-EWF-002 | **EWF 4-arg variant dropped in v3.0** |
| AdmJoint (i)-(v) | 5 conditions | 5 conditions (more detailed) | "conditions (i)-(v)" | F-EWF-000 (compressed) | **Consistent count; detail differs** |
| scope(D_joint) | NOT DEFINED | NOT DEFINED | Used in K6(c) | NOT DEFINED | **UNDEFINED CONCEPT** |
| C_K-sphere | NOT DEFINED | NOT DEFINED | Used in K6(a) | NOT DEFINED | **Used only in K6** |

### B.3 Isolate — 7 Inconsistency Candidates

#### I-01: `scope(D_joint)` — UNDEFINED CONCEPT (HIGH)

**Symptom:** K6 condition (c) says `k1 in scope(D_joint)`. The field comment says `scope(D_joint) is the set of registration acts whose claims D_joint demands joint validity evaluation for`. But:
- D_joint is defined as a predicate `D_joint(A, B, Arch) in {0,1}`
- A predicate does not have a "scope" in the set-of-acts sense
- `scope(D_joint)` is used in a FROZEN axiom (K6) but is never formally defined in any Level 4 document [S1]-[S7]

**5-Whys:**
1. Why is `scope(D_joint)` undefined? → Because D_joint was defined as a predicate, but K6 needs it to identify a set of acts.
2. Why does K6 need a set of acts? → Because Auth(k2->k1, C_K) needs to check whether k1's claim is within the validity demand's purview.
3. Why not define D_joint's scope in the D_joint definition itself? → Because the formal definition of D_joint is already extremely thin (essentially a label).
4. Why is D_joint's definition thin? → Because all the structural work is done by requires_K_joint and operational conditions A-E; D_joint acts as a conceptual anchor rather than a formal predicate.
5. **Root cause:** D_joint was introduced as a conceptual primitive (the "shared validity demand") without completing its formalization. `scope(D_joint)` exposes this gap: it requires D_joint to have set-like structure that its predicate definition does not provide.

**VVV-QMRF-EX compass:** phi-O5 [S6] identifies "C_K sphere membership and D_joint scope are K-side EPISTEMIC concepts with NO B(H) analogue" — this confirms the concept exists but also confirms it has no operator-algebraic encoding. The compass tells us scope(D_joint) is structurally important but formally under-defined.

#### I-02: D_joint Formal Thinness / Definitional Loop (MEDIUM)

**Symptom:** D_joint and requires_K_joint form a near-circular definition pair:
- requires_K_joint = 1 iff ... "brought under a shared validity demand D_joint"
- D_joint = 1 iff ... "Arch demands shared validity"
- What constitutes Arch "demanding shared validity"? → Operational conditions A-E
- But conditions A-E are defined as "Operational sufficient conditions for requires_K_joint = 1"

This creates a definitional chain: requires_K_joint -> D_joint -> Arch -> operational conditions -> requires_K_joint. The last step closes a loop.

**5-Whys:**
1. Why the loop? → D_joint and requires_K_joint were introduced together in WP v2.0 section 4.3 without independent formal content for D_joint.
2. Why no independent content? → The distinction between "there is a demand" (D_joint) and "the demand requires a joint space" (requires_K_joint) is subtle and possibly collapses in practice.
3. Why does it collapse? → Every operational sufficient condition A-E is stated for requires_K_joint, not for D_joint. D_joint has no operational conditions of its own.
4. Why not give D_joint its own operational conditions? → Because the framework treats D_joint as the structural input and requires_K_joint as the derived predicate — but the derivation is never shown; they're defined simultaneously.
5. **Root cause:** D_joint and requires_K_joint were designed as a conceptual pair (demand -> requirement) but formalized as co-defined predicates where one (D_joint) has no independent operational content beyond what the other (requires_K_joint) already expresses. This is not a logical contradiction — it's a definitional redundancy that makes D_joint a thin wrapper.

#### I-03: C_K-sphere(k) vs scope(D_joint) — Dual Membership (MEDIUM)

**Symptom:** K6 uses TWO different membership concepts for what appears to be the same underlying question: "is this registration act in the comparison context?"
- K6(a): `C_K-sphere(k1) = C_K-sphere(k2)` — comparison context membership
- K6(c): `k1 in scope(D_joint)` — validity demand scope membership

The relationship between C_K-sphere and scope(D_joint) is never formally stated. Questions that arise:
- Can k be in C_K-sphere but NOT in scope(D_joint)?
- Can k be in scope(D_joint) but NOT in C_K-sphere?
- Are they always co-extensive? If so, why two different checks?

From C_K definition [S1]: "C_K enables comparison without requiring joint validity preservation." And: C_K exists iff requires_K_joint = 1 (from K5 firing precondition). And requires_K_joint = 1 iff D_joint is imposed.

So: requires_K_joint = 1 => C_K exists AND D_joint is imposed. But does that guarantee C_K-sphere = scope(D_joint)?

**5-Whys:**
1. Why two membership concepts? → C_K-sphere was introduced for comparison context; scope(D_joint) was introduced for authority scope. They govern different aspects of K6.
2. Why different aspects? → C_K-sphere answers "are these two acts in the same comparison frame?" scope(D_joint) answers "is the earlier act's claim within the validity demand's scope?"
3. Why might they diverge? → A registration act could be in the comparison context (C_K-sphere) but its specific claim might fall outside what D_joint demands to evaluate (scope(D_joint)). For example: D_joint demands joint evaluation of outcome claims but not timing claims.
4. Why is this relationship not documented? → The distinction between comparison frame membership and claim-scope membership emerged during axiomatization (K6 was written after WP v2.0) but was never back-ported to the Level 4 definitions.
5. **Root cause:** K6 introduced granularity (separating comparison context membership from claim-scope membership) that Level 4 definitions do not reflect. The Level 4 definitions treat C_K as a single concept; K6 splits it into two checks without updating the upstream definitions.

#### I-04: K6(c) Asymmetric Scope Check (LOW)

**Symptom:** Auth(k2 -> k1, C_K) only checks `k1 in scope(D_joint)`, not `k2 in scope(D_joint)`. The asymmetry is noted in K6's source ([S3] line 446-448) but not explained.

**5-Whys:**
1. Why only k1? → Because authority is directional: k2's authority to invalidate k1 depends on whether k1's claim is within D_joint's scope.
2. Why not check k2? → k2 is the later act providing the contradiction. If k2 is in the same C_K as k1 (K6(a)), and k2 is valid (K6(b)), then k2's authority over k1 turns on whether k1's claim is within scope — not on whether k2's claim is within scope.
3. Why is this structurally coherent? → The later act k2's role is to contradict k1. The earlier act k1's role is the one whose validity is challenged. The scope check protects k1 from invalidation by acts that are in the same comparison context but whose authority doesn't extend to k1's specific claim type.
4. Why no explicit justification? → The justification is implicit in the directional nature of Auth(k2->k1) — but implicit justification in a frozen axiom is insufficient.
5. **Root cause:** The asymmetry is structurally justified (directional authority) but the justification exists only in the structural logic, not in the documentation. This is a documentation gap, not a logical defect.

#### I-05: AdmJoint (ii)/(iii) Redundancy (LOW)

**Symptom:** AdmJoint condition (ii) states "self-certification remains intrinsic to each embedded act." AdmJoint condition (iii) states "Conditions 1-6 remain satisfied for each embedded structure." Condition 4 of Conditions 1-6 IS self-certification. So self-certification is covered twice.

**5-Whys:**
1. Why the redundancy? → Self-certification (Condition 4) is architecturally central to VVV-QMRF (it's what terminates the von Neumann regress).
2. Why call it out separately? → Because embedding could theoretically break self-certification by introducing an external certifier (which is what condition (v) also guards against). Condition (ii) emphasizes that embedding must preserve the intrinsic nature of cert.
3. Why not merge (ii) into (iii)? → The separate clause signals architectural priority, not logical necessity. It's rhetorical structure, not logical structure.
4. Does the redundancy cause any logical problem? → No. A condition being stated twice doesn't create contradiction — it's just redundant enforcement.
5. **Root cause:** Intentional redundancy for architectural emphasis. Not a defect.

#### I-06: D_joint Arch Parameter Drift (MEDIUM)

**Symptom:** WP v2.0 [S2] defines `D_joint(A, B, Arch) in {0, 1}` with Arch as an explicit third argument. WP v3.0 [S1] references D_joint without the Arch parameter. The Arch concept is still present (operational conditions A-E describe specific architectures), but the formal notation dropped it.

**5-Whys:**
1. Why was Arch dropped? → v3.0 streamlined the formal notation; the Arch parameter was implicit in the operational conditions.
2. Why does this matter? → Without Arch, D_joint(A, B) looks like a 2-place predicate, but its truth value depends on the comparison architecture (EWF vs separable vs independent bookkeeping).
3. Why not restore it? → The v3.0 text still says "comparison architecture" in prose — the concept wasn't lost, only the notation changed.
4. Why is this still a gap? → K6(c) references `scope(D_joint)` — if D_joint doesn't take Arch as a parameter, then `scope(D_joint)` is ambiguous: scope under WHICH architecture?
5. **Root cause:** The Arch parameter was removed from notation without checking downstream dependencies. K6(c) `scope(D_joint)` implicitly depends on a specific Arch to determine which acts are in scope. Without Arch, scope(D_joint) is underspecified.

#### I-07: requires_K_joint Condition 5 — Definitional Self-Reference (LOW)

**Symptom:** The 5th condition for requires_K_joint = 1 is: "preserving D_joint requires a K_joint in which A and B are jointly valid." But this is essentially the definition of requires_K_joint itself — "a K_joint is required." This looks circular.

**Careful reading resolution:** The condition is: "to evaluate whether D_joint holds, you need to construct a candidate K_joint." It's a statement about EVALUATION METHODOLOGY, not about the truth of requires_K_joint. It says: D_joint's truth conditions make reference to joint validity, so checking D_joint requires building K_joint. This is structurally coherent — it's saying "the question can only be answered by attempting the construction."

**5-Whys:**
1. Why does this look circular? → Because "requires K_joint" appears in both the predicate name and one of its defining conditions.
2. Why isn't it actually circular? → The condition states an epistemic fact about evaluation, not a logical fact about the predicate. "To check X, you need Y" is not the same as "X is defined as Y."
3. Why is the phrasing confusing? → The condition is stated in definitional form ("iff ... AND preserving D_joint requires...") but is actually a meta-statement about evaluation procedure.
4. Why not separate it? → The definition blends object-level conditions (A,B valid, D_joint imposed) with methodology-level conditions (evaluation requires K_joint).
5. **Root cause:** The definition mixes object-level and methodology-level conditions. Structurally coherent but notationally imprecise.

---

## PART C — ROUND 2: 5-WHYS DEEP DIVE (CONFIRMED DEFECTS ONLY)

### C.1 I-01: `scope(D_joint)` — Deep Dive

```
WHY-1: Why is scope(D_joint) used without definition?
  -> K6 was written during axiomatization (post-WP v2.0) and introduced
     the concept organically. The field comment in K6 is the CLOSEST thing
     to a definition, but it's a comment, not a formal definition.

WHY-2: Why wasn't it added to Level 4 definitions?
  -> Level 4 was declared frozen (2026-05-31) before this audit caught the gap.
     K6's use of scope(D_joint) created a dependency that Level 4 doesn't satisfy.

WHY-3: Why does K6 need this concept at all?
  -> Auth(k2->k1, C_K) needs to ensure k1's claim is the TYPE of claim that
     D_joint is about. Without scope(D_joint), any act in C_K could be
     invalidated by any other act in C_K — the scope check narrows this.

WHY-4: Why can't C_K-sphere serve this role alone?
  -> C_K-sphere identifies WHICH comparison context an act belongs to.
     scope(D_joint) identifies WHICH CLAIMS within that context are subject
     to the validity demand. An act could be in C_K (for comparison purposes)
     but its specific claim might be outside D_joint's scope.

WHY-5 (Root Cause):
  -> K6 introduced a 2-level membership model (C_K-sphere for comparison
     context, scope(D_joint) for claim-type filtering) that was never
     formalized in Level 4. The concept is structurally necessary but
     formally orphaned. Fix: either define scope(D_joint) in Level 4 section 4.3,
     or fold it into C_K-sphere with explicit co-extensiveness.
```

**RCA Score I-01: 4.7/5** — Confirmed structural defect. K6(c) depends on an undefined concept. Fix required.

### C.2 I-03: C_K-sphere vs scope(D_joint) — Deep Dive

```
WHY-1: Why are there two membership concepts in K6?
  -> K6(a) checks "same comparison frame" — structural co-location.
     K6(c) checks "claim within validity demand scope" — semantic relevance.
     These are different questions.

WHY-2: Why is the relationship undocumented?
  -> The K_Space_Axiomatization was built bottom-up (axioms first, then
     bridge theorems). C_K-sphere and scope(D_joint) emerged during K6
     formalization but the upstream Level 4 definitions weren't updated.

WHY-3: Can they diverge in practice?
  -> Hypothetically yes: an act k could be in C_K (admitted to comparison)
     but its claim type could be outside D_joint's scope. Example: D_joint
     only demands joint evaluation of outcome claims, but k's timing claim
     is also in C_K. Then k in C_K-sphere but k not-in scope(D_joint) for the
     timing claim (though k in scope(D_joint) for the outcome claim).

WHY-4: Is this divergence tested in any concrete model?
  -> No. All concrete models (Proietti, Bong, BB, FR) only check outcome
     claims. The distinction between claim types has never been exercised.
     This means I-03 is a LATENT defect — it doesn't affect current fits
     but could cause misclassification in future scenarios.

WHY-5 (Root Cause):
  -> The 2-level model is architecturally correct (comparison frame != claim scope)
     but was introduced in K6 without updating the upstream C_K/D_joint
     definitions. Fix: add explicit relationship statement to Level 4:
     "C_K-sphere(k) is the comparison context containing k. scope(D_joint)
     is the subset of claims within C_K that D_joint demands to evaluate.
     In all current operational conditions A-E, C_K-sphere = scope(D_joint)
     for outcome claims (the only claim type currently modeled)."
```

**RCA Score I-03: 4.3/5** — Confirmed structural defect. Documentation fix required.

---

## PART D — ROUND 3: VERIFICATION, SCORING, AND SYNTHESIS

### D.1 Aggregate Scoring

| Candidate | Define | Trace | Isolate | Fix | Verify | **Total** | Verdict |
|-----------|--------|-------|---------|-----|--------|-----------|---------|
| I-01 scope(D_joint) undefined | 5.0 | 5.0 | 4.5 | 4.5 | 4.5 | **4.7** | STRUCTURAL DEFECT |
| I-02 D_joint thinness | 4.5 | 4.0 | 4.5 | 4.0 | 4.0 | **4.2** | THIN-DEFINITION |
| I-03 C_K-sphere vs scope | 4.5 | 4.5 | 4.5 | 4.0 | 4.0 | **4.3** | STRUCTURAL DEFECT |
| I-04 K6(c) asymmetry | 3.5 | 3.5 | 3.0 | 3.0 | 3.0 | **3.2** | BENIGN |
| I-05 AdmJoint (ii)/(iii) redundant | 3.0 | 2.5 | 3.0 | 3.0 | 2.5 | **2.8** | BENIGN |
| I-06 Arch parameter drift | 4.0 | 4.5 | 4.0 | 3.5 | 4.0 | **4.0** | THIN-DEFINITION |
| I-07 rKJ condition 5 self-ref | 3.5 | 3.5 | 3.5 | 3.5 | 3.5 | **3.5** | THIN-DEFINITION |

**Weighted aggregate (by severity): 4.1/5**

### D.2 Adversarial Verification

**Challenge 1: "Are I-01 and I-03 actually the same defect?"**
-> NO. I-01 is about an undefined term (`scope(D_joint)` has no formal definition anywhere). I-03 is about the relationship between two defined-or-semi-defined terms (C_K-sphere has a field comment; scope(D_joint) has a field comment; neither has formal Level 4 status). They're distinct: I-01 is about existence of definition; I-03 is about relationship between definitions.

**Challenge 2: "Does fixing I-01 automatically fix I-03?"**
-> PARTIALLY. Defining scope(D_joint) formally would give it a definition, resolving I-01. But the relationship between C_K-sphere and scope(D_joint) (I-03) would still need explicit documentation.

**Challenge 3: "Do any of these defects affect current K9_E or BB/FR fits?"**
-> NO. All current concrete models use requires_K_joint and AdmJoint at the predicate level — they ask "does K_joint exist or fail?" They never exercise the internal structure of Auth(k2->k1, C_K) at the granularity where scope(D_joint) matters. The defects are latent: they would surface only in scenarios where different claim types (outcome vs timing vs certification) need different scope treatment.

**Challenge 4: "Could fixing these defects change any existing conclusion?"**
-> NO. The defects are in precision of definition, not in truth value of any existing claim. No requires_K_joint classification, AdmJoint evaluation, or K5 firing conclusion would change.

### D.3 Relationship to Known Blockers

From `RCA_P3_P4_Relationship_Blockers_2026_06_01.md`:
- **B_PHI:** "C_K sphere membership and D_joint scope are K-side EPISTEMIC concepts with NO B(H) analogue" — this is exactly the same family as I-01/I-03. The phi-map blocker is that these K-side epistemic concepts can't be encoded in B(H). Our audit confirms these concepts exist and are structurally necessary — but also reveals they're formally under-defined even within K-space, before any attempt at B(H) encoding.
- **Implication:** B_PHI is not just about the K->B(H) boundary — it's also about internal K-side definitional incompleteness. Before asking "can we map scope(D_joint) to B(H)?" we need to first answer "what exactly IS scope(D_joint)?"

### D.4 Level 4 Unfreeze Assessment

Per `vvv_qmrf_meta_architecture_level_4_unfreeze_gate.md`:

| Gate | I-01 | I-03 |
|------|------|------|
| G1 (RCA isolated) | YES — Root cause in K6/Level 4 boundary | YES — Root cause in K6/Level 4 boundary |
| G2 (Predicate named) | YES — scope(D_joint) — but it's NOT a Level 4 predicate, it's a K6 consumer | YES — C_K-sphere + scope(D_joint) relationship |
| G3 (Downstream mapped) | YES — K6(c), potentially K5 firing scope | YES — K6(a)(c), Auth evaluation |
| G4 (Minimal fix) | YES — Add scope(D_joint) definition to Level 4 or K6 | YES — Add relationship statement |
| G5 (Verification path) | YES — Verify K6 text still compiles | YES — Verify against concrete model |

**Decision:** These fixes are in the K6->Level 4 interface, not in Level 4 semantic content. Level 4 does not need to be unfrozen — the gaps are in K6's use of Level 4 concepts, which can be resolved by:
1. Adding a formal `scope(D_joint)` definition (either in Level 4 as a non-semantic clarification, or in K6 as an axiom-local definition)
2. Adding a C_K-sphere <-> scope(D_joint) relationship statement

Neither requires changing D_joint, requires_K_joint, or AdmJoint truth conditions.

---

## PART E — FIX SPECIFICATIONS

### E.1 Fix for I-01: Define `scope(D_joint)`

**Option A (Minimal — add to K6 field comment area):**
```
scope(D_joint; Arch) := {k in K_R : the claim content o(k) is of a type
  that D_joint(., ., Arch) demands joint validity evaluation for}.

For all current operational conditions A-E, scope(D_joint; Arch) includes
all outcome claims (o(k) != empty) of acts in K-spaces brought under D_joint.
```

**Option B (Preferred — add to Level 4 section 4.3 / section 6.3 as non-semantic clarification):**
```
Definition (scope of D_joint, Class D proposed):
For a shared validity demand D_joint under comparison architecture Arch:
  scope(D_joint; Arch) := {k : k's claim type is within the set of
    claim types that D_joint demands to evaluate jointly}.

In all current operational conditions A-E, the only claim type modeled
is outcome claims (o(k) != empty). Extension to non-outcome claims (timing,
certification, validity status) is reserved for future operational conditions.
```

**Recommendation:** Option B. It places the definition where downstream consumers expect to find it (Level 4) without changing any existing Level 4 truth condition. This qualifies as a non-semantic clarification under the unfreeze gate section 6.

### E.2 Fix for I-03: Clarify C_K-sphere <-> scope(D_joint) Relationship

**Add to K6 (or Level 4 C_K definition):**
```
Relationship between C_K-sphere and scope(D_joint):
  C_K-sphere(k) identifies the comparison context that k belongs to
  (structural co-location). scope(D_joint) identifies which claims
  within that comparison context are subject to D_joint's validity
  demand (semantic relevance).

  For all k: k in scope(D_joint) => C_K-sphere(k) is defined
  (scope is always within a comparison context).

  For all current operational conditions A-E:
    C_K-sphere(k) is defined <-> k in scope(D_joint) for outcome claims
    (the two membership concepts are co-extensive for the only claim
    type currently modeled).
```

### E.3 Fix for I-06: Restore Arch Parameter (Optional)

**If adopted:** Restore `D_joint(A, B, Arch)` notation in WP v3.0 section 6.3. This is a notation consistency fix, not a semantic change. The Arch concept is already present in prose.

---

## PART F — VERIFICATION CHECKLIST

| Check | I-01 | I-03 | I-06 |
|-------|------|------|------|
| Is the fix semantic (changes truth conditions)? | NO | NO | NO |
| Is the root cause inside the fixed component? | YES (K6/Level 4 interface) | YES (K6/Level 4 interface) | YES (WP notation) |
| Are affected predicates named? | YES (scope(D_joint)) | YES (C_K-sphere, scope(D_joint)) | YES (D_joint) |
| T1-T3 impacts? | NONE | NONE | NONE |
| ODC_K impacts? | NONE | NONE | NONE |
| Falsification condition impacts? | NONE | NONE | NONE |
| WP claim class preserved? | YES | YES | YES |
| Standard QM boundary preserved? | YES | YES | YES |
| PEER-SYNC required? | YES (both K_Space_Axiom copies) | YES (both copies) | N/A (WP only) |

---

## PART G — FINAL DECISION

```
DECISION: Level 4 INTERNALLY CONSISTENT with 2 confirmed structural defects
          in the K6->Level 4 interface (not in Level 4 definitions themselves).

I-01: scope(D_joint) undefined — STRUCTURAL DEFECT (RCA 4.7/5)
      Fix: Add formal definition to Level 4 section 4.3 as non-semantic clarification.
      Blocks: Nothing currently. Latent defect.

I-03: C_K-sphere vs scope(D_joint) relationship undocumented — STRUCTURAL DEFECT (RCA 4.3/5)
      Fix: Add relationship statement to K6 or Level 4.
      Blocks: Nothing currently. Latent defect.

I-02, I-06, I-07: Thin-definition gaps — monitor, fix opportunistically.
I-04, I-05: Benign — no action needed.

Level 4 freeze: MAINTAINED. Fixes are non-semantic clarifications.
K1-K8 axioms: UNAFFECTED. K6 text unchanged (only comments/definitions added).

NEXT STEP: Apply E.1 (Option B) + E.2 fixes before next WP revision.
```

---

## PART H — CROSS-REFERENCE INDEX

| Reference | Document | Role |
|-----------|----------|------|
| [S1] | `papers/paper_003/VVV-QMRF_Working_Paper_v3.0.md` section 6.3 | Published SOT for Level 4 definitions |
| [S2] | `papers/Testable_Prediction_Section/.../VVV-QMRF_Working_Paper_v2.0.md` section 4.3 | Published reference (v2.0) |
| [S3] | `documents/.../project_vvv_qmrf_class_c/01_axiomatization/K_Space_Axiomatization.md` | Class C working copy (v2.6) |
| [S4] | `documents/.../meta_architecture/K_Space_Axiomatization.md` | Canonical copy (v2.6) |
| [S5] | `documents/.../project_vvv_qmrf_class_c/06_references/VVV_QMRF_research_terminology.md` | Terminology registry |
| [S6] | `documents/.../meta_architecture/phi_O5_n_observer_extension_v0_1.md` | phi-O5 N-observer (v0.7) |
| [S7] | `documents/.../project_vvv_qmrf_class_c/09_Fitting_Baumann_Brukner/BB_VVV_fit_plan.md` | BB fit plan (v1.4) |
| [G1] | `documents/.../project_vvv_qmrf_class_c/01_axiomatization/vvv_qmrf_meta_architecture_level_4_unfreeze_gate.md` | Level 4 unfreeze governance |
| [G2] | `documents/.../project_vvv_qmrf_class_c/04_governance/RCA_P3_P4_Relationship_Blockers_2026_06_01.md` | P3-P4 blockers RCA |

---

*RCA Level 4 Internal Consistency Audit — 2026-06-01. 3-Round RCA 4.1/5. Level 4 remains frozen. 2 structural defects identified in K6->Level 4 interface. Fixes are non-semantic clarifications.*
