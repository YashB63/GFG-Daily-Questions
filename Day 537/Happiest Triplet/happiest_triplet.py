class Solution:
    def smallestDifferenceTriplet(self, arr1, arr2, arr3):
        arr1.sort()
        arr2.sort()
        arr3.sort()

        i = j = k = 0
        minDiff = float('inf')
        result = []

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            a, b, c = arr1[i], arr2[j], arr3[k]
            maxVal = max(a, b, c)
            minVal = min(a, b, c)
            diff = maxVal - minVal

            if diff < minDiff:
                minDiff = diff
                result = [a, b, c]

            if minVal == a:
                i += 1
            elif minVal == b:
                j += 1
            else:
                k += 1

        result.sort(reverse=True)
        return result