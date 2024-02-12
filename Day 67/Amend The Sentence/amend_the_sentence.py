class Solution:

    def amendSentence(self, s):

        a = "ABCDEFGHIJKLMNNOPQRSTUVWXYZ"
        x = s[0]
        k = []
        
        for i in range(1, len(s)):
            if s[i] not in a:
                x += s[i]
            
            else:
                k.append(x.lower())
                x = s[i]
        
        k.append(x.lower())
        k = " ".join(k)
        return k