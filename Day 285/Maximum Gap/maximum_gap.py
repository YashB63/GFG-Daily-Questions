from math import inf

class Solution:
	def maxSortedAdjacentDiff(self,arr):
        if len(arr) < 2:    
            return 0
            
        minimum, maximum = min(arr), max(arr)
        count = [0] * (maximum - minimum + 1)
        
        for num in arr:
            count[num - minimum] += 1
            
        prev = inf
        res = -inf
        
        for i, num in enumerate(count):
            if num > 0:
                res = max(res, i - prev)
                prev = i
        
        return res