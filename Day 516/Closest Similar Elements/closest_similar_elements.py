from typing import List

class Solution:
    def closestSimilarElements(self, n : int, arr : List[int], indexDifference : int, valueDifference : int) -> bool:
        for i in range(n-1):
            
            for j in range(i+1,n):
                
                if abs(i-j) <= indexDifference and abs(arr[i]-arr[j]) <= valueDifference:
                    return True
        return False