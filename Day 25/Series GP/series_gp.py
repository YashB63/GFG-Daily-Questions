class Solution:
	def Nth_term(self, a, r, n):
		
        mod = 10**9 + 7
        res = (a * pow(r, n-1, mod)) % mod
        return res