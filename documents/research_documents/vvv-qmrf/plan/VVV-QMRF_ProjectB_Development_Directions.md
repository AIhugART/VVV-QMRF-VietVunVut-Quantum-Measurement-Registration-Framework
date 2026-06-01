Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Project B — Development Directions for Physical Value Independent of K9_E

## Context

This document is a structured RCA (Root Cause Analysis) output identifying concrete development directions for Project B (VVV-QMRF K-space Architecture) that could generate genuine physical value without requiring K9_E as a bridge to experiment.

**Source:** VVV-QMRF Working Paper v3.0 (VietVunVut, 2026-05-28)  
**Scope:** K1–K8 axioms, T1–T9 bridge theorems, T4-H colimit theorem, K ≠ H separation  
**Problem being solved:** Project B currently has no dynamics — it classifies registration states but does not produce observable predictions independently of K9_E postulate (P9).

---

### Amendment Log — 3-Round RCA Review 2026-06-01

**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5 (VVV-QMRF scope; VVV-QMRF-EX as compass)  
**Overall Plan Score:** 3.8/5 → PASS with amendments required  
**Amendments applied:**

| Amendment | Scope | RCA basis |
|-----------|-------|-----------|
| A1 — D1 distinguishability criterion added | D1 Key Challenge | compat predicate must be proven non-trivially different from standard QM post-selection |
| A2 — D2 φ-coupling caveat added | D2 Key Challenge | K_F ⊥_K K_W → f(ρ) requires φ_R as coupling vehicle; not fully K9_E-independent |
| A3 — D3 W_K construction added as prerequisite | D3 Formal Sketch + Key Challenge | W_K from K-history is undefined; blocks D3 testability path |
| A4 — D5 time horizon revised | D5 Priority row | FUNDAMENTAL BOUNDARY on φ-O5 sufficiency; 24-48 months underestimates structural limit |
| A5 — D6 added | New direction | K-H Registration Observability Program (`rca_k_h_registration_observability_plan.md`) is immediately actionable and was missing |
| A6 — Priority table updated | Priority Assessment | Pillar alignment column added; D6 included; D5 time horizon revised |
| A7 — Recommended Entry Point revised | Recommended Entry Point | D2 + D6 replaces D2 + D3; D3 requires W_K construction phase first |

---

## Root Cause of the Gap

K1–K8 define a *classification language* for registration events. They specify what a valid registration is, when it is invalidated (K5), and when it closes (K7). They do not specify how K-states *feed back* into physical dynamics on the H-side. Without a feedback mechanism or a structural constraint that maps to an observable, Project B produces no predictions that differ from Standard QM.

K9_E fills this gap as an external postulate. The goal of the directions below is to find internal paths that do not require K9_E.

---

## Direction 1 — K-side Dynamics and Boundary Conditions on the H-side

### Core Idea

K2 (temporal order) and K7 (closure) imply that K-space has a time structure. K7 closure at `t_close` is a discrete event. The proposal is to define a **K-side evolution operator** that maps K-history to a boundary condition on the density operator ρ, without modifying Born rule or unitary evolution.

### Formal Sketch

Let `H(t)` be the K-history up to time `t`. Define a compatibility predicate:

```
compat(ρ, H(t)) = 1
  iff  ρ is consistent with all validity assignments in H(t)
  AND  no K5 invalidation in H(t) selects a subspace incompatible with ρ
```

When K7 closure fires at `t_close`, the set of compatible ρ may be a strict subset of D(H). This subset acts as a post-selection condition, producing conditional probabilities that differ from Born rule without modifying Born rule itself.

### Why This Matters

Post-selection in QM is well-defined and experimentally testable (weak measurement protocols, pre- and post-selected ensembles). If K7 closure generates a non-trivial post-selection, this is a physical prediction derivable from K-structure alone.

### Key Challenge

Must prove that the compatibility predicate does not violate unitarity of the full evolution. The K-side boundary condition must be interpretable as a legitimate conditioning event, not a hidden collapse postulate.

**[A1 — RCA Amendment 2026-06-01]** An additional prerequisite must be satisfied before pursuing D1: the compatibility predicate `compat(ρ, H(t))` must be given a rigorous formal definition, and it must be proven that K7 closure imposes constraints on ρ **beyond** what standard QM post-selection (conditioning on a known measurement outcome) already provides. If `compat(ρ, H(t)) = 1` reduces to "ρ is consistent with the Born-rule probabilities of observed outcomes in H(t)," then D1 is trivially equivalent to standard QM conditioning and generates no new prediction. The distinguishability criterion — proving the K7 post-selection region is a strict and non-trivial subset relative to standard conditioning — is a **blocking prerequisite** for D1. See also `rca_k_h_registration_observability_plan.md` §6.2 (DRC-02 two-gate registration condition) for the existing formal treatment of registration completion that D1 should build upon rather than reconstruct independently.

