from flask import Flask, request, jsonify

from app import create_app, db
from app.models import Conversation
import requests

app = create_app()


@app.route('/')
def home(): 
    return "Welcome to the Mental Mate ChatBot"


@app.route('/process', methods = ['POST'])
def process_input():
    user_input = request.json.get('input')    
    rasa_response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": user_input})    
    response_data = rasa_response.json()
    response_text = response_data[0]['text'] if response_data else "Sorry, I didn't get that."
    

    conversation = Conversation(user_input=user_input, response_text=response_text)
    db.session.add(conversation)
    db.session.commit()
    return jsonify({'response': response_text})


if __name__ == '__main__':
    app.run(debug = True)