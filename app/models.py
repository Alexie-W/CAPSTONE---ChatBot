from app import db

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(255), nullable=False)
    response_text = db.Column(db.String(255), nullable=False)


    def __init__(self, user_input, response_text):
        self.user_input = user_input
        self.response_text = response_text
