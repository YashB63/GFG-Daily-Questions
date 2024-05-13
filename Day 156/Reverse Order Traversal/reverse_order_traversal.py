def reverseLevelOrder(root):
   
    ans=deque()
    q=deque()
    q.append(root)
    while q:
        node=q.popleft()
        ans.appendleft(node.data)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    return ans