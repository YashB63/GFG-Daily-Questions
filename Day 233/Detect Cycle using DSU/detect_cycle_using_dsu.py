class Solution:

	def detectCycle(self, V, adj):
        class dsu:
            def __init__(self,n):
                self.pr=[*range(n)]
                self.sz=[1]*n
            def fd(self,a):
                while self.pr[a]!=a:
                    a=self.pr[a]
                return a
            def un(self,a,b):
                a=self.fd(a)
                b=self.fd(b)
                if self.pr[a]==self.pr[b]:
                    return True
                if self.sz[a]>self.sz[b]:
                    a,b=b,a
                self.pr[a]=b
                self.sz[b]+=self.sz[a]
                return False
        nodes=dsu(V)
        for i,lst in enumerate(adj):
            for j in lst:
                if i>j:
                    continue
                if nodes.un(i,j):
                    return 1
        return 0