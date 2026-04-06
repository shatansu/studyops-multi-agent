import json
import re
from agents.planning_agent import planning_agent
from agents.notes_agent import notes_agent


# 🔹 Clean JSON extractor
def extract_json(text):
    text = re.sub(r"```json|```", "", text).strip()
    try:
        return json.loads(text)
    except:
        return {"raw_response": text}


# 🔹 Subject detection
def extract_subjects(text):
    subjects = []

    if "ai" in text:
        subjects.append("Artificial Intelligence")
    if "math" in text:
        subjects.append("Mathematics")
    if "physics" in text:
        subjects.append("Physics")

    return subjects


# 🔹 Primary Agent (MAIN BRAIN)
def primary_agent(user_input):

    text = user_input.lower()

    # 🔥 Dynamic planning
    if "exam" in text or "prepare" in text:

        subjects = extract_subjects(text)

        if not subjects:
            subjects = ["General"]

        results = []

        for sub in subjects:
            raw = planning_agent(user_input, sub)
            results.append(extract_json(raw))

        return {
            "type": "multi_subject_plan",
            "plans": results
        }

    # Notes flow
    elif "notes" in text:
        raw = notes_agent(user_input)
        return extract_json(raw)

    else:
        return {"message": "I can help with study plans or notes."}