class Solution:
    def minAnd2ndMin(self, arr):
        n = len(arr)

        if n < 2:
            return [-1]

        first = float('inf')
        second = float('inf')

        for i in range(n):
            if arr[i] < first:
                second = first
                first = arr[i]

            elif arr[i] < second and arr[i] != first:
                second = arr[i]

        if second == float('inf'):
            return [-1]

        return [first, second]