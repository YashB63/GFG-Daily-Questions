class Solution:
    
    def check(self, root):
        
        leaf_levels = set()
        
        def traverse(node, level):
            if not node:
                return 
            if not node.left and not node.right:
                leaf_levels.add(level)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
            
        traverse(root, 0)
        
        return len(leaf_levels) == 1