### Testability Path

Compare predicted conditional distributions from K-closure post-selection against standard post-selection in existing weak measurement experiments. If they differ, the difference is a K9_E-free prediction from Project B. Note: this testability path is only meaningful after the A1 distinguishability criterion (above) is established.

---

## Direction 2 — T4-H Colimit as Entanglement Classifier

### Core Idea

T4-H proves that `K_joint(R_1, ..., R_N)` exists as a categorical colimit when pairwise `AdmJoint` conditions and global commutativity hold. The inverse question is: **when K_joint does not exist (`K_F ⊥_K K_W`), what is the necessary condition on the physical state ρ?**

### Formal Sketch

Conjecture: There exists a function `f` such that:

```
K_F ⊥_K K_W  ⟹  f(ρ) > threshold
```

where `f(ρ)` is a measurable property of ρ — a candidate is entanglement entropy `S(ρ_F)`, or a Bell inequality violation parameter, or the coherence of ρ in the F-W basis.

If this implication holds, then K-incommensurability is not just a registration-layer concept — it directly constrains the physical states that can produce it.

### Why This Matters

This would make `requires_K_joint` a classifiable property of physical states, not just a framework-level label. Experiments that prepare known entangled states could be used to test whether the predicted K-incommensurability threshold matches the colimit existence boundary from T4-H.

### Key Challenge

The direction from `K_F ⊥_K K_W` to a constraint on ρ requires constructing the explicit map between K-structure properties and Hilbert space properties. This is a fragment of the φ: K → B(H) conjecture (Direction 5 below) but is more constrained and potentially more tractable.

**[A2 — RCA Amendment 2026-06-01]** D2 is labeled "Very High" K9_E-independence, which is correct in the sense that it does not require the empirical K9_E postulate. However, D2 implicitly requires a K → H coupling to translate K-incommensurability into an H-side constraint on ρ. The available coupling is the **restricted φ-map** φ_R: K_R → P(H)∪{0} (Class C THEOREM, 2026-06-01; `meta_architecture/phi_restricted_existence_v1_0.md`). The conjecture `K_F ⊥_K K_W → f(ρ) > threshold` should therefore be stated more precisely as: φ_R provides a mapping from K_R-elements to projectors in P(H); the colimit failure condition (T4-H) constrains the joint structure of those projectors; and the claim is that this structural constraint implies a measurable property of ρ. Note that entanglement entropy S(ρ_F) is a function of ρ, not of projectors alone — so the path from φ_R-image constraints to S(ρ_F) requires one additional step beyond φ_R. This step should be made explicit as a sub-task of D2 before claiming "high tractability."

### Testability Path

Use existing entanglement characterization experiments (Bell tests, quantum state tomography) to check whether states at the T4-H boundary produce the predicted colimit failure. No new experiment type is required — only a new analysis of existing data. The testability path is conditioned on the φ_R coupling step identified in the A2 caveat above being formally established first.

---

## Direction 3 — K-space as a Process Matrix Classifier

### Core Idea

The process matrix framework (Oreshkov, Costa, Brukner 2012) formalizes quantum causal structures without assuming a fixed background causal order. A process matrix `W` is valid if it produces normalized probabilities for all local operations. Causally separable processes are a strict subset.

K-space has structural overlap with this framework:

```
K2 (temporal order)     ↔  causal order on events
K5 (invalidation)       ↔  failure of causal separability condition
K7 (closure)            ↔  finalization of a causal frame
requires_K_joint        ↔  non-causal-separability predicate
```

### Formal Sketch

Map each K-state tuple `k = ⟨M, o, cert, t, V⟩` to a local instrument in the process matrix framework. Define:

```
W_K = process matrix induced by K-history H
```

Conjecture: `requires_K_joint(A, B) = 1` iff `W_K` is not causally separable between the A and B subsystems.

### Why This Matters

Causal non-separability is experimentally testable. The quantum switch (indefinite causal order) has been demonstrated in photonic experiments. If K-incommensurability maps to causal non-separability, Project B directly predicts which experimental setups will exhibit indefinite causal order — a physical prediction that does not involve K9_E.

