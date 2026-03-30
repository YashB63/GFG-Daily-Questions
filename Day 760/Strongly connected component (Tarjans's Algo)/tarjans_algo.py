class Solution:
    ans = []  
    temp = []  
    Time = 0
    
    def SCCUtil(self, adj, u, low, disc, stackMember, st):
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stackMember[u] = True
        st.append(u)

        for v in adj[u]:
            
            if disc[v] == -1 :
            
                self.SCCUtil(adj, v, low, disc, stackMember, st)

                low[u] = min(low[u], low[v])
                        
            elif stackMember[v] == True: 
                low[u] = min(low[u], disc[v])
        
        w = -1
        
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                self.temp.append(w)
                stackMember[w] = False
                
            self.ans.append(self.temp)
            self.temp=[]
            
    def tarjans(self, V, adj):
        
        self.ans = []
        self.temp = []
        
        disc = [-1] * (V)
        low = [-1] * (V)
        stackMember = [False] * (V)
        st =[]
        

        for i in range(V):
            if disc[i] == -1:
                self.SCCUtil(adj, i, low, disc, stackMember, st)
        
        for j in range(len(self.ans)):
            self.ans[j].sort()
        self.ans.sort()
        
        return self.ans