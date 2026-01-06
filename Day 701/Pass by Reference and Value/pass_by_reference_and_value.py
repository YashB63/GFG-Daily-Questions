class Solution:
    def passedBy(self, a, b):
        L=[]
        L.append(a)
        L.append(b)
        
        a = a+1
        L[1]=L[1]+2
        
        return a,L[1]