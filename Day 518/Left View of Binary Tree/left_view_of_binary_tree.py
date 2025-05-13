class Solution:
    
    def recLeftView(self, root, level, result):
        if root is None:
            return

        if level == len(result):
            result.append(root.data)

        self.recLeftView(root.left, level + 1, result)
        self.recLeftView(root.right, level + 1, result)

    def LeftView(self, root):
        result = []
        self.recLeftView(root, 0, result)  
        return result