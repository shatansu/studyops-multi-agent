import json
import re
from agents.planning_agent import planning_agent
from agents.notes_agent import notes_agent

def extract_json(text):
    try:
        # remove ```json ``` wrappers
        text = re.sub(r"```json|```", "", text).strip()
        return json.loads(text)
    except:
        return {"raw_response": text}


def primary_agent(user_input):

    text = user_input.lower()

    if "exam" in text or "prepare" in text:
        raw = planning_agent(user_input)

    elif "notes" in text:
        raw = notes_agent(user_input)

    else:
        return {"message": "I can help with study plans or notes."}

    return extract_json(raw)