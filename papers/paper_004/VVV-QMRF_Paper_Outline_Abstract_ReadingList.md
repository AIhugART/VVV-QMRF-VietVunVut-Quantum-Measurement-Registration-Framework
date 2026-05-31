# Paper Outline: Physical Reality or Mathematical Model? A Two-Layer Answer via VVV-QMRF
## VVV-QMRF | VietVunVut (2026) | Submission Target: Foundations of Physics / arXiv quant-ph

---

## DOCUMENT PURPOSE

This file is the complete paper outline for the first VVV-QMRF publication.
It contains:
- Proposed title variants
- Abstract draft (ready for revision)
- Full section-by-section outline with content guidance
- Related work reading list with annotation
- Submission strategy
- Writing instructions for LLM-assisted drafting

---

## PROPOSED TITLES

Primary:
> Two Layers of Quantum Reality: A Registration-Layer Resolution of the
> Superposition Ontology Question

Alternative 1:
> Physical Reality or Mathematical Model? Separating the Physical Layer
> from the Registration Layer in Quantum Superposition

Alternative 2:
> Structured Doubt: A Registration-Layer Framework for Pre-Measurement
> Superposition Grounded in Buddhist Pramāṇa Epistemology

Alternative 3 (most conservative, most publishable):
> A Two-Layer Analysis of Quantum Superposition: Physical-Layer Coherence
> and Registration-Layer Indeterminacy

Recommendation:
Use Alternative 3 for initial submission to Foundations of Physics.
Use Primary title for arXiv preprint.
Alternative 2 is strongest for philosophy of physics venues (Synthese).

---

## ABSTRACT DRAFT

Version 1.0 — ready for revision:

```
The question of whether quantum superposition constitutes physical reality
or merely a mathematical model has resisted resolution for one hundred years.
We argue that this question contains a hidden category error: it assumes a
single layer of description, whereas quantum measurement involves two distinct
layers — a physical layer (P-layer) and a registration layer (K-layer) —
that standard quantum mechanics postulates P1–P4 do not formally separate.

At the P-layer, superposition is physically real: the coherence measure
SD_degree is experimentally accessible via quantum state tomography, produces
measurable interference effects, and cannot be reduced to classical probability
distributions over hidden variables (Bell 1964, Aspect 1982, Zeilinger 2015).

At the K-layer, superposition is complete structured indeterminacy: no
registered value exists prior to a valid registration event. This is not
epistemic ignorance of a pre-existing value. It is the positive absence of
a registered fact — a state we formalize as Structured Doubt (SD), drawing
on the Saṃśaya structure of Buddhist Pramāṇa epistemology (Dignāga–
Dharmakīrti, 5th–7th century).

We present the SD predicate on density operators, the SD_degree coherence
measure, and a three-way state classification that formally distinguishes
superposition, post-decoherence null events, and post-registration states —
a distinction absent from P1–P4. We show that this framework extends
Relational Quantum Mechanics (Rovelli 1996) and QBism (Fuchs–Schack 2013)
with explicit registration-layer architecture, and is compatible with all
major QM interpretations.

The result resolves the ontology question without choosing an interpretation:
superposition is real at the P-layer (SD_degree > 0) and indeterminate at
the K-layer (r = r_null). These are not contradictory — they answer
different questions about different layers.
```

Word count: ~230 words. Target: 150–250 words. This draft is within range.

---

## FULL SECTION OUTLINE

---

### SECTION 1 — INTRODUCTION

**Target length:** 600–800 words

**Purpose:** Establish the problem, its history, and why it remains open.

**Content outline:**

