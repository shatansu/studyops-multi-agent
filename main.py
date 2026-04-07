from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import primary_agent
import threading
from scheduler import run_scheduler
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Start background scheduler
threading.Thread(target=run_scheduler, daemon=True).start()

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