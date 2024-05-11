class Solution:
    
    def verticalSum(self, root):
        
        mapp = {}
        def dfs(node, pos):
            if not node:
                return
            dfs(node.left,pos-1)
            mapp[pos] = mapp.get(pos, 0)+node.data
            dfs(node.right,pos+1)
        dfs(root,0)
        arr = []
        for key, val in mapp.items():
            arr.append([key,val])
        arr.sort()
        return [val for i, val in arr]