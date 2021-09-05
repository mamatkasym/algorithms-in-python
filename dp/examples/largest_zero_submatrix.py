"""
You are given a matrix with n rows and m columns.
Find the largest submatrix consisting of only zeros (a submatrix is a rectangular area of the matrix).
"""

from typing import List


def solve(matrix: List[List]) -> int:
    """
    :param matrix: two dimensional binary array
    :return: area of the largest 0 submatrix
    """
    n = len(matrix)
    m = len(matrix[0])

    # d[i][j] if the largest row number ( from 0 to i-1 ), in which there is an element equal to 1 in the j's column
    d = [-1] * m
    left = [0] * m
    right = [0] * m
    stack = []
    ans = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                d[j] = i

        for j in range(m):
            while stack and d[stack[-1]] <= d[j]:
                stack.pop()

            left[j] = stack[-1] if stack else -1
            stack.append(j)

        while stack:
            stack.pop()

        for j in range(m - 1, -1, -1):
            while stack and d[stack[-1]] <= d[j]:
                stack.pop()

            right[j] = stack[-1] if stack else m
            stack.append(j)

        while stack:
            stack.pop()

        for j in range(m):
            ans = max(ans, (i - d[j]) * (right[j] - left[j] - 1))
    return ans


if __name__ == '__main__':
    res = solve([
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ])
    print(res)
