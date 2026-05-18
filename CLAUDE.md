Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# CLAUDE.md

## RULE ZERO — Root Cause Analysis (RCA)

**This is the highest mandatory rule, applied to every activity: research planning, literature review, conceptual mapping, documentation, critique, revision, and publication preparation.**

Never treat a symptom, ambiguity, or attractive analogy as the conclusion. Always trace the observed issue, claim, or mismatch back to its root cause before acting.

### Five-step process

1. **Define** — Describe the observed issue precisely. Separate the *symptom* (what appears in the text, argument, mapping, citation, or structure) from the *cause* (the assumption, source gap, conceptual mismatch, or methodological error that produced it).
2. **Trace** — Follow the causal chain backward by asking: "What made this issue appear?" Repeat at least three times using the "5 Whys" method.
3. **Isolate** — Identify the starting point of the failure: an unsupported claim, weak citation, ambiguous term, broken mapping, category error, outdated source, missing definition, or structural inconsistency. If it is not isolated, do not revise yet.
4. **Fix the cause, not the symptom** — Correct the root cause directly. Do not patch prose, soften wording, add a vague caveat, or create a workaround unless it is explicitly marked as `TODO(HOTFIX)`.
5. **Verify** — Show that the root cause has been removed, not merely that the visible symptom disappeared. When possible, verify against the source text, the active mapping files, the published node/edge definitions, and the research objective.

### Activity-specific application

| Activity | RCA requirement |
|----------|-----------------|
| **Research planning** | Ask "Why is this research question necessary?" before "How should it be written?" Identify the real problem behind the requested document or section. |
| **Literature review** | Trace every major claim to a source, and distinguish established scholarship from interpretation, analogy, or hypothesis. |
| **Conceptual mapping** | Understand why each concept exists in its original system before mapping it across systems. Treat cross-domain links as analogies unless equivalence is explicitly justified. |
| **Documentation** | Find what caused confusion before rewriting. Fix the structure, terminology, missing definition, or broken reference, not only the sentence that looks unclear. |
| **Review** | Classify every finding as either symptom or root cause. A blocking issue must identify the root cause; a surface-level wording issue is only a documentation bug. |
| **Revision** | Identify what is truly causing complexity or inconsistency before simplifying, reorganizing, or abstracting. Do not create structure around a symptom. |

### Example

```text
Symptom: A section claims Buddhist Epistemology "solves" Quantum Measurement.
  → Why? The wording treats a philosophical mapping as a physical explanation.
    → Why? The document does not separate analogy, interpretation, and prediction.
      → Why? The claim lacks a formal boundary between ontology and physics.
        → Root cause: Category error between epistemological interpretation and empirical physical theory.
          → Fix: Reframe the section as an interpretive mapping unless formal proof, peer review, physical predictions, and experimental tests are supplied.
```

### Warnings

- If the revision only changes the sentence where the symptom appears, it is **not enough**; return to step 2.
- If the root cause cannot be explained in one sentence, understanding is **not complete**; return to step 1.
- If the fix only adds a vague caveat, fallback phrase, or defensive wording, it is **treating the symptom**; return to step 4.

## Core Principles

### Identity and scope rules

- VVV-QMRF stands for "VietVunVut Quantum Measurement Registration Framework". Legacy name: "VietVunVut Epistemic Quantum Measurement (VVV-EQM)". Definition: Standard Quantum Mechanics has four physical postulates (P1–P4) that describe state space, observables, measurement, and dynamics. These postulates are silent on the registration architecture of measurement — they do not specify what certifies a measurement, what distinguishes measurement from interaction, or what constitutes the registering system. VVV-QMRF fills these gaps by adding 16 registration-layer postulates derived from structural analysis of Buddhist Pramāṇa epistemology (Dignāga–Dharmakīrti tradition). The first 7 (E1–E7) define core registration operations; the remaining 9 (E8–E16) extend the framework to cover retroactive invalidation, null events, validity conditions, contrapositive evidence, transcendental observation, temporal discontinuity, absence cognition, entanglement relations, and pre-measurement indeterminacy.
- Use Buddhist Epistemology as the primary ontological frame and map Quantum Measurement onto it only within the project’s declared Quantum Measurement cases; report any content that exceeds Buddhist Epistemology scope or treats a mapping as Standard Quantum Mechanics.
- For RCA on Buddhist Epistemology node and edge definitions, use only `SYSTEM_Buddhist_Epistemology/system_be_full.md` as the single source of truth; treat other BE node/edge tables as derived references.

### Document contract rules

- Use bilingual English/Vietnamese where appropriate across project documents; keep technical terminology, formal claims, and publication-facing text in technically precise English; communicate with the user in Vietnamese, keep English technical terms inside quotation marks, and explain concepts at a high-school level.
- Apply the mandatory principle "extend, not overwrite": when revising project documents, preserve existing valid structure, claims, terminology, citations, mappings, and author intent unless the user explicitly requests replacement; add, refine, or qualify content by extending the existing document contract rather than overwriting it.
- Before creating or editing project files, check whether the file path is inside any folder named `public_documents` or `published_documents` anywhere in the repository. If it is inside either folder, do not add VVV-QMRF author metadata, VVV-QMRF author names, or project-author attribution. If it is outside those folders and the file does not already start with author metadata, add this author metadata at the top: Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet.
- When creating any new VVV-QMRF research or educational document, follow `documents/research_documents/vvv-qmrf/schema_guide.md` as the document-creation contract for source hierarchy, claim class, boundaries, traceability, and verification rules.
- Avoid negatively evaluative wording such as "logical fallacy", "Classical analogy mistake", "mistake", "wrong", "false", or "error" when explaining Standard Quantum Mechanics, educational analogies, or VVV-QMRF boundaries. Prefer neutral boundary language such as "category boundary", "scope boundary", "interpretive boundary", "not implied by this analogy", or "registration-layer distinction"; especially do not frame Standard Quantum Mechanics as logically defective.

