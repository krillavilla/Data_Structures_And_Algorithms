# Explanation for Rearrange Digits Code

The code provided is a solution to the problem of rearranging digits in an array to form two numbers such that their sum is maximum. The solution is implemented in Python and uses the Merge Sort algorithm for sorting the input list.

## Decision Making in the Code

The decision to use the Merge Sort algorithm was made due to its efficiency in sorting numbers. Merge Sort is a divide-and-conquer algorithm that splits the input array into two halves, sorts them separately, and then merges them. This makes it an efficient sorting algorithm with a time complexity of O(n log n).

The decision to use a list as the data structure to hold the input numbers was made due to the flexibility and ease of use offered by lists in Python. Lists in Python are dynamic and can hold different types of data. They also provide various built-in methods for manipulating data, which makes them a good choice for this problem.

## Efficiency of the Solution

The time complexity of the solution is primarily determined by the Merge Sort algorithm, which has a time complexity of O(n log n). This is because the Merge Sort algorithm splits the array into two halves and sorts them separately, which requires log n splits, and for each split, n operations are performed to merge the arrays.

The space complexity of the solution is O(n), which is required for the temporary arrays used during the merge process in the Merge Sort algorithm.

In the `rearrange_digits` function, the sorted array is iterated over once, which adds an additional O(n) time complexity. However, this does not change the overall time complexity, which remains O(n log n).

The space complexity of the `rearrange_digits` function is O(1), as it only uses a constant amount of space to store the two numbers formed from the digits in the array.