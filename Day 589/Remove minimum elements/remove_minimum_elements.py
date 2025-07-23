class Solution:    
    def minRemoval(self, arr):
        n = len(arr)
        arr.sort()
        max_len = 0
        
        for i in range(n):
            ind = self.upper_bound(arr, 2 * arr[i])
            max_len = max(max_len, ind - i)
        return n - max_len

    def upper_bound(self, arr, key):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] <= key:
                low = mid + 1
            else:
                high = mid
        return low