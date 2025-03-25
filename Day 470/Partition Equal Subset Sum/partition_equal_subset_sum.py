class Solution:
    def equalPartition(self, arr):
        total_sum = sum(arr)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(arr)
        
        dp = [False] * (target + 1)
        dp[0] = True  
        
        for num in arr:
            for j in range(target, num - 1, -1):  
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]