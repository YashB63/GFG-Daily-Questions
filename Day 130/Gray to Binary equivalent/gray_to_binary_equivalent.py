class Solution:    
    
    def grayToBinary(self,n):
        
        if n == 0:
            return 0
            
        if n == 1:
            return 1
        
        x = bin(n)[2:]

        ans = x[0]
        
        for i in range(1, len(x)):
            ans += str(int(ans[-1]) ^ int(x[i]))
        

        return int(ans, 2)