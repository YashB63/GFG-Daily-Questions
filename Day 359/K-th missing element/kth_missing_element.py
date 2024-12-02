class Solution:
    
    def KthMissingElement(self,arr,k): 
        start = arr[0]
        missing_count =0
        for i in range(1,len(arr)):
            missing_between = arr[i] - arr[i - 1] -1
            if missing_count + missing_between >= k:
                return arr[i - 1] + (k - missing_count)
            missing_count += missing_between
        return -1