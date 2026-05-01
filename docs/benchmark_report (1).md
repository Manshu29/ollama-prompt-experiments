Benchmark Results Report

**Project:** Ollama Prompt Experiments - OpenAI API Migration
**Dataset:** benchmark.json
**Phase 1 Models:** quiz-llama, curriculum-llama (Ollama local)
**Phase 2 Models:** gpt-4o-mini (OpenAI API)
**Date:** 30 April 2026
**Total Runs:** 5 repeat runs (Phase 1) + 1 validation run (Phase 2)

---

1. Test Cases

| Test ID | Endpoint | Difficulty |
|---|---|---|
| QUIZ-BEG-01 | quiz_generation | beginner |
| CURRICULUM-INT-01 | curriculum_generation | intermediate |
| ASSIGN-ADV-01 | assignment_generation | advanced |
| SUMMARY-INT-01 | topic_summary | intermediate |
| WEAK-BEG-01 | weak_area_analysis | beginner |

---

2. Provider and Model Reference

| Phase | Provider | Model | Infrastructure |
|---|---|---|---|
| Phase 1 | Ollama local | quiz-llama, curriculum-llama | On-device, no internet |
| Phase 2 | OpenAI API | gpt-4o-mini | Cloud API |

---

3. Phase 1 - Ollama Local Results (5 Repeat Runs)

| Test ID | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
|---|---|---|---|---|---|
| QUIZ-BEG-01 | PASS | PASS | PASS | PASS | PASS |
| CURRICULUM-INT-01 | PASS | PASS | PASS | PASS | PASS |
| ASSIGN-ADV-01 | PASS | PASS | PASS | PASS | PASS |
| SUMMARY-INT-01 | PASS | PASS | PASS | PASS | PASS |
| WEAK-BEG-01 | PASS | PASS | PASS | PASS | PASS |
| **Total Passed** | **5/5** | **5/5** | **5/5** | **5/5** | **5/5** |
| **Success Rate** | **100%** | **100%** | **100%** | **100%** | **100%** |

NOTE: CURRICULUM-INT-01 passes include safety-net correction.
Raw model output was 6 weeks. Safety net padded to 8.
All passes reflect post-correction schema validity.

---

4. Phase 1 - Repeat Run Consistency (Ollama)

| Metric | Value |
|---|---|
| Total runs conducted | 5 |
| Runs with 5/5 pass | 5 |
| Runs with any failure | 0 |
| Overall consistency | 100% stable |
| Result variance | None - identical outcome every run |
| Safety net dependency | Yes - curriculum week count only |

---

5. Phase 2 - OpenAI API Results (Validation Run)

| Test ID | Run 1 | Schema Valid | Provider | Model |
|---|---|---|---|---|
| QUIZ-BEG-01 | PASS | YES | OpenAI API | gpt-4o-mini |
| CURRICULUM-INT-01 | PASS | YES | OpenAI API | gpt-4o-mini |

**Quiz output details:**
- Topic: Python Variables
- Questions: 2
- Schema fields: topic, level, num_questions, questions[]
- Each question: question, options[4], answer, explanation - PASS

**Curriculum output details:**
- Topic: Python Basics
- Weeks: 8
- Schema fields: topic, level, total_weeks, weeks[]
- Each week: week, title, points[3] - PASS
- Safety net required: NO - gpt-4o-mini followed week count natively

Phase 2 note: OpenAI gpt-4o-mini passed all schema checks
without any safety-net intervention. Week count constraint
(8-16 weeks) was followed natively by the model.

---

6. Provider Comparison - Ollama vs OpenAI

| Criteria | Ollama Phase 1 | OpenAI gpt-4o-mini Phase 2 |
|---|---|---|
| Quiz schema adherence | PASS | PASS |
| Curriculum schema adherence | PASS with safety net | PASS no safety net |
| Week count constraint 8-16 | FAIL raw output 6 weeks | PASS native compliance |
| Safety net required | YES curriculum only | NO not needed |
| JSON output consistency | Stable | Stable |
| Repeat run stability | 100% 5/5 runs | Pending Phase 2 repeats |
| Infrastructure | Local free | Cloud API paid |
| Privacy | On-device | Data sent to OpenAI |
| Cost | Free | Per token charge |

---

7. Research Benchmark Schema Reference

NOTE: These schemas are used for research benchmark testing only.
They have not been verified against the wl branch live ai_service.
Treat as reference schemas until verified.

### Quiz Schema - quiz_generation endpoint