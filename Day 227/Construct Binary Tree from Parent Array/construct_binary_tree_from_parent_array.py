class Solution:
    def createTree(self,parent):
        n = len(parent)
        nodes = [Node(i) for i in range(n)]
        root = None
        
        for i in range(n):
            if parent[i] == -1:
                root = nodes[i]
            else:
                if nodes[parent[i]].left is None:
                    nodes[parent[i]].left = nodes[i]
                else:
                    nodes[parent[i]].right = nodes[i]
        
        return root