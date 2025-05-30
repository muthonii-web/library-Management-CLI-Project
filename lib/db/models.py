# lib/db/models.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "library.db")
DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from sqlalchemy.orm import relationship, declarative_base