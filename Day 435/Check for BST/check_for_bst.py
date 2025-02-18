class Solution:
    def isBST(self, root):
        pre, stack = None, []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return True
            node = stack.pop()
            if pre and pre.data >= node.data:
                return False
            pre = node
            root = node.right