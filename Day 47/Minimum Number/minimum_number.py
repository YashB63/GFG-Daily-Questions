class Solution:
    def minimumNumber(self, n, arr):
        
        for i in range(0, n):
            if(arr[i]%2 != 0):
                return 1
        return 2