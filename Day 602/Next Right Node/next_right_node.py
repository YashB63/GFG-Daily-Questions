from collections import deque

class Solution:
    def nextRight(self, root, key):
        if root == None:
            return 0
        
        qn = deque()  
        ql = deque()  
        
        level = 0  
        
        qn.append(root)  
        ql.append(level)  
        
        while (len(qn) > 0):  
            node = qn.popleft()  
            level = ql.popleft()  
            
            if (node.data == key):  
                if (len(ql) == 0 or ql[0] != level):  
                    ret = Node(-1)  
                    return ret
                return qn[0]  
            
            if (node.left != None):  
                qn.append(node.left)  
                ql.append(level+1)  
            
            if (node.right != None):  
                qn.append(node.right)  
                ql.append(level+1)  
        
        ret = Node(-1)  
        
        return ret  