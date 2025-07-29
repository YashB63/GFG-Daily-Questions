from typing import List

class Solution:
    def minimumSwaps(self, c: List[int], v: List[int], n: int, k: int, b: int, t: int) -> int:
        ans = 0  
        ts = 0  
        r = 0  

        for i in range(n-1, -1, -1):
            if (r >= k):
                break

            d = v[i] * t

            if (d >= b-c[i]):
                ans += ts  
                r += 1  
            else:
                ts += 1  

        if (r >= k):
            return ans  
        return -1