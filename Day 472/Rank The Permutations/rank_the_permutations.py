from collections import Counter
import math

class Solution:
    def rank(self, s):
        counter = [0] * 257
        for val in S:
            counter[ord(val)] += 1
    
        if max(counter) > 1:
            return 0
            
        const = 1000003
        ans = 0
        n = len(S)
        for i, val in enumerate(S):
            order = ord(val)
            for j in range(order):
                ans += (counter[j] * math.factorial(n-1-i))%const
            counter[order] -= 1
            ans %= const
        ans += 1
        return ans%const