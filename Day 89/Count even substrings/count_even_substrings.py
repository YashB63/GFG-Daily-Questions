class Solution:

    def evenNumSubstring(self, S):
        
        c=0
        for i in range(0,len(S)):
            if ord(S[i])%2==0:
                c+=i+1
        return c