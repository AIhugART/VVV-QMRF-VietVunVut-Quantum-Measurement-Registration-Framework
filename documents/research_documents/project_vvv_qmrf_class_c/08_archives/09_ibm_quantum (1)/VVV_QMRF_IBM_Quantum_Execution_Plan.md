# VVV-QMRF IBM Quantum Execution Plan
# K9_E Registration-Layer Suppression Test

**Version:** IBM-Plan v1.0 (2026-05-24)
**Purpose:** Step-by-step execution plan for testing K9_E predictions on IBM Quantum,
resolving K9E-PAT (2BSM/1BSM ratio), and unblocking the K-space ↔ EWF connection.
**Repository location:** `09_ibm_quantum/` under existing VVV-QMRF project root.
**Execution model:** Submit → Save Job ID → Close session → Retrieve later. No continuous runtime required.

---

## MASTER CONTEXT BLOCK
*Paste this block at the top of every IBM Quantum prompt session.*

```
FRAMEWORK: VVV-QMRF K9_E — Registration-Layer Suppression
VERSION: Class C (qualified) — structurally testable, empirically UNCONFIRMED

K9_E POSTULATE:
  P(o | K) = Tr(E_o ρ) · [1 − β · f_perp(o, K_ctx)] / Z_E
  f_perp(o, K_ctx) = fraction of K-states in context with incompatible outcomes
  β ∈ [0,1] = suppression strength (single free parameter)
  Born limit: β=0 → P(o|K) = Tr(E_o ρ) exactly

UNIVERSAL THEOREM (K9-S11c, algebraically proven):
  f_perp(+1,H) − f_perp(−1,H) = −cos(θ)
  Vanishes IFF θ = π/2 (equatorial superobserver basis)
  For z-Friend + equatorial-Superobserver: f_perp = 1/2 (constant) → K9_E = QM
  CONSEQUENCE: ALL existing EWF experiments (Proietti 2019, Bong 2020) are
  untestable by K9_E due to equatorial geometry choice.

MODIFIED BONG PROTOCOL (K9-S12):
  Superobserver tilt: α = 31° from z-axis (optimal)
  Hardware change: re-insert one quarter-wave plate (QWP)
  Predictions at α=31°, β=0.3:
    ⟨A₁B₂⟩_QM  = −0.857
    ⟨A₁B₂⟩_K9E = −0.893
    δ = −0.036 (20.8σ detectable)
  LF Genuine Facet 1: +0.089 (8.6σ violation simultaneously)

K9E-PAT OPEN ISSUE (HIGH priority):
  K9_E multiplicative model predicts: 2BSM/1BSM suppression ratio ≈ 2
  Proietti data shows: ratio = −0.78
  Sign wrong, magnitude wrong.
  Root cause unknown — may be noise artifact from 4-point fit (v30 downgrade).
  IBM experiment goal: resolve K9E-PAT with noise-characterized data.

IBM EXPERIMENT PURPOSE:
  1. Test K9_E geometric condition (α ≠ π/2 → f_perp outcome-dependent)
  2. Resolve K9E-PAT (2BSM/1BSM ratio) with clean noise characterization
  3. NOT claimed as: full EWF confirmation or Born rule modification
  4. Claimed as: proof of concept — K9_E signal detectable in tilted-basis setup

ACCESS NOTE:
  Vietnam geographic restriction: quantum.ibm.com may be blocked.
  Solution A: VPN with US/EU exit node → register account → save token → use Colab
  Solution B: Google Colab (runs on Google servers, not geographically blocked)
  Solution C: Local simulator (qiskit-aer) for circuit validation — no internet needed
  IBM job model: Submit → Save Job ID → Session can close → Retrieve later by Job ID
```

---

## FILE SYSTEM STRUCTURE

Add folder `09_ibm_quantum/` to existing VVV-QMRF project root.
Do NOT create a separate repository. Share `07_fits/utils/` across both EWF and IBM work.

