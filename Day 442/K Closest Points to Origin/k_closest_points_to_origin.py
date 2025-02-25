class Solution:
    def kClosest(self, points, k):
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
        return points[:k]