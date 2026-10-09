-- ============================================================
-- SMART LIBRARY MANAGEMENT SYSTEM
-- File: 03_indexes.sql
-- Purpose: Additional performance indexes
-- ============================================================


-- ============================================================
-- BOOKS
-- ============================================================

CREATE INDEX idx_books_title
ON books(title);

CREATE INDEX idx_books_category
ON books(category_id);

CREATE INDEX idx_books_publisher
ON books(publisher_id);


-- ============================================================
-- BOOK_COPIES
-- ============================================================

CREATE INDEX idx_book_copies_book
ON book_copies(book_id);

CREATE INDEX idx_book_copies_status
ON book_copies(status);


-- ============================================================
-- LOANS
-- ============================================================

CREATE INDEX idx_loans_member
ON loans(member_id);

CREATE INDEX idx_loans_copy
ON loans(copy_id);

CREATE INDEX idx_loans_status
ON loans(status);

CREATE INDEX idx_loans_due_date
ON loans(due_date);


-- ============================================================
-- FINES
-- ============================================================

CREATE INDEX idx_fines_loan
ON fines(loan_id);

CREATE INDEX idx_fines_status
ON fines(fine_status);


-- ============================================================
-- FINE PAYMENTS
-- ============================================================

CREATE INDEX idx_fine_payments_fine
ON fine_payments(fine_id);

CREATE INDEX idx_fine_payments_date
ON fine_payments(payment_date);


-- ============================================================
-- BOOK RESERVATIONS
-- ============================================================

CREATE INDEX idx_reservations_book
ON book_reservations(book_id);

CREATE INDEX idx_reservations_member
ON book_reservations(member_id);

CREATE INDEX idx_reservations_status
ON book_reservations(status);


-- ============================================================
-- END OF 03_indexes.sql
-- ============================================================


-- ============================================================
-- SMART LIBRARY MANAGEMENT SYSTEM
-- File: 03_indexes.sql
-- Purpose: Additional performance indexes
-- ============================================================


-- ============================================================
-- BOOKS
-- ============================================================

CREATE INDEX idx_books_title
ON books(title);

CREATE INDEX idx_books_category
ON books(category_id);

CREATE INDEX idx_books_publisher
ON books(publisher_id);


-- ============================================================
-- BOOK_COPIES
-- ============================================================

CREATE INDEX idx_book_copies_book
ON book_copies(book_id);

CREATE INDEX idx_book_copies_status
ON book_copies(status);


-- ============================================================
-- LOANS
-- ============================================================

CREATE INDEX idx_loans_member
ON loans(member_id);

CREATE INDEX idx_loans_copy
ON loans(copy_id);

CREATE INDEX idx_loans_status
ON loans(status);

CREATE INDEX idx_loans_due_date
ON loans(due_date);


-- ============================================================
-- FINES
-- ============================================================

CREATE INDEX idx_fines_loan
ON fines(loan_id);

CREATE INDEX idx_fines_status
ON fines(fine_status);


-- ============================================================
-- FINE PAYMENTS
-- ============================================================

CREATE INDEX idx_fine_payments_fine
ON fine_payments(fine_id);

CREATE INDEX idx_fine_payments_date
ON fine_payments(payment_date);


-- ============================================================
-- BOOK RESERVATIONS
-- ============================================================

CREATE INDEX idx_reservations_book
ON book_reservations(book_id);

CREATE INDEX idx_reservations_member
ON book_reservations(member_id);

CREATE INDEX idx_reservations_status
ON book_reservations(status);


-- ============================================================
-- END OF 03_indexes.sql
-- ============================================================



SELECT
    index_name,
    table_name,
    uniqueness
FROM user_indexes
WHERE table_name IN (
    'BOOKS',
    'BOOK_AUTHORS',
    'BOOK_COPIES',
    'LOANS',
    'FINES',
    'FINE_PAYMENTS',
    'BOOK_RESERVATIONS'
)
ORDER BY table_name, index_name;