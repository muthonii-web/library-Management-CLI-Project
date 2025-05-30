# lib/cli.py

from db.models import (
    Base, engine, Session,
    Author, Book, Member, Loan, Fine
)
from datetime import datetime

session = Session()

# === INIT DB ===
def init_db():
    Base.metadata.create_all(engine)
    print("\n Database initialized!")


# === HELPERS ===
def input_date(prompt="Enter date (YYYY-MM-DD): "):
    date_str = input(prompt)
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return None


# === AUTHOR ===
def add_author():
    print("\n Add Author")
    name = input("Name: ")
    biography = input("Biography: ")
    
    author = Author(name=name, biography=biography)
    session.add(author)
    session.commit()
    print(f"Author '{name}' added.")


def list_authors():
    print("\n Authors")
    for a in session.query(Author).all():
        print(f"{a.id}: {a.name} - {a.biography}")


# === BOOK ===
def add_book():
    print("\n Add Book")
    title = input("Title: ")
    genre = input("Genre: ")
    publication_year = input("Publication Year: ")
    
    list_authors()
    author_id = int(input("Author ID: "))
    author = session.get(Author, author_id)
    
    book = Book(title=title, genre=genre, year=publication_year, author=author)
    session.add(book)
    session.commit()
    print(f" Book '{title}' added.")


def list_books():
    print("\n Books")
    for b in session.query(Book).all():
        print(f"{b.id}: {b.title} ({b.year}) - {b.genre} by {b.author.name}")


# === MEMBER ===
def add_member():
    print("\n Add Member")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    
    member = Member(name=name, email=email, phone=phone)
    session.add(member)
    session.commit()
    print(f"Member '{name}' added.")


def list_members():
    print("\n Members")
    for m in session.query(Member).all():
        print(f"{m.id}: {m.name} | {m.email} | {m.phone}")


# === LOAN ===
def add_loan():
    print("\n Add Loan")
    list_books()
    book_id = int(input("Book ID: "))
    book = session.get(Book, book_id)
    
    list_members()
    member_id = int(input("Member ID: "))
    member = session.get(Member, member_id)

    loan_date = input_date("Loan Date (YYYY-MM-DD): ")
    due_date = input_date("Due Date (YYYY-MM-DD): ")

    loan = Loan(book=book, member=member, loan_date=loan_date, return_date=due_date)
    session.add(loan)
    session.commit()
    print(" Loan added.")


def list_loans():
    print("\n Current Loans")
    for l in session.query(Loan).all():
        print(f"{l.id}: {l.book.title} loaned to {l.member.name} on {l.loan_date.date()} (Due: {l.return_date.date()})")

def add_fine():
    print("\n Add Fine")
    list_members()
    member_id = int(input("Member ID: "))
    member = session.get(Member, member_id)

    amount = int(input("Amount (in Ksh): "))
    reason = input("Reason: ")
    date = input_date("Date of Fine (YYYY-MM-DD): ")

    fine = Fine(member=member, amount=amount, reason=reason, date_issued=date)
    session.add(fine)
    session.commit()
    print(f" Fine of Ksh. {amount} added for {member.name}.")

def list_fines():
    print("\n Member Fines")
    fines = session.query(Fine).all()
    if not fines:
        print(" No fines found.")
    else:
        for f in fines:
            print(f"{f.id}: {f.member.name} - Ksh. {f.amount} for '{f.reason}' on {f.date_issued.date()}")


# === MAIN MENU ===
def menu():
    print("\n Library CLI")
    while True:
        print("""
==============================
1. Init DB
2. Add Author
3. List Authors
4. Add Book
5. List Books
6. Add Member
7. List Members
8. Add Loan
9. List Loans
10. Add Fine
11. List Fines
12. Exit
==============================
""")
        choice = input("Choose an option: ").strip()

        if choice == '1': init_db()
        elif choice == '2': add_author()
        elif choice == '3': list_authors()
        elif choice == '4': add_book()
        elif choice == '5': list_books()
        elif choice == '6': add_member()
        elif choice == '7': list_members()
        elif choice == '8': add_loan()
        elif choice == '9': list_loans()
        elif choice == '10': add_fine()
        elif choice == '11': list_fines()
        elif choice == '12':
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    menu()
