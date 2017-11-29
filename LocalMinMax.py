""" Find local minimum or local maximum in O(1)

    Solution for:
    http://algorithms.tutorialhorizon.com/find-local-minimum-or-local-maximum-in-o1/

    Objective: Given an array such that every next element differs from the previous
    by +/- 1. (i.e. a[i+1] = a[i] +/-1 ) Find the local max OR min in O(1) time.
    The interviewer mentioned one more condition that the min or max should be
    non-edge elements of the array

"""

def find_max_min(arr):
    """Prints the local max or min for specific input conditions"""

    if not arr:  # Array is empty
        print("Empty array has no max/min")
        return 0
    first = arr[0]
    last = arr[-1]
    size = len(arr)
    if first + size - 1 == last or first - size + 1 == last:
        print("No local min or max")
        return 0

    if first < arr[1]:  # find local maximum
        last_should = first + (size - 1)
        print("Local max is:", (last + last_should)//2)
    else:  # find local minumum
        last_should = first - (size - 1)
        print("Local min is:", (last + last_should)//2)


def main():
    """ Test harness for find_min_max"""
    find_max_min([])
    find_max_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    find_max_min([12, 11, 10, 9, 8, 7, 6])

    find_max_min([3, 4, 5, 4, 3, 2, 1, 0, -1])
    find_max_min([-4, -5, -6, -5, -4, -3])


main()