```
VVV-QMRF/                              ← existing project root
├── 01_axiomatization/                 [UNCHANGED]
├── 02_derivation_chain/               [UNCHANGED]
├── 03_k9_sprints/                     [UNCHANGED — K9S12 is the foundation]
├── 04_governance/                     [UNCHANGED]
├── 05_ex_compass/                     [UNCHANGED]
├── 06_references/                     [UNCHANGED]
├── 07_fits/                           [UNCHANGED — utils/ shared]
│   └── utils/
│       ├── qm_standard.py             ← shared by IBM circuits
│       ├── k9e_predictor.py           ← shared by IBM circuits
│       └── k9a_predictor.py
├── 08_archives/                       [UNCHANGED]
└── 09_ibm_quantum/                    ← NEW — IBM Quantum experiment
    ├── README.md                      Purpose, links to K9S12 and K9E-PAT
    ├── IBM_JOB_REGISTRY.md            Job IDs, status, backend, shots
    ├── circuits/
    │   ├── k9e_base_circuit.py        EWF-analog: Friend (Z) + Superobserver (α)
    │   ├── k9e_alpha_sweep.py         Sweep α from 0° to 90° (18 angles)
    │   ├── k9e_1bsm_circuit.py        1-BSM analog for K9E-PAT ratio test
    │   ├── k9e_2bsm_circuit.py        2-BSM analog for K9E-PAT ratio test
    │   └── k9e_control_circuit.py     Control: α=90° (equatorial, K9_E=QM)
    ├── colab/
    │   ├── IBM_setup.ipynb            Account setup, token save, backend list
    │   ├── IBM_submit_jobs.ipynb      Submit all circuits, save Job IDs
    │   └── IBM_retrieve_results.ipynb Retrieve by Job ID, compute correlations
    ├── results/
    │   ├── raw/                       Shot-by-shot JSON from IBM
    │   │   └── [job_id]_counts.json
    │   └── processed/
    │       ├── alpha_sweep_results.csv   Correlations vs alpha
    │       ├── k9e_pat_ratio.csv         2BSM/1BSM ratio measurements
    │       └── control_baseline.csv      α=90° baseline (verify noise floor)
    ├── analysis/
    │   ├── noise_characterization.py     Distinguish K9_E signal from hardware noise
    │   ├── k9e_pat_resolution.md         K9E-PAT verdict: ratio confirmed or artifact
    │   ├── alpha_dependence_fit.py       Fit K9_E model vs noise model to α-sweep
    │   └── comparison_qm_vs_k9e.md      δ⟨A₁B₂⟩ measured vs predicted
    └── governance/
        ├── CHANGELOG_IBM.md             IBM-specific version history
        └── RCA_IBM_decisions.md         Decision records for IBM experiment
```

---

## STEP 0: Prerequisites Verification

**Goal:** Confirm all inputs from K9-S11c and K9-S12 are available before writing any code.

```
TASK: Prerequisites Verification for IBM Quantum Execution

[PASTE MASTER CONTEXT BLOCK HERE]

Verify the following inputs are available and consistent before proceeding.
For each item: state AVAILABLE / MISSING / INCONSISTENT with one-sentence reason.

INPUT 1: Universal Theorem formula
  Expected: f_perp(+1,H) − f_perp(−1,H) = −cos(θ)
  Check: Is this algebraically proven (not just numerical)?
  Source: K9-S11c Step A

INPUT 2: Optimal tilt angle
  Expected: α = 31°
  Check: Is this derived from FOM maximization, not just signal magnitude?
  Source: K9-S11d statistical significance scan

INPUT 3: K9_E predictions at α=31°
  Expected:
    ⟨A₁B₂⟩_QM  = −0.857
    ⟨A₁B₂⟩_K9E = −0.893  (at β=0.3)
    δ = −0.036 (20.8σ)
  Check: Are these numbers consistent with f_perp(31°) = |cos(31°)| = 0.857?
  Source: K9-S12

INPUT 4: K9_E predictor code
  Expected: 07_fits/utils/k9e_predictor.py functional
  Check: Does k9e_expectation(theta_A, theta_B, beta=0.3) return −0.893 at relevant angles?
  Source: 07_fits/utils/

INPUT 5: K9E-PAT statement
  Expected: 2BSM/1BSM ratio predicted ≈ 2, actual −0.78 in Proietti
  Check: Is this ratio computed from the genuine fit (proietti_raw_fit.py)?
  Source: 04_governance/ or 07_fits/

INPUT 6: IBM access path
  Expected: One of: VPN + IBM token / Colab + IBM token / Local simulator only
  Check: Which path is available?
  State: "Local simulator only" is sufficient for Steps 1-3.

PRODUCE:
  (A) Prerequisites table: 6 rows, AVAILABLE/MISSING/INCONSISTENT
  (B) Blocking items (MISSING or INCONSISTENT): list with resolution
  (C) Clearance verdict: "All prerequisites met — proceed to Step 1"
                         OR "Prerequisites [N] missing — resolve before Step 1"
```

**Save output as:** `09_ibm_quantum/governance/STEP0_prerequisites.md`

---

## STEP 1: Environment Setup

**Goal:** Install Qiskit locally and verify simulator works without internet.
This step requires NO IBM account and NO internet connection beyond pip install.

