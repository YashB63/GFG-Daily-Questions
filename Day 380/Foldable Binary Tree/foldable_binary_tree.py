def IsFoldable(root):
    
    if root == None:
        return True
    
    ans = foldable(root.left, root.right)
    return ans

def foldable(root1, root2):
    if root1==None and root2==None:
        return True
    if root1==None or root2==None:
        return False
    
    return foldable(root1.left, root2.right) and foldable(root1.right, root2.left)