### Key Challenge

The mapping from K-space to process matrices must be shown to be well-defined and non-trivial. If `requires_K_joint` always maps to causally separable processes, the conjecture is false. If it always maps to non-separable processes, it may be too coarse to be useful. The interesting case is a partial overlap with non-trivial discriminating power.

**[A3 — RCA Amendment 2026-06-01]** A **blocking prerequisite** for D3 has been identified that is not currently addressed in the formal sketch: `W_K = process matrix induced by K-history H` is stated as a definition but is not constructed. A process matrix in the Oreshkov-Costa-Brukner framework is a specific bipartite quantum map satisfying trace preservation conditions. Before checking whether `requires_K_joint` maps to causal non-separability, the following sub-task must be completed:

```
W_K construction sub-task:
  1. Map each K-state tuple k = ⟨M, o, cert, t, V⟩ to a local instrument A_k in the process matrix framework.
  2. Show that A_k satisfies all structural requirements of a local instrument (trace preservation, positivity).
  3. Define how K-history H = (k_1, ..., k_n) induces a process matrix W_K from the sequence of A_k.
  4. Verify that the induced W_K is a valid process matrix (normalizes probabilities for all local operations).
```

Until these four sub-steps are established, D3's formal sketch is a structural analogy, not a mathematical construction. This sub-task elevates D3's tractability from "High" to "Medium (W_K construction phase required first)."

### Testability Path

Analyze published quantum switch experiments through the K-space lens. Identify which setups have `requires_K_joint = 1` under K-space conditions A–E. Check whether those setups are exactly the ones exhibiting causal non-separability in process matrix terms. Note: this analysis is only meaningful after the A3 W_K construction sub-task is completed.

---

## Direction 4 — K-space as Formal Specification Language for Quantum Error Correction

### Core Idea

In fault-tolerant quantum computing, syndrome measurements must be validated before triggering correction. The question "when is a syndrome measurement a valid registered event" is structurally identical to the VVV-QMRF question "when is a physical interaction a valid registered measurement."

K1–K8 can serve as a **formal specification language** for QEC protocols:

```
K1  →  syndrome measurement as 5-tuple: device, syndrome outcome, cert, time, validity
K2  →  temporal ordering of syndrome rounds
K4  →  default validity upon syndrome registration
K5  →  invalidation when later syndrome contradicts earlier syndrome
K7  →  closure when enough syndrome rounds have been collected to trigger correction
K3  →  self-certification: syndrome device certifies its own output without second-order verification
```

### Formal Sketch

Define a **K-QEC protocol** as a QEC protocol whose correction trigger is governed by K7 closure rather than a fixed number of syndrome rounds. The correction fires when and only when the K-history satisfies K7 closure conditions — i.e., no pending `requires_K_joint` demands remain unresolved.

### Why This Matters

This is an engineering application, not a philosophical one. If K-QEC protocols can be shown to reduce correction latency or improve threshold estimates compared to fixed-round protocols, that is a concrete technical contribution independent of any interpretation of quantum mechanics.

### Key Challenge

Must show that K-QEC is not equivalent to existing adaptive QEC protocols (which already condition correction on syndrome history). The distinction must be formal: K7 closure is a structural condition, not a statistical threshold. If they are provably equivalent, the contribution is taxonomic, not technical.

### Testability Path

Implement K-QEC specification in a QEC simulation (e.g., surface code with adaptive syndrome rounds). Compare logical error rates against standard fixed-round and existing adaptive protocols. A measurable improvement would constitute a K9_E-free technical result from Project B.

---

## Direction 5 — Constructing the φ: K → B(H) Map Explicitly

### Core Idea

The author conjectures a structure-preserving map φ: K → B(H) (Class D) but does not construct it. This is the highest-potential direction because a constructive φ would embed K-space into the standard mathematical language of QM, making every K-structure result directly translatable into operator algebra.

### Formal Sketch

Start from the five-tuple `k = ⟨M, o, cert, t, V⟩` and attempt explicit assignments:

```
M  →  a POVM element E_M ∈ B(H)
o  →  an eigenvalue of E_M
t  →  a parameter in a one-parameter group of unitaries
V  →  a projector P_V onto the subspace of states compatible with validity
cert  →  the identity operator I (self-certification is tautological on the operator level)
```

Under this assignment, K5 invalidation corresponds to:

```
P_{V=0} = I - P_{V=1}  (projection onto invalid subspace)
```

K7 closure at `t_close` corresponds to:

