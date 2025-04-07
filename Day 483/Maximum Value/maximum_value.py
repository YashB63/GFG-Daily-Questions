from collections import deque

class Solution:
    def maximumValue(self,node):
        levelMax = {}
        queue = deque()
        queue.append((node,0))
        
        while queue:
            node,level = queue.popleft()
            if level in levelMax : 
                levelMax[level] = max(levelMax[level],node.data)
            else:
                levelMax[level]=node.data
            
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
            
        result = [levelMax[level] for level in sorted(levelMax)]
        return result