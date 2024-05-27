class Solution:
    
    def largestBst(self, root):
        
        int_min = -sys.maxsize - 1
        int_max = sys.maxsize
        ans = 0
        
        def dfs(root):
            nonlocal ans,int_min,int_max
            if not root:
                return [1,int_min,int_max,0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            isBST = left[0]==1 and right[0]==1 and root.data>left[1] and root.data<right[2]

            if isBST:
                ans = max(ans , 1+ left[3] +right[3])
                return [isBST,max(root.data,right[1]),min(root.data,left[2]),1+left[3]+right[3]]
            else:
                return [isBST,root.data,root.data,1]
        
        dfs(root)
        
        return ans