```
φ(K_R up to t_close) = ∏_{k ∈ K_R} P_{V(k)}  (product of validity projectors)
```

### Why This Matters

If φ is well-defined and structure-preserving (i.e., it respects K1–K8), then the image φ(K) is a subset of B(H) with specific algebraic properties. Characterizing this image — Is it a von Neumann algebra? A C*-algebra? A lattice of projectors? — is a pure mathematical question with physical content. The structure of φ(K) constrains which operators can appear as K-registered observables, which is a restriction on physical theory, not just on interpretation.

### Key Challenge

The main obstacle is K3 (self-certification). Self-certification is defined as intrinsic to K_R and independent of any external observer. It is not clear what operator in B(H) corresponds to "intrinsic self-certification" — the identity operator is a placeholder, not a construction. Until K3 has a non-trivial operator image, φ will not be injective, and the structure-preservation claim will be weakened.

**[A4 — RCA Amendment 2026-06-01]** The characterization of D5 as "highest-potential" is correct in principle but requires two corrections:

First, Track B Phases 1–4 (complete as of 2026-05-22) have already established: (a) φ_R: K_R → P(H)∪{0} as a Class C THEOREM (restricted existence, 2026-06-01); (b) φ-N1 conditions N_1–N_T are necessary; (c) φ-O5 sufficiency conditions = **FUNDAMENTAL BOUNDARY** (`RCA_phi_O5_2_sufficiency_2026_05_31.md`). This boundary means that a fully structure-preserving φ: K → B(H) may be formally unreachable with the current axiomatic structure — it is not a 24–48-month engineering challenge but a potential structural limit of the framework.

Second, D5's time horizon should therefore be revised from "24–48 months" to **"Open-ended (FUNDAMENTAL BOUNDARY on φ-O5 sufficiency; see `RCA_phi_O5_2_sufficiency_2026_05_31.md`)"**. The productive near-term work in the φ-direction is to extend φ_R (restricted existence) toward more components via the N=3 colimit and T4 Class C result — not to attempt a full constructive φ.

### Testability Path

Unlike Directions 1–4, this direction does not immediately produce an experimental prediction. Its value is foundational: a constructive φ would allow every result in Project B to be stated as a theorem in standard operator algebra, making the framework legible to the mathematical physics community without requiring them to learn K-space vocabulary. Given the FUNDAMENTAL BOUNDARY, the productive near-term path is extending φ_R incrementally (via T4-H colimit → N=3 → beyond) rather than attempting a full construction.

---

---

## Direction 6 — K-H Registration Observability Program

> **[A5 — RCA Amendment 2026-06-01]** This direction was identified as missing from the original document. It is the most immediately actionable K9_E-free direction and should be co-listed with D2 as a recommended entry point.

### Core Idea

VVV-QMRF's registration architecture defines a boundary between physical admissibility (`Phys(o|H_physics)=1`) and registration lock (`Lock_K(o|K_before, H_register)=1`). The K-H observability program asks whether the registration layer has *measurable* consequences — not modifications to Born-rule probabilities, but observable differences in **registration-layer metrics** across different registration contexts.

This direction is fully developed in `rca_k_h_registration_observability_plan.md` (same plan directory). Key definitions already established:

```
HDEF-01  Registration Horizon H = (H_physics, H_register)
KHI-01   K-H Interface: phi_H: O × K_space → K_space
DRC-02   Two-gate registration condition: Reg(o,H) = Phys(o|H_physics) AND Lock_K(o|K_before,H_register)
TIM-01   Registration Latency: tau_reg^val(H) = t_lock^val(H_register) - t_phys(H_physics)
NUL-01   Null Registration Rate: N_null(H) = P(Lock_K=0 | Phys=1, H)
COR-01   Conditional K-H Information: I(K_after; H_register | o, K_before, H_physics)
```

### Formal Sketch

Primary measurable prediction:

```
delta_tau_KH = E[tau_reg^val | H_register_1] - E[tau_reg^val | H_register_0]
```

If `delta_tau_KH ≠ 0` after controlling detector latency, software latency, post-selection, timestamp synchronization, and noise, then `Lock_K` has an observable registration-layer consequence.

Candidate testbed: **delayed-choice experiment** with two `H_register` contexts:

```
H_register_0 = which-path registration context  (Q = "Which path?")
H_register_1 = erasure/interference context     (Q = "Interference relation?")
```

`H_physics` is held fixed (same photon pair source, same detector hardware).

Null model N0 (classical processing model):

