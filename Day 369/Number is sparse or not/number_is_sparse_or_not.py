class Solution:
    def isSparse(self,n):
        b=bin(n)[2:]
        for i in range(0,len(b)-1):
            if b[i]=='1' and b[i+1]=='1':
                return 0
        return 1