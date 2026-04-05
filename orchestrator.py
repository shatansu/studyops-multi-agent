from agents.planning_agent import planning_agent
from agents.notes_agent import notes_agent

def primary_agent(user_input):

    text = user_input.lower()

    # decision logic
    if "exam" in text or "prepare" in text:
        return planning_agent(user_input)

    elif "notes" in text:
        return notes_agent(user_input)

    else:
        return "I can help with study plans or notes."