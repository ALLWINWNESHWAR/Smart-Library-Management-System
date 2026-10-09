-- ============================================================
-- SMART LIBRARY MANAGEMENT SYSTEM
-- File: 04_sample_data.sql
-- Part 1: Master Data
-- ============================================================


-- ============================================================
-- CATEGORIES
-- ============================================================

INSERT INTO categories (category_name, description)
VALUES ('Programming',
        'Books related to programming languages and software development');

INSERT INTO categories (category_name, description)
VALUES ('Database',
        'Books related to database systems, SQL and database administration');

INSERT INTO categories (category_name, description)
VALUES ('Data Science',
        'Books covering data analysis, statistics and data science');

INSERT INTO categories (category_name, description)
VALUES ('Machine Learning',
        'Books covering machine learning algorithms and applications');

INSERT INTO categories (category_name, description)
VALUES ('Artificial Intelligence',
        'Books covering artificial intelligence concepts and applications');

INSERT INTO categories (category_name, description)
VALUES ('Web Development',
        'Books related to frontend and backend web development');

INSERT INTO categories (category_name, description)
VALUES ('Computer Networks',
        'Books related to networking and communication technologies');

INSERT INTO categories (category_name, description)
VALUES ('Cyber Security',
        'Books related to information security and cybersecurity');

INSERT INTO categories (category_name, description)
VALUES ('Science',
        'General science and scientific concepts');

INSERT INTO categories (category_name, description)
VALUES ('Fiction',
        'Fictional novels and literary works');
        
        
        
-- ============================================================
-- PUBLISHERS
-- ============================================================

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('O''Reilly Media',
     'contact@oreilly.com',
     '+1-800-998-9938',
     'Sebastopol, California, USA');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('Packt Publishing',
     'contact@packtpub.com',
     '+44-20-7193-5000',
     'Birmingham, United Kingdom');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('Pearson',
     'support@pearson.com',
     '+1-800-848-9500',
     'New York, USA');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('Manning Publications',
     'info@manning.com',
     '+1-800-568-2395',
     'Shelter Island, New York, USA');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('Springer',
     'contact@springer.com',
     '+49-6221-487-0',
     'Berlin, Germany');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('Wiley',
     'info@wiley.com',
     '+1-877-762-2974',
     'Hoboken, New Jersey, USA');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('McGraw Hill',
     'info@mcgrawhill.com',
     '+1-800-338-3987',
     'New York, USA');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('Apress',
     'info@apress.com',
     '+1-800-222-0227',
     'New York, USA');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('No Starch Press',
     'info@nostarch.com',
     '+1-415-863-9900',
     'San Francisco, USA');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('Cambridge University Press',
     'contact@cambridge.org',
     '+44-1223-358331',
     'Cambridge, United Kingdom');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('Oxford University Press',
     'enquiries@oup.com',
     '+44-1865-556767',
     'Oxford, United Kingdom');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('MIT Press',
     'info@mit.edu',
     '+1-617-253-2889',
     'Cambridge, Massachusetts, USA');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('Prentice Hall',
     'contact@pearson.com',
     '+1-800-848-9500',
     'New York, USA');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('CRC Press',
     'info@crcpress.com',
     '+1-800-634-7064',
     'Boca Raton, Florida, USA');

INSERT INTO publishers
    (publisher_name, email, phone, address)
VALUES
    ('Apress Media',
     'contact@apress.com',
     '+1-800-222-0227',
     'New York, USA');
     
     
     
-- ============================================================
-- AUTHORS
-- ============================================================

INSERT INTO authors (author_name, biography)
VALUES
('Mark Lutz',
 'Author and Python programming educator.');

INSERT INTO authors (author_name, biography)
VALUES
('Eric Matthes',
 'Author known for educational Python programming material.');

INSERT INTO authors (author_name, biography)
VALUES
('Luciano Ramalho',
 'Author and Python programming expert.');

INSERT INTO authors (author_name, biography)
VALUES
('Aurélien Géron',
 'Author specializing in machine learning and practical AI.');

