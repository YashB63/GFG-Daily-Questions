class Solution:
    def NthTerm (self, N):
        if N% 2 != 0:
            p = pow(2, N//2)
        else:
            p = pow (3,N//2 - 1)
        return pow(2, p) 