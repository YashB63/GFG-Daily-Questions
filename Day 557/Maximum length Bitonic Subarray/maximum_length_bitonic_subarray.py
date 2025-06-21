class Solution:
    def bitonic(self, arr):
        n = len(arr)
        
        if n == 0:
            return 0

        max_len = 1

        start = 0
        next_start = 0

        j = 0
        while j < n - 1:
            while j < n - 1 and arr[j] <= arr[j + 1]:
                j += 1

            while j < n - 1 and arr[j] >= arr[j + 1]:
                if j < n - 1 and arr[j] > arr[j + 1]:
                    next_start = j + 1
                j += 1

            max_len = max(max_len, j - (start - 1))

            start = next_start

        return max_len