INSERT INTO authors (author_name, biography)
VALUES
('Jake VanderPlas',
 'Author and educator focused on Python data science.');

INSERT INTO authors (author_name, biography)
VALUES
('Wes McKinney',
 'Creator of the pandas library and data science author.');

INSERT INTO authors (author_name, biography)
VALUES
('Joel Grus',
 'Author and data science educator.');

INSERT INTO authors (author_name, biography)
VALUES
('Sebastian Raschka',
 'Machine learning researcher and educator.');

INSERT INTO authors (author_name, biography)
VALUES
('Francois Chollet',
 'Creator of Keras and deep learning researcher.');

INSERT INTO authors (author_name, biography)
VALUES
('Ian Goodfellow',
 'Researcher known for work in deep learning.');

INSERT INTO authors (author_name, biography)
VALUES
('Yoshua Bengio',
 'Researcher known for foundational work in deep learning.');

INSERT INTO authors (author_name, biography)
VALUES
('Andrew Ng',
 'Educator and researcher in machine learning and AI.');

INSERT INTO authors (author_name, biography)
VALUES
('Stuart Russell',
 'Researcher and author in artificial intelligence.');

INSERT INTO authors (author_name, biography)
VALUES
('Peter Norvig',
 'Computer scientist and author specializing in AI.');

INSERT INTO authors (author_name, biography)
VALUES
('Martin Kleppmann',
 'Author and researcher focused on data-intensive applications.');

INSERT INTO authors (author_name, biography)
VALUES
('Thomas H. Cormen',
 'Computer scientist and algorithms author.');

INSERT INTO authors (author_name, biography)
VALUES
('Robert C. Martin',
 'Software engineering author and educator.');

INSERT INTO authors (author_name, biography)
VALUES
('Joshua Bloch',
 'Software engineer and author known for Java programming.');

INSERT INTO authors (author_name, biography)
VALUES
('Donald E. Knuth',
 'Computer scientist known for foundational work in algorithms.');

INSERT INTO authors (author_name, biography)
VALUES
('James Clear',
 'Author focused on habits and personal development.');
 
 
 
COMMIT;

SELECT COUNT(*) AS category_count
FROM categories;

SELECT COUNT(*) AS publisher_count
FROM publishers;

SELECT COUNT(*) AS author_count
FROM authors;



-- =========================================================
-- USERS
-- =========================================================

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('admin', 'TEMP_HASH_ADMIN', 'ADMIN',
 'System Administrator', 'admin@smartlibrary.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('librarian1', 'TEMP_HASH_LIB1', 'LIBRARIAN',
 'Arun Kumar', 'arun@smartlibrary.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('librarian2', 'TEMP_HASH_LIB2', 'LIBRARIAN',
 'Priya Devi', 'priya@smartlibrary.com', 'ACTIVE');
 
 
