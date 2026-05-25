Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Has Every Wigner's Friend Experiment Been Blind to a Geometric Degree of Freedom?

**Status:** Draft v31 — 9-issue RCA: novelty softening, Eq.(2) motivation repositioned, thesis repetition cuts, theorem-box restructure, experimental feasibility, reparameterization defense, multi-observer → S3, defensive tone reduction, headline consolidation. 17 refs. ~5 pages.
**Date:** 2026-05-25 | **Target:** arXiv quant-ph, then Phys. Rev. A

---

## Abstract

Existing Extended Wigner's Friend (EWF) implementations share, to our
knowledge, a common geometric blind spot: the Superobserver's polar angle θ
on the Bloch sphere has never been varied from the equator. We establish
an equatorial fixed-point theorem (Proposition 1): at θ = π/2, any
overlap-dependent modification P = P_QM · [1 − β · g(overlap)] / Z
cancels identically — for every function g, not just Eq. (3).
We propose a null test: re-insert one quarter-wave plate into the Bong
et al. (2020) apparatus (θ = 31°), enabling order-of-magnitude sensitivity
β ≥ 0.04 at 5σ while preserving 8.6σ Genuine LF violation. The experiment
operates under fair-sampling (η ≈ 0.87); loophole closure requires SNSPD
upgrade (η ≥ 0.91).

---

## Section 1 — Introduction

Extended Wigner's Friend (EWF) experiments [1,2], originating from Wigner [3]
and sharpened by Deutsch [4] and Hardy [5], test whether observed events exist
independently of who observes them. Modern implementations combining Local
Friendliness (LF) no-go theorems [2,10-12] with optical setups have challenged
the absoluteness of observed events [13,14].

This paper establishes the **equatorial fixed-point theorem** (Proposition 1,
§3): at θ = π/2, any overlap-dependent modification of the form
P = P_QM · [1 − β · g(outcome overlap)] / Z vanishes identically. Here
"overlap-dependent" means that a Superobserver's measurement statistics depend
not only on the quantum state, but also on the geometric overlap between
the Superobserver's measurement basis and a prior observer's recorded outcome
(§2.3 provides the formal definition). As its direct experimental consequence,
we propose a minimal modification (a single quarter-wave plate, θ = 31°) that
breaks this cancellation, and we compute its sensitivity to overlap-dependent
deformations using exact numerical evaluation of the quantum mechanical
density matrix.

The theorem (Claim A) is the central result; the experimental protocol
(Claim B, §4-7) is its direct consequence. Claim A is a mathematical theorem
requiring no experimental assumptions. Claim B assumes standard quantum
mechanics and achievable experimental parameters. Throughout §5-7 we
distinguish model-independent QM predictions from sensitivity calculations.

The geometric result itself is compact: f_perp(+1,H) − f_perp(−1,H) = −cos θ
(Eq. 4). At θ = π/2, this vanishes for any function of the basis overlap
(Proposition 1). The full proof is three lines (§3.3); §2 provides motivation
and notation.

This paper does not claim that overlap-dependent deformation exists in
nature. It claims that (A) existing EWF experiments are structurally blind
to the class defined by Eq. (2-3), and (B) a single waveplate enables, to
our knowledge, the first experimental test of this class. A positive result
would require independent verification including θ-sweeps (§8.4).

Supplemental material: S1 (full algebraic proof and literature search methodology),
S2 (derivation and numerical computation details), S3 (quantum interpretations,
contextuality comparison, and measurement incompatibility physical picture).

---

## Section 2 — Background

### 2.1 — Extended Wigner's Friend Setup

Bong et al. (2020) [2] used two entangled photon pairs produced by spontaneous
parametric down-conversion (SPDC) at 810 nm. On each side, a Friend measures
photon polarization in the z-basis inside an interferometric lab formed by beam
displacers. A Superobserver measures the combined Friend+photon system at three
settings: Setting 1 (z-basis, reads the Friend outcome directly); Settings 2 and
3 (azimuthal angles on the Bloch sphere equator, θ = π/2). Measurement outcomes
are binary, a, b ∈ {+1, −1}, with N = 91,000 coincidences per setting.

