import math

def maxDiff(root):
    ans=[-math.inf]
    dfs(root,ans)
    return ans[0]

def dfs(n,ans):
    
    if not n: return math.inf
    if n.left==n.right: return n.data
    L=dfs(n.left,ans)
    R=dfs(n.right,ans)
    v=min(L,R)
    ans[0]=max(ans[0], n.data-v)
    return min(n.data, L, R)
