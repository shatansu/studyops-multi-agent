import json
import re
from agents.planning_agent import planning_agent
from agents.notes_agent import notes_agent
from firebase_db import get_tasks, get_notes
from agents.reminder_agent import reminder_agent
from firebase_db import get_reminders
# 🔥 Reminder create
if "remind" in text or "yaad" in text:
    raw = reminder_agent(user_input)
    return extract_json(raw)

# 🔥 Show reminders
elif "show reminders" in text:
    return get_reminders("user1")


# 🔹 Clean JSON
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


# 🔹 MAIN AGENT
def primary_agent(user_input):

    text = user_input.lower()

    # 🔥 1. RETRIEVE TASKS (TOP PRIORITY)
    if "show tasks" in text:
        return get_tasks("user1")

    # 🔥 2. RETRIEVE NOTES
    elif "show notes" in text:
        return get_notes("user1")

    # 🔥 3. PLANNING
    elif "exam" in text or "prepare" in text:

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

    # 🔥 4. NOTES GENERATION
    elif "notes" in text:
        raw = notes_agent(user_input)
        return extract_json(raw)

    # 🔹 fallback
    else:
        return {"message": "I can help with study plans, notes, or show your saved data."}