class Solution:
    def missingIntervals(self, arr, l, r):
        n = len(arr)
        ans = []
        if arr[0] != l:
            ans.append((l, arr[0] - 1))

        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            if diff >= 2:
                ans.append((arr[i] + 1, arr[i + 1] - 1))

        if arr[-1] != r:
            ans.append((arr[-1] + 1, r))

        if not ans:
            ans.append((-1, -1))

        return ans