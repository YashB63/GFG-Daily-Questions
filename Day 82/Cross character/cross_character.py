class Solution:
    def crossPattern (ob,S):
        
        s=""
        for i in range(0,len(S)):
            for j in range(0,len(S)):
                if i==j or i+j==len(S)-1:
                    s+=S[j]
                else:
                    s+=" "
        return s