Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# K-Space Axiomatization — Registration-Logic Foundation for VVV-QMRF
# Tiên đề hóa Không gian K — Nền tảng Registration-Logic cho VVV-QMRF

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)
**Document type:** `meta_architecture`
**Date:** 2026-05-19
**Author:** VietVunVut (Viet - Nguyen Xuan)
**Status:** Class D (proposed) — All axioms and theorems are proposed registration-layer definitions
**Source:** Derived from VVV-QMRF Working Paper v2.0 Section 7.2 deferred item #5
**Cite:** VVV-QMRF §K-AXIOM
**Plan reference:** `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/plan/VVV-QMRF_K_Space_Axiomatization_Plan.md`

**Scope:** Axiomatize the K-side registration space as a formal registration-logic structure. This document provides the mathematical/logical foundation that the working paper v2.0 structural definitions rest upon.
**Out of scope:** This document does not modify Standard Quantum Mechanics, does not change any VVV-QMRF postulate (E1-E16), does not upgrade claim classes of paper v2.0, and does not claim K-space is a canonical QM object.

> **DISCLAIMER / CẢNH BÁO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

---

## 0. RCA Motivation / Động lực RCA

### 0.1 Define — Symptom vs. Cause

| | |
|---|---|
| **Symptom** | Working paper v2.0 Section 7.2 lists "Axiomatize K as a full mathematical structure" as a deferred item. Three other deferred proof items (`Bridge_EWF` semantic proof, `⊥_K` mathematical proof, `AdmJoint` necessary-and-sufficient conditions) are all blocked by the absence of axiomatized K-space. |
| **Root cause** | K is defined **extensionally** (as a collection of tuples `k = ⟨M, o, cert, t, V⟩`) rather than **intensionally** (via axioms that determine the properties of the space). All operations on K (embedding, union for `K_joint`, `⊥_K`, validity propagation) are defined ad-hoc per use case rather than derived from an axiomatic structure. |

### 0.2 Trace — 5 Whys

1. **Why needed?** VVV-QMRF uses K as a "space" in formal claims without mathematical foundation.
2. **Why now?** Three deferred proof items in paper v2.0 are blocked by this absence.
3. **Why not before?** Paper achieved Class C/D claims with structural definitions; operational bridges sufficed.
4. **Why is this right timing?** Paper formal chain is complete (Section 7.2). Axiomatization now serves dual purpose: foundation for proof upgrades AND quality audit of the paper's formal chain before community feedback arrives.
5. **Root cause:** K was introduced architecturally (`K ≠ H`) but never given formal axiomatic definition. This was intentional architectural debt to prioritize operational contact. Debt is now due.

### 0.3 Isolate — The Gap

K is currently a **collection** without structure. To be a **space**, it requires at minimum:
- **Carrier set** — what elements belong to K
- **Order structure** — temporal ordering of registration events
- **Validity structure** — how validity propagates through order
- **Operations** — embedding (morphism between K-spaces), joint construction (for `K_joint`)

### 0.4 Fundamental Design Decision

K-space is NOT a pure mathematical space. It is a **registration-logic structure**: a mathematical carrier (poset with morphisms) whose primitive predicates are epistemological (`cert`, `V`, `⊥`). This is not Hilbert space, not phase space, not probability space — these are all (math + math). K-space is (math + registration-logic). The mathematical structure is the **carrier**, not the **content**.

### 0.5 2-Layer Architecture

```
Layer 1 — CORE AXIOMS (K1-K8): Frozen
  Based on dependency stack Level 0-3 (BE SOT, K≠H, E1-E7, K-state tuple).
  These do NOT depend on Level 4 (⊥_K formal chain, which is in community review).

Layer 2 — BRIDGE THEOREMS (T1-T4): Updatable
  Connect core axioms to Level 4 structural definitions.
  Marked "pending Level 4 freeze" — updatable without changing K1-K8.
```

---

## 1. Core Axioms — Layer 1 (Frozen) / Tiên đề Lõi — Tầng 1

### AXIOM K1 — Carrier Set / Tập nền

**Statement:**
> The K-side registration space of a registering system R is a set K_R whose elements are K-state tuples. Each tuple contains five fields: measurement-registration act identifier (M), registered outcome (o), self-certification marker (cert), registration time (t), and validity status (V).

**Formal:**
```
K_R = { k | k = ⟨M, o, cert, t, V⟩ }

where:
  M    ∈ M_K          — measurement-registration act identifier
  o    ∈ O ∪ {∅}      — registered outcome (∅ reserved for null/absence cases, E9/E14)
  cert ∈ {0,1}        — self-certification marker (admission filter at K_R boundary)
  t    ∈ T_R          — registration time (discrete index or real-valued timestamp)
  V    ∈ {0,1}        — validity status

Cert admission rule:
  k ∈ K_R ⇒ cert(k) = 1.
  Reason: K_R is "produced by R over time" — every element of K_R is a registration
  event that has occurred. By K3, occurrence implies σ_R(M) = 1, hence cert(k) = 1.
  The cert ∈ {0,1} range is retained for the admission-filtering boundary:
  events with cert = 0 are NOT admitted into K_R (admission failure outside K_R scope).

K_R is produced by registering system R over time.
K_R is finite or countably infinite (discrete sequence of registration events).
```

| Property | Value |
|---|---|
| **Source** | Level 3: K-state tuple from `meta_architecture/vvv_qmrf_meta_architecture_registration_layer_formalization.md` §1 |
| **BE lineage** | Pramāṇa — cognition as structured event: act (pramāṇa), object (prameya), self-awareness (svasaṃvedana), result (phala), validity |
| **Claim class** | C (conjectural VVV-QMRF formal definition) |
| **Dependency** | Level 3 (K-state tuple). No Level 4 dependency. |
| **Boundary** | `K_R` is not a Hilbert space, not a set of physical density matrices, not a probability space. Elements `k` are registration states — they record what was registered, not what physically exists. The `o = ∅` slot is reserved for E9 (null event) and E14 (validated absence) but is not operationalized in this axiom set. |
| **Consistency** | K1 is consistent with K ≠ H (Level 1). The carrier set contains registration tuples, not physical states. |

### AXIOM K2 — Temporal Order / Thứ tự Thời gian

**Statement:**
> (K_R, <_R) is a strict total order (chain) where k1 <_R k2 iff t(k1) < t(k2) for k1, k2 ∈ K_R produced by the same registering process R. Within a single K_R, all registration events are comparable via their timestamps. The order is discrete: between any two consecutive registration events k_i and k_{i+1}, there is no K-side registration-state identity.
>
> **Clarification on order type:** Within a single K_R, the order is **total** (every pair of elements is comparable) because all elements share the same timestamp space T_R. The term "partial order" applies only when considering the **cross-K-space** setting: elements from different K_R, K_{R'} with independent timestamp spaces are NOT comparable. K2 axiomatizes the intra-K_R case, which is a strict total order. The inter-K-space partial order emerges in T1 (K_joint construction) where independent timestamp spaces are combined.

**Formal:**
```
For all k1, k2 ∈ K_R:
  k1 <_R k2  iff  t(k1) < t(k2)

(K_R, <_R) is a strict total order (chain):
  (i)    Irreflexive:   ¬(k <_R k)
  (ii)   Transitive:    k1 <_R k2  ∧  k2 <_R k3  →  k1 <_R k3
  (iii)  Asymmetry:     k1 <_R k2  →  ¬(k2 <_R k1)     [follows from (i)+(ii)]
  (iv)   Totality:      ∀k1, k2 ∈ K_R, k1 ≠ k2  →  k1 <_R k2  ∨  k2 <_R k1
                        [all elements comparable: t(k1) ≠ t(k2) for distinct events]

  Note: Totality (iv) holds because distinct registration events in the same K_R
  have distinct timestamps. If two events were to share a timestamp, they would
  be the same registration event (identity by timestamp within K_R).

Discreteness (S2-Δ lemma):
  For any consecutive pair k_i, k_{i+1} ∈ K_R with no k' such that k_i <_R k' <_R k_{i+1}:
    ∀t ∈ (t(k_i), t(k_{i+1})),  RegistrationState(t) = ∅
```

| Property | Value |
|---|---|
| **Source** | Level 2: E6 (Registering-System-as-Process) + S2-Δ lemma |
| **BE lineage** | Kṣaṇabhaṅgavāda — momentariness: registration time is discrete; no continuous registration identity between events |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E6, S2-Δ). No Level 4 dependency. |
| **Boundary** | Does NOT claim physical time is discrete. Only registration-time is discrete within K_R. Physical time in H remains continuous as per Standard QM. The "no registration-state identity between events" is a K-side property, not a claim about physical continuity. |
| **Order type note** | Within a single K_R, the order is **strict total** (chain), not merely partial. The partial-order structure emerges only in the cross-K-space setting (K_joint, T1). Previous versions mislabeled this as "strict partial order" — corrected in v1.2. |
| **Consistency** | K2 is consistent with E6's definition of R as an ordered sequence {M_1, ..., M_n} with t(M_1) < ... < t(M_n). E6's total ordering of the sequence confirms strict totality. The discreteness clause directly instantiates the Δ lemma. |

### AXIOM K3 — Self-Certification / Tự chứng nhận

**Statement:**
> For each k ∈ K_R, the certification marker cert(k) = σ_R(M) ∈ {0,1} is determined intrinsically within K_R, not by any external registration act M' ≠ M and not by any registering system R' ≠ R. σ_R(M) = 1 iff M has occurred as a K-side registration event of R.

**Formal:**
```
σ_R: M_K → {0,1}

σ_R(M) = 1  iff  M has occurred as a K-side registration event of R,
                 and this occurrence is determined intrinsically within K_R.

For all k ∈ K_R:
  cert(k) = σ_R(M)                                    [cert tracks self-certification]

Observer-indexed independence:
  σ_R(M) is independent of σ_{R′}(M′) for any R′ ≠ R.
  σ_R(M) does not require ∃M′ ≠ M such that σ_{M′}(M) = 1.

Reflexivity (E1 core property):
  The certification of M's occurrence is part of M's own K-side instantiation.
  No second-order meta-registration chain is required on the K-side.
```

| Property | Value |
|---|---|
| **Source** | Level 2: E1 (Self-Certifying Registration) |
| **BE lineage** | Svasaṃvedana — self-awareness/self-certifying cognition: a cognition certifies its own occurrence without requiring a second-order cognition |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E1). No Level 4 dependency. |
| **Boundary** | σ_R(M) certifies the OCCURRENCE of M as a K-side registration event. It does NOT certify that the physical outcome is true/correct. It is NOT consciousness, NOT a physical detector response, NOT a second-order measurement act. It is a structural property of K-side registration events — the K-side analogue of "the detector clicked" being registered as "the detector clicked" without needing another detector to detect the first detector. |
| **Consistency** | K3 is consistent with E1's definition of σ(M) as intrinsic to M. The observer-indexed extension matches paper v2.0 §3.3. K3 does not require the equivalence of σ(M) and R̂_svasa formalisms (paper v2.0 §7.2 deferred item #4). |

### AXIOM K4 — Default Validity / Tính hợp lệ Mặc định

**Statement:**
> For any k ∈ K_R with cert(k) = 1, the validity status V(k) = 1 upon instantiation of k in K_R. Validity is the default state of a self-certified registration event; it does not require external confirmation.

**Formal:**
```
For all k ∈ K_R:
  cert(k) = 1  →  V(k) = 1  (upon instantiation of k in K_R)

Exception — E9 null registration event:
  For k_null ∈ K_R where:
    o(k_null) = ∅  (no registered outcome)
    ΔI(k_null) = 0 (null interaction — interaction occurred but zero information transfer)
  cert(k_null) = 1  (self-certified: interaction occurred)
  V(k_null) = 0     (by definition of null event, not by K5 invalidation)

  This overrides the default rule K4. Null events are self-certified
  (interaction occurred) but carry zero outcome information → V = 0.

Default rule:
  For non-null k: V(k) starts at 1. No external act is required to establish V(k) = 1.

Provision: V(k) = 1 is provisional until the registration process closes
  (per E7: V_prov vs V_final distinction; see K7 Closure Axiom).
```

