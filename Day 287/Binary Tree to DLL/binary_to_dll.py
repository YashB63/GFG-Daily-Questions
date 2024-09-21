class Solution:
    def bToDLL(self,root):
        if not root:
            return None
        
        def rec(root):
            if not root:
                return 
            
            nonlocal head
            rec(root.left)
            
            head.right = Node(root.data)
            head.right.left = head
            head = head.right
            
            rec(root.right)
        
        temp = Node(-1)
        head = temp
        rec(root)
        head = temp.right
        head.left = None
            
        return head