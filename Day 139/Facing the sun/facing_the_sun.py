class Solution:
    
    def countBuildings(self,h, n):
        
        c=1
        m=h[0]
        for i in range(1,n):
            if h[i]>m:
                c+=1
                m=h[i]
        return c