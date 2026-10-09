from app.database.db import fetch_all, execute_transaction_with_cursor


def get_all_fines():
    query = """
        SELECT
            f.fine_id,
            f.loan_id,
            f.fine_amount,
            f.reason,
            f.fine_status,
            f.created_at
        FROM fines f
        ORDER BY f.fine_id
    """

    return fetch_all(query)


def pay_fine(fine_id, payment_amount, payment_method):

    def transaction(cursor):

        # 1. Get fine details
        select_query = """
            SELECT
                fine_amount,
                fine_status
            FROM fines
            WHERE fine_id = :fine_id
        """

        cursor.execute(
            select_query,
            {"fine_id": fine_id}
        )

        fine = cursor.fetchone()

        if fine is None:
            raise ValueError("Fine not found.")

        fine_amount = fine[0]
        fine_status = fine[1]

        if fine_status == "PAID":
            raise ValueError("This fine is already fully paid.")

        # 2. Get amount already paid
        payment_query = """
            SELECT NVL(SUM(payment_amount), 0)
            FROM fine_payments
            WHERE fine_id = :fine_id
        """

        cursor.execute(
            payment_query,
            {"fine_id": fine_id}
        )

        paid_amount = cursor.fetchone()[0]

        # 3. Calculate remaining amount
        remaining_amount = fine_amount - paid_amount

        if payment_amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")

        if payment_amount > remaining_amount:
            raise ValueError(
                f"Payment exceeds remaining fine amount of ₹{remaining_amount}"
            )

        # 4. Insert payment
        insert_payment = """
            INSERT INTO fine_payments (
                fine_id,
                payment_amount,
                payment_date,
                payment_method
            )
            VALUES (
                :fine_id,
                :payment_amount,
                SYSDATE,
                :payment_method
            )
        """

        cursor.execute(
            insert_payment,
            {
                "fine_id": fine_id,
                "payment_amount": payment_amount,
                "payment_method": payment_method
            }
        )

        # 5. Determine new status
        new_paid_amount = paid_amount + payment_amount

        if new_paid_amount == fine_amount:
            new_status = "PAID"
        else:
            new_status = "PARTIALLY_PAID"

        # 6. Update fine status
        update_fine = """
            UPDATE fines
            SET fine_status = :fine_status
            WHERE fine_id = :fine_id
        """

        cursor.execute(
            update_fine,
            {
                "fine_id": fine_id,
                "fine_status": new_status
            }
        )

    return execute_transaction_with_cursor(transaction)