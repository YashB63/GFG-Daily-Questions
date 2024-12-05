class Solution:
	def addBinary(self, s1, s2):
        i=int(s2,2)
        j=int(s1,2)
        out=bin(j+i)
        return out[2::]