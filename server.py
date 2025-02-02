from flask import Flask, request
from urllib.parse import unquote
import google.generativeai as genai
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

# Replace 'os.getenv("api_key")' with your actual Gemini API Key
genai.configure(api_key = os.getenv("api_key"))

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_answer():
    question = request.args.get('question')
    decoded_question = unquote(question) if question else ""
    answer = generate_answer(decoded_question)
    return answer

def generate_answer(question):
    try:
        model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return "Sorry, I'm unable to provide an answer."

if __name__ == '__main__':
    app.run(debug=True)
