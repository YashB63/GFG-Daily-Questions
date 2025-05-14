from typing import Optional
from collections import deque
from typing import List

class Solution:
    def collectPaths(self, node, path, paths):
        if node is None:
            return

        path.append(node.data)

        if node.left is None and node.right is None:
            paths.append(list(path))
        else:
            self.collectPaths(node.left, path, paths)
            self.collectPaths(node.right, path, paths)

        path.pop()

    def Paths(self, root):  
        paths = []
        path = []
        self.collectPaths(root, path, paths)  
        return paths