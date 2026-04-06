def summ(root, k):
    a=[]
    def dfs(root,a):
        if root is None:
            return None
        a.append(root.key)
        dfs(root.left,a)
        dfs(root.right,a)
    dfs(root,a)
    a.sort()
    f=sum(a[:k])
    return f