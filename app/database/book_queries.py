from app.database.db import fetch_all, fetch_one, execute


def get_all_books():

    query = """
        SELECT
            book_id,
            isbn,
            title,
            publication_year,
            language
        FROM books
        ORDER BY book_id
    """

    return fetch_all(query)

def search_books_by_title(search_text):

    query = """
        SELECT
            book_id,
            isbn,
            title,
            publication_year,
            language
        FROM books
        WHERE LOWER(title) LIKE LOWER(:search_text)
        ORDER BY title
    """

    params = {
        "search_text": f"%{search_text}%"
    }

    return fetch_all(query, params)


def get_books_by_category(category_id):
    query = """
        SELECT
            book_id,
            isbn,
            title,
            publication_year,
            language
        FROM books
        WHERE category_id = :category_id
        ORDER BY title
    """

    params = {
        "category_id": category_id
    }

    return fetch_all(query, params)


def get_book_by_isbn(isbn):
    query = """
        SELECT
            book_id,
            isbn,
            title,
            publication_year,
            language
        FROM books
        WHERE isbn = :isbn
    """

    params = {
        "isbn": isbn
    }

    return fetch_one(query, params)

def get_book_details(book_id):

    query = """
        SELECT
            b.book_id,
            b.isbn,
            b.title,
            b.category_id,
            c.category_name,
            b.publisher_id,
            p.publisher_name,
            b.publication_year,
            DBMS_LOB.SUBSTR(b.description, 4000, 1) AS description,
            b.keywords,
            b.language
        FROM books b
        JOIN categories c
            ON b.category_id = c.category_id
        JOIN publishers p
            ON b.publisher_id = p.publisher_id
        WHERE b.book_id = :book_id
    """

    params = {
        "book_id": book_id
    }

    return fetch_one(query, params)

def add_book(
    isbn,
    title,
    category_id,
    publisher_id,
    publication_year,
    description,
    keywords,
    language
):
    query = """
        INSERT INTO books (
            isbn,
            title,
            category_id,
            publisher_id,
            publication_year,
            description,
            keywords,
            language
        )
        VALUES (
            :isbn,
            :title,
            :category_id,
            :publisher_id,
            :publication_year,
            :description,
            :keywords,
            :language
        )
    """

    params = {
        "isbn": isbn,
        "title": title,
        "category_id": category_id,
        "publisher_id": publisher_id,
        "publication_year": publication_year,
        "description": description,
        "keywords": keywords,
        "language": language
    }

    execute(query, params)

def update_book(
    book_id,
    isbn,
    title,
    category_id,
    publisher_id,
    publication_year,
    description,
    keywords,
    language
):
    query = """
        UPDATE books
        SET
            isbn = :isbn,
            title = :title,
            category_id = :category_id,
            publisher_id = :publisher_id,
            publication_year = :publication_year,
            description = :description,
            keywords = :keywords,
            language = :language,
            updated_at = SYSTIMESTAMP
        WHERE book_id = :book_id
    """

    params = {
        "book_id": book_id,
        "isbn": isbn,
        "title": title,
        "category_id": category_id,
        "publisher_id": publisher_id,
        "publication_year": publication_year,
        "description": description,
        "keywords": keywords,
        "language": language
    }

    execute(query, params)