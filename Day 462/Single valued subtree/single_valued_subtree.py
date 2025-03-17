class Solution:
    def singlevalued(self, root):
        cnt = 0 
        def f(root):
            nonlocal cnt 
            if root is None:
               return True 
            l = f(root.left)
            r  = f(root.right)
            if l and r:
                if root.left and  root.right:
                    if root.data == root.left.data and root.data == root.right.data:
                       cnt += 1
                       return True
                    return False
                if root.left:
                    if root.data == root.left.data:
                          cnt += 1
                          return True
                    return False
                if root.right:
                    if root.data == root.right.data:
                          cnt += 1
                          return True
                    return False
                elif root.right is None and root.left is None:
                    cnt+=1 
                    return True
            return  False
        f(root)
        return cnt