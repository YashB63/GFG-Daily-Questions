from collections import deque

def verticalWidth(root):
    if not root:
        return 0
    ml,mx=float('inf'),float('-inf')
    q=deque([(root,0)])
    while q:
        for _ in range(len(q)):
            node,ht=q.popleft()
            ml=min(ml,ht)
            mx=max(mx,ht)
            if node.left:
                q.append((node.left,ht-1))
            if node.right:
                q.append((node.right,ht+1))
            
    return mx-ml+1