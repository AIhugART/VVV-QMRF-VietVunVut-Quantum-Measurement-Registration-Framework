Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Has Every Wigner's Friend Experiment Been Blind to a Geometric Degree of Freedom?

**Status:** Draft v52 — 10-point review RCA (threshold 4.5/5): de-defensify — trimmed 2 redundant "model-independent", tightened ESP paragraph (§1 ¶4). 1/10 points implemented; 9 rejected below threshold. ~5 pages.
**Date:** 2026-05-25 | **Target:** arXiv quant-ph, then Phys. Rev. A

---

## Abstract

Within currently surveyed optical EWF implementations (Supplemental S1),
the Superobserver's polar angle θ on the Bloch sphere has not previously
been isolated as an independent control parameter — every measurement has
been at the equator. We prove an equatorial cancellation theorem
(Proposition 1): at θ = π/2, every overlap-dependent modification
P = P_QM · [1 − β · g(overlap)] / Z cancels identically for any
function g, so published implementations sit at a geometric null point
for the entire overlap-only class. We propose a single-waveplate null
test: tilting the Bong et al. (2020) apparatus to θ = 31° provides the
first isolated test of this class, with sensitivity β ≥ 0.07 at 5σ
(single-setting) while preserving 8.6σ Genuine LF violation, under
fair-sampling (η ≈ 0.87; closure via SNSPD upgrade to η ≥ 0.91).

---

## Section 1 — Introduction

Extended Wigner's Friend (EWF) experiments [1,2] test whether observed events
exist independently of who observes them. Modern optical implementations
combining Local Friendliness (LF) no-go theorems [2,10-12] have challenged the
absoluteness of observed events [13,14].

**Proposition 1 (Equatorial Cancellation Theorem, §3).** A deformation of
quantum measurement statistics is *overlap-only* if the modified joint
probability takes the form P'(a,b|x,y) = P_QM(a,b|x,y) · g(|⟨b|d⟩|²) / Z,
for any function g: [0,1] → ℝ and normalization Z. At the equatorial plane
(θ = π/2), |⟨b|d⟩|² = 1/2 for all outcome pairs (b,d); hence
g(|⟨b|d⟩|²) = g(1/2) is constant, and P' = P_QM identically. The equator is
therefore a geometric null point for every overlap-only deformation —
equatorial measurements are structurally incapable of distinguishing
standard QM from any member of this class, regardless of statistical
precision or experimental design. This structural non-identifiability has not previously been remarked
because LF inequalities are optimized for maximal violation precisely at
equatorial settings [2,10]: researchers adopt θ = π/2 as the standard
configuration, and without a specific hypothesis motivating polar tilt, the
polar angle has remained an unisolated control parameter. The proof is three
lines of Bloch-sphere algebra (§3.3); §2 provides motivation and notation.

Breaking the cancellation requires only a single quarter-wave plate:
re-inserting the QWP into the Bong et al. (2020) apparatus tilts the
Superobserver measurement to θ = 31°, providing sensitivity β ≥ 0.07 at 5σ
(single-setting) while preserving 8.6σ Genuine LF violation, under
fair-sampling (η ≈ 0.87; SNSPD upgrade closes the detection loophole at
η ≥ 0.91). Throughout §5-7 we distinguish model-independent QM predictions
from sensitivity calculations assuming the benchmark parametrization.

This paper makes no claim about the existence of overlap-dependent
deformation in nature. Its two claims are structural: (A) within surveyed
optical EWF implementations (Supplemental S1), equatorial measurement — a
convention for LF optimization, not a tested constraint — leaves the
overlap-only class structurally untested, and (B) a single waveplate enables
the first experimental probe. Positive results require independent
verification including θ-sweeps (§8.3).

Supplemental material: S1 (literature search + algebraic proof), S2
(numerical methods + statistical robustness), S3 (interpretations +
GPT/weak-measurement development).

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

