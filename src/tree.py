from tkinter import *
from tkinter import ttk
from treelib import Tree

def show_tree(tree: Tree=None) -> None:
    """
    Generate a tkinter view of the tree.

    Args:
        tree (Tree, optional): Tree to build the tree. Defaults to None.
    """

    # Init tkinter
    app = Tk()
    app.title(f"Groups of {tree.root}")
    app.geometry(f"{app.winfo_screenwidth() - 10}x{app.winfo_screenheight() - 10}+0+0")
    info = Text(app, state=DISABLED)
    ttk.Label(app, text ="Hierarchical view").pack()
    treeview = ttk.Treeview(app) 
    treeview.pack(side="left", fill="both", expand=True)

    infos = {} # Future feature

    # Create tree nodes in treeview component
    for node in tree.all_nodes():
        parent = node.bpointer
        if parent is not None:
            parent_id = parent
        else:
            parent_id = ""
        treeview.insert(parent_id, "end", node.identifier, text=node.tag, open=True)
        infos[node.identifier] = f"Name: {node.tag}"
    
    info.pack(side="right", fill="both", expand=True) 
    app.mainloop()