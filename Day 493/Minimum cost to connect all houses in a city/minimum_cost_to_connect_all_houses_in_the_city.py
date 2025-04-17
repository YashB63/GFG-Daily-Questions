import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        if n == 1:
            return 0
        edges = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses[j][1])
                edges[i].append((cost, j))
                edges[j].append((cost, i))
        min_heap = [(0, 0)]
        visited = set()
        total_cost = 0
        while len(visited) < n:
            cost, house = heapq.heappop(min_heap)
            if house in visited:
                continue
            visited.add(house)
            total_cost += cost
            for edge_cost, neighbor in edges[house]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_cost, neighbor))
        return total_cost