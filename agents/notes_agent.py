from gemini import ask_gemini

def notes_agent(user_input):

    prompt = f"""
You are a Notes Agent.

User request: {user_input}

STRICT RULES:
- Return ONLY valid JSON
- No extra text

FORMAT:
{{
  "type": "notes",
  "topic": "topic name",
  "points": ["point1", "point2", "point3"]
}}
"""

    return ask_gemini(prompt).strip()