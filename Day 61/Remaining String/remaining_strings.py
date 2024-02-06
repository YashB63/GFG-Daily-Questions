class Solution:
	def printString(self, S, ch, count):
		
        tempcount = 0
        if count == 0:
            return s
        
        for i in range(len(s)):
            if S[i] == ch:
                tempcount += 1
                if tempcount == count:
                    if S[i+1::] == "":
                        return "Empty string"
                    return S[i+1::]
                    
        return "Empty string"