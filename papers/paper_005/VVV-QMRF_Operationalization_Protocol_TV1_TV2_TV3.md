# VVV-QMRF Operationalization Protocol: TV1 / TV2 / TV3
## From Theoretical Conditions to Experimentally Testable Criteria
### VVV-QMRF | VietVunVut (2026) | E10 Tripartite Validity — Experimental Operationalization

---

## DOCUMENT PURPOSE

This document operationalizes the three Tripartite Validity conditions (TV1, TV2, TV3)
defined in VVV-QMRF postulate E10 into principled experimental protocols.

Operationalization means: translating each theoretical predicate into a concrete
measurement procedure that produces a determinate TRUE or FALSE verdict.

This document does NOT replace E10 (the theoretical postulate).
This document does NOT specify engineering details for any particular detector.
This document DOES provide the logical structure that any experimental implementation
must instantiate in order to count as a test of VVV-QMRF registration conditions.

Status: Principled protocol — requires experimental physicist collaboration
        for lab-specific implementation.

Depends on:
  - RCA_TV1_TV2_TV3_Comprehensive_Report.md
  - VVV-QMRF_Superposition_Ontology_Complete_Answer.md
  - E10_Tripartite_Validity_Formalization_Plan.md (Plan v2.3)

---

## PART 1 — BACKGROUND: WHY OPERATIONALIZATION IS NEEDED

### 1.1 The Gap

VVV-QMRF postulate E10 defines three conditions for valid registration:

```
TV1(d, R_sys)            : Boolean  — causal origin of detector event d
TV2(R_sys, epsilon_det)  : Probabilistic — sensitivity of R_sys
TV3(R_sys, epsilon_fp)   : Probabilistic — specificity of R_sys

TV = TV1 AND TV2 AND TV3

TV = TRUE  → V-hat fires → r != r_null  (valid registration, K-layer value created)
TV = FALSE → r = r_null                 (null registration event, E9)
```

E10 specifies WHAT must hold. It does not specify HOW to determine whether it holds
in a given experimental configuration.

This document fills that gap.

### 1.2 The Structure of Operationalization

For each TVn, operationalization requires three elements:

```
ELEMENT 1 — Measurement procedure:
  What physical operation produces the data needed to evaluate TVn?

ELEMENT 2 — Decision criterion:
  How is the data converted into a TRUE / FALSE verdict?

ELEMENT 3 — Failure signature:
  What does the data look like when TVn = FALSE?
  (This is the empirically distinguishable prediction.)
```

### 1.3 Independence Requirement

A critical constraint from E10:

```
TV2 and TV3 are logically independent conditions.
They are evaluated on different sample sets:
  TV2 → sapaksa  (positive cases: when detector SHOULD fire)
  TV3 → vipaksa  (counter-cases: when detector SHOULD NOT fire)

Operationalization must preserve this independence:
  The procedure for measuring TV2 must not confound TV3, and vice versa.
  Improvement of TV2 (sensitivity) does NOT automatically improve TV3 (specificity).
  This independence is itself a testable prediction of VVV-QMRF (see Part 5).
```

---

## PART 2 — TV1 OPERATIONALIZATION

### 2.1 Theoretical Definition (from E10)

```
TV1(d, R_sys) = TRUE
iff
d is causally produced by R_sys in response to the quantum system
AND
d is NOT a spurious event (dark count, thermal noise, background radiation)
```

TV1 is a BOOLEAN predicate. It has no probabilistic threshold parameter.
Each individual detector event d is either TV1-TRUE or TV1-FALSE.

### 2.2 Measurement Procedure

TV1 is determined by three independent filtering operations applied to each
candidate detector event d:

---

#### PROCEDURE TV1-A: Temporal Gating