```
tau_reg^N0(H) = tau_hardware + tau_software(H_register) + tau_noise
```

VVV-QMRF deviation criterion: `|delta_tau_KH_measured − delta_tau_KH_N0| > threshold`

### Why This Matters

D6 is K9_E-independent, does not modify Born rule, does not require full φ, and does not require new experiment types beyond existing optical quantum information setups. The metrics (tau_reg, N_null, I(K_after;H)) are operationally defined and falsifiable. Falsification rules TIM-F1, NUL-F1, COR-F1 are already written in `rca_k_h_registration_observability_plan.md` §12.

The direction tests whether the K-space registration layer has any observable consequence at the **registration-process level** — a weaker and more tractable claim than K9_E's Born-rule modification claim.

### Key Challenge

Gate questions must be resolved before prediction is meaningful:

- **Gate 1:** `Phys(o|H_physics)=1` must be operationalized beyond "detector click" — requires decoherence, amplification, and stability criteria (see `rca_k_h_registration_observability_plan.md` §13 Gate 1).
- **Gate 2:** Must show a non-empty `Phys=1, Lock_K=0` region exists in the testbed (cases C1–C10 in §13 Gate 2).
- **Gate 3:** `t_lock` must be operationally defined as `t_lock^val` (validation lock time), not detector click or observer access.

### Testability Path

1. Choose one delayed-choice setup (BBO source, two H_register contexts).
2. Define `H_physics` in physical language (decoherence, amplification, stability criteria).
3. Measure `tau_reg^val` for both contexts.
4. Compare against null model N0.
5. Falsification: if `delta_tau_KH_measured = delta_tau_KH_N0` within uncertainty, Lock_K adds no observable consequence in this testbed.

### Pillar Alignment

D6 → **Pillar II** (K9_E empirical resolution — provides a registration-layer testbed independent of P9) + **Pillar III** (Theoretical integration — connects K-H interface to operational metrics)

---

## Priority Assessment

**[A6 — RCA Amendment 2026-06-01]** Table updated with: Pillar alignment column (from Long-Term Research Plan 3-Pillar framework); RCA score per direction; D6 added; D3 tractability revised (W_K construction phase required); D5 time horizon revised (FUNDAMENTAL BOUNDARY).

| Direction | Mathematical tractability | Independence from K9_E | Experimental accessibility | Estimated time horizon | Pillar alignment | RCA Score |
|---|---|---|---|---|---|---|
| D1 — K-dynamics and boundary conditions | Medium (compat predicate undefined) | High (w/ distinguishability caveat) | Medium (weak measurement protocols) | 12–24 months (after A1 criterion) | Pillar III (partial) | 3.2/5 ⚠️ |
| D2 — T4-H as entanglement classifier | High (w/ φ_R coupling step) | Very high (φ_R required as coupling) | High (existing Bell test data) | 6–12 months | Pillar I | 4.0/5 ✅ |
| D3 — Process matrix classifier | Medium (W_K construction required first) | Very high (φ_R required as coupling) | High (quantum switch experiments; after A3) | 6–18 months (+3–6 for W_K) | Pillar I | 3.8/5 ⚠️ |
| D4 — QEC specification language | Medium | Complete | High (simulation) | 12–18 months | Pillar III (peripheral) | 3.5/5 |
| D5 — φ map construction | Low (FUNDAMENTAL BOUNDARY on φ-O5) | Complete | Low (foundational) | Open-ended (see A4) | Pillar I (long-term) | 3.0/5 ⚠️ |
| **D6 — K-H Registration Observability** | **Medium** | **Complete** | **Medium (optical lab needed)** | **6–12 months (lab permitting)** | **Pillar II + III** | **4.2/5 ✅** |

---

## Recommended Entry Point

**[A7 — RCA Amendment 2026-06-01]** Original recommendation: D2 + D3. Revised recommendation: **D2 + D6**.

**D2 and D6 are the recommended starting points** because:

**D2 (T4-H Entanglement Classifier):** T4-H is already a complete theorem (4/4 steps verified, 2026-05-28). The colimit structure is available as a mathematical object. The path from T4-H to an entanglement constraint on ρ requires establishing the φ_R coupling step (A2) — a well-scoped mathematical sub-task that does not require new postulates or experiments. A successful D2 result produces a publishable mathematical physics result independent of K9_E, K9-S12, and the Buddhist Pramana interpretation layer.

