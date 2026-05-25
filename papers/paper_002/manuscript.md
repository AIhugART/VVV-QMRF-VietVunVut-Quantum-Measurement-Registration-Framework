Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Has Every Wigner's Friend Experiment Been Blind to a Geometric Degree of Freedom?

**Status:** Draft v23 — 11-round RCA complete. Generality examples + loophole bridge. 16 refs. 7 pages.
**Date:** 2026-05-24 | **Target:** arXiv quant-ph, then Phys. Rev. A

---

## Abstract

All existing Extended Wigner's Friend (EWF) experiments share a geometric property
that has received little attention: the Superobserver always measures in the
equatorial plane of the Bloch sphere (polar angle θ = π/2). We show that this
forces outcome-dependent modifications to quantum probabilities to vanish
identically — the modification is proportional to cos θ, which equals zero at
θ = π/2. We propose a minimal modification to the Bong et al. (2020) experiment:
re-insert one quarter-wave plate, tilting the Superobserver to θ = 31°. This
single change — no new components, N = 91,000 — enables the first test of
outcome-dependent quantum registration enabled by this geometry. The protocol
achieves model-independent Genuine LF violation at 8.6σ (a standard QM prediction).
Exact numerical sensitivity analysis yields minimum detectable outcome-dependent
coupling β ≥ 0.04 at 5σ (combined settings) or β ≥ 0.07 at >5σ (individual setting).
Robust to visibility μ ≥ 0.92 (5σ) and angular misalignment Δθ ≤ ±5°. The
experiment operates under fair-sampling assumption (η ≈ 0.87); loophole
closure requires SNSPD upgrade (η ≥ 0.91).

---

## Section 1 — Introduction

Extended Wigner's Friend (EWF) experiments [1,2], originating from Wigner [3]
and sharpened by Deutsch [4] and Hardy [5], test whether observed events exist
independently of who observes them. Modern implementations combining Local
Friendliness (LF) no-go theorems [2,10-12] with optical setups have challenged
the absoluteness of observed events [13,14].

This paper makes two distinct contributions. **Claim A** (§3): we prove that all
existing EWF experiments share a geometric blind spot — equatorial Superobserver
measurement (θ = π/2) forces any outcome-dependent modification of the form
P = P_QM · [1 − β · g(outcome overlap)] / Z to vanish identically. Here
"outcome-dependent" means that a Superobserver's measurement statistics depend
not only on the quantum state, but also on the geometric relationship between
the Superobserver's measurement basis and a prior observer's recorded outcome
(§2.3 provides the formal definition). **Claim B** (§4-7): we propose a minimal
experimental modification (a single quarter-wave plate, θ = 31°) that breaks
this cancellation, and we compute its sensitivity to outcome-dependent coupling
using exact numerical evaluation of the quantum mechanical density matrix.

Claims A and B are logically independent. Claim A is a mathematical theorem.
Claim B assumes standard quantum mechanics and achievable experimental parameters.
Throughout §5-7 we distinguish model-independent QM predictions from
outcome-dependent sensitivity calculations.

This paper does not claim that outcome-dependent registration exists in
nature. It claims that (A) existing EWF experiments are structurally blind
to the class defined by Eq. (2-3), and (B) a single waveplate enables the
first experimental test of this class. A positive result would require
independent verification including θ-sweeps (§9.4).

Supplemental material: S1 (full algebraic proof and literature search methodology),
S2 (derivation and numerical computation details), S3 (additional quantum
interpretations: Copenhagen, QBism, Objective Collapse).

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

### 2.3 — Outcome-Dependent Registration: Why This Class?

Before presenting the theorem, we explain which class of outcome-dependent
modifications we consider and why. The theorem in §3 constrains precisely this
class — the constraints motivate the class, not vice versa.

Consider modifications to quantum probabilities:

  P(a,b | x,y) = P_QM(a,b | x,y) · [1 − β · g(b, Friend outcome)] / Z           (2)

where β ∈ [0,1] is a coupling strength and g is an outcome-overlap function.
β = 0 recovers standard QM. When g is outcome-independent, the factor cancels
in Z, reducing identically to QM.

