
"""
Business logic for handling account operations.
"""

from app.models import Account
from sqlalchemy.orm import sessionmaker
from config.database import engine

Session = sessionmaker(bind=engine)
session = Session()

def get_accounts():
    accounts = session.query(Account).all()
    return [account.name for account in accounts]
