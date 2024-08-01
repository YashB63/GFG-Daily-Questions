class Solution:
    def kPangram(self,string, k):
        string=string.split(" ")
        res=0
        for i in string:
            res+=len(i)
        if res<26:
            return False
        d={}
        for i in string:
            for j in i:
                d[j]=d.get(j,0)+1
        if len(d)==26:
            return True
        elif 26-len(d)<=k:
            return True
        return False