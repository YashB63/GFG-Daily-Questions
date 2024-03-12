class Solution:
    def longestSubstring(self, s , n):
        
        ans = "-1"
        mx = 0
        
        for i in range(n):
            x = ""
            for j in range(i,n):
                x += s[j]
                if x in s[j+1:]:
                    if mx < len(x):
                        mx = len(x)
                        ans = x
                else: break
        
        return ans