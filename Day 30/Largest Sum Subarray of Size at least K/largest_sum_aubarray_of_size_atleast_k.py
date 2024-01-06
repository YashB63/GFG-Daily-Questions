class Solution():
    def maxSumWithK(self, a, n, k):
        
        s = res = sum(a[:k])
        l = 0
        j = 0
        
        for i in range(k, n):
            
            s += a[i]
            l += a[j]
            j += 1
            
            res = max(res, s)
            
            if l < 0:
                s -= l
                l = 0
                res = max(res, s)
            
            
        return res