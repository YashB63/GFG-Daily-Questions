class Solution:
    def isPairPresent(self,root, target): 
        def ino(root):
            if root is None:
                return []
            return ino(root.left)+[root.data]+ino(root.right)
        z=ino(root)
        l=0;r=len(z)-1
        while(l<r):
            
            if z[l]+z[r]==target:
                return 1
            elif z[l]+z[r]<target:
                l+=1
            else:
                r-=1
        return 0      