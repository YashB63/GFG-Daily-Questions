class Solution:
    def minRow(self,n,m,a):
        
        mini = float('inf')
        ans = 0
        for i in range(n):
            rmini = 0
            for j in range(m):
                if a[i][j] == 1:
                    rmini += 1
            if mini > rmini:
                mini = rmini
                ans = i
        return ans+1