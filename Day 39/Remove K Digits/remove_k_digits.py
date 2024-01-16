class Solution:

    def removeKdigits(self, S, K):
       
        x = []
        for curr in S:
            while x and K > 0 and curr < x[-1]:
                K -= 1
                x.pop()
                
            x.append(curr)
            
        while K > 0:
            x.pop()
            K -= 1
            
        return "".join(x).lstrip('0') or '0'