class Solution:
    def findExtra(self,a,b,n):
        
        extraNumber = sum(a) - sum(b) # 9
        index = n//2 
        lo = 0 
        hi = len(a)-1 
        
        
        for i in range(n): 
            if a[index] == extraNumber: 
                return index 
            elif a[index] < extraNumber:
                lo = index + 1 
                index = (lo + hi) // 2 
            elif a[index] > extraNumber:
                hi = index - 1 
                index = (lo + hi) // 2 
            else:
                return -1