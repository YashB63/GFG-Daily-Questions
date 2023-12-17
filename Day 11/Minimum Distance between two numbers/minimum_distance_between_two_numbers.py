class Solution:
    def minDist(self, arr, n, x, y):
        min_distance = float('inf')
        x_index = -1
        y_index = -1
        
        for i in range(n):
            if arr[i] == x:
                x_index = i
                
                if y_index != -1:
                    min_distance = min(min_distance, abs(x_index - y_index))
                    
            if arr[i] == y:
                y_index = i
                
                if x_index != -1:
                    min_distance = min(min_distance, abs(y_index - x_index))
                    
        if x_index == -1 or y_index == -1:
            return -1
            
        return min_distance