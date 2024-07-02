# Explanation for Rotated Array Search

The provided code implements a search function for a rotated sorted array. The main function `rotated_array_search` takes an array and a target number as input, and returns the index of the target number if it is found in the array, or -1 if it is not found.

## Decision Making

The decision to use a binary search algorithm was made because of its efficiency in searching sorted arrays. Binary search has a time complexity of O(log n), which is much faster than a linear search's time complexity of O(n). This makes binary search a better choice for large arrays.

The array is assumed to be a rotated version of a sorted array. This means that there is a pivot point in the array where the elements switch from being in ascending order to starting from a smaller number again. The binary search algorithm is modified to handle this rotation.

## Efficiency

The time complexity of the solution is O(log n) because each recursive call to the `search` function reduces the size of the search space by half. This is the key characteristic of binary search and why it was chosen for this problem.

The space complexity of the solution is O(log n) because in the worst case scenario, the maximum height of the recursive call stack will be log(n). Each recursive call to the `search` function adds a new level to the stack.

The `linear_search` function is provided as a way to validate the results of the `rotated_array_search` function. It has a time complexity of O(n) because it iterates through each element in the array once. Its space complexity is O(1) because it does not use any additional space that scales with the input size.

The `test_function` is used to compare the results of the `rotated_array_search` and `linear_search` functions. If the results match, it prints "Pass", otherwise it prints "Fail". This is a simple way to validate that the `rotated_array_search` function is working correctly.