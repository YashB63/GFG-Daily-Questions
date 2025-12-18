class Solution:
    def findDuplicates(self, arr):
        ans = []

        for i in range(len(arr)):
            idx = abs(arr[i]) - 1

            if arr[idx] < 0:
                ans.append(abs(arr[i]))
            else:
                arr[idx] = -arr[idx]

        return ans