Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# K-Space Axiomatization — Registration-Logic Foundation for VVV-QMRF
# Tiên đề hóa Không gian K — Nền tảng Registration-Logic cho VVV-QMRF

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)
**Document type:** `meta_architecture`
**Date:** 2026-05-19
**Version:** 2.1
**Author:** VietVunVut (Viet - Nguyen Xuan)
**Status:** v2.1 — algebraic layer extension. Layer 1 (K1-K8) is frozen; Layer 2 extended with T5-T7. **STATUS AUDIT (2026-05-23):** This document is PURELY STRUCTURAL — contains zero probability equations, zero numerical values, zero experimental data, zero data comparisons. K9_E probability postulate exists only in separate plan documents (not part of this axiomatization). See §0.6 for full audit. Claim boundary: K1 is Class C; K2-K8 and T1-T7 remain Class D proposed registration-layer structures unless separately upgraded.
**Source:** Derived from VVV-QMRF Working Paper v2.0 Section 7.2 deferred item #5
**Cite:** VVV-QMRF §K-AXIOM
**Plan reference:** `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/plan/VVV-QMRF_K_Space_Axiomatization_Plan.md`

**Scope:** Formal registration-logic axioms, bridge theorems, and current open items only. Historical sprint, audit, proof-attempt, and freeze-check records are kept in `CHANGELOG.md`.
**Level 4 revision governance:** Semantic changes to Level 4 predicates (`D_joint`, `requires_K_joint`, `AdmJoint`, `⊥_K`, `Bridge_EWF`, `ODC_K`) are controlled by `vvv_qmrf_meta_architecture_level_4_unfreeze_gate.md`. Non-semantic clarifications do not unfreeze Level 4.
**Out of scope:** This document does not modify Standard Quantum Mechanics, does not change any VVV-QMRF postulate (E1-E16), does not upgrade claim classes of paper v2.0, and does not claim K-space is a canonical QM object.

> **DISCLAIMER / CẢNH BÁO:** VVV-QMRF is independent Class D personal research, not Standard Quantum Mechanics, not peer-reviewed or experimentally validated, and not for real-world technical use. Full boundary protocol: `DISCLAIMER.md`.

---

### 0.6 Status Audit — What This Document Contains and Does NOT Contain

*Added 2026-05-23 — RCA Status Audit v2*

> [!CAUTION]
> **This document is PURELY STRUCTURAL.** It contains axioms (K1-K8), bridge theorems (T1-T7), and open items. It does NOT contain any of the following:
>
> - ❌ **No probability equation.** No `P(o|k,Exp) = ...` formula. No K9 postulate.
> - ❌ **No numerical values.** No 0.73, 0.5, π, ℏ, or any computed number.
> - ❌ **No experimental data.** "Proietti" does not appear. No S_exp, no error bars.
> - ❌ **No data comparison.** No fit, no χ², no graph, no table of results.
> - ❌ **No numerical prediction.** No computed observable for any experiment.
> - ❌ **No β parameter.** No free parameter. No suppression strength.
>
> **K-space (as axiomatized in this document) does NOT fit EWF at any level.**
> Not "fit partially." Not "fit weakly." Zero computation has been performed.
>
> T3 (Bridge_EWF, §Layer 2) connects K-space vocabulary (⊥_K) to EWF scenarios, but this is a **definitional labeling** — it says "in EWF, ⊥_K fires" — not a quantitative fit.
>
> Separate analysis documents (`plan/Phase7-13`, `fits/`) contain K9_E work, but:
> - K9_E is a POSTULATE, not derived from K1-K8
> - Data fitting in those documents is CIRCULAR (reconstructed data, not extracted)
> - Two code implementations use different formulas
>
> See `CHANGELOG.md` §17 and §18 for full audit and prediction records.

| Content type | Present in this document? | Where it exists (if anywhere) |
|---|---|---|
| Axioms (K1-K8) | ✅ 8 axioms, Layer 1 frozen | This document §1 |
| Bridge theorems (T1-T7) | ✅ 7 theorems, Layer 2 | This document §2 |
| Probability equation (K9) | ❌ | `plan/Phase8_candidate_equation.md` (POSTULATE) |
| Numerical values | ❌ | `fits/k9e_predictor.py` (ad-hoc approximation) |
| Experimental data | ❌ | `fits/d1_blk1_4point_fit.py` (CIRCULAR reconstruction) |
| Data comparison / fit | ❌ | `plan/Phase10_data_fitting.md` (CIRCULAR) |
| Numerical predictions | ❌ | `plan/Phase11_3observer_prediction.md` (conditional on postulate) |

---

## 0. RCA Motivation / Động lực RCA

### 0.1 Define — Symptom vs. Cause

| | |
|---|---|
| **Symptom** | Working paper v2.0 Section 7.2 lists "Axiomatize K as a full mathematical structure" as a deferred item. Three other deferred proof items (`Bridge_EWF` semantic proof, `⊥_K` mathematical proof, `AdmJoint` necessary-and-sufficient conditions) are all blocked by the absence of axiomatized K-space. |
| **Root cause** | K is defined **extensionally** (as a collection of tuples `k = ⟨M, o, cert, t, V⟩`) rather than **intensionally** (via axioms that determine the properties of the space). All operations on K (embedding, union for `K_joint`, `⊥_K`, validity propagation) are defined ad-hoc per use case rather than derived from an axiomatic structure. |

### 0.2 Trace — 5 Whys

*(Note: The questions below trace the RCA Motivation — why axiomatization is needed now. This is a "Why is this the right fix?" trace, not a backward causal trace from symptom to deeper cause. The backward causal trace is: K extensional → no admission rule → axioms undefined → proofs blocked. The motivation trace and causal trace are complementary; both are valid RCA phases.)*

1. **Why needed?** VVV-QMRF uses K as a "space" in formal claims without mathematical foundation.
2. **Why now?** Three deferred proof items in paper v2.0 are blocked by this absence.
3. **Why not before?** Paper achieved Class C/D claims with structural definitions; operational bridges sufficed.
4. **Why is this right timing?** Paper formal chain is complete (Section 7.2). Axiomatization now serves dual purpose: foundation for proof upgrades AND quality audit of the paper's formal chain before community feedback arrives.
5. **Root cause:** K was introduced architecturally (`K ≠ H`) but never given formal axiomatic definition. This was intentional architectural debt to prioritize operational contact. Debt is now due.

### 0.3 Isolate — The Gap

K is currently a **collection** without structure. To be a **space**, it requires at minimum:
- **Axiomatized membership rule** — an admission criterion determining which tuples belong to K_R (K already has an extensional collection of tuples per §0.1; what it lacks is a formal membership axiom with cert-based admission rule and structural guarantees)
- **Order structure** — temporal ordering of registration events
- **Validity structure** — how validity propagates through order
- **Operations** — embedding (morphism between K-spaces), joint construction (for `K_joint`)

### 0.4 Fundamental Design Decision

K-space is NOT a pure mathematical space. It is a **registration-logic structure**: a mathematical carrier (chain within each K_R, partial order across K_R via embeddings, with morphisms preserving structure) whose primitive predicates are epistemological (`cert`, `V`, `⊥`). This is not Hilbert space, not phase space, not probability space — these are all (math + math). K-space is (math + registration-logic). The mathematical structure is the **carrier**, not the **content**.

### 0.5 2-Layer Architecture

