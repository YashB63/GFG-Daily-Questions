class Solution:

    def findMirror(self, root, target):
        if root is None:
            return -1
        if root.data == target:
            return target
        ans = self.findMirrorRec(root.left, root.right, target)
        return ans if ans != -1 else -1

    def findMirrorRec(self, left, right, target):
        if left is None or right is None:
            return -1

        if left.data == target:
            return right.data

        if right.data == target:
            return left.data

        mirror_val = self.findMirrorRec(left.left, right.right, target)
        if mirror_val != -1:
            return mirror_val

        return self.findMirrorRec(left.right, right.left, target)