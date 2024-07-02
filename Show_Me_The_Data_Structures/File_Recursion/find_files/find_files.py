"""
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().
"""

### Locally save and call this file ex.py ##

## Code to demonstrate the use of some of the OS modules in python

import os

## Let us print the files in the directory in which you are running this script
print(os.listdir("."))

## Let us check if this file is indeed a file!
print(os.path.isfile("./ex.py"))

## Does the file end with .py?
print("./ex.py".endswith(".py"))


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    ## Check if the path is a file
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []
    ## Check if the path is a directory
    elif os.path.isdir(path):
        ## Create a list to store the results
        result = []
        ## Iterate over the items in the directory
        for item in os.listdir(path):
            ## Recursively call the function on the item
            result += find_files(suffix, os.path.join(path, item))
        return result
    ## If the path is neither a file nor a directory, return None
    else:
        return None

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
print("Test Case 1: Known file suffix '.py'")
files = find_files('.py', '.')
print(files)
assert isinstance(files, list), "The result should be a list"
assert len(files) > 0, "The list should not be empty"

## Test Case 2
print("Test Case 2: Non-existent file suffix '.xyz'")
files = find_files('.xyz', '.')
print(files)
assert isinstance(files, list), "The result should be a list"
assert len(files) == 0, "The list should be empty for non-existent suffix"

## Test Case 3
print("Test Case 3: Empty file suffix ''")
files = find_files('', '.')
print(files)
assert isinstance(files, list), "The result should be a list"
assert len(files) > 0, "The list should not be empty for empty suffix"