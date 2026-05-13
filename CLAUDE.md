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

- Use bilingual English/Vietnamese where appropriate across project documents; keep technical terminology, formal claims, and publication-facing text in technically precise English.
- Before creating or editing project files outside `documents/published_documents/`, check whether the file already starts with author metadata; if it does not, add this author metadata at the top: Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet
- Do not add author metadata or author names to files under `documents/published_documents/`.
- Name each new Quantum Measurement concept node as BIAN-XX, where XX ranges from 01 to 99; here, BIAN derives from the Vietnamese word "bí ẩn", meaning "mystery" in English.
- Use five-digit Buddhist Epistemology node codes consistently: N_BE_00001, N_BE_00002, ... N_BE_00030; do not use older shorter forms.
- Use five-digit Buddhist Epistemology edge codes consistently: ED_BE_00001, ED_BE_00002, ... ED_BE_00039; do not use older shorter forms.
- Communicate with the user in Vietnamese; keep technical terms in English inside quotation marks (for example, "cat") and explain concepts at a high-school level.
- In VVV-EQM terminology, use "registration-state update" / "cập nhật trạng thái ghi nhận" for the general K-side update beyond human cognition; use "detector response" only for the apparatus' physical response.
- Method: Buddhist Epistemology as primary ontological frame; Quantum Measurement mapped onto it.
- All information must remain within the scope of Buddhist Epistemology, except for Quantum Measurement cases listed in the Quantum Measurement published documents table below; report any violation immediately.
- Think before acting.
- Use the project skill `/rca-scientific-paper` only for scientific paper documents (`scientific paper`) when planning, reviewing, or revising scientific paper claims.
- Keep mappings structurally simple.
- Make surgical changes only.
- Ask for clarification when concepts are ambiguous.

This file provides guidance to Claude Code when working in this project.

## Project context

This project maps relationships between Buddhist epistemology (Pramāṇavāda — Dignāga and Dharmakīrti) and quantum measurement. It uses a formal node/edge graph structure with 30 nodes (N_BE_00001–N_BE_00030) and 39 edges (ED_BE_00001–ED_BE_00039).

## Active mapping files

| File | Role |
|------|------|
| `documents/research_documents/Buddhist_Epistemology_and_Quantum_Measurement_refine_mapping.md` | Primary deep-analysis mapping (52 concepts, 6 tiers, 20 BIANs). Most thorough QM/philosophical analysis. |
| `documents/research_documents/Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md` | Formal system mapping with node/edge codes, definitions from published docs, and full QM depth. Single source of truth for graph structure. |
| `documents/published_documents/node_pub_doc_Buddhist_Epistemology.md` | Published node definitions (30 nodes). |
| `documents/published_documents/edge_pub_doc_Buddhist_Epistemology.md` | Published edge definitions (39 edges). |
| `SYSTEM_Buddhist_Epistemology/system_buddhist_epistemology.md` | Key concepts reference table. |

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