| Property | Value |
|---|---|
| **Source** | Level 2: E7 Axiom 1 (Default validity) |
| **BE lineage** | Svataḥ prāmāṇya — intrinsic validity: a cognition is valid by default in virtue of its occurrence (arthakriyā — causal efficacy) |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E7 Axiom 1). No Level 4 dependency. |
| **Boundary** | V(k) = 1 is default K-side registration validity for non-null events. It does NOT mean the physical outcome is correct, does NOT mean the Born-rule probability was calculated correctly, and is NOT absolute metaphysical truth. It only means: within K_R, this registration event is treated as valid until contradicted. The E9 exception (null events: cert=1, V=0) is consistent with self-certification logic: σ_R(M) certifies occurrence, not outcome validity. A null event certifies "interaction occurred" but its outcome is ∅ (zero information) → V=0 by definition, not by K5 contradiction. The provisional/final distinction is formalized in K7 (Closure Axiom). |
| **Consistency** | K4 is consistent with E7 Axiom 1. K4 works with K3: only self-certified events (cert=1) get default validity. Events that fail admission (cert=0) have no validity status defined by this axiom. K4 + exception clause is compatible with E9: null events are self-certified (interaction occurred) but carry V=0 because outcome information is ∅/zero — the exception does not break the default rule for non-null events. |

### AXIOM K5 — Invalidation / Vô hiệu hóa

**Statement:**
> V(k1) → 0 iff there exists k2 ∈ K_R with k1 <_R k2 such that k2 stands in registered contradiction (⊥) to k1 within a shared K-side comparison context C_K, and k2 has valid cross-registration authority with respect to k1. Validity cannot be externally confirmed (only contradicted). Pre-closure: V_prov(k1) → 0 is reversible in principle if the contradicting act is itself invalidated before process closure (K7). Post-closure: V_final(k1) → 0 is irreversible and absolute.

**Primitive predicate definitions:**

1. **Registered Contradiction (⊥) — minimal operational definition:**
   > For k1, k2 ∈ K_R within a shared comparison context C_K: `k2 ⊥ k1` holds iff the registration contents o(k1) and o(k2) cannot both be treated as valid K-side claims within the same C_K. This is a registration-layer contradiction, NOT a physical contradiction (ρ-side), NOT logical inconsistency in Standard QM, and NOT a claim that either physical event failed to occur.
   >
   > Minimal condition: `k2 ⊥ k1` when:
   > - k1 registers a definite outcome `o(k1) = φ` (e.g., `|h⟩⟨h|` or `|0⟩`)
   > - k2 registers a content in which `φ` is not preserved as a valid claim (e.g., superposition `|ψ⟩ ≠ |h⟩` or complementary outcome `|1⟩`)
   > - The validity of both claims cannot be simultaneously maintained without contradiction.
   >
   > Full formalization of ⊥ conditions (including boundary clauses: not physical erasure, not null event, not invalid when both sides are independently valid) is in Level 4 (paper v2.0 §4.4). The above minimal definition is sufficient for K5 operational closure.

2. **Comparison Context (C_K):**
   > A comparison context C_K is a K-side structure in which registration contents from multiple K-state tuples are evaluated for mutual consistency. C_K is defined by the D_joint demand (Level 4, §4.3): a C_K exists iff `requires_K_joint` = 1 for the relevant K-spaces.

3. **Cross-Registration Authority — deferred to K6:**
   > The "valid cross-registration authority" condition is formalized in Axiom K6 below.

**Formal:**
```
Firing precondition:
  C_K must exist — i.e., requires_K_joint = 1 for the relevant K-spaces (Level 4, §4.3).
  K5 is a cross-observer invalidation rule: it fires only in joint-registration
  (K_joint) contexts. When requires_K_joint = 0, no C_K exists, condition (ii)
  is undefined, and K5 does not fire.

V(k1) → 0  iff  ∃k2 ∈ K_R such that:

  (i)   k1 <_R k2                                    [K2: k2 is later in registration order]
  (ii)  k2 ⊥ k1  within shared C_K                    [registered contradiction in comparison context]
  (iii) k2 has valid cross-registration authority      [authority conditions from paper v2.0 §4.4]
        with respect to k1 in C_K

Asymmetry (E7 Axiom 3):
  ¬∃F such that F(k′) → {V(k) = 1}
  (No external function can restore or confirm validity.)

Validity stages (K7):
  V_prov(k)  — provisional validity, during open registration process (pre-closure)
  V_final(k) — final validity, after registration process closes (post-closure)
  K5 conditions (i)-(iii) govern V_prov transitions during the open process.
  V(k) in K5 refers to V_prov(k) pre-closure and V_final(k) post-closure.

Irreversibility (post-closure only):
  V_final(k) → 0  ⇒  V_final(k) remains 0 permanently.
  (After registration process closes (K7), invalidation is absolute and cannot be revised.)

Pre-closure (K7):
  V_prov(k) → 0 is in principle reversible: if the contradicting act k2 is itself
  invalidated (V(k2) → 0) before process closure (K7), the K5 trigger for k1 is
  removed and V_prov(k1) is no longer forced to 0. Governed by K7 — pre-closure
  K5 transitions are not final.

K_R disambiguation (cross-space context):
  When C_K exists (requires_K_joint = 1), the quantifier ∃k2 ∈ K_R operates over
  the relevant subspace of K_joint: k2 may originate from a different K-space K_X
  and appears as i_X(k2) ∈ K_joint. The concrete model (§7) uses i_W(k_W) ∈ K_joint
  — the operative reading of K_R is K_joint when C_K exists. In isolated scenarios
  (requires_K_joint = 0, no C_K), K5 does not fire because condition (ii) is
  undefined (no C_K to evaluate ⊥ within).
```

| Property | Value |
|---|---|
| **Source** | Level 2: E7 Axioms 2-3 (Invalidation + Asymmetry) |
| **BE lineage** | Parataḥ prāmāṇya — invalidity is detected extrinsically. Bādhaka pramāṇa — a contradicting cognition (bādhaka) retroactively voids the earlier cognition. |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E7 Axioms 2-3). Uses `⊥` and "cross-registration authority" as **primitive predicates** whose full formalization is in Level 4 (paper v2.0 §4.4). K5 asserts the structural rule; the precise conditions for `k2 ⊥ k1` and "valid cross-registration authority" are defined in the bridge theorems (T1-T3). **2nd-order Layer 2 dependencies — Dep-A:** C_K existence precondition requires Level 4 predicate `requires_K_joint = 1` (Level 4 §4.3); K5 does not fire when C_K is absent (also reflected in Layer 1 Summary K5 row Role 1, via F4). **Dep-B:** K5 condition (i) uses K2's `<_R` ordering; when K5 fires in K_joint (its only operative context), the ordering is T1's `<_joint` (Layer 2 bridge theorem); K8 t-field preservation guarantees `k1 <_R k2 ↔ i(k1) <_joint i(k2)` — no functional contradiction; Dep-B is a documentation dependency only. |
| **Boundary** | K5 is a registration-layer invalidation rule. It does NOT claim that the physical outcome of M_1 is retroactively erased from ρ-side history. The physical interaction I_1 still occurred; only its K-side registration validity is revised. The `⊥` relation is NOT physical orthogonality in H. The irreversibility of V→0 is a K-side property, not a claim about physical time asymmetry. |
| **Consistency** | K5 is consistent with E7 Axioms 2-3 and with the act-level contradiction definition in paper v2.0 §4.4. The primitive predicates (⊥, C_K, cross-registration authority) now have minimal operational definitions: ⊥ is defined above in K5, C_K is tied to requires_K_joint, and authority is formalized in K6 below. This removes the prior dependency inversion where frozen K5 relied on undefined Level 4 primitives. |

### AXIOM K6 — Cross-Registration Authority / Thẩm quyền Chéo

**Statement:**
> For k1, k2 ∈ K_R with k1 <_R k2, k2 has valid cross-registration authority with respect to k1 in comparison context C_K iff: (a) both k1 and k2 belong to the same C_K, (b) V(k2) = 1 at the time of the authority check (k2 has not itself been invalidated), and (c) the validity demand D_joint that defines C_K includes the claim-content of k1 within its scope. Cross-registration authority is NOT a hierarchy of observers; it is a structural relation within a shared comparison context.

**Formal:**
```
Auth(k2 → k1, C_K) = 1  iff  all of:

  (a)  C_K-sphere(k1) = C_K-sphere(k2)      [both belong to same C_K]
  (b)  V(k2) = 1                             [k2 not invalidated at check time]
  (c)  k1 ∈ scope(D_joint)                   [k1's claim falls within D_joint scope]

  where:
    C_K-sphere(k) is the comparison context that k belongs to.
    scope(D_joint) is the set of registration acts whose claims D_joint demands
    joint validity evaluation for.

Auth is NOT:
  - Observer hierarchy (no "Wigner over Friend" privilege)
  - Physical measurement authority (not a ρ-side property)
  - Absolute epistemic authority (bound to C_K, not universal)
  - Transitive across distinct C_K contexts:
      Auth(k2→k1, C_K) ∧ Auth(k3→k2, C_K') ⇏ Auth(k3→k1, ·)  [when C_K ≠ C_K']
      Note: within a single shared C_K the formal block does not exclude transitivity.

Non-transitivity proof sketch (counterexample):
  Consider three registration events k1, k2, k3 ∈ K_R with k1 <_R k2 <_R k3,
  and TWO distinct comparison contexts C_K and C_K':

  Setup:
    - Auth(k2→k1, C_K) = 1:  k1, k2 ∈ C_K, V(k2)=1, k1 ∈ scope(D_joint of C_K).
    - Auth(k3→k2, C_K') = 1: k2, k3 ∈ C_K', V(k3)=1, k2 ∈ scope(D_joint of C_K').
    - But k1 ∉ C_K' (k1 is not in the second comparison context).

  Claim: Auth(k3→k1, ·) = 0 in BOTH contexts:
    - In C_K:  k3 ∉ C_K  → condition (a) fails → Auth(k3→k1, C_K) = 0.
    - In C_K': k1 ∉ C_K' → condition (a) fails → Auth(k3→k1, C_K') = 0.

  Therefore: Auth(k2→k1, C_K) ∧ Auth(k3→k2, C_K') holds (C_K ≠ C_K'), but
  Auth(k3→k1, ·) = 0 in every available comparison context. ∎

  Scope: this counterexample proves non-transitivity across distinct C_K contexts
  (C_K ≠ C_K'). It does not claim non-transitivity within a single shared C_K.

  Physical intuition: Authority is context-bound. Two different D_joint demands
  create two different comparison scopes. Transitivity would require a single
  C_K containing all three events with overlapping scope — which is not
  guaranteed by the pairwise authority relations.
```

| Property | Value |
|---|---|
| **Source** | Level 2: E7 Axiom 2 + paper v2.0 §4.4 cross-registration authority section |
| **BE lineage** | Bādhaka pramāṇa — a contradicting cognition must be a valid cognition (pramāṇa) itself to serve as bādhaka. An invalid cognition cannot void another. |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E7 Axiom 2). Uses `C_K` and `D_joint` from Level 4 with three Auth roles: (1) existential precondition — K6 operates only when C_K exists (requires_K_joint = 1); (2) C_K-sphere membership parameter (condition a); (3) D_joint scope parameter (condition c). **Dep-A (2nd-order Layer 2 dependency):** Auth(k2→k1, C_K) requires C_K to exist (requires_K_joint = 1, Level 4 §4.3); K6 does not operate when C_K is absent — analog K5 Dep-A. **Conditional semantic dependency (I-03 pattern):** condition (c) `k1 ∈ scope(D_joint)` means Level 4 changes to D_joint scope alter which k1 have Auth = 1, without altering K6 text (syntactic freeze holds); analogous to K5 ⊥_K boundary clauses (I-03/F3). |
| **Boundary** | Auth is a K-side structural relation within C_K. It does NOT create observer hierarchy, does NOT grant absolute epistemic privilege, and is NOT a claim about physical measurement authority. Two observers in the same C_K may have mutual authority (symmetric) when both are valid. Authority is lost the moment V(k2) → 0 (K5). |
| **Consistency** | K6 operationalizes K5's condition (iii) — "valid cross-registration authority" is no longer an undefined primitive. K6 is consistent with E7 Axiom 2's extrinsic invalidation: a contradicting act must itself be valid. K6's non-transitivity preserves the pair-wise nature of authority checks. |

### AXIOM K7 — Registration Process Closure / Đóng Quá trình Ghi nhận

**Statement:**
> The registration process R of K_R closes at registration time t_close when no pending `requires_K_joint` demands remain for any pair of K-spaces involving K_R. At closure, for all k ∈ K_R: V(k) transitions from provisional status V_prov(k) to final status V_final(k). After closure: (a) no new k can be instantiated in K_R, (b) K5 irreversibility becomes absolute (V(k)→0 cannot be revised by any future event), and (c) no new D_joint involving K_R can be raised. Before closure, all V(k) are provisional and subject to K5 invalidation.

