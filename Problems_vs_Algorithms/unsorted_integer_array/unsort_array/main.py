"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?

"""
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # If the list is empty, return None
    if not ints:
        return None

    # Initialize min_val and max_val with the first element of the list
    min_val = max_val = ints[0]

    # Traverse through the list
    for num in ints:
        # If the current number is less than min_val, update min_val
        if num < min_val:
            min_val = num
        # If the current number is greater than max_val, update max_val
        elif num > max_val:
            max_val = num

    # Return the minimum and maximum values as a tuple
    return min_val, max_val

### Example Test Case of Ten Integers
import random

# Create a list of integers from 0 to 9
l = [i for i in range(0, 10)]
# Shuffle the list to make it unsorted
random.shuffle(l)

# Test the function with the shuffled list
# If the function returns (0, 9), print "Pass", otherwise print "Fail"
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")