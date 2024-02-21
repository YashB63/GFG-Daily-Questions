def solve(root, level, res):
    if not root:
        return 
    if len(res) == level:
        res.append(root.data)
    solve(root.left, level+1, res)
    solve(root.right, level+1, res)
    
def LeftView(root):
    
    res = []
    solve(root, 0, res)
    return res