class Solution:
    def leafNodes(self, preorder):
        s = []
        leaves = []
        n = len(preorder)

        for i in range(n - 1):
            found = False

            if preorder[i] > preorder[i + 1]:
                s.append(preorder[i])
            else:
                while s and preorder[i + 1] > s[-1]:
                    s.pop()
                    found = True

            if found:
                leaves.append(preorder[i])

        leaves.append(preorder[-1])

        return leaves