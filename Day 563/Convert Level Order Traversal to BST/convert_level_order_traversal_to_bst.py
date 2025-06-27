def constructBst(a,n):
    if n>0:
        root=Node(a[0])
    else:
        return None
    
    for i in range(1,n):
        insert(root,a,n,i)
        
    return root

def insert(root,a,n,i):
    if root.data>a[i]:
        if root.left:
            insert(root.left,a,n,i)
        else:
            root.left=Node(a[i])
            
    if root.data<a[i]:
        if root.right:
            insert(root.right,a,n,i)
        else:
            root.right=Node(a[i])