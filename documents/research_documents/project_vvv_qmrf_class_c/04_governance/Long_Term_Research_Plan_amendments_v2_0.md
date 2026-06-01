Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Long-Term Research Plan — Amendments v2.0
**Base plan:** `Long_Term_Research_Plan_2026_05_31.md` (v1.0, RCA 4.69/5)
**Amendment date:** 2026-06-01
**Method:** Meta-review RCA (Feasibility × Risk × Complexity × Trade-off)
**Meta-review score:** 4.08/5 PASS — 6 amendments identified, all additive (no structural change)
**Status:** AMENDMENTS ONLY — v1.0 base plan preserved unchanged

> These amendments are additive. They do not overwrite any v1.0 claim, pillar, phase, or decision. They patch operational gaps and strengthen risk mitigation.

---

## SUMMARY TABLE — v1.0 → v2.0 Changes

| # | Amendment | Affects | Type | Priority |
|---|-----------|---------|------|----------|
| A1 | Thêm Gate 0.5 — arXiv confirmation | Phase 1 entry gate | Operational gap | HIGH |
| A2 | Cụ thể hóa lab outreach strategy | Phase 2 → II.2 | Risk mitigation | HIGH |
| A3 | Thêm Position Paper (intermediate output) | Phase 2 → new III.2b | Scope extension | MEDIUM |
| A4 | Thêm funding path note cho Phase 3A | Phase 3 prerequisites | Risk mitigation | HIGH |
| A5 | AHP re-audit như gate condition | Gates 1–4 | Process compliance | MEDIUM |
| A6 | Cụ thể hóa monograph scope | Phase 5 → III.5 | Scope clarification | LOW |

---

## A1 — Gate 0.5: arXiv Confirmation (INSERT before Phase 1)

**Gap identified (5-Why):**
```
Symptom: Plan giả định K9-S12 paper "đã submitted arXiv" nhưng không track status.
  → W1: arXiv moderation có thể HOLD hoặc REJECT non-standard physics papers.
  → W2: Labs cần đọc paper TRƯỚC khi respond outreach email.
  → W3: Nếu paper bị hold, toàn bộ lab outreach strategy bị block.
  → Root cause: Thiếu Gate 0.5 để confirm paper actually publicly accessible.
```

**Amendment — INSERT after GATE 0 trong §3.3:**

```
GATE 0.5 (BEFORE Phase 1 entry):
  ├── K9-S12 paper confirmed publicly accessible on arXiv ✅
  ├── arXiv identifier recorded (arXiv:XXXX.XXXXX)
  ├── Paper DOI or permanent URL noted for lab outreach use
  └── IF moderation block:
      ├── Identify moderation reason (cross-list / content issue)
      ├── Resolve (revise abstract/classification if needed)
      └── Re-confirm, THEN enter Phase 1

Note: Gate 0.5 does NOT block Phase 1 documentation work (I.1, III.1).
      It blocks ONLY II.2 lab outreach start in Phase 2.
```

---

## A2 — Lab Outreach Strategy (REPLACE II.2 Activities section in Phase 2)

**Gap identified (5-Why):**
```
Symptom: II.2 chỉ nói "identify 3-5 optical EWF labs worldwide."
  → W1: EWF optical labs là cực kỳ hiếm (<10 worldwide in 2026).
  → W2: Cold email với 1-page summary → response rate ~0-5%.
  → W3: Không có warm-up path, không có criteria chọn lab.
  → Root cause: Outreach là deliverable format, không phải strategy.
```

**Amendment — REPLACE Activities in §II.2:**

