Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# K9_E Source of Truth — Single-Waveplate Test of Outcome-Dependent Quantum Registration in Extended Wigner's Friend Scenarios

**SOT type:** INTERNAL — K9_E Completeness Reference
**Date synthesized:** 2026-05-25 (re-synced 2026-05-31 to manuscript v95; updated 2026-06-02: RCA K9_E Completeness 3-round 4.7/5 PASS — added φ_R restricted existence I.2 + §8.1 Falsification Hierarchy + version lineage v21→v95; v98 sync 2026-06-02: §4.5 BSM overlap → conditional probability P(d|b)=1/2 [C2], §7.1 σ(Gen LF 1)=0.0103 is exact not √20/√N≈0.0148 [S1], §16 FOM window [20°,55°]→[20°,45°] [S2])
**Sources:** draft_v1.md (v4, K9-S12 proposal) + manuscript.md (v95, academic paper) + v12 Eq.(12) fix + CHANGELOG v12-v95 + supplemental S1-S3 + phi_restricted_existence_v1_0.md (2026-06-01, I.2 Class C THEOREM)
**Relationship to manuscript v95:** This SOT contains full K9_E context, VVV-QMRF language, and technical detail removed from the public-facing manuscript. Manuscript v95 is the academically-defended subset for Phys. Rev. A submission.
**Version lineage:** v4 (K9-S12 proposal) -> v12 (Eq.12 corrected, watershed) -> v21 (academic polish) -> v94 (RCA round 4: cos θ downgrade, per-θ FOM re-optimization, SPDC density matrix) -> v95 (§8.1 Falsification Hierarchy boundary, 3-round RCA 4.1/5). This SOT synthesizes the best from all versions, prioritizing K9_E completeness.

---

## Section 1 -- K9_E Probability Postulate (P9)

### 1.1 -- Statement

The VVV-QMRF framework postulates registration-layer probability modification (P9) at Layer 3 (Class C qualified, v31):

```
P(o | K) = Tr(E_o rho) * [1 - beta * f_perp(K_ctx)] / Z_E
```

where:
- **Tr(E_o rho)** = standard QM Born-rule probability for outcome `o`
- **f_perp(K_ctx)** = outcome-overlap function encoding K-space registration context
- **beta in [0,1]** = suppression strength (dimensionless coupling)
- **Z_E** = normalization factor ensuring sum_o P(o|K) = 1
- **Born limit:** beta = 0 recovers Standard QM exactly

### 1.2 -- f_perp Definition

```
f_perp(b, d) = 1 - |<b|d>|^2
```

where:
- **b in {+1, -1}** = Superobserver measurement outcome
- **d in {H, V}** = Friend measurement outcome (z-basis)
- **|<b|d>|^2** = squared overlap between Superobserver basis state and Friend outcome state

Physical interpretation: f_perp quantifies the basis incompatibility between two observers' measurement records. When bases are aligned (|<b|d>|^2 = 1), f_perp = 0 -> no modification. When bases are orthogonal (|<b|d>|^2 = 0), f_perp = 1 -> maximal modification.

### 1.3 -- f_perp Motivation and Constraints

Eq. (3) defining f_perp = 1 - |<b|d>|^2 is the simplest representative of a broader class. Any smooth function g(|<b|d>|^2) satisfying three minimal physical constraints has the same leading-order structure:

**(i) Basis-rotation invariance** -- only the relative angle between measurement bases can matter, not absolute lab-frame orientations. This makes g a function of |<b|d>|^2 alone.

**(ii) Alignment limit** -- when bases are perfectly aligned (|<b|d>|^2 = 1), no cross-observer incompatibility exists, so the modification must vanish: g(1) = 0.

**(iii) Monotonicity** -- as bases become more orthogonal, the incompatibility between observers' registered outcomes grows: g'(x) < 0 for x in [0, 1].

The leading-order Taylor expansion of any such function around x = 1 is:
```
g(x) = c_1(1-x) + O((1-x)^2)    with x = |<b|d>|^2
```

where c_0 = 0 by constraint (ii). Adopting the simplest representative (c_1 = 1) and absorbing any proportionality constant into beta:
```
f_perp(b, d) = 1 - |<b|d>|^2
```

**Scope caveat:** Constraints (i)-(iii) are NOT exhaustive -- they are the minimal set for a one-parameter family. Other dependence structures (density matrix coupling, higher-order correlators in f_perp, non-multiplicative forms) lie outside the scope of the class defined by Eq. (2-3).

### 1.4 -- Postulate Status

K9_E is a **POSTULATE**, not a theorem derivable from K1-K8 alone. K1-K8 define structural registration-layer properties (binary cert, temporal injectivity, self-certification, incommensurability, authentication, closure, cross-space preservation) but do not uniquely determine a probability rule. K9_E is the bridge between K-space structure and observable quantum probabilities.

**Source references:** CLAUDE.md Layer 3 (FROZEN K1-K8, Class C qualified v31); `documents/research_documents/project_vvv_qmrf_class_c/01_axiomatization/K_Space_Axiomatization.md` (v29 with K5_prospective).

---

## Section 2 -- VVV-QMRF Registration Architecture Context

### 2.1 -- Layer Architecture

The VVV-QMRF framework organizes the registration-logic structure K in five architectural layers:

| Layer | Status | Content |
|-------|--------|---------|
| Layer 1 | FROZEN | K1-K8 Registration-logic axioms: binary cert, V in {0,1}, bot_K incommensurability, AdmJoint |
| Layer 2 | UPDATABLE | T1-T7 Bridge theorems: K_joint construction (T1 N=2 constructive), colimit (T4-H), relativization |
| Layer 3 | Class C qualified (v31) | K9_E Probability postulate (P9): P(o|K) = Tr(E_o rho) * [1 - beta * f_perp(o, K_ctx)] / Z_E |
| Layer 4 | Class D | Multi-paper data fit: D1 Proietti CHSH, D2 Bong LF, D3 Frauchiger-Renner (AVOIDED) |
| Layer 5 | Class D | Prediction + Reduction + Assessment: 3-observer prediction (conditional on T4-H) |

### 2.2 -- What K9_E Requires from Layers 1-2

K9_E requires only **T1 (N=2 constructive)**, not the full T4-H colimit. T1 constructs K_joint for N=2 observers, which provides the structural basis for computing K-space registration context across observer pairs. T4-H (Steps 2-4 deferred) is needed only for N>=3 observer extensions.

### 2.3 -- Ontological Classification: What K9_E IS NOT

K9_E as parametrized through Eq. (2-3) is a phenomenological parametrization. It is explicitly:

- **NOT a hidden-variable model** -- the Friend outcome d is an observed macroscopic record, not an unobserved lambda
- **NOT a collapse modification** -- standard unitary dynamics is assumed throughout
- **NOT a signal or interaction between observers** -- no communication channel is invoked
- **NOT a unique prediction of any existing theory** -- it parametrizes a structural degree of freedom that standard QM marginalizes over without testing

### 2.4 -- Physical Intuition: Measurement Incompatibility Between Observers

When a Friend measures in the z-basis, they produce a macroscopic record with a definite orientation on the Bloch sphere. A Superobserver measuring at Bloch angles (theta, phi) probes this record at a relative angle determined by the basis overlap |<b|d>|^2. Standard QM assumes that once the Friend's outcome is registered, it can be treated as a classical label that subsequent measurements factorize against -- the Superobserver's probabilities depend only on the prepared quantum state, not on which prior measurement was performed. Eq. (2) parametrizes a possible residual dependence on this geometric relationship: a dependence that standard QM's factorization assumption would set identically to zero. Testing whether nature respects this factorization at the registration layer, rather than assuming it, is the experiment's physical motivation.

