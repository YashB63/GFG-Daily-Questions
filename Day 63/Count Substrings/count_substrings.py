class Solution:
	def countSubstr(self, S):
		
        res = 0
        for i in range(len(S)):
            if S[i] == '1':
                res += 1
        return res*(res - 1) // 2