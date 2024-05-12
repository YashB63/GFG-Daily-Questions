def noSibling(root):

    l=[]
    def sibling(root):
        if root:
            if not root.left and root.right:
                l.append(root.right.data)
            elif root.left and not root.right:
                l.append(root.left.data)
            sibling(root.left)
            sibling(root.right)
    sibling(root)
    l.sort()
    
    if len(l) == 0:
        return [-1]
    return l