from app.database.db import fetch_all


def get_all_members():
    query = """
        SELECT
            m.member_id,
            m.membership_number,
            u.full_name,
            u.email,
            m.phone,
            m.join_date,
            m.membership_status
        FROM members m
        JOIN users u
            ON m.user_id = u.user_id
        ORDER BY m.member_id
    """

    return fetch_all(query)


def search_members(search_text):
    query = """
        SELECT
            m.member_id,
            m.membership_number,
            u.full_name,
            u.email,
            m.phone,
            m.join_date,
            m.membership_status
        FROM members m
        JOIN users u
            ON m.user_id = u.user_id
        WHERE LOWER(u.full_name) LIKE LOWER(:search_text)
           OR LOWER(m.membership_number) LIKE LOWER(:search_text)
        ORDER BY m.member_id
    """

    params = {
        "search_text": f"%{search_text}%"
    }

    return fetch_all(query, params)