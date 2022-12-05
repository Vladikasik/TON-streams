import threading
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time


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

        img_tonkooper = ImageTk.PhotoImage(file="images/tonkooper.png")
        img_tonkooper_hover = ImageTk.PhotoImage(file="images/tonkooper_hover.png")
        login_tonkooper = tk.Label(self, image=img_tonkooper)
        login_tonkooper.grid(row=3, column=3, columnspan=2)
        login_tonkooper.image = img_tonkooper
        login_tonkooper.bind('<Button-1>', lambda e: self.spawn_waiting_window())
        login_tonkooper.bind('<Enter>', lambda e: login_tonkooper.configure(image=img_tonkooper_hover))
        login_tonkooper.bind('<Leave>', lambda e: login_tonkooper.configure(image=img_tonkooper))

        img_looplex = ImageTk.PhotoImage(file='images/looplex.png')
        img_looplex_hover = ImageTk.PhotoImage(file="images/looplex_hover.png")
        login_looplex = tk.Label(self, image=img_looplex)
        login_looplex.grid(row=4, column=3, columnspan=2)
        login_looplex.image = img_looplex
        login_looplex.bind('<Button-1>', lambda e: self.spawn_not_ready_window())
        login_looplex.bind('<Enter>', func=lambda e: login_looplex.configure(image=img_looplex_hover))
        login_looplex.bind('<Leave>', func=lambda e: login_looplex.configure(image=img_looplex))

    @staticmethod
    def spawn_not_ready_window():
        root_not_ready = tk.Toplevel()
        root_not_ready.title("Connect Looplex")
        root_not_ready.geometry('200x100')
        root_not_ready.resizable(False, False)
        root_not_ready.rowconfigure(0, minsize=50, weight=1)
        root_not_ready.rowconfigure(1, minsize=50, weight=1)
        for i in range(3):
            root_not_ready.columnconfigure(i, weight=1)
        sorry_text = ttk.Label(root_not_ready, text="Sorry, this login via this wallet is not available yet",
                               wraplength=200, justify="center", font=("Inter", 16))
        sorry_text.configure(anchor="center")
        sorry_text.grid(row=0, column=0, columnspan=3, sticky="nsew")
        button_ok_close = ttk.Button(root_not_ready, text="OK", command=root_not_ready.destroy)
        button_ok_close.grid(row=1, column=1, sticky="nsew")

    def spawn_waiting_window(self):
        root_wait = tk.Toplevel()
        root_wait.title("Connect TonKooper")
        root_wait.geometry('300x300')
        root_wait.resizable(False, False)
        for i in range(3):
            root_wait.rowconfigure(i, minsize=100, weight=1)
        for i in range(3):
            root_wait.columnconfigure(i, minsize=100, weight=1)
        waiting_text = ttk.Label(root_wait, text="Waiting for your confirmation", justify="center", font=("Inter", 16))
        waiting_text.configure(anchor="center")
        waiting_text.grid(row=0, column=0, columnspan=3, sticky="nsew")
        loading_gif_label = tk.Label(root_wait)
        loading_gif_label.grid(row=1, column=1)
        approx_time_text = ttk.Label(root_wait, text="Approximate time: less than 1 minute", font=("Inter", 14),
                                     justify="center")
        approx_time_text.configure(anchor="center")
        approx_time_text.grid(row=2, column=0, columnspan=3, sticky="nsew")

        def play_animation(label_animation, frames):
            while 1:
                for frame in frames:
                    label_animation.configure(image=frame)
                    label_animation.update_idletasks()
                    time.sleep(0.1)

        frames_list = []
        for frame_num in range(12):
            img = tk.PhotoImage(file=f'images/loading.gif', format=f"gif -index {frame_num}",
                                master=root_wait)
            frames_list.append(img)

        thread = threading.Thread(target=play_animation, args=(loading_gif_label, frames_list))
        thread.start()

        root_wait.mainloop()


# Driver Code
app = MainController()
app.mainloop()