**Formal:**
```
R closes at t_close(K_R) iff:
  ∀ pairs (K_R, K_X) where X is any registering system:
    pending(K_R, K_X) = ∅

  where pending(K_R, K_X) is the set of unresolved requires_K_joint demands
  whose D_joint involves both K_R and K_X.

At closure:
  For all k ∈ K_R:
    V_prov(k) → V_final(k)     [provisional → final]

Post-closure properties:
  (a)  K_R is closed under new k:  ∄k_new ∈ K_R with t(k_new) > t_close
  (b)  K5 irreversibility is absolute: V_final(k) = 0 → V_final(k) stays 0 permanently
  (c)  No new D_joint(K_R, ·) can be raised
  (d)  K_joint involving K_R becomes final (no reconfiguration)

Pre-closure:
  All V(k) are V_prov(k). K5 invalidation transitions modify V_prov.
  The V_final value for each k is the limit of V_prov(k) as t → t_close.
```

| Property | Value |
|---|---|
| **Source** | Level 2: E7 (V_prov vs V_final distinction, paper v2.0 §2.2) |
| **BE lineage** | Niścaya (ascertainment/determination) — a cognition becomes determinate when the cognitive process reaches closure; before that, it is provisional (saṃśaya — doubt is possible) |
| **Claim class** | D (proposed) |
| **Dependency** | Level 2 (E7 V_prov/V_final distinction). Uses `requires_K_joint` and `D_joint` from Level 4 as closure condition inputs. **Dep-B (2nd-order Layer 2 dependency):** K7 closure condition `pending(K_R, K_X) = ∅` uses the concept of "resolved demand" — a requires_K_joint demand is resolved when a K_joint registration event satisfying T2 AdmJoint conditions has occurred; without T2, "resolved" is an undefined primitive in K7; T2 is a silent Layer 2 dependency for closure semantics — analog K5 Dep-B (T1 `<_joint` for K5 condition (i)). **Conditional semantic dependency (I-03 pattern):** Level 4 extensional scope of `requires_K_joint` (which event types require joint registration) directly determines t_close timing — expanding the scope delays closure, narrowing it advances closure; K7 text is frozen but t_close (and therefore when V_prov → V_final and when K5 irreversibility becomes absolute) depends on Level 4 content; analogous to K5 ⊥_K boundary clauses (I-03/F3) and K6 D_joint scope (I-03/F6a). |
| **Boundary** | K7 defines when the K-side registration process closes. It does NOT claim the physical interaction has ended, does NOT claim the H-space state has reached a final value, and does NOT claim that all possible measurements have been completed. Closure is a K-side property: no more joint validity demands are pending. In practice, t_close may be identified with the end of an experimental protocol, the publication of results, or any agreed-upon endpoint of the registration process. |
| **Consistency** | K7 resolves the "provisional" gap in K4 and K5. K4's default validity is provisional until closure; K5's irreversibility is provisional until closure, then absolute. K7 is consistent with E7's distinction between V_prov and V_final. K7 does not conflict with K5: pre-closure K5 transitions are reversible in principle (if the contradicting act is itself invalidated before closure), but post-closure K5 transitions are absolute. |

### AXIOM K8 — Cross-Space Embedding Preservation / Bảo toàn qua Phép nhúng

**Statement:**
> For any embedding i_{R→X}: K_R → K_X that maps a K-state tuple k ∈ K_R into a joint or cross K-space K_X, the embedding preserves the validity value V(k) at the moment of embedding: V_X(i_{R→X}(k)) = V_R(k) at embedding time t_embed. Furthermore, the embedding preserves the remaining tuple fields (M, o, cert, t) unchanged. After embedding, V_X(k) evolves independently within K_X according to K4-K7 — the embedding preserves the initial validity snapshot, not immunity from future invalidation.

**Formal:**
```
For any embedding i: K_R → K_X (where K_X may be a joint K-space K_joint
or any cross-space structure):

  (i)   V-preservation (Embedding Postulate):
        V_X(i(k)) = V_R(k)  at t_embed  for all k ∈ K_R
        (V-value carries over into K_X at the moment of embedding.)

  (ii)  Field preservation:
        M_X(i(k)) = M_R(k)      [act identifier preserved]
        o_X(i(k)) = o_R(k)      [registered outcome preserved]
        cert_X(i(k)) = cert_R(k) [self-certification marker preserved]
        t_X(i(k)) = t_R(k)      [registration timestamp preserved]

  (iii) Post-embedding evolution:
        After t_embed, V_X(i(k)) evolves according to K4-K7 rules
        within K_X. K8 does NOT immunize against future K5 invalidation
        in K_X. It only guarantees that the embedding itself does not
        alter V — the embedded element enters K_X with its native validity
        intact, then stands or falls by K_X's own validity dynamics.

  (iv)  Non-redundancy:
        K8 is NOT derivable from K4. K4 governs V upon instantiation
        within a native K_R — it is silent on cross-space embedding
        behavior. K8 is an independent postulate about the behavior
        of V under the embedding operation. A framework without K8
        (or an equivalent postulate) cannot guarantee that embedded
        registration acts retain their validity status.
```

| Property | Value |
|---|---|
| **Source** | Architectural necessity identified during T1 construction: K1-K7 alone cannot guarantee V-preservation through cross-space embeddings because K4 only governs V upon instantiation within a native K_R. Formerly tracked as "Embedding Postulate (EP)" — an external postulate required by T1. Promoted to K8 (v1.4) to make the axiom set self-contained. |
| **BE lineage** | Anugama (continuity/attendant relation) — the validity of a cognition accompanies it when the cognition is taken up in a broader cognitive context; the cognition does not lose its epistemic status merely by being embedded in a larger framework |
| **Claim class** | D (proposed) |
| **Dependency** | Level 0-3 (K1 tuple structure, K4 default validity). No Level 4 dependency. |
| **Boundary** | K8 is a structural postulate about the embedding operation itself, not about the native K-spaces being embedded. It guarantees snapshot preservation, not permanent immunity. After embedding, K5 can still fire in K_X and invalidate i(k). K8 does NOT claim that V-values are absolutely invariant under all operations — only that the embedding map i itself does not alter them. |
| **Consistency** | K8 is consistent with K4: K4 defines validity at native instantiation, K8 defines validity-preservation at cross-space transfer. They govern different moments. K8 is consistent with K5: K8 guarantees the initial V snapshot in K_X, but K5 can still transition V_X(i(k)) → 0 afterwards — the embedded element inherits both rights (default validity) and liabilities (future invalidation) of its new home. K8 + K1 together guarantee that the embedded tuple maintains its identity (5-field structure) across spaces. |

### Layer 1 Summary / Tổng kết Tầng 1

| Axiom | Content | Fields covered | Source level | Freeze status | Level 4 dependency |
|---|---|---|---|---|---|
| K1 | Carrier set — K_R is a set of 5-field tuples | M, o, cert, t, V | Level 3 | Frozen | None |
| K2 | Temporal order — strict total order (chain) within K_R, discrete | t (ordering) | Level 2 | Frozen | None |
| K3 | Self-certification — σ_R(M) intrinsic to R | cert | Level 2 | Frozen | None |
| K4 | Default validity — V=1 on instantiation (with E9 exception) | V (default) | Level 2 | Frozen | None |
| K5 | Invalidation — V→0 by later ⊥ with authority; minimal ⊥ definition included | V (transition) | Level 2 | Frozen | C_K roles: (1) existential precondition — K5 fires only when C_K exists (requires_K_joint = 1); (2) ⊥ evaluation parameter (condition ii); (3) Auth evaluation parameter (condition iii) |
| K6 | Cross-registration authority — structural relation within C_K, non-hierarchical | V (authority condition) | Level 2 | Frozen | C_K roles: (1) existential precondition for all Auth checks; (2) C_K-sphere membership parameter (condition a); (3) D_joint scope parameter (condition c) |
| K7 | Registration process closure — V_prov → V_final, absolute irreversibility | V (closure) | Level 2 | Frozen | Uses requires_K_joint for pending check only |
| K8 | Cross-space embedding preservation — V preserved at embedding time; fields preserved | V (embedding) + M, o, cert, t | Level 3 | Frozen | None |

**Dependency isolation:** K1-K8 depend ONLY on Level 0-3 (BE SOT, K≠H, E1-E7, K-state tuple). Where K5-K7 reference Level 4 concepts (C_K, D_joint, requires_K_joint), they reference them for **scope identification only** (e.g., "is k1 in the same C_K as k2?"), not for their internal structure or definition.

**Syntactic freeze (unconditional):** K1-K8 text is frozen. If paper v2.0 community feedback changes the internal structure of AdmJoint, K1-K8 do not change — AdmJoint appears only in bridge theorems T1-T4, not in any K1-K8 axiom text.

**Semantic dependency for ⊥_K (conditional):** K5 minimal ⊥ definition provides K5-local operational closure. However, Level 4 §4.4 boundary clauses ("not null event", "not invalid when both sides independently valid") narrow K5 minimal ⊥ and constitute a real semantic dependency: if these boundary clauses change, K5 fires in a different set of cases even though K5 text is unchanged. The syntactic freeze guarantee holds unconditionally; the semantic behavior guarantee for K5 is conditional on Level 4 ⊥ boundary clauses remaining a conservative extension of K5 minimal ⊥ (adding scope, not contradicting it). Only bridge theorems T1-T3 need updating for structural Level 4 changes.

---

## 2. Bridge Theorems — Layer 2 (Updatable) / Định lý Cầu nối — Tầng 2

**Status note:** Theorems T1-T3 are **pending Level 4 freeze** (paper v2.0 in community review). They connect K1-K8 to the paper's structural definitions. If Level 4 definitions change, T1-T3 are updated independently of K1-K8. T4 is new (Class D).

### T1 — K_joint Construction Theorem

**Statement:**
> Given K-side spaces K_A and K_B of registering systems A, B: if requires_K_joint(A, B) = 1 via a shared validity demand D_joint, then a candidate joint K-space K_joint(A, B) exists as the minimal K-space containing order-preserving embeddings i_A: K_A → K_joint and i_B: K_B → K_joint that preserve cert and V values. The embedding respects the internal time-order of each structure, and the combined order in K_joint is the transitive closure of the two embedded orders plus cross-structure temporal relations from the shared laboratory history.

**Derivation from axioms:**
```
K_joint(A,B) exists as a candidate K-space:
  ↔ K1: K_A, K_B are sets of tuples → K_joint carrier = i_A(K_A) ∪ i_B(K_B)
  + K2: each has temporal order → combined order = (i_A(<_A) ∪ i_B(<_B) ∪ cross-rel)^+
       where ^+ is transitive closure
  + K3: embeddings i_A, i_B preserve cert values (σ_A(M) maps to same cert in K_joint)
  + K8: embeddings i_A, i_B preserve V values at embedding time
       (V_X(i(k)) = V_R(k) at t_embed — native validity carries into K_joint).
       K8 replaces the former external Embedding Postulate (EP); the axiom set
       is now self-contained for V-preservation.
  + requires_K_joint = 1 via D_joint (Level 4, §4.3)
  + K6: cross-registration authority between embedded elements is evaluated
       within the C_K defined by D_joint.

Note: existence of a candidate K_joint does NOT guarantee it is admissible.
Admissibility requires AdmJoint conditions (i)-(v) to hold (Level 4, §4.3).
```

| Property | Value |
|---|---|
| **Level 4 dependency** | `requires_K_joint` predicate, `D_joint` definition (paper v2.0 §4.3). K6 authority structure. |
| **Layer 1 dependency** | K8 (cross-space embedding preservation) — V-preservation is now derived from a core axiom, not an external postulate. **Former EP gap (G1) resolved by promoting EP → K8 (v1.4).** |
| **Claim class** | D (proposed) |
| **Freeze status** | Pending Level 4 freeze |
| **Update trigger** | If `requires_K_joint` definition changes or AdmJoint embedding conditions change |

### T2 — ⊥_K Derivation Theorem

**Statement:**
> For K-side spaces K_A and K_B: K_A ⊥_K K_B holds iff requires_K_joint(A, B) = 1 AND no admissible K_joint exists satisfying AdmJoint conditions (i)-(v) while preserving K4 (default validity) and K5 (no invalidation) for both embedded sides simultaneously. The incommensurability is traced to a K5 conflict: any candidate K_joint forces V(k_A) → 0 or V(k_B) → 0 while both are claimed as jointly valid.

