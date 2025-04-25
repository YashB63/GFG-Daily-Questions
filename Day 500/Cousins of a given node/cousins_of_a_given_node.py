class Solution:
    def printCousins(self, root, node):
        q=deque()
        q.append(root)
        exist=False
        if node==root:
            return [-1]
        while q:
            n=len(q)
            for _ in range(n):
                t=q.popleft()
                if t.left==node or t.right==node:
                    exist=True
                    continue
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            if exist:
                return [a.data for a in q] if q else [-1]
        return [-1]