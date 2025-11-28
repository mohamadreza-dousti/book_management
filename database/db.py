import sqlite3

class LibraryDB:
    def __init__(self, db_name = 'database/library.db'):
        self.con = sqlite3.connect(db_name)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            author TEXT,
            status BOOLEAN DEFAULT 1
            )
        ''')
        self.con.commit()

    def add_book(self, title, author, status):
        self.cursor.execute('''
        INSERT INTO books (title, author, status)
        VALUES (?, ?, ?)
        ''', (title, author, status))
        self.con.commit()

    
    def remove_book(self, title):
        self.cursor.execute('DELETE FROM books WHERE title = ?', (title,))
        self.con.commit()
    
    def show_books(self):
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()
    
    def close(self):
        self.con.close()