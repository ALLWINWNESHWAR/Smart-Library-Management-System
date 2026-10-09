from app.database.connection import get_connection

try:
    connection = get_connection()
    print("Oracle Database Connected Successfully!")
    connection.close()

except Exception as e:
    print("Database connection failed:", e)