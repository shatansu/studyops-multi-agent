from gemini import ask_gemini

def notes_agent(user_input):
    prompt = f"""
    You are a Notes Agent.

    User request: {user_input}

    Generate short and simple notes.
    """

    return ask_gemini(prompt)