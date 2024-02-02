class Solution:
	def helper(self, j, s, ps, x):
		# Code here
        if(j == -1):
            return 1
        sm = 0
        c = 0
        
        key = (j, ps)
        if key in x:
            return x[key]
        for i in range(j, -1, -1):
            sm += int(s[i])
            if(ps == -1 or sm <= ps):
                c += self.helper(i-1, s, sm, x)
            else:
                break
            
        x[key] = c
        return c
        
    def TotalCount(self, s):
        return self.helper(len(s) - 1, s, -1, {})