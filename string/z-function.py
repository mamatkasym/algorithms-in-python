"""
Suppose we are given a string `s` of length `n`. The `Z-function` for this string is an array of length `n` where the
`i`-th element is equal to the greatest number of characters starting from the position `i`
that coincide with the first characters of `s`.

In other words, `z[i]` is the length of the longest string that is, at the same time, a prefix of `s` and a prefix
of the suffix of `s` starting at `i`.
"""


def z_function_trivial(s: str) -> list[int]:
    """ TC: O(n^2) """
    n = len(s)

    # z[i]  is the length of the longest string that is, at the same time, a prefix of  and a prefix of the suffix of
    # starting at i
    z = [0] * n
    for i in range(1, n):
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

    return z


def z_function_efficient(s: str) -> list[int]:
    """ TC: O(n^2) """
    n = len(s)
    z = [0] * n
    ri = le = 0
    i = 1
    while i < n:
        if i <= ri:
            z[i] = min(ri - i + 1, z[i - le])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > ri:
            ri = i + z[i] - 1
            le = i

        i += 1
    return z
