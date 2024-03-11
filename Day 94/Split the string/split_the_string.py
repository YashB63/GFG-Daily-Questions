class Solution:
    def isPossible (self, S):
       
        s = set()
        m = ''
        for i in range(len(S)):
            m+=S[i]
            if m not in s:
                s.add(m)
                m = ''
            if len(s)>=4:
                return 1
        return 0