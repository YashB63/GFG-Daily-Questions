class Solution:
    
    def buildBalancedTree(self,root):
        def sorting(arr,low,high):
            if low>high:
                return None
            mid=(low+high)//2
            node=Node(arr[mid])
            node.left=sorting(arr,low,mid-1)
            node.right=sorting(arr,mid+1,high)
            return node
            
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.data)
            inorder(root.right)
        res=[]
        inorder(root)
        return sorting(res,0,len(res)-1)