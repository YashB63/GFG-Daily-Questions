class Solution:
    def getCount(self,root,n):
        q = [root]
        level = 1
        budget = n
        res = 0
        while q:
            l = len(q)
            for i in range(l):
                temp = q.pop(0)
                if not temp.left and not temp.right and budget-level >= 0:
                    res += 1
                    budget -= level
                if budget == 0:
                    q = []
                    break
                if temp.left:q.append(temp.left)
                if temp.right:q.append(temp.right)
            level += 1
        return res