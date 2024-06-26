class Solution:
    # Return the Kth smallest element in the given BST 
    def KthSmallestElement(self, root, K): 
        
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            
            K -= 1
            if K == 0:
                return cur.data
            
            cur = cur.right
            
        return -1