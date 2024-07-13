class Solution:
	def editDistance(self, s1, s2):
		
        n = len(s1)
        m = len(s2)
        t = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        # display(t)
        for i in range(n+1):
            for j in range(m+1):
                
                # Base condition
                if i ==0 and j ==0:
                    t[i][j] = 0
                elif i ==0 and j!=0:
                    t[i][j] = j
                elif i !=0 and j==0:
                    t[i][j] = i
                elif s1[i-1] ==s2[j-1]:
                    t[i][j] = t[i-1][j-1]
                else:
                    t[i][j] = 1 + min(t[i][j-1],t[i-1][j],t[i-1][j-1])   # t[i][j-1] - Insertion # t[i-1][j] - Deletion
        
        return t[i][j]