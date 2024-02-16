class Solution:
    def ReFormatString(self,S, K):
        
        res = ""
        j = 0
        for i in range(len(S)-1, -1, -1):
            if S[i] != '-':
                if j == K:
                    res += '-'
                    j = 0
                if ord(S[i]) >= 97 and ord(S[i]) <= 122:
                    res += chr(ord(S[i]) - 32)
                else:
                    res += S[i]
                j += 1
        
        res = res[::-1]
        return res