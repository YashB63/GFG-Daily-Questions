class Solution:
    
    def findCommon(self, r1, r2):
        s = set()
        ans = []
        
        def dfs(root, flag):
            if not root:
                return
            
            if not flag:
                s.add(root.data)
            

            dfs(root.left, flag)
            
            if flag and root.data in s:
                ans.append(root.data)
                
            dfs(root.right, flag)
        
        dfs(r1, False)
        dfs(r2, True)
        return ans