import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MainController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Admin Panel")
        self.geometry("800x600")
        self.minsize(800, 600)

        # creating a parent container, which will include all other frames
        parent_container = tk.Frame(self)
        parent_container.pack(side="top", fill="both", expand=True)
        parent_container.grid_rowconfigure(0, weight=1)
        parent_container.grid_columnconfigure(0, weight=1)

        # prepare all pages to be displayed
        self.frames = {}
        all_pages = (LoginPage,)
        for F in all_pages:
            frame = F(parent_container, self)  # initialize the frame for future use
            self.frames[F] = frame  # store the frame in a dictionary
            frame.grid(row=0, column=0, sticky="nsew")  # put the frame in the parent container

        # display the first page
        self.show_frame(LoginPage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        for i in range(6):
            self.rowconfigure(i, minsize=100, weight=1)
        for i in range(8):
            self.columnconfigure(i, minsize=100, weight=1)

        # self.configure(bg="red")
        # for rownum in range(6):
        #     for colnum in range(8):
        #         if (rownum == 1 and colnum == 2) or (rownum == 1 and colnum == 3) or (rownum == 1 and colnum == 4) or \
        #                 (rownum == 1 and colnum == 5) or \
        #            (rownum == 2 and colnum == 3) or (rownum == 2 and colnum == 4) or \
        #            (rownum == 3 and colnum == 3) or (rownum == 3 and colnum == 4):
        #             pass
        #         else:
        #             l = ttk.Label(self, text=f'{rownum}, {colnum}')
        #             l.configure(anchor='center')
        #             l.grid(row=rownum, column=colnum,sticky='nsew', padx=1, pady=1)

        ton_streams = ttk.Label(self, text="TON STREAMS", font=("Inter", 36))
        ton_streams.configure(anchor="center")
        ton_streams.grid(row=1, column=2, columnspan=4, sticky="nsew")

        login_info = ttk.Label(self, text="To enter Admin panel connect your wallet", font=("Inter", 16),
                               wraplength=200, justify="center")
        login_info.grid(row=2, column=3, columnspan=2, sticky="ns")

        img_tonkooper = ImageTk.PhotoImage(Image.open("images/tonkooper.png"))
        img_tonkooper_hover = ImageTk.PhotoImage(Image.open("images/tonkooper_hover.png"))
        login_tonkooper = tk.Label(self, image=img_tonkooper)
        login_tonkooper.grid(row=3, column=3, columnspan=2)
        login_tonkooper.image = img_tonkooper
        login_tonkooper.bind('<Button-1>', lambda e: print("clicked"))
        login_tonkooper.bind('<Enter>', lambda e: login_tonkooper.configure(image=img_tonkooper_hover))
        login_tonkooper.bind('<Leave>', lambda e: login_tonkooper.configure(image=img_tonkooper))

        img_looplex = ImageTk.PhotoImage(Image.open("images/looplex.png"))
        img_looplex_hover = ImageTk.PhotoImage(Image.open("images/looplex_hover.png"))
        login_looplex = tk.Label(self, image=img_looplex)
        login_looplex.grid(row=4, column=3, columnspan=2)
        login_looplex.image = img_looplex
        login_looplex.bind('<Enter>', func=lambda e: change_background(e, login_looplex, img_looplex_hover))
        login_looplex.bind('<Leave>', func=lambda e: change_background(e, login_looplex, img_looplex))

        def change_background(event, label_obj, img_obj):
            label_obj.configure(image=img_obj)

# Driver Code
app = MainController()
app.mainloop()
