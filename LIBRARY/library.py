from db import LibraryDB

class Library:
    def __init__(self, title=None, author=None, status=1):
        self.title = title
        self.author = author
        self.status = status
        db = LibraryDB()
        db.create_table()
        db.close()
        

    def add_book(self, title, author, status):
        #Library.books.append({'title':title, 'author':author, 'status' :status})
        add = LibraryDB()
        add.add_book(title, author, status)
        add.close()


    def remove_book(self, title):
        # cls.books = [item for item in cls.books 
        #                  if item['title'] != title]
        remove = LibraryDB()
        remove.remove_book(title)
        remove.close()

    def search_book(self, title):
        # for book in Library.books:
        #     if book['status'] != False and book['title'] == title:
        #         return book 
        books = LibraryDB()
        result = books.show_books()
        books.close()
        for book in result:
            if book[0] == title:
                if book[2] != False:
                    return book


    def show_books(self):
        # return cls.books
        books = LibraryDB()
        result = books.show_books()
        books.close()
        return result