**Derivation from axioms:**
```
K_A ⊥_K K_B
  ↔ requires_K_joint(A,B) = 1                              [Level 4, §4.3]
  ∧ ¬∃ K_joint: AdmJoint(K_joint; K_A, K_B) = 1             [Level 4, §4.3]

T2 focuses on the case where AdmJoint fails via K5 conflict:
  Under candidate K_joint, ∃k_A ∈ i_A(K_A), k_B ∈ i_B(K_B) such that
  k_B ⊥ k_A within C_K (registered contradiction)            [K5 primitive, Level 4 §4.4]
  AND Auth(k_B → k_A, C_K) = 1 (cross-registration authority) [K6]
  → K5 forces V(k_A) → 0  OR  V(k_B) → 0                     [K5 from Layer 1]
  → AdmJoint condition (iv) violated                         [Level 4, §4.3]
    (no invalidation while both claimed as jointly valid)

Note: K5 conflict is a SUFFICIENT condition for AdmJoint failure,
NOT a necessary condition. AdmJoint may fail for other reasons
(e.g., embedding structure fails conditions (i)-(iii) or (v);
 D_joint is ill-posed for the given K-spaces; K7 closure has
 already locked one K-space preventing reconfiguration).
In such cases, ⊥_K may still hold, but the derivation trace
differs from the T2 K5-conflict path shown above.

⚠ CIRCULARITY ACKNOWLEDGMENT:
  T2 derives ⊥_K (incommensurability) from K5 conflict.
  K5 uses ⊥ (registered contradiction) as a primitive predicate.
  The MINIMAL operational definition of ⊥ is given in K5 (Layer 1).
  The FULL formalization of ⊥ conditions is in Level 4 (paper v2.0 §4.4),
  which is itself defined in terms of "registered contradiction" —
  a concept whose precise boundary clauses are NOT yet frozen.

  Status of the circularity:
    - K5's minimal ⊥ definition (Layer 1) is self-contained:
      it defines ⊥ as "registration contents cannot both be treated
      as valid K-side claims within the same C_K." This is NOT circular.
    - v1.3 CONCRETE MODEL FINDING: Circularity does NOT arise in the
      concrete model (§7.5 Step 4) — K5 minimal ⊥ is directly verifiable
      by content inspection (|h⟩ vs |Ψ+⟩) without invoking Level 4 full ⊥.
    - The circularity only appears in the GENERAL case where T2 needs
      AdmJoint conditions that reference full ⊥ — and even there it is
      a dependency-ordering issue (Level 4 not frozen), not a logical circle.
    - Resolution path: freeze Level 4 ⊥ boundary clauses independently
      of T2, then T2's derivation becomes non-circular.
    - Until Level 4 freeze: T2 is CONDITIONAL on Level 4 ⊥ definition.
      T2's conclusion (⊥_K) is valid IF the Level 4 ⊥ formalization
      is consistent with K5's minimal definition. This is a reasonable
      assumption but NOT a proven fact.
```

Boundary clauses (from paper v2.0 §4.4):
```
  ⊥_K does NOT assert that either physical event fails to occur on the ρ-side.
  ⊥_K does NOT mean either observer's outcome is false within its own K-side.
  ⊥_K is NOT equivalent to Null_K(e) — null registration is separate (E9).
  ⊥_K applies only when both sides are valid/provisionally valid within their own K-side.
```

| Property | Value |
|---|---|
| **Level 4 dependency** | `AdmJoint` conditions (i)-(v), `⊥_K` boundary clauses, `D_joint` (paper v2.0 §4.3-4.4) |
| **Layer 1 dependency** | K5 (invalidation rule) + K6 (authority condition) + K8 (V-preservation at embedding) — T2 derivation uses all three. **K8 resolves former EP gap (G1): V-preservation is now derived from a core axiom.** |
| **Claim class** | D (proposed). Derivation trace is Class D; the ⊥_K conclusion matches paper v2.0 Class D definition. |
| **Important** | K5 conflict is a SUFFICIENT condition for AdmJoint failure, not necessary. AdmJoint may fail for other reasons. |
| **Freeze status** | Pending Level 4 freeze |
| **Update trigger** | If AdmJoint conditions (i)-(v) change, or ⊥_K boundary clauses are revised |

### T3 — Bridge_EWF Formalization Theorem

**Statement:**
> In an Extended Wigner's Friend configuration where D_joint requires F-side and W-side registrations to support one cross-observer validity constraint, Bridge_EWF(D_joint; M_F, M_W) = 1 is derivable from K5 when: (a) M_F registers a definite friend-side outcome o_F, (b) M_W registers the same laboratory as a coherent superposition in which no definite o_F is preserved as a W-side valid claim, and (c) no reinterpretation inside the same K_joint can preserve both registered contents without changing the validity claim of at least one side.

**Derivation from axioms:**
```
Bridge_EWF(D_joint; M_F, M_W) = 1
  ↔ D_joint requires F-side and W-side registrations to be evaluated
    as jointly valid parts of one laboratory registration history     [Level 4, §4.3]
  ∧ M_F: k_F = ⟨M_F, o_F, 1, t_F, 1⟩  (definite outcome, self-certified, valid)
  ∧ M_W: k_W = ⟨M_W, o_W, 1, t_W, 1⟩  (superposition registered, no definite o_F)
  ∧ Under candidate K_joint:
      k_W ⊥ k_F within C_K (registration contents incompatible)       [Level 4, §4.4]
      ∧ k_W has valid cross-registration authority                   [Level 4, §4.4]
      → K5: V(k_F) → 0  OR  V(k_W) → 0                              [K5]
      → AdmJoint condition (iv) violated                             [Level 4, §4.3]
  → M_W ⊥ M_F (act-level registered contradiction)                   [Level 4, §4.4]

External philosophical assumption — Relativization defense:
  T3 depends on the following assumption (not derived from K1-K8):
  "If K_joint only hosts meta-descriptions ('within K_F, M_F registered |h⟩'),
   it does not satisfy D_joint (which demands joint validity of original claims).
   Relativizing contents abandons D_joint rather than satisfying it."
  (paper v2.0 §4.5)

  This is an EXTERNAL PHILOSOPHICAL COMMITMENT, not a theorem derivable from
  K1-K8. It defines what counts as "satisfying D_joint" — a semantic choice
  about the nature of joint validity demands. If this assumption is rejected
  (i.e., if meta-descriptions ARE accepted as satisfying D_joint), then
  T3's conclusion (Bridge_EWF = 1) does not follow from K1-K8 alone.
```

| Property | Value |
|---|---|
| **Level 4 dependency** | `Bridge_EWF` lemma, `D_joint`, cross-registration authority (paper v2.0 §4.5) |
| **Layer 1 dependency** | K5 (invalidation) + K6 (authority) + K8 (V-preservation at embedding) — T3 derivation uses all three. |
| **External assumption** | Relativization defense (paper v2.0 §4.5) — a philosophical commitment, not derivable from K1-K8. T3 depends on this assumption. This is NOT a gap — it is a semantic boundary present in every measurement framework. |
| **Claim class** | D/C boundary (matches paper v2.0 §4.5 classification) |
| **Freeze status** | Pending Level 4 freeze |
| **Update trigger** | If `Bridge_EWF` sufficient conditions change, or cross-registration authority criteria are revised, or relativization defense is challenged |

### T4 — N-Observer Generalization Theorem

**Statement:**
> For N ≥ 2 registering systems R_1, ..., R_N with K-side spaces K_1, ..., K_N: the joint K-space K_joint(R_1, ..., R_N) exists as the colimit of the embedding diagram iff for every pair (i, j) with requires_K_joint(K_i, K_j) = 1, pairwise AdmJoint is satisfied. K-side incommensurability ⊥_K is NOT necessarily transitive: K_A ⊥_K K_B ∧ K_B ⊥_K K_C does NOT entail K_A ⊥_K K_C. Each pair requires an independent D_joint and AdmJoint check.

**Derivation from axioms:**
```
K_joint(R_1,...,R_N) = colimit of embedding diagram D where:
  objects:  K_1, K_2, ..., K_N
  morphisms: for each pair (i,j) with requires_K_joint(K_i,K_j) = 1
             and AdmJoint satisfied: embedding i_{ij}: K_i → K_j (or K_i → K_joint)
  colimit universal property: K_joint is the minimal K-space receiving
    embeddings from all K_i that commute with the diagram morphisms.

Non-transitivity of ⊥_K:
  Counter-example possibility:
    K_A ⊥_K K_B  ∧  K_B ⊥_K K_C  ∧  ¬(K_A ⊥_K K_C)
    when: requires_K_joint(A,C) = 0 (no shared validity demand)
    OR: requires_K_joint(A,C) = 1 AND AdmJoint(K_joint; K_A, K_C) = 1

  Each pair (i,j) must pass independent:
    (a) requires_K_joint check (is joint validity demanded?)
    (b) AdmJoint check (can joint validity be preserved?)

Number of pairwise checks for N observers:
  At most N(N-1)/2 pairs with requires_K_joint = 1 (when all pairs require joint check).
  Not all pairs necessarily require K_joint (some may be causally/comparison-isolated).
```

| Property | Value |
|---|---|
| **Level 4 dependency** | All Level 4 definitions, generalized to N observers |
| **Claim class** | D (proposed) — NEW. Not in paper v2.0 (which handles N=2 only). |
| **Freeze status** | New theorem. Requires independent verification for N>2. |
| **Update trigger** | When N>2 EWF scenarios are modeled; when paper v3.0 extends to multi-observer cases |

### Layer 2 Summary / Tổng kết Tầng 2

| Theorem | Bridges axioms to | Level 4 dependency | Freeze status | Risk if Level 4 changes |
|---|---|---|---|---|
| T1 | K_joint construction | `requires_K_joint`, `D_joint`, embeddings | Pending | Theorem statement updates; K1-K8 unchanged |
| T2 | ⊥_K derivation | `AdmJoint` (i)-(v), `⊥_K` boundary clauses | Pending | Derivation chain updates; K1-K8 unchanged |
| T3 | Bridge_EWF formalization | `Bridge_EWF` lemma, external assumption: relativization defense | Pending | Derivation chain + external assumption may need revision; K1-K8 unchanged |
| T4 | N-observer generalization | All Level 4, generalized to N | New — Class D | New theorem; independently updatable |

---

## 3. Audit Matrices / Ma trận Kiểm toán

### 3.1 E1-E7 Core Postulate Audit

**Question for each postulate:** Are K1-K8 sufficient to capture its K-side structural content, or do the axioms contradict it?

| Postulate | Content | K-space coverage | Verdict |
|---|---|---|---|
| **E1** | Self-Certifying Registration: σ(M)=1 intrinsic to M; no M' required | K3 directly instantiates σ_R(M) with intrinsic determination and observer-indexed independence | **COVERED — K3** |
| **E2** | Registration Self-Completion: M ≡^K r (act-result inseparability) | Not directly axiomatized. K1 includes both M and o in the same tuple — the tuple structure itself encodes act-result co-occurrence without requiring a separate axiom. The ≡^K relation is implicit in the tuple's joint instantiation. | **ENCODED — K1 tuple structure** |
| **E3** | Registration Lock: C: H→K, C(I)=k_locked | Not directly axiomatized. C is a bridge map (H→K), not an intra-K-space property. K1-K8 describe K-space structure; C belongs to the bridge layer (interface between ρ-side and K-side). | **OUT-OF-SCOPE — Bridge layer. No conflict.** |
| **E4** | Pre-Symbolic Registration Stratum: ε(M) ∈ K_pre, Sym(ε)=∅ | Not directly axiomatized. K1 defines K-state tuples at the symbolic level (o is a symbolic outcome). The pre-symbolic stratum K_pre is a substructure not formalized in K1-K8. | **OUT-OF-SCOPE — Reserved for K-space stratification extension** |
| **E5** | Internal Representation Encoding: f_enc maps apparatus state to outcome within K | Not directly axiomatized. f_enc is an encoding map that operates within K but is not a structural property of K-space itself. | **OUT-OF-SCOPE — Encoding operation. No conflict.** |
| **E6** | Registering-System-as-Process: R = {M_1,...,M_n}, no identity beyond acts | K2 directly instantiates the temporal order as a strict partial order. K1+K2 together encode: R IS the ordered set of K-state tuples — there is no "R" separate from its K_R. | **COVERED — K1+K2** |
| **E7** | Registration Validity Location: V=1 default (Axiom 1), V→0 by ⊥ (Axiom 2), asymmetry (Axiom 3) | K4 = Axiom 1 (default, with E9 exception). K5 = Axiom 2+3 (invalidation + asymmetry + irreversibility). K6 = authority condition. K7 = closure (V_prov → V_final). All three E7 axioms + provisional/final distinction are directly instantiated. | **COVERED — K4+K5+K6+K7** |

