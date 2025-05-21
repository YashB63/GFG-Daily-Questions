class Solution:
    def knots(self, M, N, K):
        def s(a,b):
            i=1
            j=a
            k=b
            while(k>0):
                k-=1
                i=i*j
                j-=1
            
            p=1
            for j in range(1,b+1):
                p=p*j
            
            return (i//p)
        ans=s(M,K)*s(N,K)
        return ans%(1000000007)