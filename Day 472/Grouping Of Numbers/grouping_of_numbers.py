class Solution:
    def maxGroupSize(self, arr, N, K):
        rem = [0] * K
        
        for num in arr:
            rem[num % K] += 1
            
        res = 0
            
        l, r = 1, K - 1
        
        while l < r:
            res += max(rem[l], rem[r])
            l += 1
            r -= 1
            
        if l == r and rem[l] > 0: 
            res += 1                           
            
        if rem[0] > 0:            
            res += 1            
        
        return res