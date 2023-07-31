"""
The Knuth-Morris-Pratt (KMP) algorithm is an algorithm that is used to search for a substring (W),
in a given string (S), in O(m+n) time (where mand n are the lengths of W and S).

You are given a string S with length N. LPS array of prefix function for string S is defined by P of length N,
where P[i] is the length of the longest proper prefix of the substring s[0...i] which is also suffix of this substring.
 A proper prefix of a string is a prefix that is not equal to the string itself. By definition, P[0] = 0.
 P[i] = max{k: s[0...k-1] = s[i-(k-1)...i]} for k in [1,...,i]
"""


def KMPStringSearch(pat: str, st: str):
    M = len(pat)
    N = len(st)

    lps = [0] * M
    j = 0

    computeLPSArray(pat, M, lps)

    i = 0
    while i < N:
        if pat[j] == st[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]

        elif i < N and pat[j] != st[i]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    length, i = 0, 1

    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
