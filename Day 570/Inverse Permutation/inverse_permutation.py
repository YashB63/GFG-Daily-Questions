class Solution:
    def inversePermutation(self, arr):
        n = len(arr)
        ans = [0] * n

        for i in range(n):
            ans[arr[i] - 1] = i + 1
        return ans