class Solution:
    def largestSwap(self, s):
        arr = list(s)
        maxDigit = '0'
        maxIndx, l, r = -1, -1, -1

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > maxDigit:
                maxDigit = arr[i]
                maxIndx = i
            elif arr[i] < maxDigit:
                l, r = i, maxIndx

        if l == -1:
            return s

        arr[l], arr[r] = arr[r], arr[l]
        return "".join(arr)