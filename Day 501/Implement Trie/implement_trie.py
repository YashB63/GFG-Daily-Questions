class TrieNode:
    def __init__(self):
        self.c={}
        self.ew=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str):
        node=self.root
        for ch in word:
            if ch not in node.c:
                node.c[ch]=TrieNode()
            node=node.c[ch]
        node.ew=True

    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            if ch not in node.c:
                return False
            node=node.c[ch]
        return node.ew

    def isPrefix(self, word: str) -> bool:
        node=self.root
        for ch in word:
            if ch not in node.c:
                return False
            node=node.c[ch]
        return True