class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True

        s1 = []
        s2 = []

        s1.append(root.left)
        s2.append(root.right)

        while s1 and s2:
            node1 = s1.pop()
            node2 = s2.pop()

            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None or node1.data != node2.data:
                return False

            s1.append(node1.left)
            s2.append(node2.right)

            s1.append(node1.right)
            s2.append(node2.left)

        return len(s1) == 0 and len(s2) == 0