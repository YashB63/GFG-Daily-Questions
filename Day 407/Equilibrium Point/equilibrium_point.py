class Solution:
    def findEquilibrium(self, arr):
        n = len(arr)
        l,r = 0,sum(arr)-arr[0]
        
        for i in range(1, n-1):
            l += arr[i-1]
            r -= arr[i]
            
            if(l == r):
                return i
                
        return -1