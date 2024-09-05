from typing import List

class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        Map = {}
        for i in arr:
            if i in Map.keys():
                Map[i] = Map[i] + 1
            else:
                Map[i] = 1
        counts = []
        for value in Map.values():
            if value in counts:
                return False
            else:
                counts.append(value)
        return True