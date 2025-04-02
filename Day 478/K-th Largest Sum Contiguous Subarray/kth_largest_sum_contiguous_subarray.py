from typing import List
import heapq

class Solution:
    def kthLargest(self, arr, k) -> int:
        l = []
        for i in range(len(arr)):
            max1 = arr[i]
            for j in range(i+1,len(arr)):
                max1 += arr[j]
                l.append(max1)
                
            
        l = sorted(l,reverse = True)
        return l[k-1]