class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.availability_status = True  # True means available, False means checked out

    def check_out_book(self):
        if self.availability_status:
            self.availability_status = False
            print(f"You have successfully checked out '{self.book_name}'.")
        else:
            print(f"Sorry, '{self.book_name}' is currently unavailable.")

    def return_book(self):
        if not self.availability_status:
            self.availability_status = True
            print(f"You have returned '{self.book_name}'. Thank you!")
        else:
            print(f"'{self.book_name}' is already in the library.")

    def display_available_books(self):
        # In this design, the object represents a single book, so we check its own status
        status = "Available" if self.availability_status else "Checked Out"
        print(f"Book: {self.book_name} by {self.author} | Status: {status}")

# --- Testing the Class ---
print("--- 6. Library Experiment ---")
book1 = Library("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Library("1984", "George Orwell")

book1.display_available_books()
book1.check_out_book()
book1.display_available_books()
book1.check_out_book()  # Try checking out again
book1.return_book()
book1.display_available_books()
