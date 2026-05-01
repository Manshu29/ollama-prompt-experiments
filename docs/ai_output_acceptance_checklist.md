# AI Output Acceptance Checklist

**Project:** AI-Powered Education Platform
**Version:** 2.0
**Date:** 30 April 2026
**Status:** Active
**Primary Provider:** OpenAI API (gpt-4o-mini)
**Fallback Provider:** Ollama (local)

---

## How to Use This Checklist

1. Generate AI output (quiz, curriculum, etc.)
2. Go through each section below
3. Mark each item PASS or FAIL
4. Use the Final Decision section at the bottom
5. You do NOT need to know the provider or prompt details

Note: This checklist works for any AI provider.
OpenAI is the primary path for MVP.

---

## Section 1 - Basic Output Check (All Types)

These apply to every single AI output before anything else.

| # | Check | Result |
|---|---|---|
| 1.1 | Output was received (not empty) | PASS / FAIL |
| 1.2 | Output is valid JSON (no broken syntax) | PASS / FAIL |
| 1.3 | All required fields are present | PASS / FAIL |
| 1.4 | No unexpected extra fields | PASS / FAIL |
| 1.5 | Field names are spelled correctly | PASS / FAIL |

IMPORTANT: If any item in Section 1 fails - Reject immediately.
Do not continue to other sections.

---

## Section 2 - Quiz Output Check

Use when: AI generated a quiz

Expected fields: topic, level, num_questions, questions[]
Each question must have: question, options[4], answer, explanation

| # | Check | Example | Result |
|---|---|---|---|
| 2.1 | topic is present and meaningful | "Python Variables" | PASS / FAIL |
| 2.2 | level is one of: beginner, intermediate, advanced | "beginner" | PASS / FAIL |
| 2.3 | num_questions matches actual number of questions | 2 questions = num_questions 2 | PASS / FAIL |
| 2.4 | Each question has a question field | "What is a variable?" | PASS / FAIL |
| 2.5 | Each question has exactly 4 options | ["A", "B", "C", "D"] | PASS / FAIL |
| 2.6 | answer matches one of the 4 options exactly | answer = "A", options include "A" | PASS / FAIL |
| 2.7 | explanation is present and at least 5 characters | "A variable stores data" | PASS / FAIL |
| 2.8 | No duplicate questions | All questions are different | PASS / FAIL |
| 2.9 | Questions match the topic and level | Beginner Python questions only | PASS / FAIL |

---

## Section 3 - Curriculum Output Check

Use when: AI generated a curriculum plan

Expected fields: topic, level, total_weeks, weeks[]
Each week must have: week, title, points[3]

| # | Check | Example | Result |
|---|---|---|---|
| 3.1 | topic is present and meaningful | "Python Basics" | PASS / FAIL |
| 3.2 | level is one of: beginner, intermediate, advanced | "beginner" | PASS / FAIL |
| 3.3 | total_weeks is present | 8 | PASS / FAIL |
| 3.4 | Number of weeks is between 8 and 16 | 8, 10, 12 are all valid | PASS / FAIL |
| 3.5 | total_weeks equals actual number of weeks | total_weeks 8 and 8 week entries | PASS / FAIL |
| 3.6 | Each week has a week number sequential from 1 | 1, 2, 3... | PASS / FAIL |
| 3.7 | Each week has a title | "Introduction to Python" | PASS / FAIL |
| 3.8 | Each week has exactly 3 points | ["point1", "point2", "point3"] | PASS / FAIL |
| 3.9 | Points are meaningful learning objectives | Not vague or repeated | PASS / FAIL |
| 3.10 | Weeks follow logical progression | Basic topics first, advanced later | PASS / FAIL |

---

## Section 4 - Assignment Output Check

Use when: AI generated an assignment

| # | Check | Result |
|---|---|---|
| 4.1 | topic is present | PASS / FAIL |
| 4.2 | Clear instructions or tasks are included | PASS / FAIL |
| 4.3 | Difficulty matches the requested level | PASS / FAIL |
| 4.4 | Expected output or guidance is included | PASS / FAIL |
| 4.5 | Tasks are practical and actionable | PASS / FAIL |

---

## Section 5 - Topic Summary Check

Use when: AI generated a topic summary

| # | Check | Result |
|---|---|---|
| 5.1 | title is present | PASS / FAIL |
| 5.2 | Content covers key concepts | PASS / FAIL |
| 5.3 | Content is structured clearly | PASS / FAIL |
| 5.4 | Easy to understand for target level | PASS / FAIL |
| 5.5 | No incorrect or misleading information | PASS / FAIL |

---

## Section 6 - Weak Area Analysis Check

Use when: AI generated a weak area analysis

| # | Check | Result |
|---|---|---|
| 6.1 | Weak areas are clearly identified | PASS / FAIL |
| 6.2 | Reasons or patterns are explained | PASS / FAIL |
| 6.3 | Improvement suggestions are provided | PASS / FAIL |
| 6.4 | Suggestions are practical and specific | PASS / FAIL |

---

## Section 7 - Content Quality (All Types)

| # | Check | Result |
|---|---|---|
| 7.1 | Content is factually correct | PASS / FAIL |
| 7.2 | Language is clear and simple | PASS / FAIL |
| 7.3 | No vague or filler content | PASS / FAIL |
| 7.4 | No duplicate or repeated content | PASS / FAIL |
| 7.5 | Appropriate for the target audience | PASS / FAIL |
| 7.6 | Useful for students in classroom or app | PASS / FAIL |

---

## Section 8 - Demo Readiness Check

Use before any product demo or stakeholder review:

| # | Check | Result |
|---|---|---|
| 8.1 | Output looks professional and complete | PASS / FAIL |
| 8.2 | No placeholder text or test data visible | PASS / FAIL |
| 8.3 | Content is relevant to the demo topic | PASS / FAIL |
| 8.4 | Output can be shown directly without editing | PASS / FAIL |

---

## Section 9 - Provider Notes

Note: These notes are for QA reference only.
Product reviewers do not need to know these details.

| Provider | Status | Notes |
|---|---|---|
| OpenAI API gpt-4o-mini | Primary | No safety net needed. All schema checks pass natively |
| Ollama quiz-llama | Fallback | Quiz output passes. No safety net needed |
| Ollama curriculum-llama | Fallback | Safety net required for week count. Output still valid after correction |

---

## Final Decision

After completing all relevant sections above:

| Decision | When to use |
|---|---|
| ACCEPT | All checks in Section 1 pass AND all checks in relevant section pass |
| MINOR FIX | Section 1 passes but 1-2 small issues in content quality |
| REJECT | Any Section 1 failure OR major content quality issues |

---

## Quick Reference - Field Names

| Output Type | Required Fields |
|---|---|
| Quiz | topic, level, num_questions, questions[] |
| Quiz Question | question, options[4], answer, explanation |
| Curriculum | topic, level, total_weeks, weeks[] |
| Curriculum Week | week, title, points[3] |

NOTE: These field names apply to all providers.
Do not use correct_answer, modules, or steps.
These are incorrect field names for this system.