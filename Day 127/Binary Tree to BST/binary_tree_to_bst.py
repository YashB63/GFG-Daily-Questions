class Solution:
    
    def level_order_traversal(self, root):
        queue, result, position, length = deque(), [], 0, 1
        queue.append(root)

        while position < length:
            current_node = queue[position]
            result.append(current_node.data)

            if current_node.left:
                queue.append(current_node.left)
                length += 1

            if current_node.right:
                queue.append(current_node.right)
                length += 1

            position += 1

        return sorted(result)
    
    def convert_to_bst(self, root, values):
        if root is None:
            return

        self.convert_to_bst(root.left, values)
        root.data = values.pop(0)
        self.convert_to_bst(root.right, values)
        
    def binaryTreeToBST(self, root):
        
        inorder_values = self.level_order_traversal(root)
        self.convert_to_bst(root, inorder_values)
        return root