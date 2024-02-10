class Solution:
    def arrangeString(self, s):
        # code here 
        l = []
        n = []
        for i in s:
            if(i.isalpha()):
                l.append(i)
            if(i.isdigit()):
                n.append(int(i))
                
        l.sort()
        m = sum(n)
        if(len(n) == 0):
            return("".join(l))
        else:
            return("".join(l) + str(m))