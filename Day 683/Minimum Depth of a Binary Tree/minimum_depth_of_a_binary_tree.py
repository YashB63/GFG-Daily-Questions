class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        q=[root]
        count=0
        while q:
            p=len(q)
            count+=1
            for i in range(p):
                node=q.pop(0)
                a=0
                if node.left:
                    q.append(node.left)
                    a+=1
                if node.right:
                    q.append(node.right)
                    a+=1
                if a==0:
                    return count
        return count