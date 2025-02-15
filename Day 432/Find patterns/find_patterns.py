class Solution:
    def numberOfSubsequences (self,S,W): 
        count = 0
        track = [False] * len(S)
        
        for start in range(len(S)):
            j = 0
            
            for i in range(start, len(S)):
                if not track[i] and S[i] == W[j]:
                    track[i] = True
                    j += 1
                    if j == len(W):
                        count += 1
                        break
                        
        return count