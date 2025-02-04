class Solution:
	def MinimumWalk(self, graph, u, v, k):
        size = len(graph)
        dp = [[[0 for i in range(k+1)] for j in range(size)] for l in range(size)]
        for z in range(k+1):
            for x in range(size):
                for y in range(size):
                    if(z == 0 and x == y):
                        dp[x][y][z] = 1
                    if(z == 1 and graph[x][y] == 1):
                        dp[x][y][z] = 1
                    if(z > 1):
                        for i in range(size):
                            if(graph[x][i]):
                                dp[x][y][z] += dp[i][y][z-1]
        return dp[u][v][k] % (10**9 +7)
