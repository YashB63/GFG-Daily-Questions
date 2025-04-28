class Solution:
    def convertToDLL(self, root):
        self.head = None
        self.tail = None
        
        def helper(root):
            if not root:
                return None
            
            if not root.left and not root.right:
                if not self.tail:
                    self.head = root
                    self.tail = root
                else:
                    self.tail.right = root
                    root.left = self.tail
                    self.tail = root
                
                return None
            
            root.left = helper(root.left)
            root.right = helper(root.right)
            return root
        
        temp = helper(root)
        return self.head