from bisect import bisect_left, insort

class Solution:    
    def countPairs(self,arr, n): 
         
        new_arr = [i * j for i, j in enumerate(arr)]
        ans = 0
        lis = []
        
        for i in range(n - 1, -1, -1):
            if not lis:
                insort(lis, new_arr[i])
                continue
            ans += bisect_left(lis, new_arr[i])
            insort(lis, new_arr[i])
        return ans