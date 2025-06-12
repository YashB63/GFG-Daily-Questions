class Solution:
    def countPaths(self, edges, V, src, dest):
        graph = [[] for _ in range(V)]
        indegree = [0] * V

        for u, w in edges:
            graph[u].append(w)
            indegree[w] += 1

        q = deque()

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        dp = [0] * V
        dp[dest] = 1

        for node in reversed(topo):
            for nei in graph[node]:
                dp[node] += dp[nei]

        return dp[src]