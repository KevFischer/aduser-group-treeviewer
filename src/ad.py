from pyad import *
from treelib import Node, Tree


def get_aduser(name: str=None):
    try:
        user = pyad.aduser.ADUser.from_cn(name)
    except:
        raise Exception("User not found")
    return user


def get_groups(user=None):
    try:
        return user.get_attribute(attribute="memberOf")
    except:
        raise Exception("User is no PYAD user object")


def get_adgroup(name: str=None):
    try:
        group = pyad.adgroup.ADGroup.from_dn(name)
    except:
        raise Exception("Group not found")
    return group


def get_groups_recursive(group: str=None, indices: list=[], rec_depth: int=0):
    groups = [group]
    group = get_adgroup(group)
    parents = group.get_attribute(attribute="memberOf")
    if parents is not None or parents is not []:
        for parent in parents:
            temp = get_groups_recursive(parent, indices, rec_depth)
            for x in temp:
                groups.append(x)
    return groups


def create_tree(tree: Tree=Tree(), parent: Node=None, ad_object=None):
    if parent is None:
        name: str = "".join(ad_object.get_attribute("SamAccountName"))
        tree.create_node(data=name, identifier=name)
        parent = name
    memberOf: list = ad_object.get_attribute(attribute="memberOf")
    for membership in memberOf:
        group: pyad.adgroup.ADGroup = get_adgroup(membership)
        name: str = "".join(group.get_attribute("SamAccountName"))
        id: str = name
        i: int = 0
        while tree.get_node(id) is not None:
            id += f" ({i})"
            i += 1
        tree.create_node(data=name, identifier=id, parent=parent)
        if group.get_attribute("memberOf") is not []:
            tree = create_tree(tree=tree, parent=id, ad_object=group)
    return tree