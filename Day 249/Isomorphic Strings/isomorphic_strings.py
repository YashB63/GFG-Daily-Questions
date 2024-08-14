class Solution:
    def areIsomorphic(self,str1,str2):
        h={}
        s=set()
        l1=len(str1)
        l2=len(str2)
        if l1!=l2:
            return 0
        for i in range(len(str1)):
            a=str1[i]
            b=str2[i]
            if a in h:
                if h[a]!=b:
                    return 0
            else:
                if b in s:
                    return 0
                h[a]=b
                s.add(b)
        return 1