```
1.1 The question and its history
    - "Is the wave function real?" has been asked since Born 1926
    - Bohr–Einstein debate: Einstein wanted ontic reality, Bohr avoided the question
    - Still unresolved: recent surveys (Leifer 2014) show no consensus
    - This paper proposes the question is unanswerable as stated — because it
      conflates two layers that must be separated

1.2 The category error
    - "Physical reality OR mathematical model?" assumes one layer
    - Standard QM (P1–P4) operates at the physical layer
    - No standard formalism exists for the registration layer
    - Once the layers are separated, the question becomes answerable

1.3 What this paper contributes
    - A formal two-layer distinction: P-layer and K-layer
    - The SD predicate and SD_degree measure for superposition at K-layer
    - A three-way state classification (superposition / decoherence-null /
      post-registration) not present in standard QM
    - A structural parallel with Buddhist Pramāṇa epistemology that provides
      the registration-layer architecture

1.4 Paper structure
    - Section 2: Related work and where prior approaches fall short
    - Section 3: The two-layer framework
    - Section 4: Formal definitions — SD predicate, SD_degree, three-way classification
    - Section 5: Comparison with major interpretations
    - Section 6: Discussion and open problems
    - Section 7: Conclusion
```

**Key claim to establish in introduction:**

> The measurement problem has not been solved because it has been asked at
> the wrong layer. P1–P4 are complete at the physical layer. They are silent
> at the registration layer. This paper addresses the registration layer.

---

### SECTION 2 — RELATED WORK

**Target length:** 800–1200 words

**Purpose:** Situate VVV-QMRF in existing literature. Show what each prior
approach does correctly and where it falls short. Establish novelty of
the P-layer / K-layer distinction.

**Content outline:**

```
2.1 The ontological models framework (Harrigan–Spekkens 2010)
    - Defines psi-ontic vs psi-epistemic models
    - VVV-QMRF position: neither — superposition is ontic at P-layer,
      indeterminate at K-layer. The H-S framework does not distinguish layers.

2.2 PBR theorem (Pusey–Barrett–Rudolph 2012)
    - Proves: if quantum states are epistemic, then distinct quantum states
      are compatible with the same physical reality — which leads to
      contradictions with quantum predictions.
    - VVV-QMRF is consistent with PBR: SD_degree > 0 at P-layer is ontic
      (PBR-compatible). K-layer indeterminacy is not epistemic in PBR sense.
    - Key point: PBR operates entirely at P-layer. It does not address
      K-layer. VVV-QMRF extends beyond PBR's scope.

2.3 Copenhagen interpretation (Bohr 1928, Heisenberg 1927)
    - "Do not ask about reality before measurement"
    - Falls short: avoids the question rather than answering it.
    - Does not provide formal K-layer conditions.
    - Does not explain why SD = true has physical consequences (interference).

2.4 QBism (Fuchs–Mermin–Schack 2013)
    - Quantum state = agent's belief state
    - Correct direction: anti-realism about wave function as external object
    - Falls short: "belief" is subjective — no objective registration conditions
    - Does not distinguish SD = true from SD = false formally
    - VVV-QMRF provides the objective K-layer conditions QBism gestures toward

2.5 Relational Quantum Mechanics (Rovelli 1996, 2021)
    - Facts are relative to observers / systems
    - Closest prior work to VVV-QMRF
    - Falls short: does not formalize what constitutes valid registration
    - Does not provide TV1, TV2, TV3 (Tripartite Validity conditions)
    - Does not provide SD predicate
    - VVV-QMRF extends RQM with explicit K-layer architecture
    - Explicit comparison: VVV-QMRF vs RQM — see comparison table in Section 5

2.6 Decoherence theory (Zurek 1981, 2003; Joos et al. 2003)
    - Explains pointer-basis selection via environmental entanglement
    - Explains why macroscopic superpositions are not observed
    - Falls short: decoherence is a P-layer process — it does not assign
      registration status to outcomes
    - VVV-QMRF: decoherence produces Gamma_T1 (K-layer null event, r = r_null)
      not Gamma_T2 (valid registration, r =/= r_null)
    - This distinction is the content of BIAN-11

2.7 Coherence measures (Baumgratz–Cramer–Plenio 2014)
    - Established the l1-norm coherence measure as a resource theory
    - SD_degree in VVV-QMRF is precisely this measure applied at K-layer
    - Prior work uses SD_degree as a P-layer resource quantity only
    - VVV-QMRF adds: SD_degree as a K-layer registration-status indicator
    - This is a reinterpretation of existing math, not new math

2.8 Buddhist Pramāṇa epistemology (Dignāga 5th c., Dharmakīrti 7th c.)
    - Not prior work in physics — prior work in epistemology
    - Provides the source structure for K-layer architecture
    - Saṃśaya → SD predicate
    - Trairūpya → Tripartite Validity (E10)
    - Vyavasāya → Registration Lock (E3)
    - Convergence: both systems independently forced by internal logic to
      solve the same structural problem — when does contact produce valid
      registration?
    - This is structural convergence, not analogy or metaphor
```