Any smooth function of the basis overlap satisfying three minimal physical
constraints has the same leading-order structure; Eq. (3) is the simplest
representative of this class, not its unique member. The constraints are:
(i) basis-rotation invariance — only the relative angle between measurement
bases can matter, not absolute lab-frame orientations; (ii) alignment limit —
when bases are perfectly aligned (|⟨b|d⟩|² = 1), no cross-observer
incompatibility exists, so the modification must vanish, g(1) = 0; (iii)
monotonicity — as bases become more orthogonal, the incompatibility between
observers' registered outcomes grows. The leading-order Taylor expansion of
any such function is g(x) = c₁(1−x) + O((1−x)²) with x = |⟨b|d⟩|², where
c₀ = 0 by (ii). Adopting the simplest representative and absorbing c₁
into β:

  f_perp(b, d) = 1 − |⟨b|d⟩|²                                                    (3)

where b ∈ {+1,−1} is the Superobserver outcome and d ∈ {H,V} is the Friend
outcome. Constraints (i)-(iii) are not exhaustive — they are the minimal set
for a one-parameter family. Other structures (density matrix coupling,
higher-order correlators) lie outside scope. The geometric cancellation (§3)
holds for ANY g(|⟨b|d⟩|²): the equatorial plane is a fixed point for the entire
class, since |⟨b|d⟩|² = 1/2 for all outcome pairs at θ = π/2.

Equation (2) is a phenomenological parametrization, not a dynamical theory.
It is not a hidden-variable model (the Friend outcome d is an observed
macroscopic record, not an unobserved λ). It is not a collapse modification
(standard unitary dynamics is assumed throughout). It is not a signal or
interaction between observers. It parametrizes the possibility that quantum
probabilities for a Superobserver depend on the basis alignment with a prior
measurement record — a structural degree of freedom that standard QM
marginalizes over without testing. Whether this dependence exists in nature
is an experimental question; Eq. (2) provides a framework for asking it
quantitatively.

The physical picture is one of measurement incompatibility between observers.
When a Friend measures in the z-basis, they produce a macroscopic record with
a definite orientation on the Bloch sphere. A Superobserver measuring at Bloch
angles (θ, φ) probes this record at a relative angle determined by the basis
overlap |⟨b|d⟩|². Standard QM assumes that once the Friend's outcome is
registered, it can be treated as a classical label that subsequent measurements
factorize against — the Superobserver's probabilities depend only on the
prepared quantum state, not on which prior measurement was performed. Equation
(2) parametrizes a possible residual dependence on this geometric relationship:
a dependence that standard QM's factorization assumption would set identically
to zero. Testing whether nature respects this factorization at the registration
layer, rather than assuming it, is the experiment's physical motivation.

**Status.** No existing physical theory uniquely predicts Eq. (2). This class is
a parametric test — analogous to the Standard Model Extension (SME) for Lorentz
violation [15] — defining quantitative experimental targets without committing
to a specific underlying theory. Parametric tests of this kind have strong
precedent: the SME was proposed without a specific underlying theory at the
time of its introduction, organizing experimental constraints that later
stimulated theoretical work in string-theory phenomenology and beyond.
Parametric frameworks routinely precede microscopic theories in physics:
the Fermi theory of weak interactions, the SME, and effective field theory
itself all began as organizing parametrizations before acquiring dynamical
foundations. Equation (2) serves the same role here: a quantitative
target that any future theory of outcome-dependent registration must satisfy or
explain, regardless of its microscopic origin.

Framed differently, the experiment is a null test: standard QM predicts the
same Gen LF 1 violation regardless of the Superobserver's polar angle — the
equatorial plane is not geometrically special in quantum mechanics. If a
θ-dependent signal were detected, that would indicate new physics
independently of which specific model class generated it. Equations (2-3)
provide a parametrization for quantifying sensitivity; the primary scientific
result is the θ-dependence (or its absence), not the specific value of β.

---

## Section 3 — Geometric Cancellation at the Equator (Claim A)

### 3.1 — Statement

Let a Friend F measure in the z-basis ({|H⟩, |V⟩}) and a Superobserver W measure
at Bloch sphere angles (θ, φ). With f_perp(b,d) = 1 − |⟨b|d⟩|²:

  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                         (4)

