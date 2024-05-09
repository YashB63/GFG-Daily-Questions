class Solution:
    def KDistance(self,root,k):
    
        result = []
        def traverse(node, distance):
            if not node:
                return
            if distance == k:
                result.append(node.data)
            else:
                traverse(node.left, distance + 1)
                traverse(node.right, distance + 1)
        
        
        traverse(root, 0)
        
        return result