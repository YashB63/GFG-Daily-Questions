def pre(root,ans):
    if root==None:
        return
    if root.right!=None and root.right.left==None and root.right.right==None:
        ans[0]+=root.right.data
    pre(root.left,ans)
    pre(root.right,ans)
    
class Solution:
    def rightLeafSum(self,root):
        a=[0]
        pre(root,a)
        return a[0]