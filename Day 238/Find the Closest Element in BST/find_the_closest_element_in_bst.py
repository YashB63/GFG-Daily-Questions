class Solution:

    def minDiff(self,root, K):
        cur = root
        res1, res2 = float("inf"), float("inf")
        while cur:
            if cur.data == K:
                return 0
            elif cur.data > K:
                res1 = cur.data
                cur = cur.left
            else:
                res2 = cur.data
                cur = cur.right
        return abs(res1 - K) if abs(res1 - K) < abs(res2 - K) else abs(res2 - K)