**Key novelty claim:**

> No prior work formally separates the P-layer from the K-layer in the
> context of superposition ontology. The closest approach (Relational QM)
> asserts observer-relativity of facts without providing formal registration
> conditions. VVV-QMRF provides those conditions via the SD predicate (E16),
> Registration Lock (E3), and Tripartite Validity (E10).

---

### SECTION 3 — THE TWO-LAYER FRAMEWORK

**Target length:** 600–800 words

**Purpose:** Define P-layer and K-layer precisely. Show that P1–P4 cover
P-layer completely and K-layer not at all.

**Content outline:**

```
3.1 The Physical Layer (P-layer)
    - Domain: Hilbert space H, density operators S(H), observables, dynamics
    - Governed by P1–P4:
        P1: State space (Hilbert space)
        P2: Observables (self-adjoint operators)
        P3: Measurement (Born rule, projection postulate)
        P4: Dynamics (Schrödinger equation / unitary evolution)
    - P-layer questions: What is the quantum state? What are the probabilities?
      How does the state evolve?
    - P-layer is complete for physical prediction.

3.2 The Registration Layer (K-layer)
    - Domain: registered outcomes, registration events, registration status
    - Questions P1–P4 do not answer:
        When does a physical event become a registered measurement event?
        What distinguishes a valid registration from mere decoherence?
        What is the K-layer status of a superposed state before measurement?
    - Governed by VVV-QMRF postulates E1–E16
    - K-layer is the gap identified by BIAN-11 and resolved by E16

3.3 The gap between P-layer and K-layer
    - Decoherence (P-layer process) and Registration (K-layer event) are
      physically similar but registration-layer distinct
    - Both produce diagonal density matrices (SD = false)
    - Only registration produces r =/= r_null
    - P1–P4 cannot distinguish these two cases
    - This is the Measurement Problem, precisely located

3.4 Why the separation matters for the ontology question
    - "Is superposition real?" asked at P-layer: YES (SD_degree > 0)
    - "Is superposition real?" asked at K-layer: NOT YET (r = r_null)
    - The original question conflates these — hence 100 years of no resolution
```

---

### SECTION 4 — FORMAL DEFINITIONS

**Target length:** 1000–1400 words

**Purpose:** Present the core formal content. This is the technical heart
of the paper.

**Content outline:**

