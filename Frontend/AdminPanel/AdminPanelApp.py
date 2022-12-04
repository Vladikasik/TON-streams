import tkinter as tk
from tkinter import ttk


class MainController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Admin Panel")
        self.geometry("800x600")

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
        tk.Frame.__init__(self, parent)
        for i in range(8):
            self.rowconfigure(i, minsize=100)
        for i in range(6):
            self.columnconfigure(i, minsize=100)
        label = ttk.Label(self, text="LoginPage", font=("Inter", 36))
        label.configure(anchor="center")
        label.grid(row=1, column=2, columnspan=4, sticky="nsew")


# Driver Code
app = MainController()
app.mainloop()
