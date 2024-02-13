class Solution:
    def DivisibleByEight(self,S):
        
        x = 0
        if len(S) >= 3:
            x = int(S[-3:])
        else:
            x = int(S)
        
        if x%8 == 0:
            return 1
        return -1