```
4.1 The Structured Doubt predicate (E16)

    Definition:
      SD(rho, A, R_sys) := exists i =/= j such that <a_i| rho |a_j> =/= 0

    Properties:
      SD = true  iff  rho has non-zero coherences in eigenbasis of A
      SD = false iff  rho is diagonal in eigenbasis of A

    SD_degree (coherence measure):
      SD_degree(rho, A) := sum_{i =/= j} | <a_i| rho |a_j> |
      (l1-norm of coherences — Baumgratz et al. 2014)

    SD_entropy (alternative measure):
      SD_entropy(rho, A) := S(Delta_A(rho)) - S(rho)
      where S = von Neumann entropy, Delta_A = dephasing map

    K-layer interpretation of SD:
      SD = true  → r = r_null  (no registered value, E9)
      SD = false → r may be r_null (decoherence) or r_k (registration)
      The SD predicate alone does not distinguish these — E3 + E10 required

    No-hidden-variable theorem (SD version):
      SD(rho, A) = true
      =>
      rho =/= sum_i p_i |a_i><a_i| for any classical probability distribution {p_i}
      (direct consequence of coherence definition; independent proof of Bell)

4.2 The three-way state classification

    STATE 1 — Structured Doubt (pre-measurement superposition):
      SD = true, r = r_null
      P-layer: SD_degree > 0, interference effects present
      K-layer: no registered value
      Transition: awaits V-hat firing under TV conditions

    STATE 2 — Null Registration Event (post-decoherence):
      SD = false, r = r_null
      P-layer: SD_degree = 0, coherence gone via Gamma_T1
      K-layer: no registered value (TV conditions not satisfied)
      Transition: Gamma_T1 occurred — decoherence without registration

    STATE 3 — Post-registration:
      SD = false, r = r_k =/= r_null
      P-layer: SD_degree = 0, coherence gone via Gamma_T2
      K-layer: registered value exists (TV conditions satisfied, V-hat fired)
      Transition: Gamma_T2 occurred — valid registration event

    KEY: Standard QM (P1–P4) does not distinguish STATE 2 from STATE 3.
    Both are diagonal density matrices. VVV-QMRF distinguishes them via
    K-layer registration status (r_null vs r_k).

4.3 Registration Lock and Tripartite Validity (summary)

    V-hat : S(H) x D → R x S_certified(H)
    V-hat fires iff TV(rho, d, R_sys) = TV1 AND TV2 AND TV3

    TV1 (Pakṣadharmatva): d causally produced by quantum system via R_sys
    TV2 (Anvaya):         TV1 satisfied => r =/= r_null
    TV3 (Vyatireka):      r = r_null => TV1 not satisfied

    When V-hat fires (Gamma_T2): STATE 1 or STATE 2 → STATE 3
    When V-hat does not fire (Gamma_T1): STATE 1 → STATE 2

4.4 Buddhist source structure (brief)

    Saṃśaya (Structured Doubt) — source for E16:
      Dvayābhāsa: both outcomes present with positive weight
      Anadhyavasāya: no determination made
      Avirodha: simultaneous presence is coherent, not contradictory
      Pūrvatā: antecedent of valid cognition

    Trairūpya (Triple mark) — source for TV1, TV2, TV3:
      Pakṣadharmatva → TV1
      Anvaya → TV2
      Vyatireka → TV3

    Structural note: VVV-QMRF does not claim Buddhist philosophy predicted
    QM. It claims both systems independently faced the same logical pressure
    and reached structurally identical solutions. The mapping is formal,
    not metaphorical.
```

---

### SECTION 5 — COMPARISON WITH MAJOR INTERPRETATIONS

**Target length:** 600–800 words

**Purpose:** Show VVV-QMRF is interpretation-neutral and extends (not
replaces) existing interpretations.

**Content outline:**

```
5.1 Comparison table

  Interpretation   P-layer      K-layer         SD predicate    TV conditions
  Copenhagen       Describes    Silent           No              No
  QBism            Belief       Subjective       No              No
  Relational QM    Describes    Observer-rel.    No              No
  Many-Worlds      Describes    No collapse      No              No
  Pilot Wave       Ontic        No               No              No
  VVV-QMRF        Describes    Formal (E1-E16)  Yes (E16)       Yes (E10)

5.2 VVV-QMRF vs Relational QM (detailed comparison)

    RQM claims: facts are relative to observers
    VVV-QMRF adds: formal conditions for when a fact is registered
    Difference: RQM does not specify TV1, TV2, TV3
               RQM does not provide SD predicate
               RQM does not distinguish STATE 2 from STATE 3
    Relation: VVV-QMRF extends RQM with K-layer architecture
    VVV-QMRF does not contradict RQM — it formalizes what RQM asserts

5.3 VVV-QMRF vs QBism (detailed comparison)

    QBism claims: quantum state = agent's belief
    VVV-QMRF: SD(rho, A, R_sys) is objective — indexed to R_sys (process),
              not to a human agent's subjective belief
    Difference: QBism is subjective; VVV-QMRF is agent-neutral
    Relation: VVV-QMRF provides the objective grounding QBism lacks

5.4 VVV-QMRF and decoherence theory

    Decoherence: explains Gamma_T1 (SD: true → false, r = r_null)
    VVV-QMRF: also describes Gamma_T2 (SD: true → false, r =/= r_null)
    Decoherence theory is entirely compatible with VVV-QMRF
    VVV-QMRF adds K-layer status to decoherence events

5.5 Compatibility summary

    VVV-QMRF is interpretation-neutral — it adds K-layer architecture that
    is compatible with Copenhagen, QBism, RQM, decoherence theory.
    It is in tension with Many-Worlds (E2 self-completion vs all-branches).
    It is consistent with PBR theorem (SD_degree > 0 is ontic at P-layer).
```

