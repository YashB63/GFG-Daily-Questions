class Solution:
    def nthCharacter(self, s, r, n):
        
        corr = {
            '1': '10',
            '0': '01'
        }
        
        r = 1 << r
        
        while r > 1:
            index = n // r
            s = corr[s[index]]
            if n >= r:
                n = n % r
            r = r // 2
            
        return s[n//r]