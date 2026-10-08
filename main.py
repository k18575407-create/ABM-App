import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="ABM AI")

app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/app")
def app_page():
    return FileResponse("static/index.html")

@app.post("/api/chat")
def chat(req: ChatRequest):
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise HTTPException(500, "OPENAI_API_KEY is not configured on the server.")

    client = OpenAI(api_key=key)
    model = os.getenv("OPENAI_MODEL", "gpt-5-mini")

    try:
        response = client.responses.create(
            model=model,
            input=req.message
        )
        return {"reply": response.output_text}
    except Exception as e:
        raise HTTPException(502, f"AI request failed: {str(e)}")