```
Layer 1 — CORE AXIOMS (K1-K8): Frozen (syntactic)
  Based on dependency stack Level 0-3 (BE SOT, K≠H, E1-E7, K-state tuple).
  K1-K8 axiom TEXT does not depend on Level 4 — text is unconditionally frozen.
  K5/K6/K7 have CONDITIONAL SEMANTIC DEPENDENCIES on Level 4:
    - K5 firing narrows by Level 4 ⊥_K boundary clauses
    - K6 Auth depends on D_joint extensional scope
    - K7 t_close timing depends on requires_K_joint extensional scope
  K1-K4 and K8 carry NO Level 4 semantic dependencies.
  See §5 C-KAXIOM-010 for full 2-part syntactic/semantic isolation breakdown.

Layer 2 — BRIDGE THEOREMS (T1-T3 pending Level 4 freeze + T4 new Class D): Updatable
  T1-T3: Connect core axioms to Level 4 structural definitions; updatable when Level 4 changes.
  T4: New Class D theorem (N-observer generalization); independently updatable; requires
      separate verification not tied to Level 4 freeze.
  All bridge theorems updatable without changing K1-K8 text.
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

  ⚠ Structural-constant clarification (PG-01):
  Within K_R, cert is effectively a structural constant: cert(k) = 1 for ALL k ∈ K_R
  by the admission rule above. The declaration cert ∈ {0,1} does NOT imply cert can
  take value 0 inside K_R — it records the type of the field at the boundary. The
  discriminating role of cert (filtering cert=0 events) is exercised at the K_R
  admission boundary, not inside K_R. Once k is inside K_R, cert(k)=1 is invariant.

Injection constraint (t-injectivity):
  t restricted to K_R is injective:
    ∀k1, k2 ∈ K_R: t(k1) = t(k2) → k1 = k2.
  Reason: registration events within K_R are identified by their timestamp;
  two distinct k cannot share t within the same K_R. This is a definitional
  property of the registration process: if two acts share a timestamp in K_R,
  they are the same registration act. The constraint is required for K2
  totality and RegistrationState well-definedness (see K2).

K_R is produced by registering system R over time.
K_R is finite or countably infinite (a consequence of K2 discreteness — see K2 S2-Δ lemma).
```

