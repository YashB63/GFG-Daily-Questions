class Solution:
    ans = 0

    def countPathsUtil(self, u, destination, vis, adj):
        vis[u] = True
        if (u == destination):
            self.ans += 1

        for v in adj[u]:
            if (vis[v] == False):
                self.countPathsUtil(v, destination, vis, adj)

        vis[u] = False

    def countPaths(self, V, adj, source, destination):
        vis = [False for i in range(V)]
        self.countPathsUtil(source, destination, vis, adj)
        return self.ans