class Solution:
    def countDistinct(self, arr, k):
        res=[]
        for i in range(len(arr) - k + 1):
            sets = set(arr[i:i+k])
            res.append(len(sets))
            
        return res