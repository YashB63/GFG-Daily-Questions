def reverseLevelOrder(root):
    
    if root:
        ans = []
        queue = []
        queue.append(root)
        while(len(queue)!=0):
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.right!= None:
                    queue.append(node.right)
                if node.left!= None:
                    queue.append(node.left)
                ans.insert(0, node.data)
        return ans
                
    else:
        return []