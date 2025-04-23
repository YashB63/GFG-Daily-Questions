from typing import Optional
from collections import deque

class Solution:
    def areAnagrams(self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:
        if(node1 is None and node2 is None):
            return 1
        elif(node1 is None or node2 is None):
            return 0
        
        q1 = [node1]
        q2 = [node2]
        
        while(len(q1)>0 and len(q2)>0):
            s1 = len(q1)
            s2 = len(q2)
            
            q1_arr = []
            q2_arr = []
            
            while(s1 > 0):
                node = q1.pop(0)
                q1_arr.append(node.data)
                
                if(node.left is not None):
                    q1.append(node.left)
                if(node.right is not None):
                    q1.append(node.right)
                
                s1 -= 1
            
            while(s2 > 0):
                node = q2.pop(0)
                q2_arr.append(node.data)
                
                if(node.left is not None):
                    q2.append(node.left)
                if(node.right is not None):
                    q2.append(node.right)
                
                s2 -= 1
            
            q1_arr.sort()
            q2_arr.sort()
            
            if(q1_arr != q2_arr):
                return False
        
        return True