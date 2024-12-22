class Solution:   
    def peakElement(self,arr):
        n = len(arr)
        low = 0
        high = n - 1
        while low <= high:
            
            mid = (high+low)//2
            
            if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid] ):
                return mid
            elif arr[mid] > arr[mid+1]:
                high = mid - 1
                
            else:
                low = mid + 1