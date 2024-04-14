def findMedian(root):
    
    l=[]
    def inorder(root):
        if root:
            inorder(root.left)
            l.append(root.data)
            inorder(root.right)
    inorder(root)
    n=len(l)
    if n%2==0:
        a=n//2
        median = (l[a - 1] + l[a]) / 2
        if median.is_integer():
            median = int(median)
        return median
    else:
        a=n//2
        return l[a]