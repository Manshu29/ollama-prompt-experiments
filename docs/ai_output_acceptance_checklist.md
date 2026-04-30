# AI Output Acceptance Checklist

## Purpose
This checklist is used to review AI-generated outputs from the OpenAI API (gpt-5.4-mini) before accepting them into the product.

---

## 1. Schema Validation (Mandatory)

- ☐ Output is valid JSON (no syntax errors)
- ☐ Matches expected schema structure
- ☐ All required fields are present
- ☐ Field names are correct (no typos)
- ☐ No extra or unexpected fields

---

## 2. Output-Type Specific Checks

### Quiz
- ☐ topic is present
- ☐ level is present (beginner/intermediate/advanced)
- ☐ num_questions matches actual number of questions
- ☐ Each question includes:
  - ☐ question
  - ☐ options
  - ☐ answer
  - ☐ explanation

### Curriculum
- ☐ topic is present
- ☐ level is present
- ☐ total_weeks is present and equals len(weeks)
- ☐ weeks[] contains between 8 and 16 entries
- ☐ Each week includes:
  - ☐ week (sequential integer)
  - ☐ title
  - ☐ points[] (exactly 3 strings)
- ☐ Logical progression (basic → advanced)

### Assignment
- ☐ topic is present
- ☐ Clear instructions/tasks
- ☐ Difficulty matches level
- ☐ Includes expected output or guidance

### Topic Summary
- ☐ title is present
- ☐ Content is structured (points or sections)
- ☐ Covers key concepts
- ☐ Easy to understand

### Weak Area Analysis
- ☐ Weak areas are identified
- ☐ Reasons or patterns are explained
- ☐ Improvement suggestions are provided

---

## 3. Content Quality

- ☐ Content is factually correct
- ☐ No misleading or incorrect information
- ☐ Clear and meaningful explanations
- ☐ Not vague or generic

---

## 4. Clarity & Readability

- ☐ Simple and clear language
- ☐ Beginner-friendly
- ☐ Well-structured (lists/sections)
- ☐ No confusing sentences

---

## 5. Duplication & Consistency

- ☐ No duplicate questions or content
- ☐ No repeated sections
- ☐ Consistent format throughout
- ☐ No contradictions

---

## 6. Usefulness (Product/Classroom Check)

- ☐ Useful for students
- ☐ Can be directly used in classroom/app
- ☐ Helps learning (not filler content)
- ☐ Output aligns with product goals

---

## 7. Final Decision

- ☐ ✅ Accept (ready to use)
- ☐ ⚠️ Needs Minor Fix (small changes required)
- ☐ ❌ Reject (regenerate output)

---

## How to Use

1. Generate AI output via OpenAI API (gpt-5.4-mini)
2. Review it using this checklist
3. Mark each item
4. Decide:
   - If all critical checks pass → Accept
   - If small issues → Fix manually
   - If major issues → Regenerate