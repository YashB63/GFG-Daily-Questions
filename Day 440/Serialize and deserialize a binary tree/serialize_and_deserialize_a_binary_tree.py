class Solution:
    def serialize(self, root):
        ans = []
        def fun(root):
            if not root: return
            fun(root.left)
            ans.append(root.data)
            fun(root.right)
        fun(root)
        return ans
     
    def deSerialize(self, arr):
        for i in arr:
            print(i, end = ' ')