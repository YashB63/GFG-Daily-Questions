from collections import defaultdict

class Solution:
    def countDistinct(self, A, N, K):
        m = defaultdict(lambda:0)
        
        dist_count = 0
        for i in range(K):
            if m[arr[i]] == 0:
                dist_count += 1
                
            m[arr[i]] += 1
            
        res = [dist_count]
        
        for i in range(K,N):
            if m[arr[i-K]] == 1:
                dist_count -= 1
                
            m[arr[i-K]] -= 1
            
            if m[arr[i]] == 0:
                dist_count += 1
            m[arr[i]] += 1
            
            res.append(dist_count)
            
        return res