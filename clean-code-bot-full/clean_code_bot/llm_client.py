import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not set")

client = Groq(api_key=api_key)

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        messages=[
            {"role": "system", "content": "You are a senior software engineer."},
            {"role": "user", "content": prompt}
        ],
        temperature=float(os.getenv("GROQ_TEMPERATURE", 0.2))
    )

    return response.choices[0].message.content
