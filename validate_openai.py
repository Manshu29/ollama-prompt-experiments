import openai
import json

client = openai.OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")

def test_quiz():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are a quiz generator. Return ONLY valid JSON in this exact format:
{
  "topic": "string",
  "level": "beginner or intermediate or advanced",
  "num_questions": 2,
  "questions": [
    {
      "question": "string",
      "options": ["option1", "option2", "option3", "option4"],
      "answer": "must match one of the options",
      "explanation": "string min 5 chars"
    }
  ]
}"""
            },
            {
                "role": "user",
                "content": "Generate a 2 question beginner quiz about Python variables"
            }
        ],
        temperature=0.3
    )
    raw = response.choices[0].message.content
    data = json.loads(raw)
    assert "topic" in data, "FAIL: missing topic"
    assert "level" in data, "FAIL: missing level"
    assert "num_questions" in data, "FAIL: missing num_questions"
    assert "questions" in data, "FAIL: missing questions"
    for q in data["questions"]:
        assert "question" in q, "FAIL: missing question"
        assert "options" in q, "FAIL: missing options"
        assert len(q["options"]) == 4, "FAIL: options must have 4 items"
        assert "answer" in q, "FAIL: missing answer"
        assert "explanation" in q, "FAIL: missing explanation"
        assert q["answer"] in q["options"], "FAIL: answer not in options"
    print("✅ PASS: Quiz schema valid")
    return data

def test_curriculum():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are a curriculum planner. Return ONLY valid JSON in this exact format:
{
  "topic": "string",
  "level": "beginner or intermediate or advanced",
  "total_weeks": 8,
  "weeks": [
    {
      "week": 1,
      "title": "string",
      "points": ["string", "string", "string"]
    }
  ]
}
RULES:
- weeks array must have exactly 8 items
- total_weeks must equal the number of weeks
- points must have exactly 3 strings per week"""
            },
            {
                "role": "user",
                "content": "Generate an 8 week beginner curriculum about Python basics"
            }
        ],
        temperature=0.6
    )
    raw = response.choices[0].message.content
    data = json.loads(raw)
    assert "topic" in data, "FAIL: missing topic"
    assert "level" in data, "FAIL: missing level"
    assert "total_weeks" in data, "FAIL: missing total_weeks"
    assert "weeks" in data, "FAIL: missing weeks"
    assert len(data["weeks"]) >= 8, f"FAIL: only {len(data['weeks'])} weeks, need 8+"
    assert len(data["weeks"]) <= 16, f"FAIL: {len(data['weeks'])} weeks, max is 16"
    assert data["total_weeks"] == len(data["weeks"]), "FAIL: total_weeks doesnt match len(weeks)"
    for w in data["weeks"]:
        assert "week" in w, "FAIL: missing week number"
        assert "title" in w, "FAIL: missing title"
        assert "points" in w, "FAIL: missing points"
        assert len(w["points"]) == 3, f"FAIL: points must have 3 items, got {len(w['points'])}"
    print("✅ PASS: Curriculum schema valid")
    return data

print("Running benchmark validation against OpenAI API...")
print("=" * 50)

try:
    quiz_output = test_quiz()
    print(f"   Topic: {quiz_output['topic']}")
    print(f"   Questions: {len(quiz_output['questions'])}")
except AssertionError as e:
    print(f"❌ {e}")
except json.JSONDecodeError:
    print("❌ FAIL: Response was not valid JSON")

print()

try:
    curriculum_output = test_curriculum()
    print(f"   Topic: {curriculum_output['topic']}")
    print(f"   Weeks: {curriculum_output['total_weeks']}")
except AssertionError as e:
    print(f"❌ {e}")
except json.JSONDecodeError:
    print("❌ FAIL: Response was not valid JSON")

print("=" * 50)
print("Benchmark validation complete.")