**E1-E7 Audit verdict: 3/7 COVERED directly (E1, E6, E7). 1/7 ENCODED implicitly (E2). 3/7 OUT-OF-SCOPE (E3, E4, E5). Zero contradictions. Coverage gaps are intentional (bridge layer items, pre-symbolic stratification, encoding operations — these belong to other architectural layers, not K-space axiomatization).**

### 3.2 E8-E16 Extension Postulate Audit

**Question for each postulate:** Does the postulate require K-space structure beyond K1-K8? If yes, is the gap documented?

| Postulate | Content | K-space requirement | Verdict |
|---|---|---|---|
| **E8** | Retroactive Registration Override: M_2 retroactively voids M_1 | K5 covers single-step invalidation (k2 ⊥ k1 → V(k1)→0). Multi-step retroactive chains (k3 voids k2 which affects k1's re-assessment) are not covered. E8's orthogonality trigger condition (⟨λ_2\|λ_1⟩=0) is a ρ-side condition, not a K-space axiom. Note: K5 Pre-closure block (F1) formalizes this: V_prov(k1) → 0 is reversible if the contradicting act k2 is itself invalidated before t_close (K7). The PARTIAL verdict is for multi-step retroactive chains only — pre-closure re-assessment of single-step invalidation is now explicitly covered by K5 + K7. | **PARTIAL — K5 single-step + pre-closure re-assessment covered (K5 F1 + K7). Multi-step retroactive chain formalization deferred.** |
| **E9** | Null Registering-System Event: interaction occurred but ΔI=0 | K1 reserves o=∅ slot. K4 now includes explicit E9 exception clause: null events have cert=1 (interaction occurred), V=0 (by definition, not K5). K4/K5 consistency with E9 is resolved. | **COVERED — K1 o=∅ + K4 E9 exception. Null events structurally accommodated.** |
| **E10** | Tripartite Registration Validity Matrix: three validity criteria | Validity criteria operate on K-side predicates; K4-K5-K6-K7 provide the underlying validity structure. The tripartite matrix is a taxonomy layer on top of K4-K7. | **COVERED — K4-K7 as foundation. No new axiom needed.** |
| **E11** | Contrapositive Quantum Evidence: evidence from absence | Evidence structure is outside K-space (bridge/evidence layer). Evidence ABOUT K-side states is not a property OF K-space. | **OUT-OF-SCOPE — Bridge/evidence layer. No conflict.** |
| **E12** | Limit-Faculty Registration: different registering capacities | Different K_R types with different registration capacities are type-level distinctions, not new axioms. K1-K8 apply to all K_R regardless of capacity type. | **COVERED — Taxonomy layer. No new axiom needed.** |
| **E13** | Temporal Discontinuity Registration | K2 already encodes discreteness via the Δ lemma clause (no registration-state identity between events). | **COVERED — K2** |
| **E14** | Validated Absence Registration: registration from absence of detection | Requires k_absence ∈ K_R with cert=1, o=∅ (or o = "absence of X"), V=1 (valid absence). K1 reserves o=∅ slot. K4's default validity applies (non-null → V=1); the absence registration is not null (it carries positive information "X is absent"). The validity conditions for absence (expectation of detection + validated non-occurrence) are beyond K4-K5 scope. | **PARTIAL — K1 o=∅ + K4 default validity structurally accommodate. Specific validity conditions for absence deferred.** |
| **E15** | Intrinsic Relational Binding: entanglement as K-side relation | Relations BETWEEN K-spaces (K_A and K_B correlated via shared quantum state) are not covered by K1-K8, which are primarily intra-K-space axioms. T1 (K_joint) handles embeddings but not the nature of the binding relation itself. | **GAP — Inter-K-space relation structure not axiomatized. Reserved for K-space relation extension.** |
| **E16** | Pre-Measurement Registration Indeterminacy: K-side state before first registration | K1-K7 describe K_R as a set of K-state tuples produced over time. The state BEFORE the first registration event (k_0 or pre-registration K-state) is not defined. | **GAP — Pre-registration K-state not defined. Reserved for K0 (pre-registration axiom).** |

**E8-E16 Audit verdict: 6/9 COVERED or structurally accommodated (E9, E10, E11, E12, E13; E8 partial; E14 partial). 2 gaps (E15, E16). All gaps explicitly documented — no hidden incompatibilities.**

### 3.3 Operational Bridge Preservation Audit

**Question for each bridge:** Do K1-K8 invalidate or alter any operational bridge defined in paper v2.0?

| Bridge | Paper § | What it does | Preservation check | Verdict |
|---|---|---|---|---|
| **Condition A** | §4.3 | Wigner interference → requires_K_joint=1 | K1-K8 do not reference `requires_K_joint` directly. Bridge operates at Level 4 (D_joint). K-space axioms do not force or prevent requires_K_joint=1. | **PASS — Bridge unchanged.** |
| **Condition B** | §4.3 | Direct comparison → requires_K_joint=1 | Same as above. K1-K5 are silent on comparison architecture. | **PASS — Bridge unchanged.** |
| **Condition B2** | §4.3 | LF constraint → requires_K_joint=1 | Same as above. | **PASS — Bridge unchanged.** |
| **Condition C** | §4.3 | No interference → requires_K_joint=0 | K1-K8 do not force K_joint construction. K_R remains isolated unless D_joint demands otherwise. | **PASS — Bridge unchanged.** |
| **Condition D** | §4.3 | Separable state → requires_K_joint=0 | K1-K8 do not reference entanglement or separability (ρ-side properties). | **PASS — Bridge unchanged.** |
| **Condition E** | §4.3 | Independent bookkeeping → requires_K_joint=0 | K1-K8 do not conflate K_R set membership with joint validity demands. | **PASS — Bridge unchanged.** |
| **ODC_K** | §4.6 | Model-fit test for K_joint existence | K1-K8 define K-space structure but do not pre-determine ODC_K outcome. τ remains a free parameter. K4-K7 define validity propagation — ODC_K tests whether a joint model preserving K4-K7 fits data. | **PASS — ODC_K unchanged. K4-K7 provide the validity constraints ODC_K checks.** |

**Operational bridge audit verdict: 7/7 bridges preserved (no bridge broken by K1-K7). However: bridges B, B2, and ODC_K have an indirect semantic dependency on K4-K7 validity structure. K4-K7 define the validity propagation rules that these bridges operationalize. If K4-K7 were to change significantly, the semantic content of these bridges would shift even though their formal predicates (requires_K_joint, D_joint, AdmJoint) remain syntactically unchanged. This is a semantic dependency, not a syntactic break.**

### 3.4 BE Source Lineage Audit

**Question for each axiom:** Is the axiom consistent with its BE structural source?

| Axiom | BE source | BE claim | K-space instantiation | Consistency |
|---|---|---|---|---|
| **K1** | Pramāṇa (cognition as structured event) | A cognition (pramāṇa) has: act, object (prameya), self-awareness (svasaṃvedana), result (phala) | K-state tuple has: M (act), o (object/outcome), cert (self-awareness marker), t (temporal index), V (validity/result status) | **Consistent — 5-field tuple maps onto pramāṇa structure** |
| **K2** | Kṣaṇabhaṅgavāda (momentariness) | Cognition is momentary; no enduring cognitive substance between moments | Registration time is discrete; no K-side identity between consecutive events (Δ lemma) | **Consistent — discrete order matches momentariness without claiming physical time is discrete** |
| **K3** | Svasaṃvedana (self-awareness) | A cognition is self-aware; it illuminates both object and itself without a second cognition | σ_R(M) determined intrinsically within K_R; no M' required | **Consistent — intrinsic certification matches self-awareness** |
| **K4** | Svataḥ prāmāṇya (intrinsic validity) | Validity is intrinsic to cognition; it is the default, not something added by verification | V(k)=1 upon instantiation; no external act required to establish validity | **Consistent — default validity matches intrinsic validity** |
| **K5** | Parataḥ prāmāṇya + Bādhaka pramāṇa | Invalidity is detected extrinsically; a contradicting later cognition (bādhaka) voids the earlier one | V(k)→0 only by later k' with ⊥ and authority; asymmetry: no external function restores V=1 | **Consistent — extrinsic invalidation matches bādhaka structure; asymmetry matches parataḥ** |

**BE lineage audit verdict: 5/5 PASS. Zero inconsistencies between K-space axioms and BE structural sources. Each axiom preserves the "structural extraction, not identity" boundary.**

---

## 4. Six-Condition Test — Derivation from Axioms / Kiểm tra Sáu Điều kiện

**Question:** Can the six conditions for valid registered measurement (paper v2.0 §3.1) be expressed in terms of K1-K8?

| Condition | Original formulation | K-space expression | Derivable? |
|---|---|---|---|
| **C1 (Physical)** | X occurs at ρ-side | Not a K-space condition. C1 is ρ-side — outside K1-K8 scope. | **N/A — ρ-side condition** |
| **C2 (Admission)** | X admitted into K-side as M_X for R | k ∈ K_R with M = M_X. Admission = instantiation of k in K_R. By K1 cert admission rule: cert(k)=1 for all k ∈ K_R. | **K1: k ∈ K_R, cert(k)=1** |
| **C3 (Process membership)** | M_X ∈ R where R = {M_R1, M_R2, ...} | k ∈ K_R, t(k) in the temporal order of K_R. | **K1 + K2: k ∈ K_R with t(k) ordered** |
| **C4 (Self-certification)** | σ_R(M_X) = 1, determined intrinsically | cert(k) = σ_R(M_X) = 1, determined within K_R. | **K3: cert(k) = σ_R(M)** |
| **C5 (Default validity)** | V(M_X) = 1 by default | V(k) = 1 upon instantiation (unless k is null event — K4 exception). | **K4: cert=1 → V=1 (with E9 exception)** |
| **C6 (Non-invalidation)** | No later M' contradicts M_X with authority | No k' > k with k' ⊥ k and Auth(k'→k, C_K)=1 → V(k) stays 1. Pre-closure: provisional. Post-closure (K7): final. | **K5 + K6 + K7** |

**Six-condition test verdict: 5/5 K-side conditions derivable from K1-K8. C1 is ρ-side — correctly outside K-space scope.**

---

## 5. Claim Traceability / Truy vết Claim

| Claim ID | Claim | Claim type | Source | Confidence | Boundary |
|---|---|---|---|---|---|
| C-KAXIOM-001 | K_R is a set of 5-field K-state tuples (K1) | Class C formal definition | This document §1, K1 | High | Not a Hilbert space; not a physical state space |
| C-KAXIOM-002 | (K_R, <_R) is a strict total order (chain) with discrete registration-time (K2) | Class D proposed | This document §1, K2; E6; S2-Δ | High | Registration-time only; not physical time. Total within K_R; partial only in cross-K-space (K_joint). |
| C-KAXIOM-003 | σ_R(M) is determined intrinsically within K_R (K3) | Class D proposed | This document §1, K3; E1 | High | Certifies occurrence, not truth of outcome |
| C-KAXIOM-004 | V(k)=1 by default for self-certified events (K4) | Class D proposed | This document §1, K4; E7 Axiom 1 | High | Default K-side validity, not absolute truth |
| C-KAXIOM-005 | V(k)→0 iff later contradicting act with authority (K5) | Class D proposed | This document §1, K5; E7 Axioms 2-3 | High | Registration-layer only; not physical erasure |
| C-KAXIOM-006 | K_joint exists as colimit of embedding diagram (T1) | Class D proposed | This document §2, T1; paper v2.0 §4.3 | Medium — pending Level 4 freeze | Candidate K_joint, not guaranteed admissible |
| C-KAXIOM-007 | ⊥_K derivable from K1-K5 + AdmJoint failure (T2) | Class D proposed | This document §2, T2; paper v2.0 §4.4 | Medium — pending Level 4 freeze | Registration-layer incommensurability only |
| C-KAXIOM-008 | Bridge_EWF derivable from K5 + EWF config (T3) | Class D/C boundary | This document §2, T3; paper v2.0 §4.5 | Medium — pending Level 4 freeze | EWF-specific; not general LF theorem |
| C-KAXIOM-009 | N-observer joint K-space is colimit; ⊥_K non-transitive (T4) | Class D proposed — NEW | This document §2, T4 | Low — new, unverified for N>2 | Generalization; requires independent verification |
| C-KAXIOM-006a | K6: Auth(k2→k1, C_K)=1 iff shared C_K, V(k2)=1, k1∈scope(D_joint); non-hierarchical, non-transitive (K6) | Class D proposed | This document §1, K6; E7 Axiom 2; paper v2.0 §4.4 | Medium | Structural relation within C_K; not observer hierarchy |
| C-KAXIOM-007a | K7: R closes at t_close when no pending requires_K_joint; V_prov→V_final; post-closure irreversibility absolute (K7) | Class D proposed | This document §1, K7; E7 V_prov/V_final; paper v2.0 §2.2 | Medium | K-side closure only; not physical process termination |
| C-KAXIOM-010 | 2-layer architecture isolates K1-K8 from Level 4 changes in two senses. **(1) Syntactic isolation (unconditional):** K1-K8 axiom text is frozen — Level 4 changes (AdmJoint criteria, D_joint definitions, requires_K_joint scope) do not alter K1-K8 text. **(2) Conditional semantic dependencies (K5/K6/K7):** K5 ⊥_K evaluation is narrowed by Level 4 boundary clauses (F3); K6 Auth evaluation depends on D_joint extensional scope (F6a); K7 t_close timing depends on requires_K_joint extensional scope (F6b). K1-K4 and K8 reference Level 4 for scope identification only or not at all. See §0.5 for full distinction. | Architectural claim | This document §0.5 | High — structural property | Architectural design, not mathematical theorem. Syntactic isolation is unconditional; semantic dependencies are conditional on Level 4 extensional content. |

