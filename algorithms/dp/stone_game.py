"""
Two players A and B are playing a stone game. There are even numbers of piles each pile containing some stones and
the total stones in all the piles is odd. A and B are supposed to pick a pile either from the starting or end of the
row one by one until no more piles are left. Player A will always start the game by picking a pile first. The player
with more stones at the end wins the game. Return true if and only if player A wins the game else return false.
"""


def stone_game(piles: list[int]) -> bool:
    n = len(piles)
    # dp[i][j] - highest score that player A and player B can get, respectively.
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = [piles[i], 0]
            else:
                left = piles[i] + dp[i + 1][j][1]
                right = piles[j] + dp[i][j - 1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]

    print('Highest scores player A and player can get:', dp[0][n - 1][0], dp[0][n - 1][1])
    return dp[0][n - 1][0] > dp[0][n - 1][1]


def test_stone_game():
    piles = [5, 3, 4, 5]
    assert stone_game(piles) is True
    piles = [3, 7, 2, 3]
    assert stone_game(piles) is True
