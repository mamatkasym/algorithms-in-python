
def make_trie(*words):
    _end = '_end_'
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})

        current_dict[_end] = _end

    return root

print(make_trie('foo', 'bar', 'baz', 'barz'))