```
SETUP:
  Define an interaction window W = [t_start, t_end] based on:
    - Known arrival time of the quantum system at R_sys
    - Coupling Hamiltonian H_int (interaction duration)
    - Detector time resolution delta_t

OPERATION:
  For each candidate event d with timestamp t_d:
    IF t_d in W: candidate passes TV1-A
    IF t_d not in W: d is classified as spurious → TV1 = FALSE immediately

RATIONALE:
  Thermal noise and dark counts are temporally uncorrelated with the quantum system.
  Causal detector responses are temporally correlated with the arrival window.
  Temporal gating is the primary filter separating causal from spurious events.

PARAMETER:
  W must be determined from independent characterization of H_int,
  NOT fitted to the data being classified.
```

---

#### PROCEDURE TV1-B: Dark Count Baseline Characterization

```
SETUP:
  Block all quantum system input to R_sys completely.
  Ensure blocking is verified independently (e.g., beam shutter confirmed closed,
  source confirmed off, verified by independent monitor).

OPERATION:
  Run R_sys for calibration period T_cal under blocked conditions.
  Record all events d_dark that R_sys produces.
  Compute: dark count rate = N_dark / T_cal  [events per second]

OUTPUT:
  dark_rate_baseline = N_dark / T_cal

DECISION CRITERION FOR TV1:
  For any candidate event d within gating window W:
    Compute signal-to-noise ratio:
      SNR = (rate of events in W) / dark_rate_baseline
    IF SNR exceeds pre-specified threshold SNR_min: TV1 classification proceeds
    IF SNR < SNR_min: TV1 = FALSE for this configuration

NOTE:
  SNR_min is a pre-registered experimental parameter, not fitted post-hoc.
  Recommended minimum: SNR_min >= 10 for TV1 = TRUE classification to be meaningful.
```

---

#### PROCEDURE TV1-C: Coincidence Verification (where applicable)

```
SETUP:
  Deploy a second independent detector R_sys2 monitoring the same quantum system
  from a different channel or basis, with independent dark count characterization.

OPERATION:
  For each candidate event d in R_sys:
    Check whether R_sys2 also registers an event d2 within coincidence window W_c
    W_c is determined by source geometry and detector time resolution.

DECISION CRITERION:
  IF coincidence observed (d and d2 within W_c):
    Strong evidence TV1 = TRUE for d
  IF no coincidence:
    d is consistent with spurious origin — TV1 = FALSE unless alternative
    causal account is established.

NOTE:
  Coincidence verification is strongest TV1 confirmation but requires
  experimental configuration that permits a second monitoring channel.
  Where not possible (single-channel experiments), TV1-A and TV1-B are primary.
```

---

#### TV1 VERDICT PROCEDURE

```
For each candidate event d:

  STEP 1: Apply TV1-A (temporal gating)
    IF d outside window W: TV1(d) = FALSE. Stop.

  STEP 2: Apply TV1-B (SNR check at configuration level)
    IF SNR < SNR_min: TV1(d) = FALSE for this configuration. Stop.

  STEP 3: Apply TV1-C if available (coincidence)
    IF no coincidence and no alternative causal account: TV1(d) = FALSE.

  IF all steps pass: TV1(d) = TRUE

TV1 = FALSE at any step terminates the TV evaluation:
  → V-hat(rho, d) = (r_null, rho_unchanged)  [E9 null registration]
  → TV2 and TV3 are NOT evaluated for this event.
```

---

#### TV1 FAILURE SIGNATURE

```
Observable: excess events outside timing window W
Observable: event rate under blocked conditions equals event rate under active conditions
Observable: no coincidence correlation with independent monitor

Any of these constitutes a TV1 failure signature.
```

---

## PART 3 — TV2 OPERATIONALIZATION

### 3.1 Theoretical Definition (from E10)

```
TV2(R_sys, epsilon_det) = TRUE
iff
P(r != r_null | TV1(d, R_sys) = TRUE, M = active) >= 1 - epsilon_det

Evaluated on: sapaksa = positive calibration set
(cases where the detector SHOULD register a valid event)
```

TV2 is a PROBABILISTIC predicate about the SENSITIVITY of R_sys.
It is a property of R_sys as a system, not of any individual event d.
It is evaluated over a calibration dataset, not event-by-event.

