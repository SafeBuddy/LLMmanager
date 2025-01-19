import google.generativeai as genai
import json
from prompt import prompt

def analyze_text(message):
    model = genai.GenerativeModel('gemini-1.5-flash')
    combined = prompt + "\n" + message

    try:
        response = model.generate_content(combined, generation_config=genai.GenerationConfig(response_mime_type="application/json"))
        return json.loads(response.text)
    except json.JSONDecodeError:
        raise ValueError("Failed to decode the model's response as JSON.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")
