class Solution:
    
    def longestConsecutive(self,arr):
        arr.sort()
        ans, maxSeq = 1,1
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                continue
            elif arr[i]-arr[i-1] == 1:
                maxSeq += 1
            else:
                maxSeq = 1
            ans = max(ans, maxSeq)
        return ans