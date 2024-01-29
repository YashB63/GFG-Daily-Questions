class Solution:
    def getTwinCount(self, N , Arr):
         
        x = {}
        
        for i in Arr:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
        
        res = 0
        
        for i,j in x.items():
            res += (j//2)*2
        return res