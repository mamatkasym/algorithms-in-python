
def edit_distance(s: str, t: str) -> int:
    """
        Minimum number of steps transform s to t:
        Allowed operations:
            1. insert a character
            2. remove a character
            3. modify a character
        :param s: initial string
        :param t: target string
        :return: result
        """
    n = len(s)
    m = len(t)
    # dis[i][j] - minimum number of steps transform s[0...i] into t[0...j]
    dis = [[n + m] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dis[i][j] = max(i, j)
            else:
                cost = s[i] != t[j]
                dis[i][j] = min(
                    dis[i][j - 1] + 1,  # insert a character at the end of s
                    dis[i - 1][j] + 1,  # remove the last character from s
                    dis[i - 1][j - 1] + cost  # match of modify the last character of s
                )
    return dis[n][m]


def test_edit_distance():
    s = 'LOVE'
    t = 'MOVIE'
    print(edit_distance(s, t))
    assert edit_distance(s, t) == 2
