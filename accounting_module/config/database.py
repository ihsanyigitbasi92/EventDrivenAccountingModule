
"""
Database connection setup.
"""

from sqlalchemy import create_engine
from config.settings import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
