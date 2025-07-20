class Solution:
    def findSmallestSubArr(self, arr, k):
        n = len(arr)
        st = self.constructST(arr)

        length = sys.maxsize

        for i in range(n):
            if arr[i] == k:
                return 1

        for i in range(n):
            end = self.endSearch(arr, st, i, n, k)
            if end != -1:
                length = min(length, end - i + 1)
        return length if length != sys.maxsize else -1

    def constructST(self, arr):
        n = len(arr)
        height = math.ceil(math.log2(n))
        size = 2 * (2**height) - 1
        st = [0] * size
        self.constructSegment(arr, 0, n - 1, st, 0)
        return st

    def constructSegment(self, arr, seg_start, seg_end, st, pos):
        if seg_start == seg_end:
            st[pos] = arr[seg_start]
            return st[pos]

        mid = (seg_start + seg_end) // 2
        st[pos] = gcd(
            self.constructSegment(arr, seg_start, mid, st, 2 * pos + 1),
            self.constructSegment(arr, mid + 1, seg_end, st, 2 * pos + 2))
        return st[pos]

    def endSearch(self, arr, st, i, n, k):
        start, end = i, n - 1
        ans = -1

        while start <= end:
            mid = (start + end) // 2
            gcd_value = self.queryGCD(st, 0, n - 1, i, mid, 0)
            if gcd_value == k:
                ans = mid
                end = mid - 1
            elif gcd_value % k == 0:
                start = mid + 1
            else:
                end = mid - 1

        return ans

    def queryGCD(self, st, seg_start, seg_end, query_start, query_end, pos):
        if seg_start > query_end or seg_end < query_start:
            return 0  
        if seg_start >= query_start and seg_end <= query_end:
            return st[pos]

        mid = (seg_start + seg_end) // 2
        return gcd(
            self.queryGCD(st, seg_start, mid, query_start, query_end,
                          2 * pos + 1),
            self.queryGCD(st, mid + 1, seg_end, query_start, query_end,
                          2 * pos + 2))