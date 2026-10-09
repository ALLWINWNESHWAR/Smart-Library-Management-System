from app.database.book_queries import (
    get_all_books,
    search_books_by_title,
    get_book_details,
    add_book,
    update_book
)


def get_books():
    return get_all_books()


def search_books(search_text):
    search_text = search_text.strip()

    if not search_text:
        return []

    return search_books_by_title(search_text)


def get_book(book_id):
    if not isinstance(book_id, int) or book_id <= 0:
        return None

    book = get_book_details(book_id)

    if book is None:
        return None

    return book


def add_library_book(
    isbn,
    title,
    category_id,
    publisher_id,
    publication_year,
    description,
    keywords,
    language
):
    # Remove unnecessary spaces
    isbn = isbn.strip()
    title = title.strip()
    description = description.strip()
    keywords = keywords.strip()
    language = language.strip()

    # Required field validation
    if not isbn:
        raise ValueError("ISBN is required.")

    if not title:
        raise ValueError("Book title is required.")

    if not isinstance(category_id, int) or category_id <= 0:
        raise ValueError("Invalid category ID.")

    if not isinstance(publisher_id, int) or publisher_id <= 0:
        raise ValueError("Invalid publisher ID.")

    if not publication_year:
        raise ValueError("Publication year is required.")

    if not language:
        raise ValueError("Language is required.")

    # Validate publication year
    if publication_year < 1000 or publication_year > 9999:
        raise ValueError("Invalid publication year.")

    add_book(
        isbn=isbn,
        title=title,
        category_id=category_id,
        publisher_id=publisher_id,
        publication_year=publication_year,
        description=description,
        keywords=keywords,
        language=language
    )

def update_library_book(
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
    if not isinstance(book_id, int) or book_id <= 0:
        raise ValueError("Invalid book ID.")

    isbn = isbn.strip()
    title = title.strip()
    description = description.strip()
    keywords = keywords.strip()
    language = language.strip()

    if not isbn:
        raise ValueError("ISBN is required.")

    if not title:
        raise ValueError("Book title is required.")

    if not isinstance(category_id, int) or category_id <= 0:
        raise ValueError("Invalid category ID.")

    if not isinstance(publisher_id, int) or publisher_id <= 0:
        raise ValueError("Invalid publisher ID.")

    if not publication_year:
        raise ValueError("Publication year is required.")

    if publication_year < 1000 or publication_year > 9999:
        raise ValueError("Invalid publication year.")

    if not language:
        raise ValueError("Language is required.")

    update_book(
        book_id=book_id,
        isbn=isbn,
        title=title,
        category_id=category_id,
        publisher_id=publisher_id,
        publication_year=publication_year,
        description=description,
        keywords=keywords,
        language=language
    )