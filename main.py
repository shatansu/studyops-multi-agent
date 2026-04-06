from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import primary_agent

app = FastAPI()

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "StudyOps Multi-Agent Running"}


@app.post("/chat")
def chat(req: ChatRequest):

    result = primary_agent(req.message)

    return {
        "input": req.message,
        "response": result
    }