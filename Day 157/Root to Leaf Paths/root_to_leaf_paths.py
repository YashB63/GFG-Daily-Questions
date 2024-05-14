from typing import Optional
from collections import deque

from typing import List


class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        
        def solve(root,ans,ds):
            if not root:
                return 
            if (root.left==None  and root.right==None):
                ds.append(root.data)
                ans.append(ds.copy())
                ds.pop()
                return
            ds.append(root.data)
            if root.left:
                solve(root.left,ans,ds)
            if root.right:
                solve(root.right,ans,ds)
            ds.pop() 
            return   
        ans=[]
        ds=[]    
        solve(root,ans,ds)
        return ans