"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
"""


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Edge case
    if not input_list:
        return -1

    # Recursive function to search the target number
    def search(arr, left, right, target):  # O(log n)
        if left > right:  # O(1)
            return -1  # O(1)

        # Find the mid point
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:  # O(1)
            return mid

        # Check if the left side is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target <= arr[mid]:  # O(1)
                return search(arr, left, mid - 1, target)  # O(log n)
            return search(arr, mid + 1, right, target)  # O(log n)

        # Check if the right side is sorted
        if arr[mid] <= target <= arr[right]:  # O(1)
            return search(arr, mid + 1, right, target)  # O(log n)
        return search(arr, left, mid - 1, target)  # O(log n)

    return search(input_list, 0, len(input_list) - 1, number)


pass


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# Test cases
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
