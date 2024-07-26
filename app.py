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
    mm_response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": user_input})    
    response_data = mm_response.json()
    response = response_data[0]['text'] if response_data else "Sorry, I did not understand."
    

    conversation = Conversation(user_input=user_input, response=response)
    db.session.add(conversation)
    db.session.commit()
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug = True)