class Solution:
    def maxDepth(self, n):
        if n is None:
            return 0
        return 1 + max((self.maxDepth(n.left), self.maxDepth(n.right)))

    def traverse(self, n, target):
        if n is None:
            return (0, 0)

        if n.data == target:
            ans = self.maxDepth(n.right)
            ans = max(ans, self.maxDepth(n.left))
            return (ans, 1)

        ans, dist = self.traverse(n.left, target)
        if dist:
            ans = max(ans, dist + self.maxDepth(n.right))
            return (ans, dist + 1)

        ans, dist = self.traverse(n.right, target)
        if dist:
            ans = max(ans, dist + self.maxDepth(n.left))
            return (ans, dist + 1)

        return (0, 0)

    def minTime(self, root, target):
        return (self.traverse(root, target))[0]