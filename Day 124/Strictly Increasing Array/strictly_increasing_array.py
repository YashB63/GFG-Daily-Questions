class Solution:
	def min_operations(self,nums):
		
        n = len(nums)
        x = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] - nums[j] >= i - j:
                    x[i] = max(x[i], x[j] + 1)

        max_ops = max(x)
        return n - max_ops