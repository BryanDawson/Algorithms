"""Implements Print All Diagonals of a given matrix

   Implementation for: http://algorithms.tutorialhorizon.com/print-all-diagonals-of-a-given-matrix/

   NOTE: This implementation deviates from the reference by using zip() in comprehensions
            and storing the result in a temporary string

   NOTE: Added a second version that is closer to the reference implementation.  Hard to say
         which one is more pythonic...

"""


def printdiagonals(arr):
    """Prints all diagonals of the input array"""

    output = ""

    # First add the diagonals that correspond to each row
    for row in range(len(arr)):
        output += ' '.join([str(arr[drow][dcol]) for drow, dcol
                            in zip(range(row, -1, -1), range(row+1))])
        output += '\n'

    # Now add the remaining diagonals that correspond to the columns 1 through n
    for col in range(1, len(arr[0])):
        output += ' '.join([str(arr[drow][dcol]) for drow, dcol
                            in zip(range(len(arr)-1, -1, -1), range(col, len(arr[0])))])
        output += '\n'

    print(output)


def printdiagonals_ref(arr):
    """Prints all diagonals of the input array
       Note: this one is in the spirit of the reference implementation,
              which is more pythonic?
    """

    # Print first half
    row = 0
    while row < len(arr):
        col = 0
        rowtemp = row
        while rowtemp >= 0:
            print(arr[rowtemp][col], end=' ')
            rowtemp -= 1
            col += 1
        print()
        row += 1

    # Print second half
    col = 1
    while col < len(arr[0]):
        coltemp = col
        row = len(arr) - 1
        while coltemp < len(arr[0]):
            print(arr[row][coltemp], end=' ')
            row -= 1
            coltemp += 1
        print()
        col += 1


def main():
    """Test harness for print diagonals"""

    rows, cols = 4, 4
    printdiagonals([[cols*y+x+1 for x in range(cols)] for y in range(rows)])
    printdiagonals_ref([[cols*y+x+1 for x in range(cols)] for y in range(rows)])
    print()

    rows, cols = 1, 1
    printdiagonals([[cols*y+x+1 for x in range(cols)] for y in range(rows)])
    printdiagonals_ref([[cols*y+x+1 for x in range(cols)] for y in range(rows)])
    print()

    rows, cols = 4, 5
    printdiagonals([[cols*y+x+1 for x in range(cols)] for y in range(rows)])
    printdiagonals_ref([[cols*y+x+1 for x in range(cols)] for y in range(rows)])
    print()


main()
