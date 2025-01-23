class Solution:
    def maxLen(self, arr):
        ans = 0
        c = 0
        d = {0:-1}
        for i in range(len(arr)):
            if arr[i] == 1:
                c += 1
            else:
                c -= 1
            
            if c in d:
                ans = max(ans,i-d[c])
            else:
                d[c] = i
        return ans