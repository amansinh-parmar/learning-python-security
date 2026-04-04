"""Write a Library class with no_of_books and books as two instance variables. 
Write a program to create a library from this Library class and show how you can
print all books, add a book and get the number of books using different methods. 
Show that your program doesnt persist the books after the program is stopped!"""

class Library:
    def __init__(self):
        self.no_books = 0 
        self.books = []

    def add_book(self, book):
        self.books.append(book)

        self.no_books = len(self.books)

    def show_details(self):
        print(f"The library has {self.no_books} books. The Books are")
        for book in self.books:
            print(book)

a = Library()
a.add_book("Good Habits, Bad Habits")
a.add_book("Think Like a Monk")
a.show_details()