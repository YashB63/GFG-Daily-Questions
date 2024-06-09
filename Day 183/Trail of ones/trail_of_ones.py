class Solution:
    def numberOfConsecutiveOnes (ob,n):
       
        fib = [0,1]
        mod = 10**9+7
        for i in range(2,n):
            fib.append((fib[i-1]+fib[i-2])%mod)

        ans = [0,1]
        for i in range(2,n):
            ans.append((ans[-1]*2 + fib[i])%mod)

        return ans[-1]