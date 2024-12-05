class Solution:
    def Selection(self, arr):
        arr.sort()
        summ = 0
        for i in range(len(arr)):
            
            summ += arr[i] * i
        return summ%(10**9+7)