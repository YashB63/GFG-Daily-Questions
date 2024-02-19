class Solution:
    
    def isBST(self, root):
        
        stack = []
        arr = []
        if root == None:
            return
        
        current = root
        while (True):
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                arr.append(current.data)
                current = current.right
            else:
                break
            
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True