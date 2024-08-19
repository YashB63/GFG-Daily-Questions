def LCA(root, n1, n2):
    def traverse(node):
        if node is None: 
            return False 
        
        if n1 <= node.data <= n2: 
            return node
        
        elif n2 < node.data: 
            return traverse(node.left)
        
        else: return traverse(node.right)
        
    if n1 > n2: 
        n1, n2 = n2, n1
        
    return traverse(root)