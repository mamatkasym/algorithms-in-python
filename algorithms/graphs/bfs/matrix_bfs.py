# def matrix_bfs(matrix: List[List], n: int, m: int, x: int, y: int):
#     marked = [[False for _ in range(m)] for _ in range(n)]
#     q = [(x, y)]
#     while q:
#         x, y = q.pop()
#         marked[x][y] = True
#         if x > 0:
#             if not marked[x-1][y]:
#                 q.append((x-1, y))
#
#         if x < n-1:
#             if not marked[x+1][y]:
#                 q.append((x+1, y))
#
#         if y > 0:
#             if not marked[x][y-1]:
#                 q.append((x, y-1))
#
#         if y > m-1:
#             if not marked[x][y+1]:
#                 q.append((x, y+1))
