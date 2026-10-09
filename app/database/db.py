'''
fetch_all()	    Get multiple rows
fetch_one()	    Get one row
execute()	    INSERT / UPDATE / DELETE

'''

from app.database.connection import get_connection
from app.exceptions import DatabaseError


def fetch_all(query, params=None):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params or {})
        return cursor.fetchall()

    except Exception as e:
        raise DatabaseError(f"Database operation failed: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def fetch_one(query, params=None):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params or {})
        return cursor.fetchone()

    except Exception as e:
        raise DatabaseError(f"Database operation failed: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def execute(query, params=None):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params or {})
        connection.commit()

    except Exception as e:
        if connection:
            connection.rollback()

        raise DatabaseError(f"Database operation failed: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def execute_transaction(queries):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        for query, params in queries:
            cursor.execute(query, params or {})

        connection.commit()

    except Exception as e:
        if connection:
            connection.rollback()

        raise DatabaseError(
            f"Transaction failed: {e}"
        )

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def execute_transaction_with_cursor(callback):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        result = callback(cursor)

        connection.commit()

        return result

    except Exception as e:
        if connection:
            connection.rollback()

        raise DatabaseError(
            f"Transaction failed: {e}"
        )

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()