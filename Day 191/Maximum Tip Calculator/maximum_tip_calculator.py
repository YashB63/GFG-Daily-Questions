from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
       
        diff = [(abs(arr[i] - brr[i]), i) for i in range(n)]
        diff.sort(reverse=True, key=lambda x: x[0])
        
        total_tips = 0
        count_a = 0
        count_b = 0
        
        for _, i in diff:
            if (arr[i] >= brr[i] and count_a < x) or count_b == y:
                total_tips += arr[i]
                count_a += 1
            else:
                total_tips += brr[i]
                count_b += 1
        
        return total_tips