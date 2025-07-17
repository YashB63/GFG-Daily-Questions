class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isEnd = True

    def allPrefixesExist(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            node = node.children[idx]

            if not node or not node.isEnd:
                return False
        return True


class Solution():
    def longestString(self, words):
        trie = Trie()

        for word in words:
            trie.insert(word)

        result = ""

        for word in words:

            if trie.allPrefixesExist(word):

                if len(word) > len(result) or (len(word) == len(result)
                                               and word < result):
                    result = word

        return result