class Solution:
    def padovanSequence(self, n):
        
        if n==0 or n==1 or n==2:
            return 1
        prev_prev=1
        prev=1
        curr=1
        next1=1
        for i in range(3,n+1):
            next1=(prev_prev+prev)%((10**9)+7)
            prev_prev=prev
            prev=curr
            curr=next1
        return next1%((10**9)+7)