class Solution:
    def minimumNumberOfSwaps(self,s):
        bal = 0
        swap = 0
        
        for i in range(len(s)):
            if s[i] =='[':
                bal -= 1
            else:
                bal += 1
                if (bal> 0):
                    swap += bal
        return swap  