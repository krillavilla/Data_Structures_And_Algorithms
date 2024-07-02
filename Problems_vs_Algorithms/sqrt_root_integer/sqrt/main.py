"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Base case
    if number == 0 or number == 1: # 0 and 1 are their own square root
        return number # Returns the

    # Binary search
    start = 1
    end = number

    while start <= end: # Binary search
        mid = (start + end) // 2 # Find the middle
        if mid * mid == number: # If the square of the middle is equal
            return mid # Return the middle
        elif mid * mid < number: # If the square of the middle is less than the number
            start = mid + 1 # Move the start to the middle + 1
            result = mid # Store the middle
        else:
            end = mid - 1 # Move the end to the middle - 1
    return result


    pass

# Test cases
print ("Pass" if  (3 == sqrt(9)) else "Fail") # 3
print ("Pass" if  (0 == sqrt(0)) else "Fail") # 0
print ("Pass" if  (4 == sqrt(16)) else "Fail") # 4
print ("Pass" if  (1 == sqrt(1)) else "Fail") # 1
print ("Pass" if  (5 == sqrt(27)) else "Fail") # 5