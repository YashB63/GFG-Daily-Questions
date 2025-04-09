class Solution:
    def duplicateSubtreeNaryTree(self, root):
        res = []
        hmap = {}

        def recurse(node):
            p = str(node.key) + "#"
            for child in node.children:
                p += recurse(child)

            if p not in hmap:
                hmap[p] = 0
            hmap[p] += 1
            return p

        recurse(root)

        ans = 0

        for val in hmap.values():
            if val > 1:
                ans += 1
        return ans