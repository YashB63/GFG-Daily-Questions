from bisect import bisect as bi

class Solution:
    def countPairs(self, arr1, arr2):
        MAX_VALUE = 10**3
        counts2 = [0] * (MAX_VALUE + 1)
        suffix_sums2 = [0] * (MAX_VALUE + 2)
        for a in arr2:
            counts2[a] += 1
        for i in reversed(range(MAX_VALUE + 1)):
            suffix_sums2[i] = suffix_sums2[i + 1] + counts2[i]
        count = 0
        arr1.sort()
        i, m = 0, len(arr1)
        while i < m and arr1[i] == 0:
            i += 1
        while i < m and arr1[i] == 1:
            i += 1
            count += counts2[0]
        while i < m and arr1[i] == 2:
            i += 1
            count += suffix_sums2[5] + counts2[0] + counts2[1]
        while i < m and arr1[i] == 3:
            i += 1
            count += suffix_sums2[4] + counts2[0] + counts2[1] + counts2[2]
        for i in range(i, m):
            count += suffix_sums2[arr1[i] + 1] + counts2[0] + counts2[1]
        return count