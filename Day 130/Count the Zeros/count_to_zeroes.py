class Solution:
    def countZeroes(self, arr, n):
        
        left=0
        right=n-1
        while left<=right:
            mid=left+(right-left)//2
            if arr[mid]==0:
                right=mid-1
            else:
                left=mid+1
        return n-left