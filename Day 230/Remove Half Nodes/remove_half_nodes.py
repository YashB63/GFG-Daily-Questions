class Solution:
    def RemoveHalfNodes(self, node):
        
        if node is None:
            return None
        
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)
        
        if node.right is None and node.left is not None:
            return node.left
            
        if node.left is None and node.right is not None:
            return node.right
        
        return node