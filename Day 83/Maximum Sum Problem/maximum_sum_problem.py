class Solution:
    def maxSum(self, n): 
        
        a = n//2
        b = n//3
        c = n//4
        
        if (a+b+c) > n:
            return self.maxSum(a) + self.maxSum(b) + self.maxSum(c)
        else:
            return n