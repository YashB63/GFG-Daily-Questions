class Solution:
    def alternatingMaxLength(self, arr):
        if not arr:
            return 0
        
        n = len(arr)
        
        up = [1] * n
        down = [1] * n
        
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif arr[i] < arr[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        
        return max(up[n-1], down[n-1])
