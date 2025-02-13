class Solution:
    def buildTree(self, inorder, preorder):
        if(inorder==[] or preorder==[]):
            return None
        root=Node(preorder[0])
        stack=[root]
        inorder_index=0
        for i in range(1,len(preorder)):
            node=stack[-1]
            current=preorder[i]
            if(node.data!=inorder[inorder_index]):
                node.left=Node(current)
                stack.append(node.left)
            else:
                while(stack and stack[-1].data==inorder[inorder_index]):
                    node=stack.pop()
                    inorder_index+=1
                node.right=Node(current)
                stack.append(node.right)
        return root