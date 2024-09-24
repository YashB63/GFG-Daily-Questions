class Solution:
    def findMagicalNumber(self, arr):
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == mid:
                if mid == 0 or arr[mid - 1] != mid - 1:
                    return arr[mid]
                else:
                    high = mid - 1
            elif arr[mid] > mid:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1