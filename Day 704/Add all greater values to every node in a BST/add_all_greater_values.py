def modify(root):
    def m(root, running_sum=0):  
        if root is None:
            return running_sum  

        running_sum = m(root.right, running_sum)  
        root.data += running_sum  
        return m(root.left, root.data)  
    m(root)  
    return root