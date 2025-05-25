class TrieNode:   
    def __init__(self): 
        self.children = [None]*26
  
        self.isEndOfWord = False
        
        self.d=[]
  
class Trie: 
    
    global d
    d=dict()

    def __init__(self): 
        self.root =TrieNode()
        
def cti(ch):
    return ord(ch)-ord('A')

def insert(root,key):
    
    for e in key:
        idx=cti(e)
        
        if idx>26:
            continue
        
        if not root.children[idx]:
            root.children[idx]=TrieNode()
        
        root=root.children[idx]
    
    root.d.append(key)
    
    root.isEndOfWord=True

def pall(root):
    
    if not root:
        return
    
    if root.isEndOfWord:
        for e in sorted(root.d):
            print(e,end=' ')
        
    for i in range(26):
        pall(root.children[i])
        
        
def search(root, key):
    
    for e in key:
        idx=cti(e)
        
        if not root.children[idx]:
            print('No match found',end=' ')
            return
        
        root=root.children[idx]
    pall(root)
    

class Solution:
    
    def findAllWords(self,dict,strs):
        t=Trie()
         
        for s in dict:
            insert(t.root,s)
        
        search(t.root,strs)