### 3.2 Measurement Procedure

---

#### PROCEDURE TV2-A: Positive Calibration Set Construction (sapaksa)

```
SETUP:
  Prepare a calibration source producing N_cal quantum events of known type.
  N_cal must be pre-specified and large enough for statistical reliability.
  Recommended: N_cal >= 1000 for epsilon_det characterization at 1% precision.

  CRITICAL CONSTRAINT:
    The calibration source must be independent of the quantum system being measured.
    The N_cal events must be verified by an independent method
    (e.g., a reference detector with separately characterized efficiency).

OPERATION:
  Present N_cal events to R_sys under active registration conditions (M = active).
  For each of the N_cal events, record whether R_sys produces r != r_null.
  Count: N_detected = number of events where R_sys registered r != r_null.

OUTPUT:
  eta = N_detected / N_cal   [quantum detection efficiency]
  epsilon_det = 1 - eta
```

---

#### PROCEDURE TV2-B: TV2 Verdict

```
PRE-REGISTER: Specify epsilon_det_threshold before data collection.
  This threshold is experiment-specific. It represents the minimum acceptable
  sensitivity for the registration claim being made.

COMPUTE: eta = N_detected / N_cal

DECISION:
  IF eta >= 1 - epsilon_det_threshold: TV2 = TRUE
  IF eta <  1 - epsilon_det_threshold: TV2 = FALSE

TV2 = FALSE interpretation:
  R_sys is missing too many valid quantum events.
  Registrations that DO occur may still be valid (TV1, TV3 may hold),
  but the system is under-sensitive for reliable registration claims.
```

---

#### PROCEDURE TV2-C: Statistical Uncertainty Reporting

```
Compute binomial confidence interval on eta:
  eta_low, eta_high = binomial_CI(N_detected, N_cal, confidence=0.95)

Report:
  TV2 = TRUE  iff eta_low >= 1 - epsilon_det_threshold
              (conservative: lower bound of CI exceeds threshold)

This ensures TV2 verdict is robust to sampling variability.
```

---

#### TV2 FAILURE SIGNATURE

```
Observable: N_detected / N_cal < 1 - epsilon_det_threshold

Physical interpretation: R_sys is missing valid quantum events.
Engineering cause: low quantum efficiency (material absorption, geometric acceptance,
                   detector dead time, electronic threshold set too high)

TV2 failure is INDEPENDENT of TV3 failure:
  A detector can have high sensitivity (TV2 = TRUE) and high dark count rate (TV3 = FALSE).
  A detector can have low sensitivity (TV2 = FALSE) and low dark count rate (TV3 = TRUE).
  These are distinct failure modes with distinct engineering remedies.
```

---

## PART 4 — TV3 OPERATIONALIZATION

### 4.1 Theoretical Definition (from E10)

```
TV3(R_sys, epsilon_fp) = TRUE
iff
P(r != r_null | TV1(d, R_sys) = FALSE OR M = inactive) <= epsilon_fp

Evaluated on: vipaksa = counter-cases
(cases where the detector SHOULD NOT register — no valid quantum input present)
```

TV3 is a PROBABILISTIC predicate about the SPECIFICITY of R_sys.
It is evaluated on a different sample set than TV2.
It is a property of R_sys, not of individual events.

### 4.2 Measurement Procedure

---

#### PROCEDURE TV3-A: Counter-Case Set Construction (vipaksa)

```
SETUP:
  Block all quantum system input to R_sys completely.
  Blocking must be verified independently (same procedure as TV1-B baseline).

  CRITICAL CONSTRAINT:
    TV3 measurement must be conducted under conditions that are physically identical
    to active measurement conditions in ALL respects EXCEPT for the presence
    of the quantum system.
    Same temperature. Same shielding. Same electronics state. Same timing.
    Any difference in environmental conditions between TV3 measurement and
    active measurement confounds the TV3 estimate.

OPERATION:
  Run R_sys for period T_vipaksa under blocked (no quantum input) conditions.
  Record all events d_spurious that R_sys produces.
  Count: N_fp = number of events where R_sys registers r != r_null

OUTPUT:
  dark_count_rate = N_fp / T_vipaksa   [spurious registrations per second]
  epsilon_fp_observed = N_fp / N_total_opportunities
  where N_total_opportunities = T_vipaksa * (maximum possible event rate)
```