```
II.2 — Lab Outreach Strategy (REVISED)

STEP 1: Lab identification (by 2026-10-15)
  Target pool (start here — không cold email other labs first):
  - Vienna: Zeilinger group / Aspelmeyer group (EWF optical expertise confirmed)
  - Geneva: Gisin group (Bell test optical — adjacent to EWF)
  - Delft: Hanson group (solid-state EWF — alternative platform)
  - Innsbruck: Blatt/Roos group (ion-trap EWF — alternative platform)
  - Add: any lab that cited Bong et al. 2020 or Proietti et al. 2019 in 2024-2026 papers

  Criteria for shortlisting:
    (a) Published EWF or entanglement-swap optical experiment in last 3 years
    (b) Group size ≥ 3 PhD/postdoc (capacity for side experiment)
    (c) Open to theory-driven experimental proposals

STEP 2: Warm-up path (2026-10-15 → 2026-11-30)
  Preferred order (not cold email first):
  1. Conference / workshop: submit poster abstract to nearest foundations of QM
     conference (FQXI, Quantum Information conferences, etc.)
  2. Online preprint visibility: share arXiv paper on PhilSci + tag relevant researchers
  3. Email via mutual connection if possible (cite shared paper in email)
  4. Direct email ONLY if no mutual connection found after step 1-3

STEP 3: Outreach package
  - 1-page experimental summary (non-technical, feasibility-focused)
  - Full K9-S12 paper (arXiv link — requires Gate 0.5 to be PASS)
  - Explicit statement: "This is a testable prediction, not a theory paper"
  - Offer: collaboration credit, co-authorship on experimental paper

STEP 4: Response tracking (ongoing until 2026-12-31)
  Track: sent / no-response (>4 weeks) / negative / positive / in-discussion

CONTINGENCY (if no positive response by 2026-12-31):
  - Trigger Phase 3B (theory-only track) as planned
  - ADD: Consider quantum simulation approach — contact quantum computing groups
    (IBM Research, Google Quantum AI) about simulating K9_E predictions on
    entanglement witnesses (not full optical EWF, but proxy test)
  - Document outreach attempt record for future grant applications
```

---

## A3 — Position Paper (NEW deliverable III.2b in Phase 2)

**Gap identified:**
```
Symptom: 15-month gap in public output (paper_002 submitted 2026-05-27 → paper_003/004 in 2027-H2).
  → Risk: Research momentum loss, low arXiv visibility, harder lab outreach.
  → Root cause: Plan nhảy thẳng từ K9-S12 paper sang Phase 4 papers.
  → Fix: One intermediate output that requires no new experimental data.
```

**Amendment — ADD III.2b in Phase 2:**

```
III.2b — Position Paper: "VVV-QMRF Status and Open Problems" (NEW)

Deliverable: papers/position_paper_2026/draft.md → arXiv + PhilSci Archive

Scope:
  - Length: 8-12 pages
  - Type: systematic review / position paper (not new results)
  - Content: Current status of K1-K8, φ-map, K9_E; open problems; experimental path
  - Key section: "Why K9-S12 is the decisive test" (doubles as lab outreach support)

Acceptance criteria:
  - [ ] All claims reference existing documents (no new unverified claims)
  - [ ] K≠H boundary explicitly stated
  - [ ] Open problems listed as open (not solved)
  - [ ] AHP check: no [AH-CRIT] in new text
  - [ ] RCA review: ≥ 4/5

Target submission: 2026-11-30 (concurrent with lab outreach)
Target venue: PhilSci Archive (immediate) → Foundations of Physics Letters (optional)

Note: This paper supports lab outreach — labs can cite it when discussing
      collaboration feasibility. It is NOT paper_003 and does NOT replace it.
```

---

## A4 — Phase 3A Funding Path (ADD to Phase 3A prerequisites)

**Gap identified:**
```
Symptom: Phase 3A prerequisites: "Funding (if needed)" — vague.
  → Optical EWF experiments cost $50K–$500K USD.
  → "If needed" không phải risk mitigation.
  → Root cause: Plan tránh discuss funding uncertainty.
```

**Amendment — ADD funding path note to Phase 3A:**

