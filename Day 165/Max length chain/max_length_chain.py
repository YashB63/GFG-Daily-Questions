class Solution:
    def maxChainLen(self,Parr, n):
        
        Parr = sorted(Parr, key = lambda x: x.b)
        prev = -1
        count=0
        for item in Parr:
            if prev<item.a:
                count+=1
                prev = item.b
        return count