class Solution:
    def kthLargest(self,arr,k):
        arr.sort()
        return(arr[-k])