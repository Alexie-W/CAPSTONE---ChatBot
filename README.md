

- in the intents.csv, i wasnt sure what wouldve been used to store the journal entries, quizzes, questions, requests , mood entries etc. , in the backend, so i put place holders. These should be replaced with actual calls to fetch jounral entries.

eg: view_mood_entries,List my mood entries,"['Here are your mood entries: {mood_entries}']"

app.py
- Includes routes for user registration, login, journal entries, mood entries, goals, conversations, requests, and quizzes.

chatbot.py
- Manages the chatbot interface and interactions with the Rasa server.
- Sends user inputs to the Rasa webhook and processes the responses.

create_tables.sql
- creates tables

populate_database.py (basically just for testing)
- Inserts records into the users, goals, journal entries, mood tracking, requests, quizzes, questions, and answers tables.

