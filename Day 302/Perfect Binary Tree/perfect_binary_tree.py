class Solution:
    def isPerfect(self,root):
        queue = [root]
        leaf_level = float("inf")
        level = 0
        while queue:
            level+=1
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)
                if not node.left and not node.right:
                    if leaf_level>level:
                        leaf_level = level
                    
                    elif leaf_level<level:
                        return False
                    continue
                        
                if not node.left or not node.right:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True
