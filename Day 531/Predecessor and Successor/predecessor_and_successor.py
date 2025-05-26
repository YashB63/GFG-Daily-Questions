class Solution:
    def rightMost(self, node):
        while node.right is not None:
            node = node.right
        return node

    def leftMost(self, node):
        while node.left is not None:
            node = node.left
        return node

    def findPreSuc(self, root, key):
        pre = None
        suc = None
        curr = root

        while curr is not None:
            if curr.data < key:
                pre = curr
                curr = curr.right
            elif curr.data > key:
                suc = curr
                curr = curr.left
            else:
                if curr.left is not None:
                    pre = self.rightMost(curr.left)
                if curr.right is not None:
                    suc = self.leftMost(curr.right)
                break

        return [pre, suc]