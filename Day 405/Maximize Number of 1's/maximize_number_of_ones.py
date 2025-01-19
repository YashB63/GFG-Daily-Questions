class Solution:
    def maxOnes(self, arr, k):
        n = len(arr)
        left = 0
        right = 0
        zeros = 0
        max_ones = 0

        while right < n:
            if arr[right] == 0:
                zeros += 1

            while zeros > k:
                if arr[left] == 0:
                    zeros -= 1
                left += 1

            max_ones = max(max_ones, right - left + 1)
            right += 1

        return max_ones