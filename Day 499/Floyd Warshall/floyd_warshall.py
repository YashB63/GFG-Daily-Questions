class Solution:
	def floydWarshall(self, dist):
        n=len(dist)
        for c in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][c]!=10**8 and dist[c][j]!=10**8:
                        dist[i][j]=min(dist[i][j],dist[i][c]+dist[c][j])
                        
        return dist