```
TASK: IBM Quantum Environment Setup and Verification

[PASTE MASTER CONTEXT BLOCK HERE]

Set up the Python environment for IBM Quantum circuit execution.
Execute each command and report the output. Do not proceed to the next
command if the previous one fails.

COMMAND 1: Install packages
  pip install qiskit qiskit-aer qiskit-ibm-runtime numpy scipy matplotlib

COMMAND 2: Verify Qiskit version
  python -c "import qiskit; print('Qiskit:', qiskit.__version__)"
  Expected: Qiskit 1.x.x or higher

COMMAND 3: Verify Aer simulator
  python -c "from qiskit_aer import AerSimulator; s = AerSimulator(); print('Aer OK:', s.name)"
  Expected: Aer OK: aer_simulator

COMMAND 4: Verify utils/ import path
  cd [VVV-QMRF root]
  python -c "
  import sys
  sys.path.append('07_fits')
  from utils.k9e_predictor import k9e_expectation
  from utils.qm_standard import qm_singlet_expectation
  import numpy as np
  result = k9e_expectation(0, np.pi/4, beta=0.3)
  qm = qm_singlet_expectation(0, np.pi/4)
  print(f'K9_E: {result:.4f}')
  print(f'QM:   {qm:.4f}')
  print(f'delta: {result-qm:.4f}')
  "
  Expected: K9_E value slightly different from QM value when beta=0.3

COMMAND 5: Verify Born rule recovery
  python -c "
  import sys, numpy as np
  sys.path.append('07_fits')
  from utils.k9e_predictor import k9e_expectation
  from utils.qm_standard import qm_singlet_expectation
  result = k9e_expectation(0, np.pi/4, beta=0.0)
  qm = qm_singlet_expectation(0, np.pi/4)
  assert abs(result - qm) < 1e-10, f'Born rule FAIL: {result} != {qm}'
  print('Born rule recovery: PASS')
  "
  Expected: Born rule recovery: PASS

PRODUCE:
  (A) Output of each command (copy-paste terminal output)
  (B) PASS/FAIL for each command
  (C) If any FAIL: error message + proposed fix
  (D) Overall verdict: "Environment ready" or "Environment setup failed at Command N"
```

**Save output as:** `09_ibm_quantum/governance/STEP1_environment.md`

---

## STEP 2: Base Circuit Design and Validation

**Goal:** Write and validate the EWF-analog quantum circuit.
Run on LOCAL SIMULATOR only — no IBM account needed.

```
TASK: EWF-Analog Circuit Design and Local Simulator Validation

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE STEP 1 ENVIRONMENT REPORT HERE]

Write the base EWF-analog circuit and validate on local Aer simulator.
The circuit is NOT expected to show K9_E deviation on a simulator
(simulators implement Standard QM). Simulator is used to verify circuit logic only.

CIRCUIT SPECIFICATION:
  q0 = Friend (Alice): measures in Z-basis → outcome c ∈ {0,1}
  q1 = Superobserver (Bob): measures at polar angle α from z-axis → outcome b ∈ {0,1}
  Initial state: singlet-analog |Φ⁻⟩ = (|01⟩ − |10⟩)/√2
  Tilt angle: parameterized (not hardcoded) — accept alpha_deg as argument

WRITE FILE: 09_ibm_quantum/circuits/k9e_base_circuit.py

Requirements:
  Function: create_ewf_circuit(alpha_deg=31.0) → QuantumCircuit
  Function: compute_correlation(counts, shots) → float in [−1, +1]
  State preparation: singlet-analog using H + CX + Z gates
  Superobserver measurement: Ry(alpha) gate before measure
  No mid-circuit measurements (use standard end-of-circuit measurement)

WRITE FILE: 09_ibm_quantum/circuits/k9e_alpha_sweep.py

Requirements:
  Sweep alpha from 0° to 90° in steps of 5° (19 angles total)
  For each alpha:
    - Create circuit
    - Run on AerSimulator with shots=10000
    - Compute correlation ⟨B·C⟩
    - Compute QM prediction: qm_singlet_expectation(0, alpha_rad)
    - Compute delta = measured − QM
    - Print: alpha, measured, QM_pred, delta
  Save results to: 09_ibm_quantum/results/processed/alpha_sweep_simulator.csv

SANITY CHECKS (run immediately after writing circuits):

CHECK-S1: α=90° (equatorial) → delta ≈ 0.000 (±0.02)
  Command: python k9e_alpha_sweep.py --alpha 90 --shots 10000
  Expected: delta between −0.02 and +0.02
  If FAIL: Circuit has equatorial geometry bug

CHECK-S2: α=0° → correlation ≈ −1.000 (±0.05)
  Command: python k9e_alpha_sweep.py --alpha 0 --shots 10000
  Expected: correlation between −1.05 and −0.95
  If FAIL: Singlet state preparation wrong

CHECK-S3: α=31° on simulator → delta ≈ 0.000 (expected — simulator = QM)
  Expected: |delta| < 0.02
  Note: This is CORRECT behavior. Simulator does not show K9_E.
  If delta is large: circuit logic wrong (not K9_E signal)

CHECK-S4: Born rule consistency across all angles
  K9_E predictor at beta=0 must match simulator output at each angle
  Max allowed discrepancy: 0.02 (statistical noise from 10000 shots)
  If FAIL: k9e_predictor.py is inconsistent with circuit definition

PRODUCE:
  (A) Complete code for both files
  (B) Sanity check results table: | Check | Expected | Actual | PASS/FAIL |
  (C) Alpha sweep CSV (first 5 rows shown)
  (D) Verdict: "Circuit validated — ready for IBM hardware submission"
               OR "Circuit failed check N — fix required"
```

