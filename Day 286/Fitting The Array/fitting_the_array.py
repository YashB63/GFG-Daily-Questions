class Solution:
    def isFit (self,arr, brr, n) : 
        arr.sort()
        brr.sort()
        k=True
        for i in range(len(arr)):
            if arr[i]>brr[i]:
                return False
        return True