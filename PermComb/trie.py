"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

from collections import defaultdict


def node():
    return defaultdict(node)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._tree = node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self._tree
        for w in word:
            tree = tree[w]
        tree[None] = None


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self._tree
        for w in word:
            if w not in tree:
                return False
            tree = tree[w]

        return None in tree


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self._tree
        for w in prefix:
            if w not in tree:
                return False
            tree = tree[w]

        return True


if __name__ == '__main__':
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
