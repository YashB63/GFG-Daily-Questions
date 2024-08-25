class Solution:
    def kthSmallest(self, arr,k):
        a=sorted(arr)
        return a[k-1]