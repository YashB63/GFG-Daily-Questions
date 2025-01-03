class Solution:
	def isEulerCircuitExist(self, V, adj):
        deg = [0 for _ in range(V)]
        
        for node in range(V):
            deg[node] = len(adj[node])
        
        def euler_path():
            
            for i in range(V):
                if deg[i]%2!=0:
                    return 0
            return 1
            
        def euler_circuit():
            odd = 0
            eve = 0
            for i in range(V):
                if deg[i]%2!=0:
                    odd+=1
                else:
                    eve +=1
            return 1 if  eve==V or odd==2 else 0
        def dfs(start , vis):
            if vis[start]==True:
                return
            
            vis[start] = True
            for neigh in adj[start]:
                if vis[neigh]==False:
                    dfs(neigh , vis)
            
        def is_connected():
            vis = [False for _ in range(V)]
            
            for i in range(V):
                if deg[i]>0:
                    dfs(i,vis)
                    break
            for i in range(V):
                if vis[i]==False and deg[i]!=0:
                    return False
            return True
                    
        if not is_connected():
            return 0
            
        score = euler_circuit()
        score += euler_path()
        return score