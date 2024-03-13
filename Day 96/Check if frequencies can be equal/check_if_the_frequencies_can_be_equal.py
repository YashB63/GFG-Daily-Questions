class Solution:
    def sameFreq(self, s):
        
        a=set(s)
        b=[]
        for i in a:
            b.append(s.count(i))
        c=max(b)-min(b)
        if b.count(max(b))==1 or b.count(max(b))==len(b) or min(b)==1:
            if (c == 0) or (c==1):
                return True
            else:
                return False
        else:
            return False