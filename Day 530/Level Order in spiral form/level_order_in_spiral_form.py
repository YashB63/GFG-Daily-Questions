class Solution:
    def findSpiral(self, root):
        res = []
        if not root:
            return res

        dq = deque([root])
        reverse = True

        while dq:
            n = len(dq)

            for _ in range(n):

                if reverse:
                    curr = dq.pop()
                    res.append(curr.data)

                    if curr.right:
                        dq.appendleft(curr.right)
                    if curr.left:
                        dq.appendleft(curr.left)
                else:
                    curr = dq.popleft()
                    res.append(curr.data)

                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)

            reverse = not reverse

        return res