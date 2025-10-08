class BST:
    def search(self, node, x):
        if (node is None):
            return None
        if node.data == x:
            return True
        elif (node.data < x):
            return self.search(node.right, x)
        else:
            return self.search(node.left, x)