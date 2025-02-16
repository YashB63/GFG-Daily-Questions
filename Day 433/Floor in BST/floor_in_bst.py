def floor(root,x):
    if not root: return -1
    if root.data == x: return x
    
    if root.data > x:        
        return floor(root.left, x)
    
    candidate = floor(root.right, x)
    return candidate if candidate != -1 else root.data