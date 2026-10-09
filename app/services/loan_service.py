from app.database.loan_queries import (
    get_active_loans,
    issue_book,
    return_book,
    renew_loan
)
from datetime import date

def get_loans():
    return get_active_loans()


def issue_library_book(copy_id, member_id, due_date):

    if not isinstance(copy_id, int) or copy_id <= 0:
        raise ValueError("Invalid book copy ID.")

    if not isinstance(member_id, int) or member_id <= 0:
        raise ValueError("Invalid member ID.")

    if not due_date:
        raise ValueError("Due date is required.")

    issue_book(
        copy_id,
        member_id,
        due_date
    )


def return_library_book(loan_id):

    if not isinstance(loan_id, int) or loan_id <= 0:
        raise ValueError("Invalid loan ID.")

    return_book(loan_id)





FINE_PER_DAY = 5

def calculate_fine(due_date, return_date):

    if return_date <= due_date:
        return 0

    overdue_days = (return_date - due_date).days

    return overdue_days * FINE_PER_DAY

def renew_library_loan(loan_id):
    if not isinstance(loan_id, int) or loan_id <= 0:
        raise ValueError("Invalid loan ID.")

    renew_loan(loan_id)