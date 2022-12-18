import random
import itertools
import math


def kth_lexicographically_smallest_string(s: chr, t: chr, A: int, B: int, k: int) -> str:
    """
    return k th lexicographically smallest string  consisting of A number os s characters and B number of t characters
    where s < t and 1 <= k <= C(A+B, A).
    """

    def kth_string(A, B, k, dp):
        if A == 0:
            return t * B
        if B == 0:
            return s * A

        if k <= dp[A - 1][B]:
            return s + kth_string(A-1, B, k, dp)
        else:
            return t + kth_string(A, B-1, k - dp[A-1][B], dp)

    # dp[i][j] is number os binary string with i number of s and j number t characters
    dp = [[0] * (B + 1) for _ in range(A + 1)]
    dp[0][0] = 1
    for i in range(A + 1):
        for j in range(B + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

    return kth_string(A, B, k, dp)


def test_kth_lexicographically_smallest_string():
    A = random.randint(1, 5)
    B = random.randint(1, 5)
    k = random.randint(1, math.comb(A+B, A))
    s = 'A'*A + 'B'*B
    p = list(set(itertools.permutations(s)))
    p.sort()
    assert "".join(p[k-1]) == kth_lexicographically_smallest_string('A', 'B', A, B, k)
