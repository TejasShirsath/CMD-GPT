from flask import Flask, request
from urllib.parse import unquote
import google.generativeai as genai
import os

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key = os.getenv("api_key"))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_answer():
    question =request.args.get('question')
    decoded_question = unquote(question) if question else ""
    answer = generate_answer(decoded_question)
    return answer

def generate_answer(question):
    try:
        model = genai.GenerativeModel('models/gemini-pro')
        response = model.generate_content(question).text
        return response
    except:
        return "Sorry, I'm unable to provide an answer."
    
if __name__ == '__main__':
    app.run(debug=True)
