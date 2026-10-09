from app.database.db import fetch_all, execute_transaction_with_cursor
from datetime import date

def get_active_loans():
    query = """
        SELECT
            l.loan_id,
            l.copy_id,
            b.title,
            l.member_id,
            u.full_name,
            l.issue_date,
            l.due_date,
            l.status
        FROM loans l
        JOIN book_copies bc
            ON l.copy_id = bc.copy_id
        JOIN books b
            ON bc.book_id = b.book_id
        JOIN members m
            ON l.member_id = m.member_id
        JOIN users u
            ON m.user_id = u.user_id
        WHERE l.status IN ('ACTIVE', 'OVERDUE')
        ORDER BY l.due_date
    """

    return fetch_all(query)



def issue_book(copy_id, member_id, due_date):

    def transaction(cursor):

        # Step 1: Update copy only if available
        update_query = """
            UPDATE book_copies
            SET status = 'ISSUED'
            WHERE copy_id = :copy_id
              AND status = 'AVAILABLE'
        """

        cursor.execute(
            update_query,
            {"copy_id": copy_id}
        )

        # Make sure the copy was actually available
        if cursor.rowcount != 1:
            raise ValueError(
                "Book copy is not available."
            )

        # Step 2: Create loan
        insert_query = """
            INSERT INTO loans (
                copy_id,
                member_id,
                issue_date,
                due_date,
                status
            )
            VALUES (
                :copy_id,
                :member_id,
                SYSDATE,
                :due_date,
                'ACTIVE'
            )
        """

        cursor.execute(
            insert_query,
            {
                "copy_id": copy_id,
                "member_id": member_id,
                "due_date": due_date
            }
        )

    return execute_transaction_with_cursor(transaction)



# returning the book to library and calculating the fine
def return_book(loan_id):
    def transaction(cursor):

        # 1. Get loan details
        select_query = """
            SELECT
                copy_id,
                due_date
            FROM loans
            WHERE loan_id = :loan_id
              AND status IN ('ACTIVE', 'OVERDUE')
        """

        cursor.execute(
            select_query,
            {"loan_id": loan_id}
        )

        loan = cursor.fetchone()

        if loan is None:
            raise ValueError("Active loan not found.")

        copy_id = loan[0]
        due_date = loan[1]

        # 2. Calculate overdue days
        cursor.execute(
            "SELECT TRUNC(SYSDATE) - TRUNC(:due_date) FROM dual",
            {"due_date": due_date}
        )

        overdue_days = cursor.fetchone()[0]

        # 3. Create fine if overdue
        if overdue_days > 0:

            fine_amount = overdue_days * 5

            fine_query = """
                INSERT INTO fines (
                    loan_id,
                    fine_amount,
                    reason,
                    fine_status
                )
                VALUES (
                    :loan_id,
                    :fine_amount,
                    :reason,
                    'UNPAID'
                )
            """

            cursor.execute(
                fine_query,
                {
                    "loan_id": loan_id,
                    "fine_amount": fine_amount,
                    "reason": f"Overdue by {overdue_days} day(s)"
                }
            )

        # 4. Update loan
        update_loan_query = """
            UPDATE loans
            SET
                return_date = SYSDATE,
                status = 'RETURNED'
            WHERE loan_id = :loan_id
              AND status IN ('ACTIVE', 'OVERDUE')
        """

        cursor.execute(
            update_loan_query,
            {"loan_id": loan_id}
        )

        if cursor.rowcount != 1:
            raise ValueError("Unable to return the loan.")

        # 5. Make book copy available
        update_copy_query = """
            UPDATE book_copies
            SET status = 'AVAILABLE'
            WHERE copy_id = :copy_id
        """

        cursor.execute(
            update_copy_query,
            {"copy_id": copy_id}
        )

        if cursor.rowcount != 1:
            raise ValueError("Unable to update book copy.")

    return execute_transaction_with_cursor(transaction)



def renew_loan(loan_id, additional_days=7):

    def transaction(cursor):

        # 1. Get current loan details
        select_query = """
            SELECT
                due_date,
                renewal_count
            FROM loans
            WHERE loan_id = :loan_id
              AND status = 'ACTIVE'
        """

        cursor.execute(
            select_query,
            {"loan_id": loan_id}
        )

        loan = cursor.fetchone()

        if loan is None:
            raise ValueError(
                "Active loan not found."
            )

        current_due_date = loan[0]
        renewal_count = loan[1]

        # 2. Check maximum renewal limit
        MAX_RENEWALS = 2

        if renewal_count >= MAX_RENEWALS:
            raise ValueError(
                "Maximum renewal limit reached."
            )

        # 3. Update due date and renewal count
        update_query = """
            UPDATE loans
            SET
                due_date = due_date + :additional_days,
                renewal_count = renewal_count + 1
            WHERE loan_id = :loan_id
              AND status = 'ACTIVE'
        """

        cursor.execute(
            update_query,
            {
                "loan_id": loan_id,
                "additional_days": additional_days
            }
        )

        if cursor.rowcount != 1:
            raise ValueError(
                "Unable to renew the loan."
            )

    return execute_transaction_with_cursor(transaction)