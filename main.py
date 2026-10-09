#checking oracledb is installed or not
'''
print("oracledb installed successfully!")

#TESTING THE CONNECTION
from app.database.connection import get_connection

try:
    connection = get_connection()
    print("Oracle Database Connected Successfully!")
    connection.close()

except Exception as e:
    print("Database connection failed.")
    print("Error:", e)


#testins select * from book
from app.database.book_queries import get_all_books


books = get_all_books()

print("Books in Library:")
print("-----------------")

for book in books:
    print(book)


'''


import tkinter as tk
from app.gui.main_window import MainWindow

root = tk.Tk()
app = MainWindow(root)
root.mainloop()