### Terminology rules

- Name each new Quantum Measurement concept node as BIAN-XX, where XX ranges from 01 to 99; here, BIAN derives from the Vietnamese word "bí ẩn", meaning "mystery" in English.
- Use five-digit Buddhist Epistemology node and edge codes consistently: N_BE_00001, N_BE_00002, ... N_BE_00030; ED_BE_00001, ED_BE_00002, ... ED_BE_00039; do not use older shorter forms.
- In VVV-QMRF terminology, use "registration-state update" / "cập nhật trạng thái ghi nhận" for the general K-side update beyond human cognition; use "detector response" only for the apparatus' physical response.

### Specialized execution rules

- Use the project skill `/rca-scientific-paper` only for scientific paper documents (`scientific paper`) when planning, reviewing, or revising scientific paper claims.

This file provides guidance to Claude Code when working in this project.

## Project context

This project maps relationships between Buddhist epistemology (Pramāṇavāda — Dignāga and Dharmakīrti) and quantum measurement. It uses a formal node/edge graph structure with 30 nodes (N_BE_00001–N_BE_00030) and 39 edges (ED_BE_00001–ED_BE_00039).

## Active mapping files

| File | Role |
|------|------|
| `SYSTEM_Buddhist_Epistemology/system_be_full.md` | Single source of truth for Buddhist Epistemology node and edge definitions used in RCA. |
| `SYSTEM_Buddhist_Epistemology/system_buddhist_epistemology.md` | Compact derived key concepts table for the 30 core BE nodes. |
| `documents/published_documents/node_pub_doc_Buddhist_Epistemology.md` | Published compact derived node definitions (30 core nodes). |
| `documents/published_documents/edge_pub_doc_Buddhist_Epistemology.md` | Published compact derived edge definitions (39 core edges). |
| `documents/research_documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_refine_mapping.md` | Primary deep-analysis BE-QM mapping that applies the BE SOT. |
| `documents/research_documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md` | Formal BE-QM system mapping that applies BE node/edge codes from the BE SOT. |

Archived (superseded): `documents/research_documents/achives/`

## Working guidelines

- Preserve conceptual nuance between Buddhist philosophy, epistemology, and quantum physics.
- Treat cross-domain links as analogies or mappings unless the text explicitly argues for equivalence.
- Prefer clear Markdown structure with descriptive headings and concise paragraphs.
- Keep terminology consistent across English and Vietnamese when bilingual wording is used.
- Do not invent citations, sources, or historical claims; mark uncertain claims clearly.
- When editing mapping files, preserve existing conceptual nodes and relationships unless asked to restructure them.
- Maintain node/edge codes (N_BE_XX, ED_BE_XX) consistently between files.
- Update both `refine_mapping.md` and `system_mapping.md` when structural changes affect both.

## Terminology

- Node: concept / khái niệm / nút (code: N_BE_XX)
- Edge: relationship / mối quan hệ / liên kết (code: ED_BE_XX)
- Directed edge: directed relationship / quan hệ có hướng
- BIAN: Buddhist Insight with No Analogue — a concept present in Buddhist Epistemology with no QM equivalent

# Research Guidelines: Buddhist Epistemology & Quantum Mechanics

## 1. Karpathy Principles (Mandatory Compliance)
- **Think Before Acting:** DO NOT make assumptions about theoretical concepts (e.g., do not hallucinate or guess the meaning of 'Pramaana'). If context or information is missing, you must ask for clarification.
- **Simplicity First:** Apply strict 1:1 logical mappings. Do not generate lengthy, verbose philosophical analyses if only a structural mapping is requested.
- **Surgical Changes:** When asked to update the mapping file, ONLY modify the exact node/section specified. Do not reformat, restructure, or touch the rest of the document.
- **Goal-Driven Execution:** Always state your plan and verify before executing. For example: "Found X. I am about to map it to Y. Do you approve?"

## 2. Logic Function Rules (Project-Specific Rules)
This environment operates based on simulated logic commands (functions). When the user inputs a command, process it strictly according to the following rules:

- **Trigger:** If the user inputs a command in the format: 
  `base [System_A], mapping find [node, System_B]`
- **Required AI Actions:**
  1. Read the current working document (`Buddhist_Epistemology_and_Quantum_Measurement_refine_mapping.md` or `Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md`).
  2. Establish `System_A` as the Ground System (primary reference frame).
  3. Search for the structurally equivalent concept (node) within `System_B`.
  4. Output the result using this exact strict format: 
     `[Node_A] <=> [Node_B] : [Brief_structural_reasoning]`
