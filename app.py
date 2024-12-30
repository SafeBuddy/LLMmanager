from flask import Flask
import google.generativeai as genai
import os

app = Flask(_name_)


genai.configure(api_key=os.getenv("GENAI_API_KEY"))


data = "What is the name of the king of england?"

@app.route('/generate', methods=['GET'])
def generate():
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(data)
    return f"<h1>{response.text}</h1>"

if _name_ == '_main_':
    app.run(debug=True,port=8080)