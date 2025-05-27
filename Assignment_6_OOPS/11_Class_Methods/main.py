# Create a class Book with a class variable total_books.
#  Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_book = 0 # class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_book += 1

b1 = Book("Pride and Prejudice", "Jane Austen")
b2 = Book("To Kill a Mockingbird", "Harper Lee")
b3 = Book("The Alchemist", "Paulo Coelho")

print(f"Total Books: {Book.total_book}")




   