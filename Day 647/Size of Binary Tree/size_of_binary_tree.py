from typing import Optional
from collections import deque

class Solution:
    def getSize(self, node : Optional['Node']) -> int:
        if node is None:
            return 0
        else:
            return self.getSize(node.left) + 1 + self.getSize(node.right)