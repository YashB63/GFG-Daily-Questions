class Solution:
    def getLastMoment(self, n, left, right):
        max_left = max(left) if left else 0
        max_right = max(n - r for r in right) if right else 0
        return max(max_left, max_right)