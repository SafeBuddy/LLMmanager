from flask import Flask, jsonify, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure the Generative AI client with the API key
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

# Prompt template
prompt = (
    "Analyze the following text for evidence of verbal abuse or grooming. If either is present, identify:\n"
    "1. Who is the aggressor and who is the victim.\n"
    "2. Assign a severity score from 0 to 2 based on the intensity and frequency of the behavior, where:\n"
    "0: No abuse or grooming.\n"
    "1: Moderate (repeated behavior, potentially harmful).\n"
    "2: Severe (persistent or highly damaging behavior, significant impact).\n"
    "Please return the answer in valid JSON format as follows:\n"
    "{\n"
    "  \"Aggressor\": \"[Insert aggressor’s name or identifier here if there is no one write null]\",\n"
    "  \"Severity score\": [Insert numerical score here]\n"
    "}\n"
    "Only return valid JSON, with no additional text or commentary."
)


# Example data
# example_data = (
#     "Side A: \"You're such a loser. Everyone hates you. Why don't you just leave already?\" "
#     "Side B: \"Please stop talking to me like that. I don't deserve this.\" "
#     "Side A: \"Oh, cry me a river. You're worthless and pathetic. Nobody cares about you.\" "
#     "Side B: \"This is really upsetting. Please stop.\" "
#     "Side A: \"You’re so dramatic. Just disappear already.\""
# )

@app.route('/check-messages', methods=['POST'])
def check_messages():
    data = request.json
    if not data or 'messages' not in data:
        return jsonify({"error": "Invalid request. 'message' field is required."}), 400
    message = data['messages']
    model = genai.GenerativeModel('gemini-1.5-flash')
    combined = prompt + "/n" + message
    response = model.generate_content(combined)
    return response.text



if __name__ == '_main_':
    app.run(debug=True,port=8080)