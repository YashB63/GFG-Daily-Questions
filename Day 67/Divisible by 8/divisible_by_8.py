from itertools import permutations

class Solution:
    def isDivisible8(self, S):
        
        if len(S) == 1:
            if int(S[0]) == 8:
                return True
        elif len(S) == 2:
            if int(S[0] + S[1]) % 8 == 0 and int(S[1] + S[0])%8 == 0:
                return True
                
        j = 0
        while j<len(S) - 2:
            for i in list(permutations(S[j:j+3])):
                a = int(''.join(i))
                if a%8 == 0:
                    return True
                    
            
            j += 1
            
        return False