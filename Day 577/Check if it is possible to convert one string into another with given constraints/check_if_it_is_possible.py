class Solution:
    def isItPossible(sef, S, T, M, N):
        i=0
        j=0
        
        if M!=N:
            return 0
        
        while i<M or j<N:
            while i<M and S[i]=="#":
                i+=1
            
            while j<N and T[j]=="#":
                j+=1
            
            if i>=M and j<N:
                return 0
            if i<M and j>=N:
                return 0
            
            if i>=M and j>=N:
                return 1
            
            if S[i]!=T[j]:
                return 0
            else:
                if S[i]=="A" and i<j:
                    return 0
                elif S[i]=="B" and i>j:
                    return 0
            
            i+=1
            j+=1
        
        return 1