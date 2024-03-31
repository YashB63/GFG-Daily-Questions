class Solution:
    
    def insert(self,root, Key):
        
        if root == None:
            return Node(key)
        if Key<root.data:
            if root.left == None:
                root.left = Node(Key)
            self.insert(root.left,Key)
        
        if Key>root.data:
            if root.right == None:
                root.right = Node(Key)
            self.insert(root.right,Key)