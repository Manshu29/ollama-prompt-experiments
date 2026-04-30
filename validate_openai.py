import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_quiz():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """Return ONLY valid JSON in this format:
{
  "topic": "string",
  "level": "beginner or intermediate or advanced",
  "num_questions": 2,
  "questions": [
    {
      "question": "string",
      "options": ["option1", "option2", "option3", "option4"],
      "correct_answer": "must match one of the options",
      "explanation": "string"
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
    print("Quiz raw output:\n", raw)

    data = json.loads(raw)

    assert "topic" in data
    assert "level" in data
    assert "num_questions" in data
    assert "questions" in data

    for q in data["questions"]:
        assert "question" in q
        assert "options" in q
        assert len(q["options"]) == 4
        assert "correct_answer" in q
        assert "explanation" in q
        assert q["correct_answer"] in q["options"]

    print("✅ PASS: Quiz schema valid")


def test_curriculum():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """Return ONLY valid JSON in this format:
{
  "topic": "string",
  "level": "beginner or intermediate or advanced",
  "total_weeks": 8,
  "weeks": [
    {
      "week": 1,
      "title": "string",
      "description": ["string", "string", "string"]
    }
  ]
}"""
            },
            {
                "role": "user",
                "content": "Generate an 8 week beginner curriculum about Python basics"
            }
        ],
        temperature=0.6
    )

    raw = response.choices[0].message.content
    print("Curriculum raw output:\n", raw)

    data = json.loads(raw)

    assert "topic" in data
    assert "level" in data
    assert "total_weeks" in data
    assert len(data["weeks"]) == 8

    for w in data["weeks"]:
        assert "week" in w
        assert "title" in w
        assert "description" in w
        assert len(w["description"]) == 3

    print("✅ PASS: Curriculum schema valid")


# 👇 THIS WAS MISSING
if __name__ == "__main__":
    print("Running tests...\n")

    test_quiz()
    print("\n-----------------\n")
    test_curriculum()