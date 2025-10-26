class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def constructTree(self, pre, post):
        post_index = {val: i for i, val in enumerate(post)}
        pre_ptr = [0]  

        def build(l, h):
            if pre_ptr[0] >= len(pre) or l > h:
                return None

            root = Node(pre[pre_ptr[0]])
            pre_ptr[0] += 1

            if l == h:
                return root

            i = post_index[pre[pre_ptr[0]]]
            if i <= h:
                root.left = build(l, i)
                root.right = build(i + 1, h - 1)
            return root

        return build(0, len(pre) - 1)