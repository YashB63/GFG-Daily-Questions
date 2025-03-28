class Solution:
    def countDer(self, n):
        if n==1:
            return 0
        if n==2:
            return 1
        prev1=0
        prev2=1
        for i in range(3,n+1):
            curr=(i-1)*(prev1+prev2)
            prev1=prev2
            prev2=curr
        return prev2