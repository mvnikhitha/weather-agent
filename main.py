from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent.chat_agent import handle_chat  # Make sure this exists and is async

app = FastAPI()

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Request Model ---
class ChatRequest(BaseModel):
    user_id: str
    message: str

# --- Chat Endpoint ---
@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # Log user input (optional, for debugging)
        print(f"[User ID: {req.user_id}] Message received: {req.message}")

        # Call the chat agent logic
        result = await handle_chat(req.user_id, req.message)

        # Log result (optional)
        print(f"[User ID: {req.user_id}] Bot response: {result}")

        return {"response": result}

    except Exception as e:
        print(f"Error in /chat: {e}")
        return {"error": f"An error occurred: {e}"}
