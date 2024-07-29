class Solution:
    def merge(self, root1, root2):
        def dfs(node,l):
            if not node: return ''
            l.append(node.data)
            dfs(node.left,l)
            dfs(node.right,l)
        l = []
        dfs(root1,l)
        dfs(root2,l)
        l.sort()
        return l