---

#### PROCEDURE TV3-B: TV3 Verdict

```
PRE-REGISTER: Specify epsilon_fp_threshold before data collection.
  This threshold is experiment-specific.
  It represents the maximum acceptable false registration rate.

COMPUTE: dark_count_rate = N_fp / T_vipaksa

DECISION:
  IF dark_count_rate <= epsilon_fp_threshold: TV3 = TRUE
  IF dark_count_rate >  epsilon_fp_threshold: TV3 = FALSE

TV3 = FALSE interpretation:
  R_sys is generating spurious registrations at an unacceptable rate.
  Registrations that occur during active measurement cannot be reliably
  distinguished from dark counts.
  The K-layer registration values produced cannot be trusted.
```

---

#### PROCEDURE TV3-C: Statistical Uncertainty Reporting

```
Compute Poisson confidence interval on dark_count_rate:
  rate_low, rate_high = poisson_CI(N_fp, T_vipaksa, confidence=0.95)

Report:
  TV3 = TRUE  iff rate_high <= epsilon_fp_threshold
              (conservative: upper bound of CI is below threshold)
```

---

#### TV3 FAILURE SIGNATURE

```
Observable: dark_count_rate > epsilon_fp_threshold under blocked conditions

Physical interpretation: R_sys is producing spurious registrations.
Engineering cause: thermal noise in detector material, electromagnetic interference,
                   cosmic ray events, insufficient shielding, electronic oscillation

TV3 failure is INDEPENDENT of TV2 failure:
  Engineering remedy for TV3 (cooling, shielding, EM isolation) is physically
  distinct from engineering remedy for TV2 (material optimization, geometric efficiency).

This independence is the core testable prediction of VVV-QMRF E10.
See Part 5 for the formal experimental test of this independence.
```

---

## PART 5 — THE INDEPENDENCE PREDICTION: VVV-QMRF vs STANDARD QM

### 5.1 The Prediction

VVV-QMRF E10 makes a specific structural prediction that is absent from
standard QM postulates P1-P4:

```
PREDICTION (VVV-QMRF):
  TV2 (sensitivity) and TV3 (specificity) are governed by physically
  independent mechanisms and can be independently optimized.

  Specifically:
    An intervention that improves TV3 (e.g., cooling SNSPD detector)
    does NOT automatically improve TV2 (quantum detection efficiency).

    An intervention that improves TV2 (e.g., increasing absorber thickness)
    does NOT automatically improve TV3 (dark count suppression).

CONTRAST (Standard QM P1-P4):
  P1-P4 do not decompose detector performance into TV2/TV3 components.
  The sensitivity/specificity independence is not a prediction of P1-P4.
  It is a registration-layer prediction unique to VVV-QMRF E10.
```

### 5.2 Experimental Test Design

