from collections import deque

class Solution:
    def StringQuery(self,N,Q,S,Q1,Q2):
        ls = []
        rt = 0
        for i in range(Q):
            if Q1[i] == 1:
                rt += N-(Q2[i]%N)
            else:
                ls.append(S[(Q2[i]+rt)%N])
        return ls