--27 members

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member01', 'TEMP_HASH_01', 'MEMBER', 'Rahul Kumar', 'rahul01@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member02', 'TEMP_HASH_02', 'MEMBER', 'Priya Sharma', 'priya02@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member03', 'TEMP_HASH_03', 'MEMBER', 'Arun Raj', 'arun03@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member04', 'TEMP_HASH_04', 'MEMBER', 'Divya S', 'divya04@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member05', 'TEMP_HASH_05', 'MEMBER', 'Karthik M', 'karthik05@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member06', 'TEMP_HASH_06', 'MEMBER', 'Sneha R', 'sneha06@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member07', 'TEMP_HASH_07', 'MEMBER', 'Vijay Kumar', 'vijay07@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member08', 'TEMP_HASH_08', 'MEMBER', 'Anitha P', 'anitha08@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member09', 'TEMP_HASH_09', 'MEMBER', 'Suresh B', 'suresh09@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member10', 'TEMP_HASH_10', 'MEMBER', 'Meena K', 'meena10@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member11', 'TEMP_HASH_11', 'MEMBER', 'Naveen T', 'naveen11@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member12', 'TEMP_HASH_12', 'MEMBER', 'Keerthana V', 'keerthana12@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member13', 'TEMP_HASH_13', 'MEMBER', 'Gokul R', 'gokul13@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member14', 'TEMP_HASH_14', 'MEMBER', 'Harini S', 'harini14@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member15', 'TEMP_HASH_15', 'MEMBER', 'Manoj P', 'manoj15@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member16', 'TEMP_HASH_16', 'MEMBER', 'Swetha M', 'swetha16@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member17', 'TEMP_HASH_17', 'MEMBER', 'Ajay K', 'ajay17@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member18', 'TEMP_HASH_18', 'MEMBER', 'Lavanya R', 'lavanya18@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member19', 'TEMP_HASH_19', 'MEMBER', 'Dinesh S', 'dinesh19@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member20', 'TEMP_HASH_20', 'MEMBER', 'Nithya P', 'nithya20@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member21', 'TEMP_HASH_21', 'MEMBER', 'Vignesh R', 'vignesh21@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member22', 'TEMP_HASH_22', 'MEMBER', 'Aishwarya K', 'aishwarya22@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member23', 'TEMP_HASH_23', 'MEMBER', 'Prakash M', 'prakash23@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member24', 'TEMP_HASH_24', 'MEMBER', 'Deepa S', 'deepa24@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member25', 'TEMP_HASH_25', 'MEMBER', 'Surya K', 'surya25@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member26', 'TEMP_HASH_26', 'MEMBER', 'Ramya V', 'ramya26@example.com', 'ACTIVE');

INSERT INTO users
(username, password_hash, role, full_name, email, status)
VALUES
('member27', 'TEMP_HASH_27', 'MEMBER', 'Bharath S', 'bharath27@example.com', 'ACTIVE');




SELECT user_id, username, full_name
FROM users
WHERE role = 'MEMBER'
ORDER BY user_id;





-- =========================================================
-- BOOKS
-- =========================================================

INSERT INTO books
(isbn, title, category_id, publisher_id, publication_year,
 description, keywords, language)
SELECT '9780262033848',
       'Introduction to Algorithms',
       category_id,
       publisher_id,
       2022,
       'A comprehensive introduction to algorithms and data structures.',
       'algorithms,data structures,programming,computer science',
       'English'
FROM categories c, publishers p
WHERE c.category_name = 'Programming'
AND p.publisher_name = 'MIT Press';

INSERT INTO books
(isbn, title, category_id, publisher_id, publication_year,
 description, keywords, language)
SELECT '9781492051367',
       'Fluent Python',
       c.category_id,
       p.publisher_id,
       2022,
       'A practical guide to advanced Python programming.',
       'python,programming,oop,advanced python',
       'English'
FROM categories c, publishers p
WHERE c.category_name = 'Programming'
AND p.publisher_name = 'O''Reilly Media';

INSERT INTO books
(isbn, title, category_id, publisher_id, publication_year,
 description, keywords, language)
SELECT '9781593279288',
       'Python Crash Course',
       c.category_id,
       p.publisher_id,
       2023,
       'A hands-on introduction to Python programming.',
       'python,programming,beginner',
       'English'
FROM categories c, publishers p
WHERE c.category_name = 'Programming'
AND p.publisher_name = 'No Starch Press';

INSERT INTO books
(isbn, title, category_id, publisher_id, publication_year,
 description, keywords, language)
SELECT '9781491957660',
       'Python for Data Analysis',
       c.category_id,
       p.publisher_id,
       2022,
       'Data analysis using Python, Pandas and NumPy.',
       'python,pandas,numpy,data analysis',
       'English'
FROM categories c, publishers p
WHERE c.category_name = 'Data Science'
AND p.publisher_name = 'O''Reilly Media';

INSERT INTO books
(isbn, title, category_id, publisher_id, publication_year,
 description, keywords, language)
