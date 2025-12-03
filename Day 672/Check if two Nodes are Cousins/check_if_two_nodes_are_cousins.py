class Solution:
    def isCousins(self, root, x, y):
        queue = deque([root])
        cousin = False  
        siblings = False  
        
        while queue and not cousin:
            q1 = deque()  
            while queue:
                n = queue.popleft()  

                if n is None:
                    siblings = False  
                else:
                    if n.data == x or n.data == y:  
                        if not cousin:
                            cousin = siblings = True  
                        else:
                            return not siblings  

                    q1.append(n.left)
                    q1.append(n.right)
                    q1.append(
                        None)  

            queue = q1  

        return False