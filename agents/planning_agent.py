from gemini import ask_gemini

def planning_agent(user_input):
    prompt = f"""
    You are a Planning Agent.

    User request: {user_input}

    Create a simple 3-day study plan.
    Keep it short and structured.
    """

    return ask_gemini(prompt)