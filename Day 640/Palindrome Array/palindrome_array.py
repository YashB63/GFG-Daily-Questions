from typing import List

class Solution:
    def isPerfect(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(0, n // 2):
            if (arr[n - i - 1] != arr[i]):
                return False
        return True