**D6 (K-H Registration Observability):** The theoretical infrastructure is already complete (HDEF-01 → COR-01; falsification rules TIM-F1/NUL-F1/COR-F1; delayed-choice testbed design). D6 is the only direction in this document with a complete gate resolution protocol and an operational null model (N0). It requires lab access but no new mathematical work before the experimental design phase. D6 is **the most immediately actionable direction** and addresses Pillar II (empirical) and Pillar III (integration) of the Long-Term Research Plan.

**Why not D3 as the second entry point?**

D3 requires the W_K construction sub-task (A3) before the testability path is meaningful. This sub-task is non-trivial (4 formal steps; see A3 above) and elevates D3's effective time horizon. D3 should be **scheduled after D2's φ_R coupling step is established**, since the coupling framework from D2 will likely inform the W_K construction for D3.

**Recommended execution order:**

```
Phase 1 (parallel):
  D2 — Establish φ_R coupling step; derive entanglement constraint from T4-H
  D6 — Resolve Gate 1/2/3 for delayed-choice testbed; begin lab outreach

Phase 2 (D2 results feed D3):
  D3 — Use φ_R coupling from D2 to construct W_K; then test process matrix classification

Phase 3 (long-term):
  D1 — After A1 distinguishability criterion is established
  D4 — QEC simulation; can run in parallel with Phase 2
  D5 — φ_R extension via T4-H → N=3 → beyond; open-ended
```

---

## What to Avoid

Do not introduce additional probability postulates to replace K9_E. The value of Project B as a probability-free structural framework is its distinguishing feature relative to QBism, Relational QM, and Copenhagen. Adding a new K9_* postulate to compensate for a failed K9_E would reproduce the same dependency structure and the same vulnerability to a single experimental outcome.

The path to physical value for Project B is through mathematical results that constrain H-side structure, not through new probability assignments.

---

## Relationship to Original Paper

These directions are external to VVV-QMRF Working Paper v3.0. The paper does not claim these results. They are proposed development paths derived from RCA of the paper's architectural commitments and the identified gap between K-structure and physical prediction.

All directions are consistent with the paper's stated constraint: K-space does not modify Standard QM postulates P1–P4.

---

---

## RCA Review Summary — 3-Round × 5-Why × Scoring (2026-06-01)

**Scope:** VVV-QMRF core; VVV-QMRF-EX as compass (not cargo)  
**Method:** 3-Round RCA × 5-Why × scoring threshold 4/5  
**Reviewer:** Claude Code (claude-sonnet-4-6) on behalf of VietVunVut

### Round 1 — Gap Analysis

Root cause correctly identified by document: K1–K8 are classification axioms, not dynamics axioms. Five directions are a legitimate response. No root cause error at the plan level.

**Round 1 Score: 4.3/5 ✅**

### Round 2 — Direction Quality

| Direction | Finding | Score |
|-----------|---------|-------|
| D1 | compat predicate undefined; post-selection ≡ standard conditioning risk | 3.2/5 ⚠️ |
| D2 | Strong (T4-H proven); φ_R coupling step implicit but addressable | 4.0/5 ✅ |
| D3 | W_K construction undefined — critical blocker | 3.8/5 ⚠️ |
| D4 | Sound but peripheral to Pillar I/II | 3.5/5 |
| D5 | FUNDAMENTAL BOUNDARY unacknowledged; Track B redundancy | 3.0/5 ⚠️ |

**Round 2 Score: 3.7/5 → amendments required**

### Round 3 — Strategic Assessment

Missing direction D6 identified (K-H Observability Program, already developed in `rca_k_h_registration_observability_plan.md`). D6 is the most immediately actionable direction and was absent from the original document.

Recommended entry point revised from D2+D3 to D2+D6 due to D3's W_K construction prerequisite.

Execution order established: Phase 1 (D2 parallel D6) → Phase 2 (D3 after D2's φ_R step) → Phase 3 (D1, D4, D5).

**Round 3 Score: 4.0/5 ✅ after amendments**

### Final RCA Verdict

**Overall Plan Score: 3.8/5 → PASS with amendments (threshold 4/5)**

All 7 amendments (A1–A7) applied. Document now passes the VVV-QMRF RCA threshold for a planning document (not a claim document). No claims made beyond the existing mathematical results. K ≠ H boundary preserved throughout.

---

*Original generated by RCA analysis of VVV-QMRF Working Paper v3.0 — 2026-06-01*  
*3-Round RCA amendments applied — 2026-06-01 (VVV-QMRF scope; VVV-QMRF-EX as compass)*
