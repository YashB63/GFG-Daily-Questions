class Solution:
	def perfectSum(self, arr, n, sum):
		
        def ss(idx, sum, memo=None):
            if memo is None:
                memo = {}
            if (idx, sum) in memo:
                return memo[(idx, sum)]
            if sum == 0 and idx == n:
                return 1
            if sum < 0 or idx == n:
                return 0
            include = ss(idx + 1, sum - arr[idx], memo)  
            exclude = ss(idx + 1, sum, memo)             
            memo[(idx, sum)] = (include + exclude) % (10**9 + 7)  
            return memo[(idx, sum)]
        
        return ss(0, sum)