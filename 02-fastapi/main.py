from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "FastAPI is running for AI project"}

@app.post("/predict")
def predict(message: Message):
    # Simulasi endpoint AI
    return {"input": message.text, "output": f"AI response to: {message.text}"}
