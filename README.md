#  Smart Library Management System

A desktop-based Library Management System developed using Python, Tkinter, and Oracle Database.

This project demonstrates Python application development, relational database design, SQL operations, and integration between Python and Oracle Database.

##  Project Objective

The objective is to develop a library management application that simplifies book management, member records, borrowing and returning books, fine management, and reservations.

##  Technology Stack

- Python
- Tkinter and ttk
- Oracle Database
- Oracle Database Python Driver (`oracledb`)
- SQL
- python-dotenv
- Git and GitHub

##  Features

- View and search books
- Add and edit book details
- View and search library members
- Issue books to members
- Renew active loans
- Return borrowed books
- Calculate overdue fines automatically
- Record fine payments
- Manage book reservations
- Store and retrieve data using Oracle Database
- Use database transactions for related operations

##  Database Design

The project uses Oracle Database with 12 relational tables:

1. USERS
2. MEMBERS
3. AUTHORS
4. CATEGORIES
5. PUBLISHERS
6. BOOKS
7. BOOK_AUTHORS
8. BOOK_COPIES
9. LOANS
10. FINES
11. FINE_PAYMENTS
12. BOOK_RESERVATIONS

The schema uses primary keys, foreign keys, unique constraints, check constraints, and indexes to support data integrity and database operations.

##  Application Architecture

The application follows a modular structure:

- **GUI Layer:** Tkinter and ttk interfaces
- **Service Layer:** Application logic and validation
- **Database Layer:** Oracle connections and SQL queries
- **Database:** Oracle relational tables

##  Project Structure

```text
Smart_Library/
├── app/
│   ├── database/
│   ├── services/
│   ├── gui/
│   └── exceptions.py
├── database/
│   └── sql/
├── tests/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

##  Prerequisites

Before running the application, install:

- Python 3.13 or a compatible Python version
- Oracle Database with the `XEPDB1` service available
- Oracle SQL Developer (recommended for database setup)
- Git (optional)

##  Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Smart-Library-Management-System
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template.

Configure your Oracle credentials:

```dotenv
ORACLE_USER=your_oracle_username
ORACLE_PASSWORD=your_oracle_password
ORACLE_DSN=localhost:1521/XEPDB1
```

Replace the placeholders with your own Oracle database details.

Never commit your `.env` file or database password.

### 4. Set up the database

Open the SQL scripts in `database/sql/` using Oracle SQL Developer.

Run the scripts in the correct order, using a dedicated project database user with the required permissions.

If you use a different Oracle username or service, update your environment configuration accordingly.

### 5. Run the application

```bash
python main.py
```

##  Security Notes

- Database credentials are stored in environment variables rather than hard-coded in Python source files.
- The `.env` file must remain private.
- Use a dedicated database account with only the permissions required by the application.
- Do not publish database passwords or private database exports.

##  Screenshots and Demo

Screenshots and a demonstration video will be added here.

##  Future Enhancements

- User authentication and role-based access
- Enhanced book-copy management
- Dashboard statistics and data visualizations
- Data analysis using Pandas and NumPy
- Machine Learning-based book recommendations
- AI-powered library assistance

##  Author

Allwin W Neshwar V

##  Project Status

Version 1.0 — Core Library Management System.

Further improvements and Data Science/AI integrations are planned for future versions.