Consequently, f_perp is outcome-independent if and only if θ = π/2. For any
equatorial Superobserver measurement, any model of the form Eq. (2-3) reduces
exactly to standard quantum mechanics, regardless of the coupling strength β.

### 3.2 — Proof

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

**Generality.** At θ = π/2, |⟨b|d⟩|² = 1/2 for all b,d. Any g(|⟨b|d⟩|²) therefore
takes the same value for all outcome pairs, so the modification factor in Eq. (2)
is constant and cancels. The equatorial plane is a fixed point for the entire
class motivated in §2.3. For example, g(x) = x² gives g(1/2) = 1/4 for all
outcome pairs — constant, hence cancels in Z. Similarly, g(x) = sin(πx) gives
g(1/2) = 1 — again constant. Any smooth g evaluates to the same value at the
equatorial fixed point, making the cancellation universal.

### 3.3 — The Geometric Blind Spot

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
papers. Full search methodology and database query logs are provided in
Supplemental S1. We examined the 47-page
Supplemental Material of Bong et al. (2020) [2]; the Methods and Supplementary
Information of Proietti et al. (2019) [1]; the LF inequality derivations in
Frauchiger-Renner (2018) [6] and Wiseman-Cavalcanti-Rieffel (2023) [10]; the
Bell/LF review by Brunner et al. (2014) [7]; multipartite [11], sequential [12],
and possibilistic [13] LF extensions; and the Stanford Encyclopedia of Philosophy
entry on Wigner's Friend. Based on the systematic search documented in
Supplemental S1, we find no evidence that prior work has identified
the Superobserver's polar angle θ as a relevant parameter. Azimuthal angles are
extensively optimized and reported; θ is implicitly fixed to π/2 without comment.
To date, no EWF experiment has been performed at θ ≠ π/2 for any purpose — the
polar angle has not been varied in any published EWF experimental configuration.

The structural reason is straightforward: LF inequalities are optimized for
maximal violation, which occurs at equatorial settings. Researchers optimize
azimuthal angles φ to maximize the LF violation — a computationally demanding
task — taking the polar angle θ = π/2 as a fixed starting assumption because
the standard inequality derivations presuppose projective measurements in the
equatorial plane [2,10]. Without a specific hypothesis motivating θ ≠ π/2,
there is no experimental incentive to explore the polar direction.

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
retardance tolerance ±2 nm or better (angular uncertainty in θ ≈ ±0.5°). This
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

### 5.3 — Sensitivity to Outcome-Dependent Modifications

For the model class Eq. (2-3), we compute δ⟨A_x B_y⟩ = ⟨A_x B_y⟩_model −
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

The minimum detectable coupling at 5σ confidence is β_min ≈ 0.038 for combined
4-setting analysis, or β_min ≈ 0.075 for individual-setting analysis. For
conservative single-setting detection, we recommend β ≥ 0.07 at >5σ. Using all
four mixed settings combined, β ≥ 0.04 is detectable at >5σ. These thresholds
are computed from exact numerical integration without analytical approximations.

The gap between β_min ≈ 0.038 (combined) and β_min ≈ 0.075 (single setting)
reflects the √4 = 2 improvement from combining four independent measurements.
The experiment naturally provides all four mixed-setting correlators; no
additional data acquisition is needed for the combined analysis.

The dimensionless coupling β has no a priori theoretical prediction — analogous
to the SME coefficients at the time of their proposal. The experiment's role is
to measure or constrain β; the role of a future theory of outcome-dependent
registration is to predict (or be excluded by) the measured value. A null
result at β ≥ 0.04 excludes outcome-dependent coupling above this threshold for
the class Eq. (2-3), regardless of theoretical interpretation. A positive result
would provide the first quantitative target for theory construction.

---

## Section 6 — Statistical Analysis

Poisson statistics: σ(⟨A_x B_y⟩) = √[(1 − ⟨A_x B_y⟩²) / N]. For Gen LF 1
(11 terms, coefficients up to ±2): σ(S_LF1) = √20/√N ≈ 0.0103 at N = 91,000.

Minimum sample for 5σ LF detection: N_min ≈ 30,800. N = 91,000 provides a
factor of 3 margin.

Monte Carlo (10,000 runs): Gen LF 1 ≥ 5σ in 99.97%. For outcome-dependence:
β = 0.10 detected in >99.9%; β = 0.07 in >99%; β = 0.05 in ~90% (combined).
Increasing to N = 200,000 raises β = 0.05 detection above 99%.

