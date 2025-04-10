from fastapi import FastAPI
from pydantic import BaseModel
from agent.chat_agent import handle_chat
app = FastAPI()
class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        result = await handle_chat(req.user_id, req.message)
        return {"response": result}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}
