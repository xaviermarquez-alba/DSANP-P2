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
    if user is None or user == '':
        print('Invalid User!')
        return

    if group is None or not isinstance(group, Group):
        print('Invalid Group!')
        return
    
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
sub_child_user = "sub_child_user" # USER 1
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)

child2 = Group("child2")
sub_child2 = Group("subchild2")
sub_child_user2 = "sub_child_user2" # USER 2
sub_child2.add_user(sub_child_user2)
child2.add_group(sub_child2)


# Test 1
if is_user_in_group(sub_child_user, parent):
    print('Test Pass')
else:
    print('Test Fail')

# Test 2
if not is_user_in_group(sub_child_user2, parent):
    print('Test Pass')
else:
    print('Test Fail')

# Test 3
if is_user_in_group(sub_child_user2, child2):
    print('Test Pass')
else:
    print('Test Fail')

# Test 4
is_user_in_group(None, parent) # expected output: "Invalid User!"

# Test 5
is_user_in_group(sub_child_user, None) # expected output: "Invalid Group!"
is_user_in_group(sub_child_user, 'Not a group') # expected output: "Invalid Group!"
