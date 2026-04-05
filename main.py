from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import primary_agent

app = FastAPI()

# Request model
class ChatRequest(BaseModel):
    message: str

# Optional: Home route (test ke liye)
@app.get("/")
def home():
    return {"message": "StudyOps Multi-Agent API Running"}

# Main chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):

    user_input = req.message

    # Call primary agent (orchestrator)
    result = primary_agent(user_input)

    return {
        "input": user_input,
        "response": result
    }