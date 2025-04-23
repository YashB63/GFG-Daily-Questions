class Solution:
    def offerings(self, N, nums):
        ans = []
        ans.append(0)
        for i in range(1,N):
            if nums[i]>nums[i-1]:
                ans.append(ans[-1]+1)
            else:
                ans.append(0)
        sumA = 0
        for i in range(N-2, -1, -1):
            if nums[i]>nums[i+1]:
                ans[i] = max(ans[i], ans[i+1]+1)
            sumA += ans[i]+1
        sumA += ans[N-1]+1
        return sumA