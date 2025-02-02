class Solution:
    def goodStones(self, n, arr) -> int:
        def dfs(i):
            if(i<0 or i>=n):
                return True
            if(visited[i]>0):
                return visited[i]==2
            visited[i]=1
            if(dfs(i+arr[i])):
                visited[i]=2
                return True
            return False
        visited=[0]*n
        res=0
        for i in range(n):
            if(dfs(i)):
                res+=1
        return res