class Solution():
    def lexicographicallyLargest(self, a, n):
        p=[]
        b=[]
        b.append(a[0])
        
        for i in range(1,n):
            if (a[i]+a[i-1])%2==0:
                b.append(a[i])
                continue
            b.sort(reverse=True)
            p+=b
            b=[]
            b.append(a[i])
        b.sort(reverse=True)
        p+=b
        return p