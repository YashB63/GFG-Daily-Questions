class Solution:
    def findKRotation(self,arr,  n):
        
        start = 0
        end = n-1
        
        while start <= end:
            if arr[start] <= arr[end]:
                return start
                
            mid = start + (end - start) // 2
            next_ = (mid + 1) % n
            prev = (mid - 1 + n) % n
            
            if arr[mid] <= arr[prev] and arr[mid] <= arr[next_]:
                return mid
            
            elif arr[mid] <= arr[end]:
                end = mid - 1
                
            elif arr[mid] >= arr[start]:
                start = mid + 1
                
        return -1