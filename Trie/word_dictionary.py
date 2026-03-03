"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""
from typing import Optional

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie[''] = None

    def search(self, word: str) -> bool:
        matches = [self.trie]
        for c in word:
            if c == '.':
                matches = [d for match in matches if match is not None for k, d in match.items() if k != '']
            else:
                matches = [d for match in matches if match is not None for k, d in match.items() if k == c]

        return any('' in m for m in matches)



class WordDictionary:

    def __init__(self):

        # Initialize your data structure here.
        self.children = [None] * 26
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:

        # Adds a word into the data structure.
        curr = self
        for c in word:
            if curr.children[ord(c) - ord('a')] is None:
                curr.children[ord(c) - ord('a')] = WordDictionary()
            curr = curr.children[ord(c) - ord('a')]

        curr.isEndOfWord = True

    def search(self, word: str) -> bool:

        # Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch is not None and ch.search(word[i + 1:]):
                        return True
                return False

            if curr.children[ord(c) - ord('a')] is None:
                return False
            curr = curr.children[ord(c) - ord('a')]

        return curr is not None and curr.isEndOfWord



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        current_node = self.root
        for character in word:
            current_node = current_node.children.setdefault(character, TrieNode())
        current_node.is_word = True

    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.is_word

            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True

            if word[index] in node.children:
                return dfs(node.children[word[index]], index + 1)

            return False

        return dfs(self.root, 0)


wordDictionary = WordDictionary()
wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")
print(wordDictionary.search("a"))
print(wordDictionary.search(".at"))
wordDictionary.addWord("bat")
print(wordDictionary.search(".at"))
print(wordDictionary.search("an."))
print(wordDictionary.search("b."))
