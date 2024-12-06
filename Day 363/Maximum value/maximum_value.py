class Solution:
    def findMaxValue(self, arr):
        n = len(arr)
        if n < 4:
            return -1  

        
        dp1 = -arr[0]  
        dp2 = float('-inf')  
        dp3 = float('-inf')  
        dp4 = float('-inf')  

        for x in arr[1:]:
            dp4 = max(dp4, dp3 + x)

            dp3 = max(dp3, dp2 - x)

            dp2 = max(dp2, dp1 + x)

            dp1 = max(dp1, -x)

        return dp4