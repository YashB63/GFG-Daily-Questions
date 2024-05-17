def merge(a,b):
    temp = Node(0)
    res = temp
    while a and b:
        if a.data < b.data:
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
        if a:
            temp.bottom = a
        else:
            temp.bottom = b
    return res.bottom
    
def flatten(root):
    
    if root is None or root.next is None:
        return root
    mergedroot = flatten(root.next)
    return merge(root,mergedroot)