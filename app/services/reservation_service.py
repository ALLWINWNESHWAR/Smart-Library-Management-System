from app.database.reservation_queries import (
    get_all_reservations,
    create_reservation,
    cancel_reservation,
    fulfill_reservation,
    expire_reservations
)


def get_reservations():
    return get_all_reservations()


def reserve_book(book_id, member_id, expiry_date):

    if not isinstance(book_id, int) or book_id <= 0:
        raise ValueError("Invalid book ID.")

    if not isinstance(member_id, int) or member_id <= 0:
        raise ValueError("Invalid member ID.")

    if not expiry_date:
        raise ValueError("Expiry date is required.")

    create_reservation(
        book_id,
        member_id,
        expiry_date
    )

def cancel_library_reservation(reservation_id):

    if not isinstance(reservation_id, int) or reservation_id <= 0:
        raise ValueError("Invalid reservation ID.")

    cancel_reservation(reservation_id)

def fulfill_library_reservation(reservation_id):

    if not isinstance(reservation_id, int) or reservation_id <= 0:
        raise ValueError("Invalid reservation ID.")

    fulfill_reservation(reservation_id)

def expire_library_reservations():
    return expire_reservations()