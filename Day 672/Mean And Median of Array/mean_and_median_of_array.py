class Solution:
    def median(self, arr):
        arr.sort()
        n = len(arr)
        if n % 2 == 0:
            return (arr[n // 2] + arr[(n // 2) - 1]) // 2
        else:
            return arr[n // 2]

    def mean(self, arr):
        return sum(arr) // len(arr)