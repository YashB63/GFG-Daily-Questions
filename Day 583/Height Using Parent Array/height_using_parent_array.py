class Solution:
    def fillDepth(parent, i, depth):
        if depth[i] != 0:
            return
        if parent[i] == -1:
            depth[i] = 1
            return
        if depth[parent[i]] == 0:
            Solution.fillDepth(parent, parent[i], depth)
        depth[i] = depth[parent[i]] + 1

   
    def findHeight(self, n, arr):
        depth = [0] * n
        for i in range(n):
            Solution.fillDepth(arr, i, depth)
        ht = depth[0]
        for i in range(1, n):
            if ht < depth[i]:
                ht = depth[i]
        return ht