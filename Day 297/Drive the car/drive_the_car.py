class Solution:
    def required(self, arr, k):
        ans=float('-inf')
        for i in arr:
            ans=max(ans, i-k)
        if ans<=0:
            return -1
        return ans