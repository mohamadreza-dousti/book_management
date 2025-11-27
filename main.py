import os
from LIBRARY.library import Library


def addBook():
    os.system('cls')
    title = input("enter book name: ")
    author = input("enter author: ")
    available = int(input('enter status: '))
    book = Library()
    book.add_book(title, author, available)
    print("book added succefully!")

def removeBook():
    os.system('cls')
    title = input("enter title: ")
    del_book = Library()
    del_book.remove_book(title)
    print("book removed succefully!")

def searchBook():
    os.system('cls')
    title = input("enter title: ")
    s_book = Library()
    print(s_book.search_book(title))

def showBooks():
    os.system('cls')
    print("\t\t\tSHOW BOOKS")
    books = Library()
    result = books.show_books()
    print(result)

def Exit():
    os.system('cls')


def display():
    print("\t\t\tBOOK")
    print('1.add book\n\n2.remove book\n\n3.search book\n\n'
          '4.show books\n\n5.exit\n\n')
    
def default():
    global x
    while x>5 or x<1:
        print("choose your option from 1 to 5")
        break
    
    
if __name__ == "__main__":
    while True:
        display()
        x = int(input("choose your option: "))
        switch = {
            1: addBook,
            2: removeBook,
            3: searchBook,
            4: showBooks,
            5: Exit
        }

        switch.get(x, default)()
        if x == 5:
            break
        os.system("pause")
        os.system('cls')