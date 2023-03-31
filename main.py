from fastapi import FastAPI
from pydantic import BaseModel

from typing import Optional

from ner_test_code import ner

app = FastAPI()

class request_chat(BaseModel):
    content: str
    userSend: bool
    elderlyId: int
    type: Optional[str] = None

@app.post("/")
def read_root(chat: chat_text):
    a = ner()
    output = a(chat.text)

    return output

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}