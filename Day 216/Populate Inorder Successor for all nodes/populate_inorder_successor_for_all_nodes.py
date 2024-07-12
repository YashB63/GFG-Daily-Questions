class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None

class Solution:

    def populateNext(self, root):
        self.last = None
        self.inorder_transversal(root)
        return root
    
    def inorder_transversal(self, node):

            
        if not self.last  and not node.left:
            self.last = node
            if node.right:
                self.inorder_transversal(node.right)    
            return
        
        if node.left:
            self.inorder_transversal(node.left)
            
        if self.last:
            self.last.next = node
            self.last = node
            
        if node.right:
            self.inorder_transversal(node.right)