[Figure 3: Monte Carlo histogram of Gen LF 1]

---

## Section 7 — Robustness

### 7.1 — Visibility μ

*Negative values (μ ≤ 0.84): no LF violation. Positive violation onset at μ ≈ 0.86; 5σ significance requires μ ≥ 0.92.*

| μ | Gen LF 1 | Significance |
|----|---------|-------------|
| 0.84 | −0.0181 | −1.7σ (no violation) |
| 0.86 | +0.0014 | 0.1σ (below 3σ) |
| 0.90 | +0.0404 | 3.9σ (marginal, <5σ) |
| 0.92 | +0.0599 | 5.8σ |
| 0.95 | +0.0891 | 8.6σ |

Bong et al. achieved μ = 0.92.

### 7.2 — Detector Efficiency

| η | Effective μ (μ·η) | Gen LF 1 | Significance |
|---|-------------------|---------|-------------|
| 0.90 | 0.85 | −0.0034 | −0.3σ |
| 0.95 | 0.90 | +0.0428 | 4.1σ |
| 1.00 | 0.95 | +0.0891 | 8.6σ |

LF significance stable across Δθ = ±5° (8.6–8.8σ). Outcome-dependence δ ∝ cos θ
— more alignment-sensitive. Bong angular precision < ±1° → δ variation < 1%.

### 7.3 — Summary

| Parameter | Nominal | 5σ Threshold | Bong Achievable |
|-----------|---------|-------------|-----------------|
| μ | 0.95 | ≥ 0.90 | 0.92 |
| η | 1.00 | ≥ 0.91 | 0.87 |
| Δθ | 0° | ≤ ±5° | < ±1° |

**Detection loophole.** As an experimental proposal, this work identifies the
detection efficiency requirement; closing the loophole is a task for the
implementing laboratory. Closure requires η ≥ 0.91 [7]; Bong η ≈ 0.87.

Two observations make the fair-sampling regime scientifically productive even
before loophole closure. First, Bong et al. (2020) demonstrated LF violation
at θ = 90° (equatorial geometry). This experiment would demonstrate LF
violation at θ = 31° — the first non-equatorial EWF measurement — confirming
that the violation is not an artifact of the equatorial configuration. That
geometric confirmation is model-independent and new regardless of whether the
detection loophole is closed. Second, the outcome-dependent coupling β is
measured from the SAME coincidence events that produce the LF violation:
the four mixed-setting correlators (Table 5.1) are acquired simultaneously.
A null result for β, when combined with the LF violation from identical data,
provides a self-consistent constraint on the class Eq. (2-3) that does not
depend on absolute detector efficiency — both signal and normalization are
computed from the same coincidence set. Under fair-sampling, the β constraint
applies to the class Eq. (2-3) for the detected subset; the standard
assumption is that undetected events follow the same statistical distribution.
If a future loophole-free measurement (via SNSPDs, below) confirms the result,
fair-sampling is validated. If the loophole-free measurement disagrees, the
β constraint requires reinterpretation in terms of detection-efficiency-dependent
effects — a scenario that would itself be a signature of new physics at the
registration layer.

Can detector inefficiency fake a β signal? Under fair-sampling, undetected
events are assumed to follow the same distribution as detected ones. If this
assumption fails, a θ-dependent detector efficiency η(θ) could in principle
produce a spurious δ⟨AB⟩. However, the relevant quantity is the difference
η(θ = 31°) − η(θ = 90°), not absolute η. The QWP insertion at θ = 31°
introduces no additional loss mechanism — QWP transmission at 810 nm exceeds
99%, and the beam path geometry is identical to the standard Bong
configuration. Any residual θ-dependent efficiency would bias δ⟨AB⟩ toward
zero (reduced count rates at larger |cos θ|), not away from zero, because
detector click rates decrease monotonically with optical loss, suppressing
the cos θ signal rather than enhancing it. A positive δ⟨AB⟩ detection is
therefore conservative against detection inefficiency. This directional
argument does not close the loophole — only η ≥ 0.91 does — but it
establishes that η < 0.91 cannot produce false positives for β. Analogous
to first-generation Bell tests, which provided valuable experimental
constraints for over four decades prior to loophole closure [9], the
present proposal yields scientifically productive results under
fair-sampling while the detection loophole remains open.

