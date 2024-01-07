class Solution:
    def smallestSubstring(self, S):
       
        n = [-1, -1, -1]
        left = len(S)
        right = left + 1
        for i in range(left):
            x = int(S[i])
            n[x] = i
            ma = max(n)
            mi = min(n)
            if(mi != -1):
                right = min(ma-mi+1, right)
            
        if(right == left + 1):
            return -1
        
        return right