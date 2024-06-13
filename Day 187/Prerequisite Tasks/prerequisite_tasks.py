class Solution:
    def isPossible(self,N,P,prerequisites):
        
        adj =[[]for i in range(N)]
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
        q = Queue()
        indegree =[0]*(N)
        for i in range(N):
            for x in adj[i]:
                indegree[x] += 1
        for i in range(N):
            if indegree[i] == 0:
                q.put(i)
        topo = []
        while not q.empty():
            node = q.get()
            topo.append(node)
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.put(i)
        if len(topo) == N:
            return True
        else : return False