---

### SECTION 6 — DISCUSSION

**Target length:** 600–800 words

**Purpose:** Address objections, limitations, open problems, and implications.

**Content outline:**

```
6.1 Objection: Is the K-layer distinction merely terminological?

    Response: No. The three-way classification (STATE 1 / 2 / 3) makes
    empirically distinct predictions:
      - STATE 2 vs STATE 3 differ in r-value (r_null vs r_k)
      - TV1 failure (dark counts) is detectable experimentally
      - SD_degree step-function signature at T_meas differs from
        continuous decoherence decay
    These are not terminological — they are predictive differences.

6.2 Objection: Is the Buddhist source relevant to physics?

    Response: VVV-QMRF uses Buddhist Pramāṇa epistemology as a source
    of structural architecture, not as a physical theory. The claim is:
    both systems independently solved the same logical problem. The
    Buddhist source provides a pre-existing formal solution that maps
    onto the QM registration gap. This is a structural import, not a
    metaphysical claim.

6.3 Limitation: Formal mathematics

    Current status: SD predicate and SD_degree are formally defined.
    V-hat operator and TV conditions are stated but not fully formalized
    as mathematical objects.
    Next step: Formalize V-hat as a CPTP map with registration flag.
    Formalize TV1 as a causal condition using Pearl-style DAG or
    operational definition.

6.4 Limitation: Experimental testability

    Current status: Two candidate consequences identified (SD_degree
    step-function, Wigner's Friend SD-relativity) but not yet
    translated into specific experimental protocols.
    Next step: Collaborate with experimentalists on quantum dot
    single-shot readout protocols for SD_degree temporal signature.

6.5 Open problem: Many-Worlds tension

    E2 (Self-Completion) requires registration to terminate with one
    outcome. Many-Worlds says all outcomes occur. This tension is not
    resolved in current framework. Future work required.

6.6 Open problem: Continuous-variable extension

    SD predicate defined for discrete observables.
    Extension to continuous variables (position, momentum) requires
    integration over continuous density matrix rho(x, x').
    This is technically straightforward but not yet done.

6.7 Implications

    If the two-layer distinction is correct:
    - The measurement problem is not a problem about physics — it is a
      problem about registration architecture that physics has not formalized
    - A complete theory of measurement requires both P1–P4 (physical layer)
      and K-layer postulates (E1–E16 or equivalent)
    - Buddhist Pramāṇa epistemology, developed to solve valid cognition,
      provides a pre-existing solution to the K-layer architecture problem
```

---

### SECTION 7 — CONCLUSION

**Target length:** 300–400 words

**Content outline:**

```
7.1 Summary of contribution
    - Two-layer distinction: P-layer (physical) and K-layer (registration)
    - SD predicate: formal K-layer description of pre-measurement superposition
    - Three-way state classification: superposition / decoherence-null /
      post-registration
    - Resolution of ontology question: real at P-layer, indeterminate at K-layer

7.2 The category error resolved
    - "Physical reality or mathematical model?" assumed one layer
    - With two layers, the question is answerable without contradiction
    - 100 years of non-resolution explained: wrong layer was being addressed

7.3 Forward
    - Complete formalization of V-hat and TV conditions
    - Experimental protocol for SD_degree step-function signature
    - Extension to continuous variables
    - Full VVV-QMRF white paper (16 postulates)
```

