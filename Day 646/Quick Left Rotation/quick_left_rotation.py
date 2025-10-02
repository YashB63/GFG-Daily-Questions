class Solution:
    def reverseArray(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def leftRotate(self, arr, k):
        n = len(arr)
        k = k % n
        if k == 0:
            return

        self.reverseArray(arr, 0, k - 1)
        self.reverseArray(arr, k, n - 1)
        self.reverseArray(arr, 0, n - 1)