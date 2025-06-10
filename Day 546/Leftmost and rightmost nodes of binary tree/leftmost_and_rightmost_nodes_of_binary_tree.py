def printCorner(root):
    if not root:
        return
    queue = [root]
    
    while queue:
        level_size = len(queue)
        
        leftmost = queue[0]
        rightmost = queue[-1]
        
        for _ in range(level_size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        print(leftmost.data, end=" ")
        if leftmost != rightmost:
            print(rightmost.data, end=" ")