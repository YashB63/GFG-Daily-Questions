class Solution:
    def dupSub(self, root):
        seen=set()
        _,_,found=dfs(root,seen)
        return +found
    
def dfs(n,seen):
    if not n: return '(#)',0,False
    lhash,lsz,lfound=dfs(n.left,seen)
    rhash,rsz,rfound=dfs(n.right,seen)
    h='('+str(n.data)+')'+lhash+rhash
    sz=1+lsz+rsz
    found=lfound or rfound or (h in seen and sz>=2)
    seen.add(h)
    return h,sz,found