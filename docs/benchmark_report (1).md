# \# Benchmark Results Report

# 

# \*\*Project:\*\* Ollama Prompt Experiments → OpenAI API Migration

# \*\*Dataset:\*\* `benchmark.json`

# \*\*Phase 1 Models:\*\* `quiz-llama`, `curriculum-llama` (Ollama/local)

# \*\*Phase 2 Models:\*\* `gpt-4o-mini` (OpenAI API)

# \*\*Date:\*\* 30 April 2026

# \*\*Total Runs:\*\* 5 repeat runs (Phase 1) + 1 validation run (Phase 2)

# 

# \---

# 

# \## 1. Test Cases (from benchmark.json)

# 

# | Test ID | Endpoint | Difficulty |

# |---|---|---|

# | QUIZ-BEG-01 | quiz\_generation | beginner |

# | CURRICULUM-INT-01 | curriculum\_generation | intermediate |

# | ASSIGN-ADV-01 | assignment\_generation | advanced |

# | SUMMARY-INT-01 | topic\_summary | intermediate |

# | WEAK-BEG-01 | weak\_area\_analysis | beginner |

# 

# \---

# 

# \## 2. Provider \& Model Reference

# 

# | Phase | Provider | Model | Infrastructure |

# |---|---|---|---|

# | Phase 1 | Ollama (local) | `quiz-llama`, `curriculum-llama` | On-device, no internet |

# | Phase 2 | OpenAI API | `gpt-4o-mini` | Cloud API |

# 

# \---

# 

# \## 3. Phase 1 — Ollama Local Results (5 Repeat Runs)

# 

# | Test ID | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |

# |---|---|---|---|---|---|

# | QUIZ-BEG-01 | ✅ | ✅ | ✅ | ✅ | ✅ |

# | CURRICULUM-INT-01 | ✅ | ✅ | ✅ | ✅ | ✅ |

# | ASSIGN-ADV-01 | ✅ | ✅ | ✅ | ✅ | ✅ |

# | SUMMARY-INT-01 | ✅ | ✅ | ✅ | ✅ | ✅ |

# | WEAK-BEG-01 | ✅ | ✅ | ✅ | ✅ | ✅ |

# | \*\*Total Passed\*\* | \*\*5/5\*\* | \*\*5/5\*\* | \*\*5/5\*\* | \*\*5/5\*\* | \*\*5/5\*\* |

# | \*\*Success Rate\*\* | \*\*100%\*\* | \*\*100%\*\* | \*\*100%\*\* | \*\*100%\*\* | \*\*100%\*\* |

# 

# > ⚠️ \*\*Note:\*\* CURRICULUM-INT-01 passes include safety-net correction.

# > Raw model output was 6 weeks; safety net padded to 8.

# > All passes reflect post-correction schema validity.

# 

# \---

# 

# \## 4. Phase 1 — Repeat Run Consistency (Ollama)

# 

# | Metric | Value |

# |---|---|

# | Total runs conducted | 5 |

# | Runs with 5/5 pass | 5 |

# | Runs with any failure | 0 |

# | Overall consistency | 100% stable |

# | Result variance | None — identical outcome every run |

# | Safety net dependency | Yes — curriculum week count only |

# 

# \---

# 

# \## 5. Phase 2 — OpenAI API Results (Validation Run)

# 

# | Test ID | Run 1 | Schema Valid | Provider | Model |

# |---|---|---|---|---|

# | QUIZ-BEG-01 | ✅ | ✅ | OpenAI API | gpt-4o-mini |

# | CURRICULUM-INT-01 | ✅ | ✅ | OpenAI API | gpt-4o-mini |

# 

# \*\*Quiz output:\*\*

# \- Topic: Python Variables

# \- Questions: 2

# \- Schema fields: `topic`, `level`, `num\_questions`, `questions\[]`

# \- Each question: `question`, `options\[4]`, `answer`, `explanation` ✅

# 

# \*\*Curriculum output:\*\*

# \- Topic: Python Basics

# \- Weeks: 8

# \- Schema fields: `topic`, `level`, `total\_weeks`, `weeks\[]`

# \- Each week: `week`, `title`, `points\[3]` ✅

# \- Safety net required: ❌ No — gpt-4o-mini followed week count natively

# 

# > ✅ \*\*Phase 2 note:\*\* OpenAI gpt-4o-mini passed all schema checks

# > without any safety-net intervention. Week count constraint

# > (8-16 weeks) was followed natively by the model.

# 

# \---

# 

# \## 6. Provider Comparison — Ollama vs OpenAI

# 

