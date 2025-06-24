class Solution:
    def minimumCoins(self, arr, k):
        n = len(arr)
        arr.sort()

        total = sum(arr)
        min_removed = total
        window_sum = 0
        prefix = 0
        end = 0

        for start in range(n):
            while end < n and arr[end] - arr[start] <= k:
                window_sum += arr[end]
                end += 1

            upper = arr[start] + k
            right_count = n - end

            remove_right = (total - prefix - window_sum) - right_count * upper
            removed = prefix + remove_right
            min_removed = min(min_removed, removed)

            if end == start:
                end += 1
            else:
                window_sum -= arr[start]

            prefix += arr[start]

        return min_removed