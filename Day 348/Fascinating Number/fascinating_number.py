class Solution:
	def fascinating(self,n):
        if n<100:
            return false
        concatenated=str(n)+str(n*2)+str(n*3)
        return len(concatenated) == 9 and set(concatenated) == set("123456789")
