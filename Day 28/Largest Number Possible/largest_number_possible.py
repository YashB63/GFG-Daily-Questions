class Solution:
    def findLargest(self, N, S):
        
        res = ''
        if S == 0 and N > 1:
            return -1
        for i in range(0, N):
            if S > 9:
                res += '9'
                S -= 9
            else:
                res += str(S)
                S -= S
        
        if S != 0:
            return -1
        
        return res    