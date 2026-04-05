from fastapi import FastAPI
from pydantic import BaseModel
from gemini import ask_gemini

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    
    prompt = f"""
    You are a study planner AI.
    User: {req.message}
    
    Create a simple study plan.
    """
    
    response = ask_gemini(prompt)
    
    return {"response": response}