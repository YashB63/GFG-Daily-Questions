
class Solution:
    def firstRepeated(self,arr, n):
        element_indices = {}
        
        min_index = float('inf')
        
        for i in range(n):
            if arr[i] in element_indices:
                min_index = min(min_index, element_indices[arr[i]])
                
            else:
                element_indices[arr[i]] = i + 1
                
        if min_index == float('inf'):
            return -1
            
        return min_index