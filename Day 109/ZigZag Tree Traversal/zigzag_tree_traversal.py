class Solution:
    
    def zigZagTraversal(self, root):
        
        ans=[]
        d=deque()
        d.append(root)
        ltr=True
        while d:
            n=len(d)
            for _ in range(n):
                if ltr:
                    item=d.popleft()
                else:
                    item=d.pop()
                ans.append(item.data)
                if ltr:
                    if item.left:
                        d.append(item.left)
                    if item.right:
                        d.append(item.right)
                else:
                    if item.right:
                        d.appendleft(item.right)
                    if item.left:
                        d.appendleft(item.left)
            ltr= not ltr
        return ans