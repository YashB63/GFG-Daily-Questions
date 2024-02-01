class Solution:
    def nthFaithfulNum(self, N):
         
        total, i = 0, 0
        
        while N:
            if (N&1):
                total += 7**i
                
            N = N>>1
            i += 1
            
        return total