**Save output as:** `09_ibm_quantum/governance/STEP2_circuit_validation.md`
**Save circuits as:** `09_ibm_quantum/circuits/k9e_base_circuit.py`
                     `09_ibm_quantum/circuits/k9e_alpha_sweep.py`

---

## STEP 3: K9E-PAT Circuit Design

**Goal:** Design circuits that test the 2BSM/1BSM suppression ratio.
This directly resolves K9E-PAT without relying on Proietti's 4-point noisy data.

```
TASK: K9E-PAT Resolution Circuit Design

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE STEP 2 VALIDATION REPORT HERE]

K9E-PAT states: K9_E multiplicative model predicts 2BSM/1BSM ratio ≈ 2.
Proietti data shows ratio = −0.78. IBM experiment will measure this ratio
directly with characterized noise.

CIRCUIT SPECIFICATION:

1-BSM circuit (k9e_1bsm_circuit.py):
  Description: Single Bell-state measurement step
  Qubits: q0 (Friend), q1 (Superobserver)
  Protocol:
    Prepare singlet state on (q0, q1)
    Friend q0 measures in Z-basis (1 BSM-equivalent interaction)
    Superobserver q1 measures at α=31°
  K_ctx size: 1 (one Friend registration)
  Expected K9_E suppression: f_perp × β = |cos(31°)| × 0.3 ≈ 0.257

2-BSM circuit (k9e_2bsm_circuit.py):
  Description: Two Bell-state measurement steps
  Qubits: q0 (Friend 1), q1 (Friend 2), q2 (Superobserver)
  Protocol:
    Prepare GHZ-analog state on (q0, q1, q2)
    Friend 1 (q0) measures in Z-basis (BSM step 1)
    Friend 2 (q1) measures in Z-basis (BSM step 2)
    Superobserver q2 measures at α=31°
  K_ctx size: 2 (two Friend registrations)
  Expected K9_E suppression: 2 × f_perp × β ≈ 0.514 (multiplicative model)
  Expected ratio: suppression_2BSM / suppression_1BSM ≈ 2.0

Control circuit (k9e_control_circuit.py):
  Description: α=90° (equatorial) — K9_E = QM exactly
  Purpose: Measure hardware noise floor
  Protocol: same as 1-BSM but α=90°
  Expected: delta = 0.000 (any nonzero = hardware noise)

WRITE ALL THREE FILES.

RATIO COMPUTATION:

def compute_k9e_pat_ratio(counts_1bsm, counts_2bsm, shots, alpha_deg=31.0):
    """
    Compute 2BSM/1BSM suppression ratio.
    K9_E multiplicative model predicts: ratio ≈ 2.0
    
    Returns:
        ratio: float (predicted ≈ 2.0 if K9_E correct)
        delta_1: suppression in 1BSM circuit
        delta_2: suppression in 2BSM circuit
        verdict: string interpretation
    """
    import sys, numpy as np
    sys.path.append('../../07_fits')
    from utils.qm_standard import qm_singlet_expectation

    corr_1 = compute_correlation(counts_1bsm, shots)
    corr_2 = compute_correlation(counts_2bsm, shots)
    
    alpha_rad = np.radians(alpha_deg)
    qm_pred = qm_singlet_expectation(0, alpha_rad)
    
    delta_1 = corr_1 - qm_pred
    delta_2 = corr_2 - qm_pred
    
    if abs(delta_1) < 0.005:
        return None, delta_1, delta_2, "delta_1 too small — noise dominated"
    
    ratio = delta_2 / delta_1
    
    if abs(ratio - 2.0) < 0.3:
        verdict = f"RATIO={ratio:.2f}: consistent with K9_E multiplicative model (~2.0)"
    elif ratio < 0:
        verdict = f"RATIO={ratio:.2f}: sign error — K9_E model incorrect for this regime"
    else:
        verdict = f"RATIO={ratio:.2f}: inconsistent with K9_E prediction (~2.0)"
    
    return ratio, delta_1, delta_2, verdict

SANITY CHECKS ON SIMULATOR:

CHECK-P1: Control (α=90°) → delta ≈ 0 on simulator
  If nonzero: state preparation wrong

CHECK-P2: 1-BSM (α=31°) → delta ≈ 0 on simulator (expected — simulator = QM)
  If nonzero: circuit logic wrong

CHECK-P3: 2-BSM (α=31°) → delta ≈ 0 on simulator (expected — simulator = QM)
  If nonzero: 3-qubit state preparation wrong

CHECK-P4: Ratio on simulator ≈ undefined or noise (expected — simulator = QM, both deltas ≈ 0)
  This is CORRECT. Ratio test only meaningful on real hardware.

PRODUCE:
  (A) Complete code for all three circuit files
  (B) Sanity check results (simulator)
  (C) Expected hardware results table:
      | Circuit | QM prediction | K9_E prediction | delta (predicted) |
  (D) Ratio interpretation guide:
      ratio ≈ 2.0 → K9_E multiplicative model confirmed
      ratio ≠ 2.0, ratio > 0 → K9_E needs different functional form
      ratio < 0 → K9_E model wrong sign in this regime → major revision
      |delta_1| < noise floor → K9E-PAT unresolvable at this N
```

