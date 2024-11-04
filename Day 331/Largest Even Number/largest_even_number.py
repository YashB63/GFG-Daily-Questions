class Solution:
    def LargestEven(self, S):
        a = list(S)
        e = []
        o = []
        for i in range(len(a)):
            if int(a[i])%2==0:
               e.append(int(a[i]))
            else: 
               o.append(int(a[i]))
       
        if len(e)==0:
           return "".join(sorted(a, reverse=True))
       
        e.sort()
        t = e[0]
        e.pop(0)
       
        c = e+o
        c.sort(reverse=True)
        c.append(t)
        for i in range(len(c)):
           c[i] = str(c[i])
        return "".join(c)