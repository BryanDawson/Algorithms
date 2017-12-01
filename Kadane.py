"""Implements Kadane's algorithm for maximum subarray

   Implementation for:
   https://en.wikipedia.org/wiki/Maximum_subarray_problem  (Algorithm 3)

   Note: this implements the case where all items may be negative
"""


def max_subarray(arr):
    """Returns the sum of the subarray with the maximum sum"""

    max_so_far, max_ending_here = arr[0], arr[0]
    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def main():
    """Test harness for Kadane's algorithm"""

    test = [1, 2, -3, -4, 2, 7, -2, 3]
    print("Maximum sum subarray is: ", max_subarray(test))

    test = [-2, -3, -4, -2, -7, -2, -3, -11]
    print("Maximum sum subarray is: ", max_subarray(test))


main()
