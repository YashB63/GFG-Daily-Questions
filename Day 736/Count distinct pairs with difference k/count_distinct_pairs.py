class Solution:
    def TotalPairs(self, nums, k):
        unique_nums = set(nums)
        count = 0

        if k == 0:
            for num in unique_nums:
                if nums.count(num) > 1:
                    count += 1
        else:
            for num in unique_nums:
                if num + k in unique_nums:
                    count += 1

        return count