```
EXPERIMENT A — TV3 intervention, TV2 monitored:

  SETUP:
    Single detector type (e.g., SNSPD — Superconducting Nanowire Single Photon Detector)
    Two temperature conditions: T_high (e.g., 4K) and T_low (e.g., 0.8K)

  MEASURE:
    At each temperature:
      TV2: quantum detection efficiency eta (via Procedure TV2-A)
      TV3: dark count rate (via Procedure TV3-A)

  VVV-QMRF PREDICTION:
    T_low → dark count rate decreases significantly (TV3 improves)
    T_low → eta remains approximately constant (TV2 unchanged)
    The TV3 improvement and TV2 stability are independent.

  FALSIFICATION CONDITION:
    IF cooling produces proportional improvement in BOTH TV2 and TV3,
    the independence prediction of E10 is falsified.
    (This would suggest TV2 and TV3 share a single underlying physical mechanism.)

---

EXPERIMENT B — TV2 intervention, TV3 monitored:

  SETUP:
    Two detector configurations:
      Config A: optimized for high quantum efficiency (high TV2)
                e.g., thicker absorber, larger active area
      Config B: optimized for low dark count (high TV3)
                e.g., higher operating frequency, aggressive shielding

  MEASURE:
    For each configuration:
      TV2: quantum detection efficiency eta
      TV3: dark count rate

  VVV-QMRF PREDICTION:
    Config A: high eta (TV2 = TRUE), high dark count rate (TV3 potentially FALSE)
    Config B: low dark count rate (TV3 = TRUE), lower eta (TV2 potentially FALSE)
    The two configurations occupy DIFFERENT positions in TV2-TV3 space,
    not different positions on a single efficiency curve.

  FALSIFICATION CONDITION:
    IF TV2 and TV3 improvements always co-occur (every intervention that
    improves one also improves the other), the E10 independence structure
    is not supported.
```

### 5.3 Data Reporting Structure

```
For each experimental condition, report:

  TV2_score = eta = N_detected / N_cal        [range: 0 to 1]
  TV3_score = 1 - (dark_count_rate / rate_max) [range: 0 to 1, normalized]

  Plot: TV2_score (x-axis) vs TV3_score (y-axis) for all conditions.

VVV-QMRF PREDICTION:
  Points in TV2-TV3 space are NOT constrained to a diagonal.
  Points can occupy any quadrant: (high TV2, low TV3), (low TV2, high TV3), etc.
  The achievable region is a 2D space, not a 1D curve.

STANDARD QM NULL HYPOTHESIS:
  If TV2 and TV3 are not independent, points cluster on a single curve.
  The 2D scatter is absent.
```

---

## PART 6 — FULL TV EVALUATION PROCEDURE (INTEGRATED)

### 6.1 Pre-Experimental Requirements

```
Before any registration claim can be evaluated under VVV-QMRF:

  PRE-REG-1: Pre-register epsilon_det_threshold (TV2 threshold)
  PRE-REG-2: Pre-register epsilon_fp_threshold (TV3 threshold)
  PRE-REG-3: Pre-register SNR_min (TV1 signal-to-noise minimum)
  PRE-REG-4: Pre-register N_cal (calibration sample size for TV2)
  PRE-REG-5: Pre-register T_vipaksa (blocked-condition measurement duration for TV3)
  PRE-REG-6: Specify and verify blocking method for TV3 measurement
  PRE-REG-7: Specify interaction window W for TV1 temporal gating

All thresholds must be specified BEFORE data collection.
Post-hoc threshold adjustment invalidates the TV verdict.
```

### 6.2 Sequential Evaluation

