class Solution:
    def closer(self, a, n,  x):
        l=0
        h=n-1
        while(l<=h):
         m= (l+h)//2
         if(a[m]==x):
             return m
         elif(m>0 and a[m-1]==x):
             return m-1
         elif(m<n-1 and a[m+1]==x):
             return m+1
         elif(a[m-1]>x):
             h=m-2
         else:
             l=m+2
        return -1    