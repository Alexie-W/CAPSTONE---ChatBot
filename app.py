from flask import Flask, request, jsonify, send_from_directory
from app import create_app, db
from app.models import Conversation, User, Goal, JournalEntry, MoodTracking, Request, Quiz, Question, Answer
from flask_cors import CORS
import requests


app = create_app()
CORS(app)

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/chatbot', methods=['POST'])
def process_input():
    user_input = request.json.get('message')
    user_id = request.json.get('_v7ttyvkg8')

    # Find a matching pattern
    response = match_intent(user_input, intents)

    return jsonify({'response': response})

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(UID=data['UID'], username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email'], password=data['password']).first()
    if user:
        return jsonify({'message': 'Login successful', 'UID': user.UID})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/journal', methods=['POST'])
def add_journal_entry():
    data = request.json
    journal_entry = JournalEntry(UID=data['UID'], entry_text=data['entry_text'])
    db.session.add(journal_entry)
    db.session.commit()
    return jsonify({'message': 'Journal entry added successfully'})

@app.route('/journal/<UID>', methods=['GET'])
def view_journal_entries(UID):
    journal_entries = JournalEntry.query.filter_by(UID=UID).all()
    entries = [{'JID': entry.JID, 'entry_date': entry.entry_date, 'entry_text': entry.entry_text} for entry in journal_entries]
    return jsonify({'journal_entries': entries})

@app.route('/mood', methods=['POST'])
def add_mood():
    data = request.json
    mood_entry = MoodTracking(UID=data['UID'], mood=data['mood'])
    db.session.add(mood_entry)
    db.session.commit()
    return jsonify({'message': 'Mood entry added successfully'})

@app.route('/mood/<UID>', methods=['GET'])
def view_mood_entries(UID):
    mood_entries = MoodTracking.query.filter_by(UID=UID).all()
    entries = [{'MID': entry.MID, 'mood_date': entry.mood_date, 'mood': entry.mood} for entry in mood_entries]
    return jsonify({'mood_entries': entries})

@app.route('/goal', methods=['POST'])
def add_goal():
    data = request.json
    goal = Goal(UID=data['UID'], g_description=data['g_description'])
    db.session.add(goal)
    db.session.commit()
    return jsonify({'message': 'Goal added successfully'})

@app.route('/goal/<UID>', methods=['GET'])
def view_goals(UID):
    goals = Goal.query.filter_by(UID=UID).all()
    entries = [{'GID': goal.GID, 'g_description': goal.g_description, 'date_created': goal.date_created} for goal in goals]
    return jsonify({'goals': entries})

@app.route('/conversations/<UID>', methods=['GET'])
def view_conversations(UID):
    conversations = Conversation.query.filter_by(UID=UID).all()
    entries = [{'id': conv.id, 'user_input': conv.user_input, 'response_text': conv.response_text, 'conversation_date': conv.conversation_date} for conv in conversations]
    return jsonify({'conversations': entries})

@app.route('/request', methods=['POST'])
def add_request():
    data = request.json
    request_entry = Request(UID=data['UID'], symptom=data['symptom'])
    db.session.add(request_entry)
    db.session.commit()
    return jsonify({'message': 'Request added successfully'})

@app.route('/request/<UID>', methods=['GET'])
def view_requests(UID):
    requests = Request.query.filter_by(UID=UID).all()
    entries = [{'RID': req.RID, 'symptom': req.symptom, 'request_date': req.request_date} for req in requests]
    return jsonify({'requests': entries})

@app.route('/quiz', methods=['POST'])
def add_quiz():
    data = request.json
    quiz = Quiz(UID=data['UID'])
    db.session.add(quiz)
    db.session.commit()
    for question_data in data['questions']:
        question = Question(QID=quiz.QID, question_text=question_data['question_text'])
        db.session.add(question)
        db.session.commit()
        for answer_text in question_data['answers']:
            answer = Answer(question_id=question.question_id, answer_text=answer_text)
            db.session.add(answer)
            db.session.commit()
    return jsonify({'message': 'Quiz added successfully'})

@app.route('/quiz/<UID>', methods=['GET'])
def view_quizzes(UID):
    quizzes = Quiz.query.filter_by(UID=UID).all()
    entries = [{'QID': quiz.QID, 'quiz_date': quiz.quiz_date} for quiz in quizzes]
    return jsonify({'quizzes': entries})

import csv
import random
from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import word_tokenize

# Ensure NLTK resources are downloaded
nltk.download('punkt')

def load_intents(filename):
    intents = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tag = row['tags']
            patterns = row['patterns'].split('|')
            responses = row['responses'].split('|')
            intents[tag] = {'patterns': patterns, 'responses': responses}
    return intents

def match_intent(user_input, intents):
    tokenized_input = word_tokenize(user_input.lower())
    for tag, intent in intents.items():
        for pattern in intent['patterns']:
            tokenized_pattern = word_tokenize(pattern.lower())
            if set(tokenized_pattern).issubset(set(tokenized_input)):
                return random.choice(intent['responses'])
    return "I'm sorry, I don't understand."






# Load intents
intents = load_intents('intents.csv')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = match_intent(user_input, intents)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
