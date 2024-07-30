import csv
from app import create_app, db
from app.models import User, Goal, JournalEntry, MoodTracking, Request, Quiz, Question, Answer, Intent

app = create_app()
app.app_context().push()

def populate_users_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_user = User(
                UID=row['uid'],
                username=row['username'],
                email=row['email'],
                password=row['password']
            )
            db.session.add(new_user)
        db.session.commit()
    print('Users added successfully from CSV.')

def populate_goals_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_goal = Goal(
                UID=row['uid'],
                g_description=row['goal_description']
            )
            db.session.add(new_goal)
        db.session.commit()
    print('Goals added successfully from CSV.')

def populate_journal_entries_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_journal_entry = JournalEntry(
                UID=row['uid'],
                entry_text=row['entry_text']
            )
            db.session.add(new_journal_entry)
        db.session.commit()
    print('Journal entries added successfully from CSV.')

def populate_mood_tracking_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_mood_entry = MoodTracking(
                UID=row['uid'],
                mood=row['mood_description']
            )
            db.session.add(new_mood_entry)
        db.session.commit()
    print('Mood entries added successfully from CSV.')

def populate_requests_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_request = Request(
                UID=row['uid'],
                symptom=row['request_description']
            )
            db.session.add(new_request)
        db.session.commit()
    print('Requests added successfully from CSV.')

def populate_quizzes_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_quiz = Quiz(
                UID=row['uid']
            )
            db.session.add(new_quiz)
        db.session.commit()
    print('Quizzes added successfully from CSV.')

def populate_questions_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_question = Question(
                QID=row['qid'],
                question_text=row['question_text']
            )
            db.session.add(new_question)
        db.session.commit()
    print('Questions added successfully from CSV.')

def populate_answers_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_answer = Answer(
                question_id=row['question_id'],
                answer_text=row['answer_text']
            )
            db.session.add(new_answer)
        db.session.commit()
    print('Answers added successfully from CSV.')

def populate_intents_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_intent = Intent(
                intent_name=row['tag'],
                examples=row['patterns'],
                responses=row['responses']
            )
            db.session.add(new_intent)
        db.session.commit()
    print('Intents added successfully from CSV.')

if __name__ == "__main__":
    populate_users_from_csv('users.csv')
    populate_goals_from_csv('goals.csv')
    populate_journal_entries_from_csv('journal_entries.csv')
    populate_mood_tracking_from_csv('mood_tracking.csv')
    populate_requests_from_csv('requests.csv')
    populate_quizzes_from_csv('quizzes.csv')
    populate_questions_from_csv('questions.csv')
    populate_answers_from_csv('answers.csv')
    populate_intents_from_csv('intents.csv')
