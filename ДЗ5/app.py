from pydantic import BaseModel, EmailStr
from utils.log_operation import log_operation

class Book(BaseModel):
    title: str
    author: str
    year: int
    avaliable: bool
    categories: list[str]

class User(BaseModel):
    name: str
    email: EmailStr
    membership_id: str

class Library(BaseModel):
    books: list
    users: list

    @log_operation('adding book')
    def add_book(self, book: Book) -> Book | None:
        self.books.append(book)
    
    @log_operation('finding book')
    def find_book(self, title: str | None = None, author: str | None = None, year: int | None = None, category: str | None = None) -> Book | None:
        for book in self.books:
            if  (
                    ( title is None or book.title == title)
                    and ( author is None or book.author == author ) 
                    and (year is None or book.year == year) 
                    and (category is None or book.categories.count(category))
                ):
                return book
        return None
    
    @log_operation('checking book')
    def is_book_borrow(self, title: str) -> bool:
        if self.find_book(title) is None:
            raise BookNotAvailable(title)
        book = self.find_book(title)
        return book.avaliable

    @log_operation('returning book')
    def return_book(self, book: Book) -> None:
        for b in self.books:
            if b == book:
                b.avaliable = True
                break

    @log_operation('borrowing book')
    def borrow_book(self, book: Book) -> None:
        if not book.avaliable:
            raise BookNotAvailable(book.title)
        book.avaliable = False

class BookNotAvailable(Exception):
    def __init__(self, title: str):
        self.title = title
        super().__init__(f"Book {title} not availeble")



book1 = Book(title="War and Peace", author="Leo Tolstoy", year=1869, avaliable=True, categories=["Novel"])
book2 = Book(title="The Lord of the Rings", author="J.R.R. Tolkien", year=1954, avaliable=True, categories=["Fantasy"])

library = Library(books=[book1, book2], users=[ User(name="John", email="lazyboi@example.com", membership_id="123")])

library.add_book(book=Book(title="The Hobbit", author="J.R.R. Tolkien", year=1937, avaliable=True, categories=["Fantasy"]))

print(library.find_book(title="War and Peace"))
print(library.is_book_borrow(title="War and Peace"))
library.borrow_book(book=book1)
print(library.is_book_borrow(title="War and Peace"))
library.return_book(book=book1)
print(library.is_book_borrow(title="War and Peace"))