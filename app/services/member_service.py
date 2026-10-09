from app.database.member_queries import (
    get_all_members,
    search_members
)


def get_members():
    return get_all_members()


def search_member_records(search_text):
    search_text = search_text.strip()

    if not search_text:
        return []

    return search_members(search_text)