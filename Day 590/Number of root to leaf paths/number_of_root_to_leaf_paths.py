class Solution:
    def pathCountUtil(self, node, m, pl):
        if node is None:
            return

        if node.left is None and node.right is None:
            m[pl] = m.get(pl, 0) + 1
            return

        self.pathCountUtil(node.left, m, pl + 1)
        self.pathCountUtil(node.right, m, pl + 1)

    def pathCounts(self, root):
        if root is None:
            return

        m = {}

        self.pathCountUtil(root, m, 1)

        for path_length, count in sorted(m.items()):
            print("{} {} $".format(path_length, count), end="")