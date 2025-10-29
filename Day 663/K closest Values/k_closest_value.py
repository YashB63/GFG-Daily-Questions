from collections import deque

class Solution:
    def getKClosest(self, root, target, k):
        def getInorder(node, x, k, kClosest):
            if not node:
                return

            getInorder(node.left, x, k, kClosest)

            if len(kClosest) < k:
                kClosest.append(node.data)
                
            elif abs(kClosest[0] - x) > abs(node.data - x):
                kClosest.popleft()
                kClosest.append(node.data)
            else:
                return

            getInorder(node.right, x, k, kClosest)

        dq = deque()
        getInorder(root, target, k, dq)

        ans = []
        while dq:
            ans.append(dq.popleft())

        return ans
