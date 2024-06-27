class Solution:
    def nCr(self, n, r):
        
        def fact(num):
            ans=1
            for i in range(1, num+1):
                ans*=i
            return ans
        return (fact(n)//(fact(r)*fact(n-r)))%(10**9+7)
