from gemini import ask_gemini
from tools import create_task
import json
import re

# 🔹 Clean JSON helper
def clean_json(text):
    text = re.sub(r"```json|```", "", text).strip()
    return json.loads(text)


def planning_agent(user_input, subject):

    prompt = f"""
You are a Planning Agent.

User request: {user_input}
Subject: {subject}

Create a simple 3-day study plan ONLY for this subject.

STRICT RULES:
- Return ONLY valid JSON
- Do NOT use ```json
- No extra text

FORMAT:
{{
  "subject": "{subject}",
  "days": [
    {{"day": 1, "topics": ["topic1", "topic2"]}},
    {{"day": 2, "topics": ["topic1", "topic2"]}},
    {{"day": 3, "topics": ["topic1", "topic2"]}}
  ]
}}
"""

    # 🔹 Gemini call
    raw = ask_gemini(prompt)

    # 🔹 Convert to JSON
    data = clean_json(raw)

    # 🔥 SAVE TASKS TO FIREBASE
    for day in data.get("days", []):
        for topic in day.get("topics", []):
            create_task({
                "user_id": "user1",
                "subject": subject,
                "day": day.get("day"),
                "task": topic,
                "status": "pending"
            })

    # 🔹 Return original raw (orchestrator handle karega)
    return raw.strip()