**Save output as:** `09_ibm_quantum/governance/STEP3_k9e_pat_circuits.md`
**Save circuits as:** `09_ibm_quantum/circuits/k9e_1bsm_circuit.py`
                     `09_ibm_quantum/circuits/k9e_2bsm_circuit.py`
                     `09_ibm_quantum/circuits/k9e_control_circuit.py`

---

## STEP 4: IBM Account Setup and Job Submission

**Goal:** Connect to IBM Quantum, select backend, submit all circuits.
Session can close after this step — results retrieved later by Job ID.

**Access path:** Use Google Colab if quantum.ibm.com is geographically blocked.
Colab runs on Google servers — not subject to IBM geographic restrictions.

```
TASK: IBM Quantum Job Submission via Colab

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE STEP 2 AND STEP 3 VALIDATION REPORTS HERE]

Write a complete Google Colab notebook for IBM job submission.
The notebook must:
  1. Install packages
  2. Connect to IBM using saved token
  3. Select optimal backend
  4. Submit all circuits
  5. Save all Job IDs
  6. Print summary — then session can safely close

NOTEBOOK STRUCTURE (IBM_submit_jobs.ipynb):

Cell 1: Install
  !pip install qiskit qiskit-aer qiskit-ibm-runtime -q

Cell 2: Import and connect
  from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Options
  from qiskit import transpile
  import json

  TOKEN = "YOUR_IBM_TOKEN_HERE"  # Get from quantum.ibm.com
  service = QiskitRuntimeService(channel="ibm_quantum", token=TOKEN)
  print("Connected to IBM Quantum")
  print("Available backends:")
  for b in service.backends(operational=True, simulator=False):
      print(f"  {b.name}: {b.num_qubits} qubits, queue={b.status().pending_jobs}")

Cell 3: Select backend
  # Auto-select least busy with enough qubits
  backend_2q = service.least_busy(
      operational=True, simulator=False, min_num_qubits=2)
  backend_3q = service.least_busy(
      operational=True, simulator=False, min_num_qubits=3)
  print(f"2-qubit backend: {backend_2q.name}")
  print(f"3-qubit backend: {backend_3q.name}")

Cell 4: Load circuits
  import sys
  sys.path.append('/content/09_ibm_quantum/circuits')
  from k9e_base_circuit import create_ewf_circuit, compute_correlation
  from k9e_1bsm_circuit import create_1bsm_circuit
  from k9e_2bsm_circuit import create_2bsm_circuit
  from k9e_control_circuit import create_control_circuit

  circuits = {
      'control_alpha90':  create_control_circuit(alpha_deg=90.0),
      'base_alpha31':     create_ewf_circuit(alpha_deg=31.0),
      'base_alpha60':     create_ewf_circuit(alpha_deg=60.0),
      'base_alpha45':     create_ewf_circuit(alpha_deg=45.0),
      '1bsm_alpha31':     create_1bsm_circuit(alpha_deg=31.0),
      '2bsm_alpha31':     create_2bsm_circuit(alpha_deg=31.0),
  }

Cell 5: Submit jobs
  options = Options()
  options.resilience_level = 1  # basic error mitigation
  options.execution.shots = 10000

  job_registry = {}
  sampler_2q = Sampler(backend=backend_2q, options=options)
  sampler_3q = Sampler(backend=backend_3q, options=options)

  for name, circuit in circuits.items():
      sampler = sampler_3q if circuit.num_qubits == 3 else sampler_2q
      backend = backend_3q if circuit.num_qubits == 3 else backend_2q
      qc_t = transpile(circuit, backend, optimization_level=3)
      job = sampler.run(qc_t)
      job_registry[name] = {
          'job_id': job.job_id(),
          'backend': backend.name,
          'shots': 10000,
          'status': 'SUBMITTED'
      }
      print(f"Submitted {name}: {job.job_id()}")

Cell 6: Save and display Job IDs (CRITICAL — save before closing)
  print("\n" + "="*60)
  print("SAVE THESE JOB IDs BEFORE CLOSING SESSION")
  print("="*60)
  for name, info in job_registry.items():
      print(f"{name}: {info['job_id']}")
  
  # Save to file
  with open('IBM_job_registry_[DATE].json', 'w') as f:
      json.dump(job_registry, f, indent=2)
  print("\nSaved to IBM_job_registry_[DATE].json")
  print("Session can now be closed safely.")

ALSO WRITE: IBM_JOB_REGISTRY.md template

File location: 09_ibm_quantum/IBM_JOB_REGISTRY.md

Content:
  # IBM Job Registry
  # Update this file immediately after submitting jobs.
  # DO NOT close Colab without saving Job IDs here.
  
  | Name | Job ID | Backend | Shots | Submitted | Status | Retrieved |
  |---|---|---|---|---|---|---|
  | control_alpha90 | [job_id] | [backend] | 10000 | [date] | QUEUED | — |
  | base_alpha31 | [job_id] | [backend] | 10000 | [date] | QUEUED | — |
  | 1bsm_alpha31 | [job_id] | [backend] | 10000 | [date] | QUEUED | — |
  | 2bsm_alpha31 | [job_id] | [backend] | 10000 | [date] | QUEUED | — |

PRODUCE:
  (A) Complete Colab notebook code (all 6 cells)
  (B) IBM_JOB_REGISTRY.md template
  (C) Checklist before closing session:
      ☐ All Job IDs printed to screen
      ☐ Job IDs saved to IBM_JOB_REGISTRY.md
      ☐ JSON file downloaded from Colab
      ☐ Status shows SUBMITTED (not ERROR)
```

