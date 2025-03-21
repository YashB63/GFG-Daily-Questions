class Solution():
    def specialPalindrome(self,s1, s2):
        def _get(k): 
            return (s2[k-i], True) if i <= k < i + N2 else (s1[k], False)
        
        INV, N1, N2 = 10**9, len(s1), len(s2)
        ans, baseline = INV, 0

        for i in range(N1 // 2):
            if s1[i] != s1[N1 - 1 - i]: 
                baseline += 1
        
        for i in range(N1 - N2 + 1):
            tmp = baseline  
            for j in range(i, i + N2):
                c0, (c1, f1) = s2[j - i], _get(N1 - 1 - j)
                
                if s1[j] != s1[N1 - 1 - j] and (not f1 or j < N1 - 1 - j): 
                    tmp -= 1
                if c0 != s1[j]: 
                    tmp += 1
                if c0 != c1:
                    if f1: 
                        tmp = INV  
                        break
                    tmp += 1
            
            ans = min(ans, tmp)  
        
        return -1 if ans >= INV else ans