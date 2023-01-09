from tkinter import *
from tkinter import ttk
from treelib import Tree
import pyad.adquery

attributes: list = [
                "canonicalName",
                "cn",
                "distinguishedName",
                "dSCorePropagationData",
                "groupType",
                "instanceType",
                "member",
                "memberOf",
                "managedBy",
                "name",
                "nTSecurityDescriptor",
                "ObjectCategory",
                "ObjectClass",
                "ObjectGUID",
                "objectSid",
                "SamAccountName",
                "sAMAccountType",
                "sDRightsEffective",
                "SIDHistory",
                "uSNChanged",
                "uSNCreated",
                "whenChanged",
                "whenCreated",
            ]


app = Tk()
treeview = ttk.Treeview(app)
info = Text(app, state=DISABLED)
infos = {}


def onClick(event):
    info.configure(state="normal")
    info.delete('1.0', END)
    info.insert(END, chars=infos[treeview.selection()[0]])
    info.configure(state=DISABLED)


def show_tree(tree: Tree=None) -> None:
    """
    Generate a tkinter view of the tree.

    Args:
        tree (Tree, optional): Tree to build the tree. Defaults to None.
    """

    # Init tkinter
    app.title(f"Groups of {tree.root}")
    app.geometry(f"{app.winfo_screenwidth() - 10}x{app.winfo_screenheight() - 10}+0+0")
    ttk.Label(app, text ="Hierarchical view").pack()
    treeview.pack(side="left", fill="both", expand=True)
    # Create tree nodes in treeview component
    for node in tree.all_nodes():
        parent = node.bpointer
        if parent is not None:
            parent_id = parent
        else:
            parent_id = ""

        query: pyad.adquery.ADQuery = pyad.adquery.ADQuery()
        query.execute_query(
            attributes=attributes,
            where_clause=f"SamAccountName = '{node.data}'"
        )
        results = query.get_single_result()
        infos[node.identifier] = ""
        for attr in results:
            infos[node.identifier] += f"{attr}\t:\t\t{results[attr]}\n\n"
        treeview.insert(parent_id, "end", node.identifier, text=node.tag, open=True, )

    treeview.bind("<ButtonRelease-1>", onClick)
    info.pack(side="right", fill="both", expand=True) 
    app.mainloop()