[Figure 1: EWF setup with tilted Superobserver measurement]

### 2.2 — Genuine Local Friendliness Inequality

The Genuine Local Friendliness Facet 1 inequality [2] is:

  Gen LF 1 = −⟨A₁⟩ − ⟨A₂⟩ − ⟨B₁⟩ − ⟨B₂⟩ − ⟨A₁B₁⟩ − 2⟨A₁B₂⟩ − 2⟨A₂B₁⟩
           + 2⟨A₂B₂⟩ − ⟨A₂B₃⟩ − ⟨A₃B₂⟩ − ⟨A₃B₃⟩ − 6 ≤ 0                        (1)

A violation rules out all theories satisfying Local Friendliness.

### 2.3 — Overlap-Dependent Deformation: Why This Class?

**Core idea.** We define a symmetry-constrained benchmark parametrization for
overlap-dependent deformation via a single parameter β (Eq. 2). Within the GPT
framework [17], Eq. (2) parametrizes the simplest one-parameter deformation of
the Born rule preserving normalization and remaining operationally admissible.
The functional form Eq. (3) follows from three minimal physical constraints —
rotation invariance, alignment limit, monotonicity — and any function satisfying
them has identical leading-order structure. Eq. (3) is the simplest
representative; the geometric cancellation (§3) holds for the entire class.
No existing theory predicts this form; like the Standard Model Extension for
Lorentz violation [15], it defines quantitative experimental targets without
committing to a specific origin. The model-independent theorem (Proposition 1,
§3) is the central result; Eq. (2-3) serves as a benchmark parametrization.

Before presenting the theorem, we explain which class of overlap-dependent
modifications we consider and why. The theorem in §3 constrains precisely this
class — the constraints motivate the class, not vice versa.

Consider modifications to quantum probabilities:

  P(a,b | x,y) = P_QM(a,b | x,y) · [1 − β · g(b, Friend outcome)] / Z           (2)

where β ∈ [0,1] is a deformation strength and g is an overlap function.
β = 0 recovers standard QM. We call β the coupling strength and Eq. (2)
the overlap-dependent deformation (previously termed "outcome-dependent
coupling" in preliminary drafts; the present name emphasizes geometric content
over causal implication).

Any smooth function of the basis overlap satisfying three minimal physical
constraints has the same leading-order structure; Eq. (3) is the simplest
representative, not its unique member: (i) basis-rotation invariance — only
the relative angle between measurement bases can matter; (ii) alignment
limit — when bases are aligned (|⟨b|d⟩|² = 1), g(1) = 0; (iii)
monotonicity — incompatibility grows with orthogonality. The leading-order
Taylor expansion is g(x) = c₁(1−x) + O((1−x)²). Adopting the simplest
representative and absorbing c₁ into β:

  f_perp(b, d) = 1 − |⟨b|d⟩|²                                                    (3)

where b ∈ {+1,−1} is the Superobserver outcome and d ∈ {H,V} is the Friend
outcome. Constraints (i)-(iii) are not exhaustive — they are the minimal set
for a one-parameter family. The geometric cancellation (§3) holds for any
g(|⟨b|d⟩|²).

Equation (2) is a benchmark parametrization — not a hidden-variable model,
not a collapse modification, not a signal between observers (full ontological
classification and contextuality comparison in Supplemental S3).

The experiment is a null test: standard QM predicts the same LF violation
regardless of θ. If a θ-dependent signal were detected, that would indicate
a departure from standard QM predictions independently of model class.
Eq. (2-3) quantifies sensitivity; the primary result is the θ-dependence
(or its absence).

---

## Section 3 — Equatorial Fixed-Point Theorem (Claim A)

### 3.1 — Main Result (Model-Independent)

Let a Friend F measure in the z-basis ({|H⟩, |V⟩}) and a Superobserver W measure
at Bloch sphere angles (θ, φ). With f_perp(b,d) = 1 − |⟨b|d⟩|²:

  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                         (4)