```
II.3A FUNDING PATH (ADD as sub-section in Phase 3A):

Three viable funding structures (in order of likelihood):

  Option A — Lab self-funded collaboration (most likely for initial run):
    VVV-QMRF = theoretical collaborator, NOT funder
    Lab uses existing equipment + personnel budget
    Feasible for: small-scale pilot run (N=10,000–50,000) to test protocol
    Cost to VVV-QMRF side: 0 (theoretical contribution = in-kind)

  Option B — Co-PI on lab's existing grant:
    If lab has active optical quantum grant, K9-S12 can be added as sub-aim
    Requires: lab PI's initiative; VVV-QMRF provides protocol + theory
    Timeline: grant amendment → typically 3-6 months

  Option C — Independent small grant (fallback):
    If no lab has capacity, apply to foundations:
    - John Templeton Foundation (physics-philosophy interface — GOOD FIT)
    - FQXi (Foundational Questions Institute) — directly relevant
    - National science foundation of Vietnam (VinIF) — accessible to VVV author
    Timeline: application → 12-18 months typically

GATE 2.5 (INSERT between Gate 2 and Phase 3A start):
  ├── Lab collaboration agreement drafted OR
  ├── Funding pathway explicitly chosen (A/B/C above) ✅
  └── IF neither → trigger Phase 3B
```

---

## A5 — AHP Gate Condition (ADD to Gates 1–4)

**Gap identified:**
```
Symptom: CLAUDE.md mandates AHP re-audit after each Phase.
         No Gate condition currently enforces this.
  → Root cause: AHP là cross-cutting rule nhưng không được operationalized trong gates.
```

**Amendment — ADD to EACH of Gates 1, 2, 3, 4:**

```
[INSERT into each gate's condition list]:
  ├── AHP top-10 re-audited: no [AH-CRIT] (score 9-10) components ✅
  └── IF [AH-CRIT] found: resolve before gate PASS declared
```

Gate 1 (Phase 1 end): AHP audit covers I.1 (boundary theorem) + III.1 (composition framework)
Gate 2 (Phase 2 end): AHP audit covers I.2 (restricted existence) + III.2 (motivation chain) + III.2b (position paper)
Gate 3 (Phase 3 end): AHP audit covers all new claims in WP v4.0 or experimental data interpretation
Gate 4 (Phase 4 end): AHP audit covers ALL papers before submission

---

## A6 — Monograph Scope Clarification (REPLACE III.5 Deliverable note in Phase 5)

**Gap identified:**
```
Symptom: III.5 monograph spec: "Complete exposition... ~4 parts."
         No target length, publisher path, or trigger condition.
  → Risk: Monograph becomes open-ended indefinite project.
  → Fix: Scope it concretely.
```

**Amendment — ADD to III.5:**

```
III.5 — Monograph (SCOPED)

Target spec:
  - Length: 200–300 pages (4 parts × 50-75 pages each)
  - Audience: Philosophers of physics, Foundations of QM researchers
  - Language: English (technical); Vietnamese preface (contextual)

Publisher path (in order of preference):
  1. Springer Briefs in Physics (50-125pp — if scoped down to brief)
  2. Open Access preprint → monograph (arXiv + Zenodo)
  3. Conventional press (only if peer-reviewed papers already accepted)

TRIGGER: Begin monograph work ONLY AFTER:
  - Phase 4 papers submitted (paper_003 + paper_004) ✅
  - arXiv confirmation for both papers ✅
  - NOT concurrent with Phase 4 work (sequential, not parallel)

ANTI-SCOPE-CREEP rule:
  Parts I–III use EXISTING documents (axioms, φ-map, K9_E papers) as primary source.
  Part IV (philosophical implications) is the ONLY genuinely new writing required.
  Total new writing: ~50-75 pages.
```

---

## AMENDED RESOURCE ESTIMATE

