class Solution:
   
    def isInterleave(self, A, B, C):
        lnA = len(A)
        lnB = len(B)
        lnC = len(C)

        if lnC != lnA + lnB:
            return 0

        dp = [[False for _ in range(lnB+1)] for _ in range(lnA+1)]
        
        dp[0][0] = True

        for iA in range(lnA + 1):
            for iB in range(lnB + 1):
                if iA > 0 and A[iA-1] == C[iA+iB-1]:
                    dp[iA][iB] |= dp[iA-1][iB]
                    
                if iB > 0 and B[iB-1] == C[iA+iB-1]:
                    dp[iA][iB] |= dp[iA][iB-1]
                    
        return int(dp[lnA][lnB])