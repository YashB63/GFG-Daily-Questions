from typing import List

class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        dup_arr = arr.copy()
        dup_arr.sort()
        num_sum_dict = {}
        total = 0
        for num in dup_arr:
            if num not in num_sum_dict:
                num_sum_dict.update({num:total})
            total += num
        result = []
        for num in arr:
            if num not in num_sum_dict:
                result.append(0)
            else:
                result.append(num_sum_dict.get(num))
        return result