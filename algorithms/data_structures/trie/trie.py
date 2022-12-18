class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

    def add(self, word: str) -> None:
        root = self
        for char in word:
            if char not in root.children:
                root = root.children.setdefault(char, Trie())
        root.word = word

    def search(self, word: str) -> bool:
        root = self
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.word is not None

    def remove(self, word):
        raise NotImplementedError


def test():
    trie = Trie()
    trie.add("banana")
    trie.add("baby")
    trie.add("babble")
    trie.add("basket")
    assert trie.search("babel") is False
    assert trie.search("baby") is True
    assert trie.search("bab") is False
