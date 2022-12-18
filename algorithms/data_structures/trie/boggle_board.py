"""
Sources:
    https://www.techiedelight.com/generate-list-of-possible-words-from-a-character-matrix/

"""


class Trie:
    """A class to store a Trie node"""

    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word):
        root = self
        for c in word:
            c = root.children.setdefault(c, Trie())
        root.is_word = True


def adj(x: int, y: int, m: int, n: int):
    """generator that yields adjacent cells"""
    for i, j in [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]:
        if 0 <= x + i < m and 0 <= y + j < n:
            yield x + i, y + j


def search(trie: Trie, board, i, j, path, result):
    """DFS search with prefix `path`, last cell (i,j) on board `board`"""
    if not trie:
        return
    if trie.is_word:
        result.add(path)
    # temporarily change board value at (i, j) in order ot not to visit again
    ch, board[i][j] = board[i][j], "#"
    for key, node in trie.children.items():
        for x, y in adj(i, j, len(board), len(board[0])):
            if board[x][y] == key:
                search(node, board, x, y, path + key, result)
    board[i][j] = ch


def search_in_boggle(board: list[list[str]], words: list[str]) -> set[str]:
    result = set()
    trie = Trie()
    for word in words:
        trie.insert(word)
    m, n = len(board), len(board[0])

    for i in range(m):
        for j in range(n):
            ch = board[i][j]
            if ch in trie.children:
                search(trie.children[ch], board, i, j, ch, result)
    return result
