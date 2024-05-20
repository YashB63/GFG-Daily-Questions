class Solution:
    def isSubTree(self, T, S):
        
        if T is None and S is None:
            return True
        if T is None or S is None:
            return False
            
        def checker(root1,root2):
            if root1==None and root2==None:
                return True
            if root1==None or root2==None:
                return False
            if root1.data!=root2.data:
                return False
            leftside = checker(root1.left,root2.left)
            rightside = checker(root1.right,root2.right)
            return leftside and rightside
        
        def helper(T,S):
            if T is None:
                return
            if T.data == S.data:
                if checker(T,S):
                    return True
            left = helper(T.left,S)
            right = helper(T.right,S)
            return left or right
        return helper(T,S)