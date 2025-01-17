class Solution:
    def checkCompressed(self, S, T):
        lenS = len(S)
        position = 0
        i = 0
        while i < len(T):
            
            char = ""
            if T[i].isdigit():
                
                while i < len(T) and T[i].isdigit():
                    char += T[i]
                    i += 1
                
                position += int(char)
                if position > lenS:
                    return 0
            else:
                if T[i] != S[position]:
                    return 0
                i += 1
                position += 1
        
        return int(position == lenS)