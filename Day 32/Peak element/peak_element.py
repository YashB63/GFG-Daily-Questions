class Solution:   
    def peakElement(self,arr, n):
        
        for i in range(len(arr)):
            if i == len(arr) - 1:
                return i
            else:
                if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                    return i
                else:
                    continue