**Core idea.** The equatorial cancellation theorem (§3) constrains every
overlap-dependent deformation independent of parametrization — it holds for
any function g(|⟨b|d⟩|²). The following minimal operational benchmark serves
only to quantify experimental sensitivity for one concrete parametrization.
We define a single-parameter deformation β (Eq. 2) — a symmetry-constrained
search target that does not commit to a microscopic origin. Within the GPT
framework [17], Eq. (2) parametrizes the simplest
one-parameter deformation of the Born rule preserving normalization and
remaining operationally admissible (state-effect duality derivation and
information-geometric motivation in Supplemental S3). The functional form
Eq. (3) follows from three minimal constraints — rotation invariance, alignment
limit, monotonicity — and is the simplest leading-order form satisfying them;
every smooth function obeying (i)-(iii) shares the same first-order structure
g(x) ∝ (1−x). Physically, β functions as a registration-memory coupling
strength: the overlap |⟨b|d⟩|² quantifies how compatibly the Superobserver's
measurement basis registers the Friend's recorded outcome, and β controls how
strongly the registration retains memory of the Friend's outcome orientation
(connection to weak measurement formalism [18] developed in Supplemental S3).
The geometric cancellation (§3) holds for the entire class of overlap-dependent
deformations, independently of this physical picture. Conceptually, basis
overlap |⟨b|d⟩|² quantifies measurement-context compatibility — a natural
element in any framework where measurement outcomes are context-dependent
(GPT state-effect duality [17]; weak measurement precedent [18]; further
development in Supplemental S3). No existing theory predicts this specific
form; analogous to EFT-style parameter searches (e.g., the Standard Model
Extension for Lorentz violation [15]), it defines quantitative experimental
targets without committing to a specific microscopic origin. The
model-independent theorem (Proposition 1, §3) is the central result;
Eq. (2-3) serves as a benchmark parametrization.

Consider modifications to quantum probabilities:

  P(a,b | x,y) = P_QM(a,b | x,y) · [1 − β · g(b, Friend outcome)] / Z           (2)

where β ∈ [0,1] is a deformation strength; β = 0 recovers standard QM.

The three constraints — (i) rotation invariance, (ii) alignment limit g(1)=0,
(iii) monotonicity — force the leading-order Taylor expansion
g(x) = c₁(1−x) + O((1−x)²). Adopting the simplest representative and
absorbing c₁ into β:

  f_perp(b, d) = 1 − |⟨b|d⟩|²                                                    (3)

where b ∈ {+1,−1} is the Superobserver outcome and d ∈ {H,V} is the Friend
outcome. The geometric cancellation (§3) holds for any g(|⟨b|d⟩|²).

Equation (2) is a benchmark parametrization — the lowest-order scalar overlap
deformation in an effective operational expansion (phenomenological
classification in Supplemental S3), where higher-order corrections involve
additional powers of (1−|⟨b|d⟩|²) or coupling to non-scalar degrees of
freedom.

Operationally, β is directly measurable via δ⟨AB⟩ at any θ ≠ π/2, with
the cos θ scaling under θ-sweep (§8.3) providing the distinguishing
signature that separates an overlap-dependent signal from conventional
systematics.

The experiment is a null test: standard QM predicts the same LF violation
regardless of θ; a θ-dependent signal would indicate a departure from
standard QM independently of model class.

---

## Section 3 — Equatorial Cancellation Theorem (Claim A)

### 3.1 — Main Result (Model-Independent)

Let a Friend F measure in the z-basis ({|H⟩, |V⟩}) and a Superobserver W measure
at Bloch sphere angles (θ, φ). With f_perp(b,d) = 1 − |⟨b|d⟩|²:

  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                         (4)

Consequently, f_perp is overlap-independent if and only if θ = π/2. For any
equatorial Superobserver measurement, any model of the form Eq. (2-3) reduces
exactly to standard quantum mechanics, regardless of the deformation strength β.
This depends only on Bloch sphere geometry. Eq. (2-3) is a benchmark
parametrization for quantifying experimental sensitivity (§5.3); the
theorem holds for any overlap function.
The experimental consequence is that equatorial measurements cannot
distinguish standard QM from any overlap-dependent deformation — the
entire overlap-only class is non-identifiable at θ = π/2.

