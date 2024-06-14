class Solution:
    def findExtra(self,n,a,b):
        #add code here
        b.append(0)
        for i,j in zip(a,b):
            if i==j:
                continue
            else:
                return a.index(i)