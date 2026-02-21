class Solution:
     def find_cost(self, heights, costs, target_height):
          cost = 0
          for i in range(len(heights)):
               cost += abs(target_height - heights[i]) * costs[i]
          return cost


     def minCost(self, heights, costs):
          low = min(heights)
          high = max(heights)
          ans = float('inf')

          while low <= high:
               mid1 = low + (high - low) // 3
               mid2 = high - (high - low) // 3

               cost1 = self.find_cost(heights, costs, mid1)
               cost2 = self.find_cost(heights, costs, mid2)

               ans = min(ans, cost1, cost2)
               if cost1 < cost2:
                    high = mid2 - 1
               else:
                    low = mid1 + 1
          return ans