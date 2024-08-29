def LeftView(root):
    view=[]
    def LeftViewUtil(node,depth):
        if not node:
            return
        if depth == len(view):
            view.append(node.data)
        LeftViewUtil(node.left,depth+1)
        LeftViewUtil(node.right,depth+1)
        
    LeftViewUtil(root,0)
    return view