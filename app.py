from flask import Flask, jsonify, request
from services.generative import analyze_text

app = Flask(__name__)

@app.route('/check-messages', methods=['POST'])
def check_messages():
    data = request.json
    if not data or 'messages' not in data:
        return jsonify({"error": "Invalid request. 'messages' field is required."}), 400

    message = data['messages']

    try:
        response_json = analyze_text(message)
        return jsonify(response_json), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
