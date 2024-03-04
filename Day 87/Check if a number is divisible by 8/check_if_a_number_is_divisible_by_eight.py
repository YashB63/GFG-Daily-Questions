class Solution:
    def DivisibleByEight(self,s):
        
        if s[-3:]=="000" or int(s[-3:])%8==0:
            return 1
        else:
            return -1