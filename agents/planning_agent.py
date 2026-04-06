from gemini import ask_gemini

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

    return ask_gemini(prompt).strip()