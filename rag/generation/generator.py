import requests

def generate_answer(query, docs, history=""):
    """
    Generates answer using local Ollama model (phi3 / mistral / llama3).
    Safe parsing included for all response formats.
    """

    # Build context from retrieved docs
    context = "\n\n".join([d["text"] for d in docs])

    # Prompt with memory + context
    prompt = f"""
You are a helpful AI assistant.

You answer ONLY using the provided document context.

If the answer is not in the context, say:
"Not found in document"

--- Conversation History ---
{history}

--- Document Context ---
{context}

--- User Question ---
{query}
"""

    # Call Ollama API
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",   # 👈 your current model
            "prompt": prompt,
            "stream": False
        }
    )

    # Parse response safely
    data = response.json()

    # ✅ Handle different Ollama response formats safely
    if isinstance(data, dict):
        if "response" in data:
            return data["response"]

        if "message" in data:
            return data["message"]

        if "error" in data:
            return f"❌ Ollama error: {data['error']}"

    # fallback (debug)
    return str(data)