class Solution:
    def findPreSuc(self, root, pre, suc, key):
       
        cur = root
        
        while cur:
            if cur.key <= key:
                cur = cur.right
            else:
                suc.key = cur.key
                cur = cur.left
            
        cur = root
        while cur:
            if cur.key >= key:
                cur = cur.left
            else:
                pre.key = cur.key
                cur = cur.right