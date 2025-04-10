import uuid
import os
import google.generativeai as genai
from dotenv import load_dotenv
from memory.vector_store import index

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class MemoryManager:
    def embed_text(self, text: str):
        try:
            response = genai.embed_content(
                model="models/embedding-001",
                content=text,
                task_type="retrieval_document"
            )
            return response['embedding']
        except Exception as e:
            print(f"[ERROR] Embedding failed: {e}")
            return []

    def store_memory(self, user_id: str, memory_text: str, assistant_reply: str):
        combined_text = f"User: {memory_text}\nAssistant: {assistant_reply}"
        embedding = self.embed_text(combined_text)
        if not embedding:
            print("[WARNING] No embedding generated, skipping memory store.")
            return

        unique_id = str(uuid.uuid4())
        index.upsert([
            (unique_id, embedding, {
                "user_id": user_id,
                "text": combined_text
            })
        ])
        print(f"[DEBUG] Stored memory with ID {unique_id}")

    def retrieve_memory(self, user_id: str, query_text: str, top_k: int = 3):
        query_vec = self.embed_text(query_text)
        if not query_vec:
            print("[WARNING] No query embedding generated, returning empty memory.")
            return ""

        results = index.query(
            vector=query_vec,
            top_k=top_k,
            include_metadata=True
        )
        user_memories = [
            match["metadata"]["text"]
            for match in results.get("matches", [])
            if match["metadata"].get("user_id") == user_id
        ]
        print(f"[DEBUG] Retrieved {len(user_memories)} memories.")
        return "\n".join(user_memories)
