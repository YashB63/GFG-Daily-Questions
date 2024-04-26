class Solution:
    def isRepresentingBST(self, arr, N):
       
        i = 0
        while i < N-1:
            if arr[i] > arr[i+1]:
                return 0
            i += 1
        return 1