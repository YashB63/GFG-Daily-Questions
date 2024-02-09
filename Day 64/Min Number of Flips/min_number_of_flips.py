class Solution:
    def minFlips(self, S):
       
        def zero(S, d):
            res = 0
            for i in range(0, len(S), 2):
                if (S[i] == d):
                    continue
                
                else:
                    
                    res += 1
            
            for i in range(1, len(S), 2):
                if(S[i] != d):
                    continue
                
                else:
                    
                    res += 1
                    
            return res
            
        return min(zero(S, "0"), zero(S, "1"))