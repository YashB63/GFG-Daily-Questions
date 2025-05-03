class Solution:
    def c(self, r):
        return 1 + self.c(r.left) + self.c(r.right) if r else 0
    def p(self, r, i, n):
        return (not r) or (
            i < n
            and (not r.left  or r.data >= r.left.data)
            and (not r.right or r.data >= r.right.data)
            and self.p(r.left,  2*i+1, n)
            and self.p(r.right, 2*i+2, n)
        )
    def isHeap(self, root):
        return self.p(root, 0, self.c(root))