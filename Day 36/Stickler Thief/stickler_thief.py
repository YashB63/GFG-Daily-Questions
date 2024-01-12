class Solution:  
    
    def FindMaxSum(self,a, n):
        
        if n == 0:
            return 0
        
        if n == 1:
            return a[0]
            
        prev = 0
        curr = 0
        
        for i in range(n):
            new = max(curr, prev + a[i])
            prev = curr
            curr = new
            
        return curr