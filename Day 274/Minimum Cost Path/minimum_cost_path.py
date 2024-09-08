import heapq

class Solution:
	def minimumCostPath(self, grid):
        n=len(grid)
        m=len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pq=[]
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = grid[0][0]
        heapq.heappush(pq, (grid[0][0], 0, 0))
        while pq:
            current_cost, x, y = heapq.heappop(pq)
    
            if x == n - 1 and y == m - 1:
                return current_cost
        
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    new_cost = current_cost + grid[nx][ny]
           
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))