from collections import Counter,deque

class Solution:
    def firstNonRepeating(self, s):
        ret=[]
        cnt=Counter()
        cand=deque()
        for c in s:
            cnt[c]+=1
            if cnt[c]==1:
                cand.append(c)
            while cand and cnt[cand[0]]>1:
                cand.popleft()
            if cand:
                ret.append(cand[0])
            else:
                ret.append('#')
        return ''.join(ret)