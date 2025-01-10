class Solution:
    def postOrder(self,node):
        res = []
        st1 = [node]
        st2 = []
        
        while st1:
            val = st1.pop()
            st2.append(val.data)
            
            if val.left:
                st1.append(val.left)
                
            if val.right:
                st1.append(val.right)
                
        while st2:
            value = st2.pop()
            res.append(value)
        return res