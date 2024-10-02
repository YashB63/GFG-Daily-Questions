class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        dict1 = {}
        for i in range(len(arr)):
            if arr[i] in dict1 and abs(dict1[arr[i]]-i) <= k:
                return True
            dict1[arr[i]]=i
        return False