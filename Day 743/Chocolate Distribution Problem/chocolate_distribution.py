class Solution:
    def findMinDiff(self, arr,M):
        lth=len(arr)
        arr.sort()
        mn=float('inf')
        for left,ve in enumerate(arr):
            right=left+M-1
            if right>=lth:
                break
            mn=min(mn,arr[right]-arr[left])
        return mn