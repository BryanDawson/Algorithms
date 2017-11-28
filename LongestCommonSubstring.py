""" Implements solution(s) for the Longest Common Substring problem.

    In this case, the "strings" are themselves strings, so in a sense,
    the 'alphabet' is 'words'.  See the test cases in main() for examples

"""


def lcs_dynamic(s1, s2):
    """ Returns the longest common substring using dynamic programming"""

    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]


def main():
    """ Run the test harness for implementations of Longest Common Substring"""

    string1 = "The next virtue is: Freedom is better than slavery.".split()
    string2 = "Poverty in freedom is better than riches in chains".split()

    print(lcs_dynamic(string1, string2))


main()
