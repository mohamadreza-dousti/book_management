class Library:
    books = []
    def __init__(self, title=None, author=None, status=1):
        self.title = title
        self.author = author
        self.status = status
        

    def add_book(self, title, author, status):
        Library.books.append({'title':title, 'author':author, 'status' :status})

    @classmethod
    def remove_book(cls, title):
        cls.books = [item for item in cls.books 
                         if item['title'] != title]

    def search_book(self, title):
        for book in Library.books:
            if book['status'] != False and book['title'] == title:
                return book 

    @classmethod
    def show_books(cls):
        return cls.books