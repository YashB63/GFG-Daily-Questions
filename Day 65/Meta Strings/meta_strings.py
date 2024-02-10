class Solution:
    def metaStrings(self, S1, S2):
        
        n1, n2 = len(S1), len(S2)
        if n1 != n2 or S1==S2:
            return False
        count = 0
        idx1, idx2 = None, None
        for i in range(n1):
            if S1[i] != S2[i]:
                count += 1
                if count > 2:
                    return False
                if idx1 is None:
                    idx1 = i
                else:
                    idx2 = i
        
        if count == 1:
            return False
        if S1[idx1] == S2[idx2] and S1[idx2] == S2[idx1]:
            return True
        return False