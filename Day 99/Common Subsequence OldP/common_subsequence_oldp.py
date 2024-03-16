class Solution:
    def commonSubseq (ob, S1, S2):
        
        chars1 = set(S1)
        return +any(c in chars1 for c in S2)