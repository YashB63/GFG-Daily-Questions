class Solution:
    def brainGame(self, nums):
        a = [0] * 1005
        
        for i in range(2, 1001):
            for j in range(2 * i, 1001, i):
                a[j] = max(a[j], 1 + a[i])
        x = 0

        for i in range(len(nums)):
            x = x ^ a[nums[i]]
        
        if (x == 0):
            return False
        return True