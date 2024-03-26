class Solution:
    def longestPalin(self, S):
        
        if len(S) <= 1:
            return S
        Max_Len=1
        Max_Str=S[0]
        for i in range(len(S)-1):
            for j in range(i+1,len(S)):
                if j-i+1 > Max_Len and S[i:j+1] == S[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = S[i:j+1]
        return Max_Str