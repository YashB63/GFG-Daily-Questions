class Solution:
    def depthOfOddLeaf(self,root):
        res=rootlevel(root,1)
        return res
    
def rootlevel(root,level):        
    if root is None:
        return 0
    if root.left is None and root.right is None and  level%2!=0:
        return level
    h=rootlevel(root.left,level+1)
    l=rootlevel(root.right,level+1)
    return max(l,h) 