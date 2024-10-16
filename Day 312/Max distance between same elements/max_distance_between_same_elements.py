class Solution:
    def maxDistance(self, arr):
        h={}
        max_val=-float('inf')
        for i in range(len(arr)):
            if arr[i] not in h:
                h[arr[i]]=i
        for i in range(len(arr)):
            dis=i-h[arr[i]]
            max_val=max(max_val,dis)
        return max_val