SELECT '9781098104030',
       'Hands-On Machine Learning',
       c.category_id,
       p.publisher_id,
       2022,
       'Practical machine learning using Python and Scikit-learn.',
       'machine learning,python,scikit-learn,ai',
       'English'
FROM categories c, publishers p
WHERE c.category_name = 'Machine Learning'
AND p.publisher_name = 'O''Reilly Media';



SELECT book_id, isbn, title
FROM books
ORDER BY book_id;
SELECT author_id, author_name
FROM authors
ORDER BY author_id;


--book author
INSERT INTO book_authors (book_id, author_id)
VALUES (1, 17);

INSERT INTO book_authors (book_id, author_id)
VALUES (2, 3);

INSERT INTO book_authors (book_id, author_id)
VALUES (3, 2);

INSERT INTO book_authors (book_id, author_id)
VALUES (4, 6);

INSERT INTO book_authors (book_id, author_id)
VALUES (5, 4);

COMMIT;

SELECT
    ba.book_id,
    b.title,
    ba.author_id,
    a.author_name
FROM book_authors ba
JOIN books b
    ON ba.book_id = b.book_id
JOIN authors a
    ON ba.author_id = a.author_id
ORDER BY ba.book_id;



-- =========================================================
-- BOOK COPIES
-- =========================================================

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(1, 'ACC-0001', 'BC-0001', 'AVAILABLE', 'A-01');

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(1, 'ACC-0002', 'BC-0002', 'AVAILABLE', 'A-01');

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(1, 'ACC-0003', 'BC-0003', 'AVAILABLE', 'A-01');


INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(2, 'ACC-0004', 'BC-0004', 'AVAILABLE', 'A-02');

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(2, 'ACC-0005', 'BC-0005', 'AVAILABLE', 'A-02');

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(2, 'ACC-0006', 'BC-0006', 'AVAILABLE', 'A-02');


INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(3, 'ACC-0007', 'BC-0007', 'AVAILABLE', 'A-03');

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(3, 'ACC-0008', 'BC-0008', 'AVAILABLE', 'A-03');

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(3, 'ACC-0009', 'BC-0009', 'AVAILABLE', 'A-03');


INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(4, 'ACC-0010', 'BC-0010', 'AVAILABLE', 'B-01');

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(4, 'ACC-0011', 'BC-0011', 'AVAILABLE', 'B-01');

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(4, 'ACC-0012', 'BC-0012', 'AVAILABLE', 'B-01');


INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(5, 'ACC-0013', 'BC-0013', 'AVAILABLE', 'B-02');

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(5, 'ACC-0014', 'BC-0014', 'AVAILABLE', 'B-02');

INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(5, 'ACC-0015', 'BC-0015', 'AVAILABLE', 'B-02');

COMMIT;



SELECT
    copy_id,
    book_id,
    accession_number,
    barcode,
    status,
    shelf_location
FROM book_copies
ORDER BY copy_id;

SELECT COUNT(*) AS copy_count
FROM book_copies;



SELECT
    loan_id,
    copy_id,
    member_id,
    issue_date,
    due_date,
    return_date,
    renewal_count,
    status
FROM loans
ORDER BY loan_id;

SELECT
    m.member_id,
    m.user_id,
    m.membership_number,
    u.username,
    u.full_name
FROM members m
JOIN users u
    ON m.user_id = u.user_id
ORDER BY m.member_id;
SELECT COUNT(*) AS member_count
FROM members;


INSERT INTO members
(
    user_id,
    membership_number,
    phone,
    address
)
SELECT
    user_id,
    'MEM' || LPAD(ROW_NUMBER() OVER (ORDER BY user_id), 3, '0'),
    '98765' || LPAD(ROW_NUMBER() OVER (ORDER BY user_id), 5, '0'),
    'Karur, Tamil Nadu'
FROM users
WHERE role = 'MEMBER'
AND user_id IN (
    SELECT user_id
    FROM (
        SELECT user_id
        FROM users
        WHERE role = 'MEMBER'
        ORDER BY user_id
    )
    WHERE ROWNUM <= 20
);

COMMIT;






