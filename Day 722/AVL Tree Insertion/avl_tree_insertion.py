class Solution:
    def height(self,node):
        if node:
            return node.height
        return 0
    def leftrotate(self,root):
        temp = root.right
        temp2 = temp.left
        temp.left =root
        root.right = temp2
        root.height = 1 + max(self.height(root.left),self.height(root.right))
        temp.height = 1 + max(self.height(temp.left),self.height(temp.right))
        
        return temp
        
    def rightrotate(self,root):
        temp = root.left
        temp2 = temp.right
        temp.right =root
        root.left = temp2
        
        root.height = 1 + max(self.height(root.left),self.height(root.right))
        temp.height = 1 + max(self.height(temp.left),self.height(temp.right))
        
        return temp
        
    def insertToAVL(self, node, key):
        if not node:
            return Node(key)
        if node.data<key:
            node.right =  self.insertToAVL(node.right,key)
        else:
            node.left =  self.insertToAVL(node.left,key)
        
        node.height = 1+max(self.height(node.left),self.height(node.right))
        diff = self.height(node.left)-self.height(node.right)
        if diff<-1 and key>node.right.data:
            return self.leftrotate(node)
        elif diff>1 and key<node.left.data:
            return self.rightrotate(node)
        elif diff<-1 and key<node.right.data:
            node.right = self.rightrotate(node.right)
            return self.leftrotate(node)
        elif diff>1 and key>node.left.data:
            node.left = self.leftrotate(node.left)
            return self.rightrotate(node)
        return node