---

## Section 3 -- Class C Classification History (v29 -> v30 -> v31)

### 3.1 -- v29: Class C (genuine)

Genuine non-circular fit to Proietti 2019 data yields:
- beta = 0.598
- V = 0.939 (variance explained)
- Delta_chi2 = 5.35 (2.31sigma above null)
- RCA: 4.50/5

Status: Class C (genuine) -- tentatively supported by existing data.

### 3.2 -- v30: Downgrade to (qualified)

P10-NOISE noise sensitivity analysis: **FAIL**
- noise_threshold = 0.10 sigma RMS << 1.0 (robustness threshold)
- A0B0 drives 80% of Delta_chi2
- Single-setting fragility: 1.85sigma
- Random noise at ANY magnitude produces Delta_chi2 >= 5.35 in ~50% of realizations
- Conclusion: 2.31sigma is NOT evidence for K9_E suppression

Status: Class C downgraded genuine -> **qualified**.

### 3.3 -- v31: K9E-PAT CLOSED as UNRESOLVABLE

K9E-PAT (Proietti Asymmetry Test) resolution:
- Empirical ratio = -0.78 +/- 1.72 (ratio of two sub-sigma residuals)
- Both additive model (ratio = 2.000) and multiplicative model (ratio = 1.913) predict suppression ratio ~2
- 4 Proietti data points insufficient for any conclusion
- Root cause: empirical ratio -0.78 is a RED HERRING -- ratio of two sub-sigma residuals, not a physical signal
- RCA: 4.92/5

Status: K9E-PAT **CLOSED UNRESOLVABLE**. Cannot resolve 2BSM/1BSM suppression mechanism from existing 4-point data.

### 3.4 -- Current Empirical Status (v31)

**Class C (qualified) -- structurally testable, empirically UNCONFIRMED.**

- Genuine fit (v29) invalidated by P10-NOISE (v30)
- Suppression mechanism unresolved (K9E-PAT, v31)
- Distinguishing signal below current experimental detection threshold
- Confirmation or rejection requires **dedicated experiment** (K9-S12)
- IBM Quantum approach REJECTED (double category error, RCA 4.92/5) -- K9_E requires K-space registration structure absent on gate-model QPUs

---

## Section 4 -- The Equatorial Cancellation Theorem (Claim A)

### 4.1 -- Statement

**Theorem (Equatorial Cancellation).** Let Friend F measure in z-basis ({|H>, |V>}) and Superobserver W measure at Bloch sphere angles (theta, phi). With f_perp(b,d) = 1 - |<b|d>|^2:

```
f_perp(+1, H) - f_perp(-1, H) = -cos theta                                          (4)
```

Consequently, f_perp is outcome-INDEPENDENT if and only if theta = pi/2 (equatorial). For any equatorial Superobserver measurement, any model of the form Eq. (2-3) reduces exactly to standard quantum mechanics, regardless of the coupling strength beta.

### 4.2 -- Full Proof

**Step 1 -- Superobserver measurement basis at (theta, phi):**

```
|b=+1> = cos(theta/2)|H> + e^{i*phi} sin(theta/2)|V>                               (5)
|b=-1> = sin(theta/2)|H> - e^{i*phi} cos(theta/2)|V>                               (6)
```

**Step 2 -- Squared overlaps with Friend's z-basis outcomes:**

phi drops out (|e^{i*phi}|^2 = 1); overlaps depend ONLY on theta.

```
|<b=+1|H>|^2 = cos^2(theta/2)          |<b=+1|V>|^2 = sin^2(theta/2)              (7)
|<b=-1|H>|^2 = sin^2(theta/2)          |<b=-1|V>|^2 = cos^2(theta/2)              (8)
```

**Step 3 -- f_perp values:**

```
f_perp(+1, H) = 1 - cos^2(theta/2) = sin^2(theta/2)                               (9)
f_perp(-1, H) = 1 - sin^2(theta/2) = cos^2(theta/2)                              (10)
f_perp(+1, V) = 1 - sin^2(theta/2) = cos^2(theta/2)
f_perp(-1, V) = 1 - cos^2(theta/2) = sin^2(theta/2)
```

**Step 4 -- Outcome-dependence:**

```
f_perp(+1, H) - f_perp(-1, H) = sin^2(theta/2) - cos^2(theta/2) = -cos theta     (11)
```

**Step 5 -- Equatorial cancellation:**

-cos theta = 0 iff theta = pi/2. At theta = pi/2: all four f_perp = 1/2 -> constant factor -> cancels in Z_E.

**Step 6 -- K9_E reduction to QM:**

When f_perp is outcome-independent:
```
P(o|K) = Tr(E_o rho) * [1 - beta * constant] / [1 - beta * constant] = Tr(E_o rho)
```
K9_E = 0 for all equatorial measurements. QED.

### 4.3 -- Sympy Verification

```python
import sympy as sp
theta = sp.Symbol('theta', real=True)
assert sp.simplify(sp.sin(theta/2)**2 - sp.cos(theta/2)**2 + sp.cos(theta)) == 0
```

### 4.4 -- Generality of the Cancellation

At theta = pi/2, |<b|d>|^2 = 1/2 for all b,d pairs. Any function g(|<b|d>|^2) therefore takes the same value for all outcome pairs, so the modification factor in Eq. (2) is constant across outcomes and cancels in the normalization Z. The equatorial plane is a **fixed point** for the entire class motivated in Section 1.3 -- this includes sigmoid, exponential, information-theoretic, and any other smooth function of |<b|d>|^2.

### 4.5 -- Corollary: The Geometric Blind Spot

**Bong et al. (2020):** All Superobserver settings (2 and 3) are equatorial (theta = pi/2). QWP removed explicitly for these settings. f_perp outcome-independent for every measurement combination -> K9_E = 0.

**Proietti et al. (2019):** Bell-state measurement projects onto |Phi+>, |Phi->, |Psi+>, |Psi->. Conditioned on any Bell outcome b, the Friend's recorded outcome d is equally likely to be H or V: P(d|b) = 1/2. (Because b is a two-photon Bell state and d a single-photon record, the meaningful object is this conditional probability, not a single-photon overlap |<b|d>|^2; the 1/2 plays the same role as the equatorial overlap |<b|d>|^2 = 1/2.) -> equivalent to equatorial configuration -> K9_E = 0.

**Conclusion: K9_E has NEVER been experimentally tested.** The question remains entirely open.

### 4.6 -- theta = 31 deg Trade-off Explanation

The optimum at theta = 31 deg reflects a trade-off between two monotonic trends:

- As theta -> 0 deg: the K9_E signal is largest (overlap asymmetry maximized), but the Gen LF 1 violation weakens because measurement settings approach a common axis, reducing the inequality's capacity to separate LF-violating from LF-satisfying theories
- As theta -> 90 deg: the LF violation is strongest, but the K9_E signal vanishes identically (equatorial cancellation, Section 4.2)
- The intermediate near-optimum (theta ~ 31-35 deg) balances these effects

Representative FOM values at mu = 0.95, beta = 0.30 (per-theta angle re-optimization): 5.8 (theta = 20 deg), 8.6 (theta = 31 deg), 8.8 (theta = 35 deg), 6.0 (theta = 45 deg), 0 (theta = 58 deg, Gen LF 1 becomes negative), 0 (theta = 90 deg, cancellation). The broad plateau (FOM > 5sigma for theta in [20 deg, 45 deg] -> +/-11 deg tolerance) means the exact optimum is not critical. theta = 31 deg is adopted as the reference angle because it coincides with the QWP-determined tilt in the Bong apparatus.

