from collections import defaultdict
from itertools import product

class Solution:
    def findOrder(words):
        g = defaultdict(set)
        n = len(words)
        chars = set(words[-1])
        for i in range(n-1):
            chars.update(words[i])
            for j in range(i+1, n):
                w1, w2 = words[i], words[j]
                for k in range(min(len(w1), len(w2))):
                    if w1[k] != w2[k]:
                        g[w1[k]].add(w2[k])
                        break
                else:
                    if len(w1) > len(w2):
                        return ""
                
        
        visited, on_stack = set(), set()
        result = []
        
        def dfs(n):
            if n in on_stack:
                return True 
            if n in visited:
                return False
            
            on_stack.add(n)
            for nbr in g.get(n, []):
                if dfs(nbr):
                    return True
            on_stack.remove(n)
            visited.add(n)
            result.append(n)
            
        for n in g.keys():
            if n not in visited:
                if dfs(n):
                    return ""
 
        result.extend(chars - set(result))
        return "".join(reversed(result))