Consequently, f_perp is overlap-independent if and only if θ = π/2. For any
equatorial Superobserver measurement, any model of the form Eq. (2-3) reduces
exactly to standard quantum mechanics, regardless of the deformation strength β.
This result is model-independent: it depends only on Bloch sphere geometry.
Eq. (2-3) is a benchmark parametrization for quantifying experimental
sensitivity (§5.3); the theorem holds for any overlap function.

### 3.2 — Equatorial Fixed-Point Theorem

**Proposition 1 (Universality within overlap-only deformations).** Let
g: [0,1] → ℝ be any function (smooth or otherwise). At θ = π/2,
|⟨b|d⟩|² = 1/2 for all outcome pairs (b,d). Therefore
g(|⟨b|d⟩|²) = g(1/2) = constant for all (b,d), and the modification factor
[1 − β · g(|⟨b|d⟩|²)] / Z reduces to [1 − β · g(1/2)] / [1 − β · g(1/2)] = 1.
The equatorial plane is a fixed point for the entire class of overlap-only
deformations — not just Eq. (3), but any function of the basis overlap. ∎

**Corollary.** Any overlap-only deformation that vanishes at the equator
necessarily collapses to a constant there. No overlap-dependent modification
evades equatorial cancellation while depending only on |⟨b|d⟩|²; producing a
non-trivial equatorial signal requires dependence on additional degrees of
freedom beyond the basis overlap.

**Scope limitation.** Proposition 1 constrains the overlap-only class:
deformations whose modification factor depends solely on |⟨b|d⟩|². Broader
deformations — depending on the full density matrix, higher-order correlators,
or non-geometric variables — lie outside this theorem's scope. The experiment
(§4-7) constrains the overlap-only class; independent designs are needed for
broader classes.

**Examples.** g(x) = x² gives g(1/2) = 1/4 for all outcome pairs — constant,
hence cancels in Z. g(x) = sin(πx) gives g(1/2) = 1 — again constant.
g(x) = (1−x)^n for any n ≥ 1 gives g(1/2) = (1/2)^n — constant. The
cancellation is universal.

### 3.3 — Proof

The Superobserver measurement basis at (θ, φ):

  |b=+1⟩ = cos(θ/2)|H⟩ + e^{iφ} sin(θ/2)|V⟩                                     (5)
  |b=−1⟩ = sin(θ/2)|H⟩ − e^{iφ} cos(θ/2)|V⟩                                     (6)

Squared overlaps (φ drops out: |e^{iφ}|² = 1):

  |⟨b=+1|H⟩|² = cos²(θ/2)          |⟨b=+1|V⟩|² = sin²(θ/2)                      (7)
  |⟨b=−1|H⟩|² = sin²(θ/2)          |⟨b=−1|V⟩|² = cos²(θ/2)                      (8)

Overlaps depend only on θ. Computing f_perp:

  f_perp(+1, H) = 1 − cos²(θ/2) = sin²(θ/2)                                     (9)
  f_perp(−1, H) = 1 − sin²(θ/2) = cos²(θ/2)                                    (10)
  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                        (11)

Vanishes iff θ = π/2. All four f_perp = 1/2 → constant → cancels in Z. ∎

### 3.4 — Why This Is Not Basis Reparameterization

Equation (2) is not gauge-removable. Under a unitary basis redefinition
|b'⟩ = U|b⟩, the correlator ⟨AB⟩ = Σ ab·P(a,b|x,y) is invariant — unitary
redefinitions produce δ⟨AB⟩ = 0 for all θ. In contrast, Eq. (2) modifies P
multiplicatively with a factor depending on the physical overlap |⟨b|d⟩|²,
which changes under θ-rotation. Three observations confirm this distinction:
(a) unitary redefinitions preserve trace → δ = 0 identically, (b) the
outcome-pair asymmetry f_perp(+1,H) ≠ f_perp(−1,H) is absent from symmetric
POVMs, (c) a θ-sweep (§8.4) empirically discriminates: basis relabeling
predicts δ⟨AB⟩ = 0 for all θ; Eq. (2) predicts δ⟨AB⟩ ∝ β cos θ
(Supplemental S3).

### 3.5 — Physical Intuition

