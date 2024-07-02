
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    # Count the number of 0s, 1s and 2s
    count_0 = 0
    count_1 = 0
    count_2 = 0

    # Count the number of 0s, 1s and 2s
    for i in input_list:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        else:
            count_2 += 1

    # Create a new list with the sorted elements
    sorted_list = [0] * count_0 + [1] * count_1 + [2] * count_2

    # Return the sorted list
    return sorted_list

    pass


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
