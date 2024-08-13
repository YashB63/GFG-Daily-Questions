from collections import deque

def findSpiral(root):
    
    if root==None:
        return []
    res=[]
    q=deque([root])
    L=0
    while q:
        currentlevel=deque()
        size=len(q)
        
        for _ in range(size):
            node=q.popleft()
            if L%2==0:
                currentlevel.appendleft(node.data)
            else:
                currentlevel.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        res.extend(currentlevel)
        L+=1
    return res