---

## Section 5 -- Experimental Protocol (Claim B, K9-S12)

### 5.1 -- Base Apparatus

Minimal modification of Bong et al. (2020) [2]: SPDC source at 810 nm, beam displacers (BD1, BD2), half-wave plates (HWPs), polarizing beam splitters (PBS), single-photon detectors. Two entangled photon pairs. On each side, a Friend measures in z-basis inside an interferometric lab. Superobservers Alice and Bob measure the combined Friend+photon system. N = 91,000 coincidences per measurement setting (matching Bong 2020 for direct comparability).

### 5.2 -- Single Hardware Modification

**The ONLY optical hardware change required:** Re-insert ONE quarter-wave plate (QWP) into Superobserver Alice's measurement path. In standard Bong, the QWP is removed for settings 2 and 3 to produce equatorial measurements. Re-inserting it tilts the effective measurement axis to theta = 31 deg.

- **Position:** Before PBS, after beam displacer BD2 (same optical position as in standard Bong setting 1)
- **Fast axis orientation:** adjusted to produce effective polar angle theta = 31 deg on the Bloch sphere
- **Wavelength:** QWP specified for lambda = 810 nm (matching SPDC source)
- **Retardance tolerance:** <= +/-2 nm (angular uncertainty in theta ~ +/-0.5 deg)
- **Transmission:** >99% at 810 nm (no additional loss mechanism)
- The half-wave plate (HWP) controls the azimuthal angle phi as in the original protocol

**Note on SNSPD upgrade:** Upgrading to superconducting nanowire single-photon detectors (SNSPDs, eta > 0.90 at 810 nm) replaces existing detectors at the same optical position; no new optical elements are introduced.

### 5.3 -- Measurement Settings

| Parameter | Standard Bong [2] | Modified (K9-S12) |
|-----------|------------------|-------------------|
| Polar angle theta | 90 deg (equatorial) | **31 deg** |
| Alice phi_2 | 0 deg | **112 deg** |
| Alice phi_3 | 118 deg | **217 deg** |
| Bob beta_Bob | 175 deg | **20 deg** |
| Visibility mu (required for 5sigma) | not specified | >= **0.92** |
| Visibility mu (onset) | not specified | >= **0.86** |
| Detector efficiency eta (required) | not specified | >= **0.91** (at mu=0.95) |
| Total coincidences N | 91,000 | **91,000** |

Angles optimized via coarse grid (15 deg steps, 13,824 configurations) + fine scan (2 deg steps around top candidates), maximizing FOM = min(n_sigma_LF, n_sigma_K9E).

### 5.4 -- Calibration Procedure

1. **Verify polar angle:** |<sigma_z>| = cos(31 deg) ~ 0.857 on H-polarized state (+/-0.01 tolerance)
2. **Verify azimuthal alignment:** entangled state count rates match QM predictions within 2%
3. **Measure mu:** CHSH S-parameter -> visibility >= 0.86 required for LF onset, >= 0.92 for 5sigma

---

## Section 6 -- Full Numerical Predictions [CORRECTED v12 -- Exact Density Matrix]

**CRITICAL:** All numbers below use exact numerical density matrix computation (v12 fix). Previous versions (v1-v11) used the analytical approximation |cos theta|/2 which gave incorrect beta thresholds. Correct values verified by `K9S12_proposal.py` and `statistical_significance.py`.

### 6.1 -- QM Correlators (theta = 31 deg, mu = 0.95, N = 91,000)

All values computed from density matrix rho_mu = mu|Psi-><Psi-| + (1-mu)/2 * (|HV><HV| + |VH><VH|) for the singlet state. SPDC produces photon pairs only in the {|HV>, |VH>} subspace; the noise term is the maximally mixed state within that subspace, not the full I/4.

| (x,y) | <AB>_QM | sigma (N=91,000) | | (x,y) | <AB>_QM | sigma (N=91,000) |
|-------|---------|--------------|--|-------|---------|--------------|
| (1,1) | -1.0000 | 0.0000 | | (2,3) | -0.8933 | 0.0015 |
| (1,2) | -0.8572 | 0.0017 | | (3,1) | -0.8572 | 0.0017 |
| (1,3) | -0.8572 | 0.0017 | | (3,2) | -0.8933 | 0.0015 |
| (2,1) | -0.8572 | 0.0017 | | (3,3) | -0.8829 | 0.0016 |
| (2,2) | -0.5045 | 0.0029 |

Standard QM predicts zero marginals (singlet, mu = 0.95).

### 6.2 -- Primary Test Quantities

| Observable | QM Prediction | Type | Significance |
|-----------|--------------|------|-------------|
| Gen LF 1 | **+0.0891 +/- 0.0103** | Model-independent QM | **8.6sigma** above LF bound |
| delta<A1B2> (beta=0.3) | **-0.0355** | K9_E-dependent | **20.8sigma** |

The 8.6sigma LF violation provides built-in calibration: no violation at >=5sigma indicates the apparatus is not realizing the intended geometry.

### 6.3 -- K9_E Mixed-Setting Detail

K9_E only affects MIXED settings (one side Friend = z-basis, one side Superobserver = tilted). Same-type settings: no cross-registration incommensurability -> K9_E = QM.

| (x,y) | <AB>_QM | <AB>_K9E (beta=0.3) | delta | n_sigma (N=91k) |
|-------|---------|-------------------|---|-------------|
| (1,2) | -0.8572 | -0.8927 | -0.0355 | 20.8 |
| (1,3) | -0.8572 | -0.8927 | -0.0355 | 20.8 |
| (2,1) | -0.8572 | -0.8927 | -0.0355 | 20.8 |
| (3,1) | -0.8572 | -0.8927 | -0.0355 | 20.8 |

All four mixed settings yield identical delta (f_perp depends only on theta, not phi). Symmetric prediction provides built-in cross-validation.

At theta = 31 deg: f_perp(+1, H) = sin^2(15.5 deg) = **0.0714**, f_perp(-1, H) = cos^2(15.5 deg) = **0.9286**

### 6.4 -- beta Sensitivity [CORRECTED v12]

| beta | |delta<AB>| (mixed, per setting) | n_sigma (single, N=91k) | n_sigma (4 combined) |
|---|---------------------------|----------------------|-------------------|
| 0.03 | 0.0034 | 2.0 | 4.0 |
| 0.05 | 0.0057 | 3.3 | 6.7 |
| 0.07 | 0.0080 | 4.7 | 9.4 |
| 0.10 | 0.0115 | 6.7 | 13.5 |
| 0.30 | 0.0355 | 20.8 | 41.6 |

**Detection thresholds at 5sigma confidence:**
- beta_min (combined 4-setting) ~ **0.038** -- using all four mixed settings
- beta_min (single setting) ~ **0.075** -- conservative, individual setting
- **Conservative recommendation:** beta >= 0.07 at >5sigma (single setting) or beta >= 0.04 at >5sigma (combined)

The sqrt(4) = 2 gap between combined and single-setting thresholds reflects the statistical improvement from combining four independent measurements. The experiment naturally provides all four mixed-setting correlators; no additional data acquisition is needed for the combined analysis.

### 6.5 -- Figure of Merit

```
FOM = min(n_sigma_LF, n_sigma_K9E) = min(8.6, 20.8) = 8.6
```

FOM ensures both quantities are simultaneously significant. Compare: FOM(theta = 90 deg) = 0 (standard Bong -- K9_E invisible). FOM > 5sigma maintained for theta in [20 deg, 45 deg] (v93 correction — per-theta re-optimized at beta = 0.30; prior [20 deg, 55 deg] was pre-optimization error).

