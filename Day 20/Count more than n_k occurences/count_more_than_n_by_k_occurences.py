class Solution:
    
   
    def countOccurence(self,arr,n,k):
        
        x = {}
        for i in arr:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
            
        y = 0
        for i in x:
            if x[i] > n // k:
                y += 1
        return y
