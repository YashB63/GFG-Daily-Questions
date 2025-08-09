class Solution:
    def newIPAdd(self, S):
        return '.'.join(str(int(i)) for i in S.split('.'))