class Solution:
	def firstAlphabet(self, S):
        a=S[0]
        for i in range(1,len(S)):
            if(S[i]==" "):
                a+=S[i+1]
        return a 