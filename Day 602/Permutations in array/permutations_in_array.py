class Solution:
    def isPossible(self, k, arr1, arr2):
        arr1.sort()
        arr2.sort(reverse=True)

        for a, b in zip(arr1, arr2):
            if a + b < k:
                return False
        return True