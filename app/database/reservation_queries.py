from app.database.db import fetch_all, execute_transaction_with_cursor


def get_all_reservations():

    query = """
        SELECT
            r.reservation_id,
            r.book_id,
            b.title,
            r.member_id,
            u.full_name,
            r.reservation_date,
            r.expiry_date,
            r.status
        FROM book_reservations r
        JOIN books b
            ON r.book_id = b.book_id
        JOIN members m
            ON r.member_id = m.member_id
        JOIN users u
            ON m.user_id = u.user_id
        ORDER BY r.reservation_id
    """

    return fetch_all(query)

def create_reservation(book_id, member_id, expiry_date):

    def transaction(cursor):

        # 1. Check whether the book exists
        book_query = """
            SELECT book_id
            FROM books
            WHERE book_id = :book_id
        """

        cursor.execute(
            book_query,
            {"book_id": book_id}
        )

        if cursor.fetchone() is None:
            raise ValueError("Book not found.")

        # 2. Check whether member exists and is active
        member_query = """
            SELECT member_id
            FROM members
            WHERE member_id = :member_id
              AND membership_status = 'ACTIVE'
        """

        cursor.execute(
            member_query,
            {"member_id": member_id}
        )

        if cursor.fetchone() is None:
            raise ValueError("Active member not found.")

        # 3. Check existing active reservation
        existing_query = """
            SELECT reservation_id
            FROM book_reservations
            WHERE book_id = :book_id
              AND member_id = :member_id
              AND status = 'ACTIVE'
        """

        cursor.execute(
            existing_query,
            {
                "book_id": book_id,
                "member_id": member_id
            }
        )

        if cursor.fetchone() is not None:
            raise ValueError(
                "Member already has an active reservation for this book."
            )

        # 4. Create reservation
        insert_query = """
            INSERT INTO book_reservations (
                book_id,
                member_id,
                reservation_date,
                expiry_date,
                status
            )
            VALUES (
                :book_id,
                :member_id,
                SYSTIMESTAMP,
                :expiry_date,
                'ACTIVE'
            )
        """

        cursor.execute(
            insert_query,
            {
                "book_id": book_id,
                "member_id": member_id,
                "expiry_date": expiry_date
            }
        )

        #5 Check whether any copy is available
        availability_query = """
            SELECT COUNT(*)
            FROM book_copies
            WHERE book_id = :book_id
            AND status = 'AVAILABLE'
        """

        cursor.execute(
            availability_query,
            {"book_id": book_id}
        )

        available_copies = cursor.fetchone()[0]

        if available_copies > 0:
            raise ValueError(
                "Reservation is not allowed because the book has available copies."
            )

            return execute_transaction_with_cursor(transaction)

def cancel_reservation(reservation_id):

    def transaction(cursor):

        # 1. Check reservation
        select_query = """
            SELECT status
            FROM book_reservations
            WHERE reservation_id = :reservation_id
        """

        cursor.execute(
            select_query,
            {"reservation_id": reservation_id}
        )

        reservation = cursor.fetchone()

        if reservation is None:
            raise ValueError("Reservation not found.")

        status = reservation[0]

        # 2. Only ACTIVE reservations can be cancelled
        if status != "ACTIVE":
            raise ValueError(
                f"Reservation cannot be cancelled because its status is {status}."
            )

        # 3. Update reservation
        update_query = """
            UPDATE book_reservations
            SET status = 'CANCELLED'
            WHERE reservation_id = :reservation_id
              AND status = 'ACTIVE'
        """

        cursor.execute(
            update_query,
            {"reservation_id": reservation_id}
        )

        if cursor.rowcount != 1:
            raise ValueError("Unable to cancel reservation.")

    return execute_transaction_with_cursor(transaction)

def fulfill_reservation(reservation_id):

    def transaction(cursor):

        # 1. Check reservation
        select_query = """
            SELECT
                status
            FROM book_reservations
            WHERE reservation_id = :reservation_id
        """

        cursor.execute(
            select_query,
            {"reservation_id": reservation_id}
        )

        reservation = cursor.fetchone()

        if reservation is None:
            raise ValueError("Reservation not found.")

        status = reservation[0]

        # 2. Only ACTIVE reservations can be fulfilled
        if status != "ACTIVE":
            raise ValueError(
                f"Reservation cannot be fulfilled because its status is {status}."
            )

        # 3. Mark reservation as fulfilled
        update_query = """
            UPDATE book_reservations
            SET status = 'FULFILLED'
            WHERE reservation_id = :reservation_id
              AND status = 'ACTIVE'
        """

        cursor.execute(
            update_query,
            {"reservation_id": reservation_id}
        )

        if cursor.rowcount != 1:
            raise ValueError("Unable to fulfill reservation.")

    return execute_transaction_with_cursor(transaction)

def expire_reservations():
    def transaction(cursor):

        update_query = """
            UPDATE book_reservations
            SET status = 'EXPIRED'
            WHERE status = 'ACTIVE'
              AND expiry_date IS NOT NULL
              AND TRUNC(expiry_date) < TRUNC(SYSDATE)
        """

        cursor.execute(update_query)

        return cursor.rowcount

    return execute_transaction_with_cursor(transaction)