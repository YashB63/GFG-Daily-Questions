class Solution:
    def isLeaf(self, node):
        if node is None:
            return False
        if node.left is None and node.right is None:
            return True
        return False

    def leftLeavesSum(self, root_node):
        if root_node is None:
            return 0

        ans = 0

        if self.isLeaf(root_node.left):
            ans += root_node.left.data
        else:
            ans += self.leftLeavesSum(root_node.left)

        ans += self.leftLeavesSum(root_node.right)

        return ans