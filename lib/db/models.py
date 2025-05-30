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

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    biography = Column(String)

    books = relationship("Book", back_populates="author", cascade="all, delete")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    year = Column(Integer)

    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")

    loans = relationship("Loan", back_populates="book", cascade="all, delete")

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

    loans = relationship("Loan", back_populates="member", cascade="all, delete")

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    loan_date = Column(DateTime)
    return_date = Column(DateTime)

    member_id = Column(Integer, ForeignKey("members.id"))
    member = relationship("Member", back_populates="loans")

    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="loans")