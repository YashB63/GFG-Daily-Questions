import heapq

class Solution:
    def squaredDis(self, point):
        return point[0] * point[0] + point[1] * point[1]

    def kClosest(self, points, k):
        maxHeap = []

        for i in range(len(points)):
            dist = self.squaredDis(points[i])

            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist, points[i]))
            else:
                if dist < -maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-dist, points[i]))

        res = []
        while maxHeap:
            res.append(heapq.heappop(maxHeap)[1])

        return res