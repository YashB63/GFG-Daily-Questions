class Solution:
    def inversionCount(self, arr):
        m = max(arr)
        tree = [0]*(m+1)
        
        def update(tree, i, v):
            while i < len(tree):
                tree[i] += v
                i += i&-i
        
        def query(tree, i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i&-i 
            return s
        
        ans = 0
        for i in range(len(arr)-1, -1, -1):
            ans += query(tree, arr[i]-1)
            update(tree, arr[i], 1)
        
        return ans