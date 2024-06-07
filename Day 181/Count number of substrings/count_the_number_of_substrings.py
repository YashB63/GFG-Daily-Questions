class Solution:
    def substrCount (self,s, k):
        
        n = len(s)
        
        def atLeastk(k):
            f = 0
            count = [0] * 26
            ans = 0
            i = 0
            j = 0
            for i in range(n):
                while j < n and f < k:
                    count[ord(s[j]) - ord('a')] += 1
                    if count[ord(s[j]) - ord('a')] == 1:
                        f += 1
                    j += 1
               
                if f >= k:
                    ans += (n - j + 1)
                    
                count[ord(s[i]) - ord('a')] -= 1
                if count[ord(s[i]) - ord('a')] == 0:
                    f -= 1
            return ans
        
        return atLeastk(k) - atLeastk(k + 1)