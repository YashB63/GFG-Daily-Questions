class Solution:
    def numProvinces(self, adj_mat, V):
        
        def dfs(node):
            visited[node] = True
            for i in range(n):
                if not visited[i] and adj_mat[node][i]==1:
                    dfs(i)


        n = len(adj_mat)
        visited = [False]*n
        ct = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ct+=1

        return ct