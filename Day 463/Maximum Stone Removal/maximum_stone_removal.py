class Solution:
    def maxRemove(self, adj, n):
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rootx=find(x)
            rooty = find(y)
            if rootx!=rooty:
                sizex=size[rootx]
                sizey = size[rooty]
                if sizex<sizey:
                    parent[rootx]=rooty
                    size[rooty]+=size[rootx]
                else:
                    parent[rooty]=rootx
                    size[rootx]+=size[rooty]
        parent={}
        size = {}
        for x,y in adj:
            y=y+10001
            if x not in parent:
                parent[x]=x
                size[x]=1
            if y not in parent:
                parent[y]=y
                size[y]=1
            union(x,y)
        return n-sum(1 for i in parent if i==find(i))