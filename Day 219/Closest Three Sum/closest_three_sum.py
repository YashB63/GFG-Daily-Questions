class Solution:
    def threeSumClosest (self, a, target):
        n=len(a)
        m=[float("inf"),-float("inf")]
        a.sort()
        for i in range(n-2):
            l=i+1
            r=n-1
            while(l<r):
                    x=a[i]+a[l]+a[r]
                    if(x==target):
                        return x
                    y=abs(target-x)
                    if(m[0]==y):
                        m[1]=max(m[1],x)
                    if(y<m[0]):
                        m[0]=y
                        m[1]=x
                    if(x<target):
                        l+=1
                    if(x>target):
                        r-=1
        return(m[1])