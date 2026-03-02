class Solution:
    def preOrder(self, root):
        ans = []
        stk = [root]
        while stk:
            item = stk.pop()
            ans.append(item.data)
            if item.right:
                stk.append(item.right)
            if item.left:
                stk.append(item.left)
        return ans