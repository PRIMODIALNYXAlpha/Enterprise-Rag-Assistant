from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("❌ GROQ_API_KEY not found")

    return ChatGroq(
        groq_api_key=api_key,
        model="llama-3.3-70b-versatile",  # ✅ FIXED PARAM NAME
        temperature=0.2
    )