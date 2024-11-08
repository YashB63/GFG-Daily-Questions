class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        n = len(arr)
        for i in range(n-1):
            if k+i <= n:
                if arr[i] in arr[i+1:i+k+1]:
                    return True
            else:
                if arr[i] in arr[i+1:]:
                    return True
        return False