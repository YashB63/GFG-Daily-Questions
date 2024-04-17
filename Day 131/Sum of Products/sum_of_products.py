class Solution:
    def pairAndSum(self, n, arr):
        
        ans = 0
      
        for i in range(32):
            c = 0
            
            for j in arr:
                if (j>>i)&1:
                    c += 1
                  
            if c > 1:
                ans += (2**i)*((c-1) * c)//2
        
        return ans