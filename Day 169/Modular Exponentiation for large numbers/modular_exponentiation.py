class Solution:
	def PowMod(self, x, n, m):
		
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            x %= m
            n //= 2
        return result%m