from collections import defaultdict

class Solution:

    def CountPs(self, s):
        d=defaultdict(list)
        for i,c in enumerate(s):
            d[c].append(i)
            
        cnt=0
        for c in d:
            if len(d[c])>1:
                i=0
                while i+1<len(d[c]):
                    j=i+1
                    while j<len(d[c]):
                        string=s[d[c][i]:d[c][j]+1]
                        if string==string[::-1]:
                            cnt+=1
                        j+=1
                    i+=1
        return cnt