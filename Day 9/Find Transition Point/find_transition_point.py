class Solution:
    def transitionPoint(self, arr, n): 
        low = 0
        high = n - 1
        transition_index = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == 1:
                transition_index = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return transition_index