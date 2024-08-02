from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Initialize the SQLAlchemy object for use with the Flask application
db = SQLAlchemy()

#Factory function to create and configure a Flask application instance.
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # Load configuration from Config class
    
    db.init_app(app) # Initialize the SQLAlchemy object with the Flask app

    with app.app_context():
        try:
            db.create_all() # Create database tables based on the defined models
        except Exception as e:
            app.logger.error(f"Error creating database tables: {e}") # Log any errors during table creation

    return app
