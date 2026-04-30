# \# MVP Model \& Prompt Recommendation

# 

# \*\*Document Type:\*\* Internal Technical Recommendation

# \*\*Date:\*\* April 30, 2026

# \*\*Status:\*\* ✅ Final — Ready for Team Review

# \*\*Author:\*\* AI/ML Team

# 

# \---

# 

# \## 1. Overview

# 

# This document captures the final model and prompt configuration recommended for the MVP of our AI-powered education platform. It is based on testing using the OpenAI API with gpt-5.4-mini.

# 

# \---

# 

# \## 2. Recommended Models

# 

# | Role | Model | Provider |

# |---|---|---|

# | Quiz Generation | `gpt-5.4-mini` | OpenAI API |

# | Curriculum Planning | `gpt-5.4-mini` | OpenAI API |

# 

# Both roles use the same model with different system prompts tuned for each task.

# 

# \---

# 

# \## 3. Why This Model Was Chosen

# 

# \- \*\*Powerful\*\* — gpt-5.4-mini reliably follows strict JSON schema instructions including numeric constraints.

# \- \*\*Cost-efficient\*\* — Lower cost per token compared to larger OpenAI models, suitable for MVP scale.

# \- \*\*No local setup needed\*\* — Accessed via OpenAI API, no hardware or Ollama installation required.

# \- \*\*Strong instruction-following\*\* — Handles numeric constraints (e.g. week counts) without a safety net.

# 

# \---

# 

# \## 4. Prompt Setup

# 

# \### Quiz — System Prompt Summary

# \- Returns a \*\*valid JSON array\*\* of quiz questions

# \- Each item includes: `question`, `options\[]`, `answer`, `explanation`

# \- Temperature: 0.3–0.5 for consistent, structured output

# 

# \### Curriculum — System Prompt Summary

# \- Returns a \*\*structured JSON curriculum\*\* conforming to the live `curriculum\_generation` schema

# \- Fields: `topic`, `level`, `total\_weeks`, `weeks\[]` (each with `week`, `title`, `points\[3]`)

# \- Temperature: 0.6 for varied week content

# 

# \---

# 

# \## 5. Where It Works Well

# 

# \- ✅ \*\*JSON output\*\* — gpt-5.4-mini reliably returns well-structured, machine-parseable JSON.

# \- ✅ \*\*Quiz generation\*\* — Produces consistent, schema-valid quiz output.

# \- ✅ \*\*Curriculum structure\*\* — Correctly generates topic, level, week titles, and points\[].

# \- ✅ \*\*Week count constraint\*\* — Follows the 8–16 week requirement without requiring a safety net.

# 

# \---

# 

# \## 6. Known Limitations

# 

# \### 6.1 API Cost \& Rate Limits

# \- OpenAI API calls incur a cost per token. Monitor usage during MVP to avoid unexpected charges.

# \- Rate limits may apply depending on your API tier.

# 

# \### 6.2 No Other Critical Failures

# All test cases (quiz, assignment, summary, weak area, curriculum) pass schema validation without post-processing correction.

# 

# \---

# 

# \## 7. What Was Ruled Out

# 

# | Model | Reason Rejected |

# |---|---|

# | Local Ollama models (quiz-llama, curriculum-llama) | Could not reliably follow numeric constraints; required safety net workarounds |

# | `llama3.2:latest` | Small 2B parameter model; poor instruction-following for strict schemas |

# | `gpt-5.5` | Higher cost; not needed for MVP scale |

# 

# \---

# 

# \## 8. Recommended Next Steps

# 

# 1\. \*\*Store API key securely\*\* — use environment variables, never hardcode in source files

# 2\. \*\*Add JSON sanitization\*\* in the app layer for any edge-case malformed outputs

# 3\. \*\*Log API responses during MVP\*\* to build a dataset for future fine-tuning

# 4\. \*\*Monitor token usage and costs\*\* via OpenAI dashboard

# 5\. \*\*Revisit post-MVP\*\* — evaluate gpt-5.5 if higher accuracy is needed after user feedback

# 

# \---

# 

# \## 9. Approval Signatures

# 

# | Role | Name | Date | Status |

# |------|------|------|--------|

# | ML Lead | Manshu | 30-04-2026 | ✅ Approved |

# | Backend Dev | Manshu | 30-04-2026 | ✅ Approved |

# | Product Owner | Manshu | 30-04-2026 | ✅ Approved |

# 

# \---

# 

# \*\*Signed off by:\*\* Manshu  

# \*\*Date:\*\* 30-04-2026  

# \*\*Status:\*\* ✅ APPROVED FOR RELEASE

