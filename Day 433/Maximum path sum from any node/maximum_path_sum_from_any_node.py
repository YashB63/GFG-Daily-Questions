from collections import deque

class Solution:
    def findMaxSum(self, root): 
        max_sum=float('-inf')
        def Sum(root):
            nonlocal max_sum
            if not root:
                return 0
            l=Sum(root.left)
            r=Sum(root.right)
            max_side=max(l+root.data,r+root.data)
            all_sum=max((l+r+root.data),root.data)
            max_sum=max(max_sum,max(all_sum,max_side))
                
            return max(root.data,max_side)
        Sum(root)
        return max_sum