-- =========================================================
-- LOANS
-- =========================================================

-- Returned loans

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(1, 1, DATE '2026-08-01', DATE '2026-08-15', DATE '2026-08-12', 0, 'RETURNED');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(2, 2, DATE '2026-08-05', DATE '2026-08-19', DATE '2026-08-18', 1, 'RETURNED');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(3, 3, DATE '2026-08-10', DATE '2026-08-24', DATE '2026-08-23', 0, 'RETURNED');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(4, 4, DATE '2026-08-15', DATE '2026-08-29', DATE '2026-08-30', 0, 'RETURNED');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(5, 5, DATE '2026-08-20', DATE '2026-09-03', DATE '2026-09-02', 1, 'RETURNED');


-- Active loans

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(6, 6, DATE '2026-10-01', DATE '2026-10-15', NULL, 0, 'ACTIVE');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(7, 7, DATE '2026-10-02', DATE '2026-10-16', NULL, 1, 'ACTIVE');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(8, 8, DATE '2026-10-03', DATE '2026-10-17', NULL, 0, 'ACTIVE');


-- Overdue loans

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(9, 9, DATE '2026-09-01', DATE '2026-09-15', NULL, 0, 'OVERDUE');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(10, 10, DATE '2026-09-05', DATE '2026-09-19', NULL, 1, 'OVERDUE');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(11, 11, DATE '2026-09-10', DATE '2026-09-24', NULL, 0, 'OVERDUE');


-- Additional returned loans

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(12, 12, DATE '2026-07-01', DATE '2026-07-15', DATE '2026-07-14', 0, 'RETURNED');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(13, 13, DATE '2026-07-05', DATE '2026-07-19', DATE '2026-07-25', 0, 'RETURNED');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(14, 14, DATE '2026-07-10', DATE '2026-07-24', DATE '2026-07-23', 1, 'RETURNED');

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(15, 15, DATE '2026-07-15', DATE '2026-07-29', DATE '2026-07-28', 0, 'RETURNED');

COMMIT;

SELECT
    status,
    COUNT(*) AS loan_count
FROM loans
GROUP BY status
ORDER BY status;

SELECT
    loan_id,
    copy_id,
    member_id,
    issue_date,
    due_date,
    return_date,
    status
FROM loans
ORDER BY loan_id;


INSERT INTO book_copies
(book_id, accession_number, barcode, status, shelf_location)
VALUES
(2, 'ACC-0016', 'BC-0016', 'AVAILABLE', 'A-02');

COMMIT;

SELECT
    copy_id,
    book_id,
    accession_number,
    barcode,
    status
FROM book_copies
WHERE accession_number = 'ACC-0016';

INSERT INTO loans
(copy_id, member_id, issue_date, due_date, return_date, renewal_count, status)
VALUES
(17, 5, DATE '2026-08-20', DATE '2026-09-03',
 DATE '2026-09-02', 1, 'RETURNED');

COMMIT;

SELECT
    status,
    COUNT(*) AS loan_count
FROM loans
GROUP BY status
ORDER BY status;



-- =========================================================
-- FINES
-- =========================================================

-- Fines for currently overdue loans

INSERT INTO fines
(loan_id, fine_amount, reason, fine_status)
VALUES
(15, 220.00, 'Book overdue by multiple days', 'UNPAID');

INSERT INTO fines
(loan_id, fine_amount, reason, fine_status)
VALUES
(16, 180.00, 'Book overdue by multiple days', 'UNPAID');

INSERT INTO fines
(loan_id, fine_amount, reason, fine_status)
VALUES
(17, 150.00, 'Book overdue by multiple days', 'UNPAID');


-- Fines for books returned late

INSERT INTO fines
(loan_id, fine_amount, reason, fine_status)
VALUES
(10, 20.00, 'Book returned one day late', 'PAID');

INSERT INTO fines
(loan_id, fine_amount, reason, fine_status)
VALUES
(19, 60.00, 'Book returned six days late', 'PARTIALLY_PAID');

