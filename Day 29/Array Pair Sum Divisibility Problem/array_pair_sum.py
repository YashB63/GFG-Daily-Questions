class Solution:
	def canPair(self, nums, k):
		
        x = len(nums)
        if x % 2 == 1:
            return False
        
        y = set()
        
        for i in range(x):
            if (k - nums[i]) % k in y:
                y.remove((k - nums[i]) % k)
            else:
                y.add(nums[i] % k)
        
        return False if y else True