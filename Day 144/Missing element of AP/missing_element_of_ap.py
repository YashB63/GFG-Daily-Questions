class Solution:
    def findMissing(self, arr, n):
        
        d = (arr[-1]-arr[0])//n
        for i in range(n):
            t = arr[i]+d
            if arr[i+1] != 