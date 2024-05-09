def solve(root,ans):
    if(root):
        solve(root.left,ans)
        solve(root.right,ans)
        if(root.left is None and root.right is None):
            ans[0]+=root.data
def sumLeaf(root):
    ans=[0]
    solve(root,ans)
    return ans[0]