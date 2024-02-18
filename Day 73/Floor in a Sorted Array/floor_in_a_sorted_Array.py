class Solution:
    
    def findFloor(self,arr,N,X):
       
        low = 0
        high = N - 1
        
        while(low <= high):
            mid = (low + high) // 2
            if(arr[mid] > X):
                high = mid - 1
            elif(arr[mid] == X):
                return mid
            else:
                if(mid == N - 1 or arr[mid + 1] > X):
                    return mid
                else:
                    low = mid + 1
        
        return -1