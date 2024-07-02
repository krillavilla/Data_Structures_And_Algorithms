
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # sort the input list
    input_list = merge_sort(input_list)

    # initialize two numbers
    num1 = 0
    num2 = 0

    # assign the digits to the two numbers alternatively
    for i in range(len(input_list)):
        if i % 2 == 0:
            num1 = num1 * 10 + input_list[i]
        else:
            num2 = num2 * 10 + input_list[i]

    return [num1, num2]

    pass

# Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # split the array into two halves
    mid = len(arr) // 2
    left = arr[:mid] # left half
    right = arr[mid:] # right half

    # recursively call merge_sort on the two halves
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

    pass

# Merge function
def merge(left, right):
    result = [] # merged array
    left_index = 0 # left array index
    right_index = 0 # right array index

    # merge the two arrays
    while left_index < len(left) and right_index < len(right):
        # compare the two elements
        if left[left_index] > right[right_index]:
            # append the larger element to the result
            result.append(right[right_index])
            # increment the right index
            right_index += 1
        else:
            # append the larger element to the result
            result.append(left[left_index])
            # increment the left index
            left_index += 1

    # append the remaining elements
    result += left[left_index:]
    result += right[right_index:]

    return result


    pass

# Test cases
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]