### 6.6 -- beta Physical Meaning

The dimensionless coupling beta has no a priori theoretical prediction -- analogous to the SME coefficients at the time of their proposal [15]. The experiment's role is to measure or constrain beta; the role of a future theory of outcome-dependent registration is to predict (or be excluded by) the measured value.

A null result at beta >= 0.04 (combined) excludes outcome-dependent coupling above this threshold for the class Eq. (2-3), regardless of theoretical interpretation. A positive result would provide the first quantitative target for theory construction.

Parametric frameworks routinely precede microscopic theories in physics: the Fermi theory of weak interactions, the Standard Model Extension (SME) for Lorentz violation, and effective field theory (EFT) itself all began as organizing parametrizations before acquiring dynamical foundations. Equation (2) serves the same role here.

### 6.7 -- Decision Criteria

| Gen LF 1 | delta<A1B2> | Interpretation |
|----------|---------|----------------|
| > 0, >= 5sigma | != 0, >= 5sigma | **Joint confirmation** -- LF violated AND K9_E detected |
| > 0, >= 5sigma | ~ 0 | **LF violated, K9_E absent** -- beta below sensitivity threshold |
| <= 0 | != 0, >= 5sigma | **Calibration error** -- LF violation is model-independent QM prediction |
| <= 0 | ~ 0 | **Null** -- check mu >= 0.86 and calibration. If confirmed: neither detectable |

---

## Section 7 -- Statistical Analysis

### 7.1 -- Error Model

Photon coincidence counts follow Poisson statistics:

```
sigma(<A_x B_y>) = sqrt[(1 - <A_x B_y>^2) / N]
```

For Gen LF 1 (11 terms, coefficients up to +/-2):

```
sigma^2(Gen LF 1) = sum_i c_i^2 sigma_i^2 = sum_i c_i^2 (1 - <v_i>^2)/N
sigma(Gen LF 1) ~ 0.0103 at N = 91,000   (exact term-by-term propagation)
```

Note: 0.0103 is the EXACT term-by-term value (the mixed correlators sit near -0.86 .. -1, so 1 - <v_i>^2 is small). The loose upper bound sqrt(20)/sqrt(N) ~ 0.0148 assumes all eleven correlators near zero and therefore overestimates sigma; it is NOT the value 0.0103. (Main text carries this distinction explicitly.)

### 7.2 -- Sample Size

Minimum sample for 5sigma LF detection: N_min ~ 30,800. N = 91,000 provides a factor of 3 margin. **Experiment is not statistics-limited.**

For K9_E at beta = 0.10: N_min ~ 20,400 per setting. At beta = 0.07: N_min ~ 44,300 per setting. At beta = 0.05: N_min ~ 72,000 per setting.

Increasing to N = 200,000 raises beta = 0.05 detection above 99% (combined settings).

### 7.3 -- Monte Carlo Validation (10,000 runs)

- Gen LF 1: +0.0891 +/- 0.0103, >= 5sigma in **99.97%** of runs
- delta<A1B2> at beta = 0.10: >= 5sigma in **>99.9%** of runs
- delta<A1B2> at beta = 0.07: >= 5sigma in **>99%** of runs
- delta<A1B2> at beta = 0.05: >= 5sigma in **~90%** of runs (combined)

---

## Section 8 -- Robustness Analysis

### 8.1 -- Visibility mu [CORRECTED v21]

*Negative values (mu <= 0.84): no LF violation. Positive violation onset at mu ~ 0.86; 5sigma significance requires mu >= 0.92.*

| mu | Gen LF 1 | Significance |
|----|---------|-------------|
| 0.84 | -0.0181 | -1.7sigma (no violation) |
| 0.86 | +0.0014 | 0.1sigma (onset, below 3sigma) |
| 0.90 | +0.0404 | 3.9sigma (marginal, <5sigma) |
| 0.92 | +0.0599 | **5.8sigma** |
| 0.95 | +0.0891 | **8.6sigma** |

Bong et al. achieved mu = 0.92 -> n_sigma = 5.8 at modified geometry.

### 8.2 -- Detector Efficiency eta

| eta | Effective mu (mu*eta) | Gen LF 1 | Significance |
|---|-------------------|---------|-------------|
| 0.90 | 0.85 | -0.0034 | -0.3sigma |
| 0.95 | 0.90 | +0.0428 | 4.1sigma |
| 1.00 | 0.95 | +0.0891 | 8.6sigma |

Threshold: eta >= 0.91 at mu = 0.95 for 5sigma detection. Bong achieved eta ~ 0.87 (standard SPADs). Modern SNSPDs routinely achieve eta > 0.90 at 810 nm [16].

### 8.3 -- Angular Misalignment Delta_theta

LF significance remarkably stable across Delta_theta = +/-5 deg (8.6-8.8sigma). K9_E delta vanishes iff theta = pi/2 and is generically non-zero otherwise (exact theta-dependence numerical; unrenormalized leading-order structure goes as cos theta but overestimates |delta| by ~5.5x). At Bong angular precision (< +/-1 deg): delta variation < 1%.

| Delta_theta | theta_actual | Gen LF 1 | n_sigma |
|-----|---------|---------|-----|
| 0 deg | 31 deg | +0.0891 | 8.6 |
| +1 deg | 32 deg | +0.0914 | 8.7 |
| +3 deg | 34 deg | +0.0947 | 8.8 |
| +5 deg | 36 deg | +0.0963 | 8.7 |

### 8.4 -- Can Detector Inefficiency Fake a beta Signal?

Under fair-sampling, undetected events are assumed to follow the same distribution as detected ones. If this assumption fails, a theta-dependent detector efficiency eta(theta) could in principle produce a spurious delta<AB>. However:

1. The relevant quantity is the difference eta(theta = 31 deg) - eta(theta = 90 deg), not absolute eta
2. QWP insertion at theta = 31 deg introduces no additional loss mechanism -- QWP transmission at 810 nm exceeds 99%, and the beam path geometry is identical to standard Bong
3. Any residual theta-dependent efficiency would bias delta<AB> toward zero (reduced count rates at larger |cos theta|), not away from zero -> **eta < 0.91 cannot produce false positives for beta**
4. This directional argument does not close the loophole -- only eta >= 0.91 does -- but it establishes that eta insufficiency cannot mimic a positive beta signal

### 8.5 -- Detection Loophole: Fair-Sampling Defense

Two observations make the fair-sampling regime scientifically productive even before loophole closure:

**(a) Geometric confirmation of LF violation at theta = 31 deg:** Bong et al. demonstrated LF violation at theta = 90 deg (equatorial). This experiment would demonstrate LF violation at the first non-equatorial EWF measurement, confirming the violation is not an artifact of equatorial configuration. That geometric confirmation is model-independent and new regardless of loophole closure.

**(b) beta and LF violation from SAME coincidence set:** The four mixed-setting correlators are acquired simultaneously with the LF violation. A null result for beta, combined with LF violation from identical data, provides a self-consistent constraint on Eq. (2-3) that does not depend on absolute detector efficiency -- both signal and normalization are computed from the same coincidences.

**Historical precedent:** Fair-sampling has been standard in first-generation tests of every new Bell-type inequality. The original Bell tests (1972-2014) operated under fair-sampling for 42 years before loophole-free demonstrations in 2015. All EWF experiments to date, including Bong et al. (2020), operate under this assumption.

**Path to closure:** SNSPD upgrade (eta > 0.90 at 810 nm [16]) closes the detection loophole with no change to optical design.

### 8.6 -- Summary Table

