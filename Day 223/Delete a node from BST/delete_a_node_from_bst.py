def deleteNode(root, X):
    
    if not root:
        return None

    if X < root.data:
        root.left = deleteNode(root.left, X)
    elif X > root.data:
        root.right = deleteNode(root.right, X)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
            
        if root.right.left:
            temp = root.right.left
        else:
            temp = root.right
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root