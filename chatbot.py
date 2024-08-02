from flask import Flask, request, jsonify
from app import create_app
from app.models import get_user_requests, get_user_quizzes, get_quiz_questions

# Create an instance of the Flask application
app = create_app()

  # Endpoint to handle chatbot interactions
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    user_id = request.json.get('user_id')  # Assuming user_id 

     # Determine response based on user input
    if "show me my requests" in user_input.lower():
        response = generate_requests_response(user_id)
    elif "start a new quiz" in user_input.lower():
        quiz_id = extract_quiz_id(user_input) # Extract quiz ID from user input
        response = generate_first_question_response(quiz_id)
    elif "show me my quizzes" in user_input.lower():
        response = generate_quizzes_response(user_id)
    else:
        response = "I'm sorry, I don't understand that."

    return jsonify({"response": response})

 # Generate a response listing all user requests
def generate_requests_response(user_id):
    requests = get_user_requests(user_id)
    if not requests:
        return "You have no requests."
    response = "Here are your requests:\n"
    for req in requests:
        response += f"- {req.symptom} (Date: {req.request_date})\n"
    return response

 # Generate a response listing all user quizzes
def generate_quizzes_response(user_id):
    quizzes = get_user_quizzes(user_id)
    if not quizzes:
        return "You have no quizzes."
    response = "Here are your quizzes:\n"
    for quiz in quizzes:
        response += f"- Quiz ID: {quiz.QID} (Date: {quiz.quiz_date})\n"
    return response

# Generate the first question of a specified quiz
def generate_first_question_response(quiz_id):
    questions = get_quiz_questions(quiz_id)
    if not questions:
        return "This quiz has no questions."
    first_question = questions[0]
    return f"Here is your first question: {first_question.question_text}"

 # Extract quiz ID from user input
def extract_quiz_id(user_input):
    # placeholder implementation
    return int(user_input.split()[-1])

if __name__ == '__main__':
    app.run(debug=True)
