class Solution:
	def maxProduct(self, n):
        if n < 8:
            if n == 1: return 1
            return n // 2 * (n - n // 2)
        q, r = divmod(n, 3)
        return 3**q if r == 0 else 3**q * 2 if r == 2 else 3**(q - 1) * 4
