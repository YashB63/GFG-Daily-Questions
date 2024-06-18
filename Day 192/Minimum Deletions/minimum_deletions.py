class Solution:
    def minimumNumberOfDeletions(self,S):
        
        st=''
        l=len(S)
        t=[[0]*(l+1) for _ in range(l+1)]
        for i in range(l-1,-1,-1):
            st+=S[i]
            
            
        for i in range(1,l+1):
            for j in range(1,len(st)+1):
                if S[i-1]==st[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return l-t[l][l] 
