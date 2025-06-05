class Solution:
    def sumOfRootToLeaf(self, root, sum, length, maxLen, maxSum):
        if not root:

            if length > maxLen[0]:
                maxLen[0] = length
                maxSum[0] = sum

            elif length == maxLen[0] and sum > maxSum[0]:
                maxSum[0] = sum
            return

        self.sumOfRootToLeaf(root.left, sum + root.data, length + 1, maxLen,
                             maxSum)
        self.sumOfRootToLeaf(root.right, sum + root.data, length + 1, maxLen,
                             maxSum)

    def sumOfLongRootToLeafPath(self, root):
        if not root:
            return 0

        maxSum = [-float('inf')]
        maxLen = [0]

        self.sumOfRootToLeaf(root, 0, 0, maxLen, maxSum)

        return maxSum[0]