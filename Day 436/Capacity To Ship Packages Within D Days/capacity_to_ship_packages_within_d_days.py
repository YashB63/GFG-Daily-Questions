class Solution:
    def leastWeightCapacity(self, arr, n, d):
        def canShip(capacity):
            days, current_weight = 1, 0
            for weight in arr:
                if current_weight + weight > capacity:
                    days += 1
                    current_weight = weight
                    if days > d:
                        return False
                else:
                    current_weight += weight
            return True

        left, right = max(arr), sum(arr)
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left