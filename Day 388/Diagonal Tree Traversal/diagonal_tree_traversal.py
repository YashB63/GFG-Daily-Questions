class Solution:
    def diagonal(self,root):
        def helper(root, slope, map):
            if not root:
                return
            if slope not in map:
                map[slope] = []
            map[slope].append(root.data)
            helper(root.left, slope + 1, map)
            helper(root.right, slope, map)
        
        if not root:
            return []
        map = {}
        helper(root, 0, map)
        res = []
        for slope in sorted(map):
            res.extend(map[slope])
        return res  