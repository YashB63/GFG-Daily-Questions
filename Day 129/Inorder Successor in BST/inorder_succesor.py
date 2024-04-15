class Solution:
   
    def inorderSuccessor(self, root, x):
        
        result=None
        value=x.data
        pointer=root
        while pointer:
            if pointer.data<=value:
                pointer=pointer.right
            else: 
                result = pointer
                pointer=pointer.left
        return result