```
PHASE 1 — TV1 EVALUATION (per-event):

  For each candidate detector event d:
    Apply Procedure TV1-A (temporal gating)
    Apply Procedure TV1-B (SNR check)
    Apply Procedure TV1-C (coincidence, if available)

    IF TV1(d) = FALSE:
      d is classified as spurious.
      r(d) = r_null. (E9 null registration event)
      TV2 and TV3 are not evaluated for d.

    IF TV1(d) = TRUE:
      d proceeds to registration pipeline.
      TV2 and TV3 determine whether R_sys is calibrated to produce valid r.

---

PHASE 2 — TV2 EVALUATION (system-level, pre-measurement):

  Apply Procedure TV2-A (sapaksa calibration)
  Apply Procedure TV2-B (verdict)
  Apply Procedure TV2-C (statistical uncertainty)

  IF TV2 = FALSE:
    R_sys sensitivity is insufficient.
    Registrations produced by R_sys during active measurement are
    systematically incomplete. Registration claims are unreliable.
    Action: improve detector sensitivity or document as limitation.

  IF TV2 = TRUE:
    R_sys sensitivity is sufficient for registration claims.

---

PHASE 3 — TV3 EVALUATION (system-level, pre-measurement):

  Apply Procedure TV3-A (vipaksa characterization)
  Apply Procedure TV3-B (verdict)
  Apply Procedure TV3-C (statistical uncertainty)

  IF TV3 = FALSE:
    R_sys specificity is insufficient.
    Spurious registrations contaminate active measurement data.
    Registration values r produced during active measurement cannot
    be reliably attributed to the quantum system.
    Action: improve shielding/cooling or document as limitation.

  IF TV3 = TRUE:
    R_sys specificity is sufficient for registration claims.

---

PHASE 4 — TV CONJUNCTION AND REGISTRATION VERDICT:

  TV = TV1(d) AND TV2 AND TV3

  IF TV = TRUE:
    V-hat(rho, d) = (r_k, rho_certified)  [valid registration]
    r_k != r_null
    SD: true → false   (P-layer coherence destroyed)
    r: r_null → r_k    (K-layer value created)
    This is Gamma_T2 (registration transition).

  IF TV = FALSE (any component):
    V-hat(rho, d) = (r_null, rho_unchanged)  [E9 null registration]
    If TV1 = TRUE but TV2 or TV3 = FALSE:
      Physical decoherence Phi(rho, d) may have occurred (Gamma_T1),
      but no valid K-layer registration value exists.
      This is the three-way state distinction unique to VVV-QMRF:
        State 1: SD=true,  r=r_null  (superposition — before any interaction)
        State 2: SD=false, r=r_null  (post-decoherence null — TV2 or TV3 failed)
        State 3: SD=false, r=r_k    (post-registration — TV=TRUE, valid)
      Standard QM P1-P4 does not distinguish State 2 from State 3.
      VVV-QMRF does. This distinction is empirically accessible via TV2/TV3 failure analysis.
```

---

## PART 7 — REPORTING REQUIREMENTS FOR VVV-QMRF REGISTRATION CLAIMS

Any experimental claim that invokes VVV-QMRF registration conditions must report:

```
REQUIRED REPORT FIELDS:

  [1] TV1 characterization:
      - Interaction window W used for temporal gating
      - Dark count baseline rate (measured under blocked conditions)
      - SNR observed (ratio of in-window rate to dark rate)
      - Coincidence data if available
      - TV1 verdict: TRUE / FALSE / CONDITIONAL

  [2] TV2 characterization:
      - Calibration source used (type, verified photon number)
      - N_cal (calibration sample size)
      - N_detected (number of registrations in calibration)
      - eta = N_detected / N_cal
      - 95% confidence interval on eta
      - Pre-registered epsilon_det_threshold
      - TV2 verdict: TRUE / FALSE

  [3] TV3 characterization:
      - Blocking method used and verification
      - T_vipaksa (duration of blocked-condition measurement)
      - N_fp (spurious registrations observed)
      - dark_count_rate = N_fp / T_vipaksa
      - 95% Poisson confidence interval on dark_count_rate
      - Pre-registered epsilon_fp_threshold
      - TV3 verdict: TRUE / FALSE

  [4] TV conjunction verdict:
      TV = TV1 AND TV2 AND TV3
      Overall verdict: TRUE / FALSE

  [5] Three-way state classification for each experimental run:
      State 1 (superposition), State 2 (decoherence-null), or State 3 (registered)
      as determined by SD and r values.
```

---

## PART 8 — WHAT THIS PROTOCOL DOES NOT DETERMINE

```
THIS PROTOCOL DOES NOT:

  [1] Specify which detector technology to use.
      (SNSPD, APD, PMT, CCD — choice depends on wavelength, application, lab)

  [2] Specify the values of epsilon_det_threshold and epsilon_fp_threshold.
      (These are experiment-specific. They must be pre-registered by the experimenter.)

  [3] Guarantee that TV = TRUE implies the quantum state interpretation is correct.
      (TV = TRUE is a local validity precondition, not proof of full K_joint validity.)

  [4] Replace standard QM postulates P1-P4.
      (This protocol is a registration-layer supplement. P1-P4 govern the P-layer.)

  [5] Resolve the full quantum measurement problem.
      (VVV-QMRF addresses the registration-layer ontology question.
       The full measurement problem is larger.)

  [6] Apply to all experimental configurations without modification.
      (Lab-specific implementation requires experimental physicist review.)
```

