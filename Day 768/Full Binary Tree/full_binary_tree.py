def isFullTree(root):
    if root.right and root.left:
        return isFullTree(root.left) and isFullTree(root.right)
    elif not(root.right or root.left):
        return True
    else:
        return False