class Solution:
	def checkTriplet(self,arr):
        sqr = [x**2 for x in arr]
        m = max(sqr)
        l = [x for x in range(1, m+1)]
        f = [0]*(m+1)
        for x in sqr:
            f[x] = f[x]+1
            
        for i in l:
            if f[i] == 0:
                continue
            for j in l:
                if j == i and f[j] < 2:
                    continue
                elif f[j] == 0:
                    continue
                if i + j < m and f[i + j] != 0:
                    return True
        return False