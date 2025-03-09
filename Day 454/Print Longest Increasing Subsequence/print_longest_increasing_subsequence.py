class Solution:
    def longestIncreasingSubsequence(self, N, nums):
        dp = [1] * len(nums)
        ans  = [i for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[j] + 1 > dp[i]: 
                        ans[i] = j
                        dp[i] =  dp[j] + 1

        max_ind = 0
        for i in range(len(dp)):
            if dp[i]>dp[max_ind]:
                max_ind = i
        res = []
        while ans[max_ind]!=max_ind:
            res.append(nums[max_ind])
            max_ind = ans[max_ind]
        res.append(nums[max_ind])
        res.reverse()
        return res