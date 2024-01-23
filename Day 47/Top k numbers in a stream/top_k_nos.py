from collections import defaultdict

class Solution:
    def kTop(self,a, N, K):
        
        res = []
        count = defaultdict(int)
        ls = []
        for i, j in enumerate(a):
            count[j] += 1
            if count[j] == 1:
                ls.append(j)
            ls.sort(key = lambda x:(-count[x],x))
            res.append(ls[:min(K, i+1)])
        return res