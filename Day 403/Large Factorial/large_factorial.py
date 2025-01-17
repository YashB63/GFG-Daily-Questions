class Solution:
	def factorial(self,a, n):
        MOD = 10**9 + 7
        max_val = max(a)  
        factorial = [1] * (max_val + 1)
        for i in range(2, max_val + 1):
            factorial[i] = (factorial[i - 1] * i) % MOD
        result = [factorial[num] for num in a]
        return result