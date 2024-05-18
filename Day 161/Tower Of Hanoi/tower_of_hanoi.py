class Solution:

	def orangesRotting(self, grid):
		
		queue = []
        cntFresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append([i,j])
                if grid[i][j]==1:
                    cntFresh+=1
        dx = [1,0,-1,0]
        dy = [0,-1,0,1]
        n =len(grid)
        m =len(grid[0])
        count=0
        if cntFresh == 0:
            return 0
        while len(queue)>0:
            count+=1
            size = len(queue)
            for i in range(size):
                [x,y] = queue.pop(0)
                for c in range(4):
                    drow = x+dx[c]
                    dcol = y+dy[c]
                    if drow>=0 and dcol>=0 and drow < n and dcol < m and grid[drow][dcol]==1:
                        grid[drow][dcol]=2
                        queue.append([drow,dcol])
                        cntFresh-=1
        if cntFresh >0:
            return -1
        return count-1