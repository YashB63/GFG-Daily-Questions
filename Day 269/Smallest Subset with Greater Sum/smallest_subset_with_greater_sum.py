class Solution:
    def minSubset(self, a,n):
        s=sum(a)
        a.sort(reverse=True)
        c=0
        t=0
        for i in a:
            t+=i
            c+=1
            if t>(s-t):
                break
        return c