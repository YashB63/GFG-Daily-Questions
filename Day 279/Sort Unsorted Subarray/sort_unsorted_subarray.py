class Solution:
    def printUnsorted(self, arr):
        n = len(arr)
        start = 0
        end = n - 1
        while start < n - 1 and arr[start] <= arr[start+1]:
            start += 1
        if start == n-1:
            return [0, 0]
        
        while end > 0 and arr[end] >= arr[end-1]:
            end -= 1
        
        min_elem = min(arr[start:end+1])
        max_elem = max(arr[start:end+1])
        
        while start > 0 and arr[start-1] > min_elem:
            start -= 1
        
        while end < n-1 and arr[end+1] < max_elem:
            end += 1
        
        return [start, end]