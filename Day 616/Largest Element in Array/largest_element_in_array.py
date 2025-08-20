class Solution:
    def largest(self, arr):
        max_no = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] > max_no:
                max_no = arr[i]
        return max_no