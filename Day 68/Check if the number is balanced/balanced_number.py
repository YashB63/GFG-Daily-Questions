class Solution:
	def balancedNumber(self, N):
        
        lhs = 0
        rhs = 0
        for i in range(len(N)//2):
            lhs += int(N[i])
        for i in range((len(N)//2)+1, len(N)):
            rhs += int(N[i])
        
        return 1 if lhs == rhs else 0