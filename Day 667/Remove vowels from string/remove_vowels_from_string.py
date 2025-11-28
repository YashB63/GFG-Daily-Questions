class Solution:
    def removeVowels(self, s):
        n = len(s)
        j = 0
        s = list(s)  
        
        for i in range(n):
            if s[i] not in ['a', 'e', 'i', 'o', 'u']:
                s[j] = s[i]  
                j += 1

        return ''.join(s[:j])