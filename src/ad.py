from pyad import *
from treelib import Node, Tree
import pyad.adquery, pyad.adsearch, pyad.adcomputer, pyad.adbase, pyad.adcontainer, pyad.addomain, pyad.adgroup, pyad.aduser, pyad.pyad


def get_aduser(name: str=None) -> pyad.aduser.ADUser:
    """
    Function to get a pyad.ADUser object from a string

    Args:
        name (str, optional): String of the searched user. Defaults to None.

    Raises:
        Exception: Exception when user can not be resolved in AD

    Returns:
        pyad.ADUser: ADUser Object matching to given string.
    """
    query: pyad.adquery.ADQuery= pyad.adquery.ADQuery()
    query.execute_query(
        attributes=["name"],
        where_clause=f"SamAccountName = '{name}'"
    )
    name = query.get_single_result()["name"]
    try:
        user = pyad.aduser.ADUser.from_cn(name)
    except:
        raise Exception("User not found")
    return user


def get_groups(user: pyad.aduser.ADUser=None) -> list:
    """
    Function to get all groups of a user

    Args:
        user (pyad.ADUser, optional): ADUser object to get the memberships from. Defaults to None.

    Raises:
        Exception: Exception when user is not an pyad.ADUser object

    Returns:
        list: list of all distinguishedNames the user is a member of
    """
    try:
        return user.get_attribute(attribute="memberOf")
    except:
        raise Exception("User is no PYAD user object")


def get_adgroup(name: str=None) -> pyad.adgroup.ADGroup:
    """
    Get a specified group by its name

    Args:
        name (str, optional): Name of the group. Defaults to None.

    Raises:
        Exception: When group can not be resolbved

    Returns:
        pyad.ADGroup: Group matching to name
    """
    try:
        group = pyad.adgroup.ADGroup.from_dn(name)
    except:
        raise Exception("Group not found")
    return group


def create_tree(tree: Tree=Tree(), parent: Node=None, ad_object=None) -> Tree:
    """
    Generate a hierarchical tree a given ad_object is member of.

    Args:
        tree (Tree, optional): Tree object for recursion, leave empty! Defaults to Tree().
        parent (Node, optional): Parent for recursion, leave empty! Defaults to None.
        ad_object (pyad.ADObject, optional): ADObject, should be root element. Defaults to None.

    Returns:
        treelib.Tree: Hierarchical tree of memberships
    """

    # Root Element
    if parent is None:
        name: str = "".join(ad_object.get_attribute("SamAccountName"))
        tree.create_node(data=name, identifier=name, tag=name)
        parent = name

    memberOf: list = ad_object.get_attribute(attribute="memberOf")
    for membership in memberOf:
        group: pyad.adgroup.ADGroup = get_adgroup(membership)
        name: str = "".join(group.get_attribute("SamAccountName"))

        # Duplicate identifier prevention
        id: str = name
        i: int = 1
        while tree.get_node(id) is not None:
            id += f" (DUPLICATE {i})"
            i += 1
        
        tree.create_node(data=name, identifier=id, parent=parent, tag=id)

        # Check if child nodes have groups and start recursion
        if group.get_attribute("memberOf") is not []:
            tree = create_tree(tree=tree, parent=id, ad_object=group)
    return tree