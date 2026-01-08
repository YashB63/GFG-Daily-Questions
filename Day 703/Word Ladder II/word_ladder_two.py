import collections

class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        tree = collections.defaultdict(set)
        words = set(wordList)
        n = len(beginWord)

        if endWord not in wordList:
            return []
        
        found = False
        q = {beginWord}  
        nq = set() 
        
        while q and not found:
            words -= set(q)

            for x in q:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y == endWord: 
                            found = True
                        else: 
                            nq.add(y)
                        tree[x].add(y)
            q, nq = nq, set()
        
        return self.solve(beginWord, endWord, tree)
    
    def solve(self, x, endWord, tree):
        if x == endWord:
            return [[x]]
        
        return [[x] + rest for y in tree[x] for rest in self.solve(y, endWord, tree)]