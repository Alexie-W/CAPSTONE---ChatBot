import csv # Library for reading and writing CSV files
from app import create_app, db # Import application factory and database instance
from app.models import User, Goal, JournalEntry, MoodTracking, Request, Quiz, Question, Answer, Intent

app = create_app()  # Create an application instance
app.app_context().push() # Push application context for using database

def populate_users_from_csv(csv_file_path):
    """
    Populate the User table with data from a CSV file.
    
    Args:
        csv_file_path (str): Path to the CSV file containing user data.
    """
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_user = User(
                UID=row['uid'],
                username=row['username'],
                email=row['email'],
                password=row['password']
            )
            db.session.add(new_user)  # Add new user to the database session
        db.session.commit() # Commit the transaction to the database
    print('Users added successfully from CSV.')

def populate_goals_from_csv(csv_file_path):
    with open(csv_file_path, newline='') as csvfile: # Populate the Goal table with data from a CSV file.
        reader = csv.DictReader(csvfile) # Read CSV file into a dictionary format
        for row in reader:
            new_goal = Goal(
                UID=row['uid'],
                g_description=row['goal_description']
            )
            db.session.add(new_goal) # Add new goal to the database session
        db.session.commit() # Commit the transaction to the database
    print('Goals added successfully from CSV.')

def populate_journal_entries_from_csv(csv_file_path): # Populate the JournalEntry table with data from a CSV file.
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile) # Read CSV file into a dictionary format
        for row in reader:
            new_journal_entry = JournalEntry(
                UID=row['uid'],
                entry_text=row['entry_text']
            )
            db.session.add(new_journal_entry) # Add new journal entry to the database session
        db.session.commit()  # Commit the transaction to the database
    print('Journal entries added successfully from CSV.')


 #Populate the MoodTracking table with data from a CSV file and adding to database
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

 #Populate the Request table with data from a CSV file and adding to database
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

 #Populate the Quiz table with data from a CSV file and adding to database
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

 #Populate the Question table with data from a CSV file and adding to database
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

 #Populate the Answer table with data from a CSV file and adding to database
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

 #Populate the Intent table with data from a CSV file and adding to database
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

  # Populate database tables from respective CSV files
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
