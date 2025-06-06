import sys
from typing import List
sys.setrecursionlimit(10**5)

class Solution:
    def isSafe(self,pos, n,m,visited, mat):
        return pos[0]>=0 and pos[0]<n and pos[1]>=0 and pos[1]<m and mat[pos[0]][pos[1]]!=0 and (pos[0],pos[1]) not in visited
    def util(self,start, end, mat, visited, n,m, res, d):
        visited.add((start[0],start[1]))
        if start[0]==end[0] and start[1]==end[1]:
            if res[0]<d:
                res[0]=d
                visited.remove((start[0],start[1]))
                return
        path=[[0,1],[1,0],[0,-1],[-1,0]]
        for p in path:
            if self.isSafe((start[0]+p[0], start[1]+p[1]), n,m, visited, mat):
                self.util((start[0]+p[0], start[1]+p[1]), end, mat, visited, n,m, res, d+1)
        visited.remove((start[0],start[1]))
        return
    
    def longestPath(self,mat : List[List[int]],n : int, m : int, xs : int, ys : int, xd : int, yd : int) -> int:
        visited=set()
        visited.add((xs,ys))
        res=[0]
        
        if mat[xs][ys]==0 :
            return -1
        self.util((xs,ys),(xd,yd), mat, visited, n,m, res,0)
        if res[0]!=0:
            return res[0]
        return -1