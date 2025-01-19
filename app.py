from flask import Flask, jsonify, request
import google.generativeai as genai
import os
import json

app = Flask(__name__)


api_key = os.getenv("GENAI_API_KEY")


if not api_key:
    raise ValueError("The API key is not provided. Please add the API key to the environment.")
else:
    genai.configure(api_key=api_key)


prompt = (
    "Analyze the following text for evidence of verbal abuse or grooming. If either is present, identify:\n"
    "1. Who is the aggressor and who is the victim.\n"
    "2. Assign a severity score from 0 to 2 based on the intensity and frequency of the behavior, where:\n"
    "0: No abuse or grooming.\n"
    "1: Moderate (repeated behavior, potentially harmful).\n"
    "2: Severe (persistent or highly damaging behavior, significant impact).\n"
    "Please return the answer in valid JSON format as follows:\n"
    "{\n"
    "  \"aggressor\": \"[Insert aggressor’s name or identifier here, or write null if there is no one]\",\n"
    "  \"severity\": [Insert numerical score here]\n"
    "}\n"
    "Only return valid JSON, with no additional text or commentary."
)



# Example data
# example_data = (
    # "Side A: \"You're such a loser. Everyone hates you. Why don't you just leave already?\" "
    # "Side B: \"Please stop talking to me like that. I don't deserve this.\" "
    # "Side A: \"Oh, cry me a river. You're worthless and pathetic. Nobody cares about you.\" "
    # "Side B: \"This is really upsetting. Please stop.\" "
    # "Side A: \"You’re so dramatic. Just disappear already.\""
# )

@app.route('/check-messages', methods=['POST'])
def check_messages():
    data = request.json
    if not data or 'messages' not in data:
        return jsonify({"error": "Invalid request. 'messages' field is required."}), 400
    
    message = data['messages']
    model = genai.GenerativeModel('gemini-1.5-flash')
    combined = prompt + "\n" + message  # תיקון newline

    try:
        response = model.generate_content(combined, generation_config=genai.GenerationConfig(response_mime_type="application/json"))
        # המרה של התגובה מ-JSON string למילון
        response_json = json.loads(response.text)
        return jsonify(response_json), 200
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to decode the model's response as JSON."}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '_main_':
    app.run(debug=True,port=5000)