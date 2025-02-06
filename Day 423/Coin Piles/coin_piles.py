import bisect

class Solution:
    def minSteps(self, a, N, K):
        def upper_bound(A,L,R,K):
            pos=R+1;
            while(L<=R):
                M = (L+R)//2
                if A[M]>K : 
                    pos=M
                    R=M-1
                else : 
                    L=M+1
        
            return pos
        
        
        p = [0]*N
        
        a.sort();
        
        p[0] = a[0];
        for i in range(1,N):
            p[i] = p[i-1] + a[i]
           
        ans = (1<<31)-1  
        prev = 0
        
        for i in range(N):
            pos = bisect.bisect_right(a, a[i]+K, i, N)
            
            if i > 0 and a[i] != a[i-1] :
                prev = p[i-1]
            
            ans = min(ans, prev + p[N-1]-p[pos-1]-(N-pos)*(a[i]+K))
           
        return ans