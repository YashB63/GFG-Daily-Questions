class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)
        maxEle = 0
        for ele in arr:
            maxEle = max(maxEle, ele)

        vis = [False] * (maxEle + 1)

        for ele in arr:
            vis[ele] = True

        for a in range(1, maxEle + 1):
            if not vis[a]:
                continue

            for b in range(1, maxEle + 1):
                if not vis[b]:
                    continue

                c = int(math.sqrt(a * a + b * b))

                if (c * c) != (a * a + b * b) or c > maxEle:
                    continue

                if vis[c]:
                    return True

        return False