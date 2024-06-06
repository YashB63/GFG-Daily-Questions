class Solution:
    def swapNibbles (self, n):
        
        n=bin(n)[2:]
        l=len(n)
        n=((8-l)*'0')+n
       
        s1=n[4:]
        s2=n[:4]
        return int(s1+s2,2)