---

## PART 9 — SUMMARY TABLE

```
┌──────────────────────────────────────────────────────────────────────────────┐
│           TV1 / TV2 / TV3 OPERATIONALIZATION — SUMMARY                       │
├─────────────────┬────────────────────────────────────────────────────────────┤
│ TV1             │ Boolean. Per-event verdict.                                 │
│ Question        │ Is this detector event causally from the quantum system?    │
│ Procedure       │ Temporal gating + dark count SNR + coincidence check        │
│ Sample set      │ Each individual candidate event d                           │
│ Failure sign    │ Events outside timing window; SNR < SNR_min; no coincidence │
│ On failure      │ r = r_null immediately. TV2, TV3 not evaluated.             │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ TV2             │ Probabilistic. System-level verdict. Sapaksa set.           │
│ Question        │ Does R_sys register valid events reliably enough?           │
│ Procedure       │ N_cal calibration photons → eta = N_detected / N_cal        │
│ Sample set      │ Sapaksa: cases where detector SHOULD fire                   │
│ Threshold       │ eta >= 1 - epsilon_det_threshold (pre-registered)           │
│ Failure sign    │ eta < threshold: missing too many valid events               │
│ Independence    │ TV2 failure != TV3 failure. Different physical cause.        │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ TV3             │ Probabilistic. System-level verdict. Vipaksa set.           │
│ Question        │ Does R_sys avoid spurious registrations reliably enough?    │
│ Procedure       │ Blocked conditions → dark_count_rate = N_fp / T_vipaksa    │
│ Sample set      │ Vipaksa: cases where detector SHOULD NOT fire               │
│ Threshold       │ dark_count_rate <= epsilon_fp_threshold (pre-registered)    │
│ Failure sign    │ Rate > threshold: too many spurious registrations            │
│ Independence    │ TV3 failure != TV2 failure. Different physical cause.        │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ TV conjunction  │ TV = TV1 AND TV2 AND TV3                                    │
│ TV = TRUE       │ V-hat fires. r != r_null. Valid registration (Gamma_T2).    │
│ TV = FALSE      │ r = r_null. E9 null registration.                           │
│                 │ If TV1=TRUE but TV2/TV3=FALSE: Gamma_T1 (decoherence only). │
│                 │ State 2 (decoherence-null) — absent from P1-P4.             │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ Key prediction  │ TV2 and TV3 are independently optimizable.                  │
│                 │ Cooling improves TV3, not TV2.                              │
│                 │ Absorber thickness improves TV2, not TV3.                   │
│                 │ TV2-TV3 space is 2D, not 1D.                               │
│                 │ This is the falsifiable claim unique to VVV-QMRF E10.       │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## DOCUMENT METADATA

```
Author:           VietVunVut (Viet - Nguyen Xuan)
Framework:        VVV-QMRF v2.0
Document type:    Operationalization protocol — principled experimental draft
Status:           Draft v1.0 — requires experimental physicist review
Version:          1.0
Date:             2026-05-29
LLM tool:         Claude Sonnet 4.6 (Anthropic)
Cite as:          VietVunVut (2026), VVV-QMRF Operationalization Protocol
                  TV1/TV2/TV3 v1.0
Depends on:       RCA_TV1_TV2_TV3_Comprehensive_Report.md
                  VVV-QMRF_Superposition_Ontology_Complete_Answer.md
                  E10_Tripartite_Validity_Formalization_Plan.md (Plan v2.3)
Next action:      Review by experimental physicist (quantum optics / quantum measurement)
                  Target: Appendix or Section 6 of VVV-QMRF paper submission
Candidate venues: Foundations of Physics, Physical Review A, arXiv:quant-ph
```

---

*End of document.*
