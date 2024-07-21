class Solution:
    def isHeap(self, root):
        pri=-1
        q=[(root,0)]
        while q:
            n,ni=q.pop(0)
            if ni>pri+1:
                return 0
            if n.left:
                if n.left.data>n.data:
                    return 0
                else:
                    q.append((n.left,2*ni+1))
            if n.right:
                if n.right.data>n.data:
                    return 0
                else:
                    q.append((n.right,2*ni+2))
            pri=ni
        return 1