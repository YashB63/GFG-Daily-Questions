class Solution:
    def findKRotation(self, arr):
        sortedArr=sorted(arr)
        maxEle=max(arr)
        if sortedArr!=arr:
            ans=arr.index(maxEle)
            return  ans+1
        return 0