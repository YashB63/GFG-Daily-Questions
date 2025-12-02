class Solution:
    def maxBalls(self, n: int, m: int, a: list[int], b: list[int]) -> int:
        asum, bsum = 0, 0
        i, j = 0, 0

        while i < n and j < m:
            if a[i] == b[j]:
                sa, sb = 0, 0
                ia, jb = i, j

                while i + 1 < n and a[i] == a[i + 1]:
                    sa += a[i]
                    i += 1

                while j + 1 < m and b[j] == b[j + 1]:
                    sb += b[j]
                    j += 1

                ea = i - ia + 1
                eb = j - jb + 1

                e1 = asum + sa + a[i]
                if ea > 1 and eb > 1:
                    e1 = max(e1, asum + ea * a[i] + eb * a[i] - 2 * a[i])
                e1 = max(e1, bsum + ea * a[i] + eb * a[i] - a[i])

                e2 = bsum + sb + a[i]
                if ea > 1 and eb > 1:
                    e2 = max(e2, bsum + ea * a[i] + eb * a[i] - 2 * a[i])
                e2 = max(e2, asum + ea * a[i] + eb * a[i] - a[i])

                asum, bsum = e1, e2
                i += 1
                j += 1

            elif a[i] < b[j]:
                asum += a[i]
                i += 1
            else:
                bsum += b[j]
                j += 1

        while i < n:
            asum += a[i]
            i += 1
        while j < m:
            bsum += b[j]
            j += 1

        return max(asum, bsum)