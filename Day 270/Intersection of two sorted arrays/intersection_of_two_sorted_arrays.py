class Solution:
    def printIntersection(self, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        i, j = 0, 0
        intersection = []

        while i < n and j < m:
            while i > 0 and i < n and arr1[i] == arr1[i - 1]:
                i += 1
            while j > 0 and j < m and arr2[j] == arr2[j - 1]:
                j += 1

            if i < n and j < m:
                if arr1[i] < arr2[j]:
                    i += 1
                elif arr1[i] > arr2[j]:
                    j += 1
                else:
                    intersection.append(arr1[i])
                    i += 1
                    j += 1

        if not intersection:
            return [-1]
        return intersection