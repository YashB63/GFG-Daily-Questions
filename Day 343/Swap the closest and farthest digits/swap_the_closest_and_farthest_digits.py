s = ""
n = ""

class Solution:
    def swapDigits(self, n1, n2):
        global s, n
        n1 = list(n1)
        n2 = list(n2)
        
        n1[0], n2[-1] = n2[-1], n1[0]
        n2[0], n1[-1] = n1[-1], n2[0]
        
        s = "".join(n1)
        
        n = "".join(n2)