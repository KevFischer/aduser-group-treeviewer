from pyad import *


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