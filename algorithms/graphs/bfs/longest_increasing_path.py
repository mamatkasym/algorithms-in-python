"""
Source: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Time complexity: O(n*m)
    If we do DFS from each cell, then we would be calculating results for a particular path multiple times, that is,
    we would have overlapping subproblems. This would increase our time complexity. We can optimize it further using
    memoization.
Memory complexity: O(m*n)
"""
from collections import deque


def longest_increasing_path(self, matrix: list[list[int]]) -> int:
    def is_in_matrix(x, y):
        """Check if cell (x, y) is inside the matrix"""
        return 0 <= x < m and 0 <= y < n

    def dfs(a, b):
        for dx, dy in delta:
            x, y = a + dx, b + dy
            if is_in_matrix(x, y) and matrix[x][y] > matrix[a][b] and dp[x][y] < dp[a][b] + 1:
                dp[x][y] = dp[a][b] + 1
                dfs(x, y)

    def bfs(a, b):
        q = deque([(a, b)])
        while q:
            f, s = q.popleft()
            for dx, dy in delta:
                x, y = f + dx, s + dy
                if is_in_matrix(x, y) and matrix[x][y] > matrix[f][s] and dp[x][y] < dp[f][s] + 1:
                    dp[x][y] = dp[f][s] + 1
                    q.append((x, y))

    m = len(matrix)
    n = len(matrix[0])
    # Solution matrix, dp[i][j] - longest increasing path ending at (i, j)
    dp = [[1] * n for _ in range(m)]
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for i in range(m):
        for j in range(n):
            # assume the desired path starts at (i, j). Can be also used dfs
            bfs(i, j)

    return max([max(row) for row in dp])
