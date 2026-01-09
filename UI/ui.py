import customtkinter as ctk
from UI.main_ui import MyApp

class Ui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('600x600')
        self.title('Book management')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.lable_add = ctk.CTkLabel(self, text='1.Add book', text_color='gray')
        self.lable_add.grid(row=0, column=0, pady=10)
        self.lable_add = ctk.CTkLabel(self, text='کتاب افزودن.1', text_color='gray')
        self.lable_add.grid(row=0, column=1, pady=10)

        self.lable_remove = ctk.CTkLabel(self, text='2.Remove book', text_color='gray')
        self.lable_remove.grid(row=1, column=0, pady=10)
        self.lable_remove = ctk.CTkLabel(self, text='کتاب حذف.2', text_color='gray')
        self.lable_remove.grid(row=1, column=1, pady=10)
        
        self.lable_search = ctk.CTkLabel(self, text='3.Search book', text_color='gray')
        self.lable_search.grid(row=2, column=0, pady=10)
        self.lable_remove = ctk.CTkLabel(self, text='کتاب جوی و جست.3', text_color='gray')
        self.lable_remove.grid(row=2, column=1, pady=10)

        self.lable_show = ctk.CTkLabel(self, text='4.Show book', text_color='gray')
        self.lable_show.grid(row=3, column=0, pady=10)
        self.lable_remove = ctk.CTkLabel(self, text='کتاب نمایش.4', text_color='gray')
        self.lable_remove.grid(row=3, column=1, pady=10)

        self.get_order = ctk.CTkEntry(self, placeholder_text='choose your option')
        self.get_order.grid(row=4, columnspan=2, pady=5)

        self.send_btn = ctk.CTkButton(self, text='send', command=self.get)
        self.send_btn.grid(row=5, columnspan=2, pady=5)

        self.bck_btn = ctk.CTkButton(self, text='back', command=self.back, state='disabled',
                                text_color_disabled='gray')
        self.bck_btn.grid(row=6, columnspan=2, pady=5)

        self.display = ctk.CTkScrollableFrame(self, width=350, height=250, corner_radius=10)
        self.display.grid(row=7, columnspan=2)

    def add_book(self):
        self.lable_title = ctk.CTkLabel(self.display, text='Add book')
        self.lable_title.pack(pady=5, fill='both')

        self.title = ctk.CTkEntry(self.display, placeholder_text='title')
        self.title.pack(pady=2)

        self.author = ctk.CTkEntry(self.display, placeholder_text='author')
        self.author.pack(pady=2)

        self.avalable = ctk.CTkEntry(self.display, placeholder_text='avalable')
        self.avalable.pack(pady=2)

        self.save_btn_avalable = ctk.CTkButton(self.display, text='save', command=lambda:self.save(self.title, self.author, self.avalable, self.save_btn_avalable))
        self.save_btn_avalable.pack(pady=5)

    def remove_book(self):
        self.lable_title = ctk.CTkLabel(self.display, text='Remove book')
        self.lable_title.pack(pady=5)

        self.title_rem = ctk.CTkEntry(self.display, placeholder_text='enter title')
        self.title_rem.pack(pady=2)

        self.remove_btn_avalable = ctk.CTkButton(self.display, text='remove', command=lambda:self.remove(self.title_rem, self.remove_btn_avalable))
        self.remove_btn_avalable.pack(pady=5)


    def search_book(self):
        self.lable_title = ctk.CTkLabel(self.display, text='Search book')
        self.lable_title.pack(pady=5)

        self.title_ser = ctk.CTkEntry(self.display, placeholder_text='enter title')
        self.title_ser.pack(pady=2)

        self.option = ['1', '0', 'both']
        self.filter_var = ctk.StringVar(value='status')

        self.filter = ctk.CTkOptionMenu(self.display, values=self.option, variable=self.filter_var, command=lambda value:self.search(self.title_ser, self.scroll_frame,self.filter, value))
        self.filter.pack(pady=3)

        self.search_btn_avalable = ctk.CTkButton(self.display, text='search', command=lambda:self.search(self.title_ser, self.scroll_frame, self.filter))
        self.search_btn_avalable.pack(pady=5)

        self.scroll_frame = ctk.CTkScrollableFrame(self.display, width=250, height=30)
        self.scroll_frame.pack(pady=15)
        self.scroll_frame.grid_columnconfigure(0, weight=1)
        self.scroll_frame.grid_columnconfigure(1, weight=1)
        self.scroll_frame.grid_columnconfigure(2, weight=1)

        self.books = MyApp()
        self.result = self.books.showBooks()
        i=0
        for self.book in self.result:
            self.book_title = ctk.CTkLabel(self.scroll_frame, fg_color='black', text=f'title:{self.book[0]}')
            self.book_title.grid(row=i, column=0, pady=5)
            self.book_author = ctk.CTkLabel(self.scroll_frame, fg_color='black', text=f'author:{self.book[1]}')
            self.book_author.grid(row=i, column=1)
            self.book_status = ctk.CTkLabel(self.scroll_frame, fg_color='black', text=f'status:{self.book[2]}')
            self.book_status.grid(row=i, column=2)
            i += 1


    def show_books(self):
        self.lable_title = ctk.CTkLabel(self.display, text='Show books')
        self.lable_title.pack(pady=5)

        self.show_btn_avalable = ctk.CTkButton(self.display, text='show books', command=lambda:self.show(self.show_btn_avalable))
        self.show_btn_avalable.pack(pady=5)

    def default(self):
        self.lable_err = ctk.CTkLabel(self.display, text='choose your option from 1-4', fg_color='red')
        self.lable_err.pack(pady=20)


    def get(self):
        self.bck_btn.configure(state='abled', hover=True)
        self.res = self.get_order.get()
        switch = {
                '1': self.add_book,
                '2': self.remove_book,
                '3': self.search_book,
                '4': self.show_books
            }
        switch.get(self.res, self.default)()

    def save(self, title, author, avalable, save_btn_avalable):
        save_btn_avalable.configure(state='disabled', fg_color='green',
                                    text='saved!')
        self.save = MyApp()
        self.save.addBook(title, author, avalable)
        

    def remove(self, title_rem, remove_btn_avalable):
        remove_btn_avalable.configure(state='disabled', fg_color='red',
                                    text='removed!')
        self.remove = MyApp()
        self.remove.removeBook(title_rem)
        

    def search(self, title_ser, scroll_frame, filter, value=2):
        value = filter.get()
        for self.widget in scroll_frame.winfo_children():
            self.widget.destroy()
        self.search_b = MyApp()
        self.res = self.search_b.searchBook(title_ser, value)
        if self.res == []:
            self.book_lab = ctk.CTkLabel(scroll_frame, text='None', fg_color='black')
            self.book_lab.pack(pady=20)
        else:
            i=0
            for self.book in self.res:
                self.book_title = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'title:{self.book[0]}')
                self.book_title.grid(row=i, column=0, pady=5)
                self.book_author = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'author:{self.book[1]}')
                self.book_author.grid(row=i, column=1)
                self.book_status = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'status:{self.book[2]}')
                self.book_status.grid(row=i, column=2)
                i+=1


    def show(self, show_btn_avalable):
        show_btn_avalable.configure(state='disabled')
        self.scroll_frame = ctk.CTkScrollableFrame(self.display, width=250, height=30)
        self.scroll_frame.pack(pady=15)
        self.books = MyApp()
        self.result = self.books.showBooks()
        for self.book in self.result:
            self.book_label = ctk.CTkLabel(self.scroll_frame, fg_color='black', text=f'title:{self.book[0]}  author:{self.book[1]}  status:{self.book[2]}')
            self.book_label.pack(pady=5)

    def back(self):
        self.get_order.delete(0, 'end')
        self.bck_btn.configure(state='disabled')
        for self.widget in self.display.winfo_children():
            self.widget.destroy()