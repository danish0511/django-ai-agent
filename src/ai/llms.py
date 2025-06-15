from langchain_google_genai import ChatGoogleGenerativeAI
from django.conf import settings


def get_gemini_api_key():
    return settings.GOOGLE_API_KEY

def get_gemini_model(model="gemini-2.0-flash"):
    
    return ChatGoogleGenerativeAI(
        model=model,
        temperature=0,
        max_retries=2,
        api_key=get_gemini_api_key(),
    )
