from app import db

class User(db.Model):
    UID = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    goals = db.relationship('Goal', order_by='Goal.GID', back_populates='user')
    journal_entries = db.relationship('JournalEntry', order_by='JournalEntry.JID', back_populates='user')
    mood_tracking = db.relationship('MoodTracking', order_by='MoodTracking.MID', back_populates='user')
    conversations = db.relationship('Conversation', order_by='Conversation.CID', back_populates='user')
    requests = db.relationship('Request', order_by='Request.RID', back_populates='user')
    quizzes = db.relationship('Quiz', order_by='Quiz.QID', back_populates='user')

    def __init__(self, UID, username, email, password):
        self.UID = UID
        self.username = username
        self.email = email
        self.password = password

class Goal(db.Model):
    GID = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.String(50), db.ForeignKey('user.UID'), nullable=False)
    g_description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    user = db.relationship('User', back_populates='goals')

    def __init__(self, UID, g_description):
        self.UID = UID
        self.g_description = g_description

class JournalEntry(db.Model):
    JID = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.String(50), db.ForeignKey('user.UID'), nullable=False)
    entry_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    entry_text = db.Column(db.Text, nullable=False)
    user = db.relationship('User', back_populates='journal_entries')

    def __init__(self, UID, entry_text):
        self.UID = UID
        self.entry_text = entry_text

class MoodTracking(db.Model):
    MID = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.String(50), db.ForeignKey('user.UID'), nullable=False)
    mood_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    mood = db.Column(db.String(50), nullable=False)
    user = db.relationship('User', back_populates='mood_tracking')

    def __init__(self, UID, mood):
        self.UID = UID
        self.mood = mood

class Conversation(db.Model):
    CID = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.String(50), db.ForeignKey('user.UID'), nullable=False)
    conversation_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    conversation_text = db.Column(db.Text, nullable=False)
    user = db.relationship('User', back_populates='conversations')

    def __init__(self, UID, conversation_text):
        self.UID = UID
        self.conversation_text = conversation_text

class Request(db.Model):
    RID = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.String(50), db.ForeignKey('user.UID'), nullable=False)
    symptom = db.Column(db.Text, nullable=False)
    request_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    user = db.relationship('User', back_populates='requests')

    def __init__(self, UID, symptom):
        self.UID = UID
        self.symptom = symptom

class Quiz(db.Model):
    QID = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.String(50), db.ForeignKey('user.UID'), nullable=False)
    quiz_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    user = db.relationship('User', back_populates='quizzes')

    questions = db.relationship('Question', order_by='Question.question_id', back_populates='quiz')

    def __init__(self, UID):
        self.UID = UID

class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    QID = db.Column(db.Integer, db.ForeignKey('quiz.QID'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    quiz = db.relationship('Quiz', back_populates='questions')

    answers = db.relationship('Answer', order_by='Answer.answer_id', back_populates='question')

    def __init__(self, QID, question_text):
        self.QID = QID
        self.question_text = question_text

class Answer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.question_id'), nullable=False)
    answer_text = db.Column(db.Text, nullable=False)
    question = db.relationship('Question', back_populates='answers')

    def __init__(self, question_id, answer_text):
        self.question_id = question_id
        self.answer_text = answer_text

class Intent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intent_name = db.Column(db.String(50), nullable=False)
    examples = db.Column(db.Text, nullable=False)
    responses = db.Column(db.Text, nullable=False)

    def __init__(self, intent_name, examples, responses):
        self.intent_name = intent_name
        self.examples = examples
        self.responses = responses

User.goals = db.relationship('Goal', order_by=Goal.GID, back_populates='user')
User.journal_entries = db.relationship('JournalEntry', order_by=JournalEntry.JID, back_populates='user')
User.mood_tracking = db.relationship('MoodTracking', order_by=MoodTracking.MID, back_populates='user')
User.conversations = db.relationship('Conversation', order_by=Conversation.CID, back_populates='user')
User.requests = db.relationship('Request', order_by=Request.RID, back_populates='user')
User.quizzes = db.relationship('Quiz', order_by=Quiz.QID, back_populates='user')
Quiz.questions = db.relationship('Question', order_by=Question.question_id, back_populates='quiz')
Question.answers = db.relationship('Answer', order_by=Answer.answer_id, back_populates='question')
