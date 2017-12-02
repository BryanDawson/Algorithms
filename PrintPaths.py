"""Implements Print All Paths from Top left to bottom right in Two Dimensional Array

   Implementation for:
   http://algorithms.tutorialhorizon.com/print-all-paths-from-top-left-to-bottom-right-in-two-dimensional-array/

   NOTE: This implementation deviates from the reference by passing slices of the original
            array during recursion.  This is surely less efficient, but good practice for
            manipulating 2d array slices.

            Performance test with printing commented out shows acceptable interactive performance
            up to about 12x12 array -- 705474 paths

"""

prints = 0


def printall(arr, path):
    """Recursively builds and then prints all paths"""

    global prints
    if len(arr) == 1:   # We have hit the last row
        # Add the rest of the row to path and print result
        for i in arr[0]:
            path += str(i)+"-"
        print(path[:-1])  # Slice off the trailing dash, which is always present
        prints += 1
        return
    if len(arr[0]) == 1:  # We have hit the last column
        # Add the rest of the column to path and print result
        for row in arr:
            path += str(row[0])+"-"
        print(path[:-1])   # Slice off the trailing dash, which is always present
        prints += 1
        return
    path += str(arr[0][0])+"-"
    # Call recursively printAll(currentRow+1, currentcolumn,path)
    printall([arr[1:][i] for i in range(len(arr[1:]))], path)
    # Call recursively printAll(currentRow, currentcolumn+1,path)
    printall([arr[i][1:] for i in range(len(arr))], path)


def main():
    """Test harness for print all paths"""

    rows, cols = 3, 3
    printall([[cols*y+x+1 for x in range(cols)] for y in range(rows)], "")
    print()

    rows, cols = 1, 1
    printall([[cols*y+x+1 for x in range(cols)] for y in range(rows)], "")
    print()

    rows, cols = 4, 5
    printall([[cols*y+x+1 for x in range(cols)] for y in range(rows)], "")
    print()

    # As expected, larger arrays generate **many** paths.
    # This 10x20 works but generates 168002 paths
    # rows, cols = 12, 12
    # printall([[cols*y+x+1 for x in range(cols)] for y in range(rows)], "")
    # print()

    print("Number of lines printed: ", prints)


main()