---

## 6. Non-Overclaim Guardrails / Ranh giới Chống Khẳng định Quá mức

1. **K-space is NOT a Hilbert space.** K_R is a set of registration tuples, not a vector space with inner product. K ≠ H is the core architectural commitment.

2. **K-space axioms do NOT modify Standard QM.** P1-P4, Born rule, Schrödinger equation, and ρ-side dynamics are unchanged.

3. **K-space axioms are NOT physical laws.** They are proposed registration-layer structural definitions (Class D). They do not make empirically testable predictions independent of the operational bridges in paper v2.0.

4. **K-space is registration-logic, not pure mathematics.** The axioms include primitive epistemological predicates (σ, V, ⊥) that have no analogue in standard mathematical spaces. This is intentional — K-space is a different kind of structure than Hilbert space.

5. **Bridge theorems T1-T3 are pending Level 4 freeze.** They derive current paper v2.0 definitions from axioms. If community feedback changes those definitions, T1-T3 are updated — K1-K8 are not. T3 additionally depends on an external philosophical assumption (relativization defense, paper v2.0 §4.5) not derivable from K1-K8.

6. **K1-K8 cover E1-E7, E9, E10, E11, E12, E13.** E8 (multi-step retroactive chain), E14 (validated absence beyond structural accommodation), E15, E16 require extensions deferred to future work. This is explicitly documented in §3.2.

7. **This document does NOT upgrade any paper v2.0 claim class.** All claims remain Class D/C as in the paper. Axiomatization provides the foundation for future upgrades but does not perform them.

8. **BE sources are structural lineage, NOT proof.** Each axiom annotates its BE source for traceability. The BE source is a structural analogue, not empirical evidence for the axiom's truth.

---

## 7. Concrete Model & Proof Attempt — Level 4 Freeze Check / Mô hình Cụ thể & Nháp Chứng minh

**Methodology:** Following the "smallest model first, consistency before derivability" protocol. This section:
1. Defines the smallest concrete EWF model (2 observers, 1 registration event each)
2. Walks K1-K8 for consistency
3. Walks Level 4 definitions for consistency
4. Presents a proof attempt for T2 with gaps explicitly marked

### 7.1 Concrete Model Definition / Định nghĩa Mô hình Cụ thể

**Scenario:** Extended Wigner's Friend (EWF), minimal configuration.

- **Friend F** measures spin of particle S inside sealed laboratory. Outcome: spin-up (|h⟩).
- **Wigner W** performs interference measurement on F's entire laboratory. Registers superposition |Ψ+⟩ = (1/√2)(|h⟩|"saw h"⟩ + |v⟩|"saw v"⟩). No definite o_F preserved as W-side valid claim.

**Concrete K-spaces:**

```
K_F = { k_F }     where k_F = ⟨M_F, |h⟩, 1, t_F, 1⟩

  M_F  = "Friend measures spin of S"
  o_F  = |h⟩  (definite outcome: spin-up)
  cert = 1     (self-certified)
  t_F  = 1     (registration time index)
  V    = 1     (valid by default)

K_W = { k_W }     where k_W = ⟨M_W, |Ψ+⟩, 1, t_W, 1⟩

  M_W  = "Wigner interference measurement on F+S laboratory"
  o_W  = |Ψ+⟩  (superposition: no definite spin-up preserved)
  cert = 1      (self-certified)
  t_W  = 2      (registration time index; after t_F in laboratory history)
  V    = 1      (valid by default)
```

**Model properties:**
- |K_F| = 1, |K_W| = 1 (one event each — smallest non-trivial case)
- F and W are distinct registering systems (R_F ≠ R_W)
- Both are non-null events (o ≠ ∅)

### 7.2 K1-K8 Consistency Walk / Kiểm tra Nhất quán K1-K8

| Axiom | Check on K_F | Check on K_W | Result |
|---|---|---|---|
| **K1** (Carrier) | k_F = ⟨M_F, \|h⟩, 1, 1, 1⟩ is a 5-field tuple. k_F ∈ K_F. cert(k_F) = 1 → admitted. | k_W = ⟨M_W, \|Ψ+⟩, 1, 2, 1⟩ is a 5-field tuple. k_W ∈ K_W. cert(k_W) = 1 → admitted. | ✅ Both satisfy K1 |
| **K2** (Total order) | K_F = {k_F}: singleton. Trivially a strict total order (no pair to compare). Discrete: trivially satisfied. | K_W = {k_W}: singleton. Same reasoning. | ✅ Both satisfy K2 |
| **K3** (Self-cert) | σ_F(M_F) = 1, determined within K_F. No M' ≠ M_F required. No R' ≠ R_F involved. | σ_W(M_W) = 1, determined within K_W. No M' ≠ M_W required. No R' ≠ R_W involved. σ_F and σ_W are independent. | ✅ Both satisfy K3 |
| **K4** (Default V) | cert(k_F) = 1 → V(k_F) = 1 upon instantiation. k_F is non-null (o_F = \|h⟩ ≠ ∅). No E9 exception applies. | cert(k_W) = 1 → V(k_W) = 1 upon instantiation. k_W is non-null (o_W = \|Ψ+⟩ ≠ ∅). No E9 exception applies. | ✅ Both satisfy K4 |
| **K5** (Invalidation) | No k' ∈ K_F with k_F <_F k'. K_F has only one element. No invalidation possible within K_F. V(k_F) remains 1. | No k' ∈ K_W with k_W <_W k'. K_W has only one element. No invalidation possible within K_W. V(k_W) remains 1. | ✅ K5 vacuously satisfied (no later event exists in either K-space) |
| **K6** (Authority) | No pair within K_F to check authority. Vacuously satisfied. | No pair within K_W to check authority. Vacuously satisfied. | ✅ Vacuously satisfied |
| **K7** (Closure) | No pending requires_K_joint involving K_F → K_F closes at t_close = t_F. V_prov(k_F) = 1 → V_final(k_F) = 1. | No pending requires_K_joint involving K_W → K_W closes at t_close = t_W. V_prov(k_W) = 1 → V_final(k_W) = 1. **BUT: see §7.3 — requires_K_joint may be pending, preventing closure.** | ⚠ Conditional — depends on D_joint status (Level 4) |
| **K8** (Embedding) | Intra-K-space: k_F has no embedding to check (K_F is native). Vacuously satisfied. | Intra-K-space: k_W has no embedding to check (K_W is native). Vacuously satisfied. **Tested in K_joint context at L4-7 below.** | ✅ Vacuously satisfied intra-K-space; tested cross-space in §7.3 |

**K1-K8 intra-K-space consistency verdict:**
> K_F and K_W each individually satisfy K1-K8 without contradiction. K5, K6, and K8 are vacuously satisfied because each K-space has only one element. K7 is conditionally satisfied: if requires_K_joint = 1 (Level 4), then closure is blocked until D_joint is resolved, making V_final pending. This is not an inconsistency — it is K7 working as designed. K8's embedding preservation is tested in the cross-space K_joint construction at L4-7.

### 7.3 Level 4 Definitions Walk / Kiểm tra Định nghĩa Tầng 4

Walking through each Level 4 definition (paper v2.0 §4.3-4.5) applied to the concrete model.

**Step L4-1: requires_K_joint predicate**

```
requires_K_joint(F, W) = ?

Check conditions (paper v2.0 §4.3):
  (a) K_F and K_W are each valid within their own K-side?       YES (K4, verified §7.2)
  (b) Are they brought under a shared validity demand D_joint?   YES — EWF setup demands both
      be assessed as parts of one laboratory registration history
  (c) Does D_joint require both to be parts of the same          YES — LF/no-go constraint requires
      registration target/history/validity claim?                 F's and W's outcomes to be assigned
                                                                  simultaneous cross-observer validity
  (d) Can D_joint be evaluated while leaving K_F, K_W            NO — the comparison demands
      in fully independent K-spaces?                              embedding into one candidate K_joint
  (e) Does preserving D_joint require a candidate K_joint?       YES

→ requires_K_joint(F, W) = 1    via Condition A (Wigner interference)
```

| Check | Status |
|---|---|
| Condition A (Wigner interference) | ✅ W performs interference on F+S lab. M_W registers superposition. M_F registers definite outcome. Both concern same lab history. |

**Step L4-2: D_joint predicate**

```
D_joint(K_F, K_W, Arch_EWF) = 1

Arch_EWF = "Extended Wigner's Friend: F measures S inside lab;
            W performs interference on F+S; LF comparison demands
            both claims support one cross-observer validity constraint."

D_joint evaluates to 1 because Arch_EWF demands that K_F and K_W
support one shared registration-validity claim about the same laboratory.
```

| Check | Status |
|---|---|
| D_joint = 1 | ✅ Consistent with paper v2.0 §4.3 definition |

**Step L4-3: Comparison context C_K**

```
C_K exists for (k_F, k_W)?

Check conditions (paper v2.0 §4.4):
  (a) Both acts admitted into same comparison domain?     YES — D_joint demands it
  (b) Both indexed to same registration target/history?   YES — same laboratory F+S
  (c) Comparison does not presuppose both already         YES — comparison TESTS whether
      jointly valid?                                       they can be jointly valid

→ C_K(k_F, k_W) exists.
```

| Check | Status |
|---|---|
| C_K exists | ✅ All three conditions met |

**Step L4-4: Cross-registration authority**

```
Auth(k_W → k_F, C_K) = ?

Check conditions (paper v2.0 §4.4 + K6):
  (a) C_K-sphere(k_F) = C_K-sphere(k_W)?                YES — both in same C_K (L4-3)
  (b) V(k_W) = 1?                                        YES — K4 default, not invalidated
  (c) k_F ∈ scope(D_joint)?                               YES — D_joint demands F's claim
                                                                 be part of joint evaluation

Paper v2.0 §4.4 additional conditions:
  (a') k_W is valid registered measurement?               YES — σ_W(M_W)=1, V(k_W)=1
  (b') k_W's content concerns same target as k_F?         YES — same laboratory F+S
  (c') k_W produced by measurement structurally required   YES — W's interference measurement
       to register state of same system k_F registered?         measures the lab containing F+S
  (d') No arbitrary privilege?                             YES — only temporal ordering
                                                                 and content incompatibility used

→ Auth(k_W → k_F, C_K) = 1
```

| Check | Status |
|---|---|
| Auth = 1 | ✅ All conditions met. k_W has authority over k_F in this C_K. |

**Step L4-5: Registered contradiction ⊥**

```
k_W ⊥ k_F within C_K?

Check K5 minimal definition:
  - k_F registers o_F = |h⟩ (definite outcome)
  - k_W registers o_W = |Ψ+⟩ (superposition; no definite |h⟩ preserved as W-side valid claim)
  - Can both be treated as valid K-side claims within the same C_K?
    NO — |h⟩ is a definite state claim; |Ψ+⟩ is a superposition that does not preserve
    |h⟩ as a valid claim. Within one C_K, claiming both "outcome is definitely |h⟩"
    AND "outcome is superposition with no definite |h⟩" is a registration contradiction.

→ k_W ⊥ k_F within C_K.    [K5 minimal definition satisfied]

Check paper v2.0 §4.4 act-level definition:
  - Same C_K?                                              YES (L4-3)
  - Same registration target?                              YES (same lab F+S)
  - Cannot both satisfy validity conditions?               YES (above)
  - Later act has valid cross-registration authority?       YES (L4-4)

→ M_W ⊥ M_F    [act-level registered contradiction confirmed]
```