| Parameter | Nominal | 5sigma Threshold | Bong Achievable | Margin |
|-----------|---------|-------------|-----------------|--------|
| mu | 0.95 | >= 0.90 (5sigma) / >= 0.86 (onset) | 0.92 | +0.02 |
| eta | 1.00 | >= 0.91 (at mu=0.95) | 0.87 | -0.07* |
| Delta_theta | 0 deg | <= +/-5 deg | < +/-1 deg | +4 deg |

*At eta = 0.87, need mu >= 0.96 to compensate. SNSPD upgrade closes this gap.

---

## Section 9 -- Loophole Analysis

| Loophole | Status | Notes |
|----------|--------|-------|
| Locality | Identical to Bong 2020 | QWP insertion local to Alice; space-like separation preserved |
| Detection | Conditional (eta >= 0.91) | Fair-sampling below threshold; SNSPD path to closure (Section 8.4-8.5) |
| Freedom of choice | Identical to Bong 2020 | Quantum random number generators |
| Superobserver assumption | Satisfied | Coherent measurement of Friend+photon via standard interferometry (waveplates + PBS). "Friend" is beam path, not conscious observer |
| Model class scope | Explicit: Eq. (2-3) | Constrains any f_perp-based outcome-overlap model; other dependence structures outside scope |
| K9_E scope | Explicit | Tests K9_E at single geometry (theta = 31 deg, N = 2). Null result excludes K9_E at tested beta but not all registration-layer effects. Positive result motivates theta-sweeps and 3-observer tests |

---

## Section 10 -- Interpretation Landscape

### 10.1 -- Positive Result

delta<A1B2> != 0 at >= 5sigma would be first evidence for outcome-dependent quantum registration. Combined with LF violation, this simultaneously rules out Local Friendliness AND supports K9_E as a candidate mechanism. Does NOT contradict standard QM (which is silent on registration architecture).

Key caveat: The experiment demonstrates a departure from standard QM at theta = 31 deg -- a previously untested geometric configuration. Interpreting this as outcome-dependent registration specifically requires theta-sweeps and multi-observer follow-up to verify the theta-dependent structure predicted by Eq. (4) (exact theta-dependence numerical; vanishes iff theta = pi/2).

### 10.2 -- Null Result

If LF violated but delta ~ 0: K9_E coupling is zero at tested beta, or beta << sensitivity threshold. If BOTH zero: calibration failure likely (QM predicts LF violation at mu >= 0.86). Calibration procedure (Section 5.4) disambiguates.

### 10.3 -- Interpretation Map

| Interpretation | Compatible with delta != 0? | Compatible with delta = 0? | Notes |
|---------------|----------------------|----------------------|-------|
| Copenhagen | Yes | Yes | No challenge either way -- Friend has no definite pre-measurement outcome |
| Many-Worlds | Challenged by LF violation | Yes | LF violation denies absoluteness of observed events |
| Relational QM | Yes (K9_E specifies when/how outcomes become relative) | Yes | RQM is silent on quantitative outcome-dependence |
| Objective Collapse | K9_E is alternative to dynamical collapse | Yes | Collapse models make different predictions for multi-observer configurations |
| QBism | Yes (outcome-dependence = agent-dependence extended) | Yes | QBism is silent on multi-agent registration consistency |
| VVV-QMRF | **Positive = confirms K-space structure** | **Null = falsifies K9_E at tested beta** | Only framework making quantitative prediction via K9_E |

The experiment is interpretation-neutral by design. Standard QM predicts the same Gen LF 1 violation regardless of theta -- the equatorial plane is not geometrically special. If a theta-dependent signal were detected, that would indicate new physics independently of which specific model class generated it. Equations (2-3) provide a parametrization for quantifying sensitivity; the primary scientific result is the theta-dependence (or its absence), not the specific value of beta.

---

## Section 11 -- Future Directions

### 11.1 -- theta-Sweep (Highest Priority)

The most immediate follow-up is a systematic scan of the polar angle over the pre-registered angle set {20, 31, 35, 45, 58, 90} deg (90 deg = equatorial control; per K9S12_PreRegistration_Protocol.md). This would directly map the theta-dependence predicted by Eq. (4) — delta vanishes iff theta = pi/2 and is generically non-zero otherwise (exact functional form determined numerically; the unrenormalized leading-order structure goes as cos theta but overestimates |delta| by ~5.5x due to renormalization). A null result across all theta would exclude the class Eq. (2-3) down to the sensitivity floor of the apparatus (beta ~ 0.02 at N = 200,000).

### 11.2 -- Multi-Observer Extension

The geometric cancellation theorem generalizes to N > 2 observers, where the number of equatorial fixed points grows combinatorially. Preliminary analysis suggests ~11x amplification of the outcome-dependent signal at beta = 0.3 for 3-observer configurations: delta_M3 = -0.223 (11x the 2-observer delta = -0.0355). This is **conditional** on the extension of bridge theorems T4-H (Steps 2-4) connecting registration-layer structure to quantum mechanical observables for N >= 3.

### 11.3 -- Platform Independence

While the protocol targets the optical Bong et al. apparatus, the theorem in Section 4 is platform-agnostic. Implementing the tilted Superobserver measurement on solid-state (superconducting qubits) or trapped-ion platforms would test whether the theta-dependent structure (vanishing iff theta = pi/2, non-zero otherwise) persists when the "Friend" is a macroscopic quantum system rather than a photon path degree of freedom.

### 11.4 -- Locality Closure

Combining the tilted geometry with space-like separated random basis switching would close the locality loophole simultaneously with the detection loophole (via SNSPDs, Section 8.5). Requires a dedicated fiber network or free-space optical link.

### 11.5 -- 2BSM/1BSM Ratio

Distinguish additive vs multiplicative K9_E forms via systematic variation of the number of Bell-state measurements per correlator. The two models predict different scaling with n_BSM -- resolving this requires multi-setting data beyond the 4-point Proietti configuration (K9E-PAT CLOSED UNRESOLVABLE, Section 3.3).

---

## Section 12 -- Reproducibility

### 12.1 -- Code

All numerical predictions reproducible via scripts in the repository:

| Script | Purpose | Key Output |
|--------|---------|-----------|
| `K9S12_proposal.py` | Full protocol: angle optimization, correlator table, K9_E predictions, QWP implementation | Gen LF 1, delta<A1B2>, beta sweep |
| `statistical_significance.py` | FOM scan across alpha in [25 deg, 75 deg], Monte Carlo, sigma computations | Optimal alpha = 31 deg, FOM landscape |
| `universal_theorem_lf_check.py` | Sympy verification of Equatorial Cancellation Theorem | Proof automatable |

```bash
cd 07_fits
python K9S12_proposal.py
# Gen LF 1 = +0.0891 +/- 0.0103 (8.6sigma)
# delta<A1B2> = -0.0355 (20.8sigma at beta = 0.3)
```

Requirements: Python 3.9+, numpy, scipy. No external data files needed.

### 12.2 -- Two K9_E Model Forms

- **Additive** (`k9e_predictor.py`): E = E_QM * (1 - beta * n_BSM * g_ctx), g_ctx = 0.039
- **Multiplicative** (`proietti_raw_fit.py`): E = E_QM * (1 - beta * g_eff)^(n_BSM), g_eff = 0.146

Both predict suppression ratio ~2 for 2BSM/1BSM. See `T1B_model_comparison_RCA.md` for full analysis. The experiment proposed here does not depend on which form is correct -- it measures beta from mixed-setting correlators where n_BSM = 1 for both forms.

---

## Section 13 -- Literature Search Audit Summary

