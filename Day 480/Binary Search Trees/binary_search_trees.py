class Solution:
    def isBSTTraversal(self, a):
        for i in range(1,len(a)):
            if a[i]<=a[i-1]: return False
        return True