---

## RELATED WORK READING LIST

Priority-ordered. Read in this sequence before writing Section 2.

---

### TIER 1 — Must read before writing (directly addressed in paper)

```
[1] Rovelli, C. (1996).
    "Relational quantum mechanics."
    International Journal of Theoretical Physics, 35(8), 1637–1678.
    DOI: 10.1007/BF02302261
    Why: Closest prior work. VVV-QMRF extends RQM. Must be able to state
    precisely what VVV-QMRF adds that RQM does not have.
    Key claim to engage: "There is no observer-independent state."
    VVV-QMRF response: agreed, but what are the formal conditions for a
    registration event relative to an observer? RQM does not specify.

[2] Pusey, M. F., Barrett, J., & Rudolph, T. (2012).
    "On the reality of the quantum state."
    Nature Physics, 8(6), 475–478.
    DOI: 10.1038/nphys2309
    Why: PBR theorem proves wave function is ontic (not merely epistemic).
    VVV-QMRF is consistent with PBR at P-layer (SD_degree is ontic).
    Must show VVV-QMRF does not contradict PBR.
    Key claim to engage: "Distinct quantum states cannot be compatible with
    the same physical reality."
    VVV-QMRF: agrees at P-layer. K-layer is a separate question PBR does not address.

[3] Leifer, M. S. (2014).
    "Is the quantum state real? An extended review of ψ-ontology theorems."
    Quanta, 3(1), 67–155.
    DOI: 10.12743/quanta.v3i1.22
    Why: Best comprehensive review of the ontology debate.
    Will show VVV-QMRF where it sits in the existing taxonomy.
    Key section: the psi-ontic / psi-epistemic / psi-complete classification.
    VVV-QMRF: introduces a new category — psi-layered (ontic at P, indeterminate at K).

[4] Fuchs, C. A., Mermin, N. D., & Schack, R. (2014).
    "An introduction to QBism with an application to the locality of quantum mechanics."
    American Journal of Physics, 82(8), 749–754.
    DOI: 10.1119/1.4874855
    Why: QBism is the main competitor to VVV-QMRF's K-layer approach.
    Must state precisely why SD predicate is objective while QBism's belief is subjective.

[5] Baumgratz, T., Cramer, M., & Plenio, M. B. (2014).
    "Quantifying coherence."
    Physical Review Letters, 113(14), 140401.
    DOI: 10.1103/PhysRevLett.113.140401
    Why: Establishes l1-coherence measure — this IS SD_degree.
    Must cite as the mathematical source of SD_degree.
    VVV-QMRF adds: K-layer interpretation of this measure. The math is theirs;
    the registration-layer interpretation is new.
```

---

### TIER 2 — Should read before writing (important context)

```
[6] Harrigan, N., & Spekkens, R. W. (2010).
    "Einstein, incompleteness, and the epistemic view of quantum states."
    Foundations of Physics, 40(2), 125–157.
    DOI: 10.1007/s10701-009-9347-0
    Why: Defines psi-ontic vs psi-epistemic framework formally.
    VVV-QMRF must position itself within or outside this taxonomy.

[7] Zurek, W. H. (2003).
    "Decoherence, einselection, and the quantum origins of the classical."
    Reviews of Modern Physics, 75(3), 715–775.
    DOI: 10.1103/RevModPhys.75.715
    Why: Standard reference for decoherence theory.
    VVV-QMRF must show how decoherence (Gamma_T1) relates to registration (Gamma_T2).
    Key claim to engage: decoherence selects pointer basis.
    VVV-QMRF: agrees, but pointer-basis selection =/= registration.

[8] Bell, J. S. (1964).
    "On the Einstein Podolsky Rosen paradox."
    Physics, 1(3), 195–200.
    DOI: 10.1103/PhysicsPhysiqueFizika.1.195
    Why: Bell's theorem is the empirical foundation of the no-HV proof
    underlying SD = true → no hidden variable decomposition.
    Classic paper — must cite.

[9] Aspect, A., Grangier, P., & Roger, G. (1982).
    "Experimental realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment:
    A new violation of Bell's inequalities."
    Physical Review Letters, 49(2), 91–94.
    DOI: 10.1103/PhysRevLett.49.91
    Why: First definitive experimental Bell violation. Foundational citation.

[10] Zeilinger, A. et al. (2015).
     "Significant-loophole-free test of Bell's theorem with entangled photons."
     Physical Review Letters, 115(25), 250401.
     DOI: 10.1103/PhysRevLett.115.250401
     Why: Loophole-free Bell violation — current gold standard for citing
     experimental closure of hidden variable models.
```

