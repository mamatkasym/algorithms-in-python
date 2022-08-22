"""
Given two sequences A, B, count number of unique ways in sequence A, to form a subsequence that is identical
to the sequence B.
Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, “ACE” is a subsequence of “ABCDE” while “AEC” is not).

https://leetcode.com/problems/distinct-subsequences/
"""


def distinct_subsequences(A: str, B: str) -> int:
    n = len(A)
    m = len(B)
    # dp[i][j] is the answer for the sub problem A[0...i] and B[0...j]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(min(i+1, m)):
            if i == j == 0:
                dp[i][j] = int(A[i] == B[j])
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + int(A[i] == B[j])
            else:
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[n-1][m-1]
