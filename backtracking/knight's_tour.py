"""
Time complexity: O(8 ^ (N ^ 2))
"""
from typing import List


def is_safe_move(x: int, y: int, N: int, ans: List):
    return N > x >= 0 and N > y >= 0 and ans[x][y] == -1


def solve(N: int, x: int, y: int, moves: int, ans: List, dx: List, dy: List):
    if moves == N * N:
        return True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if is_safe_move(nx, ny, N, ans):
            ans[nx][ny] = moves
            if solve(N, nx, ny, moves + 1, ans, dx, dy):
                return True
            ans[nx][ny] = -1

    return False


def knight_tour(n: int):
    ans = [[-1 for _ in range(n)] for _ in range(n)]
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    # since knight is at (0,0) in the beginning
    ans[0][0] = 0
    if solve(n, 0, 0, 1, ans, dx, dy):
        for row in ans:
            print(" ".join(str(x) for x in row))

    else:
        print("Solution does not exist")


def main():
    N = int(input())
    knight_tour(N)


if __name__ == "__main__":
    main()
