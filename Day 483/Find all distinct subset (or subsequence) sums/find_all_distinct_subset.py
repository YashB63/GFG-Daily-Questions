class Solution:
	def DistinctSum(self, nums):
        total_sum = sum(nums)
        possible_sums = {0}  
        
        for num in nums:
            new_sums = set()
            for s in possible_sums:
                new_sums.add(s + num)
            possible_sums.update(new_sums)
        
        return sorted(possible_sums)