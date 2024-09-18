class Solution:
    def getStar(self,arr):
        elm = []
        n = len(arr)
        greater = float("-inf")
        for i in range(n-1, -1, -1):
            if arr[i] > greater:
                elm.append(arr[i])
                greater = arr[i]
        return sorted(elm, reverse=True)