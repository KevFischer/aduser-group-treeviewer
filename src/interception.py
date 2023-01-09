from tkinter import *
from tkinter import ttk
from src.ad import get_aduser, create_tree
from src.tree import show_tree


def show_input():
    app = Tk()
    user_in = ttk.Entry(app)


    def check_input(event):
        try:
            user = get_aduser(user_in.get())
            if user is not None or user != "":
                tree = create_tree(ad_object=user)
                show_tree(tree=tree)
                app.destroy
        except:
            raise Exception("Invalid username")


    confirm = ttk.Button(app, text="Confirm")
    confirm.bind("<ButtonRelease-1>", check_input)
    app.title(f"Enter SamAccountName of ADUser")
    app.geometry(f"{200}x{100}+0+0")
    user_in.pack(side="top")
    confirm.pack(side="bottom")
    app.mainloop()