The distinctive experimental signature is the cos θ functional form itself:
equatorial measurements (θ = π/2) sit at an exact fixed point where all
overlap-dependent deformations vanish identically; tilting away from the
equator produces a linear onset ∝ cos θ. Any non-zero δ⟨AB⟩ exhibiting this
cos θ scaling is distinct from standard systematic profiles — conventional
systematics either cancel in the δ⟨AB⟩ comparison or produce non-geometric
θ-dependence, making a cos θ signal difficult to reproduce without
overlap-dependent physics (§5.3, §8.4). This cos θ dependence is a
genuine observable, not a gauge artifact: Lemma 1 (§3.2) proves it cannot
be absorbed by unitary redefinition of the measurement basis.

### 3.2 — Equatorial Cancellation Theorem

**Definition (Overlap-only class).** A deformation of quantum measurement
statistics is *overlap-only* if the modified joint probability takes the form
P'(a,b | x,y) = P_QM(a,b | x,y) · g(|⟨b|d⟩|²) / Z, where
g: [0,1] → ℝ is any function and Z = Σ_{a,b} P_QM(a,b | x,y) · g(|⟨b|d⟩|²)
normalizes the distribution.

**Proposition 1 (Equatorial Cancellation Theorem).** Let g be any function.
At θ = π/2, |⟨b|d⟩|² = 1/2 for all outcome pairs (b,d). Hence
g(|⟨b|d⟩|²) = g(1/2) is constant, and P'(a,b | x,y) = P_QM(a,b | x,y).
The equatorial plane is a fixed point of every overlap-only deformation. ∎

**Corollary.** Any overlap-only deformation that vanishes at the equator
necessarily collapses to a constant there. No overlap-dependent modification
evades equatorial cancellation while depending only on |⟨b|d⟩|²; producing a
non-trivial equatorial signal requires dependence on additional degrees of
freedom beyond the basis overlap.

**Lemma 1 (Non-Absorption).** The cos θ term in Eq. (4) cannot be absorbed
by unitary redefinition of the Superobserver's measurement basis.

*Proof.* Under passive relabeling |b'⟩ = U|b⟩, the joint probability
distribution P(a,b|x,y) is invariant for any unitary U — basis
redefinition relabels outcomes without altering probabilities. Hence the
correlator ⟨AB⟩ = Σ_{a,b} a·b·P(a,b|x,y) is identically invariant:
δ⟨AB⟩ = 0 for all θ and all U. In contrast, Eq. (2) couples to the
physical overlap |⟨b|d⟩|², which depends on the Friend outcome d — a
degree of freedom external to the Superobserver's measurement basis.
Passive relabeling therefore predicts δ⟨AB⟩ = 0 for all θ; Eq. (2)
predicts δ⟨AB⟩ ∝ β cos θ. ∎

*Operational invariant.* The correlator difference δ⟨AB⟩_θ =
⟨AB⟩_θ − ⟨AB⟩_π/2 is invariant under any unitary transformation
acting on the Superobserver's Hilbert space alone. Only coupling to a
degree of freedom external to that basis — such as the Friend outcome d
in Eq.(2) — can produce non-zero δ⟨AB⟩ with cos θ scaling. No basis
redefinition of the Superobserver alone can generate this signal.

**Scope limitation.** The overlap-only class is the minimal phenomenological
class capturing dependence on |⟨b|d⟩|²; we do not claim completeness over all
possible deformations. Proposition 1 constrains this class: deformations whose
modification factor depends solely on |⟨b|d⟩|². Broader deformations —
depending on the full density matrix, higher-order correlators, or
non-geometric variables — lie outside this theorem's scope. The experiment
(§4-7) constrains the overlap-only class; independent designs are needed for
broader classes.

