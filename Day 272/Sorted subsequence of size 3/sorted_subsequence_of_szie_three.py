class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []
        
        left_min = [0] * n
        right_max = [0] * n
        
        left_min[0] = arr[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], arr[i])
        
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])
        
        for j in range(1, n - 1):
            if left_min[j - 1] < arr[j] < right_max[j + 1]:
                return [left_min[j - 1], arr[j], right_max[j + 1]]
        
        return []