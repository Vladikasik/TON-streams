import tkinter as tk
from tkinter import ttk
import socket
import tonkooper_config as config
import time


class AppController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TonKooper App")
        self.geometry("400x100")
        self.resizable(None, None)

        # creating a parent container, which will include all other frames
        parent_container = tk.Frame(self)
        parent_container.pack(side="top", fill="both", expand=True)
        parent_container.grid_rowconfigure(0, weight=1)
        parent_container.grid_columnconfigure(0, weight=1)

        main_frame = MainPage(parent_container, self)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        for i in range(2):
            self.rowconfigure(i, minsize=50, weight=1)
        for i in range(4):
            self.columnconfigure(i, minsize=50, weight=1)

        confirm_text = ttk.Label(self, text='Confirm Ton Streams collection', font=("Inter", 16), justify="center")
        confirm_text.configure(anchor="center")
        confirm_text.grid(row=0, column=1, columnspan=2, sticky="nsew")
        button_approve_login = ttk.Button(self, text='Approve', command=lambda: self.send_wallet(button_approve_login))
        button_approve_login.grid(row=1, column=1, columnspan=2, sticky="nsew")

    @staticmethod
    def send_wallet(button_obj):
        button_obj.update_idletasks()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        wallet_b = config.wallets["Vlad"].encode('UTF-8')
        sock.sendto(wallet_b, ('127.0.0.1', 17001))


app = AppController()
app.mainloop()