**Save output as:** `09_ibm_quantum/governance/STEP4_submission_notebook.md`
**Save notebook as:** `09_ibm_quantum/colab/IBM_submit_jobs.ipynb`

---

## STEP 5: Results Retrieval

**Goal:** Retrieve completed jobs by Job ID. Open a new Colab session — no need
to re-run circuits or re-submit. IBM stores results on their servers.

```
TASK: IBM Job Results Retrieval and Raw Data Processing

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE IBM_JOB_REGISTRY.md with actual Job IDs HERE]

Write a Colab notebook that retrieves results and saves raw data.
This notebook must work in a FRESH session — no dependency on previous session.

NOTEBOOK STRUCTURE (IBM_retrieve_results.ipynb):

Cell 1: Install and connect
  !pip install qiskit qiskit-ibm-runtime -q
  from qiskit_ibm_runtime import QiskitRuntimeService
  import json, numpy as np

  TOKEN = "YOUR_IBM_TOKEN_HERE"
  service = QiskitRuntimeService(channel="ibm_quantum", token=TOKEN)

Cell 2: Define Job IDs (paste from IBM_JOB_REGISTRY.md)
  JOB_IDS = {
      'control_alpha90': "PASTE_JOB_ID_HERE",
      'base_alpha31':    "PASTE_JOB_ID_HERE",
      'base_alpha60':    "PASTE_JOB_ID_HERE",
      'base_alpha45':    "PASTE_JOB_ID_HERE",
      '1bsm_alpha31':    "PASTE_JOB_ID_HERE",
      '2bsm_alpha31':    "PASTE_JOB_ID_HERE",
  }

Cell 3: Check status before retrieving
  for name, job_id in JOB_IDS.items():
      job = service.job(job_id)
      status = job.status()
      print(f"{name}: {status}")
  # Wait until all show: JobStatus.DONE
  # If QUEUED or RUNNING: check again later — do not force retrieve

Cell 4: Retrieve and save raw counts
  results = {}
  for name, job_id in JOB_IDS.items():
      job = service.job(job_id)
      if str(job.status()) != 'JobStatus.DONE':
          print(f"SKIP {name}: not done yet ({job.status()})")
          continue
      
      result = job.result()
      counts = dict(result.quasi_dists[0])
      results[name] = {
          'job_id': job_id,
          'counts': counts,
          'shots': sum(int(v * 10000) for v in counts.values()),
          'backend': job.backend().name
      }
      print(f"Retrieved {name}: {len(counts)} outcomes")
      
      # Save raw counts
      with open(f'results/raw/{job_id}_counts.json', 'w') as f:
          json.dump(results[name], f, indent=2)

Cell 5: Compute correlations
  import sys
  sys.path.append('/content/09_ibm_quantum/circuits')
  from k9e_base_circuit import compute_correlation
  sys.path.append('/content/07_fits')
  from utils.qm_standard import qm_singlet_expectation

  ANGLES = {
      'control_alpha90': 90.0,
      'base_alpha31': 31.0,
      'base_alpha60': 60.0,
      'base_alpha45': 45.0,
      '1bsm_alpha31': 31.0,
      '2bsm_alpha31': 31.0,
  }

  correlations = {}
  print(f"\n{'Circuit':<20} {'Alpha':>6} {'Measured':>10} {'QM pred':>10} {'delta':>8}")
  print("-" * 60)
  
  for name, data in results.items():
      alpha = ANGLES[name]
      corr = compute_correlation(data['counts'], 10000)
      qm = qm_singlet_expectation(0, np.radians(alpha))
      delta = corr - qm
      correlations[name] = {'alpha': alpha, 'measured': corr, 'qm': qm, 'delta': delta}
      print(f"{name:<20} {alpha:>6.1f} {corr:>10.4f} {qm:>10.4f} {delta:>8.4f}")

Cell 6: Save processed results
  import csv
  with open('results/processed/ibm_hardware_results.csv', 'w', newline='') as f:
      writer = csv.DictWriter(f, fieldnames=['circuit','alpha','measured','qm','delta'])
      writer.writeheader()
      for name, data in correlations.items():
          writer.writerow({'circuit': name, **data})
  print("Saved: results/processed/ibm_hardware_results.csv")

PRODUCE:
  (A) Complete Colab notebook code (all 6 cells)
  (B) Expected output format (example with placeholder numbers):
      Circuit              Alpha   Measured    QM pred    delta
      control_alpha90       90.0    -0.707     -0.707     0.000  ← noise floor
      base_alpha31          31.0    -0.XXX     -0.857     -0.0XX ← K9_E signal?
      1bsm_alpha31          31.0    -0.XXX     -0.857     -0.0XX
      2bsm_alpha31          31.0    -0.XXX     -0.857     -0.0XX
  (C) Decision rule:
      If |delta_control| > 0.03: hardware noise too high → flag, do not interpret other deltas
      If |delta_control| < 0.03: noise floor acceptable → proceed to Step 6 analysis
```

