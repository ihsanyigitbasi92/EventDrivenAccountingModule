
"""
Application configuration settings.
"""

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/dbname'
    SECRET_KEY = 'your_secret_key'
