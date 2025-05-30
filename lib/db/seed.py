from datetime import datetime, timedelta
from models import Session, Base, engine, Author, Book, Member, Loan, Fine


# Drop all tables and recreate them (for development only!)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session()

# Authors
author1 = Author(name="Chinua Achebe", biography="Nigerian novelist and author of 'Things Fall Apart'.")
author2 = Author(name="J.K. Rowling", biography="British author of the Harry Potter series.")

# Books
book1 = Book(title="Things Fall Apart", genre="Historical Fiction", year=1958, author=author1)
book2 = Book(title="Harry Potter and the Sorcerer's Stone", genre="Fantasy", year=1997, author=author2)

# Members
member1 = Member(name="John Doe", email="john@example.com", phone="0700000001")
member2 = Member(name="Jane Smith", email="jane@example.com", phone="0700000002")

# Loans
loan1 = Loan(loan_date=datetime.now() - timedelta(days=7), return_date=datetime.now() + timedelta(days=7),
             member=member1, book=book1)

loan2 = Loan(loan_date=datetime.now() - timedelta(days=14), return_date=datetime.now() - timedelta(days=2),
             member=member2, book=book2)

# Fines
fine1 = Fine(amount=300, reason="Late return", date_issued=datetime.now(), member=member2)


session.add_all([author1, author2, book1, book2, member1, member2, loan1, loan2, fine1])
session.commit()

print("Database seeded successfully!")
