""" Implements solution(s) for the Longest Common Substring problem.

    In this case, the "strings" are themselves strings, so in a sense,
    the 'alphabet' is 'words'.  See the test cases in main() for examples

"""


def lcs_dynamic(str1, str2):
    """ Returns the longest common substring using dynamic programming"""

    mat = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
    longest, x_longest = 0, 0
    for x in range(1, len(str1) + 1):
        for y in range(1, 1 + len(str2)):
            if str1[x - 1] == str2[y - 1]:
                mat[x][y] = mat[x - 1][y - 1] + 1
                if mat[x][y] > longest:
                    longest = mat[x][y]
                    x_longest = x
            else:
                mat[x][y] = 0
    return str1[x_longest - longest: x_longest]


def main():
    """ Run the test harness for implementations of Longest Common Substring"""

    string1 = "The next virtue is: Freedom is better than slavery.".split()
    string2 = "Poverty in freedom is better than riches in chains".split()

    print(lcs_dynamic(string1, string2))


main()