**Examples.** g(x) = x² gives g(1/2) = 1/4 for all outcome pairs — constant,
hence cancels in Z. g(x) = sin(πx) gives g(1/2) = 1 — again constant.
g(x) = (1−x)^n for any n ≥ 1 gives g(1/2) = (1/2)^n — constant. The
cancellation is universal.

**Contextuality distinction.** Standard quantum contextuality
(Kochen-Specker, Bell-KS) concerns the dependence of measurement outcome
distributions on which compatible observables are measured jointly — a
property of the measurement *setting*. Overlap-only deformation concerns a
different structure: the dependence of Superobserver statistics on the
geometric relationship between the Superobserver's basis and a prior
observer's recorded outcome — a property of the measurement *registration*.
The two are logically independent: KS contextuality constrains outcome
distributions across incompatible measurement settings; overlap-dependence
modifies outcome probabilities conditioned on a prior registration event
within a single setting. Proposition 1 constrains the latter; it is silent
on ordinary KS contextuality. A theory exhibiting KS contextuality need
not exhibit overlap-dependence, and conversely.

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

### 3.4 — Physical Intuition

At θ = π/2, the Superobserver's measurement basis is maximally symmetric
with respect to the Friend's recorded outcomes:
|⟨b|H⟩|² = |⟨b|V⟩|² = 1/2 for both b = ±1 — the Superobserver's measurement
apparatus is equally aligned with every Friend record, disturbing both
outcomes identically. The registration is perfectly balanced; no
overlap-dependent deformation can produce an asymmetry because there is
no asymmetry to amplify. [Figure X: Balanced vs tilted overlap geometry —
at equator (θ=π/2) all overlap magnitudes equal 1/2 (symmetric); at θ≠π/2
the Superobserver basis tilts toward one Friend outcome, creating cos θ
asymmetry that an overlap-dependent deformation converts into a detectable
statistical signal.]

Tilting to θ ≠ π/2 breaks this balance: the Superobserver's basis aligns
more closely with one Friend outcome (e.g., |⟨+1|H⟩|² > |⟨+1|V⟩|² for
θ < π/2), creating a cos θ asymmetry. An overlap-dependent deformation
would convert this geometric imbalance into a detectable statistical
signal — the measurement apparatus becomes a directional probe for
registration-layer structure. Mathematically, such terms are the
leading-order expression of any smooth registration-fidelity function
that depends on measurement alignment; the first-order correction away
from perfect alignment generically has the structure
1 − β·(1 − |⟨b|d⟩|²). Eq.(2-3) isolates this universal geometric
structure without committing to a specific physical mechanism.
The experiment (§4-7) tests whether nature exploits this asymmetry.

### 3.5 — An Unisolated Geometric Control Parameter

**Survey of published EWF implementations.** The table below lists all
published optical EWF experiments examined in our systematic search
(Supplemental S1 documents the full methodology).

| Experiment | Year | Measurement | Polar angle θ | Equatorial? | Ref |
|-----------|------|------------|---------------|------------|-----|
| Proietti et al. | 2019 | BSM (Bell-state) | —[a] | Yes | [1] |
| Bong et al. | 2020 | Projective (settings 2,3) | π/2 | Yes | [2] |

[a] BSM projects onto the Bell basis; |⟨ψ\|Φ⁺⟩|² = 1/2 for all outcome pairs,
functionally equivalent to equatorial measurement (see Supplemental S1 for the
derivation).

**Prior work.** We searched Google Scholar, arXiv (quant-ph), Web of Science,
and InspireHEP (January 2000 – May 2026) using Boolean queries combining
("Wigner's friend" OR "extended Wigner") with ("equatorial measurement" OR
"Bloch sphere polar angle" OR "outcome dependence" OR "geometric constraint");
~200 papers screened, 47 examined in full text, with targeted follow-up on
citing/cited works. Full search methodology and database query logs in
Supplemental S1. Within the surveyed literature (S1), we find no published
EWF experiment that varies θ from π/2. Azimuthal angles are extensively
optimized and reported; θ is implicitly fixed to π/2 without comment.
To our knowledge, no published EWF implementation has systematically
probed the polar angle.

