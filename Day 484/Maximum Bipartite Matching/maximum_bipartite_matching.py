class Solution:
	def maximumMatch(self, G):
        matched = [-1]*len(G[0])
        ans = 0
        def dfs(u, visited):
            for i, v in enumerate(G[u]):
                if v == 1 and i not in visited:
                    visited.add(i)
                    if matched[i] == -1 or dfs(matched[i], visited):
                        matched[i] = u
                        return True
            return False
        
        for u, _ in enumerate(G):
            if dfs(u, set()):
                ans += 1
        return ans