import os

api_key = os.getenv("GENAI_API_KEY")

if not api_key:
    raise ValueError("The API key is not provided. Please add the API key to the environment.")
