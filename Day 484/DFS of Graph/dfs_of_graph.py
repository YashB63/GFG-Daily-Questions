class Solution:
    def dfs(self, adj):
        n=len(adj)
        v=[False]*n
        result=[]
        
        def func(vertices):
            v[vertices]=True
            result.append(vertices)
            
            for i in adj[vertices]:
                if not v[i]:
                    func(i)
                    
        func(0)
        return result