from LIBRARY.library import Library

class MyApp():
    def __init__(self):
        pass

    def addBook(self, title, author, available):
        self.title = title.get()
        self.author = author.get()
        self.available = available.get()
        book = Library()
        book.add_book(self.title, self.author, self.available)

    def removeBook(self, title):
        self.title = title.get()
        del_book = Library()
        del_book.remove_book(self.title)

    def searchBook(self, title, val):
        self.title = title.get()
        s_book = Library()
        res = s_book.search_book(self.title, val)
        return res

    
    def showBooks(self):
        books = Library()
        result = books.show_books()
        return result

