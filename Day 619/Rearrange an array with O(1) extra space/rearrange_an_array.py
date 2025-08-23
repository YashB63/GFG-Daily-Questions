class Solution:
    def arrange(self, arr):
        n = len(arr)
        for i in range(0, n):
            arr[i] += (arr[arr[i]] % n) * n

        for i in range(0, n):
            arr[i] = arr[i] // n