class Solution:

	def nthRowOfPascalTriangle(self,n):

        mod = 10**9 + 7
        x = [1]
        for i in range(1, n):
            x.append((x[i-1] *(n - i)) % mod * pow(i, mod-2, mod) % mod)
        return x