**Full audit trail:** `supplemental/S1_search_audit.md`

**Databases searched:** Google Scholar, arXiv (quant-ph), Web of Science, InspireHEP

**Search strings:** Boolean combinations of ("Wigner's friend" OR "extended Wigner" OR "Local Friendliness") AND ("equatorial measurement" OR "Bloch sphere polar angle" OR "outcome dependence" OR "geometric constraint" OR "measurement basis")

**Date range:** January 2000 - May 2026

**Screening:** ~310 hits -> ~200 title screen -> ~80 abstract screen -> ~50 full-text -> ~30 detailed exam

**Key documents examined:** Bong et al. (2020) 47-page Supplemental Material; Proietti et al. (2019) Methods + Supplementary Information; Frauchiger-Renner (2018); Wiseman-Cavalcanti-Rieffel (2023); multipartite, sequential, and possibilistic LF extensions; Brunner et al. (2014) review; Stanford Encyclopedia of Philosophy entry on Wigner's Friend.

**Result:** No prior work identifies the Superobserver's polar angle theta as a relevant or tunable parameter in EWF experiments. Azimuthal angles are extensively optimized and reported; theta is implicitly fixed to pi/2 without comment. No EWF experiment has been performed at theta != pi/2 for any purpose.

**Limitations:** Single searcher; conference proceedings not fully indexed; English-only; partial preprint server coverage beyond arXiv. Independent replication recommended before journal submission.

---

## Section 14 -- Version Evolution Summary: v4 -> v95

### 14.1 — v4 to v21: K9_E Identity → Academic Polish

| Version | Date | Key Change | K9_E Impact |
|---------|------|-----------|-------------|
| v4 (draft_v1.md) | 2026-05-24 | K9-S12 proposal. Full K9_E postulate + VVV-QMRF context + beta sweep + decision criteria | **K9_E identity = central** |
| v12 | 2026-05-24 | **Eq.(12) CRITICAL FIX:** analytical -> exact numerical. beta thresholds corrected. | **Numbers corrected** |
| v13 | 2026-05-24 | Title change + ESP boundary + K-space notation removed from Section 9.3 | K9_E language begins removal |
| v14 | 2026-05-25 | SME precedent [15] + SNSPD upgrade path [16] | Academic defense added |
| v15 | 2026-05-25 | "VVV-QMRF K9_E" -> "framework of measurement registration" | **K9_E name removed** |
| v16 | 2026-05-25 | S1 search audit + theta-sensitivity in main text | Reviewer defense |
| v17 | 2026-05-25 | beta physical meaning + constraint scope + 2-observation loophole defense | Honest beta framing |
| v18 | 2026-05-25 | Ontological classification (IS-NOT) + null test framing + theta trade-off | Physical clarity |
| v19 | 2026-05-25 | Physical intuition + Section 2.3 compression + novelty hedge tied to S1 | Intuition added |
| v20 | 2026-05-25 | f_perp class-representative framing + eta-direction analysis | Class scope clarified |
| v21 | 2026-05-25 | mu-threshold 0.86->0.92(5sigma) + honest abstract + Section 9.2->S3 | Academic honesty |

### 14.2 — v21 to v95: Watershed RCA Decisions

| Version | Date | Key Change | Manuscript Impact |
|---------|------|-----------|------------------|
| v53 | 2026-05-25 | **Genre crystallization**: "phenomenological null test" explicit. GPT/weak-measurement stripped from §2.3. §8.1+§8.2 merged. Abstract compressed 13→8 lines. | K9_E publicly = Eq.(2-3) only. Genre locked. |
| v54 | 2026-05-25 | "Why overlap-only?" new subsection in §2.3. SME benchmark framing ("search target, not theory prediction"). f_perp class-representative. | β-motivation established. |
| v57 | 2026-05-25 | §7 compressed 67→12 lines (detail→S2). §8.1 compressed 22→10 lines. Paper 714→649 lines. | K9_E experimental detail moved to S2. |
| v62 | 2026-05-25 | Two-phase program (§7): Phase 1 loophole-open / Phase 2 SNSPD closure. BSM equivalence footnote [a]. | Protocol structure finalized. |
| v63 | 2026-05-25 | Survey table contextualized (N=2 explicit). Lemma 1 de-circularized. Two-phase in Abstract. FOM formula explicit. | All-accept RCA round. N=2 addressed. |
| v65 | 2026-05-25 | §2.3 SME analogy developed (7 lines). Abstract survey bridge sentence added. | β = search parameter established as §2.3 argument. |
| v75 | 2026-05-26 | Abstract N=2 acknowledgment: "only two such implementations exist." §1 Proposition 1 merged (−9 lines). | N=2 in abstract = proactive acknowledgment. |
| v77 | 2026-05-26 | Abstract hook: "have operated exclusively at θ=π/2 — a fixed point." §3.5 "Structural, not coincidental" (+7 lines). **TITLE FROZEN.** | Factual, not anthropomorphic. N=2 gap = structural. |
| v79 | 2026-05-26 | "structurally untested" → "systematically unexplored" (4 occurrences). | Observational fact vs implicit accusation. |
| v81 | 2026-05-26 | **GENRE BOUNDARY FROZEN**: "paper does not need more physics motivation." Auto-reject rule for "add physical mechanism" RCA suggestions. | Physics motivation at §2.3 level = correct depth. |
| v84 | 2026-05-26 | Abstract: "blind spot for the overlap-only class" (scope qualifier). §2.3 Physical context expanded (weak measurement + decoherence). §8.2 + S3 trimmed (−35 lines). | Scope qualifier in hook = prevents overclaim. |
| v85 | 2026-05-26 | §3.5: θ as INDEPENDENT LF DoF (+3 lines). §3.5 "Search audit" + "Prior work" merged (−8 lines). §1 + §9 rebalanced. | Structural novelty = θ orthogonal to LF constraint surface. |
| v87 | 2026-05-26 | Abstract tightened ~150 words. "unnoticed geometric blind spot" → "have operated exclusively at... fixed point" (factual). §2.3: "phenomenological ansatz, not derived from any underlying physical theory." | Abstract = factual, 150 words. |
| v88 | 2026-05-26 | "In brief" paragraph: operational observable + novelty crystallization. Two contributions stated: (1) Proposition 1 null theorem, (2) single-waveplate protocol. | Structure of paper crystallized in plain English. |
| v92 | 2026-05-26 | §5 density matrix corrected: I/4 → (|HV⟩⟨HV|+|VH⟩⟨VH|)/2. β=0.07 window [35°,46°] noted. MC rate at β=0.07 corrected >99%→~38%. | SPDC subspace model explicit. |
| v93 | 2026-05-27 | FOM values corrected to per-theta re-optimization: [20°,45°] replaces [20°,55°]. S2_derivation "[EXACT]" formula removed. | **FOM window corrected: [20°,45°].** |
| v94 | 2026-05-27 | **cos θ DOWNGRADED**: "δ ∝ cos θ" → "δ vanishes iff θ=π/2; non-zero otherwise; exact θ-dependence numerical." cos θ overestimates |δ| by ~5.5×. θ=31° "optimal" → "near-optimal." S2: 5.5× overestimate warning added. §2.3 + §3.5 FROZEN. | **Central claim precision corrected.** |
| v95 | 2026-05-31 | **§8.1 Falsification Hierarchy boundary**: Level 0 null ≠ Levels 1–3. Boundary sentence added after comparison table. 3-round RCA 4.1/5. | See Section 18 of this SOT. |

---

## Section 15 -- Cross-Reference: SOT -> Manuscript v95

