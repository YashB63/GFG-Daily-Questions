class Solution:
    def getNode(self):
        return TrieNode()
    
    def _charToIndex(self,ch):
    
        return ord(ch)-ord('a')
    
    def insert(self,root, key):
    
        pCrawl = root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
    
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
    
        pCrawl.isEndOfWord = True
    
    def search(self,root, key):
    
        pCrawl = root
        length = len(key)
        for level in range(length-1):
            index =self. _charToIndex(key[level])
            if not pCrawl.children[index]:
                return level
            pCrawl = pCrawl.children[index]
    
        if(pCrawl.isEndOfWord==False):
            return length-1
        return -1
    
    def check(self,lst, n):
        mp = {}
        root = self.getNode()
        for i in range(n):
            
            k = self.search(root, lst[i])
            s = lst[i]
            
            if (k==-1):
                if s not in mp:
                    mp[s]=1
                else:
                    mp[s]+=1
                print(s, end=" ")
                if(mp[s]>1):
                    print(mp[s])
                else:
                    print()
            else:
                
                for j in range(k+1):
                    print(s[j], end="")
                    
                self.insert(root, s)
                if s not in mp:
                    mp[s]=1
                else:
                    mp[s]+=1
                if(mp[s]>1):
                    print(mp[s])
                else:
                    print()