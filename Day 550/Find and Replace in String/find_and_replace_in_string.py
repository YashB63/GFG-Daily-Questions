class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        sortd = []
        
        for i in range(Q):
            sortd.append([index[i],i])
        
        sortd.sort(reverse=True)
        
        for ind in sortd:
            i = ind[0]
            s = sources[ind[1]]
            t = targets[ind[1]]
            
            if S[i:i+len(s)] == s:
                S = S[0:i] + t + S[i+len(s):]
        
        return S