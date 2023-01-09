from argparse import ArgumentParser, Namespace
from src.ad import create_tree, get_aduser
from src.tree import show_tree
from treelib import Tree
from src.interception import show_input


def main(args: Namespace) -> None:
    """
    Main function of the program

    Args:
        args (Namespace): Start arguments by argumentparser
    """

    if args.nogui:
        if args.user:
            user = args.user
        else:
            user = input("Enter SamAccountName: ")
        tree: Tree = create_tree(ad_object=get_aduser(user))
        print(tree)
    else:
        if args.user:
            tree: Tree = create_tree(ad_object=get_aduser(args.user))
            show_tree(tree=tree)
        show_input()


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(
        prog="ADUser-Group-Treeviewer",
        description="Get a treediagram of all group memberships of a ADuser",
        epilog="© Kevin Fischer, Weidmüller Interface GmbH & Co. KG"
    )
    parser.add_argument("-ng", "--nogui", required=False, help="Get the output printed on the current console", action='store_true')
    parser.add_argument("-u", "--user", required=False, help="Active Directory username of user to browse groups")
    parser.add_argument("-o", "--outfile", required=False, help="Filename of output HTML file.")
    main(args=parser.parse_args())