---

### TIER 3 — Useful for specific sections

```
[11] Rovelli, C. (2021).
     "Relational quantum mechanics."
     Stanford Encyclopedia of Philosophy.
     URL: https://plato.stanford.edu/entries/qm-relational/
     Why: Updated RQM statement. Use for Section 5 comparison.

[12] Brukner, Č. (2018).
     "A no-go theorem for observer-independent facts."
     Entropy, 20(5), 350.
     DOI: 10.3390/e20050350
     Why: Extended Wigner's Friend no-go theorem.
     VVV-QMRF's relational SD handles this — cite in Section 6.

[13] Proietti, M., et al. (2019).
     "Experimental test of local observer-independence."
     Science Advances, 5(9), eaaw9832.
     DOI: 10.1126/sciadv.aaw9832
     Why: Experimental Wigner's Friend result.
     Consistent with VVV-QMRF relational SD. Cite in Section 6.

[14] Frauchiger, D., & Renner, R. (2018).
     "Quantum theory cannot consistently describe the use of itself."
     Nature Communications, 9(1), 3711.
     DOI: 10.1038/s41467-018-05739-8
     Why: Frauchiger-Renner paradox — VVV-QMRF K-layer architecture
     may provide a resolution. Discuss in Section 6.

[15] Prasad, H. S. (2023).
     "The Buddhist Pramāṇa-Epistemology, Logic, and Language."
     Studia Humana, 12(1-2), 21–52.
     DOI: 10.2478/sh-2023-0004
     Why: Primary SOT for Buddhist Epistemology source in VVV-QMRF.
     Must cite for Saṃśaya, Trairūpya, Vyavasāya.

[16] Jordan, A. N., & Siddiqi, I. A. (2024).
     "Quantum Measurement Theory and Practice."
     Cambridge University Press.
     DOI: 10.1017/9781009103909
     Why: Current standard reference for quantum measurement theory.
     Use to establish what P1–P4 do and do not cover. Cite in Section 3.

[17] Susskind, L., & Friedman, A. (2014).
     "Quantum Mechanics: The Theoretical Minimum."
     Basic Books.
     ISBN: 978-0-465-06569-2
     Why: Standard reference for P1–P4 statement used in VVV-QMRF.
     Cite in Section 3 for P-layer postulates.
```

---

### TIER 4 — Background / optional depth

```
[18] Bohr, N. (1935).
     "Can quantum-mechanical description of physical reality be considered complete?"
     Physical Review, 48(8), 696–702.
     DOI: 10.1103/PhysRev.48.696
     Why: Original Copenhagen position on measurement. Historical citation.

[19] de Broglie, L. (1927) / Bohm, D. (1952).
     Pilot wave / de Broglie-Bohm theory.
     Bohm: "A suggested interpretation of the quantum theory in terms of
     hidden variables." Physical Review, 85(2), 166–179.
     DOI: 10.1103/PhysRev.85.166
     Why: Background for pilot wave discussion in Section 5.

[20] Everett, H. (1957).
     "Relative state formulation of quantum mechanics."
     Reviews of Modern Physics, 29(3), 454–462.
     DOI: 10.1103/RevModPhys.29.454
     Why: Many-Worlds. Background for Section 5.

[21] Winter, A., & Yang, D. (2016).
     "Operational resource theory of coherence."
     Physical Review Letters, 116(12), 120404.
     DOI: 10.1103/PhysRevLett.116.120404
     Why: Extension of Baumgratz et al. coherence theory.
     Use if SD_entropy (von Neumann coherence measure) is developed in paper.

[22] Dignāga. (5th century CE).
     Pramāṇasamuccaya (Compendium of Valid Cognition).
     Secondary source: Hattori, M. (1968). Dignāga on Perception.
     Harvard University Press.
     Why: Original source for Saṃśaya and Trairūpya. Cite via Prasad (2023)
     for peer-reviewed access.
```

