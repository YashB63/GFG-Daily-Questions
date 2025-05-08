class Solution:
    def countOfSubstrings(self, S, K):
        hm={}
        count=0
        i=0
        j=0
        n=len(S)
        while j<n:
            if S[j] not in hm:
                hm[S[j]]=1
            else:
                hm[S[j]]+=1
            if j-i+1==K:
                if len(hm)==K-1:
                    count+=1
                hm[S[i]]-=1
                if hm[S[i]]==0:
                    del hm[S[i]]
                i+=1
            j+=1
        return(count)