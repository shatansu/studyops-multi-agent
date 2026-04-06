from gemini import ask_gemini
from tools import store_notes
import json
import re

# 🔹 Clean JSON helper
def clean_json(text):
    text = re.sub(r"```json|```", "", text).strip()
    return json.loads(text)


def notes_agent(user_input):

    prompt = f"""
You are a Notes Agent.

User request: {user_input}

STRICT RULES:
- Return ONLY valid JSON
- Do NOT use ```json
- No extra text

FORMAT:
{{
  "type": "notes",
  "topic": "topic name",
  "points": ["point1", "point2", "point3"]
}}
"""

    # 🔹 Gemini call
    raw = ask_gemini(prompt)

    # 🔹 Convert to JSON
    data = clean_json(raw)

    # 🔥 SAVE NOTES TO FIREBASE
    store_notes({
        "user_id": "user1",
        "topic": data.get("topic", ""),
        "points": data.get("points", [])
    })

    # 🔹 Return raw (orchestrator handle karega)
    return raw.strip()