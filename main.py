from argparse import ArgumentParser, Namespace
from src.ad import create_tree, get_aduser
from src.tree import show_tree
from treelib import Tree


def main(args: Namespace) -> None:
    """
    Main function of the program

    Args:
        args (Namespace): Start arguments by argumentparser
    """
    tree: Tree = create_tree(ad_object=get_aduser(args.user))
    if args.nogui:
        print(tree)
    else:
        show_tree(tree=tree)


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(
        prog="ADUser-Group-Treeviewer",
        description="Get a treediagram of all group memberships of a ADuser",
        epilog="© Kevin Fischer, Weidmüller Interface GmbH & Co. KG"
    )
    parser.add_argument("-ng", "--nogui", required=False, help="Get the output printed on the current console", action='store_true')
    parser.add_argument("-u", "--user", required=True, help="Active Directory username of user to browse groups")
    parser.add_argument("-o", "--outfile", required=False, help="Filename of output HTML file.")
    main(args=parser.parse_args())