class Solution:
	def totalWays(self, n, capacity):
        capacity.sort()

        ans = 1
        mod = 1000000007

        for i in range(n):
            ans = ans*(capacity[i]-i)%mod

        return int(ans%mod)