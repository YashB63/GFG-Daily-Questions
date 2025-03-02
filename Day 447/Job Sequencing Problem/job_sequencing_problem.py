from heapq import heappush, heappop

class Solution:
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda j: j.deadline)
        sums = 0
        h = []
        for j in Jobs:
            sums += j.profit
            heappush(h, j.profit)
            while len(h) > j.deadline:
                sums -= heappop(h)
        return len(h), sums