class Solution:
    def countOfNodes(self, graph,n):
        dis=[0]*(n+1)
        vis=[True]*(n+1)
        
        def dfs(node,c):
            vis[node]=False
            dis[node]=c
            
            for i in graph[node]:
                if vis[i]:
                    dfs(i,c+1)
        
        dfs(1,0)
        
        even=odd=0
        
        for i in range(1,n+1):
            if dis[i]%2:
                odd+=1
            
            else:
                even+=1
        
        return (even*(even-1)//2+(odd)*(odd-1)//2)