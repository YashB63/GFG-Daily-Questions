class Solution:
    def formatArray(self, arr):
        arr.sort()
        i = 0
        j = len(arr) // 2
        if len(arr) % 2 == 1:
            j += 1
        while j < len(arr):
            if arr[i] >= arr[j]:
                return False
            i += 1
            j += 1
        return True