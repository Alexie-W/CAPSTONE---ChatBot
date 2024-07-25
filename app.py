from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home(): 
    return "Welcome to the Mental Mate ChatBot"


@app.route('/process', methods = ['POST'])
def process_input():
    user_input = request.json.get('input')
    
    rasa_response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": user_input})

    
    response_data = rasa_response.json()
    response_text = response_data[0]['text'] if response_data else "Sorry, I didn't get that."
    
        # Placeholder for processing user input
    intent = "anxious"  # Replace with actual intent from NLU model
    mood = "anxious"  # Replace with actual mood analysis result

    # Log the interaction (You can replace this with your DB interaction)
    print(f"User Input: {user_input}, Response: {response_text}, Intent: {intent}, Mood: {mood}")

    return jsonify({'response': response_text})


if __name__ == '__main__':
    app.run(debug = True)