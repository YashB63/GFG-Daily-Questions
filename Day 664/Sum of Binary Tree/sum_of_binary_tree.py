class Solution:
    def sumBT(self, root):
        if root is None:
            return 0

        stack = [root]
        total_sum = 0

        while stack:
            node = stack.pop()
            total_sum += node.data

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return total_sum