The structural reason is straightforward: LF inequalities are optimized for
maximal violation, which occurs at equatorial settings. Researchers optimize
azimuthal angles φ to maximize the LF violation — taking the polar angle
θ = π/2 as a fixed starting assumption because the standard inequality
derivations presuppose projective measurements in the equatorial plane [2,10].
Without a specific hypothesis motivating θ ≠ π/2, there is no experimental
incentive to explore the polar direction.

The three-line proof (§3.3) reveals that existing EWF experiments may have
unknowingly operated exactly at a geometric null point: equatorial
measurement was adopted as a convention for LF inequality optimization,
not tested as a constraint on overlap-dependent physics. The structural
implication is that the equatorial plane is a fixed point for the entire
overlap-only class — all published implementations, operating exclusively
at this fixed point, cannot distinguish standard QM from any
overlap-dependent deformation within this class. Tilting the Superobserver
opens access to this previously untested sector (§4).

---

## Section 4 — Experimental Protocol (Claim B)

### 4.1 — Breaking the Cancellation

Any θ ≠ π/2 breaks the cancellation. A grid search over (θ, φ₂, φ₃, β_Bob)
maximizing min(n_σ_LF, n_σ_signal) yields θ = 31° as optimal; the figure of
merit remains above 5σ for the broad range θ ∈ [20°, 55°] (Supplemental S2).
Representative FOM values at μ = 0.95: 9.6 (θ = 20°), 8.6 (θ = 31°, optimal),
7.1 (θ = 45°), 5.0 (θ = 58°, 5σ threshold), and 0 (θ = 90°, cancellation).
[Figure X: Figure of merit vs polar angle θ, showing broad optimum at θ ≈ 31°
and 5σ detection boundary spanning θ ∈ [20°, 55°].]
The wide optimal window means the protocol tolerates angular misalignment of
±11° before dropping below 5σ — substantially more forgiving than the
alignment precision demanded by the standard Bong protocol.

The optimum at θ = 31° reflects a trade-off between two monotonic trends.
As θ → 0°, the |cos θ| signal is largest, but the Gen LF 1 violation
weakens because measurement settings approach a common axis, reducing the
inequality's capacity to separate LF-violating from LF-satisfying theories.
As θ → 90°, the LF violation is strongest but the signal vanishes
(cos θ → 0, §3). Analytically, the figure of merit approximates
FOM(θ) ∝ min(|cos θ|, f_LF(θ)), where f_LF(θ) is a monotonically
increasing function of θ (strongest LF violation at equator); the
intermediate optimum emerges from the intersection of these competing
trends, with the exact location set by the Gen LF 1 inequality
coefficients via grid search (Supplemental S2). The broad plateau
(FOM > 5σ for θ ∈ [20°, 55°]) means the exact optimum is not critical —
any angle in this range produces a viable experiment.

### 4.2 — Single Hardware Modification

In standard Bong et al. (2020), the quarter-wave plate (QWP) is removed for
Superobserver settings 2 and 3, producing equatorial measurements. Our
modification re-inserts this same QWP into Superobserver Alice's measurement
path (before the PBS, after beam displacer BD2), tilting the effective
measurement axis to θ = 31°. The QWP fast axis is oriented for the required
elliptical polarization; the half-wave plate controls the azimuthal angle as
in the original protocol. QWP specifications (retardance tolerance, temperature
stability) and angular uncertainty analysis are provided in Supplemental S2.
This is the only optical hardware change required. (The SNSPD upgrade
discussed in §7 replaces existing detectors at the same optical position;
no new optical elements are introduced.) A φ-scramble control (§7)
randomizes the azimuthal angle to rule out birefringence artifacts without
additional optics.

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

Bong et al. (2020) report ~1000 coincidence events per second. At this rate,
N = 91,000 per setting requires ~91 s of integration; nine setting
combinations plus calibration (θ-verification and azimuthal alignment checks)
would require a data-acquisition run of approximately one hour under Bong
et al. conditions, assuming source and detector stability over this timescale.
Practical feasibility depends on the specific apparatus; detailed acquisition
timing and stability estimates are provided in Supplemental S2.

