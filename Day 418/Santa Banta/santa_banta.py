class Solution:
    def precompute(self):
        self.ans=[]
        self.arr=[-1]*(int(1e6)+1)
        
        def eratos(num):
            
            i=2
            n=num
            while num<=int(1e6):
                self.arr[num]=1
                num=n*i
                i+=1
        
        for i in range(2,len(self.arr)):
            if self.arr[i]==-1:
                self.ans.append(i)
                eratos(i)
                
    def helpSanta (self, n, m, g) : 
        if not g:
            return -1
        
        size=[1]*n
        parent=[i+1 for i in range(n)]
        
        
        def findParent(num):
            
            if num==parent[num-1]:
                return num
            
            parent[num-1]=findParent(parent[num-1])
            
            return parent[num-1]
        
        
        for i in g:
            a=findParent(i[0])
            b=findParent(i[1])
            
            if a!=b:
                
                if size[a-1] >= size[b-1]:
                    parent[b-1]=a
                    size[a-1]+=size[b-1]
                else:
                    parent[a-1]=b
                    size[b-1]+=size[a-1]
        
        m=0
        for i in range(n):
            if i+1==parent[i]:
                m=max(m,size[i])
        
        
        return self.ans[m-1]