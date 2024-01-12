class Solution:
    def trappingWater(self, arr,n):
        
        left = [0] * n
        right = [0] * n
        
        left[0] = arr[0]
        
        for i in range(1, n):
                left[i] = max(left[i - 1], arr[i])
                
        right[n - 1] = arr[n - 1]
            
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], arr[i])
        
        res = 0        
            
        for i in range(n):
            res += min(left[i], right[i]) - arr[i]
            
        return res