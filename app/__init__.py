from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder='C:/Users/ebank/Documents/GitHub/CAPSTONE---ChatBot/CAPSTONE---ChatBot/frontend/dist', static_url_path='')
    app.config.from_object(Config)
    
    db.init_app(app)

    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            app.logger.error(f"Error creating database tables: {e}")

    return app
