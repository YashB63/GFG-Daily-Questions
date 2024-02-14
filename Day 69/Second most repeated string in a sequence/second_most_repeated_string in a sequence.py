class Solution:
    def secFrequent(self, arr, n):
        
        x = {}
        for i in range(0, len(arr)):
            x[arr[i]] = arr.count(arr[i])
        p = sorted(x.values())
        q = p[-2]
        for key, val in x.items():
            if val == q:
                return key