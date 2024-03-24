import heapq

class Solution:
    
    def minCost(self,arr,n) :
    
        heapq.heapify(arr)
        costs = []
        while len(arr) != 1:
            price1 = heapq.heappop(arr)
            price2 = heapq.heappop(arr)
            cost = price1 + price2
            costs.append(price1+price2)
            heapq.heappush(arr, cost)
        return sum(costs)