class Solution:
    def convertToMaxHeapUtil(self, root):
        inorder = []
        def dfs(node):
            nonlocal inorder
            if node:
                dfs(node.left)
                inorder.append(node.data)
                dfs(node.right)
        dfs(root)
        
        def populatePostOrder(node):
            nonlocal ind
            nonlocal inorder
            if node:
                populatePostOrder(node.left)
                populatePostOrder(node.right)
                node.data = inorder[ind]
                ind += 1
        ind = 0
        populatePostOrder(root)
        return root