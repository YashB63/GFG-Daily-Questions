class Solution:
    def nthMagicNo (self, n):
        j,sum=1,0
        for i in range(32):
            ans=(n>>i)&1
            sum=sum+(5**j)*ans
            j+=1
        return sum%(10**9+7)