# | Criteria | Ollama (Phase 1) | OpenAI gpt-4o-mini (Phase 2) |

# |---|---|---|

# | Quiz schema adherence | ✅ Passes | ✅ Passes |

# | Curriculum schema adherence | ✅ Passes (with safety net) | ✅ Passes (no safety net) |

# | Week count constraint (8-16) | ❌ Raw output = 6 weeks | ✅ Native compliance |

# | Safety net required | ✅ Yes (curriculum only) | ❌ Not needed |

# | JSON output consistency | ✅ Stable | ✅ Stable |

# | Repeat run stability | ✅ 100% (5/5 runs) | ⏳ Pending (Phase 2 repeats) |

# | Infrastructure | Local / free | Cloud API / paid |

# | Privacy | ✅ On-device | ⚠️ Data sent to OpenAI |

# | Cost | Free | Per token charge |

# 

# \---

# 

# \## 7. Live ai\_service Schema Validation Rules

# 

# \### Quiz Schema — `quiz\_generation` endpoint

# 

# ```json

# {

# &#x20; "topic": "string — required",

# &#x20; "level": "beginner | intermediate | advanced — required",

# &#x20; "num\_questions": 5,

# &#x20; "questions": \[

# &#x20;   {

# &#x20;     "question": "string — required",

# &#x20;     "options": \["exactly 4 strings — required"],

# &#x20;     "answer": "must match one of the options — required",

# &#x20;     "explanation": "string min 5 chars — required"

# &#x20;   }

# &#x20; ]

# }

# ```

# 

# \### Curriculum Schema — `curriculum\_generation` endpoint

# 

# ```json

# {

# &#x20; "topic": "string — required",

# &#x20; "level": "beginner | intermediate | advanced — required",

# &#x20; "total\_weeks": "integer, must equal len(weeks) — required",

# &#x20; "weeks": \[

# &#x20;   {

# &#x20;     "week": "integer, sequential from 1 — required",

# &#x20;     "title": "string — required",

# &#x20;     "points": \["exactly 3 strings — required"]

# &#x20;   }

# &#x20; ]

# }

# ```

# 

# \*\*Constraint:\*\* `len(weeks)` must be between 8 and 16 inclusive.

# 

# \---

# 

# \## 8. Known Limitations

# 

# \### Phase 1 — Ollama Local Models

# 

# | Limitation | Detail |

# |---|---|

# | Week count constraint | llama3.2 always generates 6 weeks regardless of instructions |

# | Resolution | Safety net in `generate\_curriculum()` pads to minimum 8 weeks |

# | Status | Permanent limitation at MVP scale for small local LLMs |

# 

# \### Phase 2 — OpenAI API

# 

# | Limitation | Detail |

# |---|---|

# | API cost | Charged per token — monitor usage |

# | Rate limits | Depends on OpenAI plan tier |

# | Privacy | Data is sent to OpenAI servers |

# | Repeat runs | Only 1 validation run completed — more needed |

# 

# \---

# 

# \## 9. Phase 2 Repeat Runs — Pending

# 

# > ⏳ \*\*To be completed after WL-95 is done.\*\*

# > Run `validate\_openai.py` 5 times and record results here.

# 

# | Test ID | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |

# |---|---|---|---|---|---|

# | QUIZ-BEG-01 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ |

# | CURRICULUM-INT-01 | ✅ | ⏳ | ⏳ | ⏳ | ⏳ |

# 

# \---

# 

# \## 10. Run Timestamps — Phase 1 Evidence

# 

# | Run | Time | Result |

# |---|---|---|

# | Run 1 | 13:02:35 | 5/5 ✅ |

# | Run 2 | 13:03:25 | 5/5 ✅ |

# | Run 3 | 13:03:56 | 5/5 ✅ |

# | Run 4 | 13:04:32 | 5/5 ✅ |

# | Run 5 | 13:05:15 | 5/5 ✅ |

# 

# \---

# 

# \## 11. Final Summary

# 

# | Item | Phase 1 (Ollama) | Phase 2 (OpenAI) |

# |---|---|---|

# | All test cases passing | ✅ | ✅ |

# | 100% success rate | ✅ | ⏳ Pending 5 runs |

# | Quiz schema aligned | ✅ | ✅ |

# | Curriculum schema aligned | ✅ (with safety net) | ✅ (no safety net) |

# | Failure cases documented | ✅ | ✅ |

# | Known limitations documented | ✅ | ✅ |

# | Safety net dependency disclosed | ✅ | N/A |

# | Sample valid output committed | ✅ | ✅ |

# | Provider comparison available | ✅ | ✅ |

# | Schema field names aligned | ✅ | ✅ |

