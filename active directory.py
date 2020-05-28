class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    find_user = False
    users = group.get_users()
    if user in users:
        return True
    
    groups = group.get_groups()
    for group in groups:
        find_user = find_user or is_user_in_group(user, group)

    return find_user


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
no_child = Group("no_child")

sub_child_user = "sub_child_user"
no_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_group(no_child)

print(is_user_in_group("sub_child_user", parent))