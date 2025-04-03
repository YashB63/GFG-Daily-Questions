from typing import Optional
from collections import deque

class Solution:
    def findLargestSubtreeSum(self, root : Optional['Node']) -> int:
        def dfs(root):
            if not root:
                return 0
            nonlocal s
            l,r = dfs(root.left),dfs(root.right)
            s = max(s, l+r+root.data)
            return l+r+root.data
        s = -10**8
        dfs(root)
        return s