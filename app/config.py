import os

#Configuration class for setting up the Flask application and SQLAlchemy.
class Config:
     # URI for connecting to the MySQL database using the mysqlconnector driver
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:#PromiseWayne001@localhost:3306/mental_mate'
    # Disable SQLAlchemy event system for tracking modifications to objects and emit signals
    SQLALCHEMY_TRACK_MODIFICATIONS = False
