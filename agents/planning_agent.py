from gemini import ask_gemini

def planning_agent(user_input):

    prompt = f"""
You are a Planning Agent.

User request: {user_input}

Create a simple 3-day study plan.

STRICT RULES:
- Return ONLY valid JSON
- Do NOT use ```json or ``` anywhere
- Do NOT add explanation
- Do NOT add text before or after JSON

FORMAT:
{{
  "type": "study_plan",
  "days": [
    {{"day": 1, "topics": ["topic1", "topic2"]}},
    {{"day": 2, "topics": ["topic1", "topic2"]}},
    {{"day": 3, "topics": ["topic1", "topic2"]}}
  ]
}}
"""

    response = ask_gemini(prompt)

    return response.strip()