class Solution:
    def nullPoints(self, n, a, getAnswer):
        def neutral_point(low, high):
            while low < high:
                mid = (low + high) / 2
                totalforce = 0
                for magnet in a:
                    totalforce += 1 / (mid - magnet)

                if abs(totalforce) < 0.000001:
                    return mid
                elif totalforce < 0:
                    high = mid
                else:
                    low = mid

            return low  

        for i in range(n - 1):
            getAnswer[i] = neutral_point(a[i], a[i + 1])