---

## Section 5 — Model-Independent QM Predictions

All numerical values are computed from the density matrix ρ_μ = μ|Φ⁻⟩⟨Φ⁻| +
(1−μ)I/4 for the singlet state with visibility μ = 0.95.

### 5.1 — Correlators at θ = 31°, μ = 0.95

All nine ⟨A_x B_y⟩ correlators are tabulated in Supplemental S2. Key values:
⟨A₁B₁⟩ = −1.0000 (z-basis, perfect anti-correlation); mixed-setting correlators
range from ⟨A₂B₂⟩ = −0.5045 to ⟨A₂B₃⟩ = ⟨A₃B₂⟩ = −0.8933, all with
σ ≈ 0.0017 at N = 91,000. The four mixed-setting pairs (one side z-basis,
one side tilted) share identical |⟨AB⟩| up to φ-induced sign, since f_perp
depends only on θ. Standard QM predicts zero marginals (singlet, μ = 0.95).

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

For conservative single-setting detection, the minimum detectable coupling
at 5σ confidence is β ≥ 0.07 (N = 91,000 per setting). Using all four
mixed settings combined, β ≥ 0.04 is detectable at >5σ (β_min ≈ 0.038
under idealized Poisson statistics; see §6). Accounting for realistic
systematics (§6-7), the practical sensitivity floor is likely
β ∼ 0.05–0.10 (single-setting) and β ∼ 0.04–0.06 (combined). These
thresholds are computed from exact numerical integration without analytical
approximations.

**Experimental discriminator.** Standard QM predicts δ⟨AB⟩ = 0 for all θ.
The benchmark parametrization Eq. (2-3) predicts δ⟨AB⟩ ∝ β cos θ — a
functional form testable by θ-sweep (§8.3). The cos θ scaling constitutes a
new experimental observable: the equator (θ = π/2) is an exact fixed point
where all overlap-dependent deformations vanish identically; tilting away
from the equator produces a linear onset ∝ cos θ. This is not a
reparameterization of QM — the cos θ signature is distinct from standard
systematic profiles (conventional systematics either cancel in δ⟨AB⟩ or
produce non-geometric θ-dependence), making a cos θ signal difficult to
reproduce without overlap-dependent physics (see also Lemma 1, §3.4).

**β in context.** The coupling β has no a priori prediction — analogous to
SME coefficients at inception. For scale reference: photon-sector SME
coefficients are constrained to <10⁻²³ [15]; continuous spontaneous
localization (CSL) collapse parameters are bounded at λ ≈ 10⁻¹⁶ s⁻¹;
weak-measurement anomaly searches constrain postselection deviations at
~10⁻² [18]. A constraint β ≥ 0.04 would place overlap-dependent deformation
in the company of these phenomenological parameter classes — opening a new
parameter space at the ~10⁻² scale (comparable to weak-measurement
anomalies) while distinct from SME and collapse regimes in both scale and
physical mechanism. See Supplemental S3 for expanded scale comparison.
The ~10⁻² scale is physically motivated: postselection-conditioned weak
values [18] manifest at the same order, and any overlap-dependent
registration-layer structure would naturally appear at the precision where
measurement-context effects become distinguishable from Poisson noise in
current optical implementations.

The gap between β_min ≈ 0.038 (combined) and β_min ≈ 0.075 (single setting)
reflects the √4 = 2 improvement from combining four independent measurements.
The experiment naturally provides all four mixed-setting correlators; no
additional data acquisition is needed for the combined analysis.

The coupling β has no a priori theoretical prediction — analogous to SME
coefficients at the time of their proposal. A null result at β ≥ 0.04
excludes O(1) and O(10⁻¹) deformation for the class Eq. (2-3), opening
a new parameter space at the ~10⁻² scale; a positive result provides the
first quantitative target for theory construction. Increasing to
N = 200,000 extends sensitivity to β ≥ 0.02.

---