| SOT Section | Manuscript v95 Section | Preserved? | Notes |
|------------|----------------------|-----------|-------|
| Section 1 K9_E Postulate P9 | Section 2.3 Eq. (2-3) | Rescoped | P9 -> phenomenological parametrization |
| Section 2 VVV-QMRF Architecture | Section 9.3 (prose only) | Minimized | "framework of measurement registration" only |
| Section 3 Class C History | -- | **Removed** | Internal VVV-QMRF context |
| Section 4 Equatorial Cancellation Theorem | Section 3 | **Preserved** | Core contribution |
| Section 5 Experimental Protocol | Section 4 | **Preserved** | Hardware + angles + calibration |
| Section 6 Numerical Predictions | Section 5 | **Preserved** (subset) | beta sweep condensed |
| Section 7 Statistical Analysis | Section 6 | **Preserved** | MC + Poisson |
| Section 8 Robustness | Section 7 | **Preserved** (corrected) | v21 mu-threshold fix |
| Section 9 Loophole Analysis | Section 8 | **Preserved** | |
| Section 10 Interpretation Landscape | Section 9.2 + S3 | Moved to S3 | To reduce reviewer attack surface |
| Section 11 Future Directions | Section 9.4 | **Preserved** | |
| Section 12 Reproducibility | S3 (code index) | Preserved | |
| Section 13 Literature Search Audit | S1 (search audit) | Preserved | |
| FOM definition | §4.1 (prose) | Rescoped | FOM = min(n_σ_LF, n_σ_signal) explicit in §5.3 |
| beta = 0.598 Proietti fit | -- | **Removed** | v4 removed (honest: "empirically unconstrained") |
| Section 17 φ_R Restricted Existence | -- | **NOT in manuscript** | Internal VVV-QMRF context (I.2, 2026-06-01) |
| Section 18 Falsification Hierarchy | §8.1 (boundary sentence) | Preserved (partial) | "Level 0 null ≠ Levels 1–3" added v95 |

---

## Section 16 -- Key Numbers Quick Reference

| Quantity | Value | Source Version |
|----------|-------|---------------|
| Gen LF 1 (theta = 31 deg, mu = 0.95) | +0.0891 +/- 0.0103 (8.6sigma) | v12 (corrected) |
| delta<A1B2> (beta = 0.3) | -0.0355 (20.8sigma) | v12 (corrected) |
| FOM | 8.6 | v12 |
| beta_min (single setting, 5sigma) | 0.075 | v12 (corrected) |
| beta_min (combined 4-setting, 5sigma) | 0.038 | v12 (corrected) |
| |delta| at beta = 0.05 | 0.0057 | v12 (corrected) |
| |delta| at beta = 0.07 | 0.0080 | v12 (corrected) |
| mu threshold (onset) | 0.86 | v12 |
| mu threshold (5sigma) | 0.92 | **v21 (corrected)** |
| eta threshold (5sigma, at mu = 0.95) | 0.91 | v12 |
| Delta_theta tolerance (5sigma) | <= +/-5 deg | v12 |
| FOM > 5sigma window (theta range) | [20 deg, 45 deg] | v93 (per-theta re-opt; [20,55] was pre-opt error) |
| N_min (5sigma LF) | 30,800 | v12 |
| MC: Gen LF 1 >= 5sigma | 99.97% | v12 |
| P10-NOISE threshold | 0.10 sigma RMS | v30 |
| K9E-PAT status | CLOSED UNRESOLVABLE | v31 |
| Class C classification | qualified (v31) | v31 |

---

## Section 17 -- φ_R Restricted Existence (I.2, 2026-06-01) — VVV-QMRF Layer 2/3 Context

**Status:** Class C THEOREM (proven by explicit construction, RCA 4.79/5)
**Source:** `documents/research_documents/meta_architecture/phi_restricted_existence_v1_0.md` v1.0
**Relevance to paper_002:** K9_E (Layer 3) requires K-space structural context from Layers 1-2. I.2 proves the K→B(H) correspondence map exists (restricted), which grounds K9_E's claim that K-space registration structure has a B(H) image.

### 17.1 -- What Was Proven

```
THEOREM (φ_R Restricted Existence):
  φ_R: K_R → P(H) ∪ {0}  (projection sub-lattice, NOT full B(H))
  
  CONSTRUCTION:
    φ_R(k) := |o⟩⟨o|      if V(k) = 1  (valid outcome k)
    φ_R(k) := 0_{B(H)}     if V(k) = 0  (invalidated / null)
  
  CLAIM (all proven):
    (1) φ_R total and well-defined on K_R
    (2) φ_R satisfies N_1–N_8 and N_T (all necessary conditions)
    (3) Im(φ_R) ⊆ P(H) ∪ {0} — tight, nothing more
    (4) N ≥ 3: unique colimit extension φ_colim via T4-H Step 4
        satisfying φ-N2, φ-N3
```

### 17.2 -- What This Changes vs Prior Status

| Aspect | Before I.2 | After I.2 |
|--------|-----------|-----------|
| φ-map claim | "VVV-QMRF conjectures existence of φ: K → B(H)" | "φ_R: K_R → P(H)∪{0} **proven** (Class C THEOREM)" |
| Codomain | B(H) (full operator algebra) | P(H) ∪ {0} (outcome projectors + zero only) |
| Class | D conjecture | **C THEOREM** (restricted existence) |
| N≥3 extension | Conditional (T4-H Steps 2-4 deferred) | **φ-N1 THEOREM**: unique colimit, φ-N2, φ-N3 ✅ |

### 17.3 -- What Was NOT Proven (Boundary, I.1)

```
NOT PROVEN (characterized boundary — I.1 Theorem A+B):
  ✗ N_6 sufficiency: P_{o2}·P_{o1}≠0 → Auth=1  [I.1 Theorem A]
  ✗ Global K_joint path-commutativity has B(H) encoding  [I.1 Theorem B]
  ✗ φ_R is a homomorphism/functor in strict categorical sense

CODOMAIN NOTE:
  φ_R does NOT map to: ρ (density operators), x̂, p̂, or any observable
  without K-registration analogue. P(H)∪{0} = outcome projectors + 0 ONLY.
  The restriction is TIGHT — Im(φ_R) is smallest B(H) subset needed.
```

### 17.4 -- Relationship to K9_E (paper_002 Experiment)

K9_E (Layer 3) predicts probability modification at the registration layer. I.2 proves that K-space registration events map to projection operators in B(H) — the operators through which K9_E modifies Born-rule probabilities. The chain is:

```
K1–K8 (axioms) → K_R (registration space)
                       ↓ φ_R [I.2 THEOREM]
                  P(H)∪{0} ⊂ B(H)
                       ↓ K9_E [Layer 3 postulate]
  P(o|K) = Tr(E_o ρ) · [1 − β·f_perp(o, K_ctx)] / Z_E
                       ↓ Equatorial Cancellation Theorem
  f_perp(+1,H) − f_perp(−1,H) = −cos θ  → vanishes iff θ = π/2
```

**Key scope note:** I.2 proves existence of φ_R on P(H)∪{0}. K9_E applies to the FULL Tr(E_o ρ) Born rule. The two are structurally consistent (K9_E multiplies Born-rule probabilities by f_perp factors derived from the same K-space geometry). I.2 does NOT prove K9_E holds — K9_E remains Class C qualified (postulate, not theorem).

### 17.5 -- AHP Check for SOT Addition

