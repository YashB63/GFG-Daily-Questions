class Solution:
    def numberOfSubsequences (ob,N,A):
        MOD = 10**9 + 7

        def isPowerOf2(x):
            return x > 0 and (x & (x - 1)) == 0

        count = 0
        for num in A:
            if isPowerOf2(num):
                count += 1

        if count == 0:
            return 0

       
        result = (pow(2, count, MOD) - 1) % MOD
        return result