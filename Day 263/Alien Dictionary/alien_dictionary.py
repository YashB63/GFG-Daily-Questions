from typing import List

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        def dfs(node, visit, st, adj):
            visit[node]=1
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei, visit, st, adj)
            st.append(node)
            
        adj = {i: [] for i in range(k)}
        
        n=len(dict)
        
        for i in range(n-1):
            s1=dict[i]
            s2=dict[i+1]
            
            length=min(len(s1), len(s2))
            for ptr in range(length):
                if s1[ptr]!=s2[ptr]:
                    adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))  
                    break
            
        visit=[0]*k
        st=[]
        for i in range(k):
            if not visit[i]:
                dfs(i, visit, st, adj)
                
        topo=[]
        while st:
            topo.append(st.pop())
            
        res=""
        
        for node in topo:
            res+=chr(node + ord('a'))
            
        return res