**Save output as:** `09_ibm_quantum/governance/STEP5_retrieval_notebook.md`
**Save notebook as:** `09_ibm_quantum/colab/IBM_retrieve_results.ipynb`

---

## STEP 6: Noise Analysis and K9E-PAT Resolution

**Goal:** Distinguish K9_E signal from hardware noise. Compute K9E-PAT ratio.
Produce final verdict.

```
TASK: Noise Analysis and K9E-PAT Resolution

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE ibm_hardware_results.csv content HERE]

[PASTE control_alpha90 delta value HERE]

Analyze whether the IBM hardware results support, falsify, or are inconclusive
for K9_E. Resolve K9E-PAT by computing the 2BSM/1BSM ratio.

PART 1: NOISE FLOOR ASSESSMENT

Control circuit (α=90°) gives delta_control.
This is hardware noise — K9_E predicts exactly 0 at α=90° (Universal Theorem).

Noise threshold:
  If |delta_control| < 0.02: noise floor ACCEPTABLE
  If 0.02 ≤ |delta_control| < 0.05: MARGINAL — note in report, proceed with caution
  If |delta_control| ≥ 0.05: noise floor TOO HIGH — results unreliable
                               Recommend: switch to less noisy backend or increase shots

PART 2: ALPHA-DEPENDENCE TEST

K9_E predicts: delta(α) = −β · |cos(α)| · QM_correlation(α)
Noise predicts: delta(α) = constant (random, no α-dependence)

Fit both models to (alpha_31, alpha_45, alpha_60) data points:
  Model K9_E: delta = −β · |cos(α)| · ⟨A·B⟩_QM(α)   [1 free param: β]
  Model NOISE: delta = c                                [1 free param: c]

Compare chi-squared:
  Δχ² = χ²_noise − χ²_K9E
  If Δχ² > 9.0 (3σ): K9_E model preferred
  If Δχ² < 9.0: inconclusive
  If Δχ² < 0: noise model preferred → K9_E disfavored

Report:
  β_fit (best-fit suppression parameter)
  Δχ² value
  Verdict: SUPPORTED / INCONCLUSIVE / DISFAVORED

PART 3: K9E-PAT RATIO COMPUTATION

From 1BSM and 2BSM circuits at α=31°:
  delta_1 = corr_1bsm − QM_prediction
  delta_2 = corr_2bsm − QM_prediction
  ratio = delta_2 / delta_1

Interpretation:
  ratio ≈ 2.0 (±0.4): K9_E multiplicative model CONFIRMED
  ratio > 0, ≠ 2.0:   K9_E needs different functional form
  ratio < 0:           K9_E model WRONG SIGN — major structural revision needed
  |delta_1| < noise:   UNRESOLVABLE at current N — recommend 10× shots

PART 4: PRODUCE FINAL VERDICT DOCUMENT

Write: 09_ibm_quantum/analysis/k9e_pat_resolution.md

Sections:
  1. Noise floor: [value] → ACCEPTABLE / MARGINAL / TOO HIGH
  2. Alpha-dependence: Δχ² = [value] → K9_E SUPPORTED / INCONCLUSIVE / DISFAVORED
  3. K9E-PAT ratio: [value] → CONFIRMED / WRONG FORM / WRONG SIGN / UNRESOLVABLE
  4. Overall verdict (one of):
     A: "K9_E signal detected. β_fit=[value]. K9E-PAT resolved: ratio=[value]."
     B: "K9_E inconclusive. Noise floor acceptable but signal below threshold.
         Recommend: increase shots to N=[estimate]."
     C: "K9_E disfavored in this regime. K9E-PAT ratio=[value] contradicts
         multiplicative model. Recommend: revise K9_E functional form."
     D: "Hardware noise too high for meaningful analysis.
         Recommend: switch backend or use error mitigation level 2."
  5. Next step: (derived from verdict A/B/C/D)
```

