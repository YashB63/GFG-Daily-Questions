MOD = 1000000007

def factorial(n):
    f = 1
    if n == 0 or n == 1:
        return 1
    for i in range(2, n + 1):
        f = (f * i) % MOD
    return f

class Solution:
    def getSum(self, arr):
        n = len(arr)  

        fact = factorial(n)

        digit_sum = sum(arr) % MOD

        fact_div_n = (fact *
                      pow(n, MOD - 2, MOD)) % MOD  
        digit_sum = (digit_sum * fact_div_n) % MOD

        result = 0
        k = 1
        for _ in range(n):
            result = (result + k * digit_sum) % MOD
            k = (k * 10) % MOD

        return (result + MOD) % MOD