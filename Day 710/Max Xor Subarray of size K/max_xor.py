class Solution:
    def maxSubarrayXOR(self, arr, k):
        sub = 0
        for i in range(k):
            sub ^= arr[i]
        ans = sub
        for i in range(k,len(arr)):
            sub ^= arr[i-k]
            sub ^= arr[i]
            ans = max(ans,sub)
        return ans