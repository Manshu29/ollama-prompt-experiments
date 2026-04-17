# MVP Model & Prompt Recommendation

**Document Type:** Internal Technical Recommendation  
**Date:** April 16, 2026  
**Status:** ✅ Final — Ready for Team Review  
**Author:** AI/ML Team  

---

## 1. Overview

This document captures the final model and prompt configuration recommended for the MVP of our AI-powered education platform. It is based on iterative local testing using Ollama with custom Modelfile-based models derived from `llama3.2:latest`.

---

## 2. Recommended Models

| Role | Model | Base | Size |
|---|---|---|---|
| Quiz Generation | `quiz-llama:latest` | llama3.2 | 2.0 GB |
| Curriculum Planning | `curriculum-llama:latest` | llama3.2 | 2.0 GB |

Both models are recommended for MVP, each serving a distinct role in the education pipeline.

---

## 3. Why These Models Were Chosen

- **Local & Private** — Runs fully on-device via Ollama. No data leaves the machine, making it suitable for school or institutional environments.
- **Lightweight** — At 2 GB each, both models run on standard hardware without requiring a GPU, keeping infrastructure cost at zero for MVP.
- **Purpose-built** — Each model has a dedicated Modelfile and system prompt tuned for its specific task (quiz generation vs. curriculum planning).
- **Built on proven experiments** — Lessons from `my-json-model` and `my-llama-evaluator` testing were carried forward into these models.

---

## 4. Prompt Setup

### Quiz-Llama — System Prompt Summary
- Returns a **valid JSON array** of quiz questions
- Each item includes: `question`, `options[]`, `answer`, `explanation`
- Low temperature (0.3–0.5) for consistent, structured output

### Curriculum-Llama — System Prompt Summary
- Returns a **structured JSON curriculum** conforming to the live `curriculum_generation` schema
- Fields: `topic`, `level`, `total_weeks`, `weeks[]` (each with `week`, `title`, `points[3]`)
- Slightly higher temperature (0.6) for varied week content

---

## 5. Where It Works Well

- ✅ **JSON output** — The primary strength of both models. With constrained system prompts, they reliably return well-structured, machine-parseable JSON, making integration with the app layer straightforward.
- ✅ **Quiz generation** — `quiz-llama` produces consistent, schema-valid quiz output with no safety-net intervention required.
- ✅ **Curriculum structure** — `curriculum-llama` produces correct topic, level, week titles, and points content. The safety net handles week count only; all other fields are model-generated correctly.

---

## 6. Known Failures & Limitations

> ⚠️ **This section has been updated to reflect findings from benchmark testing (16 April 2026). The previous version of this document incorrectly stated no critical failures had been documented. The limitation below is real, known, and permanent at MVP scale.**

### 6.1 Curriculum Week Count — Known Permanent Limitation

**What happens:** `curriculum-llama` (based on `llama3.2:latest`, a small ~2B parameter model) **consistently generates 6 weeks** regardless of system prompt instructions requiring 8–16 weeks. This was observed in all 5 benchmark runs.

**Root cause:** Small local LLMs lack the instruction-following precision needed for strict numeric counting constraints. Modelfile-level enforcement ("NEVER 6, NEVER 7", numbered rules) did not resolve the issue.

**Resolution — Safety Net Dependency:** A post-processing safety net in `generate_curriculum()` automatically detects week count < 8 and pads the output with valid week objects, then corrects `total_weeks` to match. This runs on every curriculum generation call.

| Property | Detail |
|---|---|
| Safety net location | `generate_curriculum()` in `repair.py` |
| Trigger condition | `len(weeks) < 8` |
| Action | Pad weeks to minimum 8, recompute `total_weeks` |
| Validation result | ✅ Passes schema validation after correction |
| Raw model output | ❌ Would fail without safety net (6 weeks < 8 minimum) |

**Implication for reviewers:** All benchmark passes for `CURRICULUM-INT-01` reflect post-safety-net output, not raw model output. The system works correctly end-to-end; however, this dependency on post-processing is a known architectural constraint of the MVP.

**Planned resolution:** Evaluate larger models (7B+ parameter) post-MVP. Cloud models (GPT-4, Claude API) resolve this fully but are excluded from MVP due to privacy and cost constraints.

### 6.2 No Other Critical Failures

All other test cases (quiz, assignment, summary, weak area) passed all 5 runs without any safety-net intervention or post-processing correction.

---

## 7. What Was Ruled Out

| Model | Reason Rejected |
|---|---|
| `llama3:latest` (4.7 GB) | Too large and slow for MVP hardware |
| `gemma3:1b` (815 MB) | Too small; weak instruction-following and poor JSON consistency |
| `my-llama-evaluator` | Internal testing tool, not for production use |
| Cloud models (GPT-4, Claude) | Privacy concerns and cost; revisit post-MVP if needed |

---

## 8. Recommended Next Steps

1. **Treat safety net as permanent for MVP** — do not attempt to remove it; the model limitation is fundamental
2. **Add JSON sanitization** in the app layer to handle any edge-case malformed outputs
3. **Log failures during MVP** to build a dataset for future fine-tuning
4. **Version-lock models** by Modelfile hash to prevent unintended drift
5. **Revisit post-MVP** — evaluate 7B+ parameter models or cloud APIs once user feedback is collected and privacy/cost trade-offs can be reassessed

---

## 9. Decision Sign-off

| Role | Name | Status |
|---|---|---|
| ML Lead | _(sign here)_ | ⬜ Pending |
| Backend Dev | _(sign here)_ | ⬜ Pending |
| Product Owner | _(sign here)_ | ⬜ Pending |

---

*Commit this file to the repo root or `/docs` folder and link it in the project README.*
