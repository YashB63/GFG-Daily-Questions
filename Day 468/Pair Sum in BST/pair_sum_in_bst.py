def inorder(root, x, s):
    if root is None:
        return False
    
    if inorder(root.left, x, s):
        return True
    
    if x - root.key in s:
        return True
    
    else:
        s.add(root.key)
    
    return inorder(root.right, x, s)
    
def findPair(root,X):   
    s = set()
    return inorder(root, X, s)