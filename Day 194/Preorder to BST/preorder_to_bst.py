class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def Bst(pre, size) -> Node:
    
    i = [0]
    A = pre
    def build(A,i,bound):
        if i[0] == len(A) or A[i[0]]>bound:
            return None
        root = Node(A[i[0]])
        i[0]=i[0]+1
        root.left = build(A,i,root.data)
        root.right = build(A,i,bound)
        return root
    return build(A,i,float('inf'))
