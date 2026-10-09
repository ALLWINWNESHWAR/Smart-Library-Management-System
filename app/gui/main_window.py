import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from app.services.book_service import get_books, search_books, add_library_book, update_library_book, get_book
from app.services.member_service import get_members, search_member_records
from app.services.loan_service import get_loans, issue_library_book, renew_library_loan, return_library_book
from app.services.fine_service import get_fines, make_fine_payment
from app.services.reservation_service import get_reservations, cancel_library_reservation, fulfill_library_reservation, expire_library_reservations

class MainWindow:

    def __init__(self, root):
        self.root = root

        self.root.title("Smart Library Management System")
        self.root.geometry("1000x600")

        self.create_widgets()

    def create_widgets(self):
        # Header
        header = ttk.Frame(self.root)
        header.pack(fill="x", padx=20, pady=20)

        title_label = ttk.Label(
            header,
            text="Smart Library Management System",
            font=("Arial", 22, "bold")
        )
        title_label.pack(side="left")

        role_label = ttk.Label(
            header,
            text="Role: ADMIN",
            font=("Arial", 11)
        )
        role_label.pack(side="right")

        # Main area
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Sidebar
        sidebar = ttk.Frame(main_frame, width=200)
        sidebar.pack(side="left", fill="y", padx=(0, 20))

        # Content area
        self.content = ttk.Frame(main_frame)
        self.content.pack(side="left", fill="both", expand=True)

        # Sidebar buttons
        menu_items = [
            "Dashboard",
            "Books",
            "Members",
            "Loans",
            "Issue Book",
            "Returns",
            "Fines",
            "Reservations",
            "Analytics",
            "AI Recommendation"
        ]

        for item in menu_items:
            button = ttk.Button(
                sidebar,
                text=item,
                command=lambda page=item: self.show_page(page)
            )
            button.pack(fill="x", pady=5)

        # Initial content
        content_label = ttk.Label(
            self.content,
            text="Welcome to the Dashboard",
            font=("Arial", 18, "bold")
        )
        content_label.pack(pady=50)

    def show_page(self, page_name):

        for widget in self.content.winfo_children():
            widget.destroy()

        if page_name == "Books":
            self.show_books_page()
        elif page_name == "Members":
            self.show_members_page()
        elif page_name == "Loans":
            self.show_loans_page()
        elif page_name == "Issue Book":
            self.show_issue_book_page()
        elif page_name == "Fines":
            self.show_fines_page()
        elif page_name == "Reservations":
            self.show_reservations_page()
        elif page_name == "Returns":
            self.show_returns_page()
        else:
            page_label = ttk.Label(
                self.content,
                text=f"{page_name} Page",
                font=("Arial", 20, "bold")
            )

            page_label.pack(pady=50)

    def show_books_page(self):

        title = ttk.Label(
            self.content,
            text="Books",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        # Search area
        search_frame = ttk.Frame(self.content)
        search_frame.pack(fill="x", padx=20, pady=10)

        search_entry = ttk.Entry(search_frame, width=40)
        search_entry.pack(side="left", padx=(0, 10))


        def perform_search():

            search_text = search_entry.get()

            books = search_books(search_text)

            # Clear existing rows
            for row in tree.get_children():
                tree.delete(row)

            # Insert search results
            for book in books:
                tree.insert(
                    "",
                    "end",
                    values=(
                        book[0],
                        book[1],
                        book[2],
                        book[3],
                        book[4]
                    )
                )

        search_button = ttk.Button(
            search_frame,
            text="Search",
            command=perform_search
        )
        search_button.pack(side="left")


        add_button = ttk.Button(
            search_frame,
            text="Add Book",
            command=self.show_add_book_window
        )

        add_button.pack(side="left", padx=10)

        edit_button = ttk.Button(
            search_frame,
            text="Edit Book",
            command=lambda: self.show_edit_book_window(tree)
        )

        edit_button.pack(side="left", padx=10)




        # Table
        columns = (
            "book_id",
            "isbn",
            "title",
            "year",
            "language"
        )

        tree = ttk.Treeview(
            self.content,
            columns=columns,
            show="headings"
        )

        #scrollbar
        scrollbar = ttk.Scrollbar(
            self.content,
            orient="vertical",
            command=tree.yview
        )

        tree.configure(
            yscrollcommand=scrollbar.set
        )

        tree.heading("book_id", text="ID")
        tree.heading("isbn", text="ISBN")
        tree.heading("title", text="Title")
        tree.heading("year", text="Year")
        tree.heading("language", text="Language")

        tree.column("book_id", width=50)
        tree.column("isbn", width=150)
        tree.column("title", width=300)
        tree.column("year", width=80)
        tree.column("language", width=100)

        tree.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(20, 0),
            pady=10
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 20),
            pady=10
        )

        tree.bind(
        "<Double-1>",
        lambda event: self.show_book_details(tree)
        )



        # Load all books initially
        books = get_books()

        for book in books:
            tree.insert(
                "",
                "end",
                values=(
                    book[0],
                    book[1],
                    book[2],
                    book[3],
                    book[4]
                )
            )


    def show_edit_book_window(self, tree):

        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select a book to edit."
            )
            return

        values = tree.item(selected[0], "values")
        book_id = int(values[0])

        book = get_book(book_id)

        if book is None:
            messagebox.showerror(
                "Error",
                "Book details not found."
            )
            return

        # Safely convert Oracle CLOB values to Python strings.
        def to_text(value):
            if value is None:
                return ""
            if hasattr(value, "read"):
                return value.read()
            return str(value)

        description_value = book[8] or ""
        keywords_value = book[9] or ""
        language_value = book[10] or "English"

        window = tk.Toplevel(self.root)
        window.title("Edit Book")
        window.geometry("650x650")
        window.resizable(False, False)

        ttk.Label(
            window,
            text="Edit Book",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        form = ttk.Frame(window)
        form.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=5
        )

        ttk.Label(form, text="ISBN:").grid(
            row=0, column=0, padx=10, pady=6, sticky="w"
        )
        isbn_entry = ttk.Entry(form, width=45)
        isbn_entry.grid(row=0, column=1, padx=10, pady=6)
        isbn_entry.insert(0, str(book[1]))

        ttk.Label(form, text="Title:").grid(
            row=1, column=0, padx=10, pady=6, sticky="w"
        )
        title_entry = ttk.Entry(form, width=45)
        title_entry.grid(row=1, column=1, padx=10, pady=6)
        title_entry.insert(0, str(book[2]))

        ttk.Label(form, text="Category ID:").grid(
            row=2, column=0, padx=10, pady=6, sticky="w"
        )
        category_entry = ttk.Entry(form, width=45)
        category_entry.grid(row=2, column=1, padx=10, pady=6)
        category_entry.insert(0, str(book[3]))

        ttk.Label(form, text="Publisher ID:").grid(
            row=3, column=0, padx=10, pady=6, sticky="w"
        )
        publisher_entry = ttk.Entry(form, width=45)
        publisher_entry.grid(row=3, column=1, padx=10, pady=6)
        publisher_entry.insert(0, str(book[5]))

        ttk.Label(form, text="Publication Year:").grid(
            row=4, column=0, padx=10, pady=6, sticky="w"
        )
        year_entry = ttk.Entry(form, width=45)
        year_entry.grid(row=4, column=1, padx=10, pady=6)
        year_entry.insert(0, str(book[7]))

        ttk.Label(form, text="Description:").grid(
            row=5, column=0, padx=10, pady=6, sticky="nw"
        )
        description_text = tk.Text(form, width=34, height=4)
        description_text.grid(row=5, column=1, padx=10, pady=6)
        if description_value:
            description_text.insert("1.0", description_value)

        ttk.Label(form, text="Keywords:").grid(
            row=6, column=0, padx=10, pady=6, sticky="w"
        )
        keywords_entry = ttk.Entry(form, width=45)
        keywords_entry.grid(row=6, column=1, padx=10, pady=6)
        if keywords_value:
            keywords_entry.insert(0, keywords_value)

        ttk.Label(form, text="Language:").grid(
            row=7, column=0, padx=10, pady=6, sticky="w"
        )
        language_entry = ttk.Entry(form, width=45)
        language_entry.grid(row=7, column=1, padx=10, pady=6)
        language_entry.insert(0, language_value)

        def save_changes():

            try:
                isbn = isbn_entry.get().strip()
                title = title_entry.get().strip()
                category_id = int(category_entry.get().strip())
                publisher_id = int(publisher_entry.get().strip())
                publication_year = int(year_entry.get().strip())

                description = description_text.get(
                    "1.0", "end"
                ).strip()

                keywords = keywords_entry.get().strip()
                language = language_entry.get().strip()

                update_library_book(
                    book_id,
                    isbn,
                    title,
                    category_id,
                    publisher_id,
                    publication_year,
                    description,
                    keywords,
                    language
                )

                messagebox.showinfo(
                    "Success",
                    "Book updated successfully."
                )

                window.destroy()
                self.show_books_page()

            except ValueError as e:
                messagebox.showerror(
                    "Validation Error",
                    str(e)
                )

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    str(e)
                )

        # Fixed button area: outside the form.
        button_frame = ttk.Frame(window)
        button_frame.pack(
            side="bottom",
            fill="x",
            pady=15
        )

        ttk.Button(
            button_frame,
            text="Save Changes",
            command=save_changes
        ).pack(
            side="left",
            padx=(120, 10)
        )

        ttk.Button(
            button_frame,
            text="Cancel",
            command=window.destroy
        ).pack(
            side="left",
            padx=10
        )


    def show_add_book_window(self):

        window = tk.Toplevel(self.root)

        window.title("Add Book")
        window.geometry("500x600")

        ttk.Label(
            window,
            text="Add New Book",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        form = ttk.Frame(window)
        form.pack(padx=30, pady=10)

        # ISBN
        ttk.Label(form, text="ISBN:").grid(
            row=0, column=0, padx=10, pady=8, sticky="w"
        )

        isbn_entry = ttk.Entry(form, width=35)
        isbn_entry.grid(row=0, column=1, padx=10, pady=8)

        # Title
        ttk.Label(form, text="Title:").grid(
            row=1, column=0, padx=10, pady=8, sticky="w"
        )

        title_entry = ttk.Entry(form, width=35)
        title_entry.grid(row=1, column=1, padx=10, pady=8)

        # Category ID
        ttk.Label(form, text="Category ID:").grid(
            row=2, column=0, padx=10, pady=8, sticky="w"
        )

        category_entry = ttk.Entry(form, width=35)
        category_entry.grid(row=2, column=1, padx=10, pady=8)

        # Publisher ID
        ttk.Label(form, text="Publisher ID:").grid(
            row=3, column=0, padx=10, pady=8, sticky="w"
        )

        publisher_entry = ttk.Entry(form, width=35)
        publisher_entry.grid(row=3, column=1, padx=10, pady=8)

        # Publication Year
        ttk.Label(form, text="Publication Year:").grid(
            row=4, column=0, padx=10, pady=8, sticky="w"
        )

        year_entry = ttk.Entry(form, width=35)
        year_entry.grid(row=4, column=1, padx=10, pady=8)

        # Description
        ttk.Label(form, text="Description:").grid(
            row=5, column=0, padx=10, pady=8, sticky="nw"
        )

        description_entry = tk.Text(
            form,
            width=26,
            height=4
        )
        description_entry.grid(row=5, column=1, padx=10, pady=8)

        # Keywords
        ttk.Label(form, text="Keywords:").grid(
            row=6, column=0, padx=10, pady=8, sticky="w"
        )

        keywords_entry = ttk.Entry(form, width=35)
        keywords_entry.grid(row=6, column=1, padx=10, pady=8)

        # Language
        ttk.Label(form, text="Language:").grid(
            row=7, column=0, padx=10, pady=8, sticky="w"
        )

        language_entry = ttk.Entry(form, width=35)
        language_entry.insert(0, "English")
        language_entry.grid(row=7, column=1, padx=10, pady=8)

        def save_book():

            try:

                isbn = isbn_entry.get()
                title = title_entry.get()

                category_id = int(
                    category_entry.get()
                )

                publisher_id = int(
                    publisher_entry.get()
                )

                publication_year = int(
                    year_entry.get()
                )

                description = description_entry.get(
                    "1.0",
                    "end"
                ).strip()

                keywords = keywords_entry.get()

                language = language_entry.get()

                add_library_book(
                    isbn=isbn,
                    title=title,
                    category_id=category_id,
                    publisher_id=publisher_id,
                    publication_year=publication_year,
                    description=description,
                    keywords=keywords,
                    language=language
                )

                messagebox.showinfo(
                    "Success",
                    "Book added successfully."
                )

                window.destroy()

                # Refresh Books page
                self.show_books_page()

            except ValueError as e:

                messagebox.showerror(
                    "Invalid Input",
                    str(e)
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        ttk.Button(
            window,
            text="Save Book",
            command=save_book
        ).pack(pady=20)


    def show_book_details(self, tree):
        selected = tree.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select a book."
            )
            return

        values = tree.item(selected[0], "values")
        book_id = int(values[0])

        from app.services.book_service import get_book

        book = get_book(book_id)

        if book is None:
            messagebox.showerror(
                "Error",
                "Book details not found."
            )
            return

        details_window = tk.Toplevel(self.root)
        details_window.title("Book Details")
        details_window.geometry("600x500")

        ttk.Label(
            details_window,
            text="Book Details",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        details_frame = ttk.Frame(details_window)
        details_frame.pack(fill="both", expand=True, padx=20, pady=10)

        details = [
            ("Book ID", book[0]),
            ("ISBN", book[1]),
            ("Title", book[2]),
            ("Category ID", book[3]),
            ("Category", book[4]),
            ("Publisher ID", book[5]),
            ("Publisher", book[6]),
            ("Publication Year", book[7]),
            ("Description", book[8]),
            ("Keywords", book[9]),
            ("Language", book[10])
        ]

        for row, (label, value) in enumerate(details):

            ttk.Label(
                details_frame,
                text=f"{label}:",
                font=("Arial", 10, "bold")
            ).grid(
                row=row,
                column=0,
                sticky="nw",
                padx=10,
                pady=7
            )

            ttk.Label(
                details_frame,
                text=str(value) if value is not None else "",
                wraplength=400
            ).grid(
                row=row,
                column=1,
                sticky="nw",
                padx=10,
                pady=7
            )

        ttk.Button(
            details_window,
            text="Close",
            command=details_window.destroy
        ).pack(pady=15)
        


    def show_members_page(self):

        title = ttk.Label(
            self.content,
            text="Members",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        # Search area
        search_frame = ttk.Frame(self.content)
        search_frame.pack(fill="x", padx=20, pady=10)

        search_entry = ttk.Entry(search_frame, width=40)
        search_entry.pack(side="left", padx=(0, 10))

        # Table
        columns = (
            "member_id",
            "membership_number",
            "name",
            "email",
            "phone",
            "join_date",
            "status"
        )

        tree = ttk.Treeview(
            self.content,
            columns=columns,
            show="headings"
        )

        tree.heading("member_id", text="ID")
        tree.heading("membership_number", text="Membership No.")
        tree.heading("name", text="Name")
        tree.heading("email", text="Email")
        tree.heading("phone", text="Phone")
        tree.heading("join_date", text="Join Date")
        tree.heading("status", text="Status")

        tree.column("member_id", width=50)
        tree.column("membership_number", width=120)
        tree.column("name", width=150)
        tree.column("email", width=200)
        tree.column("phone", width=120)
        tree.column("join_date", width=100)
        tree.column("status", width=100)

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        def load_members(members):

            for row in tree.get_children():
                tree.delete(row)

            for member in members:

                tree.insert(
                    "",
                    "end",
                    values=(
                        member[0],
                        member[1],
                        member[2],
                        member[3],
                        member[4],
                        member[5],
                        member[6]
                    )
                )

        def perform_search():

            search_text = search_entry.get()

            members = search_member_records(search_text)

            load_members(members)

        search_button = ttk.Button(
            search_frame,
            text="Search",
            command=perform_search
        )
        search_button.pack(side="left")

        # Load all members initially
        load_members(get_members())



    def show_loans_page(self):

        title = ttk.Label(
            self.content,
            text="Active / Overdue Loans",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        columns = (
            "loan_id",
            "copy_id",
            "book",
            "member_id",
            "member",
            "issue_date",
            "due_date",
            "status"
        )

        tree = ttk.Treeview(
            self.content,
            columns=columns,
            show="headings"
        )

        tree.heading("loan_id", text="Loan ID")
        tree.heading("copy_id", text="Copy ID")
        tree.heading("book", text="Book")
        tree.heading("member_id", text="Member ID")
        tree.heading("member", text="Member")
        tree.heading("issue_date", text="Issue Date")
        tree.heading("due_date", text="Due Date")
        tree.heading("status", text="Status")

        tree.column("loan_id", width=70)
        tree.column("copy_id", width=70)
        tree.column("book", width=220)
        tree.column("member_id", width=80)
        tree.column("member", width=150)
        tree.column("issue_date", width=100)
        tree.column("due_date", width=100)
        tree.column("status", width=100)

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        loans = get_loans()

        for loan in loans:

            tree.insert(
                "",
                "end",
                values=(
                    loan[0],
                    loan[1],
                    loan[2],
                    loan[3],
                    loan[4],
                    loan[5],
                    loan[6],
                    loan[7]
                )
            )

        # Renew selected loan
        def renew_selected_loan():

            selected = tree.selection()

            if not selected:
                messagebox.showwarning(
                    "No Selection",
                    "Please select a loan."
                )
                return

            values = tree.item(selected[0], "values")

            loan_id = int(values[0])

            try:
                renew_library_loan(loan_id)

                messagebox.showinfo(
                    "Success",
                    "Loan renewed successfully.\nDue date extended by 7 days."
                )

                # Refresh loan page
                self.show_loans_page()

            except ValueError as e:

                messagebox.showerror(
                    "Renewal Error",
                    str(e)
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )


        ttk.Button(
            self.content,
            text="Renew Selected Loan",
            command=renew_selected_loan
        ).pack(
            pady=10
        )

    def show_issue_book_page(self):

        title = ttk.Label(
            self.content,
            text="Issue Book",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=20)

        form = ttk.Frame(self.content)
        form.pack(pady=20)

        # Member ID
        ttk.Label(
            form,
            text="Member ID:"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        member_entry = ttk.Entry(form, width=30)
        member_entry.grid(row=0, column=1, padx=10, pady=10)

        # Copy ID
        ttk.Label(
            form,
            text="Copy ID:"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

        copy_entry = ttk.Entry(form, width=30)
        copy_entry.grid(row=1, column=1, padx=10, pady=10)

        # Due Date
        ttk.Label(
            form,
            text="Due Date (YYYY-MM-DD):"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

        due_date_entry = ttk.Entry(form, width=30)
        due_date_entry.grid(row=2, column=1, padx=10, pady=10)

        # Issue button
        def issue_book_action():

            try:
                member_id = int(member_entry.get().strip())
                copy_id = int(copy_entry.get().strip())

                due_date = datetime.strptime(
                    due_date_entry.get().strip(),
                    "%Y-%m-%d"
                ).date()

                issue_library_book(
                    copy_id=copy_id,
                    member_id=member_id,
                    due_date=due_date
                )

                messagebox.showinfo(
                    "Success",
                    "Book issued successfully!"
                )

                member_entry.delete(0, "end")
                copy_entry.delete(0, "end")
                due_date_entry.delete(0, "end")

            except ValueError as e:

                messagebox.showerror(
                    "Invalid Input",
                    str(e)
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )


        issue_button = ttk.Button(
            form,
            text="Issue Book",
            command=issue_book_action
        )
        issue_button.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20
        )


    def show_returns_page(self):

        title = ttk.Label(
            self.content,
            text="Return Book",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=20)

        form = ttk.Frame(self.content)
        form.pack(pady=20)

        # Loan ID
        ttk.Label(
            form,
            text="Loan ID:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        loan_id_entry = ttk.Entry(
            form,
            width=30
        )
        loan_id_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        def return_book_action():

            try:

                loan_id = int(
                    loan_id_entry.get().strip()
                )

                return_library_book(loan_id)

                messagebox.showinfo(
                    "Success",
                    "Book returned successfully."
                )

                loan_id_entry.delete(0, "end")

            except ValueError as e:

                messagebox.showerror(
                    "Return Error",
                    str(e)
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        ttk.Button(
            form,
            text="Return Book",
            command=return_book_action
        ).grid(
            row=1,
            column=0,
            columnspan=2,
            pady=20
        )


    def show_fines_page(self):

        ttk.Label(
            self.content,
            text="Fines",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        columns = (
            "fine_id",
            "loan_id",
            "amount",
            "reason",
            "status"
        )

        tree = ttk.Treeview(
            self.content,
            columns=columns,
            show="headings"
        )

        tree.heading("fine_id", text="Fine ID")
        tree.heading("loan_id", text="Loan ID")
        tree.heading("amount", text="Amount")
        tree.heading("reason", text="Reason")
        tree.heading("status", text="Status")

        tree.column("fine_id", width=80)
        tree.column("loan_id", width=80)
        tree.column("amount", width=100)
        tree.column("reason", width=250)
        tree.column("status", width=120)

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # Load fines
        fines = get_fines()

        for fine in fines:
            tree.insert(
                "",
                "end",
                values=(
                    fine[0],
                    fine[1],
                    f"₹{fine[2]}",
                    fine[3],
                    fine[4]
                )
            )

        # Payment section
        payment_frame = ttk.LabelFrame(
            self.content,
            text="Fine Payment"
        )

        payment_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ttk.Label(
            payment_frame,
            text="Fine ID:"
        ).grid(row=0, column=0, padx=10, pady=10)

        fine_id_entry = ttk.Entry(payment_frame, width=15)
        fine_id_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(
            payment_frame,
            text="Payment Amount:"
        ).grid(row=0, column=2, padx=10, pady=10)

        amount_entry = ttk.Entry(payment_frame, width=15)
        amount_entry.grid(row=0, column=3, padx=10, pady=10)

        ttk.Label(
            payment_frame,
            text="Payment Method:"
        ).grid(row=0, column=4, padx=10, pady=10)

        payment_method = ttk.Combobox(
            payment_frame,
            values=("CASH", "CARD", "UPI", "ONLINE"),
            state="readonly",
            width=12
        )

        payment_method.grid(
            row=0,
            column=5,
            padx=10,
            pady=10
        )

        payment_method.set("UPI")

        def process_payment():

            try:
                fine_id = int(fine_id_entry.get())
                amount = float(amount_entry.get())
                method = payment_method.get()

                make_fine_payment(
                    fine_id,
                    amount,
                    method
                )

                messagebox.showinfo(
                    "Success",
                    "Fine payment successful."
                )

                # Refresh the Fines page
                self.show_fines_page()

            except ValueError as e:

                messagebox.showerror(
                    "Payment Error",
                    str(e)
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        ttk.Button(
            payment_frame,
            text="Pay Fine",
            command=process_payment
        ).grid(
            row=0,
            column=6,
            padx=15,
            pady=10
        )


    def show_reservations_page(self):

        ttk.Label(
            self.content,
            text="Book Reservations",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        columns = (
            "reservation_id",
            "book_id",
            "book",
            "member_id",
            "member",
            "reservation_date",
            "expiry_date",
            "status"
        )

        tree = ttk.Treeview(
            self.content,
            columns=columns,
            show="headings"
        )

        headings = {
            "reservation_id": "Reservation ID",
            "book_id": "Book ID",
            "book": "Book",
            "member_id": "Member ID",
            "member": "Member",
            "reservation_date": "Reservation Date",
            "expiry_date": "Expiry Date",
            "status": "Status"
        }

        for column, heading in headings.items():
            tree.heading(column, text=heading)

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        reservations = get_reservations()

        for reservation in reservations:
            tree.insert(
                "",
                "end",
                values=reservation
            )

        def cancel_selected_reservation():

            selected = tree.selection()

            if not selected:
                messagebox.showwarning(
                    "No Selection",
                    "Please select a reservation."
                )
                return

            values = tree.item(selected[0], "values")

            reservation_id = int(values[0])

            try:
                cancel_library_reservation(reservation_id)

                messagebox.showinfo(
                    "Success",
                    "Reservation cancelled successfully."
                )

                # Refresh page
                self.show_reservations_page()

            except ValueError as e:

                messagebox.showerror(
                    "Cancellation Error",
                    str(e)
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )


        def fulfill_selected_reservation():

            selected = tree.selection()

            if not selected:
                messagebox.showwarning(
                    "No Selection",
                    "Please select a reservation."
                )
                return

            values = tree.item(selected[0], "values")

            reservation_id = int(values[0])

            try:
                fulfill_library_reservation(reservation_id)

                messagebox.showinfo(
                    "Success",
                    "Reservation fulfilled successfully."
                )

                # Refresh page
                self.show_reservations_page()

            except ValueError as e:

                messagebox.showerror(
                    "Fulfillment Error",
                    str(e)
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )
                

        def expire_selected_reservations():

            try:
                count = expire_library_reservations()

                messagebox.showinfo(
                    "Reservation Expiry",
                    f"{count} reservation(s) expired."
                )

                # Refresh page
                self.show_reservations_page()

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )


        ttk.Button(
            self.content,
            text="Cancel Reservation",
            command=cancel_selected_reservation
        ).pack(
            pady=10
        )


        ttk.Button(
            self.content,
            text="Fulfill Reservation",
            command=fulfill_selected_reservation
        ).pack(
            pady=5
        )



        ttk.Button(
            self.content,
            text="Expire Reservations",
            command=expire_selected_reservations
        ).pack(
            pady=5
        )



def run_app():

    root = tk.Tk()

    app = MainWindow(root)

    root.mainloop()