class Solution:
    def search(self,arr, N, X):
        for i in range(N):
            if arr[i] == X:
                return i
        return -1