| Property | Value |
|---|---|
| **Source** | Level 3: K-state tuple from `meta_architecture/vvv_qmrf_meta_architecture_registration_layer_formalization.md` §1 |
| **BE lineage** | Pramāṇa — cognition as structured event: act (pramāṇa), object (prameya), self-awareness (svasaṃvedana), result (phala), validity |
| **Claim class** | C (conjectural VVV-QMRF formal definition) |
| **Dependency** | Level 3 (K-state tuple). No Level 4 dependency. |
| **Boundary** | `K_R` is not a Hilbert space, not a set of physical density matrices, not a probability space. Elements `k` are registration states — they record what was registered, not what physically exists. The `o = ∅` slot is reserved for E9 (null event) and E14 (validated absence). K4 operationalizes E9 via the `isNull(k) := o(k) = ∅ ∧ ΔI(k) = 0` guard (cert=1 ∧ isNull(k) → V=0 by definition); E14 (validated absence) accommodation is structural only (see Open Item #3). |
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
                        [all elements comparable — follows from K1 t-injectivity]

  Totality proof (from K1 injection constraint):
    Take k1, k2 ∈ K_R with k1 ≠ k2.
    By K1 t-injectivity: t(k1) ≠ t(k2).
    By T_R strict total order: t(k1) < t(k2)  ∨  t(k2) < t(k1).
    By <_R definition: k1 <_R k2  ∨  k2 <_R k1.  ∎

Discreteness (S2-Δ lemma):
  Define: RegistrationState: T_R → (K_R ∪ {∅})
          RegistrationState(t) = k    if ∃k ∈ K_R with t(k) = t
          RegistrationState(t) = ∅    otherwise
  (Well-defined: K1 t-injectivity guarantees at most one k per distinct t in K_R;
   K2 strict total order then ensures the map is well-defined.)
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
Act-token convention:
  M_K is a set of measurement-registration act TOKENS (unique event identifiers).
  Two registration events of the same act-type but different timestamps are
  distinct M_K members: token(M_1) ≠ token(M_2) even if type(M_1) = type(M_2).
  K5 and T1 apply token-level reasoning; act-type reasoning requires separate notation.

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
> For any k ∈ K_R with ¬isNull(k), the validity status V(k) = 1 upon instantiation of k in K_R. [cert(k) = 1 for all k ∈ K_R by K1 admission rule — not restated here.] Validity is the default state of a non-null registration event; it does not require external confirmation. For isNull(k), V(k) = 0 by K4(b). All k ∈ K_R are covered by one of the two clauses.

**Formal:**
```
isNull(k) :=  o(k) = ∅  ∧  ΔI(k) = 0
              (E9 null event: interaction occurred but zero information transfer)

For all k ∈ K_R:
  (a) ¬isNull(k)  →  V(k) = 1   (upon instantiation: non-null self-certified events
                                  are valid by default)
  (b)  isNull(k)  →  V(k) = 0   (E9 null events: o=∅ ∧ ΔI=0 → zero information
                                  transfer → V=0 by K4 formal convention)

Joint exhaustiveness:
  K1 admission rule (cert=1) + isNull dichotomy partition all k ∈ K_R.
  K4 defines V for both branches: no k has V undetermined by K4.

  [cert(k) = 1 for all k ∈ K_R is guaranteed by K1 admission rule — clause (a) need
   not restate it; it is shown here for clarity and omitted from K5/K7 downstream proofs.]

E9 null registration event — K4(b) explanatory note:
  For k_null ∈ K_R with isNull(k_null):
    cert(k_null) = 1  (self-certified: interaction occurred, K1 admission rule)
    V(k_null) = 0     (K4(b) formal clause — not external commentary)
  The isNull guard excludes k_null from clause (a) — no conflict, no override.

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
| **Boundary** | V(k) = 1 is default K-side registration validity for non-null events. It does NOT mean the physical outcome is correct, does NOT mean the Born-rule probability was calculated correctly, and is NOT absolute metaphysical truth. It only means: within K_R, this registration event is treated as valid until contradicted. The isNull guard (o=∅ ∧ ΔI=0) excludes E9 null events from the `cert=1 → V=1` rule — no override is needed. A null event certifies "interaction occurred" but its outcome is ∅ (zero information) → V=0 by definition, not by K5 contradiction. The provisional/final distinction is formalized in K7 (Closure Axiom). |
| **Consistency** | K4 is consistent with E7 Axiom 1. K4 works with K3: only self-certified events (cert=1) get default validity. Events that fail admission (cert=0) have no validity status defined by this axiom. K4 + isNull guard is compatible with E9: null events are self-certified (interaction occurred) but carry V=0 because outcome information is ∅/zero — the isNull guard excludes them from the `cert=1 → V=1` rule without contradiction. K4 + K3 together: cert=1 (K3 intrinsic) ∧ ¬isNull(k) → V=1 (K4 default). |

### AXIOM K5 — Invalidation / Vô hiệu hóa

**Statement:**
> V(k1) → 0 iff there exists k2 ∈ K_R with k1 <_R k2 such that k2 stands in registered contradiction (⊥) to k1 within a shared K-side comparison context C_K, and k2 has valid cross-registration authority with respect to k1. Validity cannot be externally confirmed (only contradicted). Pre-closure: V_prov(k1) → 0 is reversible in principle if the contradicting act is itself invalidated before process closure (K7). Post-closure: V_final(k1) → 0 is irreversible and absolute. *(Note: "k2 ∈ K_R" has two readings — native intra-K_R and cross-space via K_joint. See K_R disambiguation in formal block below.)*

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

Asymmetry (E7 Axiom 3, post-closure):
  Post-closure: ¬∃F such that F(k′) → V_final(k) = 1.
  (No external function can restore V_final once K7 closes.)
  Pre-closure: V_prov(k) can return to 1 if the K5 trigger k2 is itself invalidated
  before closure — this is reversibility, not a violation of asymmetry.
  The asymmetry guarantee is absolute only for V_final (post-closure K7).

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

Reversibility corollary (explicit revert path — corollary of biconditional iff):
  Step 1: If ∃k2 satisfying (i)+(ii)+(iii) → V_prov(k1) = 0.   [K5 fires]
  Step 2: If k2 itself later invalidated: V(k2) → 0 before K7 closure
          → condition (iii) "k2 has valid cross-registration authority" fails for k2.
  Step 3: If no other k2′ satisfies all of (i)+(ii)+(iii) for k1
          → ¬∃k2 satisfying (i)+(ii)+(iii)
          → K5 biconditional LHS: V_prov(k1) = 0 no longer holds
          → V_prov(k1) reverts to K4 default: V_prov(k1) = 1.
  Mechanism: V_prov(k1) is re-evaluated via biconditional, not "stuck at 0".
  The notation "→ 0" describes a state assignment governed by iff, not a
  one-way imperative transition. Sticky-at-0 reading is incorrect for V_prov.

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
| **Dependency** | Level 2 (E7 Axioms 2-3). Uses `⊥` and "cross-registration authority" as **primitive predicates** whose full formalization is in Level 4 (paper v2.0 §4.4). K5 asserts the structural rule; the precise conditions for `k2 ⊥ k1` and "valid cross-registration authority" are defined in the bridge theorems (T1-T3). **2nd-order Layer 2 dependencies — Dep-A:** C_K existence precondition requires Level 4 predicate `requires_K_joint = 1` (Level 4 §4.3); K5 does not fire when C_K is absent (also reflected in Layer 1 Summary K5 row Role 1, via F4). **Dep-B (F7a non-circularity guard):** K5 condition (i) is defined natively by K2's `<_R` ordering. In cross-space application, K5 can only be evaluated after a candidate `K_joint` has already been constructed. T1 constructs `<_joint>` from K2 native orders + Level 4 cross-structure temporal relations + K8 field preservation; K5 does not define or prove `<_joint>`. Therefore Dep-B is an application-order dependency only: K5 uses `<_joint>` inside `K_joint` after T1 supplies the candidate joint order, so no circular dependency is introduced. |
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

Notation note:
  Auth(k2 → k1, C_K) is an INSTANCE-LEVEL relation, not a global direction.
  Auth(k1 → k2, C_K) may hold simultaneously when both k1, k2 are valid within
  the same C_K — mutual authority is permitted. The arrow "k2 → k1" reads
  "k2 has authority with respect to k1 in this instance", not "k2 always ranks
  above k1". K5 applies Auth with temporal direction (k1 <_R k2) — directionality
  is imposed by K5, not by K6 itself.

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

  ⚠ Intra-C_K transitivity and K5 invalidation chains (PG-07):
  Even if Auth is transitive within a single shared C_K — i.e., Auth(k2→k1, C_K)=1
  and Auth(k3→k2, C_K)=1 could in principle yield Auth(k3→k1, C_K)=1 — this does
  NOT enable transitive K5 invalidation chains. K5 requires an INDEPENDENT ⊥_K
  relation for each pair: V(k1)→0 requires Auth(k2→k1, C_K)=1 checked atomically
  at the moment of invalidation. The transitivity of Auth within C_K provides no
  shortcut: k3 cannot void k1 merely because k3 has authority over k2 and k2 has
  authority over k1. Each K5 invalidation step is an independent check; no chain
  propagation is implied by Auth transitivity alone.

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
> The registration process R of K_R closes at registration time t_close when no pending `requires_K_joint` demands remain for any pair of K-spaces involving K_R. At closure, for all k ∈ K_R: V(k) transitions from provisional status V_prov(k) to final status V_final(k). After closure: (a) no new k can be instantiated in K_R, (b) K5 irreversibility becomes absolute (V(k)→0 cannot be revised by any future event), (c) no new D_joint involving K_R can be raised, and (d) K_joint involving K_R becomes final (no reconfiguration of the joint space is permitted). Before closure, all V(k) are provisional and subject to K5 invalidation.

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

  Stabilization condition (V_final well-definedness):
    Within any compact time interval [t_start, t_close], the number of K5
    validity transitions for any k ∈ K_R is finite (finiteness of K_R and
    of the set of K5 triggers ensures this). Therefore V_prov(k) stabilizes
    before t_close, and V_final(k) = lim_{t → t_close^-} V_prov(k) is
    well-defined.

  Equivalent formulation:
    V_final(k) := V_prov(k) at t = t_close (value at exact closure time).
    This is consistent with the limit: the final value equals the stabilized
    pre-closure value.
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

        ΔI auxiliary (E9 derivability):
        ΔI(k) is determined by M(k) and o(k) per E9 definition — it is an
        auxiliary quantity, not an additional tuple field. Because (ii) preserves
        M and o exactly, ΔI is automatically preserved: ΔI(i(k)) = ΔI(k).
        Consequence: isNull(k) = [o(k)=∅ ∧ ΔI(k)=0] is preservation-invariant
        across embedding — null status cannot flip from K_R to K_X via K8.

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

        Counter-model (K4 holds, K8 fails):
          Let K_F = { k_F } with V_F(k_F) = 1 (K4 satisfied at
          native instantiation in K_F).
          Define embedding i: K_F → K_joint where the embedding
          operation assigns V_joint(i(k_F)) = 0 (validity dropped
          on transfer).
          K4 is satisfied in K_F: cert(k_F) = 1 ∧ ¬isNull(k_F)
          → V_F(k_F) = 1.  ✓
          K8 fails: V_joint(i(k_F)) ≠ V_F(k_F).  ✗
          Therefore K4 ⊬ K8. K8 is an independent postulate. □
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

| Axiom | Content | Fields covered | Source level | Freeze status | Level 4 dependency | Layer 2 theorem dep. (semantic) |
|---|---|---|---|---|---|---|
| K1 | Carrier set — K_R is a set of 5-field tuples | M, o, cert, t, V | Level 3 | Frozen | None | None |
| K2 | Temporal order — strict total order (chain) within K_R, discrete; RegistrationState defined | t (ordering) | Level 2 | Frozen | None | None |
| K3 | Self-certification — σ_R(M) intrinsic to R | cert | Level 2 | Frozen | None | None |
| K4 | Default validity — V=1 on instantiation for ¬isNull(k); E9 covered by isNull guard (no override) | V (default) | Level 2 | Frozen | None | None |
| K5 | Invalidation — V→0 by later ⊥ with authority; minimal ⊥ definition included | V (transition) | Level 2 | Frozen (syntactic) | C_K roles: (1) existential precondition — K5 fires only when C_K exists (requires_K_joint = 1); (2) ⊥ evaluation parameter (condition ii); (3) Auth evaluation parameter (condition iii) | **T1** (Dep-B): `<_joint` ordering used by K5 inside K_joint is constructed by T1; K5 applied only after T1 candidate K_joint exists |
| K6 | Cross-registration authority — structural relation within C_K, non-hierarchical | V (authority condition) | Level 2 | Frozen (syntactic) | C_K roles: (1) existential precondition for all Auth checks; (2) C_K-sphere membership parameter (condition a); (3) D_joint scope parameter (condition c) | None direct |
| K7 | Registration process closure — V_prov → V_final, absolute irreversibility | V (closure) | Level 2 | Frozen (syntactic) | Uses requires_K_joint for pending check only | **T2** (Dep-B): "resolved demand" semantics (when pending = ∅) requires T2 AdmJoint resolution definition; K7 closure timing depends on T2 |
| K8 | Cross-space embedding preservation — V preserved at embedding time; fields preserved | V (embedding) + M, o, cert, t | Level 3 | Frozen | None | None |

**Dependency isolation:** K1-K8 depend ONLY on Level 0-3 (BE SOT, K≠H, E1-E7, K-state tuple). Where K5-K7 reference Level 4 concepts (C_K, D_joint, requires_K_joint), they reference them for **scope identification only** (e.g., "is k1 in the same C_K as k2?"), not for their internal structure or definition.

**Syntactic freeze (unconditional):** K1-K8 text is frozen. If paper v2.0 community feedback changes the internal structure of AdmJoint, K1-K8 do not change — AdmJoint appears only in bridge theorems T1-T4, not in any K1-K8 axiom text.

**Layer 2 semantic dependencies (K5, K7):** "Frozen (syntactic)" means the axiom TEXT is frozen. The SEMANTIC BEHAVIOR of K5 (when it fires via `<_joint`) and K7 (when closure occurs via "resolved demand") depends on Layer 2 theorems T1 and T2 respectively. If T1 or T2 are updated (pending Level 4 freeze), K5/K7 semantics may shift even though K5/K7 text does not change. This is an application-order dependency (T1/T2 supply inputs K5/K7 consume), not a logical circularity. K1-K4 and K8 carry no Layer 2 semantic dependencies.

**Semantic dependency for ⊥_K (conditional):** K5 minimal ⊥ definition provides K5-local operational closure. However, Level 4 §4.4 boundary clauses ("not null event", "not invalid when both sides independently valid") narrow K5 minimal ⊥ and constitute a real semantic dependency: if these boundary clauses change, K5 fires in a different set of cases even though K5 text is unchanged. The syntactic freeze guarantee holds unconditionally; the semantic behavior guarantee for K5 is conditional on Level 4 ⊥ boundary clauses remaining a conservative extension of K5 minimal ⊥ (adding scope, not contradicting it). Only bridge theorems T1-T3 need updating for structural Level 4 changes.

---

## 2. Bridge Theorems — Layer 2 (Updatable) / Định lý Cầu nối — Tầng 2

**Status note:** Theorems T1-T3 are **pending Level 4 freeze** (paper v2.0 in community review). They connect K1-K8 to the paper's structural definitions. If Level 4 definitions change, T1-T3 are updated independently of K1-K8. T4 is new (Class D).

### T1 — K_joint Construction Theorem

**Statement:**
> Given K-side spaces K_A and K_B of registering systems A, B: if requires_K_joint(A, B) = 1 via a shared validity demand D_joint, then a candidate joint K-space K_joint(A, B) exists as the categorical colimit of the embedding diagram (K_A, K_B with structure-preserving morphisms). Equivalently: K_joint is the smallest K-space (up to isomorphism) containing order-preserving embeddings i_A: K_A → K_joint and i_B: K_B → K_joint that preserve cert and V values — "smallest" meaning minimal w.r.t. inclusion of K1-K8 structure, not minimal in cardinality. The embedding respects the internal time-order of each structure, and the combined order in K_joint is the transitive closure of the two embedded orders plus cross-structure temporal relations from the shared laboratory history. See T4 for the N-observer colimit generalization.

**Derivation — Layer 1 inputs + Level 4 inputs (composition, not pure derivation):**

> **Architectural note (F-RCA-P4-02):** T1 is a *composition theorem*, not a pure Layer 1 derivation. It combines Layer 1 axioms (K1-K8) with Level 4 inputs (D_joint context, cross-structure temporal relations). The cross-structure temporal relations encode physical laboratory history — a fact external to K-space axioms. T1 constructs `<_joint` from these two input streams; it does NOT derive cross-rel from K1-K8 alone.

```
Layer 1 inputs (K1-K8):
  - K1: K_A, K_B are sets of tuples → K_joint carrier = i_A(K_A) ∪ i_B(K_B)
  - K2: each K-space has native temporal order <_A, <_B (chains)
  - K3: embeddings i_A, i_B preserve cert values
  - K6: cross-registration authority evaluated within C_K defined by D_joint
  - K8: embeddings preserve V values at embedding time
        (V_X(i(k)) = V_R(k) at t_embed — K8 replaces former external EP; axiom
        set now self-contained for V-preservation)

Level 4 inputs (D_joint context — external to K1-K8):
  - requires_K_joint(A, B) = 1 via shared validity demand D_joint (§4.3)
  - cross-structure temporal relations (cross-rel) from shared laboratory history:
    e.g., t_F < t_W established by experimental protocol, not derivable from K1-K8
  - C_K specification for authority context

Composition:
  <_joint = (i_A(<_A) ∪ i_B(<_B) ∪ cross-rel)^+   [transitive closure]

Order type of <_joint:
  (K_joint, <_joint) is a PARTIAL ORDER (not necessarily total).
  Restricted to each image i_X(K_X): <_joint is a CHAIN (preserved from <_X by K2).
  Across distinct images i_A(K_A) and i_B(K_B): <_joint is PARTIAL — elements are
  comparable only through explicit cross-rel from Level 4 D_joint or transitive chain.
  (See K2 dòng Order type note: partial-order structure emerges at cross-K-space level.)
  T4 extends this to N-observer colimit: the colimit order is also partial in general.

  K_joint(A,B) exists as a candidate K-space with this combined order,
  preserving K1 carrier structure + K2 intra-order + K3 cert + K8 V.

Note: existence of a candidate K_joint does NOT guarantee admissibility.
Admissibility requires AdmJoint conditions (i)-(v) to hold (Level 4, §4.3).

F7a non-circularity guard:
  T1 does not depend on K5 Dep-B. K5 is evaluated only AFTER a candidate
  K_joint with <_joint exists. Dependency direction:
    [K1/K2/K3/K6/K8] + [Level 4 cross-rel + D_joint]
      → T1 candidate K_joint / <_joint
        → K5 application inside K_joint.
  No circularity: T1 supplies inputs K5 consumes; K5 does not supply inputs T1 needs.
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
  → K5 forces V_prov(k_A) → 0  OR  V_prov(k_B) → 0     [K5 pre-closure]
  → AdmJoint condition (iv) violated                         [Level 4, §4.3]
    (no V_prov invalidation while both are claimed jointly valid
     during the candidate K_joint admissibility check)

F7b timing guard:
  T2's AdmJoint(iv) check is pre-closure. It operates on V_prov because
  K7 assigns V_final only after pending requires_K_joint demands have
  been resolved. Therefore T2 cannot use V_final as the admissibility
  input without creating a timing inversion between T2 and K7.

Note: K5 conflict is a SUFFICIENT condition for AdmJoint failure,
NOT a necessary condition. AdmJoint may fail for other reasons.

Non-K5 failure example (K7 lock path):
  Suppose K_A has already closed at t_close(K_A) before D_joint is raised.
  A new D_joint(K_A, K_B) demands joint registration involving K_A.
  K7 post-closure property (a): no new k can be instantiated in K_A after t_close.
  → Embedding i_A: K_A → K_joint cannot satisfy AdmJoint condition (i) for the
    new acts demanded by D_joint (they cannot exist in closed K_A).
  → AdmJoint = 0 via K7 lock, with NO K5 contradiction required.
  → ⊥_K(K_A, K_B) holds via T2 (⊥_K iff requires_K_joint=1 ∧ ¬∃admissible K_joint),
    but the failure path is K7 closure, not K5 registered contradiction.
In such cases, ⊥_K may still hold, but the derivation trace
differs from the T2 K5-conflict path shown above.

⚠ TEMPORAL DEPENDENCY ACKNOWLEDGMENT:
  T2 derives ⊥_K (incommensurability) from K5 conflict.
  K5 uses ⊥ (registered contradiction) as a primitive predicate.
  The MINIMAL operational definition of ⊥ is given in K5 (Layer 1).
  The FULL formalization of ⊥ conditions is in Level 4 (paper v2.0 §4.4),
  whose precise boundary clauses are NOT yet frozen.

  This is a TEMPORAL DEPENDENCY, not a logical circularity:
    - K5's minimal ⊥ definition (Layer 1) is self-contained and NOT circular.
    - T2 needs Level 4 full ⊥ boundary clauses to complete its derivation in
      the general case. Level 4 is not yet frozen — this is an incompleteness,
      not a self-referential loop.
    - v1.3 CONCRETE MODEL FINDING: The dependency does NOT arise in the
      concrete model (§7.5 Step 4) — K5 minimal ⊥ is directly verifiable
      by content inspection (|h⟩ vs |Ψ+⟩) without invoking Level 4 full ⊥.
    - In the general case: T2 derivation is CONDITIONAL on Level 4 ⊥
      boundary clauses being a conservative extension of K5 minimal ⊥
      (adding scope, not contradicting it). This is a temporal dependency
      that resolves when Level 4 freezes — it is not a logical circle.
    - Resolution path: freeze Level 4 ⊥ boundary clauses independently
      of T2. T2's derivation is then complete without any circularity.
```

Boundary clauses (from paper v2.0 §4.4):
```
  ⊥_K does NOT assert that either physical event fails to occur on the ρ-side.
  ⊥_K does NOT mean either observer's outcome is false within its own K-side.
  ⊥_K is NOT equivalent to Null_K(e) — null registration is separate (E9).
  ⊥_K applies only when both sides are valid/provisionally valid within their own K-side.
```

F7b K7 resolution semantics:
```
  For K7 closure, a requires_K_joint demand is resolved when T2 yields
  one of two admissibility outcomes:

    (1) Success path:
        ∃K_joint such that AdmJoint(K_joint; K_A, K_B) = 1.
        The demand is resolved by successful joint registration.

    (2) Failure path:
        ¬∃K_joint such that AdmJoint(K_joint; K_A, K_B) = 1.
        The demand is resolved as K_A ⊥_K K_B.

  In both cases, the pending demand is no longer open. K7 may then
  evaluate whether pending(K_R, K_X) = ∅. T2 supplies the resolution
  semantics; K7 performs the closure transition from V_prov to V_final.
```

| Property | Value |
|---|---|
| **Level 4 dependency** | `AdmJoint` conditions (i)-(v), `⊥_K` boundary clauses, `D_joint` (paper v2.0 §4.3-4.4) |
| **Layer 1 dependency** | K5 (invalidation rule) + K6 (authority condition) + K8 (V-preservation at embedding) — T2 derivation uses all three. **K8 resolves former EP gap (G1): V-preservation is now derived from a core axiom.** |
| **Claim class** | D (proposed). Derivation trace is Class D; the ⊥_K conclusion matches paper v2.0 Class D definition. |
| **Important** | K5 conflict is a SUFFICIENT condition for AdmJoint failure, not necessary. AdmJoint may fail for other reasons. F7b: AdmJoint(iv) is checked against `V_prov` during pre-closure admissibility testing; `V_final` is assigned only after K7 closure. T2 also supplies K7's "resolved demand" semantics: a demand is resolved either by successful `AdmJoint = 1` or by failure `AdmJoint = 0` producing `⊥_K`. |
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

Temporal precondition (EWF setup — explicit):
  t_F < t_W in laboratory history:
    F measures the particle/friend system first (inside lab, at t_F).
    W performs the interference measurement afterward (on the lab, at t_W).
  This satisfies K5 condition (i): k_F <_R k_W in K_joint via cross-rel
  (K2 native orders + Level 4 cross-rel supply t_F < t_W → i_F(k_F) <_joint i_W(k_W)).
  T3 derivation presupposes EWF temporal ordering; it is not valid for t_W < t_F.

  ∧ M_F: k_F = ⟨M_F, o_F, 1, t_F, 1⟩  (definite outcome, self-certified, valid)
  ∧ M_W: k_W = ⟨M_W, o_W, 1, t_W, 1⟩  (superposition registered, no definite o_F)
  ∧ Under candidate K_joint:
      k_W ⊥ k_F within C_K (registration contents incompatible)       [Level 4, §4.4]
      ∧ k_W has valid cross-registration authority                   [Level 4, §4.4]
      → K5: V(k_F) → 0  OR  V(k_W) → 0                              [K5]
      → AdmJoint condition (iv) violated                             [Level 4, §4.3]
  → M_W ⊥ M_F (act-level registered contradiction)                   [Level 4, §4.4]

Semantic Postulate dependency — AJVS:
  T3 depends on AJVS (Axiom of Joint Validity Semantics — see AJVS section below T3):
  "A K_joint satisfies D_joint iff it hosts original first-order K-side validity
   claims of both K_A and K_B as jointly evaluable. Hosting only meta-descriptions
   ('within K_F, M_F registered |h⟩') does NOT satisfy D_joint — relativizing
   registration contents abandons D_joint rather than satisfying it."

  AJVS is a named Semantic Layer postulate (Layer 0.5), separate from K1-K8.
  It defines what counts as "satisfying D_joint" in VVV-QMRF.
  If AJVS is rejected → T3's conclusion (Bridge_EWF = 1) does not follow from
  K1-K8 alone. K1-K8 remain structurally valid; only D_joint semantic scope changes.
```

| Property | Value |
|---|---|
| **Level 4 dependency** | `Bridge_EWF` lemma, `D_joint`, cross-registration authority (paper v2.0 §4.5) |
| **Layer 1 dependency** | K5 (invalidation) + K6 (authority) + K8 (V-preservation at embedding) — T3 derivation uses all three. |
| **Semantic postulate** | Relativization defense — formalized as **AJVS** (see below). T3 is conditional on AJVS. This is not an internal contradiction; AJVS is a declared Semantic Layer postulate defining what counts as satisfying `D_joint`. |
| **Claim class** | D/C boundary (matches paper v2.0 §4.5 classification) |
| **Freeze status** | Pending Level 4 freeze |
| **Update trigger** | If `Bridge_EWF` sufficient conditions change, or cross-registration authority criteria are revised, or AJVS is challenged |

---

### AJVS — Axiom of Joint Validity Semantics / Tiên đề Ngữ nghĩa Hiệu lực Chung

> **Architectural note:** AJVS is a **Semantic Layer postulate** — it sits above Level 4 structural definitions but is separate from K1-K8 registration-logic axioms. K1-K8 govern K-space structure and operations; AJVS governs what "satisfying D_joint" means at the level of claim content. This is the formalization of F-RCA-P7-04 (Action Item A1).

**Statement:**
> A candidate K_joint satisfies D_joint(A, B) iff it hosts the **original** K-side validity claims of both K_A and K_B as **jointly evaluable first-order claims** in a shared comparison context C_K. Hosting only meta-descriptions of the form "within K_A, M_A registered o_A" does NOT satisfy D_joint. Relativizing registration contents to sub-context descriptions abandons D_joint rather than satisfying it.

**Formal:**
```
Let D_joint(A, B) be raised: requires_K_joint(A, B) = 1.
Let K_joint be a candidate with embeddings i_A: K_A → K_joint, i_B: K_B → K_joint.

K_joint satisfies D_joint iff:
  ∀k ∈ K_A ∪ K_B claimed as jointly valid:
    i_X(k) carries o(k) as a FIRST-ORDER validity claim in K_joint
    — directly evaluable, not wrapped in a meta-description predicate.

Relativization escape (violates AJVS):
  A K_joint that hosts only:
    "within K_F, M_F registered |h⟩"   [meta-description of K_F-internal fact]
  does NOT constitute joint evaluation of M_F's claim.
  D_joint requires: i_F(k_F) evaluated directly as "o(k_F) = |h⟩ is valid in K_joint".

AJVS boundary:
  First-order:  o(k) directly evaluable in K_joint     → D_joint satisfied.
  Second-order: "K_X says o(k) is valid within K_X"   → D_joint NOT satisfied.
```

| Property | Value |
|---|---|
| **Nature** | Semantic Postulate — Layer 0.5 (above Level 4 structural defs; separate from K1-K8 registration-logic) |
| **BE lineage** | Dignāga–Dharmakīrti distinction: pratyakṣa (direct first-order perception/registration) vs anumāna (inferential / meta-cognition). Joint validity in VVV-QMRF requires pratyakṣa-level first-order registration, not anumāna-level meta-description |
| **Claim class** | D (proposed semantic postulate) |
| **Source** | VVV-QMRF architectural stance (paper v2.0 §4.5, now elevated to named postulate) |
| **If AJVS holds** | T3 conclusion Bridge_EWF = 1 follows from K1-K8 + AJVS. Relativization escape route closed. |
| **If AJVS rejected** | T3 conclusion does NOT follow from K1-K8 alone. Relativization escape open. K1-K8 remain structurally valid — only D_joint semantic scope changes. |
| **Cascade** | T3 (cites AJVS instead of unnamed external assumption); §10.5 Final Verdict; §10.6 A1 (resolved); Layer 2 Summary T3 row |

---

### T4 — N-Observer Generalization Theorem

**Statement:**
> For N ≥ 2 registering systems R_1, ..., R_N with K-side spaces K_1, ..., K_N: the joint K-space K_joint(R_1, ..., R_N) exists as the colimit of the embedding diagram only when (1) every pair (i, j) with requires_K_joint(K_i, K_j) = 1 satisfies pairwise AdmJoint, and (2) the N-observer embedding diagram satisfies global overlap compatibility: shared K-state images and all embedding paths commute in the candidate K_joint. K-side incommensurability ⊥_K is NOT necessarily transitive: K_A ⊥_K K_B ∧ K_B ⊥_K K_C does NOT entail K_A ⊥_K K_C. Each pair requires an independent D_joint and AdmJoint check, but pairwise admissibility alone does not prove N-way colimit commutativity.

**Derivation from axioms:**
```
K_joint(R_1,...,R_N) = colimit of embedding diagram D where:
  objects:  K_1, K_2, ..., K_N
  morphisms: for each pair (i,j) with requires_K_joint(K_i,K_j) = 1
             and AdmJoint satisfied: embedding i_{ij}: K_i → K_j (or K_i → K_joint)
  colimit universal property: K_joint is the minimal K-space receiving
    embeddings from all K_i that commute with the diagram morphisms.

F7d global commutativity guard:
  Pairwise AdmJoint is necessary but not sufficient for N-observer colimit
  existence. K8 preserves tuple fields and V values along each embedding,
  but K8 does not by itself guarantee path-independence across multiple
  embeddings. For N > 2, T4 requires an additional global compatibility
  condition: whenever two embedding paths carry the same source K-state or
  shared overlap into K_joint, their images must agree on M, o, cert, t,
  and initial V at embedding time, and their post-embedding validity dynamics
  must not force inconsistent identifications. Thus the diagram must commute
  globally, not merely pairwise.

T4-H — Colimit Existence Hypothesis (explicit conditional — F-RCA-P4-06 Option A):
  The category C_{K-space} — whose objects are K-spaces (K1-K8-structured
  sets) and whose morphisms are K1-K8-preserving embeddings — is assumed
  to have colimits for all finite embedding diagrams.

  Formal statement of T4-H:
    For any finite diagram D of K-spaces with K1-K8-preserving morphisms,
    the colimit colim(D) exists in C_{K-space}.

  Status: CONDITIONAL THEOREM (2/4 steps verified — 2026-05-23 RCA).

    Step 1 (C_{K-space} category): VERIFIED — identity, composition, associativity.
    Step 2 (colimit construction): VERIFIED — K_colim = (∐_i K_i)/~ constructed;
      all 5 tuple fields well-defined via lexicographic t-assignment (SP1 resolved)
      and embedding-time V snapshot (SP2 resolved); <_colim constructed via
      T1-generalized transitive closure (SP3 constructed, cycle detection deferred
      to Step 3); 5/5 verification gates PASS.
      Proof: project_vvv_qmrf_class_c/02_derivation_chain/T4_H_step2_colimit_construction.md
      (3-Round RCA, aggregate 4.73/5).
    Step 3 (K1-K8 preservation through quotient): DEFERRED — K5 cross-K_R ⊥ paths,
      V dynamics, cycle detection in <_colim.
    Step 4 (universal property): DEFERRED — existence + uniqueness of mediating
      morphism.
    K1-K8 define the structure of individual K-spaces; they do NOT by themselves
    prove that C_{K-space} is cocomplete. T4 conclusions hold CONDITIONAL on
    T4-H Steps 1-4.

  Conditional scope:
    If T4-H Steps 1-4 hold  → T4 conclusions valid for all N ≥ 2.
    If T4-H fails  → N-observer colimit may not exist in general; T1
                     (N = 2, constructive) remains valid independently
                     because T1 builds K_joint explicitly without invoking
                     the colimit universal property.
    Current (2/4): K_colim EXISTS as a well-defined set with well-defined K1
    tuple fields. Steps 3-4 remain deferred but the construction is explicit.

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
| **Level 4 dependency** | All Level 4 definitions, generalized to N observers; global overlap/path-commutativity condition for N-observer diagrams |
| **Claim class** | D (proposed) — NEW. Not in paper v2.0 (which handles N=2 only). |
| **Important** | Pairwise `AdmJoint` checks are necessary local conditions, not sufficient global conditions. N-observer `K_joint` requires pairwise admissibility plus global overlap/path-commutativity. K8 supplies field/V preservation along each embedding but does not by itself prove global commutativity. |
| **Freeze status** | New theorem. Requires independent verification for N>2. |
| **Update trigger** | When N>2 EWF scenarios are modeled; when paper v3.0 extends to multi-observer cases |

---

### T5 — K_joint Composition / Associativity Theorem

**Statement:**
> Given admissible K-side spaces K_A, K_B, K_C and successive K_joint constructions K_joint(A,B) (via T1) and K_joint(K_joint(A,B), C) (via T1 applied again), the resulting space is isomorphic — as a K1-K8-structured set — to the N=3 colimit K_joint(A,B,C) as defined by T4. K_joint construction is therefore associative up to K1-K8-preserving isomorphism. This theorem is conditional on T4-H (Colimit Existence Hypothesis). T5 does not claim ρ-side associativity or physical composition of measurement outcomes.

**Derivation from axioms:**
```
Inputs (Layer 1 + Layer 2):
  Layer 1 (K1-K8):
    K1: carrier sets — K_A, K_B, K_C are K_R sets of tuples
    K2: intra-K_R chains preserved under each T1 embedding
    K4+K5+K7: V-propagation follows K-axiom rules uniformly in both composition paths
    K8: V-preservation at each embedding step (per T1)

  Layer 2 (T1, T4):
    T1: K_joint(A,B) is the colimit of the 2-object diagram (K_A, K_B)
        when requires_K_joint(A,B) = 1 and AdmJoint conditions satisfied
    T4 + T4-H: K_joint(A,B,C) is the colimit of the 3-object diagram
        when pairwise + global commutativity conditions satisfied

Composition argument:
  Path 1 (incremental): K_joint(A,B) first, then K_joint(K_joint(A,B), C)
  Path 2 (one-shot):    K_joint(A,B,C) directly (T4)

  By the universal property of colimits (T4-H):
    The colimit of a diagram is unique up to canonical isomorphism.
    Both Path 1 and Path 2 are colimits of the same underlying diagram
    D = {K_A, K_B, K_C, morphisms} — provided K8 V-preservation ensures
    the same K1-K8-preserving embedding conditions hold along each path.
    Therefore Path 1 ≅ Path 2 as K1-K8-structured sets.

F-T5-01 (commutativity guard):
  This isomorphism holds only when Path 1's incremental embeddings preserve
  the same global commutativity condition required by T4 (F7d guard).
  If the intermediate K_joint(A,B) introduces path-dependent V-transitions
  (K5 invalidations that differ between paths), the paths may produce
  distinct but non-isomorphic candidate K_joints. T5 asserts isomorphism
  ONLY when the global F7d commutativity is confirmed for the full diagram.

Conditional scope:
  If T4-H holds  → T5 associativity holds for all K_A, K_B, K_C.
  If T4-H fails  → T5 does not follow in general; T1 N=2 case remains valid
                   independently of T5.
```

| Property | Value |
|---|---|
| **Bridges axioms to** | K_joint composition (algebraic associativity of colimit construction) |
| **Layer 1 dependency** | K1 (carrier), K2 (chain order), K4+K5+K7 (V lifecycle), K8 (V-preservation at embedding) |
| **Layer 2 dependency** | T1 (K_joint construction), T4 + T4-H (N-observer colimit, colimit existence hypothesis) |
| **Level 4 dependency** | `requires_K_joint`, `D_joint`, `AdmJoint` (for admissibility of each K_joint step) |
| **EX anchor** | No direct EX intersection node — internal algebraic theorem; EX compass used as sanity check (no K_joint composition tension in EX graph) |
| **BE lineage** | Continuity of K-side registration structure across sequential joint contexts — structural extension of K2 chain property to multi-K_R scope |
| **Claim class** | D (proposed) — conditional on T4-H which is itself a hypothesis |
| **Freeze status** | Conditional on T4-H + Level 4 freeze |
| **Update trigger** | If T4-H is established or refuted; if K_joint compatibility conditions change; if global commutativity (F7d) conditions are revised |

---

### T6 — Decoherence-Induced Registration Update Theorem

**Statement:**
> When a ρ-side decoherence event occurs at registration time t_decohere, the K-side responds through one of two mutually exclusive registration-layer paths. **Path A (K5 invalidation):** if a comparison context C_K exists (requires_K_joint = 1) and k_coherent satisfies K5 conditions (⊥ within C_K + Auth(k_decohere → k_coherent, C_K) = 1), then V_prov(k_coherent) → 0 via K5. **Path B (k_new instantiation):** if C_K is absent or K5 conditions are not met, a new tuple k_new = ⟨M_new, o_new, cert=1, t_decohere, V=1⟩ is instantiated with cert intrinsic per K3 and default validity per K4. In neither path does T6 modify the ρ-side decoherence process. Certification is always intrinsic (K3); "extrinsic re-certification" is NOT a K-side concept.

**Derivation from axioms:**
```
Boundary setup — ρ-side vs K-side split (mandatory):
  ρ-side: decoherence occurs via environment coupling |ψ_S⟩ → ρ_mixed
          This is Standard QM; T6 does not touch this mechanism.
  K-side: registering system R is coupled to the decoherence event.
          T6 characterizes what happens in K_R as a result.

Path A — K5 Invalidation Path:
  Precondition: C_K exists (requires_K_joint = 1, Level 4 §4.3)

  k_coherent ∈ K_R: the prior registration of coherent state o_coherent
  k_decohere ∈ K_R at t_decohere: the decoherence registration
    cert(k_decohere) = σ_R(M_decohere) = 1   [K3 intrinsic — NOT extrinsic]
    k_coherent <_R k_decohere                 [K2 temporal order]
    k_decohere ⊥ k_coherent within C_K        [K5 primitive — decoherence content
                                               is incompatible with coherent state
                                               registration content within shared C_K]
    Auth(k_decohere → k_coherent, C_K) = 1   [K6 cross-registration authority]
  → K5 fires: V_prov(k_coherent) → 0

  Bhrānti channel (EX anchor):
    The K5 invalidation corresponds to bhrānti (erroneous cognition) in BE:
    k_coherent is revealed as having recorded a superposed state that —
    in the new C_K — cannot be jointly valid with k_decohere.
    EX anchor: N_QM_VVV_00032 (Registration Error / Bhrānti Status)
    BE anchor: N_BE_00006 (Erroneous cognition)
    QM anchor: N_QM_00095 (Decoherence & Environment as Measurement)

Path B — k_new Instantiation Path:
  Precondition: C_K absent (requires_K_joint = 0) OR K5 conditions unmet

  k_new = ⟨M_new, o_new, cert=1, t_decohere, V=1⟩   [K1 carrier set]
  cert(k_new) = σ_R(M_new) = 1                        [K3 intrinsic]
  ¬isNull(k_new) → V(k_new) = 1                       [K4 default validity]

  k_coherent remains in K_R with V(k_coherent) unchanged by T6 alone.
  K7 governs finalization at process closure.

Disambiguation from E9/E14 (mandatory):
  E9 (null event): o=∅ ∧ ΔI=0 → V=0 — decoherence registration has o ≠ ∅;
                   T6 is NOT E9.
  E14 (validated absence): registers the absence of a result — T6 registers
    a positive decoherence-induced update, not an absence. T6 is NOT E14.

K3 preservation note (mandatory):
  T6 uses "cert = σ_R(M) = 1" throughout — cert is always intrinsic.
  "Extrinsic certification" is not a K-side concept; T6 does not
  introduce extrinsic cert in any path.
```

| Property | Value |
|---|---|
| **Bridges axioms to** | K-side registration response to ρ-side decoherence — algebraic characterization of two response paths (K5 invalidation or k_new instantiation) |
| **Layer 1 dependency** | K1 (carrier set), K2 (temporal order), K3 (intrinsic cert), K4 (default validity), K5 (invalidation), K6 (authority), K7 (closure) |
| **Level 4 dependency** | `requires_K_joint`, C_K existence (Path A); `⊥_K` boundary clauses (for K5 condition in Path A) |
| **EX anchor** | `N_QM_VVV_00032` (Registration Error / Bhrānti Status) — intersection node; BE anchor: `N_BE_00006` (Erroneous cognition); QM anchor: `N_QM_00095` (Decoherence & Environment as Measurement) |
| **BE lineage** | Bhrānti (erroneous cognition) via N_BE_00006 — Path A maps decoherence-induced K5 invalidation to the K-side analogue of a cognition revealed as erroneous; Path B maps to fresh k instantiation (svataḥ prāmāṇya — K4 default validity on new registration) |
| **Claim class** | D (proposed) |
| **Freeze status** | Pending Level 4 freeze (Path A uses `requires_K_joint` + `⊥_K` boundary clauses) |
| **Update trigger** | If Level 4 `⊥_K` boundary clauses change (affects Path A K5 firing condition); if `requires_K_joint` scope changes; if E9 or E14 definitions are revised (disambiguation section may need update) |

---

### T7 — IRB Registration-Scope Propagation Theorem

**Statement:**
> When IRB(A,B) and IRB(B,C) both hold (E15 — Intrinsic Relational Binding), a shared comparison context C_K can be instantiated over K_joint(A,B,C) (T4 N=3 colimit), provided T4's admissibility conditions are satisfied. This is a K-side registration-scope extension subject to three mandatory boundary clauses: **(BC-1) no physical transitivity claim** — T7 does not assert that physical entanglement is transitive; monogamy of entanglement is a Standard QM result and T7 makes no ρ-side claim; **(BC-2) no ⊥_K transitivity** — K_A ⊥_K K_B ∧ K_B ⊥_K K_C does NOT entail K_A ⊥_K K_C (T4 non-transitivity of ⊥_K is preserved); **(BC-3) K-side scope only** — "scope propagation" means C_K can cover A-B-C jointly as a registration admission question; it does not add a new physical correlation between A and C.

**Derivation from axioms:**
```
Inputs (E15 + Layer 1 + Layer 2):
  E15 (framework postulate):
    IRB(A,B): |ψ_AB⟩ ≠ |ψ_A⟩ ⊗ |ψ_B⟩ — entangled state → K-side
              registration non-separability; K_A and K_B cannot be
              fully specified independently within the shared-state context
    IRB(B,C): analogously for B, C

  Layer 1 (K1-K8):
    K1: K_A, K_B, K_C are K_R sets of tuples
    K8: V-preservation at embedding across each K_joint step

  Layer 2 (T1, T4, T5):
    T1: K_joint(A,B) constructable when requires_K_joint(A,B) = 1 + AdmJoint
    T4: K_joint(A,B,C) constructable when pairwise + global commutativity
    T5: K_joint(K_joint(A,B), C) ≅ K_joint(A,B,C)    [conditional on T4-H]

  Level 4 (external inputs):
    IRB-induced D_joint: the IRB non-separability of A-B and B-C implies
    that joint validity demands may be raised for A-B-C under appropriate
    experimental conditions (Level 4 §4.3 scope for requires_K_joint).
    D_joint(A,B,C) is raised when the experimental context demands joint
    validity evaluation across all three.

Scope propagation chain:
  IRB(A,B) ∧ IRB(B,C)
  → D_joint(A,B) ∧ D_joint(B,C) potentially raised     [Level 4 §4.3]
  → requires_K_joint(A,B) = 1 ∧ requires_K_joint(B,C) = 1
  → K_joint(A,B) admissible (T1)
  → K_joint(K_joint(A,B), C) admissible (T1 applied again)
  → K_joint(A,B,C) ≅ K_joint(K_joint(A,B), C)          [T5 — conditional T4-H]
  → Extended C_K over A-B-C instantiated in K_joint(A,B,C)

Boundary clause BC-1 — no physical transitivity (MANDATORY):
  T7 asserts nothing about whether A and C are physically entangled.
  Monogamy of entanglement: Standard QM result — T7 does not touch it.
  If the physical experiment involves an A-C interaction, that is a
  separate E15 instance IRB(A,C), not derivable from T7 alone.

Boundary clause BC-2 — ⊥_K non-transitivity preserved (MANDATORY):
  K_A ⊥_K K_B  ∧  K_B ⊥_K K_C  ⇏  K_A ⊥_K K_C         [T4, preserved]
  T7 does not assert K_A ⊥_K K_C. The extended C_K over A-B-C may or may
  not lead to ⊥_K(A,C) — that depends on an independent T2 + T4 check.
  T7 only asserts that a shared C_K CAN be instantiated; not that it will
  produce incommensurability.

Boundary clause BC-3 — K-side scope only (MANDATORY):
  "IRB scope propagation" = C_K can cover A-B-C jointly as a registration
  admission question. The extended C_K is a structural consequence of
  admissibility conditions (T1+T4+T5), not a new physical relation.
  No new ρ-side correlation is asserted between A and C.

F-T7-01 (T5 dependency):
  T7 uses T5 (associativity) which is conditional on T4-H.
  If T4-H fails, T7 does not follow in the general N=3 case;
  T1 pairwise constructions remain valid independently.
```

| Property | Value |
|---|---|
| **Bridges axioms to** | E15 IRB → K-side registration-scope propagation for multi-body entangled systems |
| **Layer 1 dependency** | K1 (carrier sets), K8 (V-preservation at embedding) |
| **Layer 2 dependency** | T1 (K_joint construction), T4 + T4-H (N=3 colimit), T5 (composition associativity — T7 depends on T5) |
| **Level 4 dependency** | `requires_K_joint`, `D_joint`, `AdmJoint` (for all pairwise + N=3 admissibility checks); IRB-induced D_joint scope |
| **EX anchor** | `N_QM_VVV_00025` (IRB / Entanglement) — intersection node; BE anchor: `N_BE_00021` (Essential relation / svabhāvapratibandha); QM anchors: `N_QM_00047` (Entanglement), `N_QM_00090` (Bell correlations) |
| **BE lineage** | Svabhāvapratibandha extended via E15 IRB — registration non-separability as the K-side analogue of intrinsic-nature relational binding in Dharmakīrti; extended to multi-body scope |
| **Claim class** | D (proposed) — conditional on T4-H, E15 wording stability, and Level 4 freeze |
| **Freeze status** | Conditional on T4-H + Level 4 freeze + E15 wording |
| **Update trigger** | If E15 IRB definition is revised; if T4-H is established or refuted; if T5 is revised; if Level 4 `requires_K_joint` scope changes for IRB-induced D_joint demands |

### Layer 2 Summary / Tổng kết Tầng 2

| Theorem | Bridges axioms to | Level 4 dependency | Freeze status | Risk if Level 4 changes |
|---|---|---|---|---|
| T1 | K_joint construction | `requires_K_joint`, `D_joint`, embeddings | Pending | Theorem statement updates; K1-K8 unchanged |
| T2 | ⊥_K derivation | `AdmJoint` (i)-(v), `⊥_K` boundary clauses | Pending | Derivation chain updates; K1-K8 unchanged |
| T3 | Bridge_EWF formalization | `Bridge_EWF` lemma, **AJVS** (Semantic Postulate Layer 0.5 — relativization defense, formalized) | Pending | Derivation chain may need revision if AJVS challenged; K1-K8 unchanged |
| T4 | N-observer generalization | All Level 4, generalized to N; **T4-H** Colimit Existence Hypothesis (conditional) | New — Class D | Conditional on T4-H; independently updatable |
| T5 | K_joint composition (algebraic associativity) | `requires_K_joint`, `D_joint`, `AdmJoint` (per T1+T4) | Conditional on T4-H | K_joint composition structure updates; K1-K8 unchanged |
| T6 | Decoherence-induced registration update (Path A: K5 invalidation; Path B: k_new instantiation) | `requires_K_joint`, C_K, `⊥_K` boundary clauses (Path A only) | Pending Level 4 freeze | Path A K5 conditions update; K3 intrinsic cert unchanged |
| T7 | IRB registration-scope propagation (E15 → extended C_K for A-B-C) | `requires_K_joint`, `D_joint`, `AdmJoint` for A-B-C; IRB-induced D_joint scope; E15 framework | Conditional on T4-H + Level 4 + E15 | If E15 IRB changes or T4-H fails; T4 ⊥_K non-transitivity preserved; K1-K8 unchanged |

---


## 3. Current Open Items / Các mục Để Mở Hiện hành

| # | Item | Status | Priority |
|---|------|--------|:--------:|
| 1 | Multi-step retroactive chain (E8 extension) | Deferred — K5 single-step; K5 V_prov pre-closure mechanism allows re-assessment of invalidating acts before K7 closure (F1: V_prov/V_final lifecycle — V_prov→0 reversible pre-closure, V_final→0 irreversible post-closure). Multi-step chain requires additional axiom(s). | Medium |
| 2 | Null K-state full formalization (E9 detailed operationalization) | Partial — K1 o=∅ + K4 E9 exception structurally accommodate null events. Detailed operationalization deferred. | Low-Medium |
| 3 | Validated absence validity conditions (E14 extension) | Partial — K1 o=∅ + K4 default validity structurally accommodate. Specific absence validity conditions deferred. | Medium |
| 4 | Inter-K-space relation structure (E15 extension) | Partially addressed by T7 (IRB Registration-Scope Propagation, Layer 2 bridge theorem) — T7 provides C_K extension and multi-body scope propagation derived from E15 IRB. Full axiomatization of inter-K-space IRB relations as a Layer 1 axiom remains deferred. | Low-Medium |
| 5 | Pre-registration K-state (E16 extension / K0) | Deferred — new axiom needed | Low-Medium |
| 6 | Pre-symbolic registration stratum (E4 formalization) | Deferred — K-space stratification | Low |
| 7 | Equivalence of σ(M) and R̂_svasa formalisms | Deferred — separate research track (paper v2.0 §7.2 item #4) | Low |
| 8 | Full semantic proof for Bridge_EWF "no admissible reinterpretation" | Pending Level 4 freeze + T3 completion. External assumption (relativization defense) documented. | High |
| 9 | T4 N>2 verification | Requires multi-observer EWF modeling | Medium |
| 10 | Update paper v2.0 Section 7.2 deferred item #5 status | After community feedback on this document | Low |
| 11 | RCA re-audit after community feedback | After Level 4 freeze and T1-T3 finalization | High |
| 12 | `CHANGELOG.md` §3.3 Operational Bridge semantic dependency on K4-K7 untracked | `CHANGELOG.md` §3.3 lists 7 sufficient-condition bridges (Condition A, B, B2, C, D, E, ODC_K) for raising `requires_K_joint`. The verdict notes B, B2, and ODC_K have indirect semantic dependency on K4-K7 validity propagation, but the table does not annotate which K-axioms each Condition row depends on. Add K-axiom dependency annotations (e.g., K4, K5, K7) to each §3.3 Condition row. Note: the predicate-level mapping (σ, V, ⊥, Auth, D_joint, requires_K_joint, C_K → K-axioms) is a separate task belonging to Layer 4 §4.4, not to §3.3. | Medium |
| 13 | **Probability postulate (K9/P9)** | **Partially Addressed** — K9-S8 defines joint probability composition law ($P9-JC$) for two observers, proving Marginalization Cancellation. However, it remains a postulate rather than derived from K1-K8. Full Layer 1 or Layer 2 formal integration in this document is still pending. | **Critical** |
| 14 | **Non-circular data comparison** | **Ongoing** — Known that marginal CHSH correlators cannot test the deviation due to Marginalization Cancellation. A genuine non-circular comparison requires extracting individual conditional correlators or joint outcome histograms from Proietti Figure 3 raw data. | **Critical** |
| 15 | **Code consistency** | **Addressed (fits/K9S9)** — Formalized and implemented the exact P9-JC conditional prediction engine (`K9S9_conditional_predictions.py`), achieving 11% deviation at beta=0.3. Approximations in `k9e_predictor.py` and `d1_blk1_4point_fit.py` are deprecated. | High |
| 16 | **Numerical predictions in main document** | **Ongoing** — First genuine numerical predictions generated in `plan/k9_analysis/K9S9_conditional_predictions.md`. Stating them formally in this main document is pending community review. | **Critical** |

---


## 4. Cross-References / Tham chiếu Chéo

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


- Historical sprint/audit/proof/freeze records: `CHANGELOG.md`.