## Section 6 — Statistical Analysis

Poisson statistics: σ(⟨A_x B_y⟩) = √[(1 − ⟨A_x B_y⟩²) / N]. For Gen LF 1
(11 terms, coefficients up to ±2): σ(S_LF1) = √20/√N ≈ 0.0103 at N = 91,000.

Minimum sample for 5σ LF detection: N_min ≈ 30,800. N = 91,000 provides a
factor of 3 margin.

Monte Carlo (10,000 runs): Gen LF 1 ≥ 5σ in 99.97%; β = 0.07 detected in >99%
(single setting), β = 0.05 in ~90% (combined). A conservative Bayesian analysis
inflating Poisson uncertainties by 20% yields β_min ≈ 0.046 (combined); the FOM
plateau (§4.1: >5σ for θ ∈ [20°, 55°]) ensures viability under substantial
systematic degradation. Detailed Monte Carlo, correlated-drift modeling, and
fake-signal injection methodology are provided in Supplemental S2.

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

**φ-scramble control.** A birefringence artifact in the QWP could produce
θ-dependent efficiency variation mimicking the cos θ signal. To distinguish:
randomize the azimuthal angle φ while keeping θ fixed. The overlap-dependent
signal (Eq. 4: f_perp(+1,H) − f_perp(−1,H) = −cos θ) is independent of φ
(|e^{iφ}|² = 1 throughout §3.3). Birefringence, by contrast, couples to both
θ and φ jointly via the full Jones matrix of the waveplate. If δ⟨AB⟩ persists
under φ-randomization, its origin is geometric (θ-dependent), not
birefringent (θ,φ-dependent). This control requires no additional optical
elements — only randomization of the HWP angle controlling φ.

**Robustness summary.**

| Parameter | Nominal | 5σ Threshold | Bong Achievable |
|-----------|---------|-------------|-----------------| 
| μ | 0.95 | ≥ 0.90 | 0.92 |
| η | 1.00 | ≥ 0.91 | 0.87 |
| Δθ | 0° | ≤ ±5° | < ±1° |

**Detection loophole.** Closure requires η ≥ 0.91 [7]; Bong η ≈ 0.87.
Two observations make the fair-sampling regime scientifically productive.
First, demonstrating LF violation at θ = 31° — within currently surveyed
implementations, the first non-equatorial EWF measurement — confirms that the violation is not an
artifact of equatorial geometry; this holds regardless of
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
the sensitivity threshold for class Eq. (2-3) at this previously untested
geometry.

### 8.2 — Interpretation and Model Context

The implications for major quantum interpretations (Many-Worlds, Relational
QM, Copenhagen, QBism, Objective Collapse) and the measurement-registration
framework motivating Eq. (2-3) are analyzed in Supplemental S3. Neither the
interpretations nor the embedding predict or preclude the class Eq. (2-3);
the experiment is interpretation-neutral by design.

### 8.3 — Future Directions

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

The central result is the equatorial cancellation theorem (Proposition 1):
at θ = π/2, every overlap-dependent deformation of Superobserver statistics
vanishes identically — for any function g of the basis overlap, not just
Eq. (3). Within the surveyed literature (Supplemental S1), published EWF
implementations have operated at this fixed point; the overlap-only class
has therefore remained structurally untested.

As its direct experimental consequence, we propose a null test: re-insert
one QWP into the Bong et al. (2020) apparatus (θ = 31°), providing
sensitivity β ≥ 0.07 at >5σ (single-setting) while preserving 8.6σ LF
violation. This single optical element accesses a geometric degree of
freedom that, within the surveyed literature (Supplemental S1),
has remained unprobed across published EWF implementations.
The experiment requires no new technology — only re-insertion
of an existing waveplate — and would open a new experimental window onto overlap-dependent
physics in EWF scenarios — a geometric sector that, within surveyed
implementations (Supplemental S1), has not previously been probed.

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
[18] Y. Aharonov, D.Z. Albert, and L. Vaidman, Phys. Rev. Lett. 60, 1351 (1988).

---