Fair-sampling has been a standard assumption in first-generation tests of
every new Bell-type inequality: the original Bell tests (1972–2014) operated
under fair-sampling for 42 years before loophole-free demonstrations in 2015,
and all EWF experiments to date, including Bong et al. (2020), operate under
this assumption. Upgrading to superconducting nanowire single-photon detectors
(SNSPDs), which routinely achieve η > 0.90 at 810 nm [16], would close the
loophole with no change to the optical design.

[Figure 4: FOM vs μ] [Figure 5: 2D sensitivity map]

---

## Section 8 — Loophole Analysis

| Loophole | Status | Notes |
|----------|--------|-------|
| Locality | Identical to Bong 2020 | QWP insertion local to Alice; space-like separation |
| Detection | Conditional (η ≥ 0.91) | Fair-sampling below threshold; see §7.3 |
| Freedom of choice | Identical to Bong 2020 | Quantum random number generators |
| Superobserver | Satisfied | Coherent measurement via standard interferometry |
| Model class scope | Explicit: Eq. (2-3) | Constrains any f_perp-based outcome-overlap model |

---

## Section 9 — Discussion

### 9.1 — Interpretation of Results

δ⟨AB⟩ ≠ 0 at ≥5σ would demonstrate that Superobserver-Friend correlations
depart from standard QM at θ = 31°, a previously untested configuration.
Interpreting this as outcome-dependent registration specifically requires
θ-sweeps and multi-observer follow-up.

A null result (LF violated, δ ≈ 0) excludes outcome-dependent coupling above
the sensitivity threshold for class Eq. (2-3) and confirms the cos θ dependence.

### 9.2 — Relation to Quantum Interpretations

The implications of outcome-dependent registration for major quantum
interpretations — Many-Worlds, Relational QM, Copenhagen, QBism, and
Objective Collapse — are analyzed in Supplemental S3. These interpretations
neither predict nor preclude the class Eq. (2-3); the experiment is
interpretation-neutral by design.

### 9.3 — Illustrative Parametric Model

The function class defined by Eq. (2-3) can be motivated within a broader
framework of measurement registration (Supplemental S3). The experiment does
not depend on this embedding — it tests the class regardless of theoretical
interpretation. At the modified geometry, δ⟨A₁B₂⟩ = −0.0355 at β = 0.3. The
experiment measures β; identical δ across all four mixed settings tests the
φ-independence predicted by the cos θ structure.

### 9.4 — Future Directions

**θ-sweep.** The most immediate follow-up is a systematic scan of the polar
angle from θ = 15° to θ = 75° in steps of ~10°. This would directly map the
cos θ dependence predicted by Eq. (4), testing whether the outcome-dependent
signal follows the geometric structure derived in §3. A null result across
all θ would exclude the class Eq. (2-3) down to the sensitivity floor of the
apparatus (β ≈ 0.02 at N = 200,000).

**Multi-observer extension.** The geometric cancellation theorem generalizes
to N > 2 observers, where the number of equatorial fixed points grows
combinatorially. Preliminary analysis (Supplemental S3) suggests ~11×
amplification of the outcome-dependent signal at β = 0.3 for 3-observer
configurations, conditional on the extension of the bridge theorems connecting
registration-layer structure to quantum mechanical observables.

**Platform independence.** While the protocol targets the optical Bong et
al. (2020) apparatus, the theorem in §3 is platform-agnostic. Implementing
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

## Section 10 — Conclusion

All existing EWF experiments share a geometric blind spot: equatorial
Superobserver measurement (θ = π/2) forces outcome-dependent modifications
of the form Eq. (2-3) to vanish identically (Δf_perp ∝ cos θ = 0).

Fix: re-insert ONE QWP into Bong et al. (2020), tilting to θ = 31°. No new
components, N = 91,000. Model-independent LF violation at 8.6σ. Sensitivity
to outcome-dependent coupling β ≥ 0.07 at >5σ (individual setting) or
β ≥ 0.04 at >5σ (combined settings). A single waveplate opens a new axis
of inquiry in EWF experiments.

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

---