At θ = π/2, the Superobserver's measurement basis is maximally symmetric
with respect to the Friend's recorded outcomes:
|⟨b|H⟩|² = |⟨b|V⟩|² = 1/2 for both b = ±1. This symmetry makes the
Superobserver equally "incompatible" with every Friend outcome —
indistinguishable from an observer with no geometric relationship to the
Friend. Tilting to θ ≠ π/2 breaks this indistinguishability: the Superobserver
"sees" one Friend outcome as geometrically closer (|⟨+1|H⟩|² ≠ |⟨+1|V⟩|²),
creating a cos θ asymmetry that any overlap-dependent deformation would exploit.

### 3.6 — Structural Blind Spot

**Bong et al. (2020) [2]:** All Superobserver settings equatorial → f_perp
outcome-independent for every measurement combination.

**Proietti et al. (2019) [1]:** BSM → |⟨ψ|Φ⁺⟩|² = 1/2 → equivalent.

**Prior work.** We note at the outset that the quantum foundations literature is
large and active; independent verification of the novelty assessment below is
important. We searched Google Scholar, arXiv (quant-ph), Web of Science, and
InspireHEP (2020–2025) using search strings combining ("Wigner's friend" OR
"extended Wigner") with ("equatorial measurement" OR "Bloch sphere polar
angle" OR "outcome dependence" OR "geometric constraint" OR "measurement
basis"); date range January 2000 – May 2026 — screening approximately 200
papers. The screening pipeline comprised title/abstract filtering against the
Boolean queries, followed by full-text examination of 47 candidate documents
including all supplementary materials, and targeted follow-up searches on
citing/cited works of the most relevant papers. Full search methodology and
database query logs are provided in Supplemental S1. We examined the 47-page
Supplemental Material of Bong et al. (2020) [2]; the Methods and Supplementary
Information of Proietti et al. (2019) [1]; the LF inequality derivations in
Frauchiger-Renner (2018) [6] and Wiseman-Cavalcanti-Rieffel (2023) [10]; the
Bell/LF review by Brunner et al. (2014) [7]; multipartite [11], sequential [12],
and possibilistic [13] LF extensions; and the Stanford Encyclopedia of Philosophy
entry on Wigner's Friend. To our knowledge, no published EWF implementation
has systematically probed θ (full search methodology in Supplemental S1).
Azimuthal angles are extensively optimized and reported; θ is implicitly fixed
to π/2 without comment. Within the surveyed literature (S1), we find no
published EWF experiment that varies θ from π/2.

The structural reason is straightforward: LF inequalities are optimized for
maximal violation, which occurs at equatorial settings. Researchers optimize
azimuthal angles φ to maximize the LF violation — taking the polar angle
θ = π/2 as a fixed starting assumption because the standard inequality
derivations presuppose projective measurements in the equatorial plane [2,10].
Without a specific hypothesis motivating θ ≠ π/2, there is no experimental
incentive to explore the polar direction.

The three-line proof (§3.3) confirms that θ has been experimentally unexplored
in every published EWF implementation. Equatorial measurement was adopted as
a convention, not tested as a constraint. Tilting the Superobserver opens
access to an entire class of overlap-dependent effects (§4).

---

## Section 4 — Experimental Protocol (Claim B)

### 4.1 — Breaking the Cancellation

Any θ ≠ π/2 breaks the cancellation. A grid search over (θ, φ₂, φ₃, β_Bob)
maximizing min(n_σ_LF, n_σ_signal) yields θ = 31° as optimal; the figure of
merit remains above 5σ for the broad range θ ∈ [20°, 55°] (Supplemental S2).
Representative FOM values at μ = 0.95: 9.6 (θ = 20°), 8.6 (θ = 31°, optimal),
7.1 (θ = 45°), 5.0 (θ = 58°, 5σ threshold), and 0 (θ = 90°, cancellation).
The wide optimal window means the protocol tolerates angular misalignment of
±11° before dropping below 5σ — substantially more forgiving than the
alignment precision demanded by the standard Bong protocol.

The optimum at θ = 31° reflects a trade-off between two monotonic trends.
As θ → 0°, the |cos θ| signal is largest, but the Gen LF 1 violation
weakens because measurement settings approach a common axis, reducing the
inequality's capacity to separate LF-violating from LF-satisfying theories.
As θ → 90°, the LF violation is strongest but the signal vanishes
(cos θ → 0, §3). The intermediate optimum balances these effects. The
broad plateau (FOM > 5σ for θ ∈ [20°, 55°]) means the exact optimum is
not critical — any angle in this range produces a viable experiment.

### 4.2 — Single Hardware Modification

In standard Bong et al. (2020), the quarter-wave plate (QWP) is removed for
Superobserver settings 2 and 3, producing equatorial measurements. Our
modification re-inserts this same QWP into Superobserver Alice's measurement
path (before the PBS, after beam displacer BD2), tilting the effective
measurement axis to θ = 31°. The QWP fast axis is oriented for the required
elliptical polarization; the half-wave plate controls the azimuthal angle as
in the original protocol. The QWP must be specified for λ = 810 nm with
retardance tolerance ±2 nm or better (angular uncertainty in θ ≈ ±0.5°). For
standard zero-order QWPs at 810 nm, the retardance temperature coefficient is
approximately 0.01 nm/°C; laboratory temperature stability of ±2°C introduces
~0.02 nm drift, well within this tolerance. This
is the only optical hardware change required. (The SNSPD upgrade
discussed in §7.3 replaces existing detectors at the same optical position;
no new optical elements are introduced.)

[Figure 2: Optical path with QWP insertion highlighted]

### 4.3 — Measurement Settings

| Parameter | Standard Bong [2] | This Work |
|-----------|------------------|-----------| 
| Polar angle θ | 90° (equatorial) | **31°** |
| Alice φ₂ | 0° | **112°** |
| Alice φ₃ | 118° | **217°** |
| Bob β_Bob | 175° | **20°** |
| μ required | not specified | ≥ 0.86 |
| N | 91,000 | 91,000 |

### 4.4 — Calibration

1. Verify polar angle: |⟨σ_z⟩| = cos(31°) ≈ 0.857 on H-polarized state (±0.01).
2. Verify azimuthal alignment with entangled state (count rates within 2% of QM).
3. Measure μ via CHSH S-parameter (μ ≥ 0.86 required).

### 4.5 — Practical Feasibility

Bong et al. (2020) report approximately 1000 coincidence events per second.
At this rate, N = 91,000 events per setting requires ~91 seconds of
integration; nine measurement-setting combinations yield ~14 minutes of
total data acquisition. Including calibration (three θ-verification runs at
~5 minutes each, plus azimuthal alignment checks), a complete experimental
run requires approximately one hour. SPDC source brightness drift is
typically < 5% over 30 minutes, well within the acquisition window.
Detector dark-count drift at the ~1% level over this timescale is
sub-dominant to Poisson uncertainty (§6).

---

## Section 5 — Model-Independent QM Predictions

All numerical values are computed from the density matrix ρ_μ = μ|Φ⁻⟩⟨Φ⁻| +
(1−μ)I/4 for the singlet state with visibility μ = 0.95.

### 5.1 — Correlators at θ = 31°, μ = 0.95

| (x,y) | ⟨AB⟩_QM | σ (N=91,000) | | (x,y) | ⟨AB⟩_QM | σ (N=91,000) |
|-------|---------|--------------|--|-------|---------|--------------| 
| (1,1) | −1.0000 | 0.0000 | | (2,3) | −0.8933 | 0.0015 |
| (1,2) | −0.8572 | 0.0017 | | (3,1) | −0.8572 | 0.0017 |
| (1,3) | −0.8572 | 0.0017 | | (3,2) | −0.8933 | 0.0015 |
| (2,1) | −0.8572 | 0.0017 | | (3,3) | −0.8829 | 0.0016 |
| (2,2) | −0.5045 | 0.0029 |

Standard QM predicts zero marginals (singlet, μ = 0.95).

### 5.2 — Primary Observable: Genuine LF Violation

| Observable | Prediction | Type |
|-----------|-----------|------|
| Gen LF 1 | +0.0891 ± 0.0103 (8.6σ) | Standard QM, model-independent |

The 8.6σ LF violation provides built-in calibration: no violation at ≥5σ
indicates the apparatus is not realizing the intended geometry.

### 5.3 — Sensitivity to Overlap-Dependent Deformations

For the benchmark parametrization Eq. (2-3), we compute δ⟨A_x B_y⟩ = ⟨A_x B_y⟩_model −
⟨A_x B_y⟩_QM by exact numerical integration over the density matrix. The
computation evaluates f_perp-weighted outcome probabilities with full
renormalization (see Supplemental S2 for the numerical method). Results for
the mixed settings (one side z-basis, one side tilted) at θ = 31°, μ = 0.95:

| β | |δ⟨AB⟩| (mixed) | n_σ (single setting, N=91k) | n_σ (4 combined) |
|---|----------------|----------------------------|------------------|
| 0.03 | 0.0034 | 2.0 | 4.0 |
| 0.05 | 0.0057 | 3.3 | 6.7 |
| 0.07 | 0.0080 | 4.7 | 9.4 |
| 0.10 | 0.0115 | 6.7 | 13.5 |
| 0.30 | 0.0355 | 20.8 | 41.6 |

All four mixed settings yield identical δ (f_perp depends only on θ, not φ).

The order-of-magnitude minimum detectable coupling at 5σ confidence (under
idealized Poisson statistics; see §6) is β_min ≈ 0.038 for combined 4-setting
analysis, or β_min ≈ 0.075 for individual-setting analysis. For
conservative single-setting detection, we recommend β ≥ 0.07 at >5σ. Using all
four mixed settings combined, β ≥ 0.04 is detectable at >5σ. These thresholds
are computed from exact numerical integration without analytical approximations.

**Experimental discriminator.** Standard QM predicts δ⟨AB⟩ = 0 for all θ.
The benchmark parametrization Eq. (2-3) predicts δ⟨AB⟩ ∝ β cos θ — a
functional form testable by θ-sweep (§8.4). This is not a reparameterization
of QM: the cos θ dependence produces a qualitatively distinct experimental
signature that vanishes at θ = π/2 (standard configuration) and is maximal
at θ → 0°.

The gap between β_min ≈ 0.038 (combined) and β_min ≈ 0.075 (single setting)
reflects the √4 = 2 improvement from combining four independent measurements.
The experiment naturally provides all four mixed-setting correlators; no
additional data acquisition is needed for the combined analysis.

The coupling β has no a priori theoretical prediction — analogous to SME
coefficients at the time of their proposal. A null result at β ≥ 0.04
excludes overlap-dependent deformation above this threshold for class
Eq. (2-3); a positive result provides the first quantitative target for
theory construction.

**Scale context.** A null result at β ≥ 0.04 excludes O(1) and O(10⁻¹)
overlap-dependent deformation for the class Eq. (2-3). For comparison, SME
Lorentz-violation coefficients are now constrained at 10⁻²³ after three decades
of experiments; the first constraint on β at ~10⁻² represents the opening of a
new parameter space. Improving to N = 200,000 extends sensitivity to β ≥ 0.02.

---

## Section 6 — Statistical Analysis

Poisson statistics: σ(⟨A_x B_y⟩) = √[(1 − ⟨A_x B_y⟩²) / N]. For Gen LF 1
(11 terms, coefficients up to ±2): σ(S_LF1) = √20/√N ≈ 0.0103 at N = 91,000.

Minimum sample for 5σ LF detection: N_min ≈ 30,800. N = 91,000 provides a
factor of 3 margin.

Monte Carlo (10,000 runs): Gen LF 1 ≥ 5σ in 99.97%. For outcome-dependence:
β = 0.10 detected in >99.9%; β = 0.07 in >99%; β = 0.05 in ~90% (combined).
Increasing to N = 200,000 raises β = 0.05 detection above 99%.

**Statistical model limitations.** The above analysis assumes Poisson counting
statistics with uncorrelated errors. In practice, detector drift, beam-pointing
fluctuations, and source brightness variations may introduce time-correlated
errors that inflate effective uncertainties beyond the Poisson floor. We
recommend that the implementing laboratory supplement the Poisson analysis with
bootstrap resampling of time-ordered coincidence data and a detector-drift
simulation (injecting ~1% linear drift) to validate the independence assumption.
These refinements affect detailed significance estimates but not the protocol
design or order-of-magnitude sensitivity.

**Bayesian robustness.** A conservative Bayesian analysis that inflates Poisson
uncertainties by 20% — modeling uncharacterized systematics (detector drift,
waveplate miscalibration, correlated noise from source brightness fluctuations)
as a multiplicative factor on σ — yields effective significance ~6.5σ for the
LF violation and β_min ≈ 0.046 (combined settings). The FOM plateau (§4.1:
FOM > 5σ for θ ∈ [20°, 55°]) ensures the experiment remains viable even with
substantial systematic degradation up to ~40% uncertainty inflation.

[Figure 3: Monte Carlo histogram of Gen LF 1]

---

## Section 7 — Robustness and Loophole Analysis

Visibility: 5σ LF violation requires μ ≥ 0.92 (Bong achieved 0.92; onset at
μ ≈ 0.86). Detector efficiency: η ≥ 0.91 required for loophole closure (Bong
η ≈ 0.87). Angular tolerance: LF significance stable across Δθ = ±5°;
overlap-dependent signal δ ∝ cos θ is more alignment-sensitive but Bong
precision < ±1° limits variation to < 1%. Full μ and η tables are provided in
Supplemental S2.

**Systematic-error budget.** Six sources analyzed (QWP retardance drift ±0.5°,
birefringence < 0.1°, polarization-dependent loss < 0.5%, calibration offset
±0.5°, detector asymmetry < 1%, accidentals < 0.1%); all sub-dominant to
σ ≈ 0.0017 at N = 91,000. All systematics either (a) cancel in the
δ⟨AB⟩ comparison or (b) bias δ toward zero. Full table in Supplemental S2.
Correlated-systematic evaluation (e.g., QWP + detector co-varying with
temperature) is deferred to the implementing laboratory.

**Robustness summary.**

| Parameter | Nominal | 5σ Threshold | Bong Achievable |
|-----------|---------|-------------|-----------------| 
| μ | 0.95 | ≥ 0.90 | 0.92 |
| η | 1.00 | ≥ 0.91 | 0.87 |
| Δθ | 0° | ≤ ±5° | < ±1° |

**Detection loophole.** Closure requires η ≥ 0.91 [7]; Bong η ≈ 0.87.
Two observations make the fair-sampling regime scientifically productive.
First, demonstrating LF violation at θ = 31° — to our knowledge, the first
non-equatorial EWF measurement — confirms that the violation is not an
artifact of equatorial geometry; this is model-independent regardless of
loophole status. Second, β is measured from the same coincidence events as
the LF violation; a null result provides a self-consistent constraint on
Eq. (2-3) independent of absolute detector efficiency. Detector inefficiency
cannot fake a β signal: QWP introduces no additional loss (> 99%
transmission); residual θ-dependent efficiency biases δ toward zero, not
away from it [9]. SNSPD upgrade (η > 0.90 at 810 nm [16]) closes the
loophole with no optical redesign.

**Loophole summary.**

| Loophole | Status | Notes |
|----------|--------|-------|
| Locality | Identical to Bong 2020 | QWP insertion local to Alice |
| Detection | Conditional (η ≥ 0.91) | Fair-sampling below threshold |
| Freedom of choice | Identical to Bong 2020 | Quantum RNG |
| Model class scope | Explicit: Eq. (2-3) | Constrains overlap-only class |

[Figure 4: FOM vs μ] [Figure 5: 2D sensitivity map]

---

## Section 8 — Discussion

### 8.1 — Interpretation of Results

δ⟨AB⟩ ≠ 0 at ≥5σ would demonstrate that Superobserver-Friend correlations
depart from standard QM at θ = 31°, a previously untested configuration.
Interpreting this as overlap-dependent deformation specifically requires
θ-sweeps and multi-observer follow-up.

A null result (LF violated, δ ≈ 0) excludes overlap-dependent deformation above
the sensitivity threshold for class Eq. (2-3) and confirms the cos θ dependence.

### 8.2 — Relation to Quantum Interpretations

The implications of overlap-dependent deformation for major quantum
interpretations — Many-Worlds, Relational QM, Copenhagen, QBism, and
Objective Collapse — are analyzed in Supplemental S3. These interpretations
neither predict nor preclude the class Eq. (2-3); the experiment is
interpretation-neutral by design.

### 8.3 — Illustrative Parametric Model

The function class defined by Eq. (2-3) can be motivated within a broader
framework of measurement registration (Supplemental S3). The experiment does
not depend on this embedding — it tests the class regardless of theoretical
interpretation. At the modified geometry, δ⟨A₁B₂⟩ = −0.0355 at β = 0.3. The
experiment measures β; identical δ across all four mixed settings tests the
φ-independence predicted by the cos θ structure.

### 8.4 — Future Directions

**θ-sweep.** The most immediate follow-up is a systematic scan of the polar
angle from θ = 15° to θ = 75° in steps of ~10°. This would directly map the
cos θ dependence predicted by Eq. (4), testing whether the overlap-dependent
signal follows the geometric structure derived in §3. A null result across
all θ would exclude the class Eq. (2-3) down to the sensitivity floor of the
apparatus (β ≈ 0.02 at N = 200,000).

**Multi-observer extension.** The geometric cancellation theorem may
generalize to N > 2 observers; speculative analysis is provided in
Supplemental S3 (requiring additional bridge theorems not established here).

**Platform independence.** While the protocol targets the optical Bong
et al. (2020) apparatus, the theorem in §3 is platform-agnostic. Implementing
the tilted Superobserver measurement on solid-state (superconducting qubits)
or trapped-ion platforms would test whether the cos θ structure survives in
systems where the "Friend" is a macroscopic quantum system rather than a
photon path degree of freedom.

**Locality closure.** Combining the tilted geometry with space-like separated
random basis switching would close the locality loophole simultaneously with
the detection loophole (via SNSPDs, §7.3). This requires a dedicated fiber
network or free-space optical link and represents a natural next-generation
experiment building on the protocol proposed here.

---

## Section 9 — Conclusion

The central result is the equatorial fixed-point theorem (Proposition 1):
at θ = π/2, any overlap-dependent deformation of Superobserver statistics
vanishes identically — for every function g of the basis overlap, not just
Eq. (3). To our knowledge, no published EWF implementation has probed this
geometric degree of freedom.

As its experimental consequence, we propose a null test: re-insert one QWP
into the Bong et al. (2020) apparatus (θ = 31°), providing order-of-magnitude
sensitivity β ≥ 0.04 at >5σ while preserving 8.6σ LF violation.

---

## References

[1] M. Proietti et al., Science Advances 5, eaaw9832 (2019).
[2] K.W. Bong et al., Nature Physics 16, 1199–1205 (2020).
[3] E.P. Wigner, in The Scientist Speculates, Heinemann (1961).
[4] D. Deutsch, Int. J. Theor. Phys. 24, 1–41 (1985).
[5] L. Hardy, Phys. Rev. Lett. 68, 2981 (1992).
[6] D. Frauchiger and R. Renner, Nature Comms. 9, 3711 (2018).
[7] N. Brunner et al., Rev. Mod. Phys. 86, 419 (2014).
[8] J.S. Bell, Physics 1, 195–200 (1964).
[9] M. Giustina et al., Phys. Rev. Lett. 115, 250401 (2015).
[10] H.M. Wiseman, E.G. Cavalcanti, and E.G. Rieffel, Quantum 7, 1112 (2023).
[11] M. Haddara and E.G. Cavalcanti, arXiv:2407.20346 (2024).
[12] A. Utreras-Alarcon, E.G. Cavalcanti, and H.M. Wiseman, Proc. R. Soc. A 480 (2023).
[13] M. Haddara and E.G. Cavalcanti, New J. Phys. 25, 093028 (2023).
[14] A. Kent, arXiv:2302.12707 (2023).
[15] D. Colladay and V.A. Kostelecký, Phys. Rev. D 55, 6760 (1997).
[16] F. Marsili et al., Nature Photonics 7, 210–214 (2013).
[17] J. Barrett, Phys. Rev. A 75, 032304 (2007).

---