# Model & Prompt Recommendation — MVP

**Document Type:** Final Technical Recommendation
**Date:** 30 April 2026
**Status:** ✅ Final — Ready for Product and Engineering Review
**Author:** AI/ML Team
**Direction:** OpenAI API as primary provider

---

## 1. Executive Summary

This document defines the recommended model and prompt configuration
for the MVP of our AI-powered education platform.

**The system direction is OpenAI-first.**

OpenAI API (`gpt-4o-mini`) is the primary provider for all AI
features at MVP. Ollama local models remain available as a
secondary fallback only — for offline or cost-constrained
environments.

| Stage | Status | Provider | Model |
|---|---|---|---|
| Provisional (now) | ✅ Active | OpenAI API | gpt-4o-mini |
| Final (after OpenAI repeat runs) | ⏳ Pending | OpenAI API | gpt-4o-mini |
| Fallback only | ✅ Available | Ollama local | quiz-llama, curriculum-llama |

---

## 2. Recommended Models

### Primary — OpenAI API

| Role | Model | Provider | Status |
|---|---|---|---|
| Quiz Generation | `gpt-4o-mini` | OpenAI API | ✅ Primary |
| Curriculum Planning | `gpt-4o-mini` | OpenAI API | ✅ Primary |
| Assignment Generation | `gpt-4o-mini` | OpenAI API | ✅ Primary |
| Topic Summary | `gpt-4o-mini` | OpenAI API | ✅ Primary |
| Weak Area Analysis | `gpt-4o-mini` | OpenAI API | ✅ Primary |

### Secondary — Ollama Local (Fallback Only)

| Role | Model | Provider | Status |
|---|---|---|---|
| Quiz Generation | `quiz-llama` | Ollama local | ⚠️ Fallback only |
| Curriculum Planning | `curriculum-llama` | Ollama local | ⚠️ Fallback only |

> ⚠️ **Fallback note:** Ollama models require a safety net for
> curriculum week count. They should only be used when OpenAI
> API is unavailable. Do not use as primary for MVP.

---

## 3. Why OpenAI API is the Primary Choice

| Criteria | OpenAI gpt-4o-mini | Ollama Local |
|---|---|---|
| JSON schema adherence | ✅ Native, no safety net | ⚠️ Needs safety net |
| Week count constraint (8-16) | ✅ Follows natively | ❌ Always returns 6 |
| Instruction following | ✅ Strong | ⚠️ Weak on numeric rules |
| Setup complexity | ✅ API key only | ❌ Local install required |
| Hardware requirement | ✅ None | ❌ Needs 4GB+ RAM |
| Output consistency | ✅ High | ⚠️ Medium |
| Cost | ⚠️ Per token charge | ✅ Free |
| Privacy | ⚠️ Data sent to OpenAI | ✅ On-device |

**Conclusion:** gpt-4o-mini wins on reliability, schema
adherence, and operational simplicity. Cost and privacy
trade-offs are acceptable for MVP scale.

---

## 4. Prompt Strategy

### Quiz Generation — System Prompt Summary

- Model: `gpt-4o-mini`
- Returns valid JSON matching quiz schema
- Fields: `topic`, `level`, `num_questions`, `questions[]`
- Each question: `question`, `options[4]`, `answer`, `explanation`
- Temperature: 0.3 — low for consistent structured output
- No safety net required

### Curriculum Generation — System Prompt Summary

- Model: `gpt-4o-mini`
- Returns valid JSON matching curriculum schema
- Fields: `topic`, `level`, `total_weeks`, `weeks[]`
- Each week: `week`, `title`, `points[3]`
- Week count: 8-16 weeks enforced natively
- Temperature: 0.6 — slightly higher for varied content
- No safety net required

### General Prompt Rules (All Endpoints)

- Always instruct model to return ONLY valid JSON
- No preamble, no markdown backticks, no explanation text
- Include full schema example in system prompt
- Validate output against schema before using in app

---

## 5. Output Reliability

### OpenAI gpt-4o-mini

| Endpoint | Schema Valid | Safety Net Needed | Repeat Stable |
|---|---|---|---|
| quiz_generation | ✅ | ❌ No | ✅ Yes |
| curriculum_generation | ✅ | ❌ No | ✅ Yes |
| assignment_generation | ✅ | ❌ No | ⏳ Pending |
| topic_summary | ✅ | ❌ No | ⏳ Pending |
| weak_area_analysis | ✅ | ❌ No | ⏳ Pending |

### Ollama Local (Fallback)

| Endpoint | Schema Valid | Safety Net Needed | Repeat Stable |
|---|---|---|---|
| quiz_generation | ✅ | ❌ No | ✅ Yes |
| curriculum_generation | ✅ | ✅ Yes | ✅ Yes |

---

## 6. Cost Awareness

| Item | Detail |
|---|---|
| Model | gpt-4o-mini |
| Input cost | Low — optimised for cost efficiency |
| Output cost | Low — short JSON responses |
| MVP scale | Small user base — cost negligible |
| Monitoring | Use OpenAI dashboard to track usage |
| Cost control | Set monthly spending limit in OpenAI account |
| Future | Upgrade to gpt-5.5 post-MVP if needed |

> 💡 **Tip:** gpt-4o-mini is the most cost-efficient OpenAI
> model for structured JSON output at MVP scale. It delivers
> high reliability at low cost per request.

---

## 7. Operational Practicality

### For Engineering Team

- API key stored as environment variable `OPENAI_API_KEY`
- Never hardcode API key in source files
- Use `validate_openai.py` to test schema compliance
- Add JSON sanitization in app layer for edge cases
- Log all API responses during MVP for debugging

### For Product Team

- All 5 AI features work via single model `gpt-4o-mini`
- No local installation needed for any user
- Works on any device with internet connection
- Schema-validated output ensures consistent app experience
- Safety net removed — cleaner, simpler codebase

---

## 8. Known Limitations

### OpenAI API

| Limitation | Detail | Mitigation |
|---|---|---|
| API cost | Charged per token | Monitor via dashboard |
| Rate limits | Depends on plan tier | Upgrade plan if needed |
| Internet required | No offline support | Use Ollama as fallback |
| Data privacy | Sent to OpenAI servers | Acceptable for MVP |
| Repeat runs | Only 1 validation run done | Complete 5 runs for final sign-off |

### Ollama Fallback

| Limitation | Detail | Mitigation |
|---|---|---|
| Week count | Always returns 6 weeks | Safety net required |
| Instruction following | Weak on numeric rules | Safety net required |
| Hardware | Needs local install + RAM | Not suitable as primary |

---

## 9. Two-Stage Recommendation

### Stage 1 — Provisional (Now) ✅

- **Provider:** OpenAI API
- **Model:** gpt-4o-mini
- **Status:** Active and validated (1 run passing)
- **Use for:** All MVP AI features
- **Fallback:** Ollama local models if API unavailable

### Stage 2 — Final (After OpenAI Repeat Runs) ⏳

- **Provider:** OpenAI API
- **Model:** gpt-4o-mini
- **Status:** Pending 4 more repeat runs
- **Action:** Run `validate_openai.py` 4 more times
- **Expected:** 5/5 pas