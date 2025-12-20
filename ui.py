import customtkinter as ctk
from UI.main_ui import MyApp

class Ui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('600x600')
        self.title('Book management')
        self.grid_columnconfigure(0, weight=1)

        self.lable_add = ctk.CTkLabel(self, text='1.Add book', text_color='gray')
        self.lable_add.grid(row=0, column=0, pady=10)

        self.lable_remove = ctk.CTkLabel(self, text='2.Remove book', text_color='gray')
        self.lable_remove.grid(row=1, column=0, pady=10)

        self.lable_search = ctk.CTkLabel(self, text='3.Search book', text_color='gray')
        self.lable_search.grid(row=2, column=0, pady=10)

        self.lable_show = ctk.CTkLabel(self, text='4.Show book', text_color='gray')
        self.lable_show.grid(row=3, column=0, pady=10)

        self.get_order = ctk.CTkEntry(self, placeholder_text='choose your option')
        self.get_order.grid(row=4, column=0, pady=5)

        self.send_btn = ctk.CTkButton(self, text='send', command=self.get)
        self.send_btn.grid(row=5, column=0, pady=5)

        self.bck_btn = ctk.CTkButton(self, text='back', command=self.back, state='disabled',
                                text_color_disabled='gray')
        self.bck_btn.grid(row=6, column=0, pady=5)

        self.display = ctk.CTkScrollableFrame(self, width=350, height=250, corner_radius=10)
        self.display.grid(row=7, column=0)

    def add_book(self):
        frame = ctk.CTkFrame(self.display)
        frame.pack()

        lable_title = ctk.CTkLabel(frame, text='Add book')
        lable_title.pack(pady=5)

        global title
        title = ctk.CTkEntry(frame, placeholder_text='title')
        title.pack(pady=2)

        global author
        author = ctk.CTkEntry(frame, placeholder_text='author')
        author.pack(pady=2)

        global avalable
        avalable = ctk.CTkEntry(frame, placeholder_text='avalable')
        avalable.pack(pady=2)

        global save_btn_avalable
        save_btn_avalable = ctk.CTkButton(frame, text='save', command=self.save)
        save_btn_avalable.pack(pady=5)

    def remove_book(self):
        frame = ctk.CTkFrame(self.display)
        frame.pack()

        lable_title = ctk.CTkLabel(frame, text='Remove book')
        lable_title.pack(pady=5)

        global title_rem
        title_rem = ctk.CTkEntry(frame, placeholder_text='enter title')
        title_rem.pack(pady=2)

        global remove_btn_avalable
        remove_btn_avalable = ctk.CTkButton(frame, text='remove', command=self.remove)
        remove_btn_avalable.pack(pady=5)


    def search_book(self):
        global frame
        frame = ctk.CTkFrame(self.display)
        frame.pack()

        lable_title = ctk.CTkLabel(frame, text='Search book')
        lable_title.pack(pady=5)

        global title_ser
        title_ser = ctk.CTkEntry(frame, placeholder_text='enter title')
        title_ser.pack(pady=2)

        option = ['1', '0', 'both']
        filter_var = ctk.StringVar(value='status')
        global filter
        filter = ctk.CTkOptionMenu(frame, values=option, variable=filter_var, command=self.search)
        filter.pack(pady=3)

        global search_btn_avalable
        search_btn_avalable = ctk.CTkButton(frame, text='search', command=self.search)
        search_btn_avalable.pack(pady=5)

        global scroll_frame
        scroll_frame = ctk.CTkScrollableFrame(frame, width=250, height=30)
        scroll_frame.pack(pady=15)
        scroll_frame.grid_columnconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(1, weight=1)
        scroll_frame.grid_columnconfigure(2, weight=1)

        books = MyApp()
        result = books.showBooks()
        i=0
        for book in result:
            book_title = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'title:{book[0]}')
            book_title.grid(row=i, column=0, pady=5)
            book_author = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'author:{book[1]}')
            book_author.grid(row=i, column=1)
            book_status = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'status:{book[2]}')
            book_status.grid(row=i, column=2)
            i += 1


    def show_books(self):
        global frame
        frame = ctk.CTkFrame(self.display)
        frame.pack()

        lable_title = ctk.CTkLabel(frame, text='Show books')
        lable_title.pack(pady=5)

        global show_btn_avalable
        show_btn_avalable = ctk.CTkButton(frame, text='show books', command=self.show)
        show_btn_avalable.pack(pady=5)

    def default(self):
        frame = ctk.CTkFrame(self.display)
        frame.pack()
        lable_err = ctk.CTkLabel(frame, text='choose your option from 1-4', fg_color='red')
        lable_err.pack(pady=20)


    def get(self):
        self.bck_btn.configure(state='abled', hover=True)
        res = self.get_order.get()
        switch = {
                '1': self.add_book,
                '2': self.remove_book,
                '3': self.search_book,
                '4': self.show_books
            }
        switch.get(res, self.default)()

    def save(self):
        save_btn_avalable.configure(state='disabled', fg_color='green',
                                    text='saved!')
        save = MyApp()
        save.addBook(title, author, avalable)
        

    def remove(self):
        remove_btn_avalable.configure(state='disabled', fg_color='red',
                                    text='removed!')
        remove = MyApp()
        remove.removeBook(title_rem)
        

    def search(self, value=1):
        value = filter.get()
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        search = MyApp()
        res = search.searchBook(title_ser, value)
        if res == []:
            book_lab = ctk.CTkLabel(scroll_frame, text='None', fg_color='black')
            book_lab.pack(pady=20)
        else:
            i=0
            for book in res:
                book_title = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'title:{book[0]}')
                book_title.grid(row=i, column=0, pady=5)
                book_author = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'author:{book[1]}')
                book_author.grid(row=i, column=1)
                book_status = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'status:{book[2]}')
                book_status.grid(row=i, column=2)
                i+=1


    def show(self):
        show_btn_avalable.configure(state='disabled')
        scroll_frame = ctk.CTkScrollableFrame(frame, width=250, height=30)
        scroll_frame.pack(pady=15)
        books = MyApp()
        result = books.showBooks()
        for book in result:
            book_label = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'title:{book[0]}  author:{book[1]}  status:{book[2]}')
            book_label.pack(pady=5)

    def back(self):
        self.get_order.delete(0, 'end')
        self.bck_btn.configure(state='disabled')
        for widget in self.display.winfo_children():
            widget.destroy()

my_app = Ui()
my_app.mainloop()