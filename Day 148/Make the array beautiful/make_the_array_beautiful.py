from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        
        list1 = []
        for i in arr:
            if len(list1) == 0:
                list1.append(i)
            elif (list1[-1] < 0 and i >= 0) or (list1[-1] >= 0 and i < 0):
                list1.pop()
            else:
                list1.append(i)
        return list1