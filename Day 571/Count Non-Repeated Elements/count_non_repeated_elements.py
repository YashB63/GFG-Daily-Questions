class Solution:
    def countNonRepeated(self, arr):
        dict = {}
        n = len(arr)
        for i in arr:
            dict[i] = 0

        for i in arr:
            dict[i] += 1
        counter = 0

        for i in arr:
            if dict[i] == 1:
                counter += 1

        return counter