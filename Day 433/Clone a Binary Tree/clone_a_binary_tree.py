class Solution:
    def cloneTree(self, root):
        head=Node(root.data)
        pair=dict()
        pair[root]=head
        def fun(root,head):
            if root.left!=None:
                head.left=Node(root.left.data)
                pair[root.left]=head.left
                fun(root.left,head.left)
            if root.right!=None:
                head.right=Node(root.right.data)
                pair[root.right]=head.right
                fun(root.right,head.right)
        fun(root,head)
        
        for key in pair:
            if key.random!=None:
                pair[key].random=pair[key.random]
        return head
