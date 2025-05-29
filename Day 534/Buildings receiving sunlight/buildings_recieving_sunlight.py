class Solution:
    def longest(self, arr):
        i, count = 1, 1
        n = len(arr)
        new_element = arr[0]

        for i in range(1, n):
            if (new_element <= arr[i]):
                new_element = arr[i]
                count += 1

        return count