class Solution:
    #Function to merge the arrays.
    def merge(self,a,b,x,y):
        b.extend(a)
        b.sort()
        c=[]
        c.extend(b)
        l=len(c)
        d1=[]
        d2=[]
        d1.extend(c[0:x])
        d2.extend(c[x:l])
        a.clear()
        b.clear()
        a.extend(d1)
        b.extend(d2)
        return a,b