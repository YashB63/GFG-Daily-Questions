from collections import deque

class Solution:
    def extremeNodes(self, root):
        level = 0
        result = []
        queue = deque()
        
        queue.append(root)
        
        while queue:
            size = len(queue)
            if level % 2 == 0:
                result.append(queue[-1].data)
            else:
                result.append(queue[0].data)
            while size:
                curr = queue.popleft()
                size -= 1
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
                    
        return result