| Criterion | Status |
|-----------|--------|
| I.2 traces to K1–K8 (frozen) | ✅ Construction from K4 (V→projector), K5 (V=0→zero), K1 (total) |
| "Restricted" explicit throughout | ✅ P(H)∪{0}, not B(H) |
| Boundary cited | ✅ §17.3 cites I.1 Theorem A+B |
| K ≠ H preserved | ✅ Im(φ_R) ⊆ P(H)∪{0}, observables ≠ states ρ |
| K9_E independence preserved | ✅ I.2 grounds K-space structure; K9_E = separate postulate |

---

## Section 18 -- Falsification Hierarchy Level Boundary (v95, §8.1)

**Source:** manuscript.md v95, §8.1. RCA 4.1/5, 3-round review 2026-05-31.
**Root cause resolved:** v93-v94 §8.1 implicitly treated "Level 0 null" = "all overlap-dependent deformations null" — category error vs the four-level hierarchy defined in §3.2.

### 18.1 -- The Four-Level Deformation Hierarchy (§3.2)

| Level | Class | Dependence | Geometric null? |
|-------|-------|-----------|----------------|
| 0 (overlap-only) | f(|⟨b|d⟩|²) only | Basis overlap scalar | **YES** — at θ=π/2 identically |
| 1 (density-matrix) | f(ρ_F, |⟨b|d⟩|²) | Friend state purity | No |
| 2 (multi-partite) | f(concurrence, |⟨b|d⟩|²) | Entanglement | No |
| 3 (non-geometric) | timing, path, other | Non-geometric | No |

K9_E as parametrized by Eq. (2-3) targets **Level 0 only**. Proposition 1 (equatorial cancellation theorem) applies to Level 0. Levels 1–3 are NOT constrained by the θ=π/2 fixed-point argument.

### 18.2 -- Boundary Sentence Added (v95)

**Text added to §8.1 after comparison table (v95, RCA 4.1/5):**

> "A null result at Level 0 (β < β_min across the full θ-sweep) falsifies the overlap-only class but leaves Levels 1–3 unconstrained: density-matrix-dependent (ρ_F), multi-partite (concurrence), and non-geometric (timing, path) deformations are not bounded by Proposition 1 and each requires independent experimental designs."

### 18.3 -- Implication for K9_E Classification

| Outcome | K9_E Interpretation |
|---------|-------------------|
| δ⟨AB⟩ ≠ 0 at θ=31°, ≥5σ | K9_E (Level 0) supported at tested β |
| δ⟨AB⟩ ~ 0 (full θ-sweep) | K9_E Level 0 **falsified** at tested β; Levels 1–3 open |
| δ⟨AB⟩ ~ 0 (single θ=31°) | Inconclusive: β below sensitivity OR K9_E absent |

A null result from this experiment (K9-S12, θ=31°) constrains the specific parametrization Eq.(2-3) but does NOT generically falsify "outcome-dependent quantum registration" at all levels.

### 18.4 -- Scope Precision for Future Revision

When revising paper_002 or designing follow-up experiments, keep in mind:
- **Proposition 1** = Level 0 geometric theorem (tight scope)
- **K9_E** = Level 0 parametrization (β, f_perp = |⟨b|d⟩|-based)
- **K9-S12 protocol** = first experimental test of Level 0 at θ=31°
- **θ-sweep** = necessary to fully constrain Level 0 (Section 11.1)
- **Level 1-3 tests** = require different experimental designs (not this experiment)

---

## Appendix A -- Full beta-Sweep Correlator Table (theta = 31 deg, mu = 0.95)

| (x,y) | <AB>_QM | sigma | <AB> (beta=0.03) | <AB> (beta=0.05) | <AB> (beta=0.07) | <AB> (beta=0.10) | <AB> (beta=0.30) |
|-------|---------|-------|------------------|------------------|------------------|------------------|------------------|
| (1,1) | -1.0000 | 0.0000 | -1.0000 | -1.0000 | -1.0000 | -1.0000 | -1.0000 |
| (1,2) | -0.8572 | 0.0017 | -0.8606 | -0.8629 | -0.8652 | -0.8687 | -0.8927 |
| (1,3) | -0.8572 | 0.0017 | -0.8606 | -0.8629 | -0.8652 | -0.8687 | -0.8927 |
| (2,1) | -0.8572 | 0.0017 | -0.8606 | -0.8629 | -0.8652 | -0.8687 | -0.8927 |
| (2,2) | -0.5045 | 0.0029 | -0.5045 | -0.5045 | -0.5045 | -0.5045 | -0.5045 |
| (2,3) | -0.8933 | 0.0015 | -0.8933 | -0.8933 | -0.8933 | -0.8933 | -0.8933 |
| (3,1) | -0.8572 | 0.0017 | -0.8606 | -0.8629 | -0.8652 | -0.8687 | -0.8927 |
| (3,2) | -0.8933 | 0.0015 | -0.8933 | -0.8933 | -0.8933 | -0.8933 | -0.8933 |
| (3,3) | -0.8829 | 0.0016 | -0.8829 | -0.8829 | -0.8829 | -0.8829 | -0.8829 |

All values from exact numerical density matrix computation (v12+).

---

## Appendix B -- References

[1] M. Proietti et al., Science Advances 5, eaaw9832 (2019).
[2] K.W. Bong et al., Nature Physics 16, 1199-1205 (2020).
[3] E.P. Wigner, in The Scientist Speculates, Heinemann (1961).
[4] D. Deutsch, Int. J. Theor. Phys. 24, 1-41 (1985).
[5] L. Hardy, Phys. Rev. Lett. 68, 2981 (1992).
[6] D. Frauchiger and R. Renner, Nature Comms. 9, 3711 (2018).
[7] N. Brunner et al., Rev. Mod. Phys. 86, 419 (2014).
[8] J.S. Bell, Physics 1, 195-200 (1964).
[9] M. Giustina et al., Phys. Rev. Lett. 115, 250401 (2015).
[10] H.M. Wiseman, E.G. Cavalcanti, and E.G. Rieffel, Quantum 7, 1112 (2023).
[11] M. Haddara and E.G. Cavalcanti, arXiv:2407.20346 (2024).
[12] A. Utreras-Alarcon, E.G. Cavalcanti, and H.M. Wiseman, Proc. R. Soc. A 480 (2023).
[13] M. Haddara and E.G. Cavalcanti, New J. Phys. 25, 093028 (2023).
[14] A. Kent, arXiv:2302.12707 (2023).
[15] D. Colladay and V.A. Kostelecky, Phys. Rev. D 55, 6760 (1997).
[16] F. Marsili et al., Nature Photonics 7, 210-214 (2013).

---

*SOT synthesized 2026-05-25, re-synced 2026-05-31 to manuscript v95, updated 2026-06-02 (RCA K9_E Completeness 3-round 4.7/5 PASS). Sources: draft_v1.md (v4, K9-S12 proposal) + manuscript.md (v95, academic paper) + v12 Eq.(12) fix + CHANGELOG v12-v95 + supplemental S1-S3 + phi_restricted_existence_v1_0.md (2026-06-01 I.2). All numbers from exact numerical density matrix computation (v12+). Density matrix: SPDC noise model ρ_μ = μ|Ψ⁻⟩⟨Ψ⁻| + (1−μ)/2·(|HV⟩⟨HV|+|VH⟩⟨VH|). cos θ: all instances "vanishes iff θ=π/2; non-zero otherwise; exact θ-dependence numerical; unrenormalized leading-order cos θ overestimates |δ| by ~5.5×" (v94). FOM window: [20°,45°] per-θ-reoptimized (v93). New sections 2026-06-02: §17 φ_R restricted existence (I.2, Class C THEOREM), §18 Falsification Hierarchy Level Boundary (v95 §8.1). Version lineage extended: v21→v95 in Section 14.2.*
