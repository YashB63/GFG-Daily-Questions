def getHeight(n):
    if n is None:
        return 0
    return n.height

def getBalance(n):
    return getHeight(n.left) - getHeight(n.right)

def leftRotate(z): 
    
    y = z.right 
    T2 = y.left 
    
    y.left = z 
    z.right = T2 
    
    z.height = 1 + max(getHeight(z.left), getHeight(z.right)) 
    y.height = 1 + max(getHeight(y.left), getHeight(y.right)) 
    
    return y

def rightRotate(z): 
    
    y = z.left 
    T3 = y.right 
    
    y.right = z 
    z.left = T3 
    
    z.height = 1 + max(getHeight(z.left), getHeight(z.right)) 
    y.height = 1 + max(getHeight(y.left), getHeight(y.right)) 
    
    return y

def deleteNode(root, key):
    if root is None:
        return None
    
    if root.data > key:
        root.left = deleteNode(root.left, key)
    
    elif root.data < key:
        root.right = deleteNode(root.right, key)
    
    else:
        if root.left is None:
            return root.right
        
        if root.right is None:
            return root.left
        
        if root.right.left is None:
            root.right.left = root.left
            root = root.right
        
        else:
            parent = root.right
            nxt = parent.left
            while nxt.left:
                parent = nxt
                nxt = nxt.left
        
            parent.left = nxt.right
            nxt.right , nxt.left = root.right , root.left
            root = nxt
            
            root.right = deleteNode(root.right, key)
    
    balance = getBalance(root)
    
    if balance < -1:
        if getBalance(root.right) < 1:
            return leftRotate(root)
        
        root.right = rightRotate(root.right)
        return leftRotate(root)
    
    if balance > 1:
        if getBalance(root.left) > -1:
            return rightRotate(root)
        
        root.left = leftRotate(root.left)
        return rightRotate(root)
    
    root.height = 1 + max( getHeight(root.left) , getHeight(root.right) )
    return root