INSERT INTO fines
(loan_id, fine_amount, reason, fine_status)
VALUES
(20, 10.00, 'Book returned one day late', 'PAID');

COMMIT;

SELECT COUNT(*) AS fine_count
FROM fines;



-- =========================================================
-- FINE PAYMENTS
-- =========================================================

-- Full payment for fine 1
INSERT INTO fine_payments
(fine_id, payment_amount, payment_date, payment_method)
VALUES
(1, 220.00, DATE '2026-10-01', 'UPI');

-- Full payment for fine 4
INSERT INTO fine_payments
(fine_id, payment_amount, payment_date, payment_method)
VALUES
(4, 20.00, DATE '2026-09-01', 'CASH');

-- Partial payment for fine 5
INSERT INTO fine_payments
(fine_id, payment_amount, payment_date, payment_method)
VALUES
(5, 30.00, DATE '2026-09-05', 'UPI');

-- Another partial payment for the same fine
INSERT INTO fine_payments
(fine_id, payment_amount, payment_date, payment_method)
VALUES
(5, 30.00, DATE '2026-09-10', 'CARD');

-- Full payment for fine 6
INSERT INTO fine_payments
(fine_id, payment_amount, payment_date, payment_method)
VALUES
(6, 10.00, DATE '2026-08-05', 'ONLINE');

COMMIT;

SELECT
    payment_id,
    fine_id,
    payment_amount,
    payment_date,
    payment_method
FROM fine_payments
ORDER BY payment_id;



-- =========================================================
-- BOOK RESERVATIONS
-- =========================================================

INSERT INTO book_reservations
(book_id, member_id, reservation_date, expiry_date, status)
VALUES
(1, 16, TIMESTAMP '2026-10-01 10:00:00',
 DATE '2026-10-10', 'ACTIVE');

INSERT INTO book_reservations
(book_id, member_id, reservation_date, expiry_date, status)
VALUES
(2, 17, TIMESTAMP '2026-10-02 11:30:00',
 DATE '2026-10-12', 'ACTIVE');

INSERT INTO book_reservations
(book_id, member_id, reservation_date, expiry_date, status)
VALUES
(3, 18, TIMESTAMP '2026-09-20 09:15:00',
 DATE '2026-09-27', 'FULFILLED');

INSERT INTO book_reservations
(book_id, member_id, reservation_date, expiry_date, status)
VALUES
(4, 19, TIMESTAMP '2026-09-25 14:00:00',
 DATE '2026-10-02', 'CANCELLED');

INSERT INTO book_reservations
(book_id, member_id, reservation_date, expiry_date, status)
VALUES
(5, 20, TIMESTAMP '2026-09-28 16:45:00',
 DATE '2026-10-05', 'EXPIRED');

COMMIT;

SELECT
    reservation_id,
    book_id,
    member_id,
    reservation_date,
    expiry_date,
    status
FROM book_reservations
ORDER BY reservation_id;







SELECT 'USERS' AS table_name, COUNT(*) AS record_count FROM users
UNION ALL
SELECT 'MEMBERS', COUNT(*) FROM members
UNION ALL
SELECT 'AUTHORS', COUNT(*) FROM authors
UNION ALL
SELECT 'CATEGORIES', COUNT(*) FROM categories
UNION ALL
SELECT 'PUBLISHERS', COUNT(*) FROM publishers
UNION ALL
SELECT 'BOOKS', COUNT(*) FROM books
UNION ALL
SELECT 'BOOK_AUTHORS', COUNT(*) FROM book_authors
UNION ALL
SELECT 'BOOK_COPIES', COUNT(*) FROM book_copies
UNION ALL
SELECT 'LOANS', COUNT(*) FROM loans
UNION ALL
SELECT 'FINES', COUNT(*) FROM fines
UNION ALL
SELECT 'FINE_PAYMENTS', COUNT(*) FROM fine_payments
UNION ALL
SELECT 'BOOK_RESERVATIONS', COUNT(*) FROM book_reservations;