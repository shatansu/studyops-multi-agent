from gemini import ask_gemini
from tools import create_reminder
import json
import re

def clean_json(text):
    text = re.sub(r"```json|```", "", text).strip()
    return json.loads(text)

def reminder_agent(user_input):

    prompt = f"""
You are a Reminder Agent.

User request: {user_input}

Extract reminder info.

STRICT RULES:
Return ONLY JSON

FORMAT:
{{
  "task": "what to do",
  "time": "ISO datetime"
}}
"""

    raw = ask_gemini(prompt)

    data = clean_json(raw)

    # 🔥 SAVE REMINDER
    create_reminder({
        "user_id": "user1",
        "task": data.get("task"),
        "time": data.get("time"),
        "status": "pending"
    })

    return raw