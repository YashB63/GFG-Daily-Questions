class Solution:
    def bottomView(self, root):
        if root is None:
            return []

        hash = {}

        minHD = 0
        maxHD = 0

        q = deque()

        q.append([root, 0])

        while q:
            top = q.popleft()

            node = top[0]
            hd = top[1]

            hash[hd] = node.data

            minHD = min(minHD, hd)
            maxHD = max(maxHD, hd)

            if node.left is not None:
                q.append([node.left, hd - 1])

            if node.right is not None:
                q.append([node.right, hd + 1])

        ans = []
        for i in range(minHD, maxHD + 1):
            ans.append(hash[i])

        return ans