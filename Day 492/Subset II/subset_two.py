class Solution:
    def solve(self, i, nums, com, ans):
        ans.append(com[:])
        
        for j in range(i, len(nums)):
            if j>i and nums[j]==nums[j-1]:
                continue
            
            com.append(nums[j])
            self.solve(j+1, nums, com, ans)
            com.pop()
            
    def printUniqueSubset(self, nums):
        ans = []
        nums.sort()
        self.solve(0, nums, [], ans)
        return ans