| Check | Status |
|---|---|
| k_W ⊥ k_F | ✅ Registration contradiction established |

**Step L4-6: Bridge_EWF**

```
Bridge_EWF(D_joint; M_F, M_W) = ?

Check conditions (paper v2.0 §4.5):
  (a) D_joint requires F-side and W-side registrations to be     YES (L4-2)
      evaluated as jointly valid parts of one lab history?
  (b) M_F registers definite friend-side outcome o_F?            YES — o_F = |h⟩
  (c) M_W registers same lab as coherent superposition with      YES — o_W = |Ψ+⟩,
      no definite o_F preserved as W-side valid claim?                no |h⟩ preserved
  (d) LF/no-go comparison requires both claims to support        YES — by EWF setup
      one cross-observer validity constraint?
  (e) No reinterpretation inside same K_joint can preserve       CHECK — this is the
      both contents without changing validity of at least              relativization
      one side?                                                        defense question

Relativization defense check (paper v2.0 §4.5):
  Could K_joint host meta-descriptions ("within K_F, M_F registered |h⟩")?
  Paper's answer: NO — D_joint demands joint validity of original claims,
  not meta-descriptions. Relativizing abandons D_joint rather than satisfying it.
  This is an EXTERNAL PHILOSOPHICAL COMMITMENT (documented in T3).

→ Bridge_EWF(D_joint; M_F, M_W) = 1    [assuming relativization defense holds]
```

| Check | Status |
|---|---|
| Bridge_EWF = 1 | ✅ All conditions met (conditional on relativization defense — external assumption) |

**Step L4-7: AdmJoint check**

```
Does an admissible K_joint(K_F, K_W) exist?

Candidate K_joint = i_F(K_F) ∪ i_W(K_W) = { i_F(k_F), i_W(k_W) }

Check AdmJoint conditions (paper v2.0 §4.3):
  (i)   Embeddings preserve act, outcome, cert, time/order, V?
        i_F(k_F) = ⟨M_F, |h⟩, 1, t_F, V_joint(k_F)⟩
        i_W(k_W) = ⟨M_W, |Ψ+⟩, 1, t_W, V_joint(k_W)⟩
        Act, outcome, cert preserved? YES.
        Order: t_F < t_W in lab history → i_F(k_F) <_joint i_W(k_W). YES.
        V preservation by K8: V_joint(i(k)) = V_original(k) at embedding time.
        K8 guarantees V(k_F)=1 and V(k_W)=1 carry into K_joint.          ✅ K8

  (ii)  Self-certification intrinsic to each embedded act?
        σ_F(M_F) = 1 in K_joint? Must remain intrinsic → not redefined by K_joint. YES.
        σ_W(M_W) = 1 in K_joint? Same. YES.                              ✅

  (iii) Conditions 1-6 satisfied for each embedded structure?
        For i_F(k_F): C1-C5 carry over. C6 (non-invalidation) → CHECK:
          Is there k' in K_joint with k' ⊥ i_F(k_F) and Auth?
          → i_W(k_W) ⊥ i_F(k_F) within C_K (established in L4-5)
          → Auth(i_W(k_W) → i_F(k_F), C_K) = 1 (established in L4-4)
          → K5 FIRES: V(i_F(k_F)) → 0                                    ⚠ CONFLICT
        For i_W(k_W): C1-C6 → no later event contradicts k_W in K_joint. OK.  ✅

  (iv)  No required registration-state update invalidates either embedded
        structure while both claimed as jointly valid?
        → K5 just fired: V(i_F(k_F)) → 0 while both were claimed jointly valid.
        → AdmJoint condition (iv) VIOLATED.                                ❌ FAILS

→ AdmJoint(K_joint; K_F, K_W) = 0    [no admissible K_joint exists for this model]
```

| Check | Status |
|---|---|
| AdmJoint = 0 | ❌ Condition (iv) violated via K5 conflict |

**Step L4-8: ⊥_K conclusion**

```
K_F ⊥_K K_W?

  requires_K_joint(F, W) = 1?                              YES (L4-1)
  ∃ admissible K_joint?                                     NO  (L4-7)

→ K_F ⊥_K K_W    [K-side incommensurability holds in this model]
```

| Check | Status |
|---|---|
| K_F ⊥_K K_W | ✅ Incommensurability established for this concrete model |

### 7.4 Consistency Verdict / Kết luận Nhất quán

> **The concrete model is internally consistent.** Walking K1-K8 on K_F and K_W individually produces no contradiction. Walking Level 4 definitions on the joint scenario produces a well-defined chain:
>
> requires_K_joint = 1 → D_joint = 1 → C_K exists → Auth = 1 → k_W ⊥ k_F → Bridge_EWF = 1 → K5 fires in K_joint → AdmJoint(iv) fails → K_F ⊥_K K_W.
>
> Each step follows from the previous without circular reasoning within THIS model. The concrete model serves as **evidence of consistency** (a satisfying model exists for all axioms simultaneously).

**Identified gaps (not inconsistencies):**

| # | Gap | Severity | Location |
|---|-----|----------|----------|
| G1 | Relativization defense is external philosophical commitment (unavoidable in any measurement framework) | Medium | L4-6, step (e). Documented in T3. |
| G2 | K7 closure conditional on D_joint resolution | Low | §7.2 K7 row. Working as designed. |
| G3 | K5 minimal ⊥ definition used here; full Level 4 ⊥ formalization not frozen | Medium | L4-5. Documented in Open Item #14. |

### 7.5 T2 Proof Attempt / Nháp Chứng minh T2

**Goal:** Derive K_F ⊥_K K_W from K1-K8 + Level 4 definitions in the concrete model.

**Statement to prove:**
> In the EWF concrete model (§7.1): if requires_K_joint(F,W) = 1 via D_joint, and Bridge_EWF(D_joint; M_F, M_W) = 1, then K_F ⊥_K K_W.

**Proof attempt:**

```
Step 1 — Setup (SOLID ✅):
  K_F = {k_F} with k_F = ⟨M_F, |h⟩, 1, 1, 1⟩.     [K1: well-formed tuple, cert=1]
  K_W = {k_W} with k_W = ⟨M_W, |Ψ+⟩, 1, 2, 1⟩.    [K1: well-formed tuple, cert=1]
  σ_F(M_F) = 1, σ_W(M_W) = 1, independent.           [K3: intrinsic self-certification]
  V(k_F) = 1, V(k_W) = 1 by default.                  [K4: cert=1 → V=1, non-null]

Step 2 — requires_K_joint (SOLID ✅, modulo Level 4 definition):
  requires_K_joint(F, W) = 1.
  Justification: Condition A — W performs interference on F+S lab.
  D_joint(K_F, K_W, Arch_EWF) = 1.
  Source: paper v2.0 §4.3 definition. Applied correctly in L4-1, L4-2.
  Confidence: HIGH — direct application of sufficient condition A.

Step 3 — C_K and Auth (SOLID ✅):
  C_K(k_F, k_W) exists.                               [L4-3: all three conditions met]
  Auth(k_W → k_F, C_K) = 1.                           [K6 + L4-4: all conditions met]
  Confidence: HIGH — mechanical check of conditions.

Step 4 — Registered contradiction (SOLID ✅ at K5 minimal level):
  k_W ⊥ k_F within C_K.
  Justification: o_F = |h⟩ (definite), o_W = |Ψ+⟩ (superposition, no |h⟩ preserved).
  These cannot both be valid K-side claims within one C_K.
  Source: K5 minimal definition.
  Confidence: HIGH for K5 minimal. MEDIUM for full Level 4 ⊥ (not frozen).
  ⚠ GAP G4: Full Level 4 ⊥ boundary clauses not frozen. K5 minimal used here
  is self-contained but may need revision if Level 4 changes ⊥ semantics.

Step 5 — Bridge_EWF (MEDIUM ⚠ — external assumption):
  Bridge_EWF(D_joint; M_F, M_W) = 1.
  Justification: All conditions (a)-(d) mechanically checked in L4-6.
  Condition (e) — "no reinterpretation preserves both" — depends on
  relativization defense (paper v2.0 §4.5).
  ⚠ GAP G2: Relativization defense is an external philosophical commitment.
  If rejected, Bridge_EWF = 1 does not follow from K1-K8 alone.
  Confidence: MEDIUM — conditional on external assumption.

Step 6 — K5 fires in candidate K_joint (SOLID ✅, modulo EP):
  By K8: embeddings i_F, i_W preserve V values.         [K8: V_X(i(k)) = V_R(k)]
  In candidate K_joint:
    i_F(k_F) <_joint i_W(k_W)                          [K2: t_F < t_W]
    i_W(k_W) ⊥ i_F(k_F) within C_K                    [Step 4]
    Auth(i_W(k_W) → i_F(k_F), C_K) = 1                 [Step 3]
    → K5: V(i_F(k_F)) → 0                              [K5 invalidation rule]
  This happens while D_joint claims both as jointly valid.
  → AdmJoint condition (iv) violated.
  Confidence: HIGH — direct K5 + K8 application. No gap.

Step 7 — Conclusion (SOLID ✅):
  requires_K_joint(F, W) = 1                            [Step 2]
  ¬∃ K_joint: AdmJoint(K_joint; K_F, K_W) = 1          [Step 6]
  → K_F ⊥_K K_W                                         [Definition of ⊥_K, paper v2.0 §4.4]
  ∎ (conditional)
```

### 7.6 Proof Attempt Assessment / Đánh giá Nháp Chứng minh

| Step | Confidence | Depends on | Gap? |
|------|-----------|------------|------|
| 1 (Setup) | HIGH | K1, K3, K4, K8 | None |
| 2 (requires_K_joint) | HIGH | Level 4 §4.3 Condition A definition | Level 4 not frozen |
| 3 (C_K, Auth) | HIGH | K6 + Level 4 §4.4 | Level 4 not frozen |
| 4 (⊥ contradiction) | HIGH/MEDIUM | K5 minimal / Level 4 full ⊥ | **G3**: Level 4 ⊥ not frozen |
| 5 (Bridge_EWF) | MEDIUM | External philosophical assumption | **G1**: Relativization defense |
| 6 (K5 in K_joint) | HIGH | K5 + K8 | None (resolved by K8) |
| 7 (Conclusion) | HIGH | Steps 2+6 + ⊥_K definition | Level 4 definition |

**Overall assessment:**
> The proof attempt is **valid conditional on two remaining identified dependencies** (G1, G3). Neither is an internal contradiction — one is a philosophical boundary, one is a temporal dependency:
>
> - **G1 (Relativization defense)**: Unavoidable philosophical commitment — not derivable from ANY axiom set. Every measurement framework must take a stance on what counts as "satisfying a joint validity demand." Documented as a semantic boundary, not a mathematical gap.
> - **G3 (Level 4 ⊥ freeze)**: Temporal dependency — resolves when paper v2.0 Level 4 boundary clauses are frozen. K5 minimal ⊥ is sufficient for the concrete model.
>
> **Former EP gap (G1 in v1.3): RESOLVED.** EP promoted to K8 (v1.4) — V-preservation through cross-space embedding is now a core axiom. The proof chain no longer depends on an external postulate for Step 6.
>
> The circularity concern from v1.2 Open Item #14 is **not present in this concrete model** because K5's minimal ⊥ definition is sufficient for Step 4 without invoking Level 4's full ⊥ formalization. The circularity only appears in the GENERAL case where T2 needs AdmJoint conditions that reference full ⊥. In the concrete model, ⊥ is directly verified by content inspection (|h⟩ vs |Ψ+⟩).

### 7.7 Next Steps / Bước Tiếp theo

Following the 5-step methodology:

