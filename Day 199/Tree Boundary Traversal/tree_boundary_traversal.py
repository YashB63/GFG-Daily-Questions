class Solution:
    def printBoundaryView(self, root):
        
        if not root:
            return []
        ans = []
        if root.left or root.right:
            ans.append(root.data)
        def leftboundary(root):
            curr = root.left
            while curr:
                if curr.left or curr.right:
                    ans.append(curr.data)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
            
        def rightboundary(root):
            node = root.right
            right = []
            while node:
                if node.left or node.right:
                    right.append(node.data)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            ans.extend(right[::-1])
            
        def findleaves(root):
            if not root:
                return
            if not root.left and not root.right:
                ans.append(root.data)
            findleaves(root.left)
            findleaves(root.right)
           
        leftboundary(root)
        findleaves(root)
        rightboundary(root)
        
        return ans