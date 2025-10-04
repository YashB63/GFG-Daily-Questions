class Solution:
    def reverseList(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotateDeque(self, dq, type, k):
        n = len(dq)

        if n == 0:
            return

        k = k % n
        if k == 0:
            return

        arr = list(dq)

        if type == 1:
            self.reverseList(arr, 0, n - 1)
            self.reverseList(arr, 0, k - 1)
            self.reverseList(arr, k, n - 1)

        elif type == 2:
            self.reverseList(arr, 0, k - 1)
            self.reverseList(arr, k, n - 1)
            self.reverseList(arr, 0, n - 1)

        dq.clear()
        dq.extend(arr)