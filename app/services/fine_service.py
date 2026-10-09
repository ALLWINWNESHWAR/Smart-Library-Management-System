from app.database.fine_queries import (
    get_all_fines,
    pay_fine
)


def get_fines():
    return get_all_fines()


def make_fine_payment(fine_id, payment_amount, payment_method):

    if not isinstance(fine_id, int) or fine_id <= 0:
        raise ValueError("Invalid fine ID.")

    if payment_amount <= 0:
        raise ValueError("Payment amount must be greater than zero.")

    if payment_method not in ("CASH", "CARD", "UPI", "ONLINE"):
        raise ValueError("Invalid payment method.")

    pay_fine(
        fine_id,
        payment_amount,
        payment_method
    )