from argparse import ArgumentParser, Namespace
from src.ad import create_tree, get_aduser


def main(args: Namespace) -> None:
    tree = create_tree(ad_object=get_aduser(args.user))
    if args.nogui:
        print(tree)
    else:
        pass


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(
        prog="ADUser-Group-Treeviewer",
        description="Get a treediagram of all group memberships of a ADuser",
        epilog="© Kevin Fischer, Weidmüller Interface GmbH & Co. KG"
    )
    parser.add_argument("-ng", "--nogui", required=False, help="Get the output printed on the current console", action='store_true')
    parser.add_argument("-u", "--user", required=True, help="Active Directory username of user to browse groups")
    main(args=parser.parse_args())