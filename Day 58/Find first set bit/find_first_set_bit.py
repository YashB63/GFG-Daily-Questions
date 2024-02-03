class Solution:
    
    def getFirstSetBit(self,n):
        
        b = bin(n).replace("0b","")
        b = b[::-1]
        for i in range(len(b)):
            if b[i] == '1':
                return i + 1
        return 0