**Save output as:** `09_ibm_quantum/analysis/k9e_pat_resolution.md`
                   `09_ibm_quantum/analysis/noise_characterization.py`

---

## DECISION GATES

```
GATE 0: After Step 0
  ALL prerequisites AVAILABLE → proceed to Step 1
  ANY prerequisite MISSING → resolve first

GATE 1: After Step 1
  All 5 commands PASS → proceed to Step 2
  Any command FAIL → fix environment, re-run

GATE 2: After Step 2
  Checks S1, S2, S3, S4 all PASS → proceed to Step 3
  Any FAIL → fix circuit, re-run

GATE 3: After Step 3
  Checks P1, P2, P3 all PASS → proceed to Step 4
  Any FAIL → fix circuit, re-run
  Note: Check P4 always passes (simulator = QM)

GATE 4: After Step 5 retrieval
  |delta_control| < 0.05 → proceed to Step 6
  |delta_control| ≥ 0.05 → switch backend or increase shots → re-submit

GATE 5: After Step 6 verdict
  Verdict A: → write paper (K9-S12 Modified Bong proposal)
  Verdict B: → increase N to recommended value → re-submit
  Verdict C: → revise K9_E functional form → new K9 analysis sprint
  Verdict D: → switch to less noisy backend → re-submit
```

---

## JOB SUBMISSION MODEL

IBM Quantum does NOT require Colab to stay open after submission.

```
Workflow:
  Step 4: Open Colab → submit jobs → SAVE JOB IDs → close Colab
               ↓
          IBM queue runs jobs (minutes to hours)
               ↓
  Step 5: Open NEW Colab → paste Job IDs → retrieve results → close
               ↓
  Step 6: Run analysis locally (no internet needed)

Check job status without Colab:
  quantum.ibm.com → Jobs → find by Job ID → check status field
```

---

## EXECUTION NOTES

**Local simulator is sufficient for Steps 0-3.** No IBM account needed.
All sanity checks run on AerSimulator. Real hardware only needed for Steps 4-6.

**Geographic access:** If quantum.ibm.com is blocked:
  1. Use VPN to register account and get API token (one time only)
  2. Save token string locally
  3. Use Google Colab for all subsequent sessions (Colab is not blocked)
  4. Token works from Colab regardless of local geographic restrictions

**Session safety:** After Step 4 submission, save Job IDs in THREE places:
  1. IBM_JOB_REGISTRY.md in repository
  2. Local text file or note
  3. quantum.ibm.com Jobs page (IBM stores these permanently)

**Estimated timeline:**
  Steps 0-3 (local, no account): 2-3 sessions
  Step 4 (submission): 1 session (30 minutes active)
  IBM queue wait: 30 minutes to 6 hours (variable)
  Step 5 (retrieval): 1 session (15 minutes)
  Step 6 (analysis): 1-2 sessions

**LLM recommendation:** Use Claude Opus or GPT-4 class models for Steps 0, 2, 3, 6
(require reasoning). Use any model for Steps 4-5 (primarily code execution).
For Step 6, run in a fresh session with adversarial framing to avoid confirmation bias.
