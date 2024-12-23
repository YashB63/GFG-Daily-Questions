class Solution:

    def kthElement(self, a, b, k):
        if len(a) > len(b):
            return self.kthElement(b, a, k)

        n, m = len(a), len(b)
        low, high = max(0, k - m), min(k, n)

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1

            l1 = a[cut1 - 1] if cut1 > 0 else float('-inf')
            l2 = b[cut2 - 1] if cut2 > 0 else float('-inf')
            r1 = a[cut1] if cut1 < n else float('inf')
            r2 = b[cut2] if cut2 < m else float('inf')

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return -1