| Step | Status | Timeline estimate |
|------|--------|-------------------|
| ✅ Step 1 — Concrete Model (§7.1-7.4) | **DONE** — consistency established | — |
| ✅ Step 2 — Proof attempt for T2 (§7.5-7.6) | **DONE** — 2 remaining dependencies (G1: relativization; G3: Level 4 ⊥ freeze). Former EP gap resolved by K8. | — |
| ⬜ Step 3 — Submit K-Axiom + Concrete Model to PhilSci | Ready for community review | 1-2 weeks |
| ⬜ Step 4 — Based on feedback, decide: close remaining gaps or find collaborator | Pending feedback | After Step 3 |
| ⬜ Extension — Generalize from N=2 to N>2 | T4 verification (Open Item #9) | After Step 4 |

**Decision point after community feedback:**
- If gaps G1, G3 are accepted as documented → Level 4 freeze proceeds
- If G1 (relativization) is challenged → T3 needs revision, but K1-K8 unchanged (this is a philosophical/semantic challenge, not mathematical)
- If consistency check reveals new issues → return to concrete model, extend

---

## 8. Open Items / Các mục Để Mở

| # | Item | Status | Priority |
|---|------|--------|:--------:|
| 1 | Multi-step retroactive chain (E8 extension) | Deferred — K5 single-step; K7 pre-closure allows re-assessment of invalidating acts | Medium |
| 2 | Null K-state full formalization (E9 detailed operationalization) | Partial — K1 o=∅ + K4 E9 exception structurally accommodate null events. Detailed operationalization deferred. | Low-Medium |
| 3 | Validated absence validity conditions (E14 extension) | Partial — K1 o=∅ + K4 default validity structurally accommodate. Specific absence validity conditions deferred. | Medium |
| 4 | Inter-K-space relation structure (E15 extension) | Deferred — new axiom needed | Low-Medium |
| 5 | Pre-registration K-state (E16 extension / K0) | Deferred — new axiom needed | Low-Medium |
| 6 | Pre-symbolic registration stratum (E4 formalization) | Deferred — K-space stratification | Low |
| 7 | Equivalence of σ(M) and R̂_svasa formalisms | Deferred — separate research track (paper v2.0 §7.2 item #4) | Low |
| 8 | Full semantic proof for Bridge_EWF "no admissible reinterpretation" | Pending Level 4 freeze + T3 completion. External assumption (relativization defense) documented. | High |
| 9 | T4 N>2 verification | Requires multi-observer EWF modeling | Medium |
| 10 | Update paper v2.0 Section 7.2 deferred item #5 status | After community feedback on this document | Low |
| 11 | RCA re-audit after community feedback | After Level 4 freeze and T1-T3 finalization | High |
| 12 | K6 Auth non-transitivity edge cases (circular authority chains) | **Resolved v1.2** — counterexample provided in K6 formal block. Remaining: N≥3 exotic topologies. | Low |
| 13 | Embedding Postulate (EP) promotion decision | **Resolved v1.4** — EP promoted to K8 (Cross-Space Embedding Preservation). K8 is now a frozen Layer 1 core axiom. T1-T3 no longer depend on an external postulate for V-preservation. | ~~High~~ → Resolved |
| 14 | T2 circularity resolution — Level 4 ⊥ freeze | T2 derivation is conditional on Level 4 ⊥ formalization being consistent with K5 minimal definition. Circularity resolves when Level 4 freezes. **v1.3 update:** Circularity NOT present in concrete model (§7.5 Step 4) — K5 minimal ⊥ is directly verifiable by content inspection (|h⟩ vs |Ψ+⟩). Circularity remains only in general case. | **High** |
| 15 | Concrete model gaps G1-G3 (§7.4) | G1 (Relativization): unavoidable philosophical commitment in any measurement framework. G2 (K7 closure): working as designed. G3 (Level 4 ⊥): see #14. All gaps are external dependencies, not internal contradictions. **v1.4:** Former EP gap resolved by K8. Renumbered G1-G4 → G1-G3. | Medium |

---

## 9. Cross-References / Tham chiếu Chéo

| Document | Relationship |
|---|---|
| `papers/.../VVV-QMRF_Working_Paper_v2.0.md` | Downstream — K-space axioms are the foundation for §3-4 structural definitions |
| `meta_architecture/vvv_qmrf_meta_architecture_registration_layer_formalization.md` | Upstream — Defines the K-state tuple, σ(M), V(M), and the symbol registry that K1-K5 axiomatize |
| `framework/vvv_qmrf_framework_e01_self_certifying_registration_postulate.md` | Upstream — Source for K3 |
| `framework/vvv_qmrf_framework_e06_registering_system_as_process_postulate.md` | Upstream — Source for K2 |
| `framework/vvv_qmrf_framework_e07_registration_validity_location_postulate.md` | Upstream — Source for K4, K5 |
| `synthesis/vvv_qmrf_synthesis_s3_registering_system_as_process_foundation.md` | Upstream — Source for K2 discreteness (Δ lemma) |
| `SYSTEM_Buddhist_Epistemology/system_be_full.md` | Diagonal — BE SOT for lineage annotations |
| `vvv-qmrf/schema_guide.md` | Process — Document creation contract; this document follows schema |

---

## 10. Level 4 Freeze Check — Internal Consistency Verdict / Phán quyết Nhất quán Nội tại

### 10.1 Question / Câu hỏi

> Can the Level 4 definitions (⊥_K, AdmJoint, D_joint, requires_K_joint, Bridge_EWF, C_K, Auth) be formally proven consistent with K1-K8 without external confirmation?

### 10.2 RCA Trace / Truy vết RCA

| Step | Question | Answer |
|------|----------|--------|
| **Define** | What is the "Level 4 freeze check"? | A formal proof that all Level 4 definitions from paper v2.0 §4.3-4.5 are consistent with Layer 1 axioms K1-K8 — no contradiction arises when combining them. |
| **Trace (Why 1)** | Why is this needed? | Level 4 is currently the least stable layer (in community review). Before freezing it, internal consistency must be established so that community feedback does not hit contradictions that could have been caught internally. |
| **Trace (Why 2)** | Why is it hard? | Because Level 4 definitions were designed bottom-up (from EWF use case) while K1-K8 were designed top-down (from BE structural sources). The two directions may not converge. Plus, Level 4 uses complex primitives (⊥, Authority, C_K) whose full formalization is not yet frozen. |
| **Trace (Why 3)** | Why can't it be purely internal? | Because one Level 4 dependency — the relativization defense (Bridge_EWF condition (e), paper v2.0 §4.5) — is a SEMANTIC choice about what counts as "satisfying D_joint." No measurement framework can derive this from its own axioms — it's a Gödel-like semantic boundary. Every framework (Copenhagen, Many-Worlds, QBism, VVV-QMRF) must take an irreducible philosophical stance on joint validity. |
| **Isolate** | What are the blockers? | (1) Relativization defense = unavoidable philosophical commitment (not a mathematical gap). (2) Full Level 4 ⊥ boundary clauses = not yet frozen (temporal dependency). (3) General case proof (arbitrary |K_R| and N observers) = requires stronger mathematical foundations. |
| **Fix cause** | What CAN be done internally? | Promote EP → K8 (DONE v1.4). Concrete model consistency proof (DONE v1.3). Edge case testing. General case proof sketch with explicit boundary documentation. |
| **Verify** | How to verify? | Walk every Level 4 definition against K1-K8 in the concrete model (§7). Check no contradiction arises. Document what IS proven vs. what depends on external assumptions. |

### 10.3 What CAN Be Proven Internally / Có thể Chứng minh Nội tại

| # | Statement | Status | Confidence |
|---|-----------|--------|:----------:|
| P1 | K1-K8 are internally consistent (concrete model: 2 observers, 1 event each) | **PROVEN** (§7.2-7.4) | HIGH |
| P2 | Level 4 definitions can be expressed in terms of K1-K8 primitives | **PROVEN** (§7.3) | HIGH |
| P3 | The derivation chain requires_K_joint → D_joint → C_K → Auth → ⊥ → Bridge_EWF → K5 fires → AdmJoint fails → ⊥_K is well-defined (no circular reasoning) | **PROVEN** (§7.3, §7.5) | HIGH |
| P4 | Step 6 (K5 fires in K_joint) does NOT depend on any external postulate | **PROVEN** (v1.4: K8 resolves former EP gap) | HIGH |
| P5 | K5 minimal ⊥ can be verified by content inspection without invoking Level 4 full ⊥ (circularity absent in concrete model) | **PROVEN** (§7.5 Step 4) | HIGH |
| P6 | K_joint candidate existence is derivable from K1-K8 + Level 4 scope identifiers | **PROVEN** (T1, updated v1.4) | HIGH |

### 10.4 What CANNOT Be Proven Internally / Không thể Chứng minh Nội tại

| # | Statement | Why not | Nature of boundary |
|---|-----------|---------|-------------------|
| E1 | Relativization defense: "meta-descriptions do not satisfy D_joint" | Semantic choice about the nature of joint validity — not derivable from ANY axiom set | **Philosophical commitment** (unavoidable in every measurement framework) |
| E2 | Full Level 4 ⊥ boundary clauses are correct | Still in community review (paper v2.0). Internal consistency with K5 minimal ⊥ can be checked, but community may disagree with boundary clauses. | **Temporal dependency** (resolves when Level 4 freezes) |
| E3 | General case proof (arbitrary N, arbitrary |K_R|) | Requires stronger mathematical foundations (structural induction proofs, category-theoretic colimit properties for N>2). | **Mathematical capacity boundary** (documented honestly) |

### 10.5 Final Verdict / Phán quyết Cuối cùng

> **Level 4 definitions ARE internally consistent with K1-K8 in the concrete model.**
>
> The proof chain has exactly **one irreducible external dependency**: the relativization defense (a philosophical commitment about what counts as satisfying D_joint). This is NOT a gap — it is a **semantic boundary** present in every measurement framework. Copenhagen chooses "Heisenberg cut," Many-Worlds chooses "decoherence branching," QBism chooses "agent belief update," VVV-QMRF chooses "relativization defense." No framework can derive its semantic boundary from its own axioms.
>
> **Decision:** Level 4 can freeze with **one documented external philosophical commitment** (relativization defense). The former EP gap (G1 in v1.3) is resolved by promoting EP → K8. The ⊥ circularity concern (Open Item #14) is absent in the concrete model. The remaining temporal dependency (Level 4 ⊥ full boundary clauses) resolves when paper v2.0 exits community review.
>
> **Confidence level for Level 4 freeze:** **MEDIUM-HIGH.** Internal consistency is proven for the relevant model class. The only blocker is the philosophical commitment that every measurement framework must make.

### 10.6 Remaining Action Items After Freeze / Các Mục Hành động Sau Freeze

| # | Item | Priority | Blocks |
|---|------|:--------:|--------|
| A1 | Document relativization defense as "Axiom of Joint Validity Semantics" (separate from K1-K8) | High | T3 completeness |
| A2 | Freeze Level 4 ⊥ boundary clauses after community feedback resolves Open Item #14 | High | T2 non-circularity in general case |
| A3 | General case proof (structural induction on |K_R|, N observers) | Medium | T4, E8, E15 |
| A4 | Edge case: E9 null events, E14 validated absence | Medium | E8-E16 audit phase |
| A5 | Category-theoretic formalization of K_joint as colimit (N>2) | Low-Medium | T4 |

---

*Document v1.4 — 2026-05-19 — VVV-QMRF §K-AXIOM*
*Status: Class D (proposed). All axioms and theorems are proposed registration-layer definitions.*
*Layer 1 (K1-K8): Frozen. Layer 2 (T1-T4): Updatable pending Level 4 freeze.*
*RCA audit (v1.3 → v1.4): (1) EP promoted to K8 (Cross-Space Embedding Preservation) — Layer 1 now has 8 core axioms. K8 guarantees V-preservation through cross-space embeddings. (2) T1 derivation updated: V-preservation now from K8, not external postulate. Former EP gap (G1) RESOLVED. (3) T2 proof attempt gaps reduced from 3 to 2: only relativization defense (G1, philosophical) and Level 4 ⊥ freeze (G3, temporal) remain. (4) Concrete model §7 updated: K8 consistency walk, AdmJoint check (i) now derives from K8. (5) §10 Level 4 Freeze Check verdict added: internal consistency PROVEN for concrete model; relativization defense documented as unavoidable semantic boundary. (6) Open Item #13 closed (EP → K8). Open Items #14, #15 updated.*
*Previous (v1.2 → v1.3): (1) Concrete model §7 added: minimal EWF (2 observers, 1 event each). K1-K7 consistency walk completed — no contradictions. Level 4 definitions walk completed — derivation chain verified. (2) T2 proof attempt with 3 gaps. (3) Circularity shown absent in concrete model. (4) Open Items #14, #15 added.*
*Previous (v1.1 → v1.2): K2 corrected to total order. T1 EP gap acknowledged. K6 non-transitivity counterexample. T2 circularity acknowledgment.*
*Previous (v1.0 → v1.1): Added K6, K7, K4 E9 exception, K5 minimal ⊥ definition, K1 cert admission rule. Fixed T1 V-preservation (EP), T2 sufficient-vs-necessary, T3 external assumption.*
*Next: PhilSci submission → Community feedback → Level 4 ⊥ boundary clauses freeze (resolves #14) → T1-T3 finalization → N>2 generalization (T4, #9) → E8-E16 extension audit phase.*
