"""
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy as such. Where User is represented by str representing their ids.
"""


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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

'''
Write a function that provides an efficient look up of whether the user is in a group.
'''


def is_user_in_group(user, group):
    """
        Return True if user is in the group, False otherwise.

        Args:
          user(str): user name/id
          group(class:Group): group to check user membership against
        """
    ## Check if the user is in the group
    if user in group.get_users():
        return True
    ## Check if the user is in the subgroups
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True
    return False

    return None


## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Normal case where user is in the group
print(is_user_in_group("sub_child_user", parent))  # Expected output: True

# Test Case 2: Edge case where user is not in the group
print(is_user_in_group("non_existent_user", parent))  # Expected output: False

# Test Case 3: Edge case where user is None
print(is_user_in_group(None, parent))  # Expected output: False

# Test Case 4: Edge case where group is None
try:
    print(is_user_in_group("sub_child_user", None))  # Expected output: Error
except AttributeError:
    print("Error: Group is None")

# Test Case 5: Edge case where user and group are None
try:
    print(is_user_in_group(None, None))  # Expected output: Error
except AttributeError:
    print("Error: User and Group are None")
