class Solution:
    def diameter(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        if V == 0:
            return 0
            
        import sys
        sys.setrecursionlimit(max(1000, V + 10))

        visited = [False] * V
        height = [-1] * V

        def dfsPrune(curr):
            visited[curr] = True
            for nxt in adj[curr]:
                if not visited[nxt]:
                    adj[nxt].remove(curr)
                    dfsPrune(nxt)

        dfsPrune(0)

        def findHeight(curr):
            if height[curr] != -1:
                return height[curr]
            best = 0
            for nxt in adj[curr]:
                best = max(best, 1 + findHeight(nxt))
            height[curr] = best
            return best

        findHeight(0)

        res = 0
        for i in range(V):
            firstMax = -1
            secondMax = -1
            for nxt in adj[i]:
                h = height[nxt]
                if h > firstMax:
                    secondMax = firstMax
                    firstMax = h
                elif h > secondMax:
                    secondMax = h

            if firstMax != -1 and secondMax != -1:
                res = max(res, 2 + firstMax + secondMax)
            elif firstMax != -1:
                res = max(res, 1 + firstMax)

        return res