class Solution:
    def maxSumSubarray(self, arr):
        n = len(arr)

        max_sum = arr[0]

        no_skip = arr[0]

        one_skip = 0

        for i in range(1, n):
            one_skip = max(no_skip, one_skip + arr[i])
            no_skip = max(arr[i], no_skip + arr[i])
            max_sum = max(max_sum, no_skip, one_skip)

        return max_sum