from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        
        dp1, dp2 = [0] * n, [0] * n
        least, highest = price[0], price[-1]
        
        for i in range(1, n):
            least = min(price[i], least)
            val = price[i] - least
            dp1[i] = max(dp1[i-1], val);
            
        for i in range(n-2, -1, -1):
            highest = max(highest, price[i])
            val = highest - price[i]
            dp2[i] = max(dp2[i+1], val)
            
        ans = 0
        for i in range(n):
            ans = max(ans, dp1[i] + dp2[i])
        return ans