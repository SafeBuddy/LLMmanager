from flask import Flask
import google.generativeai as genai
import os

app = Flask(__name__)


genai.configure(api_key=os.getenv("GENAI_API_KEY"))


prompt = "Analyze the following text for evidence of verbal abuse or grooming. If either is present, identify: \n" \
         "1. Who is the aggressor and who is the victim. \n" \
         "2. Assign a severity score from 1 to 10 based on the intensity and frequency of the behavior, where: \n" \
         "1-3: Mild (isolated incident, minor impact). \n" \
         "4-7: Moderate (repeated behavior, potentially harmful). \n" \
         "8-10: Severe (persistent or highly damaging behavior, significant impact). \n" \
         "Please return the answer in the following format: \n" \
         "Aggressor: [Insert aggressor’s name or identifier here] \n" \
         "Severity score: [Insert numerical score here] and thats it no more text"



example_data = (
    "Side A: \"You're such a loser. Everyone hates you. Why don't you just leave already?\" "
    "Side B: \"Please stop talking to me like that. I don't deserve this.\" "
    "Side A: \"Oh, cry me a river. You're worthless and pathetic. Nobody cares about you.\" "
    "Side B: \"This is really upsetting. Please stop.\" "
    "Side A: \"You’re so dramatic. Just disappear already.\""
)


@app.route('/generate', methods=['GET'])
def generate():
    # model = genai.GenerativeModel('gemini-1.5-flash')
    # combined = prompt + "/n" + example_data
    # response = model.generate_content(combined)
    # return f"<h1>{response.text}</h1>"
    return "<h1>hello from generate</h1>"

if __name__ == '_main_':
    app.run(debug=True,port=8080)