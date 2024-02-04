class Solution:
    #Function to insert string into TRIE.
    def insert(self, root, key):
        
        for char in key:
            nextNode = root.children[ord(char) - 97]
            if not nextNode:
                newNode = TrieNode()
                root.children[ord(char) - 97] = newNode
                root = newNode
            else:
                root = nextNode
        root.isEndOfWord = True
        
    
    #Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        
        for char in key:
            nextNode = root.children[ord(char) - 97]
            if not nextNode:
                return False
            else:
                root = nextNode
                
        return root.isEndOfWord is True