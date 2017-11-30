"""Implements Boyer-Moore majority algorithm

   Implementation for:
   https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
"""


def majority(arr):
    """Returns the majority element in the array (if any)
       ...or None if no majority element exists

       Note: writen so that array can be any valid list in Python
    """

    maj, count = None, 0

    for item in arr:
        if count == 0:
            maj = item
            count = 1
        elif item == maj:
            count += 1
        else:
            count -= 1

    # maj now contains our majority *candidate* -- verify if it is a majority
    if arr.count(maj) > (len(arr) // 2):
        return maj

    return None


def main():
    """Test harness for majority algorithm"""

    test_array = [1, 1, 1, 3, 3, 1, 4, 1, 3, 1]
    print("Majority of:\n", test_array, "\nis:", majority(test_array))

    test_array = []
    print("Majority of:\n", test_array, "\nis:", majority(test_array))

    test_array = ["blue", 9, "blue", "red", "blue", 10, "blue"]
    print("Majority of:\n", test_array, "\nis:", majority(test_array))

    test_array = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    print("Majority of:\n", test_array, "\nis:", majority(test_array))


main()