| Phase | Duration | Sessions (v1.0 est.) | Sessions (v2.0 est.) | Delta |
|-------|----------|---------------------|---------------------|-------|
| Phase 1 | 3 months | 6-9 | 6-9 | No change |
| Phase 2 | 3 months | 6-9 | 8-12 | +2-3 (position paper III.2b) |
| Phase 3 | 6 months | 9-15 | 9-15 | No change (A4 is administrative) |
| Phase 4 | 6 months | 9-15 | 9-15 | No change |
| Phase 5 | Open-ended | TBD | TBD | Scoped better but open |
| **Total (Ph 1-4)** | **18 months** | **30-48** | **32-51** | **+2-3 sessions total** |

Cost of amendments: **+2-3 sessions** for position paper. All other amendments are administrative (zero execution cost).

---

## AMENDED RISK MATRIX (v2.0)

| Risk | v1.0 Mitigation | v2.0 Mitigation | Residual risk |
|------|----------------|----------------|---------------|
| arXiv moderation block | None | Gate 0.5 added | LOW |
| Lab cold outreach fails | Theory-only contingency | Warm-up strategy + quantum simulation fallback | MEDIUM |
| 15-month output gap | None | Position paper III.2b | LOW |
| Funding for Phase 3A | "If needed" | 3 options A/B/C + Gate 2.5 | MEDIUM (external) |
| AHP drift between phases | Cross-cutting rule only | Gate condition mandatory | LOW |
| Monograph scope creep | None | Trigger condition + 50-75pp new writing only | LOW |

---

## WHAT DID NOT CHANGE (v1.0 fully preserved)

- **3-Pillar structure** (φ-map / K9_E / Integration) — unchanged
- **5-Phase sequence** — unchanged (Gate 0.5 adds before Phase 1, not a new phase)
- **RCA method** (3-Round × 5-Why × 4/5) — unchanged
- **ERR ON TYPE II principle** — unchanged
- **φ-map characterization strategy** (boundary = research result) — unchanged
- **K9_E blocked-on-experiment diagnosis** — unchanged
- **EX compass rules** — unchanged
- **K≠H boundary** — unchanged
- **All CLAUDE.md cross-cutting rules** — unchanged
- **All v1.0 Gate conditions** (A5 only ADDS to them, does not replace)

---

## BLOCKER STATUS (2026-06-01)

| Blocker | Description | Status |
|---------|-------------|--------|
| B0 | v2.0 amendments untracked (git violation) | **RESOLVED** — committed 2026-06-01 (15c3e82) |
| B1 | Gate 0.5 — arXiv accessibility not confirmed | **PENDING** — awaiting arXiv ID for K9-S12 paper |
| B2 | External lab dependency (Phase 3A) | **PENDING** — outreach plan defined (A2); execution starts Phase 2 |
| B3 | Plan approval Gate 0 not recorded | **RESOLVED** — Gate 0 approved 2026-06-01 by user (Viet); v1.0 → v1.1 |
| B4 | AHP gate conditions not operationalized | **RESOLVED** — A5 in force (committed 15c3e82) |
| B5 | φ-map sufficiency fundamental boundary | **MANAGED** — boundary theorem I.1 scheduled Phase 1 |
| B6 | Funding Phase 3A vague | **MANAGED** — 3 options A/B/C defined (A4); Gate 2.5 added |

---

## CHANGE LOG

| Date | Version | Change |
|------|---------|--------|
| 2026-05-31 | 1.0 | Initial plan. 3-Round RCA (aggregate 4.69/5). Base plan. |
| 2026-06-01 | 2.0 | 6 amendments (A1-A6). Meta-review score 4.08/5. Additive only. No structural change to v1.0. |
| 2026-06-01 | 2.1 | Blocker status table added. B0/B3/B4 → RESOLVED; B1/B2 → PENDING; B5/B6 → MANAGED. |

---

*Long-Term Research Plan Amendments v2.0 — 2026-06-01.*
*To be read alongside v1.0 base plan (`Long_Term_Research_Plan_2026_05_31.md`).*
*Apply amendments by inserting/replacing the indicated sections when v1.0 is next opened for editing.*
