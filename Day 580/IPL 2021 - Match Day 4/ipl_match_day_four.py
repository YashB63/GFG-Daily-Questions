class Solution:
    def checkBit(self, pattern, arr,n):
        count=0
        
        for i in range(0,n):
            if((pattern&arr[i])==pattern):
                count+=1
                
        return count
    
    def maxAND(self, arr,n):
        res=0
        
        for bit in range(16,-1,-1):
            count=self.checkBit(res|(1<<bit),arr,n)
            
            if count>=2:
                res|=(1<<bit)
                
        return res