# Library Management CLI Project

## Project Overview

This project is a Command Line Interface (CLI) application for managing a library system. It allows users to manage authors, books, members, loans, and fines through an interactive menu-driven interface.

The application uses Python with SQLAlchemy ORM for database interactions and Alembic for database migrations. The database is SQLite-based for simplicity.

## Directory Structure

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py            # Main CLI application script
    ├── db
    │   ├── models.py     # SQLAlchemy ORM models for database tables
    │   ├── seed.py       # Script to seed the database with initial data (optional)
    │   └── migrations    # Alembic migration scripts for database schema changes
    ├── debug.py          # Debugging utilities (if any)
    └── helpers.py        # Helper functions used by the CLI
```

## Setup and Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd library-Management-CLI-Project
```

2. **Set up Python environment**

This project uses Pipenv for dependency management. Install Pipenv if you don't have it:

```bash
pip install pipenv
```

3. **Install dependencies**

```bash
pipenv install
```

4. **Activate the virtual environment**

```bash
pipenv shell
```

5. **Initialize the database**

Run the CLI and choose option 1 to initialize the database schema:

```bash
python3 lib/cli.py
```

Select:

```
1. Init DB
```

This will create the necessary tables in the SQLite database.

## Usage

Run the CLI application:

```bash
python3 lib/cli.py
```

You will see a menu with the following options:

```
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
```

### Menu Options Description

- **Init DB**: Initializes the database schema.
- **Add Author**: Add a new author with name and biography.
- **List Authors**: Display all authors.
- **Add Book**: Add a new book with title, genre, publication year, and author.
- **List Books**: Display all books with details.
- **Add Member**: Add a new library member with name, email, and phone.
- **List Members**: Display all members.
- **Add Loan**: Record a new loan of a book to a member with loan and due dates.
- **List Loans**: Display all current loans.
- **Add Fine**: Add a fine for a member with amount, reason, and date.
- **List Fines**: Display all fines for members.
- **Exit**: Exit the CLI application.

### Input Formats

- Dates should be entered in `YYYY-MM-DD` format.
- Amounts for fines should be entered as integers (e.g., 500).

## Database

The project uses SQLite database located at `lib/db/library.db`. The schema is managed using SQLAlchemy models and Alembic migrations.

## Development Notes

- The CLI is implemented in `lib/cli.py`.
- Database models are defined in `lib/db/models.py`.
- Alembic is used for database migrations (`lib/db/migrations`).
- Helper functions and debugging utilities are in `lib/helpers.py` and `lib/debug.py`.

## Contributing

Feel free to fork the project and submit pull requests. Please ensure code quality and test thoroughly.

## License

This project is open source and available under the MIT License.

## Resources

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

---

Happy coding and managing your library!
