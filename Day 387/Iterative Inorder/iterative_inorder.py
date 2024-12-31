class Solution:
    def inOrder(self, root):
        stack = []
        curr = root
        ans = []
        while curr is not None or len(stack)>0:
            
            while curr is not None:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            ans.append(curr.data)
            curr  = curr.right
           
        return ans