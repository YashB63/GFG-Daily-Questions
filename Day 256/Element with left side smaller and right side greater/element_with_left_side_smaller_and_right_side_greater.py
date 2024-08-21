class Solution:
    def findElement(self, arr):
        for index in range(1, len(arr) - 1):
            left_side = arr[:index]
            right_side = arr[index + 1:]
            if arr[index] > max(left_side) and arr[index] < min(right_side):
                return arr[index]
        return -1