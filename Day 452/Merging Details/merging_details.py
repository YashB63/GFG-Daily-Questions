from collections import defaultdict
from typing import List

class Solution:
    def mergeDetails(self, details : List[List[str]]) -> List[List[str]]:
        hm = {}
        n=len(details)
        parent = [i for i in range(n)]
        size=[1 for i in range(n)]
        def find(u):
            if u!=parent[u]:
                parent[u]=find(parent[u])
            return parent[u]
        def union(u,v):
            rootx=find(u)
            rooty=find(v)
            if rootx!=rooty:
                sizex=size[rootx]
                sizey=size[rooty]
                if sizex<sizey:
                    parent[rootx]=rooty
                    size[rooty]+=size[rootx]
                else:
                    parent[rooty]=rootx
                    size[rootx]+=size[rooty]
        
        for i in range(n):
            for j in range(1,len(details[i])):
                mail = details[i][j]
                if mail in hm:
                    union(find(hm[mail]),i)
                hm[mail]=i
        
        emails=defaultdict(list)
        for mail,ids in hm.items():
            root=find(ids)
            emails[root].append(mail)
        res=[]
        for ids,email in emails.items():
            res.append([details[ids][0] ]+ sorted(email))
        return res