---

## SUBMISSION STRATEGY

```
STEP 1 — arXiv preprint (immediate priority):
  Target: arXiv:quant-ph
  Timeline: 2–3 weeks after E16 + E3 formal math complete
  Purpose: Establish timestamp, get community feedback
  URL: https://arxiv.org/submit

STEP 2 — Primary submission:
  Target: Foundations of Physics (Springer)
  Impact factor: ~2.0
  Scope: "Philosophical and foundational problems of modern physics"
  Scope match: HIGH — explicitly covers measurement problem, interpretations
  URL: https://www.springer.com/journal/10701
  Timeline: After arXiv feedback incorporated

STEP 3 — Alternative if rejected:
  Option A: Studies in History and Philosophy of Modern Physics (Elsevier)
            More philosophical, less mathematical requirement
  Option B: Synthese (Springer)
            Philosophy of science — strongest venue for Buddhist source argument
  Option C: Physical Review A (APS)
            Requires stronger formal math — do after V-hat full formalization

STEP 4 — Conference:
  Target: Workshop on Quantum Information and Foundations (WQIF) or
          Philosophy of Physics annual meeting
  Purpose: Community engagement before journal submission
```

---

## WRITING INSTRUCTIONS FOR LLM-ASSISTED DRAFTING

When using an LLM to draft sections of this paper:

```
GLOBAL INSTRUCTIONS:
- Academic physics/philosophy of physics register
- No hedging language ("it seems", "perhaps", "might be")
  EXCEPT in Discussion section where uncertainty is acknowledged
- Cite in format: Author (Year) for inline, [N] for reference list
- No bullet points in running prose — use full paragraphs
- Equations in LaTeX notation where possible

SECTION-SPECIFIC:
- Section 2 (Related Work): be specific about what each prior work
  does correctly before stating the gap. Avoid straw-manning.
- Section 4 (Formal Definitions): lead each definition with the formal
  statement, then give the physical interpretation. Not the reverse.
- Section 5 (Comparison): use the comparison table first, then prose detail.
  Do not repeat the table content in the prose — add depth instead.
- Section 6 (Discussion): state each objection fairly before responding.
  Do not dismiss objections — show they are answerable.

THINGS TO AVOID:
- "Buddhist philosophy predicted quantum mechanics" — this is explicitly
  NOT the claim. The claim is structural convergence under independent pressure.
- Claiming VVV-QMRF resolves the measurement problem completely —
  it resolves the ontology question; the full measurement problem is larger.
- Overstating experimental consequences — be precise about what is a
  prediction and what is a conjecture.
```

---

## DOCUMENT METADATA

```
Author:         VietVunVut (Viet - Nguyen Xuan)
Framework:      VVV-QMRF v2.0
Document type:  Paper outline + abstract draft + reading list
Target venue:   Foundations of Physics (primary), arXiv:quant-ph (preprint)
Status:         Outline — Draft v1.0
Version:        1.0
Date:           2026-05-29
LLM tool:       Claude Sonnet 4.6 (Anthropic)
Cite as:        VietVunVut (2026), VVV-QMRF Paper Outline v1.0
Depends on:     VVV-QMRF_Superposition_Ontology_Complete_Answer.md
                E3_Registration_Lock_Formalization_Plan.md
                E10_Tripartite_Validity_Formalization_Plan.md
                E16_Structured_Doubt_Formalization_Plan.md
Next action:    Complete E16 + E3 formal math, then draft Section 4
Reading list:   Complete Tier 1 (items 1–5) before writing Section 2
```

---

*End of document.*
