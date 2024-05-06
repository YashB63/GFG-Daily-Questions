class Solution:
	def NthTerm(self, n):
        l = 1
        for i in range(1,n+1):
            l = ((l*i)+1)%(10**9+7)
        return l